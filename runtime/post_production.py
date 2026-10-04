"""Campaign-essay preparation, human handoffs, and static validation.

This is a small set of role-specific executors used by the existing runtime DAG.
It is not an additional scheduler, model client, or browser automation layer.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
from datetime import date, datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

from runtime.models import ExecutionResult, JobContext, WaitingForHuman

POST_IDS = tuple(f"POST-{index:02d}" for index in range(1, 6))


class PostValidationError(ValueError):
    """The model response cannot be safely treated as a public Jekyll post."""


def _write_once(path: Path, text: str) -> None:
    """Persist an immutable file; an identical retry is allowed, replacement is not."""
    path.parent.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8")
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    except FileExistsError:
        if path.read_bytes() == data:
            return
        raise RuntimeError(f"immutable post-production artifact changed on retry: {path}")
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except Exception:
        path.unlink(missing_ok=True)
        raise


def _post_id_from_job(job_id: str) -> str | None:
    match = re.search(r"post[-_ ]?(0[1-5])", job_id, re.IGNORECASE)
    return f"POST-{match.group(1)}" if match else None


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def _packet_metadata(packet: str) -> dict[str, Any]:
    match = re.search(
        r"<!-- POST_PRODUCTION_VALIDATOR_METADATA\s*(\{.*?\})\s*-->\s*$",
        packet,
        re.DOTALL,
    )
    if not match:
        raise PostValidationError("compiler validator metadata is missing from the evidence packet")
    try:
        value = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise PostValidationError("compiler validator metadata is not valid JSON") from exc
    if not isinstance(value, dict):
        raise PostValidationError("compiler validator metadata must be a JSON object")
    return value


def _extract_numbers(text: str) -> set[str]:
    """Return normalized numeric literals, ignoring internal IDs and URLs."""
    text = re.sub(r"https?://[^\s)\]>]+", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"\bPOST-0[1-5]\b|\bF-\d{2,}\b|\bC-\d{2,}\b", " ", text)
    values: set[str] = set()
    pattern = re.compile(r"(?<![A-Za-z0-9_])\d{1,3}(?:,\d{3})*(?:\.\d+)?%?(?![A-Za-z0-9_])")
    for match in pattern.finditer(text):
        token = match.group(0)
        normalized = token.replace(",", "")
        values.add(normalized)
        if normalized.endswith("%"):
            values.add(normalized[:-1])
    return values


def _strip_markdown_for_checks(text: str) -> str:
    text = re.sub(r"(?ms)^---\s*\n.*?\n---\s*\n", " ", text, count=1)
    text = re.sub(r"(?s)```.*?```|~~~.*?~~~", " ", text)
    text = re.sub(r"(?s)\$\$.*?\$\$|(?<!\\)\$[^$\n]+\$", " ", text)
    text = re.sub(r"!?(\[[^\]]*\])\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"`[^`]*`", " ", text)
    return text


def _word_count(text: str) -> int:
    plain = _strip_markdown_for_checks(text)
    return len(re.findall(r"\b[\w’'-]+\b", plain, flags=re.UNICODE))


_NUMBER_WORDS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,
    "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
    "ninety": 90,
}
_QUANTITATIVE_NOUNS = (
    "cases?|episodes?|results?|environments?|posts?|runs?|seeds?|replicates?|rows?|"
    "passes?|fails?|points?|percent(?:age)?|attempts?|tokens?|calls?|requests?|"
    "omissions?|items?|judges?|conditions?|classes?|controls?|axes|steps?|levels?|"
    "examples?|checks?|dimensions?|days?|years?|times?|minutes?|seconds?|hours?|"
    "links?|families|tasks?|cells?|scores?|failures?|transients?"
)


def _number_word_value(phrase: str) -> int | None:
    words = re.split(r"[- ]+", phrase.lower())
    total = 0
    current = 0
    for word in words:
        if word in _NUMBER_WORDS:
            value = _NUMBER_WORDS[word]
            if value >= 20:
                current = value
            else:
                current += value
        elif word == "hundred" and current:
            current *= 100
        elif word in {"thousand", "million"} and current:
            total += current * (1000 if word == "thousand" else 1_000_000)
            current = 0
        else:
            return None
    return total + current if words else None


def _extract_quantitative_word_tokens(text: str) -> set[str]:
    noun_pattern = re.compile(rf"\b({_QUANTITATIVE_NOUNS})\b", re.IGNORECASE)
    words = "|".join(sorted(_NUMBER_WORDS, key=len, reverse=True))
    phrase_pattern = re.compile(rf"\b({words})(?:[- ](?:{words}))?\s+(?={_QUANTITATIVE_NOUNS}\b)", re.IGNORECASE)
    values: set[str] = set()
    for match in phrase_pattern.finditer(text):
        value = _number_word_value(match.group(1))
        if value is not None and noun_pattern.search(text[match.end() : match.end() + 40]):
            values.add(str(value))
    return values


def _extract_trace_rows(packet: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for match in re.finditer(
        r"## BEGIN INPUT ARTIFACT: ([^\n]*trace_rows[^\n]*)\n(.*?)\n## END INPUT ARTIFACT:",
        packet,
        re.DOTALL,
    ):
        section = match.group(2)
        lines = section.splitlines()
        header_index = next((i for i, line in enumerate(lines) if line.startswith("post_id,claim_id,")), None)
        if header_index is None:
            continue
        try:
            rows.extend(csv.DictReader(io.StringIO("\n".join(lines[header_index:]))))
        except csv.Error:
            continue
    return rows


def _extract_finding_rows(packet: str) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    pattern = re.compile(
        r"## BEGIN INPUT ARTIFACT: ([^\n]*relevant_findings[^\n]*)\n(.*?)\n## END INPUT ARTIFACT:",
        re.DOTALL,
    )
    for match in pattern.finditer(packet):
        lines = match.group(2).splitlines()
        content_index = next((i + 1 for i, line in enumerate(lines) if not line.strip()), len(lines))
        content = "\n".join(lines[content_index:]).strip()
        try:
            payload = json.loads(content)
        except json.JSONDecodeError:
            continue
        rows = payload.get("findings", []) if isinstance(payload, dict) else []
        if isinstance(rows, list):
            findings.extend(row for row in rows if isinstance(row, dict) and row.get("id"))
    return findings


def _extract_failure_detail_rows(packet: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    pattern = re.compile(
        r"## BEGIN INPUT ARTIFACT: ([^\n]*failure_details[^\n]*)\n(.*?)\n## END INPUT ARTIFACT:",
        re.DOTALL,
    )
    for match in pattern.finditer(packet):
        lines = match.group(2).splitlines()
        header_index = next(
            (i for i, line in enumerate(lines) if line.startswith("environment,condition,judge,score,failure,detail")),
            None,
        )
        if header_index is None:
            continue
        try:
            rows.extend(csv.DictReader(io.StringIO("\n".join(lines[header_index:]))))
        except csv.Error:
            continue
    return rows


def _audit_numeric_claim_traceability(
    body: str,
    trace_rows: list[dict[str, str]],
    finding_rows: list[dict[str, Any]] | None = None,
    failure_rows: list[dict[str, str]] | None = None,
) -> dict[str, Any]:
    """Map each numeric sentence through its claim row to the cited finding records."""
    finding_by_id = {
        str(row.get("id")): row
        for row in (finding_rows or [])
        if isinstance(row, dict) and row.get("id")
    }
    case_evidence_by_claim = {
        "POST-01-C03": {"regex_state_machine"},
        "POST-01-C04": {"css_state_machine", "sql_fixed_point"},
        "POST-01-C05": {"moco", "rd_adaptive_halting"},
    }
    case_rows = failure_rows or []
    clean = _strip_markdown_for_checks(body)
    sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+|\n+", clean) if part.strip()]
    mapped: list[dict[str, Any]] = []
    unmapped: list[str] = []
    for sentence in sentences:
        numeric = _extract_numbers(sentence) | _extract_quantitative_word_tokens(sentence)
        if not numeric:
            continue
        candidates: list[dict[str, Any]] = []
        for row in trace_rows:
            finding_ids = re.findall(r"\bF-\d{2,}\b", str(row.get("finding_ids", "")))
            source_parts = [
                str(row.get("claim_summary", "")),
                str(row.get("external_references", "")),
            ]
            for finding_id in finding_ids:
                finding = finding_by_id.get(finding_id, {})
                source_parts.extend(
                    str(finding.get(key, ""))
                    for key in ("claim", "quantitative_result", "limitations", "alternatives")
                )
            claim_id = str(row.get("claim_id", ""))
            related_environments = case_evidence_by_claim.get(claim_id, set())
            for case_row in case_rows:
                if case_row.get("environment") in related_environments:
                    source_parts.extend(
                        str(case_row.get(key, ""))
                        for key in ("condition", "judge", "score", "failure", "detail")
                    )
            source_text = " ".join(source_parts)
            source_numbers = _extract_numbers(source_text) | _extract_quantitative_word_tokens(source_text)
            overlap = sorted(numeric & source_numbers)
            if overlap:
                candidates.append(
                    {
                        "claim_id": row.get("claim_id"),
                        "finding_ids": row.get("finding_ids", ""),
                        "matched_numbers": overlap,
                    }
                )
        # A literal present somewhere in the packet is not enough: every sentence
        # with a number also needs a claim row whose finding records support it.
        if candidates:
            mapped.append({"sentence": sentence, "numbers": sorted(numeric), "candidate_trace_rows": candidates})
        else:
            unmapped.append(sentence)
    return {"mapped_numeric_claim_sentences": mapped, "unmapped_numeric_claim_sentences": unmapped}


def _slugify(title: str) -> str:
    value = title.lower().replace("’", "").replace("'", "")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def _extract_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.DOTALL)
    if not match:
        raise PostValidationError("missing YAML frontmatter delimited by ---")
    try:
        metadata = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise PostValidationError(f"frontmatter is invalid YAML: {exc}") from exc
    if not isinstance(metadata, dict):
        raise PostValidationError("frontmatter must be a YAML mapping")
    return metadata, text[match.end() :]


def _balanced_fences(body: str) -> list[str]:
    problems: list[str] = []
    for marker in ("```", "~~~"):
        count = sum(1 for line in body.splitlines() if line.lstrip().startswith(marker))
        if count % 2:
            problems.append(f"unclosed Markdown {marker} code fence")
    return problems


def _validate_links(body: str) -> list[str]:
    problems: list[str] = []
    code_masked = re.sub(r"(?ms)```.*?```|~~~.*?~~~|`[^`]*`", " ", body)
    for match in re.finditer(r"(?<!!)\[[^\]\n]+\]\(([^)\s]+)(?:\s+[^)]*)?\)", code_masked):
        target = match.group(1).strip("<>")
        if target.startswith(("#", "/", "{{", "mailto:")):
            if "{{" in target and "}}" not in target:
                problems.append(f"unresolved link target: {target}")
            continue
        parsed = urlparse(target)
        if parsed.scheme not in {"https", "http"} or not parsed.netloc:
            problems.append(f"external link is not a valid absolute URL: {target}")
        if any(char.isspace() for char in target):
            problems.append(f"link target contains whitespace: {target}")
    for match in re.finditer(r"\b(?:href|src)\s*=\s*([\"'])(.*?)\1", code_masked, re.IGNORECASE):
        target = match.group(2).strip()
        if not target or any(char.isspace() for char in target):
            problems.append(f"HTML link/resource target is empty or contains whitespace: {target!r}")
            continue
        if target.startswith(("#", "/", "{{")):
            if "{{" in target and "}}" not in target:
                problems.append(f"unclosed Jekyll expression in HTML link/resource: {target}")
            continue
        parsed = urlparse(target)
        if parsed.scheme not in {"https", "http", "data"} or (parsed.scheme != "data" and not parsed.netloc):
            problems.append(f"HTML external link/resource is not a valid absolute URL: {target}")
    if re.search(r"\]\(\s*\)|\]\(TODO|\]\(URL\)|\]\(https?://\s*\)", code_masked, re.IGNORECASE):
        problems.append("Markdown contains a placeholder or empty link target")
    return problems


class _TagBalanceParser(HTMLParser):
    VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.problems: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() not in self.VOID_TAGS:
            self.stack.append(tag.lower())

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        return

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in self.VOID_TAGS:
            self.problems.append(f"void HTML tag </{tag}> must not be closed")
            return
        if not self.stack:
            self.problems.append(f"unexpected closing HTML tag </{tag}>")
            return
        if self.stack[-1] != tag:
            self.problems.append(
                f"HTML tag nesting mismatch: expected </{self.stack[-1]}>, found </{tag}>"
            )
            if tag in self.stack:
                while self.stack and self.stack[-1] != tag:
                    self.stack.pop()
                if self.stack:
                    self.stack.pop()
            return
        self.stack.pop()


def _positive_claim(sentence: str, topic: re.Pattern[str]) -> bool:
    if not topic.search(sentence):
        return False
    if re.search(r"\b(?:not|never|no|cannot|can't|doesn't|does not|isn't|is not|isn't yet|hasn't|has not)\b", sentence, re.IGNORECASE):
        return False
    return bool(
        re.search(
            r"\b(?:shows?|demonstrates?|proves?|establishes?|measures?|tests?|is|are|was|were|constitutes?|provides?)\b",
            sentence,
            re.IGNORECASE,
        )
    )


def validate_article(
    article: str,
    post_id: str,
    evidence_packet: str,
    *,
    expected_date: str | None = None,
) -> dict[str, Any]:
    """Run conservative, deterministic checks before a response enters the DAG."""
    errors: list[str] = []
    warnings: list[str] = []
    try:
        frontmatter, body = _extract_frontmatter(article)
    except PostValidationError as exc:
        return {
            "schema_version": 1,
            "post_id": post_id,
            "valid": False,
            "errors": [str(exc)],
            "warnings": [],
            "word_count": _word_count(article),
        }

    title = frontmatter.get("title")
    if not isinstance(title, str) or not title.strip():
        errors.append("frontmatter.title must be a non-empty string")
        title = ""
    layout = frontmatter.get("layout")
    if layout != "post":
        errors.append("frontmatter.layout must be 'post' for the target Jekyll site")
    raw_date = frontmatter.get("date")
    if isinstance(raw_date, (date, datetime)):
        post_date = raw_date.date().isoformat() if isinstance(raw_date, datetime) else raw_date.isoformat()
    elif isinstance(raw_date, str):
        post_date = raw_date[:10]
        try:
            date.fromisoformat(post_date)
        except ValueError:
            errors.append("frontmatter.date must begin with a valid YYYY-MM-DD date")
    else:
        post_date = ""
        errors.append("frontmatter.date must be a valid YYYY-MM-DD date")
    if expected_date and post_date != expected_date:
        errors.append(f"frontmatter.date is {post_date!r}; expected {expected_date!r}")
    slug = _slugify(title)
    if not slug:
        errors.append("title does not produce a usable Jekyll slug")

    # Posts without TeX do not need a MathJax include; formula-bearing posts do.
    math_markup = re.search(
        r"(?s)(?:\$\$.*?\$\$|(?<!\\)\$[^$\n]+\$|\\\[.*?\\\]|\\\(.*?\\\))",
        body,
    )
    if math_markup and "{% include mathjax.html %}" not in body:
        errors.append(
            "math markup is present but the required target-site include is missing: "
            "{% include mathjax.html %}"
        )
    if '<span class="icon-self">StrangeTcy</span>' not in body:
        errors.append("target-site author signature is missing or mismatched")
    if "{% include " in body and not re.search(r"\{% include [\w./-]+\.html %\}", body):
        errors.append("Jekyll include syntax appears malformed")
    if re.search(r"\{%\s*include\s+[^%]+%\}", body):
        for include in re.findall(r"\{%\s*include\s+([^%]+?)\s*%\}", body):
            if not re.fullmatch(r"[\w./-]+\.html", include.strip()):
                errors.append(f"include path is not a target-site .html include: {include.strip()}")

    errors.extend(_balanced_fences(body))
    errors.extend(_validate_links(body))
    html_parser = _TagBalanceParser()
    html_check_body = re.sub(
        r"(?s)```.*?```|~~~.*?~~~|`[^`]*`|\$\$.*?\$\$|(?<!\\)\$[^$\n]+\$",
        " ",
        body,
    )
    html_check_body = re.sub(r"<(https?://[^>]+)>", r"\1", html_check_body, flags=re.IGNORECASE)
    html_check_body = re.sub(r"<(?=\s)", "&lt;", html_check_body)
    try:
        html_parser.feed(html_check_body)
        html_parser.close()
    except Exception as exc:  # HTMLParser is forgiving, but malformed input is still reported.
        errors.append(f"HTML parsing failed: {exc}")
    errors.extend(html_parser.problems)
    if html_parser.stack:
        errors.append("unclosed HTML tags: " + ", ".join(html_parser.stack))

    word_count = _word_count(body)
    if not 1200 <= word_count <= 3200:
        errors.append(f"article body has {word_count} words; expected 1200–3200")

    internal_patterns = [
        (r"⟦", "internal claim-trace annotation marker ⟦"),
        (r"\bF-\d{2,}\b", "internal F-xx evidence ID"),
        (r"\bPOST-0[1-5](?:-C\d{2})?\b", "internal post or claim ID"),
        (r"\b(?:editor(?:ial)?['’]s? notes?|internal trace|compiler prompt)\b", "internal editorial note"),
        (r"(?im)^\s*(?:draft|writer\s*[ab]|final[_ ]writer|editor(?:ial)?\s+(?:note|blueprint|critique)|post[- ]?0?[1-5](?:-c\d{2})?)\s*[:—-]?", "internal draft/post/editor label"),
        (r"\b(?:internal|source) draft\b|\b__seed-\d+\b|\b(?:run|case)[_ -]?id\b", "internal source or result identifier"),
        (r"\b(?:TODO|TBD|PLACEHOLDER)\b", "unresolved placeholder"),
        (r"/tmp/|runtime/runs/|source_snapshots/|artifacts/jobs/|campaign-01-analysis/|trace_index\.csv|claim_traceability\.csv", "internal workspace/provenance path"),
        (r"POST_PRODUCTION_(?:VALIDATOR|SOURCE_INPUT)_METADATA", "compiler-only metadata marker"),
        (r"repository\.dirty\s*=\s*true", "raw internal dirty-repository flag"),
    ]
    for pattern, description in internal_patterns:
        if re.search(pattern, article, re.IGNORECASE):
            errors.append(f"public copy leaks {description}")

    metadata: dict[str, Any] = {}
    try:
        metadata = _packet_metadata(evidence_packet)
    except PostValidationError as exc:
        errors.append(str(exc))
    allowed_numbers = set(str(value) for value in metadata.get("allowed_numbers", []))
    body_for_numbers = _strip_markdown_for_checks(body)
    used_numbers = _extract_numbers(body_for_numbers)
    unsupported_numbers = sorted(used_numbers - allowed_numbers, key=lambda value: (float(re.sub(r"%$", "", value)) if re.fullmatch(r"\d+(?:\.\d+)?%?", value) else float("inf"), value))
    if unsupported_numbers:
        errors.append(
            "numeric literals are not present in the source draft/evidence packet: "
            + ", ".join(unsupported_numbers)
        )
    used_number_words = _extract_quantitative_word_tokens(body_for_numbers)
    unsupported_number_words = sorted(used_number_words - allowed_numbers, key=lambda value: (int(value) if value.isdigit() else 10**12, value))
    if unsupported_number_words:
        errors.append(
            "spelled-out quantitative counts are not present in the source draft/evidence packet: "
            + ", ".join(unsupported_number_words)
        )

    trace_rows = _extract_trace_rows(evidence_packet)
    finding_rows = _extract_finding_rows(evidence_packet)
    failure_rows = _extract_failure_detail_rows(evidence_packet)
    traceability_audit = _audit_numeric_claim_traceability(body, trace_rows, finding_rows, failure_rows)
    unresolved_trace_sentences = []
    for sentence in traceability_audit["unmapped_numeric_claim_sentences"]:
        if re.search(r"\b(?:seed|dirty source|dirty repository|working tree|comparator|role passes|independent replication)\b", sentence, re.IGNORECASE):
            warnings.append(f"methodological numeric caveat is sourced in the immutable packet but has no post-claim row: {sentence}")
        else:
            unresolved_trace_sentences.append(sentence)
    if unresolved_trace_sentences:
        errors.append(
            "quantitative result claim sentence(s) do not map to an internal claim-traceability row; see traceability_audit"
        )

    clean_sentences = re.split(r"(?<=[.!?])\s+|\n+", _strip_markdown_for_checks(body))
    independent_pattern = re.compile(
        r"\bindependent(?:ly)?\s+(?:replication|replications|replicated|replicate|(?:Arena\s+)?models?(?:\s+(?:runs?|outputs?|calls?|responses?))?)\b",
        re.IGNORECASE,
    )
    for sentence in clean_sentences:
        if independent_pattern.search(sentence) and not re.search(
            r"\b(?:not|no|never|without|cannot|does not|aren't|are not)\b",
            sentence,
            re.IGNORECASE,
        ):
            errors.append("article overstates independent replication or independent model execution")
            break

    recursive_tom = re.compile(
        r"\b(?:recursive\s+(?:theory\s+of\s+mind|ToM|mental[- ]state reasoning)|(?:theory\s+of\s+mind|ToM)[^.!?]{0,55}recursive)\b",
        re.IGNORECASE,
    )
    turing_claim = re.compile(r"\bTuring(?:[- ]complete| completeness)\b", re.IGNORECASE)
    for sentence in clean_sentences:
        if post_id == "POST-02" and _positive_claim(sentence, recursive_tom):
            errors.append("POST-02 makes an unsupported positive recursive-ToM claim")
            break
        if post_id == "POST-05" and _positive_claim(sentence, turing_claim):
            errors.append("POST-05 makes an unsupported positive Turing-completeness claim")
            break

    caveat_text = _strip_markdown_for_checks(body).lower()
    if post_id in {"POST-01", "POST-02", "POST-03", "POST-04", "POST-05"}:
        if not re.search(r"\b(?:one|single)[- ]seed\b|\bone\s+selected\s+seed\b|\bsingle seed\b", caveat_text):
            errors.append("required caveat missing: describe the one-seed scope")
        if not re.search(r"\b(?:dirty source|source.{0,45}dirty|dirty.{0,45}(?:repository|working tree|checkout|source tree)|working tree.{0,35}dirty|uncommitted source|uncommitted changes)\b", caveat_text):
            errors.append("required caveat missing: the paid-run source/comparator identity was unresolved because the repository was dirty")
        if not re.search(r"\b(?:does not prove|doesn't prove|does not establish|doesn't establish|cannot establish|cannot show|not proof|not evidence that|does not show|doesn't show)\b", caveat_text):
            errors.append("required caveat missing: explicitly limit what the benchmark establishes")
        if not re.search(r"\bjudge\b", caveat_text):
            errors.append("required caveat missing: discuss the task/judge boundary")
    if post_id in {"POST-01", "POST-03", "POST-04"}:
        if not re.search(r"\bcompile[- ]only\b", caveat_text):
            errors.append("required caveat missing: distinguish compile-only judgments")
        if not re.search(r"\b(?:behavioral reference|behavioral-reference|exact-instance oracle)\b", caveat_text):
            errors.append("required caveat missing: distinguish behavioral-reference judgments")
        if not re.search(r"\b(?:exploratory|not a validated|not validated|no behavioral reference|without a behavioral reference)\b", caveat_text):
            errors.append("required caveat missing: compile-only results are exploratory, not a validated behavioral aggregate")
    if post_id == "POST-02":
        if not re.search(r"\b(?:Bayesian|Bayes)\b", caveat_text, re.IGNORECASE):
            errors.append("required caveat missing: identify the task as Bayesian inference")
        if not re.search(r"\b(?:not|does not|doesn't|cannot|never)\b[^.!?]{0,80}\b(?:recursive|theory of mind|ToM)\b|\b(?:not a|not an|not itself a)\s+(?:recursive\s+)?(?:theory of mind|ToM)\b", caveat_text):
            errors.append("required caveat missing: state that the epistemic-games task is not a recursive-ToM benchmark")
    if post_id == "POST-05":
        if not re.search(r"\b(?:not|does not|doesn't|cannot|no claim|not evidence)\b[^.!?]{0,80}\bturing[- ]complete\b|\b(?:not|does not|doesn't|cannot)\b[^.!?]{0,80}\b(?:turing completeness|turing-complete general computation)\b", caveat_text):
            errors.append("required caveat missing: do not claim Turing completeness from the observed behavior")

    trace_ids = metadata.get("trace_row_ids", [])
    if not isinstance(trace_ids, list) or not trace_ids:
        errors.append("no internal claim-traceability rows were loaded for the validator")
    evidence_inputs = metadata.get("evidence_input_sha256", {})
    if not isinstance(evidence_inputs, dict) or not evidence_inputs:
        errors.append("evidence packet has no input hash ledger")

    return {
        "schema_version": 1,
        "post_id": post_id,
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "title": title,
        "date": post_date,
        "slug": slug,
        "suggested_jekyll_filename": f"{post_date}-{slug}.md" if post_date and slug else None,
        "word_count": word_count,
        "numeric_literals_checked": sorted(used_numbers),
        "unsupported_numeric_literals": unsupported_numbers,
        "spelled_quantitative_counts_checked": sorted(used_number_words),
        "unsupported_spelled_quantitative_counts": unsupported_number_words,
        "traceability_audit": traceability_audit,
        "trace_row_ids_loaded": trace_ids,
        "evidence_input_sha256": evidence_inputs,
        "checks": {
            "frontmatter": True,
            "jekyll_layout_include_author": True,
            "markdown_fences_and_links": True,
            "html_tag_balance": True,
            "internal_provenance_leakage": True,
            "numerical_claim_literals": True,
            "numeric_claim_traceability": True,
            "independent_replication_overclaim": True,
            "post_specific_overclaim_and_caveats": True,
        },
    }


def _as_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def _compact_csv(text: str, columns: list[str], predicate: Any | None = None) -> str:
    reader = csv.DictReader(io.StringIO(text))
    headers = [name for name in columns if name in (reader.fieldnames or [])]
    rows = list(reader)
    if predicate is not None:
        rows = [row for row in rows if predicate(row)]
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=headers, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def _markdown_section_paragraphs(text: str, heading: str) -> list[str]:
    match = re.search(
        rf"(?ms)^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)",
        text,
    )
    if not match:
        return []
    return [part.strip() for part in re.split(r"\n\s*\n", match.group(1)) if part.strip()]


def _compact_house_style() -> str:
    return """Target Jekyll frame: YAML frontmatter with `title`, `date: 2026-10-03`, `layout: post`; when using math, place `{% include mathjax.html %}` immediately after it. Then use the exact byline `*by <span class=\"icon-self\">StrangeTcy</span>*` and the site's `<dl class=\"epistemic-status\">` fields, in order: Original ideas, Synthesis, Prose, Certainty, Importance. Attribute the actual Arena writing process accurately; do not invent outside authors.

Voice: first-person, curious, technically literate, willing to self-correct. Open in prose, not an `Introduction`; use short, specific `##` argumentative turns and airy paragraphs. Questions should move the argument. End by stating what the evidence does and does not license. Links/citations belong where they matter; avoid a generic benchmark-report register. Target 1,800–2,800 words without padding."""


def _compact_style_references(text: str) -> str:
    sources = [
        (
            "The Diagram Is the Spec — a concrete distinction",
            "A unit test says:",
            4,
            "2026-09-27-the-diagram-in-the-spec.md",
        ),
        (
            "Knowing What Kind of Problem You Are In — conceptual opening",
            "Most benchmarks hand the agent its context for free.",
            2,
            "2026-09-26-knowing-what-kind-of-problem-you-are-in.md",
        ),
        (
            "The Next Question Is Part of the Game — question-led opening",
            "Suppose I want you to make the wrong decision.",
            4,
            "2026-09-30-the-next-question-is-part-of-the-game.md",
        ),
        (
            "Lying With Truth — visible self-correction",
            "The first formalisation was wrong.",
            4,
            "2026-10-01-lying-with-truth.md",
        ),
    ]
    blocks = [
        "Short excerpts from actual StrangeTcy/strangetcy.github.io posts at revision bcc89c392920b3be172a27eec10ad205b58d4fa3; style evidence only, not wording to reuse.",
    ]
    for title, anchor, paragraph_count, filename in sources:
        start = text.find(anchor)
        if start < 0:
            continue
        paragraphs: list[str] = []
        for paragraph in re.split(r"\n\s*\n", text[start:]):
            value = paragraph.strip()
            if not value or value.startswith(("```", "## ")):
                break
            if "```" in value:
                break
            paragraphs.append(re.sub(r"(?<!\n)\n(?!\n)", " ", value))
            if len(paragraphs) == paragraph_count:
                break
        display_date = filename[:10]
        blocks.extend([f"### {title} ({display_date})", "\n\n".join(paragraphs), ""])
    return "\n".join(blocks).strip() + "\n"


def _compact_reference_list(text: str, post_id: str) -> str:
    if post_id == "POST-04":
        return """POST-04 prior-work references from the source draft; context only, not validation of this campaign.

- You Wang, Michael Pradel, and Zhongxin Liu. “Are ‘Solved Issues’ in SWE-bench Really Solved Correctly? An Empirical Study.” The study reports that 7.8% of plausible patches counted correct by benchmark validation failed the full developer-written test suite in its studied SWE-bench Verified setting. This rate is not an estimate for the Atria campaign. https://dl.acm.org/doi/10.1145/3744916.3764576
- HELM, Liang et al. (TMLR 2023), “Holistic Evaluation of Language Models”: a precedent for broad scenario and metric coverage, not a validation of this campaign. https://arxiv.org/abs/2211.09110

This targeted reference check supports no “first” or exhaustive-novelty claim."""
    if post_id == "POST-05":
        return """POST-05 prior-work references from the source draft; context only, not validation of this campaign.

- VarBench, Qian et al. (Findings of EMNLP 2024), “Robust Language Model Benchmarking Through Dynamic Variable Perturbation”: dynamic variable perturbation and repeated sampling for variable-based experiments. https://aclanthology.org/2024.findings-emnlp.946/
- HELM, Liang et al. (TMLR 2023), “Holistic Evaluation of Language Models”: broad scenario coverage and multiple metrics, as context for avoiding a single-score interpretation. https://arxiv.org/abs/2211.09110

This targeted reference check supports no “first” or exhaustive-novelty claim."""
    return """Prior-work references from the supplied campaign bibliography; context only, not validation of this campaign.

- HELM, Liang et al. (TMLR 2023), “Holistic Evaluation of Language Models”: 42 scenarios and multiple metrics. https://arxiv.org/abs/2211.09110
- VarBench, Qian et al. (Findings of EMNLP 2024), “Robust Language Model Benchmarking Through Dynamic Variable Perturbation”: dynamic variable perturbation; five sampled runs (seeds 40–44) for variable-based experiments. https://aclanthology.org/2024.findings-emnlp.946/

This targeted reference check supports no “first” or exhaustive-novelty claim."""


def _compact_source_audit(text: str) -> str:
    if "## Source identity and comparator" in text:
        return text.rstrip() + "\n"
    return """## Source identity and comparator
The archive points to commit `d7357092493f311f649a0742889b301d796911b5` and records a dirty repository. All 33 selected config hashes match the clean comparator, but exact paid-run task/judge source identity remains unresolved.

## Sampling design
One selected seed per case across 33 environments; no environment-level replication. Most contrasts are sparse one-factor substitutions, not interaction tests or population estimates."""


def _compact_evidence_extract(text: str) -> str:
    archive_hash = re.search(r"SHA-256:? `([0-9a-f]{64})`", text)
    archive = archive_hash.group(1) if archive_hash else "not reproduced in this excerpt"
    return (
        "Frozen paid-run archive SHA-256: `" + archive + "`. The archive records a dirty repository; "
        "the inspected clean source is a comparator, not proof of exact paid-run source identity. "
        "Copied tables are summaries, not substitutes for primary artifacts.\n"
    )


def _compact_limitations(text: str, post_id: str) -> str:
    if post_id == "POST-04":
        return """- One selected seed per case; no cell-level replications. Keep 194 raw results, 24 separate omissions, two provider-terminal cases, and the 192-case sensitivity set distinct.
- The eligible set mixes 72 behavioral-reference and 120 compile-only cases; compile-only results are exploratory, not a validated behavioral aggregate.
- The repository was recorded dirty; matching config hashes do not establish exact task/judge identity. Axes are task-specific and sparse; names/hints are bundled, and validator/runtime/judge failures are not behavioral misses."""
    return text.rstrip()


def _compact_failure_details(text: str) -> str:
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames and "condition" in reader.fieldnames:
        return text
    output_rows: list[dict[str, str]] = []
    relevant_modes = {"underfit", "source_invalid", "runtime_error", "runtimeerror", "overfit_visible_tests"}
    for row in reader:
        mode = str(row.get("failure_mode_raw", ""))
        if mode.lower() not in relevant_modes:
            continue
        env = str(row.get("environment", ""))
        case_id = str(row.get("case_id", ""))
        condition = case_id.split("__", 1)[1] if "__" in case_id else case_id
        condition = re.sub(r"__seed-\d+\Z", "", condition)
        try:
            notes = json.loads(row.get("final_notes", "[]"))
        except json.JSONDecodeError:
            notes = [row.get("final_notes", "")]
        note_text = " ".join(str(value) for value in notes)
        note_text = re.sub(r"\s+", " ", note_text)
        detail = ""
        match = re.search(r"length mismatch \(in=(\d+), out=(\d+)\)", note_text)
        if match:
            detail = f"length mismatch: input {match.group(1)}, output {match.group(2)}"
        elif match := re.search(r"disallowed import ['\"]([^'\"]+)", note_text):
            detail = f"source validator rejected import {match.group(1)}"
        elif "unterminated triple-quoted string" in note_text:
            detail = "source syntax error: unterminated triple-quoted string"
        elif "unexpected indent" in note_text:
            detail = "source syntax error: unexpected indentation"
        elif "dtype Float" in note_text:
            detail = "runtime error: float tensor used as a boolean condition"
        elif "missing:" in note_text or "missing required" in note_text:
            missing = re.search(r"missing: ([^,\\\"]+)", note_text)
            detail = f"required companion file missing: {missing.group(1)}" if missing else "required companion file missing"
        try:
            metrics = json.loads(row.get("final_metrics", "{}"))
        except json.JSONDecodeError:
            metrics = {}
        if isinstance(metrics, dict) and metrics.get("trusted_score") == 1.0:
            detail = (detail + "; " if detail else "") + "trusted_score=1.0 despite failed terminal label"
        output_rows.append(
            {
                "environment": env,
                "condition": condition,
                "judge": str(row.get("judge_guarantee", "")),
                "score": str(row.get("score", "")),
                "failure": mode,
                "detail": detail,
            }
        )
    buffer = io.StringIO(newline="")
    fields = ["environment", "condition", "judge", "score", "failure", "detail"]
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(output_rows)
    return buffer.getvalue()


def _render_model_artifact(name: str, text: str, post_id: str, source_sha256: str) -> str:
    """Render a concise, task-relevant view; full sources and hashes stay in the handoff ledger."""
    if (
        name in {"workflow_input_manifest", "campaign_provenance"}
        or any(token in name for token in ("campaign_exclusions", "campaign_scope"))
        or ("case_results" in name and post_id == "POST-01")
    ):
        return ""
    if "house_style" in name:
        return _compact_house_style()
    if "style_reference_material" in name:
        return _compact_style_references(text)
    if name == "references":
        return _compact_reference_list(text, post_id)
    if "relevant_findings" in name:
        try:
            payload = json.loads(text)
            compact = {
                "schema_version": payload.get("schema_version", 1),
                "post_id": payload.get("post_id", post_id),
                "claim_ids": payload.get("claim_ids", []),
                "trace_finding_ids": payload.get("trace_finding_ids", []),
                "findings": [],
            }
            fields = ("id", "status", "claim", "quantitative_result", "confidence", "limitations")
            for row in payload.get("findings", []):
                if isinstance(row, dict):
                    compact["findings"].append({key: row[key] for key in fields if key in row})
            return json.dumps(compact, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n"
        except (json.JSONDecodeError, AttributeError):
            return text
    if "trace_rows" in name:
        return _compact_csv(text, ["post_id", "claim_id", "finding_ids"])
    if "evidence_extract" in name:
        return _compact_evidence_extract(text)
    if "limitations" in name:
        return _compact_limitations(text, post_id) + "\n"
    if "source_audit" in name:
        return _compact_source_audit(text)
    if "axis_placeholder_audit" in name:
        return _compact_csv(text, ["config_path", "axis", "placeholder", "source_reference_status"])
    if "axis_summary" in name:
        env_axis = {
            "POST-01": {
                "regex_state_machine": {"hidden_depth", "surface_deceptiveness"},
                "css_state_machine": {"hidden_depth", "surface_deceptiveness"},
                "sql_fixed_point": {"hidden_depth"},
                "spreadsheet_dataflow": {"hidden_depth", "surface_deceptiveness"},
                "moco": {"visible_tests"},
                "rd_adaptive_halting": {"recurrence_depth"},
            },
            "POST-02": {"epistemic_games": None},
            "POST-03": {
                "categorical_lenses": {"naming", "symptom_mask"},
                "compositional_optimizer": {"naming", "symptom_mask"},
                "sheaf_physical_constraints": {"naming", "symptom_mask"},
            },
            "POST-04": {},
            "POST-05": {
                "regex_state_machine": {"hidden_depth", "surface_deceptiveness"},
                "css_state_machine": {"hidden_depth", "surface_deceptiveness"},
                "sql_fixed_point": {"hidden_depth", "surface_deceptiveness"},
                "spreadsheet_dataflow": {"hidden_depth", "surface_deceptiveness"},
                "ci_dependency_graph": {"hidden_depth", "surface_deceptiveness"},
                "template_interpreter": {"hidden_depth", "surface_deceptiveness"},
            },
        }.get(post_id, {})
        reader = csv.DictReader(io.StringIO(text))
        if reader.fieldnames and "control" in reader.fieldnames:
            return text
        rows: list[dict[str, str]] = []
        for source_row in reader:
            allowed = env_axis.get(source_row.get("environment", ""), set())
            if allowed is not None and source_row.get("axis") not in allowed:
                continue
            if post_id == "POST-01":
                try:
                    controls = json.loads(source_row.get("other_axis_controls", "{}"))
                except json.JSONDecodeError:
                    continue
                if not isinstance(controls, dict) or any(value != "easy" for value in controls.values()):
                    continue
            try:
                judge_values = json.loads(source_row.get("judge_guarantees", "[]"))
            except json.JSONDecodeError:
                judge_values = source_row.get("judge_guarantees", "")
            judge = ";".join(str(value) for value in judge_values) if isinstance(judge_values, list) else str(judge_values)
            rows.append(
                {
                    "environment": source_row.get("environment", ""),
                    "axis": source_row.get("axis", ""),
                    "level": source_row.get("level", ""),
                    "control": "all_other_axes_easy" if post_id == "POST-01" else source_row.get("other_axis_controls", ""),
                    "recorded": source_row.get("recorded_cases", ""),
                    "eligible": source_row.get("performance_eligible_cases", ""),
                    "passes": source_row.get("passes", ""),
                    "fails": source_row.get("fails", ""),
                    "rate": source_row.get("pass_rate", ""),
                    "judge": judge,
                }
            )
        output = io.StringIO(newline="")
        fields = ["environment", "axis", "level", "control", "recorded", "eligible", "passes", "fails", "rate", "judge"]
        writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        return output.getvalue()
    if "environment_summary" in name:
        selected_envs = {
            "POST-01": {
                "regex_state_machine", "css_state_machine", "sql_fixed_point", "spreadsheet_dataflow",
                "ci_dependency_graph", "template_interpreter", "moco", "batchnorm_ema", "glyph",
                "rd_adaptive_halting", "rd_gradient_credit", "rd_state_carry",
            },
        }.get(post_id)
        def keep_environment(row: dict[str, str]) -> bool:
            return selected_envs is None or row.get("environment") in selected_envs
        columns = [
            "environment", "recorded_cases", "performance_eligible_cases", "passes_performance_set",
            "fails_performance_set", "pass_rate_performance_set", "behavioral_reference_n",
            "behavioral_reference_passes", "behavioral_reference_fails", "compile_only_n",
            "compile_only_passes", "compile_only_fails",
        ]
        return _compact_csv(text, columns, keep_environment)
    if "analysis_family_summary" in name:
        return _compact_csv(text, [
            "analysis_family", "recorded_cases", "performance_eligible_cases",
            "passes_performance_set", "fails_performance_set", "pass_rate_performance_set",
            "behavioral_reference_n", "behavioral_reference_passes", "behavioral_reference_fails",
            "compile_only_n", "compile_only_passes", "compile_only_fails",
        ])
    if "case_results" in name:
        return _compact_csv(
            text,
            [
                "case_id", "environment", "track", "analysis_family", "seed", "difficulty_levels",
                "judge_guarantee", "status", "verdict", "score", "failure_mode_normalized",
                "final_notes", "performance_eligible", "exclusion_reason",
            ],
        )
    if "failure_details" in name:
        return _compact_failure_details(text)
    if "failure_taxonomy" in name:
        return _compact_csv(
            text,
            ["failure_mode_normalized", "count", "share_of_eligible_failures", "judge_guarantees"],
        )
    return text


def prepare_post_packet(context: JobContext) -> ExecutionResult:
    post_id = _post_id_from_job(context.job.job_id)
    if post_id is None:
        raise ValueError(f"prepare_post job id does not identify a post: {context.job.job_id}")
    lines = [
        f"# Compiler evidence packet — {post_id}",
        "",
        "This packet is an immutable snapshot of the source draft, audited findings, evidence, and style inputs attached to this DAG job.",
        "Do not treat the internal draft as prose to paraphrase. Its embedded evidence IDs are private compiler bookkeeping.",
        "",
    ]
    trace_rows: list[dict[str, Any]] = []
    evidence_hashes: dict[str, str] = {}
    numeric_sources: list[str] = []
    finding_ids: set[str] = set()
    for index, (path, record) in enumerate(zip(context.input_paths, context.input_records), start=1):
        reference = str(record.get("reference", f"input:{index - 1}"))
        name = reference.split(":", 1)[-1]
        text = _read_text(path)
        source_hash = str(record.get("sha256", ""))
        display_text = _render_model_artifact(name, text, post_id, source_hash)
        display_hash = hashlib.sha256(display_text.encode("utf-8")).hexdigest()
        label = f"{index:02d} — {name}"
        if display_text.strip():
            lines.extend(
                [
                    f"## BEGIN INPUT ARTIFACT: {label}",
                    f"Source snapshot SHA-256: `{source_hash}`",
                    f"Rendered message SHA-256: `{display_hash}`",
                    f"Original reference: `{reference}`",
                    "",
                    display_text.rstrip(),
                    "",
                    f"## END INPUT ARTIFACT: {label}",
                    "",
                ]
            )
        evidence_hashes[reference] = source_hash
        if "trace_rows" in name:
            try:
                trace_rows = list(csv.DictReader(io.StringIO(display_text)))
            except csv.Error:
                trace_rows = []
        if "relevant_findings" in name:
            try:
                finding_payload = json.loads(display_text)
                finding_ids.update(
                    str(row.get("id"))
                    for row in finding_payload.get("findings", [])
                    if isinstance(row, dict) and row.get("id")
                )
            except (json.JSONDecodeError, AttributeError):
                pass
        if display_text.strip() and name not in {"house_style", "style_reference_material", "workflow_input_manifest", "campaign_provenance"}:
            numeric_sources.append(display_text)

    trace_ids: list[str] = []
    for row in trace_rows:
        post = row.get("post_id", "")
        claim_id = row.get("claim_id", "")
        if post == post_id and claim_id:
            trace_ids.append(claim_id)
    allowed_numbers = sorted(set().union(*(_extract_numbers(source) for source in numeric_sources)))
    metadata = {
        "post_id": post_id,
        "publication_date": "2026-10-03",
        "trace_row_ids": sorted(set(trace_ids)),
        "finding_ids": sorted(finding_ids),
        "allowed_numbers": allowed_numbers,
        "evidence_input_sha256": evidence_hashes,
        "source_input_records": [
            {
                key: record.get(key)
                for key in ("reference", "source_path", "snapshot_path", "sha256", "size_bytes", "attachment_index")
            }
            for record in context.input_records
        ],
    }
    lines.extend(
        [
            "## Compiler-only validator metadata (never copy into public copy)",
            "<!-- POST_PRODUCTION_VALIDATOR_METADATA",
            json.dumps(metadata, ensure_ascii=False, sort_keys=True),
            "-->",
            "",
        ]
    )
    packet = "\n".join(lines)
    return ExecutionResult(
        response_text=packet,
        model_name="local:post-production-packet-builder",
        metadata={
            "post_id": post_id,
            "input_count": len(context.input_records),
            "input_sha256": evidence_hashes,
            "trace_row_ids": metadata["trace_row_ids"],
            "allowed_numeric_literal_count": len(allowed_numbers),
        },
    )


def _load_json_input(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(_read_text(path))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise PostValidationError(f"{label} is not valid UTF-8 JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise PostValidationError(f"{label} must contain a JSON object")
    return value


def _extract_json_object(text: str) -> dict[str, Any]:
    value = text.strip()
    value = re.sub(r"\A```(?:json)?\s*|\s*```\Z", "", value, flags=re.IGNORECASE)
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as exc:
        raise PostValidationError(f"cross-post review must be strict JSON: {exc}") from exc
    if not isinstance(parsed, dict):
        raise PostValidationError("cross-post review response must be a JSON object")
    return parsed


def _normalize_cross_review(text: str) -> dict[str, Any]:
    raw = _extract_json_object(text)
    revisions = raw.get("revisions", [])
    if not isinstance(revisions, list):
        raise PostValidationError("cross-post review 'revisions' must be a list")
    result: dict[str, Any] = {"schema_version": 1, "revisions": []}
    seen: set[str] = set()
    for item in revisions:
        if not isinstance(item, dict):
            raise PostValidationError("each cross-post revision must be a JSON object")
        post_id = item.get("post_id")
        if post_id not in POST_IDS:
            raise PostValidationError(f"unknown post_id in cross-post review: {post_id!r}")
        if post_id in seen:
            raise PostValidationError(f"duplicate cross-post revision for {post_id}")
        seen.add(post_id)
        needed = item.get("needed")
        if not isinstance(needed, bool):
            raise PostValidationError(f"revision {post_id} must have boolean 'needed'")
        request = item.get("change_request", "")
        issues = item.get("issues", [])
        if not isinstance(request, str) or not isinstance(issues, list):
            raise PostValidationError(f"revision {post_id} has malformed issues/change_request")
        result["revisions"].append(
            {
                "post_id": post_id,
                "needed": needed,
                "issues": [str(value) for value in issues],
                "change_request": request.strip(),
            }
        )
    by_post = {item["post_id"]: item for item in result["revisions"]}
    result["revisions"] = [
        by_post.get(post_id, {"post_id": post_id, "needed": False, "issues": [], "change_request": ""})
        for post_id in POST_IDS
    ]
    return result


def _conditional_result(context: JobContext, check: dict[str, Any], previous: Path) -> ExecutionResult | None:
    if check:
        response_text = _read_text(previous)
        return ExecutionResult(
            response_text=response_text,
            model_name="local:post-production-no-op-gate",
            metadata={"revision_skipped": True, "gate_result": check},
        )
    return None


def _artifact_display_title(name: str) -> str:
    if name.startswith("source_draft_"):
        return "Original source draft"
    if name.startswith("trace_rows_"):
        return "Claim-to-finding map"
    if name.startswith("relevant_findings_"):
        return "Relevant finding records"
    if name.startswith("evidence_extract_"):
        return "Archive evidence extract"
    if name.startswith("limitations_"):
        return "Evidence limitations"
    if name.startswith("source_audit_"):
        return "Source-comparator audit"
    if "axis_summary" in name:
        return "Selected axis results"
    if "environment_summary" in name:
        return "Relevant environment totals"
    if "analysis_family_summary" in name:
        return "Analysis-family totals"
    if "failure_details" in name:
        return "Selected failure details"
    if "failure_taxonomy" in name:
        return "Failure taxonomy"
    return {
        "house_style": "Target-site style and Jekyll conventions",
        "style_reference_material": "Actual StrangeTcy reference-post excerpts",
        "references": "Relevant prior-work references",
    }.get(name, name.replace("_", " ").title())


def _compact_prepared_packet(packet: str, post_id: str) -> tuple[str, list[dict[str, str]]]:
    pattern = re.compile(
        r"## BEGIN INPUT ARTIFACT: ([^\n]+)\n(.*?)\n## END INPUT ARTIFACT: \1",
        re.DOTALL,
    )
    matches = list(pattern.finditer(packet))
    if not matches:
        return packet, []
    sections: list[str] = []
    renderings: list[dict[str, str]] = []
    for match in matches:
        label = match.group(1)
        name = label.split("—", 1)[-1].strip()
        block_lines = match.group(2).splitlines()
        source_hash = ""
        reference = ""
        content_start = 0
        for index, line in enumerate(block_lines):
            hash_match = re.search(r"SHA-256: `([^`]+)`", line)
            if hash_match and not source_hash:
                source_hash = hash_match.group(1)
            ref_match = re.search(r"Original reference: `([^`]+)`", line)
            if ref_match:
                reference = ref_match.group(1)
            if not line.strip():
                content_start = index + 1
                break
        content = "\n".join(block_lines[content_start:]).rstrip()
        rendered = _render_model_artifact(name, content, post_id, source_hash)
        rendered_hash = hashlib.sha256(rendered.encode("utf-8")).hexdigest()
        renderings.append({"reference": reference, "source_sha256": source_hash, "rendered_sha256": rendered_hash})
        if rendered.strip():
            sections.extend([f"## {_artifact_display_title(name)}", rendered.rstrip(), ""])
    prefix = packet[: matches[0].start()]
    suffix = packet[matches[-1].end() :]
    compacted = prefix + "\n".join(sections) + suffix
    compacted = re.sub(
        r"\n## Compiler-only validator metadata[^\n]*\n<!-- POST_PRODUCTION_VALIDATOR_METADATA.*?-->\s*\Z",
        "\n",
        compacted,
        flags=re.DOTALL,
    )
    return compacted.rstrip() + "\n", renderings


def _compact_writer_template(post_id: str) -> str:
    post_specific = ""
    if post_id == "POST-04":
        post_specific = """
POST-04-specific evidence boundaries:
- Keep the 194 raw scored rows, 24 separate omissions, the 193-row single-provider-exclusion sensitivity set, and the 192-row two-provider-exclusion analysis set distinct. The 24 omissions are not scored failures.
- In the 192-row set, distinguish 72 behavioral-reference cases from 120 exploratory compile-only cases; scope the 61-failure taxonomy to that set.
- Two raw rows have `invalid_action` labels but final notes attributing terminal failure to provider transients. Preserve the raw labels and the terminal-note interpretation; do not describe those rows as ordinary model-format failures.
- The seven `epistemic_games` rows retain their recorded track label. Any semantic regrouping is an analysis view, not a rewrite of the archive.
- Treat configuration/telemetry inconsistencies as metadata discrepancies, not evidence about internal reasoning. The archive has no spend field, and no reasoning text is reproduced.
- The SWE-bench study's 7.8% result applies only to its studied setting; never present it as a rate for this campaign.
- For literature context, use only the SWE-bench study and HELM entries in the POST-04 reference block. Do not import unrelated cross-post bibliography items from campaign-wide evidence summaries.
"""
    return f"""# Independent StrangeTcy research essay — {post_id}

Write one complete essay with a new thesis, opening, and argument structure. Use the full draft as an evidence map, not an outline or prose to paraphrase. This is one of two parallel candidates; do not refer to or imitate another answer.

Use only supplied facts and citations. Keep raw scores, exclusions, provider-terminal cases, denominators, judge guarantees, and failure layers distinct. Compile-only outcomes are exploratory, not a validated behavioral aggregate. There is one selected seed per cell; subsequent editorial/model role passes are not independent replications. The repository was recorded dirty: the clean source is only a comparator. These sparse results do not establish causal effects, a common difficulty scale, or a general capability ranking. Keep caveats next to claims. Distinguish validator/runtime/tool/judge failures from behavioral misses.

POST-02 is Bayesian inference over stipulated policies, not recursive ToM; POST-05's Rule 110/code-repair observations do not establish Turing completeness. Category-track outcomes are heterogeneous code-repair results, not a theorem or scalar score.
{post_specific}
The packet includes verbatim excerpts from actual StrangeTcy posts: use them only for rhetorical structure, never copy distinctive wording, examples, titles, or author-process claims. Avoid generic AI prose and benchmark-report tone; use technical detail and math/tables/diagrams only when they clarify.

Return only the complete Markdown article, 1,800–2,500 words. Use frontmatter `title`, `date: 2026-10-03`, `layout: post`; the exact StrangeTcy byline; and the site's epistemic-status `<dl>` fields in order: Original ideas, Synthesis, Prose, Certainty, Importance. If using math, place `{{% include mathjax.html %}}` after frontmatter. Attribute the actual Arena writing process accurately. No preface, editor note, draft label, internal `F-xx`/`POST-xx` ID, path, hash, or response fence."""


def _handoff_prompt(context: JobContext, post_id: str | None) -> tuple[str, str, list[dict[str, Any]]]:
    if context.job.role in {"battle_writer_a", "battle_writer_b"}:
        template = _compact_writer_template(post_id or "POST-01")
    else:
        template = context.prompt_text.replace("{{POST_ID}}", post_id or "CROSS-POST")
    sections = [
        template.rstrip(),
        "",
        "# Compiler-supplied inputs",
        "Use the following attached artifacts as source material; do not echo internal paths, hashes, claim IDs, or editorial labels in public prose.",
        "Filtered evidence tables are task-relevant rendered excerpts; source snapshots and full input hashes remain immutable in the compiler.",
        "",
    ]
    renderings: list[dict[str, Any]] = []
    for index, (path, record) in enumerate(zip(context.input_paths, context.input_records), start=1):
        reference = str(record.get("reference", f"input:{index - 1}"))
        label = f"{index:02d} — {reference}"
        text = _read_text(path)
        rendered = text
        source_renderings: list[dict[str, str]] = []
        if text.startswith("# Compiler evidence packet —"):
            packet_post = re.search(r"^# Compiler evidence packet — (POST-0[1-5])$", text, re.MULTILINE)
            rendered, source_renderings = _compact_prepared_packet(text, packet_post.group(1) if packet_post else (post_id or "POST-01"))
        rendered_hash = hashlib.sha256(rendered.encode("utf-8")).hexdigest()
        sections.extend(
            [
                f"[[[ BEGIN INPUT {label} | source_sha256={record.get('sha256', '')} | rendered_sha256={rendered_hash} ]]]",
                rendered.rstrip(),
                f"[[[ END INPUT {label} ]]]",
                "",
            ]
        )
        renderings.append(
            {
                "reference": reference,
                "source_sha256": str(record.get("sha256", "")),
                "rendered_sha256": rendered_hash,
                "source_renderings": source_renderings,
            }
        )
    return template, "\n".join(sections), renderings


def _source_inputs_from_context(context: JobContext) -> list[dict[str, Any]]:
    collected: dict[tuple[str, str], dict[str, Any]] = {}
    for path in context.input_paths:
        text = _read_text(path)
        try:
            metadata = _packet_metadata(text)
            records = metadata.get("source_input_records", [])
        except PostValidationError:
            match = re.search(
                r"<!-- POST_PRODUCTION_SOURCE_INPUT_METADATA\s*(\{.*?\})\s*-->\s*$",
                text,
                re.DOTALL,
            )
            if not match:
                continue
            try:
                metadata = json.loads(match.group(1))
            except json.JSONDecodeError:
                continue
            records = metadata.get("source_input_records", [])
        if not isinstance(records, list):
            continue
        for record in records:
            if not isinstance(record, dict):
                continue
            key = (str(record.get("reference", "")), str(record.get("sha256", "")))
            if key[0] and key[1]:
                collected[key] = record
    return list(collected.values())


def _write_handoff(context: JobContext, *, post_id: str | None, next_stage: str) -> ExecutionResult:
    _, exact_prompt, input_renderings = _handoff_prompt(context, post_id)
    prompt_path = context.job_dir / "prompt_to_paste.md"
    handoff_path = context.job_dir / "handoff.json"
    prompt_bytes = exact_prompt.encode("utf-8")
    prompt_hash = hashlib.sha256(prompt_bytes).hexdigest()
    response_relative = str(context.job_state.get("output_artifact", ""))
    if not response_relative:
        raise RuntimeError("engine did not allocate this handoff's response artifact")
    prompt_relative = str(prompt_path.relative_to(context.run_dir))
    handoff_relative = str(handoff_path.relative_to(context.run_dir))
    _write_once(prompt_path, exact_prompt)
    handoff = {
        "schema_version": 1,
        "workflow_id": context.mission.mission_id,
        "run_id": context.run_dir.name,
        "job_id": context.job.job_id,
        "role": context.job.role,
        "post_id": post_id,
        "stage": context.job.role,
        "next_stage": next_stage,
        "template_prompt_sha256": context.job_state.get("prompt_sha256"),
        "template_prompt_artifact": context.job.prompt_artifact,
        "prompt_to_paste": prompt_relative,
        "prompt_sha256": prompt_hash,
        "expected_response_artifact": response_relative,
        "inputs": [
            {
                "reference": record.get("reference"),
                "source_path": record.get("source_path"),
                "snapshot_path": record.get("snapshot_path"),
                "sha256": record.get("sha256"),
                "size_bytes": record.get("size_bytes"),
                "attachment_index": record.get("attachment_index"),
            }
            for record in context.input_records
        ],
        "expanded_source_inputs": _source_inputs_from_context(context),
        "input_renderings": input_renderings,
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    _write_once(handoff_path, json.dumps(handoff, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    context.update_progress(
        {
            "stage": context.job.role,
            "handoff_kind": "model_response",
            "handoff_json": handoff_relative,
            "prompt_to_paste": prompt_relative,
            "expected_response_artifact": response_relative,
            "post_id": post_id,
            "next_stage": next_stage,
        }
    )
    raise WaitingForHuman(
        f"Paste the saved prompt into Battle and ingest its response for {context.job.job_id}.",
        details={
            "stage": context.job.role,
            "handoff_kind": "model_response",
            "handoff_json": handoff_relative,
            "prompt_to_paste": prompt_relative,
            "expected_response_artifact": response_relative,
            "post_id": post_id,
            "next_stage": next_stage,
            "prompt_sha256": prompt_hash,
        },
    )


def execute_manual_handoff(context: JobContext) -> ExecutionResult:
    """Create a prompt-to-paste handoff, or transparently pass through a no-op gate."""
    role = context.job.role
    post_id = _post_id_from_job(context.job.job_id)
    if role == "validation_revision":
        if len(context.input_paths) < 3:
            raise RuntimeError("validation_revision requires a report, article, and evidence packet")
        report = _load_json_input(context.input_paths[0], "validator report")
        if report.get("valid") is True:
            passed = _conditional_result(context, report, context.input_paths[1])
            assert passed is not None
            return passed
    elif role == "cross_post_revision":
        if len(context.input_paths) < 3:
            raise RuntimeError("cross_post_revision requires a plan, article, and evidence packet")
        plan = _load_json_input(context.input_paths[0], "cross-post revision plan")
        by_post = {item.get("post_id"): item for item in plan.get("revisions", []) if isinstance(item, dict)}
        request = by_post.get(post_id or "", {"needed": False})
        if request.get("needed") is not True:
            passed = _conditional_result(context, request, context.input_paths[1])
            assert passed is not None
            return passed
    elif role in {"battle_writer_a", "battle_writer_b"}:
        return _write_handoff(context, post_id=post_id, next_stage="editorial_critic")
    elif role == "editorial_critic":
        return _write_handoff(context, post_id=post_id, next_stage="final_writer")
    elif role == "final_writer":
        return _write_handoff(context, post_id=post_id, next_stage="post_validator")
    elif role == "cross_post_editor":
        return _write_handoff(context, post_id=None, next_stage="cross_post_review_router")
    else:
        raise ValueError(f"unsupported manual post-production role: {role}")

    next_stage = "validation_revision_validator" if role == "validation_revision" else "cross_post_revision_validator"
    return _write_handoff(context, post_id=post_id, next_stage=next_stage)


def _build_validation_report(context: JobContext) -> ExecutionResult:
    if len(context.input_paths) < 2:
        raise RuntimeError("post_validator requires an article and its source evidence packet")
    post_id = _post_id_from_job(context.job.job_id)
    if post_id is None:
        raise RuntimeError(f"validator job id does not identify a post: {context.job.job_id}")
    article = _read_text(context.input_paths[0])
    packet = _read_text(context.input_paths[1])
    metadata = _packet_metadata(packet)
    report = validate_article(
        article,
        post_id,
        packet,
        expected_date=str(metadata.get("publication_date") or "2026-10-03"),
    )
    return ExecutionResult(
        response_text=_as_json(report),
        model_name="local:post-production-validator",
        metadata={"valid": report["valid"], "error_count": len(report["errors"]), "post_id": post_id},
    )


def _prepare_cross_post_packet(context: JobContext) -> ExecutionResult:
    sections = [
        "# Cross-post consistency packet",
        "",
        "The five articles below have passed their individual Jekyll/content validators. Compare them as one series; do not rewrite them here.",
        "The actual reference-post excerpts are included once. Evidence summaries and limitations are supplied per post so factual conflicts can be checked.",
        "",
    ]
    hashes: dict[str, str] = {}
    for index, (path, record) in enumerate(zip(context.input_paths, context.input_records), start=1):
        reference = str(record.get("reference", f"input:{index - 1}"))
        text = _read_text(path)
        sections.extend(
            [
                f"## BEGIN CROSS-POST INPUT {index:02d}: {reference}",
                f"Snapshot SHA-256: `{record.get('sha256', '')}`",
                "",
                text.rstrip(),
                "",
                f"## END CROSS-POST INPUT {index:02d}",
                "",
            ]
        )
        hashes[reference] = str(record.get("sha256", ""))
    source_metadata = {
        "source_input_records": [
            {
                key: record.get(key)
                for key in ("reference", "source_path", "snapshot_path", "sha256", "size_bytes", "attachment_index")
            }
            for record in context.input_records
        ]
    }
    sections.extend(
        [
            "<!-- POST_PRODUCTION_SOURCE_INPUT_METADATA",
            json.dumps(source_metadata, ensure_ascii=False, sort_keys=True),
            "-->",
            "",
        ]
    )
    return ExecutionResult(
        response_text="\n".join(sections),
        model_name="local:cross-post-packet-builder",
        metadata={"input_sha256": hashes, "input_count": len(context.input_records)},
    )


def _route_cross_post(context: JobContext) -> ExecutionResult:
    if not context.input_paths:
        raise RuntimeError("cross-post review router requires the editor response")
    normalized = _normalize_cross_review(_read_text(context.input_paths[0]))
    return ExecutionResult(
        response_text=_as_json(normalized),
        model_name="local:cross-post-review-router",
        metadata={"revision_count": sum(1 for item in normalized["revisions"] if item["needed"])},
    )


def _assemble_final_set(context: JobContext) -> ExecutionResult:
    artifacts: dict[str, dict[str, Any]] = {}
    for path, record in zip(context.input_paths, context.input_records):
        reference = str(record.get("reference", ""))
        match = re.match(r"job:(.+):response\Z", reference)
        if not match:
            continue
        upstream_id = match.group(1)
        post_id = _post_id_from_job(upstream_id)
        if not post_id:
            continue
        if "revision_validator" not in upstream_id:
            continue
        report = _load_json_input(path, f"final validation report for {post_id}")
        if report.get("valid") is not True:
            raise PostValidationError(f"{post_id} is not valid for export: {report.get('errors', [])}")
        article_job_id = upstream_id.replace("_revision_validator", "_revision")
        article_reference = f"job:{article_job_id}:response"
        article_path = None
        for candidate_path, candidate_record in zip(context.input_paths, context.input_records):
            if candidate_record.get("reference") == article_reference:
                article_path = candidate_path
                break
        if article_path is None:
            raise PostValidationError(f"final article artifact for {post_id} is missing")
        article_bytes = article_path.read_bytes()
        article = article_bytes.decode("utf-8-sig")
        frontmatter, _ = _extract_frontmatter(article)
        title = str(frontmatter["title"])
        post_date = report["date"]
        slug = report["slug"]
        artifacts[post_id] = {
            "post_id": post_id,
            "title": title,
            "date": post_date,
            "slug": slug,
            "suggested_jekyll_filename": f"{post_date}-{slug}.md",
            "article_sha256": hashlib.sha256(article_bytes).hexdigest(),
            "article_source_artifact": article_reference,
            "validation_report_artifact": reference,
            "word_count": report["word_count"],
            "evidence_trace_row_ids": report.get("trace_row_ids_loaded", []),
        }
    missing = sorted(set(POST_IDS) - set(artifacts))
    if missing:
        raise PostValidationError("cannot assemble final set; missing validated posts: " + ", ".join(missing))
    manifest = {
        "schema_version": 1,
        "workflow_id": context.mission.mission_id,
        "status": "validated_internal_export_manifest",
        "publication_is_optional": True,
        "posts": [artifacts[post_id] for post_id in POST_IDS],
        "source_run_id": context.run_dir.name,
    }
    return ExecutionResult(
        response_text=_as_json(manifest),
        model_name="local:final-post-set-assembler",
        metadata={"post_count": len(artifacts), "status": manifest["status"]},
    )


async def execute_local(context: JobContext) -> ExecutionResult:
    role = context.job.role
    if role == "prepare_post":
        return prepare_post_packet(context)
    if role in {"post_validator", "validation_revision_validator", "cross_post_revision_validator"}:
        return _build_validation_report(context)
    if role == "prepare_cross_post":
        return _prepare_cross_post_packet(context)
    if role == "cross_post_review_router":
        return _route_cross_post(context)
    if role == "final_post_set_assembler":
        return _assemble_final_set(context)
    raise ValueError(f"unsupported local post-production role: {role}")
