# THEORIST `P01-T` — Mission 01 Formal Brief

**Scope and provenance.** I worked only from the code evidence quoted in the mission brief. I did not check the repository myself. Any claim that depends on repo details I couldn't confirm is marked **[VERIFY]**. The only computations I ran are the EIG and gauge-survival numbers in §3 and §5.

**Three corrections to the seed, up front:**

1. **"Pairwise links look valid, yet there is no global section" cannot happen for a genuine sheaf if every pairwise overlap is checked exactly.** The sheaf gluing axiom only needs pairwise agreement. So the "3-way $\check H^1$ trap" only exists if one of three things is true:
   - only a spanning tree of edges is checked;
   - overlaps are compared *up to gauge*, meaning up to a convention choice (§1.4);
   - $T(X)$ contains a constraint that can't be split into local pieces (so $\mathcal F$ is not a sheaf).
2. **$\check H^1$ classifies how gauge choices are reconciled, not the sections themselves.** It needs a gauge group $\mathcal G$. A presheaf of "sets of implementations" has no $\check H^1$ as written.
3. **$P(\text{glue})=\prod_e g_e^{-1}$ only holds under two specific assumptions:** each interface carries its own convention, and agents choose uniformly and independently. Under any other assumption it is wrong (§3).

---

## 1. Formal Sheaf-Theoretic Framework (`P01-T-1`)

### 1.1 Base space and cover
- **$X$, the specification domain.** This is the set of *observation contexts* in which the spec makes a claim. Concretely, it is the set of triples (input, step index $t$, configuration).
  - Examples: $(p, g_{1:t}, t)$ for `compositional_optimizer`; $(s, a)$ pairs for `categorical_lenses`; (chunk schedule, positions) for `rope`.
- **$U_i \subseteq X$, the charts.** A chart is a subset of contexts that one test file or one module controls. Each chart is one of two kinds:
  - **Module chart:** the contexts whose observable output depends only on the code in module $i$, given an interface contract. Examples: $U_1$=`rope.py`, $U_2$=`attention.py`, $U_3$=`cache.py`.
  - **Evaluation chart:** the support of a judge test, $\operatorname{supp}(t)\subseteq X$. Examples: $\{t=1\}$, $\{T=1.0\}$, three fixed demand dicts.
- **$U_{ij}=U_i\cap U_j$, the overlaps.** An overlap is the set of contexts observed by *both* charts. For code, it is the interface: the call signature plus its semantic contract (e.g. the value `position_offset()` returns relative to `append`). For evaluation, it is a shared observable (e.g. optimizer state $v_1$ passed to step 2).
- **Nerve $N(\mathcal U)$.** Vertices are the charts $i$, edges are the non-empty $U_{ij}$, and 2-simplices are the non-empty $U_{ijk}$.
  - A **hollow triangle** has edges 12, 23, 31 with $U_{123}=\emptyset$. This is the *only* setting where Type I-C (§2) can appear with a constant gauge group.

### 1.2 Presheaves
- **$\mathcal C$, the artifact presheaf.** $\mathcal C(U)$ is the set of behaviours of candidate code, observed on $U$. Restriction is "observe only on $U$". $\mathcal C$ is a sheaf, because one program gives a consistent behaviour everywhere.
- **$\mathcal F\subseteq\mathcal C$, the spec sub-presheaf.** $\mathcal F(U_i)=\{s\in\mathcal C(U_i): s \text{ passes } T(U_i)\}$, where $T(U_i)$ is the ideal local test, i.e. the spec restricted to $U_i$.
- **$\mathcal F_J$, the judge presheaf.** It is defined by the tests that `judge.py` runs. A single artifact is accepted iff $\forall t\in J:\ s|_{\operatorname{supp}t}\in\mathcal F_J(\operatorname{supp}t)$.
- **$\rho_{ij}:\mathcal F(U_i)\to\mathcal C(U_{ij})$, the restriction maps.** $\rho_{ij}(s_i)$ is the behaviour of $s_i$ at the interface *as $s_i$ assumes it*. For `attention.py`, this is the meaning it gives to `cache.position_offset()`.

### 1.3 The 0-coboundary (edge defect)
For a tuple $\{s_i\}\in\prod_i\mathcal F(U_i)$:
$$\delta^0(\{s_i\})_{ij}=\rho_{ij}(s_i)\ominus\rho_{ji}(s_j)\in \mathcal C(U_{ij}).$$
Here $\ominus$ is subtraction wherever the interface values form a group: $\mathbb Z$ for offsets, $\mathbb R_{>0}$ for scalings, $S_n$ for permutations. Otherwise it is the indicator of inequality.

The global sections are the equalizer:
$$\mathcal F(X)\;\to\;\prod_i\mathcal F(U_i)\;\rightrightarrows\;\prod_{i<j}\mathcal C(U_{ij}),\qquad \mathcal F(X)=\ker\delta^0\quad\text{(if } \mathcal F \text{ is a sheaf on } \mathcal U).$$

### 1.4 Where $\check H^1$ enters: gauge torsors
**Gauge group.** Let $\mathcal G(U_i)$ be the group of transformations of $\mathcal C(U_i)$ that leave the local tests invariant, i.e. $T(U_i)$ cannot tell them apart. Examples:
- coordinate swap $\sigma\in\mathbb Z/2$ in lenses;
- the choice of RoPE pairing (adjacent vs. split-half) in $\mathbb Z/2$;
- integer offset shifts in $\mathbb Z$;
- positive rescalings in $\mathbb R_{>0}$.

So each local solution space is a union of $\mathcal G(U_i)$-orbits.

**Transition data.** Suppose a protocol checks edges *up to reconciliation*: on each edge it accepts $s_i|_{ij}= g_{ij}\cdot s_j|_{ij}$ for some adapter $g_{ij}\in\mathcal G(U_{ij})$.
- The data $\{g_{ij}\}$ is a Čech 1-cochain.
- On a triple overlap it must satisfy $g_{ij}g_{jk}g_{ki}=1$.
- A consistent global gauge exists iff $g_{ij}=h_ih_j^{-1}$ for some $h_i$, i.e. iff the cochain is a coboundary.

The obstruction is therefore:
$$[g]\in \check H^1(\mathcal U,\mathcal G),\qquad \text{hol}_{123}=g_{12}\,g_{23}\,g_{31}.$$

**On a hollow triangle with constant $\mathcal G$:**
$$\check H^1 \cong \operatorname{Hom}(\pi_1(N),\mathcal G)/\text{conj}\cong \mathcal G/\text{conj}.$$
- This is non-trivial whenever $\mathcal G\neq 1$.
- Each edge can look fine after its own adapter, yet the holonomy around the loop is $\neq 1$.
- If $U_{123}\neq\emptyset$, the cocycle condition forces $\text{hol}=1$ and there is no trap.

**Falsifiable structural claim.** Every claimed Type I-C instance must exhibit *both* of the following. Otherwise it should be reclassified as a plain $\delta^0$ edge defect.
- (a) an empty triple overlap;
- (b) a non-identity holonomy that can be computed.

### 1.5 Duality theorem (`P01-T-4`)
**Definitions.**
- A **protocol** $P$ is a set of constraints on artifacts or tuples. Each constraint is either a chart predicate $s|_{U}\in\mathcal F(U)$ or an edge predicate $\delta^0_{ij}=0$ (possibly only up to gauge).
- $\mathrm{Acc}(P)$ is the set of tuples or artifacts that satisfy $P$.
- **Defect set:** $D(P)=\mathrm{Acc}(P)\setminus\mathcal F(X)$, the accepted but globally invalid ones (Type I errors).
- **Rejection set:** $R(P)=\mathcal F(X)\setminus\mathrm{Acc}(P)$, the globally valid but rejected ones (Type II errors).

**Theorem (Dual A ≡ Dual B).** A judge $J$ and an orchestration protocol $O$ that impose *the same constraint set* have the same $D$ and the same $R$. The two duals differ only in the *quantifier* applied to $D$:
- **Dual A (evaluator blindness)** is the existential question: is $D(P_J)\neq\emptyset$? A constructed `law_bypass` patch is a witness $s\in D(P_J)$.
- **Dual B (swarm gluing failure)** is the measure question: what is $\mu_{\text{agents}}(D(P_O))/\mu_{\text{agents}}(\mathrm{Acc}(P_O))$, where $\mu$ is the distribution of agent outputs?

**Proof sketch.**
- *A single artifact restricts consistently.* For one artifact $s\in\mathcal C(X)$, the restrictions $s|_{U_i}$ automatically agree on overlaps, because $\mathcal C$ is a sheaf.
- *So a chart-only judge can only be blind in two ways.*
  - (i) $\bigcup_{t\in J}\operatorname{supp}(t)\subsetneq X$: the tests do not cover $X$. Example: $\{t=1\}$ in `compositional_optimizer`.
  - (ii) Membership in $\mathcal F$ is not local on the judge's cover. Example: the lens spec $\mathcal F=\mathcal F_{\text{laws}}\times_X\mathcal F_{\text{coord}}$ where $U_{\text{coord}}$ is never tested.
  - In both cases the judge accepts $\prod_{t}\mathcal F(\operatorname{supp}t)$ pulled back, which strictly contains $\mathcal F(X)$.
- *For $k$ agents, the tuple $\{s_i\}$ is not one artifact's restrictions.* Under Chart-Only, $\mathrm{Acc}=\prod_i\mathcal F(U_i)$ and $D=\prod_i\mathcal F(U_i)\setminus\ker\delta^0$. This is the same set difference as above, but with "omitted edge" in place of "omitted chart".
- *Hence the correspondence.* Missing charts or edges in $J$ correspond exactly to unconstrained interfaces in $O$. ∎

**Corollary (testable; this is H5 below).**
- The edges a judge leaves unchecked should be the same edges where swarms fail.
- An Overlap-Aware Grader B that enforces the $\rho_{ij}$ is the *same object* as the restriction-map orchestration spec. So "Grader B catches it" and "explicit $\rho_{ij}$ rescues it" should hold on the same edges.

---

## 2. Taxonomy of Gluing Obstructions (`P01-T-2`)

| Type | Formal signature | Instances (per brief) | Measurement instrument |
|---|---|---|---|
| **0: Pointwise sampling** *(new; kept separate deliberately)* | The judge's charts are finite point sets, so $\mathcal F_J(\{x_1..x_n\})$ can be satisfied by a lookup table. This is **not a gluing failure**: no overlaps are involved. | `stochastic_monad` (`right_identity=True`), `neuro_symbolic_parser` (2 strings), `monadic_reward` ($T=1.0$), `semiring_unification` (2 cells), and the lookup table in `sheaf_physical_constraints` | Lookup-table or hard-coded patch |
| **I-A: Temporal horizon truncation** | Cover failure: $\operatorname{supp}J=\{t=1\}\subsetneq X$. The missing edge is $U_{t}\cap U_{t+1}$ (state handoff). The defect is $\delta^0_{12}= v_1^{\text{carried}}\ominus v_1^{\text{expected}}$. | `compositional_optimizer`: the stateless `(1-β)·grad` equals EMA at $t=1$ (when $v_0=0$) and diverges for $t\ge2$. Probably also `rd_state_carry` **[VERIFY]**. | Roll out to $t\in\{2,\dots,5\}$ |
| **I-B: Unanchored gauge** | $\mathcal G(U)\neq1$ acts on $\mathcal F_J$ but not on $\mathcal F_{\text{spec}}$, so the judge accepts the whole orbit. In swarms this gives $\delta^0_{ij}\in\mathcal G\setminus\{1\}$ on one edge. | Lenses: $\sigma\in\mathbb Z/2$ swap. `rope`: pairing $\mathbb Z/2$. The `rope` pre/post-`append` offset is an **edge** defect valued in $\mathbb Z$ with value $+L$. It is I-B, not I-C, unless the edge check is missing **and** the cycle is hollow. | Apply each $g\in\mathcal G$ to the reference and check whether the judge still passes |
| **I-C: Hollow-cycle holonomy** | Hollow nerve triangle, edgewise adapters, $\text{hol}_{123}\neq1$, $[g]\neq0\in\check H^1(\mathcal U,\mathcal G)$ | Candidates: `sheaf_schema_sync` circular FKs ($\mathcal G=S_n$ key bijections; holonomy is the composite permutation). `sheaf_physical_constraints` 3-switch triangle ($\mathcal G=\mathbb R_{>0}$; holonomy is the product of scaling ratios). `rope` 3-module loop, **only if** `cache.py` talks to `rope.py` directly **[VERIFY]**. If it doesn't, the third edge is closed by the oracle `chunked_equals_full`, and the holonomy is just "chunked path vs. full path" $=+L$. | Compute $\text{hol}$ explicitly, and confirm $U_{123}=\emptyset$ |
| **II: Judge-anchored, spec-unanchored gauge** | The **transpose of I-B**. The judge picks one point in a $\mathcal G$-orbit (or polytope) that the spec leaves underdetermined. So $R(P_J)\neq\emptyset$. Note that $\mathcal F_J(X)\neq\emptyset$; the real statement is $\mathcal F_J(X)\cap\mathcal F^{\text{prop}}_{\text{spec}}(X)=\emptyset$. | `sheaf_physical_constraints` Check 2 (see the worked case below) | Grade a `reference_alt` from each convention |

**Worked case for Type II: `sheaf_physical_constraints` Check 2.** Demand is $A=120$, $B=60$, $C=0$, with a route cap of 100 on A and a switch constraint $A+B\le100$. Three allocations all satisfy every constraint:

| Convention | Allocation (A, B) | Ratio A/B | Judge Check 2 |
|---|---|---|---|
| Clamp, then scale | 62.5, 37.5 | 5/3 ≈ 1.667 | PASS |
| Joint proportional | 66.7, 33.3 | 2.000 | FAIL |
| Max-min fair | 50, 50 | 1.000 | FAIL |

Clamp-then-scale is just the ordering $\pi_{\text{switch}}\circ\pi_{\text{route}}$. The two projections don't commute, so the allocation depends on which order they are applied in.

**Classification rule for the seed's own claim.** Calling `sheaf_physical_constraints` an "inconsistent oracle presheaf" is only correct if `prompt.md` asks for proportional (or order-independent) allocation **[VERIFY]**. If the prompt says local caps are applied first, the judge is consistent. Type II is then false here, and only the Type 0 lookup-table bypass survives.

---

## 3. Sharpened Hypotheses & Predictions

**Metrics (pre-register these):**
- $\beta_A$ = (number of environments with a constructed $s\in D(P_J)$ that the judge scores 1.0 and Grader B fails) / $N$. Report it twice:
  - $\beta_A^{\text{glue}}$: Types I-A, I-B and I-C only;
  - $\beta_A^{\text{all}}$: also includes Type 0.
- $N$ must be fixed in advance: either all 35 environments, or the 22 `compile_only` ones. **With $N=22$, H1 needs 11 environments; with $N=35$ it needs 18.** By my count the brief already shows about 7 candidates, but only 2–3 of them (`compositional_optimizer`, `categorical_lenses`, possibly `rope`) are gluing failures, i.e. Type I rather than Type 0.
- $\varphi_{\text{chart}}$, $\varphi_{\text{tree}}$, $\varphi_{\text{pair}}$, $\varphi_{\text{gauge-adapt}}$, $\varphi_\rho$ = global failure rates among tuples that pass 100% of local tests, under each protocol.
- **`P01-T-5`: the seed's single "Pairwise-Only" protocol should be split into three.** They make different predictions:
  - **Pairwise-Tree:** checks only spanning-tree edges.
  - **Pairwise-Complete:** checks every edge exactly.
  - **Pairwise-UpToGauge:** each edge negotiates its own adapter.

**H0 (Null).** $\beta_A^{\text{glue}}<0.10$ and $\varphi_{\text{chart}}<0.10$.
- *Falsified by:* at least 4 out of 35 (or at least 3 out of 22) verified gluing-specific bypasses, *or* $\varphi_{\text{chart}}\ge0.10$ with a 95% CI that excludes 0.10. I expect `compositional_optimizer` and `categorical_lenses` already supply 2 of these.

**H1 (Evaluator gluing blindness).** $\beta_A^{\text{glue}}\ge0.50$, using **black-box** construction: the bypass is built from `prompt.md` and visible tests only, never from reading `judge.py`.
- *Prediction:* the bypasses concentrate in the 22 `compile_only` environments. Enrichment odds ratio vs. the 12 `REFERENCES` environments is >2.
- *Falsified by:* $\beta_A^{\text{glue}}<0.5$ even though $\beta_A^{\text{all}}\ge0.5$. That would mean the blindness is real but is mostly Type 0 sampling, not a sheaf effect.

**H2 (Judge Type II contradiction).** At least 2 environments have $D(P_J)\neq\emptyset$ **and** $R(P_J)\neq\emptyset$ at the same time, with an `R` witness that conforms to the prompt.
- *Prediction:* in $\mathcal G$-underdetermined tasks, the judge's pass rate on a `reference_alt` from each convention follows a 1/|conventions| pattern. For `sheaf_physical_constraints` that is 1 pass out of 3.
- *Falsified by:* every prompt names the judge's convention explicitly.

**H3 (Gluing obstruction plus restriction-map rescue).**
- **H3a:** $\varphi_{\text{chart}}>0.60$.
- **H3b:** $\varphi_{\text{pair-complete}}\approx\varphi_\rho$, while $\varphi_{\text{tree}},\varphi_{\text{gauge-adapt}}>\varphi_\rho$ *only on hollow-cycle tasks*.
- **H3c:** $\varphi_\rho<0.05$.

**Corrected gauge-survival formula (`P01-T-3`).** There are two models, depending on where the convention lives:

| Model | Survival probability |
|---|---|
| Edge-level conventions (each interface $e$ has $g_e$ conventions; both sides choose independently with distribution $p_e$) | $P(\text{glue})=\prod_{e\in E}\kappa_e$, where $\kappa_e=\sum_c p_{e,c}^2$ |
| Vertex-level gauge (each agent picks one global gauge from $\mathcal G$) | $P(\text{glue})=\prod_{e\in\text{tree}}\kappa_e$; cycle edges add nothing |

The seed's formula $\prod_e g_e^{-1}$ is the special case of uniform choice ($\kappa_e=1/g_e$), which is the *least favourable* case. In general, $\kappa_e\ge 1/g_e$.

| Scenario | $\varphi_{\text{chart}}=1-\prod\kappa_e$ |
|---|---|
| `rope`, 2 binary edges, uniform choice ($\kappa=0.5$) | 0.75 |
| 3 binary edges, uniform choice | 0.875 |
| 2 edges, dominant convention chosen 80% of the time ($\kappa=0.68$) | **0.54**, which is below H3a's threshold |
| 2 edges, $\kappa=0.9$ (convention strongly anchored by the existing skeleton) | 0.19 |

So H3a's ">60%" is a claim about how *spread out* agents' conventions are, not about topology. **H3c's <5% is a bound on bugs that have nothing to do with gauge.** Restriction maps cannot remove those, so the threshold should be judged against the rate of local test passes that are spurious.

**H4 (new: shared-prior collapse).** Agents' convention choices are strongly correlated because they share training priors and the existing code skeleton anchors them.
- *Prediction:* $\varphi_{\text{chart}}\approx1-\prod_e\hat\kappa_e$, where $\hat\kappa_e$ is measured from **solo single-agent runs**, accurate to ±0.1. The real value is far below the uniform-choice prediction except on genuinely bimodal conventions. RoPE adjacent vs. split-half pairing is plausibly one of those.
- *Separates from H3:* H3 predicts the uniform formula; H4 predicts the formula with empirical $\hat\kappa$.

**H5 (new: duality co-location, a corollary of §1.5).** Let $E_J$ be the edges whose omission produces the judge bypasses, and $E_O$ the edges with non-zero $\delta^0$ in swarm runs.
- *Prediction:* the Jaccard overlap of $E_J$ and $E_O$ is ≥ 0.7.
- *Falsified by:* swarms failing on edges the judge does check. That would mean the failures are not purely about which constraints are imposed, e.g. they come from agent capability limits.

---

## 4. Hidden Assumptions Register

| ID | Unstated premise | Risk if false |
|---|---|---|
| A01 | `prompt.md` determines $\mathcal F_{\text{spec}}(X)$ uniquely | H2 can't be judged; "valid" `reference_alt` becomes a matter of opinion |
| A02 | Judge test supports are *meant* to cover $X$ | I-A might be intentional scoping, not blindness |
| A03 | $\mathcal F$ is a sheaf on the chosen cover (no constraint is irreducibly global) | Failures blamed on $\check H^1$ are really non-local constraints; H3c's rescue fails |
| A04 | Code overlaps can be written down as interface contracts | Hidden channels (globals, mutable shared state, dtype) create unlisted edges |
| A05 | Agents choose conventions independently and uniformly | The seed formula is overstated (see H4) |
| A06 | Local tests are gauge-invariant | If they anchor the gauge, $\varphi_{\text{chart}}\to$ bug rate |
| A07 | The repo skeleton does not already fix the gauge (`rope` existing code) | Dual B disappears in debugging-style tasks |
| A08 | `law_bypass` is built black-box | White-box construction inflates $\beta_A$ and measures something else |
| A09 | Grader B is correct, i.e. has no Type II errors of its own | The auditor swaps one convention for another |
| A10 | The denominator for $\beta_A$ is fixed in advance (35 vs. 22 vs. 17) | Choosing it afterwards can push H1 over 50% |
| A11 | PASS ≡ score 1.0, with no partial credit | Thresholds shift if bypasses score 0.9 |
| A12 | The restriction-map condition adds structure, not just information | **Confound:** $\rho_{ij}$ specs add tokens. Needs an information-matched prose control (`P01-T-6`) |
| A13 | Every I-C instance has a hollow nerve, $U_{123}=\emptyset$ | Otherwise "H¹ trap" is really a $\delta^0$ edge defect |
| A14 | The 3-chart decomposition of single-file `sheaf/*` tasks is canonical | Čech $\check H^1$ depends on the cover, so results are about *our* cover, not the task |
| A15 | Judges are deterministic (seeds, $T$) | Stochastic charts blur pass/fail |
| A16 | `env_runner._submit` = the production judge path | Oracle-gate results may not carry over |
| A17 | `compile_only` means unvalidated, not wrong | H1 enrichment must not assume it |
| A18 | Each gauge class has non-empty $\mathcal F(U_i)$ | Otherwise conventions are forced, not chosen |
| A19 | Swarm agents don't see each other's code | Implicit coordination acts like partial $\rho_{ij}$ |

---

## 5. Decision Table

**Exclusivity.** H0–H5 are not mutually exclusive as stated; for example, H1 and H3 can both be true. For the table I recast H0–H4 as **"dominant mechanism"** hypotheses, meaning whichever one explains most of the measured failure, so that they are exclusive. H5 is a structural corollary and I test it separately.

**Observation regimes (exclusive and exhaustive):**
- **O1 (Null):** $\beta_A^{\text{glue}}<0.10$ and $\varphi_{\text{chart}}<0.10$.
- **O2 (Evaluator-dominant):** $\beta_A^{\text{glue}}\ge0.50$ and $\varphi_{\text{chart}}\le0.60$.
- **O3 (Sheaf-orchestration with rescue):** $\varphi_{\text{chart}}>0.60$ and $\varphi_\rho<0.05$.
- **O4 (Residual):** everything else, including rescue failure and intermediate $\beta_A$.

| | Prior | O1 | O2 | O3 | O4 |
|---|---|---|---|---|---|
| H0 | 0.10 | very_high 0.70 | very_low 0.05 | very_low 0.05 | low 0.20 |
| H1 | 0.35 | very_low 0.03 | very_high 0.60 | low 0.12 | moderate 0.25 |
| H2 | 0.10 | low 0.15 | moderate 0.25 | low 0.10 | high 0.50 |
| H3 | 0.25 | very_low 0.02 | very_low 0.08 | very_high 0.60 | moderate 0.30 |
| H4 | 0.20 | low 0.20 | high 0.45 | very_low 0.03 | moderate 0.32 |

**Why these priors.** H1 is the highest because there are already 2–3 confirmed gluing bypasses plus about 4 Type 0 ones. The real uncertainty is the denominator and how Type 0 is classified. H3 is lower because debugging tasks come with skeletons that anchor the gauge (A07), and that favours H4.

**EIG (computed).**
- Prior entropy: 2.159 bits. Marginal $P(O)=(0.14,\,0.35,\,0.21,\,0.30)$.
- **EIG of the O-experiment: 0.44 bits.**
- Posteriors given O2: H1 0.60 and H4 0.26. **The main experiment cannot tell H1 from H4.**

**Proposals to close the gap:**
- **`P01-T-7`:** add a solo-run $\hat\kappa_e$ measurement (O5). On its own it gives 0.20 bits, mainly by separating H3 from H4.
- **`P01-T-8`:** add a `reference_alt` convention sweep (O6). This targets H2, which the O-regimes barely detect.
- Running all three together gives an EIG of about **0.67 bits**, roughly 1.5× the main experiment alone.

**Additional instrument (`P01-T-9`).** For `rope`, record the integer $\text{hol}=\text{pos}_{\text{chunked}}-\text{pos}_{\text{full}}$ for each chunk, rather than a boolean pass/fail. Prediction:
- $\text{hol}\in\{0,+L\}$ under binary edge conventions;
- $\text{hol}=+L$ exactly in the pre/post-`append` mismatch case.

This turns the cohomology class into a single number that can be measured directly, and it separates edge defects (a constant shift) from pairing defects (a rotation that depends on dimension).

**Priority [VERIFY] items:**
1. Whether `sheaf_physical_constraints/prompt.md` specifies an allocation convention (this decides Type II).
2. Whether `cache.py` and `rope.py` interact directly (this decides whether `rope` is I-C or only I-B).
3. Whether the `rope` skeleton already fixes pairing and offset semantics (this decides H3 vs. H4).
