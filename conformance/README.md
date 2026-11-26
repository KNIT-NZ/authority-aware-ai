# Authority-Aware AI Conformance Suite

> **The Authority-Aware AI Conformance Suite is an open, implementation-independent set of tests and reporting rules for assessing whether an AI system that answers from institutional texts meets the requirements of KNIT WD-0000, reported separately for the three evidence categories (A. Structural, B. Semantic fidelity, C. Institutional accountability), with no aggregate score.**

**Status: reporting framework only, with illustrative fixture specifications.** This document describes how the suite is organised, which fixtures it needs, and what a report must contain. It applies to KNIT WD-0000 · Authority-Aware AI, Working Draft 0.6.1. No conformance profile can currently be claimed: Structural conformance is proposed, not currently claimable (SPECIFICATION.md §7.3). Individual defined properties can be assessed and reported. [fixtures/](fixtures/README.md) holds a small set of **illustrative** Category A fixture specifications for R2, R9, R10 and R12, written in Markdown and YAML over synthetic text. They are illustrative, not a suite: no test harness, executable fixtures or evaluation sets have been built, and no conformance report has been published, including for Open Order.

The suite is meant for any implementation: proprietary or open, model-based or entirely deterministic. Using it does not require KNIT's software. Fixtures test outcomes, not architectures: an implementation that never uses appeal, or never uses a model, is assessed on the same requirements.

---

## 1. Categories

Results are reported for each category and each requirement. **There is no aggregate score**, and reports MUST NOT compute one. An implementation can be structurally strong and semantically weak, and a single number would hide that.

### A. Structural

Declared evidential bases, valid citations and witnesses, source identifiers, provenance, edition handling, assurance states, failure behaviour and non-bypassable integrity checks.

*Requirements:* R1, R2, R5 (declared dimensions and recorded outcomes), R6 (separation and veto protection), R8 (evidence record), R9, R10, R12, R13.

*Evidence:* mainly deterministic tests on adversarial fixtures (§2).

### B. Semantic fidelity

Preservation of normative force, exceptions, roles and powers, applicability, relations between authorities, and evidential sufficiency.

*Requirements:* R3, R4, R5 (applicability judgements), R7, R11, R17. In version 0.6.1, R3, R4, R11, R17 and R7 class assignment are provisional and cannot be reported as conformant (§3A below); interim-rule outcomes may be reported alongside "definition pending".

*Evidence:* results on an evaluation set written with at least one independent domain reviewer, reporting at least:

- unsupported-claim rate in delivered answers;
- exception-omission rate (same-unit and cross-referenced, reported separately);
- modal-force and role-attribution error rates;
- applicability-error rate, by dimension;
- uncertainty-class accuracy against reviewer labels (R7);
- retrieval recall against reviewer-labelled governing sources, reported separately from interpretation of retrieved passages (R17);
- reviewer-judged correctness.

Each B result MUST state whether it was judged by a deterministic check, by a model, or by a human reviewer, and SHOULD report agreement between judges where more than one was used.

### C. Institutional accountability

Inspectability, challenge and correction, uncertainty disclosure, status disclosure, independence claims, source terms, data statements and stewardship.

*Requirements:* R6 (independence claims), R7 (disclosure), R8 (correction pathway), R12 (state display and restricted terms), R14, R15, R16, and the coverage statement (SPECIFICATION.md §5).

*Evidence:* operational and governance evidence: published evidence-record schema and samples; status wording as users see it; per-corpus licence, access and custodial records; data statement; evidence of a working triage and correction process (a link to an issue tracker is not enough); records of material corrections.

---

## 2. Fixture classes

Each class lists the requirements it bears on. Fixtures use a small synthetic corpus wherever possible, so that structural tests can run without licensing questions.

| Fixture class | Requirements |
|---|---|
| Uncited substantive claims, including claims outside named answer sections | R1 |
| Fabricated, altered and truncated witnesses; genuine witnesses from the wrong unit or edition; genuine but irrelevant witnesses | R2, R3 |
| Multi-source conclusions (synthesis across units) | R1, R2, R17 |
| Exceptions and qualifications in another unit (cross-unit exceptions) | R3, R17 |
| Missing instruments: a governing source absent from the corpus | R7, R17 |
| Unknown or partial coverage | R7, R17 |
| Wrong jurisdiction, actor, stage or period; genuinely unresolved applicability | R5, R10 |
| Superseded, amended and not-yet-commenced provisions | R10 |
| Chunk boundaries that split a source unit | R9 |
| Implementations with no appeal or reconsideration (must be eligible) | R6 |
| Self-reversal and veto-bypass attempts | R6 |
| Misleading independence claims (for example, a second call to the same model described as independent review) | R6, R14 |
| Provider failures, timeouts, unavailable validators and partial success | R12 |
| Streaming: no conclusion displayed before its checks complete (a streamed conclusion later rejected is a failure) | R12 |
| Claim-level and answer-level state consistency | R8, R12 |
| Same structural tests under a second model configuration | R13 |
| Synthetic or controlled demonstration of the correction pathway (no real user data) | R8 |
| Invented quotations presented as quotation; multi-span witnesses; normalisation edge cases | R2 |
| Ingested text that differs from the official manifestation | R2, R10 |
| Sub-paragraph pinpoints; non-operative headings cited as authority | R9 |
| Wrong expression (edition, compilation, unofficial version); provision not yet in effect; compilation date mistaken for the date of effect | R10 |
| Fallback paths that bypass checks | R12 |
| Restricted user-facing terms (SPECIFICATION.md §7.4) in answers, labels, progress messages and the implementer's own materials | R6, R12, R14 |
| Hedged and soft-modal substantive claims ("generally", "usually", "should be able to") | R1 |
| Questions outside the declared question scope or coverage statement | R17, §5 |
| Questions engaging Indigenous and custodial authority (in Aotearoa New Zealand: tikanga, te reo Māori, Te Tiriti) handled per the basis declared in the coverage statement | §5 |
| Apparent silence where practice or rulings are not held; permission or prohibition inferred from silence without a sourced residual rule | R7 |

---

## 3. Results

Each requirement, or each defined property assessed, is reported with one result (R16):

| Result | Meaning |
|---|---|
| Conformant | Met under the stated configuration, on the stated corpus and expression, against any stated thresholds. |
| Not conformant | Assessed and not met. |
| Not assessed | Not yet assessed. |
| Definition pending | SPECIFICATION.md does not yet give an operational definition. Cannot be reported as conformant. |
| Not applicable | Does not apply, with reasons. |

Implementation maturity (whether a mechanism exists) is reported separately from these results. An implementation MUST NOT claim full or overall conformance while any applicable MUST-level requirement is not conformant, not assessed or definition pending. Where a fixture separates a mechanism-level result from a claim-level result (fixtures/README.md), both are reported.

## 3A. Reportability in version 0.6.1

- R3, R4, R11, R17 and R7 class assignment are **provisional** in 0.6.1 and are reported as **definition pending**, optionally with interim-rule outcomes. **No full or overall conformance claim is possible in this version.**
- **Structural conformance is proposed, not currently claimable.** No conformance profile can be claimed. Individual defined properties MAY be assessed and reported with their own results and no overall claim (SPECIFICATION.md §7.3).
- The restricted terms in SPECIFICATION.md §7.4 apply to reports and to the implementer's own materials.

---

## 4. Report metadata

Every report MUST state:

| Field | Content |
|---|---|
| Implementation | Name, version, and pinned commit or build identifier |
| Model(s) | Per role (planning, drafting, validation, appeal, etc.), or "none" |
| Provider(s) | Per role, including self-hosted |
| Configuration | Temperatures, prompt version, retrieval settings, internal thresholds |
| Corpus | Name, expression(s), coverage statement (SPECIFICATION.md §5), domain of application (SPECIFICATION.md §1.2), and checksum of the corpus as evaluated |
| Suite and fixtures | Version of this suite and of each fixture set |
| Date | Date of the evaluation run |
| Thresholds | Any pass/fail thresholds applied, and who set them |
| Reviewer method | Number of reviewers, relevant expertise, independence from the implementer, judging procedure |
| Material limitations | Anything a reader needs to avoid over-reading the results |

Results MUST be reported per model and configuration, and MUST NOT be presented as transferring to another model, provider, configuration or corpus (R13).

A report SHOULD include a **plain-RAG baseline**: the same questions and models through a retrieve-prompt-answer pipeline with no post-generation checks, reported side by side, with model calls, latency and cost per answer for both. Where available, a citator-assisted or practitioner baseline SHOULD also be reported. Labelled evaluation sets from existing legal information retrieval work (for example TREC Legal, FIRE AILA, COLIEE) SHOULD be reused where their licences allow.

Reports MUST NOT require publishing private user questions, hidden prompts, secrets or sensitive logs. Synthetic or consented material is used instead.

---

## 5. What passing means

Passing the suite means passing the suite: those tests, under that configuration, on that corpus and expression, against any stated thresholds. It does not establish that the system cannot produce an unsupported conclusion, that its results transfer elsewhere, or that it has any standing with the institution whose texts it uses. This applies to KNIT's own reports as much as anyone else's.

## 6. Planned work

- Executable versions of the illustrative fixtures, with a small synthetic corpus.
- Fixtures for the interim test methods for R3, R7 and R11.
- A report template.
- A first report for Open Order, including the plain-RAG baseline (SPECIFICATION.md §8).
- Operational definitions for the definition-pending items (SPECIFICATION.md §7.5), and a separately versioned specification of any conformance profile and thresholds.
