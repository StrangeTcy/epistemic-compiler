# Initial Code Snippets Proposal v2 — critique-responsive

**Target:** `rl_eval_generator`, a separate repository.
**Status:** local proposal draft, not implemented or tested against the target checkout. Target module locations below follow the linked critique as suggestions; confirm them in the actual checkout before implementation.

**Revision basis:** the final “Hostile technical review — Mission 02 implementation hooks” section of [`code snippets critique.md`](https://github.com/StrangeTcy/epistemic-compiler/blob/arena/01a107c8-epistemic-compiler/mission-02/code%20snippets%20critique.md). This v2 replaces v1’s toy helpers with exact semantic cores, explicit generation/verification boundaries, and falsifiable tests. The v1 file remains as history; it should not be used as an implementation plan.

**Portfolio boundary:** E1–E8, S1–S4, and V1–V3 remain separate questions. T1 is an additional, separate research line. The S2 endpoint remains the effect of trigger-matched versus yoked strategy cards; matcher confusion is only a supporting validity check, not a substitute S2 question. No single score or capability ladder is proposed.

**Repository-claim boundary:** the critique reports existing exact Bayesian semantics and specific generator/runner seams. This draft does not independently verify those claims in the `rl_eval_generator` checkout. In particular, factor or extend existing exact semantics rather than adding a competing implementation.

The code fences are module fragments, not one concatenated module. Import the shared exact types (`FiniteDist`, `SpecError`, `exact_fraction`) into dependent modules; add local standard-library imports as needed. The code is intended to make semantics and failure conditions explicit, not to claim the proposed module paths already exist.

## Separation of concerns and interpretation boundary

Keep these stages as separate interfaces and artifacts: the **generator** samples a frozen instance from a seed/spec and records both; the **semantic oracle** computes the exact answer from that instance; the **renderer** exposes only the public instance fields; the **scorer** applies a frozen response/rubric contract; and **validation** checks schemas, leakage, split integrity, and oracle disagreement. Do not let the renderer read hidden oracle output, or let the scorer silently regenerate/correct an instance. Record the rendered prompt and scoring input separately from the oracle result.

All outcomes in this proposal concern observable responses under specified prompts and scoring rules. Agreement with a formal prediction does not identify a solver’s hidden mechanism, and failures on one family do not establish a general capability boundary.

## Shared exact arithmetic

**Suggested home:** `shared/epistemic_semantics/bayes.py` (proposed path).

Categorical decisions use `Fraction`; floats are reserved for display and post-hoc statistics. The distribution object rejects float inputs so a caller cannot silently smuggle binary floating-point values into a supposedly exact oracle.

```python
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from types import MappingProxyType
from typing import Generic, Hashable, Mapping, TypeVar

K = TypeVar("K", bound=Hashable)


class SpecError(ValueError):
    pass


def exact_fraction(value: Fraction | int | str) -> Fraction:
    if isinstance(value, (float, bool)):
        raise SpecError("use an exact Fraction, integer, or p/q string")
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise SpecError(f"invalid exact rational: {value!r}") from exc


@dataclass(frozen=True)
class FiniteDist(Generic[K]):
    mass: Mapping[K, Fraction]

    def __post_init__(self) -> None:
        copied = {key: exact_fraction(value) for key, value in self.mass.items()}
        if not copied:
            raise SpecError("empty distribution")
        if any(value < 0 for value in copied.values()):
            raise SpecError("negative probability mass")
        if sum(copied.values(), Fraction(0)) != 1:
            raise SpecError("probability mass must sum exactly to 1")
        object.__setattr__(self, "mass", MappingProxyType(copied))

    def __getitem__(self, key: K) -> Fraction:
        return self.mass[key]
```

**Falsification tests:** reject float input; reject negative mass and a sum other than exactly one; retain exact results at a likelihood-ratio boundary such as 3; catch transposed likelihoods with an asymmetric prior.

## E — Epistemic-reasoning questions

### E1 — Supplied-policy Bayesian updating

E1 asks whether a solver’s reported posterior tracks the correct posterior when behavioral policies are supplied as common knowledge. The code below is the exact reference calculation, **not** evidence that the solver internally used Bayes. Factor this into the existing core if the critique’s repository description is confirmed; do not add a parallel float implementation.

```python
from dataclasses import dataclass
from fractions import Fraction
from types import MappingProxyType
from typing import Mapping

from .bayes import FiniteDist, SpecError, exact_fraction


@dataclass(frozen=True)
class SuppliedPolicyInstance:
    prior: FiniteDist[str]
    likelihood: Mapping[str, Fraction]  # world -> P(observed event | world)
    observation_label: str

    def __post_init__(self) -> None:
        likelihood = {
            world: exact_fraction(value)
            for world, value in self.likelihood.items()
        }
        if set(likelihood) != set(self.prior.mass):
            raise SpecError("likelihood worlds must match prior worlds")
        if any(value < 0 or value > 1 for value in likelihood.values()):
            raise SpecError("likelihood must lie in [0, 1]")
        object.__setattr__(self, "likelihood", MappingProxyType(likelihood))

    def posterior(self) -> FiniteDist[str]:
        unnormalized = {
            world: self.prior[world] * self.likelihood[world]
            for world in self.prior.mass
        }
        evidence = sum(unnormalized.values(), Fraction(0))
        if evidence == 0:
            raise SpecError("observation has zero probability under every world")
        return FiniteDist({world: mass / evidence for world, mass in unnormalized.items()})

    def likelihood_ratio(self) -> Fraction | None:
        values = tuple(self.likelihood.values())
        low, high = min(values), max(values)
        if low == high:
            return Fraction(1)
        if low == 0:
            return None  # infinite ratio; do not encode it as a float
        return high / low
```

**Required tests:** exact boundary `3/10 ÷ 1/10 == 3`; asymmetric-prior posterior fixture; impossible observation rejection. The oracle’s output and a solver’s response must be stored as different fields.

### E2 — Sequential public announcements

A world-set filter alone is not a public-announcement update. The model must restrict both the worlds and every agent’s accessibility partition.

```python
from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Callable, Iterable, Mapping, Sequence

from .bayes import SpecError


@dataclass(frozen=True)
class S5Model:
    worlds: frozenset[str]
    agents: tuple[str, ...]
    partition: Mapping[str, tuple[frozenset[str], ...]]
    valuation: Mapping[str, frozenset[str]]

    def __post_init__(self) -> None:
        worlds = frozenset(self.worlds)
        agents = tuple(self.agents)
        partition = {
            agent: tuple(frozenset(cell) for cell in cells)
            for agent, cells in self.partition.items()
        }
        valuation = {world: frozenset(props) for world, props in self.valuation.items()}
        object.__setattr__(self, "worlds", worlds)
        object.__setattr__(self, "agents", agents)
        object.__setattr__(self, "partition", MappingProxyType(partition))
        object.__setattr__(self, "valuation", MappingProxyType(valuation))
        if not worlds or not agents or len(set(agents)) != len(agents):
            raise SpecError("S5 model needs worlds and unique agents")
        if set(partition) != set(agents):
            raise SpecError("every agent needs exactly one partition")
        if set(valuation) != set(worlds):
            raise SpecError("valuation must cover exactly the model worlds")
        for agent, cells in partition.items():
            if any(not cell or not cell <= worlds for cell in cells):
                raise SpecError(f"invalid partition cell for {agent}")
            union = frozenset().union(*cells) if cells else frozenset()
            total_size = sum(len(cell) for cell in cells)
            if union != worlds or total_size != len(worlds):
                raise SpecError(f"cells for {agent} do not partition the worlds")

    def cell(self, agent: str, world: str) -> frozenset[str]:
        for cell in self.partition[agent]:
            if world in cell:
                return cell
        raise KeyError((agent, world))

    def knows(self, agent: str, world: str, phi: Callable[[S5Model, str], bool]) -> bool:
        return all(phi(self, alternative) for alternative in self.cell(agent, world))

    def announce(self, phi: Callable[[S5Model, str], bool]) -> S5Model:
        kept = frozenset(world for world in self.worlds if phi(self, world))
        if not kept:
            raise SpecError("announcement eliminates every possible world")
        refined = {
            agent: tuple(cell & kept for cell in cells if cell & kept)
            for agent, cells in self.partition.items()
        }
        return S5Model(
            worlds=kept,
            agents=self.agents,
            partition=refined,
            valuation={world: self.valuation[world] for world in kept},
        )


def announce_sequence(
    model: S5Model, announcements: Sequence[Callable[[S5Model, str], bool]]
) -> S5Model:
    for announcement in announcements:
        model = model.announce(announcement)
    return model
```

**Required test:** an agent initially cannot distinguish a `p` world from a `not-p` world; after public announcement of `p`, the agent knows `p` while the actual world’s valuation is unchanged. Also test sequential composition and rejection of an announcement that removes all worlds.

**Status:** implement after the S5/public-announcement fragment is frozen; probabilistic updates are a separate extension.

### E3 — Information carried by silence

Silence is evidence only relative to a stipulated, common-knowledge speech policy. Build matched informative/uninformative policies; do not infer a policy from the silence itself.

```python
from dataclasses import dataclass
from fractions import Fraction
from types import MappingProxyType
from typing import Mapping

from .bayes import FiniteDist, SpecError


@dataclass(frozen=True)
class SpeechPolicy:
    messages: tuple[str, ...]
    table: Mapping[str, FiniteDist[str]]  # world -> distribution over messages

    def __post_init__(self) -> None:
        messages = tuple(self.messages)
        table = MappingProxyType(dict(self.table))
        object.__setattr__(self, "messages", messages)
        object.__setattr__(self, "table", table)
        if not table or not messages or "silent" not in messages:
            raise SpecError("speech policy needs worlds and an explicit silent message")
        if len(set(self.messages)) != len(self.messages):
            raise SpecError("speech message names must be unique")
        if any(set(row.mass) != set(self.messages) for row in self.table.values()):
            raise SpecError("each world must use the same declared message set")


def posterior_given_message(
    prior: FiniteDist[str], policy: SpeechPolicy, message: str
) -> FiniteDist[str]:
    if set(prior.mass) != set(policy.table):
        raise SpecError("prior and speech-policy worlds must match")
    unnormalized = {
        world: prior[world] * policy.table[world].mass.get(message, Fraction(0))
        for world in prior.mass
    }
    evidence = sum(unnormalized.values(), Fraction(0))
    if evidence == 0:
        raise SpecError(f"message {message!r} has zero probability")
    return FiniteDist({world: value / evidence for world, value in unnormalized.items()})


def make_silence_pair(
    prior: FiniteDist[str], informative: SpeechPolicy, control: SpeechPolicy
) -> tuple[SpeechPolicy, SpeechPolicy]:
    if dict(posterior_given_message(prior, informative, "silent").mass) == dict(prior.mass):
        raise SpecError("informative arm does not change the exact posterior")
    if dict(posterior_given_message(prior, control, "silent").mass) != dict(prior.mass):
        raise SpecError("control silence is informative")
    return informative, control
```

**Required tests:** swap the informative/control labels and require failure; use an uninformative policy with identical message probabilities in every world; reject missing or impossible silence events.

### E4 — Nested knowledge

The formula is an AST evaluated against E2’s partition model. A string such as `K_a K_b p` is not itself an epistemic computation.

```python
from __future__ import annotations

from dataclasses import dataclass

from .bayes import SpecError
from .s5_pal import S5Model


@dataclass(frozen=True)
class Atom:
    name: str


@dataclass(frozen=True)
class Not:
    child: Formula


@dataclass(frozen=True)
class And:
    left: Formula
    right: Formula


@dataclass(frozen=True)
class K:
    agent: str
    child: Formula


Formula = Atom | Not | And | K


def holds(model: S5Model, world: str, formula: Formula) -> bool:
    if isinstance(formula, Atom):
        return formula.name in model.valuation[world]
    if isinstance(formula, Not):
        return not holds(model, world, formula.child)
    if isinstance(formula, And):
        return holds(model, world, formula.left) and holds(model, world, formula.right)
    if isinstance(formula, K):
        return all(holds(model, other, formula.child) for other in model.cell(formula.agent, world))
    raise TypeError(formula)


def modal_depth(formula: Formula) -> int:
    if isinstance(formula, Atom):
        return 0
    if isinstance(formula, Not):
        return modal_depth(formula.child)
    if isinstance(formula, And):
        return max(modal_depth(formula.left), modal_depth(formula.right))
    return 1 + modal_depth(formula.child)


def depth_discrimination_certificate(model: S5Model, world: str, formula: Formula) -> dict:
    if not isinstance(formula, K):
        raise SpecError("certificate currently requires an outermost knowledge operator")
    full = holds(model, world, formula)
    truncated = holds(model, world, formula.child)
    if full == truncated:
        raise SpecError("shallow truncation preserves the answer; reject this instance")
    return {"modal_depth": modal_depth(formula), "full": full, "truncated": truncated}
```

**Required test:** a deliberately shallow-solvable instance must fail certification; a depth-discriminating instance must flip truth under the declared truncation. Report behavioral consistency only—not that a solver “is” a level-k or higher-order reasoner.

**Status:** after E2’s logic fragment is fixed.

### E5 — Asymmetric or fragmented observation

Observation is per agent. The rendering must receive only the probed agent’s signal, while the oracle retains all signals.

```python
from dataclasses import dataclass
from fractions import Fraction
from types import MappingProxyType
from typing import Mapping

from .bayes import FiniteDist, SpecError


@dataclass(frozen=True)
class PrivateSignalModel:
    prior: FiniteDist[str]
    likelihood: Mapping[str, Mapping[str, FiniteDist[str]]]  # agent -> world -> signal distribution

    def __post_init__(self) -> None:
        likelihood = MappingProxyType({
            agent: MappingProxyType(dict(by_world))
            for agent, by_world in self.likelihood.items()
        })
        object.__setattr__(self, "likelihood", likelihood)
        if not likelihood:
            raise SpecError("at least one agent signal model is required")
        for agent, by_world in likelihood.items():
            if set(by_world) != set(self.prior.mass):
                raise SpecError(f"{agent}: signal rows must cover exactly the prior worlds")
            if any(not row.mass for row in by_world.values()):
                raise SpecError(f"{agent}: empty signal distribution")

    def posterior_for(self, agent: str, signal: str) -> FiniteDist[str]:
        if agent not in self.likelihood:
            raise SpecError(f"unknown agent: {agent}")
        unnormalized = {
            world: self.prior[world]
            * self.likelihood[agent][world].mass.get(signal, Fraction(0))
            for world in self.prior.mass
        }
        evidence = sum(unnormalized.values(), Fraction(0))
        if evidence == 0:
            raise SpecError("signal impossible for this agent")
        return FiniteDist({world: value / evidence for world, value in unnormalized.items()})


def asymmetry_certificate(model: PrivateSignalModel, a: str, b: str, signal_a: str, signal_b: str) -> dict:
    posterior_a = model.posterior_for(a, signal_a)
    posterior_b = model.posterior_for(b, signal_b)
    if dict(posterior_a.mass) == dict(posterior_b.mass):
        raise SpecError("posteriors are equal; instance is not asymmetric")
    return {"posterior_a": dict(posterior_a.mass), "posterior_b": dict(posterior_b.mass)}


def viewpoint_packet(agent: str, own_signal: str, public_text: str) -> dict[str, str]:
    return {"perspective": agent, "own_signal": own_signal, "public_text": public_text}
```

**Required tests:** asymmetry certificate rejects symmetric cases; the packet builder has no parameter through which another agent’s private signal can leak. Add an explicit perspective object if the target API needs richer agent identity.

**Status:** after signal semantics and probe templates are specified.

### E6 — Finite type spaces, common priors, and BNE

A best-response checker is not a ground-truth generator. The bounded enumerator below searches pure strategies using exact expected utilities, rejects oversized spaces, and requires a unique equilibrium for single-answer items.

```python
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import prod
from types import MappingProxyType
from typing import Mapping

from .bayes import FiniteDist, SpecError, exact_fraction


@dataclass(frozen=True)
class FiniteBayesianGame:
    players: tuple[str, ...]
    types: Mapping[str, tuple[str, ...]]
    actions: Mapping[str, tuple[str, ...]]
    common_prior: FiniteDist[tuple[str, ...]]
    utility: Mapping[str, Mapping[tuple[tuple[str, ...], tuple[str, ...]], Fraction]]

    def __post_init__(self) -> None:
        if not self.players or len(set(self.players)) != len(self.players):
            raise SpecError("players must be non-empty and unique")
        if set(self.types) != set(self.players) or set(self.actions) != set(self.players):
            raise SpecError("types and actions must be defined for every player")
        if set(self.utility) != set(self.players):
            raise SpecError("utilities must be defined for every player")
        if any(
            not self.types[p] or len(set(self.types[p])) != len(self.types[p])
            or not self.actions[p] or len(set(self.actions[p])) != len(self.actions[p])
            for p in self.players
        ):
            raise SpecError("every player needs unique types and actions")
        for type_profile in self.common_prior.mass:
            if len(type_profile) != len(self.players):
                raise SpecError("type-profile arity does not match players")
            if any(type_profile[i] not in self.types[player]
                   for i, player in enumerate(self.players)):
                raise SpecError("prior contains an undeclared type")
        for index, player in enumerate(self.players):
            for player_type in self.types[player]:
                marginal = sum(
                    probability for profile, probability in self.common_prior.mass.items()
                    if profile[index] == player_type
                )
                if marginal == 0:
                    raise SpecError(f"zero-prior type: {player}:{player_type}")
        action_profiles = tuple(product(*(self.actions[player] for player in self.players)))
        expected_keys = {
            (type_profile, action_profile)
            for type_profile in self.common_prior.mass
            for action_profile in action_profiles
        }
        normalized = {}
        for player in self.players:
            if set(self.utility[player]) != expected_keys:
                raise SpecError(f"{player}: utility table has missing or extra state/action rows")
            normalized[player] = MappingProxyType({
                key: exact_fraction(value) for key, value in self.utility[player].items()
            })
        object.__setattr__(self, "utility", MappingProxyType(normalized))


Strategy = Mapping[str, Mapping[str, str]]  # player -> type -> action


def interim_eu(game: FiniteBayesianGame, player: str, strategy: Strategy, player_type: str, action: str) -> Fraction:
    player_index = game.players.index(player)
    numerator = Fraction(0)
    denominator = Fraction(0)
    for type_profile, probability in game.common_prior.mass.items():
        if type_profile[player_index] != player_type or probability == 0:
            continue
        action_profile = tuple(
            action if other == player
            else strategy[other][type_profile[game.players.index(other)]]
            for other in game.players
        )
        numerator += probability * game.utility[player][(type_profile, action_profile)]
        denominator += probability
    if denominator == 0:
        raise SpecError(f"zero-prior type: {player}:{player_type}")
    return numerator / denominator


def is_pure_bne(game: FiniteBayesianGame, strategy: Strategy) -> bool:
    if set(strategy) != set(game.players):
        raise SpecError("strategy must define every player")
    for player in game.players:
        if set(strategy[player]) != set(game.types[player]):
            raise SpecError(f"strategy must define every type of {player}")
        if any(action not in game.actions[player] for action in strategy[player].values()):
            raise SpecError(f"strategy uses undeclared action for {player}")
    for player in game.players:
        for player_type in game.types[player]:
            chosen = strategy[player][player_type]
            chosen_value = interim_eu(game, player, strategy, player_type, chosen)
            if any(
                interim_eu(game, player, strategy, player_type, alternative) > chosen_value
                for alternative in game.actions[player]
            ):
                return False
    return True


def enumerate_pure_bne(game: FiniteBayesianGame, *, cap: int = 20_000) -> list[dict[str, dict[str, str]]]:
    slots = [(player, player_type) for player in game.players for player_type in game.types[player]]
    size = prod(len(game.actions[player]) for player, _ in slots)
    if size > cap:
        raise SpecError(f"strategy space {size} exceeds cap {cap}")
    equilibria = []
    for chosen_actions in product(*(game.actions[player] for player, _ in slots)):
        strategy = {player: {} for player in game.players}
        for (player, player_type), action in zip(slots, chosen_actions):
            strategy[player][player_type] = action
        if is_pure_bne(game, strategy):
            equilibria.append(strategy)
    return equilibria


def unique_pure_bne_or_reject(game: FiniteBayesianGame) -> dict[str, dict[str, str]]:
    equilibria = enumerate_pure_bne(game)
    if len(equilibria) != 1:
        raise SpecError(f"expected one pure BNE, found {len(equilibria)}")
    return equilibria[0]
```

**Required tests:** hand-verified unique-BNE fixture, exact-indifference fixture, deviation that invalidates a candidate profile, and a strategy-space cap test. The enumerator is the oracle for tiny generated games; a checker alone is not.

### E7 — Level-k versus competing solution concepts

Predictions are computed from an explicit serialized level-0 anchor and the E6 game. Ties are rejected rather than silently resolved by mapping order.

```python
from typing import Mapping

from .bayes import SpecError
from .bayesian_games import (
    FiniteBayesianGame, Strategy, interim_eu, unique_pure_bne_or_reject,
)


def validate_level0(game: FiniteBayesianGame, level0: Strategy) -> None:
    if set(level0) != set(game.players):
        raise SpecError("level-0 anchor must define every player")
    for player in game.players:
        if set(level0[player]) != set(game.types[player]):
            raise SpecError(f"level-0 anchor must define every type of {player}")
        if any(action not in game.actions[player] for action in level0[player].values()):
            raise SpecError(f"level-0 anchor uses an undeclared action for {player}")


def level_k_strategy(game: FiniteBayesianGame, player: str, k: int, level0: Strategy) -> dict[str, str]:
    validate_level0(game, level0)
    if player not in game.players:
        raise SpecError(f"unknown player: {player}")
    if k < 0:
        raise SpecError("k must be non-negative")
    if k == 0:
        return dict(level0[player])  # explicit modeling choice; serialize it with the instance
    previous = {other: level_k_strategy(game, other, k - 1, level0) for other in game.players}
    result = {}
    for player_type in game.types[player]:
        values = {
            action: interim_eu(game, player, previous, player_type, action)
            for action in game.actions[player]
        }
        best = max(values.values())
        winners = [action for action, value in values.items() if value == best]
        if len(winners) != 1:
            raise SpecError("exact best-response tie; reject or preregister a tie policy")
        result[player_type] = winners[0]
    return result


def candidate_predictions(
    game: FiniteBayesianGame, level0: Strategy, levels: tuple[int, ...]
) -> dict[str, object]:
    predictions: dict[str, object] = {
        "unique_pure_bne": unique_pure_bne_or_reject(game)
    }
    for k in levels:
        if k < 1:
            raise SpecError("compare positive levels against the explicit level-0 anchor")
        predictions[f"level_{k}"] = {
            player: level_k_strategy(game, player, k, level0)
            for player in game.players
        }
    return predictions


def divergence_certificate(predictions: Mapping[str, object]) -> dict:
    names = tuple(predictions)
    divergent = [
        (left, right)
        for index, left in enumerate(names)
        for right in names[index + 1:]
        if predictions[left] != predictions[right]
    ]
    if not divergent:
        raise SpecError("candidate concepts agree; instance does not discriminate")
    return {"prediction_disagreements": divergent}
```

**Required tests:** a hand-verified game where level 1 and level 2 differ; exact-tie rejection; no mechanism inference from an answer’s agreement with a prediction.

**Status:** after E6 and the level-0 anchor contract are frozen.

### E8 — Signaling-game beliefs and actions

PBE needs on-path Bayes consistency, receiver sequential rationality, sender sequential rationality, and an explicit off-path belief rule/grid. A receiver best-response check alone is insufficient.

```python
from dataclasses import dataclass
from fractions import Fraction
from types import MappingProxyType
from typing import Mapping

from .bayes import FiniteDist, SpecError, exact_fraction


@dataclass(frozen=True)
class SignalingGame:
    types: tuple[str, ...]
    messages: tuple[str, ...]
    responses: tuple[str, ...]
    prior: FiniteDist[str]
    sender_utility: Mapping[tuple[str, str, str], Fraction]  # type, message, response
    receiver_utility: Mapping[tuple[str, str, str], Fraction]

    def __post_init__(self) -> None:
        for name, values in (("types", self.types), ("messages", self.messages), ("responses", self.responses)):
            if not values or len(set(values)) != len(values):
                raise SpecError(f"{name} must be non-empty and unique")
        if set(self.prior.mass) != set(self.types):
            raise SpecError("prior must cover exactly the declared types")
        expected = {
            (player_type, message, response)
            for player_type in self.types
            for message in self.messages
            for response in self.responses
        }
        if set(self.sender_utility) != expected or set(self.receiver_utility) != expected:
            raise SpecError("both utility tables must cover every type/message/response tuple")
        object.__setattr__(self, "sender_utility", MappingProxyType({
            key: exact_fraction(value) for key, value in self.sender_utility.items()
        }))
        object.__setattr__(self, "receiver_utility", MappingProxyType({
            key: exact_fraction(value) for key, value in self.receiver_utility.items()
        }))


@dataclass(frozen=True)
class Assessment:
    sender: Mapping[str, str]               # type -> message
    receiver: Mapping[str, str]             # message -> response
    beliefs: Mapping[str, FiniteDist[str]]  # message -> belief over types
    off_path_grid_id: str                   # key into a frozen, declared grid registry


def on_path_bayes_consistent(game: SignalingGame, assessment: Assessment) -> bool:
    if set(assessment.sender) != set(game.types):
        return False
    if set(assessment.receiver) != set(game.messages):
        return False
    if set(assessment.beliefs) != set(game.messages):
        return False
    for belief in assessment.beliefs.values():
        if set(belief.mass) != set(game.types):
            return False
    for message in game.messages:
        senders = [t for t in game.types if assessment.sender[t] == message]
        mass = sum((game.prior[t] for t in senders), Fraction(0))
        if mass == 0:  # off-path beliefs are checked against the declared grid below
            continue
        expected = FiniteDist({
            t: (game.prior[t] / mass if t in senders else Fraction(0))
            for t in game.types
        })
        if dict(expected.mass) != dict(assessment.beliefs[message].mass):
            return False
    return True


def is_pbe(
    game: SignalingGame,
    assessment: Assessment,
    off_path_grids: Mapping[str, Mapping[str, FiniteDist[str]]],
) -> bool:
    if set(assessment.sender) != set(game.types) or set(assessment.receiver) != set(game.messages):
        return False
    if any(message not in game.messages for message in assessment.sender.values()):
        return False
    if any(response not in game.responses for response in assessment.receiver.values()):
        return False
    if set(assessment.beliefs) != set(game.messages) or not assessment.off_path_grid_id:
        return False
    if assessment.off_path_grid_id not in off_path_grids:
        return False
    grid = off_path_grids[assessment.off_path_grid_id]
    if set(grid) != set(game.messages):
        return False
    if any(set(belief.mass) != set(game.types) for belief in grid.values()):
        return False
    if not on_path_bayes_consistent(game, assessment):
        return False

    for message in game.messages:
        if not any(assessment.sender[t] == message and game.prior[t] > 0 for t in game.types):
            if dict(assessment.beliefs[message].mass) != dict(grid[message].mass):
                return False
        belief = assessment.beliefs[message]
        expected_receiver_utility = lambda response: sum(
            (belief[t] * game.receiver_utility[(t, message, response)] for t in game.types),
            Fraction(0),
        )
        if expected_receiver_utility(assessment.receiver[message]) < max(
            expected_receiver_utility(response) for response in game.responses
        ):
            return False

    for player_type in game.types:
        sender_utility = lambda message: game.sender_utility[
            (player_type, message, assessment.receiver[message])
        ]
        if sender_utility(assessment.sender[player_type]) < max(
            sender_utility(message) for message in game.messages
        ):
            return False
    return True
```

**Required tests:** a beer–quiche-style assessment where the receiver best-responds but a sender type deviates; on-path belief mismatch; and a fixture where changing the recorded off-path grid changes the equilibrium set. The exhaustive enumerator remains gated on a frozen off-path policy and a candidate-space cap.

**Status:** needs an explicit off-path belief specification and an independent tiny-game oracle before dataset generation.

## S — Strategy-pack questions

### S1 — Card content versus generic advice

Arms are prompt-assembly objects tied to the same semantic instance. Content hashes protect frozen arms; answer leakage is an apparatus failure. Token-length matching must use the target’s declared tokenizer, not word count.

```python
from dataclasses import dataclass
from hashlib import sha256
from typing import Iterable, Literal

from shared.epistemic_semantics.bayes import SpecError
from shared.epistemic_semantics.leakage import leakage_hits


@dataclass(frozen=True)
class AdviceArm:
    arm_id: Literal["card", "generic", "none"]
    semantic_instance_id: str
    advice_text: str
    content_sha256: str
    token_count: int

    def __post_init__(self) -> None:
        actual = sha256(self.advice_text.encode("utf-8")).hexdigest()
        if self.content_sha256 != actual:
            raise SpecError("advice content hash does not match frozen text")
        if self.token_count < 0:
            raise SpecError("token count cannot be negative")


def make_advice_arm(
    arm_id: Literal["card", "generic", "none"],
    instance_id: str,
    text: str,
    token_count: int,
    forbidden_gt_forms: Iterable[str],
) -> AdviceArm:
    leaked = leakage_hits(text, forbidden_gt_forms)
    if leaked:
        raise SpecError(f"advice leaks ground truth: {leaked}")
    return AdviceArm(
        arm_id=arm_id,
        semantic_instance_id=instance_id,
        advice_text=text,
        content_sha256=sha256(text.encode("utf-8")).hexdigest(),
        token_count=token_count,
    )


def validate_card_generic_pair(card: AdviceArm, generic: AdviceArm) -> None:
    if card.arm_id != "card" or generic.arm_id != "generic":
        raise SpecError("wrong arm labels")
    if card.semantic_instance_id != generic.semantic_instance_id:
        raise SpecError("arms must use the same semantic instance")
    if card.advice_text == generic.advice_text:
        raise SpecError("card and generic arms need a real content contrast")
    if card.token_count != generic.token_count:
        raise SpecError("declared tokenizer counts differ")
```

**Required tests:** exact and decimal GT leakage, changed instance ID, mismatched token counts, and frozen content-hash mismatch. Statistical paired-difference code belongs in the experiment, not a shared domain primitive.

### S2 — Incremental value of trigger matching

The **registered S2 question** remains matched-card versus yoked same-family card on identical tasks. The critique’s matcher confusion corpus is useful as a measurement-validation subtask; matcher precision/recall alone does not answer S2.

```python
from dataclasses import dataclass
from datetime import datetime
from hashlib import sha256
from typing import Literal

from shared.epistemic_semantics.bayes import SpecError


@dataclass(frozen=True)
class StrategyCard:
    card_id: str
    family: str
    trigger: str
    text: str

    def __post_init__(self) -> None:
        if not all((self.card_id, self.family, self.trigger, self.text)):
            raise SpecError("strategy card needs IDs, trigger, and frozen text")

    @property
    def digest(self) -> str:
        canonical = "\0".join((self.card_id, self.family, self.trigger, self.text))
        return sha256(canonical.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class S2Case:
    case_id: str
    family: str
    trigger: str | None
    stratum: Literal["valid_application", "invalid_application", "absent_trigger"]
    trigger_recorded_at: datetime
    solver_started_at: datetime
    trigger_record_sha256: str

    def __post_init__(self) -> None:
        if not self.case_id or not self.family:
            raise SpecError("S2 case and family IDs are required")
        if self.stratum not in {"valid_application", "invalid_application", "absent_trigger"}:
            raise SpecError("unknown S2 stratum")
        if (self.stratum == "absent_trigger") != (self.trigger is None):
            raise SpecError("trigger presence must agree with the registered stratum")
        if self.trigger == "":
            raise SpecError("trigger cannot be an empty string")
        if self.trigger_recorded_at.utcoffset() is None or self.solver_started_at.utcoffset() is None:
            raise SpecError("S2 event times must be timezone-aware")
        if self.trigger_recorded_at >= self.solver_started_at:
            raise SpecError("trigger must be frozen before solver execution")
        if (
            len(self.trigger_record_sha256) != 64
            or any(ch not in "0123456789abcdef" for ch in self.trigger_record_sha256.lower())
        ):
            raise SpecError("trigger record must carry a hexadecimal SHA-256 digest")


@dataclass(frozen=True)
class S2Assignment:
    case_id: str
    stratum: str
    matched_card_id: str | None
    matched_card_sha256: str | None
    yoked_card_id: str
    yoked_card_sha256: str
    pair_sha256: str


def validate_s2_assignment(
    case: S2Case, matched_card: StrategyCard | None, yoked_card: StrategyCard
) -> S2Assignment:
    if case.stratum == "absent_trigger":
        if case.trigger is not None or matched_card is not None:
            raise SpecError("absent-trigger stratum must not claim a matched card")
    else:
        if case.trigger is None or matched_card is None or matched_card.trigger != case.trigger:
            raise SpecError("matched card does not match the pre-solver trigger")
        if matched_card.family != case.family:
            raise SpecError("matched card is from another family")
        if yoked_card.trigger == case.trigger:
            raise SpecError("yoked card accidentally matches the trigger")
    if yoked_card.family != case.family:
        raise SpecError("yoked card must be from the same family")
    if matched_card is not None and yoked_card.card_id == matched_card.card_id:
        raise SpecError("matched and yoked arms must use distinct cards")
    matched_digest = None if matched_card is None else matched_card.digest
    manifest = "\0".join((
        case.case_id, case.family, case.trigger or "none", case.stratum,
        case.trigger_recorded_at.isoformat(), case.solver_started_at.isoformat(),
        case.trigger_record_sha256,
        matched_card.card_id if matched_card is not None else "none",
        matched_digest or "none", yoked_card.card_id, yoked_card.digest,
    ))
    return S2Assignment(
        case_id=case.case_id,
        stratum=case.stratum,
        matched_card_id=None if matched_card is None else matched_card.card_id,
        matched_card_sha256=matched_digest,
        yoked_card_id=yoked_card.card_id,
        yoked_card_sha256=yoked_card.digest,
        pair_sha256=sha256(manifest.encode("utf-8")).hexdigest(),
    )
```

**Required tests:** trigger assignment is frozen before solver output; cards remain same-family; valid, invalid, and absent-trigger strata are kept distinct; a generic-text negative fixture catches false trigger fires. The matcher fixture is validation, not the S2 outcome.

### S3 — Incremental effect of validity obligations

The critique marks S3 **blocked** until `gates/s3_rubric.md` exists and at least two independent human annotations agree on a calibration set. Do not ship a guessed obligation checker. This gate helper records that prerequisite; it does not verify annotator independence.

```python
from dataclasses import dataclass
from typing import Mapping

from shared.epistemic_semantics.bayes import SpecError


@dataclass(frozen=True)
class S3RubricEvidence:
    rubric_sha256: str | None
    annotations: tuple[Mapping[str, str], ...]  # one item_id -> label map per annotator


def require_s3_rubric(evidence: S3RubricEvidence) -> None:
    if not evidence.rubric_sha256:
        raise SpecError("S3 blocked: no frozen rubric")
    if len(evidence.annotations) < 2:
        raise SpecError("S3 blocked: need at least two independent annotations")
    item_sets = [set(annotation) for annotation in evidence.annotations]
    if any(items != item_sets[0] for items in item_sets[1:]):
        raise SpecError("S3 calibration annotations cover different items")
    for item in item_sets[0]:
        labels = {annotation[item] for annotation in evidence.annotations}
        if len(labels) != 1:
            raise SpecError(f"S3 calibration disagreement on {item}")
```

**After the gate:** obligations should be predicates over a typed answer using `Fraction` (including exact half-probability boundary behavior). S3 remains distinct from S2.

### S4 — Transfer across epistemic families

Implement the contamination certificate first. Defer a shared transfer statistic until at least two families produce actual instances.

```python
from dataclasses import dataclass

from shared.epistemic_semantics.bayes import SpecError


@dataclass(frozen=True)
class FamilySplitCertificate:
    family_a: str
    family_b: str
    ids_a: frozenset[str]
    ids_b: frozenset[str]
    template_ids_a: frozenset[str]
    template_ids_b: frozenset[str]
    surface_hashes_a: frozenset[str]
    surface_hashes_b: frozenset[str]

    def assert_clean(self) -> None:
        if self.family_a == self.family_b:
            raise SpecError("held-out family must differ")
        if self.ids_a & self.ids_b:
            raise SpecError("instance ID overlap")
        if self.template_ids_a & self.template_ids_b:
            raise SpecError("surface-template overlap")
        if self.surface_hashes_a & self.surface_hashes_b:
            raise SpecError("identical rendered surfaces across families")
```

**Required test:** disjoint instance IDs but shared templates must fail the certificate.

## V — Supporting validation questions

### V1 — English-rendering fidelity

Use a closed public schema: exact required keys, forbidden ground-truth keys, no unknown fields, exact rational parsing, and a renderer-injectivity check. Parse-back is a later step after the semantic representation is frozen.

```python
from collections.abc import Mapping
from fractions import Fraction

from shared.epistemic_semantics.bayes import SpecError, exact_fraction

REQUIRED_PUBLIC = {
    "semantic_id", "worlds", "prior_exact", "likelihood_exact",
    "observation", "question_id",
}
FORBIDDEN_PUBLIC = {
    "posterior_world1", "posterior_world1_exact", "verdict",
    "most_supported", "inference_trace",
}
OPTIONAL_PUBLIC = {"english"}


def validate_public_packet(packet: Mapping[str, object]) -> dict:
    keys = set(packet)
    missing = REQUIRED_PUBLIC - keys
    leaked = FORBIDDEN_PUBLIC & keys
    extra = keys - REQUIRED_PUBLIC - OPTIONAL_PUBLIC
    if missing or leaked or extra:
        raise SpecError({"missing": sorted(missing), "forbidden": sorted(leaked), "extra": sorted(extra)})
    worlds = packet["worlds"]
    if (
        not isinstance(worlds, (list, tuple))
        or any(not isinstance(world, str) or not world for world in worlds)
        or len(set(worlds)) != len(worlds)
    ):
        raise SpecError("worlds must be a list of unique non-empty string IDs")
    prior = packet["prior_exact"]
    likelihood = packet["likelihood_exact"]
    if not isinstance(prior, Mapping) or not isinstance(likelihood, Mapping):
        raise SpecError("prior_exact and likelihood_exact must be mappings")
    if set(prior) != set(worlds) or set(likelihood) != set(worlds):
        raise SpecError("exact probability fields must cover exactly the worlds")
    exact_prior = {world: exact_fraction(value) for world, value in prior.items()}
    exact_likelihood = {world: exact_fraction(value) for world, value in likelihood.items()}
    if any(value < 0 for value in exact_prior.values()):
        raise SpecError("prior_exact cannot contain negative mass")
    if sum(exact_prior.values(), Fraction(0)) != 1:
        raise SpecError("prior_exact must sum exactly to 1")
    if any(value < 0 or value > 1 for value in exact_likelihood.values()):
        raise SpecError("likelihood_exact values must lie in [0, 1]")
    return dict(packet)


def assert_render_injective(render, instances) -> None:
    seen = {}
    for instance in instances:
        text = render(instance).strip()
        previous = seen.get(text)
        if previous is not None and previous != instance.semantic_id:
            raise SpecError(f"render collision: {previous} vs {instance.semantic_id}")
        seen[text] = instance.semantic_id
```

**Required tests:** unknown and forbidden fields are rejected; malformed/non-normalized exact priors fail; semantically distinct instances that render identically fail.

### V2 — Characterization reliability and leakage

Do not invent one undefined “reliability” score. Implement leakage detection for exact and common decimal renderings, plus a separate relabeling-equivariance test.

```python
from decimal import Decimal, localcontext
from fractions import Fraction
from typing import Iterable
import re


def gt_render_forms(value: Fraction, labels: Iterable[str] = ()) -> frozenset[str]:
    forms = {str(value), *labels}
    with localcontext() as context:
        context.prec = 32
        decimal = Decimal(value.numerator) / Decimal(value.denominator)
        for places in (2, 3, 4, 6):
            rendered = f"{decimal:.{places}f}".rstrip("0").rstrip(".")
            if rendered:
                forms.add(rendered)
    return frozenset(form for form in forms if form)


def _contains_rendered_value(text: str, form: str) -> bool:
    escaped = re.escape(form)
    if re.fullmatch(r"[+-]?(?:\d+(?:\.\d+)?|\d+/\d+)", form):
        return re.search(rf"(?<![\w.]){escaped}(?![\w.])", text) is not None
    return re.search(rf"\b{escaped}\b", text, flags=re.IGNORECASE) is not None


def leakage_hits(visible_text: str, ground_truth_forms: Iterable[str]) -> tuple[str, ...]:
    return tuple(sorted(
        form for form in ground_truth_forms
        if _contains_rendered_value(visible_text, form)
    ))
```

**Required tests:** detect both `4/7` and a rendered decimal such as `0.571`; include negative tests for incidental substrings; relabel worlds/agents and require the semantic result to permute consistently. The scanner is a validation layer, not proof that a characterization is scientifically good.

### V3 — Independent-verifier feasibility

An AST check is only an import-edge check. V3 needs a second implementation from a frozen specification and a harness capable of exposing disagreement. Agreement does **not** prove independence.

```python
from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class OracleDisagreement:
    seed: int
    axes: Mapping[str, object]
    field: str
    value_a: str
    value_b: str


def compare_oracles(oracle_a, oracle_b, seeds, axis_grid, fields) -> list[OracleDisagreement]:
    """Compare from-spec oracle outputs. Agreement is not proof of independence."""
    axis_grid = tuple(axis_grid)  # safe when callers pass a one-shot iterator
    fields = tuple(fields)
    disagreements = []
    for seed in seeds:
        for axes in axis_grid:
            spec = {"seed": seed, **axes}  # no solver answer enters either oracle
            result_a = oracle_a(spec)
            result_b = oracle_b(spec)
            for field in fields:
                if result_a[field] != result_b[field]:
                    disagreements.append(OracleDisagreement(
                        seed, dict(axes), field, str(result_a[field]), str(result_b[field])
                    ))
    return disagreements
```

**Required test:** inject a deliberate wrong value in one oracle for one seed/axis cell and require exactly that disagreement to be emitted. A no-import check may be retained as a weak adjunct; never label it an independence proof.

## Separate research line — T1 matched-fact presentation

T1 belongs in the Arena/experiment layer, not in `envs/epistemic_games`. Semantic identity comes from canonical structured facts; rendered text hashes identify presentations and therefore must not be used to assert fact-set identity. This first slice varies ordering only; any separate framing or emphasis transform needs its own frozen operator. The outcome is a behavior/presentation effect, not attention manipulation or harm.

```python
from dataclasses import dataclass
from hashlib import sha256
from typing import Callable, Sequence
import json

from shared.epistemic_semantics.bayes import SpecError


@dataclass(frozen=True)
class AtomicFact:
    predicate: str
    arguments: tuple[str, ...]
    value: str


def semantic_fact_id(facts: Sequence[AtomicFact]) -> str:
    encoded = sorted(
        json.dumps(
            {"predicate": fact.predicate,
             "arguments": list(fact.arguments),
             "value": fact.value},
            sort_keys=True,
            separators=(",", ":"),
        )
        for fact in facts
    )
    return sha256("\n".join(encoded).encode("utf-8")).hexdigest()


def make_matched_fact_pair(
    facts: Sequence[AtomicFact],
    order_a: Sequence[int],
    order_b: Sequence[int],
    render: Callable[[Sequence[AtomicFact]], str],
) -> dict:
    facts = tuple(facts)
    order_a, order_b = tuple(order_a), tuple(order_b)
    n = len(facts)
    valid = set(range(n))
    for order in (order_a, order_b):
        if len(order) != n or set(order) != valid:
            raise SpecError("presentation order must be a permutation of the fact indices")
    if order_a == order_b:
        raise SpecError("identical orders do not define a presentation contrast")
    text_a = render(tuple(facts[i] for i in order_a))
    text_b = render(tuple(facts[i] for i in order_b))
    if text_a == text_b:
        raise SpecError("rendered texts are identical; there is no presentation contrast")
    return {
        "semantic_fact_id": semantic_fact_id(facts),
        "order_a": order_a,
        "order_b": order_b,
        "text_a": text_a,
        "text_b": text_b,
    }
```

**Required tests:** reordering the same canonical fact objects preserves `semantic_fact_id` while changing presentation order; invalid permutations and identical orders fail. Keep T1 outside the E/S/V portfolio and do not name fields `attention`, `manipulation`, or `harm`.

## Target integration points reported by the critique

These are review-reported seams, not independently confirmed from this checkout; verify them in the target session before editing. The critique says the existing `epistemic_games` judge is provenance-coupled to its semantic core, and points to `generate_env.py` for the renderer hook, `env_runner.py` for the judge-template dependency, and `instance_oracles.json` for exact-instance gating. Preserve that coding-environment path for generator/judge tasks. Direct-answer E probes, S arms, and T1 belong in `arena/` / `experiments/`, not inside a coding-environment judge.

The consequences for v2 are: E1 should factor or extend existing exact semantics rather than duplicate them; V3 must distinguish provenance from independence; and an AST import check is only a weak adjunct to a second implementation and an injected-bug sensitivity test.

## Proposed module boundaries and build order

These homes follow the critique’s proposed architecture and must be reconciled with the actual `rl_eval_generator` checkout before file creation:

```text
shared/epistemic_semantics/
  bayes.py            # exact FiniteDist; factor existing E1 semantics
  silence.py          # E3 speech policy and matched informative/control pair
  s5_pal.py           # E2 S5 model and announcement update
  formulas.py         # E4 AST, evaluator, depth-discrimination certificate
  private_signals.py  # E5 per-agent signal model and perspective packet
  bayesian_games.py   # E6 exact bounded enumerator; E7 consumes same game type
  level_k.py          # E7 explicit level-0 anchor and divergence certificates
  signaling.py        # E8 PBE checks; enumerator gated on off-path specification
  packets.py          # V1 closed public schema and renderer injectivity
  leakage.py          # V2 exact/decimal leakage forms and scan

arena/
  epistemic_arms.py   # S1/S2 prompt arms; not inside the coding-env judge
  matched_facts.py    # T1 only; keep firewalled from E/S/V

tests/ and tools/
  dual_oracle_harness.py  # V3 disagreement harness; provenance disclaimer
  test_*.py               # boundary, adversarial, and injected-bug fixtures
```

**Build-only sequence from the critique:** exact Bayes + closed packets + leakage checks; S1 arm construction and S2 fixture/assignment validation; E3; freeze the S5/PAL fragment, then E2/E4/E5; E6 capped oracle; E7 after its level-0 contract; E8 after off-path beliefs are specified; V3 once a genuinely second oracle exists; S4 split certificate when two families exist; T1 independently on the Arena line. S3 stays blocked until its rubric and independent calibration annotations are approved.

No model runs, experiments, or target-repository code changes are authorized by this proposal. The selected pieces can be packaged for approval; this v2 draft has not been pushed.
