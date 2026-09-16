# Design Reference Audit: Nature Skills × Academic Research Suite × Paper Evidence Map

This note records the architecture decisions behind PEM v0.2 so the project can borrow mature engineering patterns without becoming a clone of either reference project.

## 1. Nature Skills: what PEM borrows

The strongest influence is the **skill packaging and progressive-loading model** visible in `nature-reader`:

- a short `SKILL.md` that routes rather than containing the entire behavior contract;
- a declarative `manifest.yaml` describing what is always loaded and what is loaded only under specific conditions;
- static core rules separated from dynamic fragments;
- deep references opened only when needed;
- explicit output contracts and pre-response checks;
- follow-up questions handled locally instead of regenerating the full artifact.

PEM v0.2 adopts the same class of architecture:

```text
SKILL.md
  ↓
manifest.yaml
  ├── always_load
  ├── routing
  ├── depth/lens selection
  └── on-demand references
```

### What PEM does not copy from Nature Reader

Nature Reader's default product is a full bilingual reader with artifacts such as `paper.md`, `source_map.json`, translation notes, and extracted assets. That is not PEM's default job.

PEM remains decision- and evidence-oriented. Its output may be very small when the user only needs a Triage or Targeted answer. It does not force a whole-document artifact before answering a source-linked question.

## 2. Academic Research Suite: what PEM borrows

ARS contributes the strongest examples of **intent-first orchestration and quality/integrity boundaries**:

- do not load the whole suite by default;
- route by user intent before entering a workflow;
- keep workflow-specific rules outside the root router;
- support compatibility aliases without making aliases the only interface;
- separate broad research phases and use stronger integrity gates when claims become more consequential;
- distinguish unavailable evidence from negative evidence;
- make test/evaluation infrastructure part of the product rather than documentation only.

PEM uses those principles to support:

```text
user goal
  ↓
minimum reading depth
  ↓
selected lens(es)
  ↓
source-grounded evidence work
  ↓
stop or escalate
```

### What PEM does not copy from ARS

PEM is not an end-to-end research lifecycle suite. It does not attempt to replace ARS-style literature search, experiment orchestration, manuscript drafting, peer review simulation, or publication pipelines.

That narrow scope is deliberate.

## 3. What remains PEM-specific

PEM's scientific core is still its own evidence model:

```text
Claim
  ↓
Evidence
  ↓
Support
  ↓
Defensible Boundary
```

The v0.2 extension adds adaptive reading and traceable idea formation:

```text
Observation
  ↓
Candidate Gap
  ↓
Targeted Evidence Check
  ↓
Candidate Idea
  ↓
Novelty / feasibility checks when needed
  ↓
Research Idea
```

This supports the three project rules:

1. **No user need → no analysis.**
2. **No evidence → no strong claim.**
3. **No verified gap → no strong research idea.**

## 4. Why Goal + Depth + Lens are separate

These concepts solve different problems:

- **Goal** = why the user is reading the paper now.
- **Depth** = how much evidence work is needed.
- **Lens** = what analytical capability is relevant.

For example:

```text
Goal: decide whether the paper is useful for a research direction
Depth: Triage
Lenses: Relevance + Contribution + Gap/Idea where useful
```

or:

```text
Goal: determine whether an ablation supports a necessity claim
Depth: Targeted
Lenses: Method + Evidence + Critical
```

Collapsing these into one rigid workflow would recreate the v0.1 problem.

## 5. Why STOP is a first-class behavior

Nature Reader explicitly avoids rebuilding a full reader for a narrow follow-up question. ARS explicitly avoids loading every workflow by default. PEM applies the same efficiency principle to scientific reading itself:

> Once the user's immediate question is answered with sufficient evidence and uncertainty, stop.

A response may therefore be scientifically accurate yet still fail PEM v0.2 if it performs unnecessary full-paper analysis.

This is evaluated as `OVERREAD` or `NO_STOP`.

## 6. Evaluation consequences

PEM v0.1 mainly tested evidence fidelity. PEM v0.2 must test both:

```text
scientific evidence fidelity
+
routing / scope discipline
```

The canonical routing fixture is under `examples/adaptive-routing/`, with live evaluation guidance in `docs/evaluation-adaptive.md` and a deterministic contract checker in `scripts/check_adaptive_routes.py`.

Routing failure classes are:

- `MISROUTE`
- `OVERREAD`
- `UNDERREAD`
- `NO_STOP`
- `EVIDENCE_BYPASS`
- `IDEA_OVERPROMOTION`

The deterministic checker validates the fixture definition only. Semantic routing quality still requires repeated live runs and human review.

## 7. Current implementation status

Implemented on the v0.2 branch:

- thin `SKILL.md` router;
- `manifest.yaml` static/dynamic loading contract;
- always-loaded core principles, source gate, and output contract;
- Goal Router and Depth Router;
- composable reading lenses;
- full and compact English/Chinese adaptive Project prompts;
- README and Quickstart migration to natural-language entry;
- methodology migration from universal two-round reading to adaptive depth;
- Candidate Gap / Candidate Idea boundaries;
- adaptive routing fixture + machine-readable expectations + checker;
- adaptive routing evaluation guide and failure taxonomy.

Still required before a confident v0.2 release:

- repeated live runs across the routing matrix under recorded model/mode/date conditions;
- evidence-fidelity regression runs against existing synthetic/adversarial/access/source-precedence fixtures;
- optional integration of stable routing-contract checks into the main CI once it adds value without pretending deterministic code can judge semantic routing.

## 8. Positioning

A useful ecosystem boundary is:

```text
source-grounded paper ingestion / reader
        ↓
Paper Evidence Map
  relevance / understanding / evidence / boundary / gap / idea
        ↓
broader research suites
  literature / experiment / writing / review / publication workflow
```

PEM should stay narrow enough that users can understand its promise quickly:

> **An adaptive, evidence-grounded scientific paper reading skill that decides what to read, how deeply to read it, and what the paper actually proves before turning observations into research ideas.**
