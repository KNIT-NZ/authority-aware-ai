# Evidence: Open Order against KNIT WD-0000 · Authority-Aware AI

Historical evidence at a pinned commit, assessed against the wording of Working Drafts 0.4.0 and 0.5.0 and carried forward unchanged into Working Drafts 0.6.0 and 0.6.1 (see "Note for Working Draft 0.6.0" at the end). It is not updated as Open Order evolves.

Open Order informs the specification but is not its canonical interpretation (SPECIFICATION.md §1.3). This file records how Open Order attempted each requirement at one historical commit. It is evidence of one approach, not a conformance result (R16).

## Pin and scope

- **Repository:** github.com/KNIT-NZ/open-order
- **Pinned commit:** `a3f007e649ce6b203bbc2201aaba7ea15b349cac` ("Link Open Order OpenSSF Best Practices badge", 25 Nov 2026 13:13 NZDT).
- **Runtime assurance commit:** `4ce15ce78d0c47d5b43cf466a8237f89d30a4a9b` ("Harden Open Order dependencies and establish regression assurance", 25 Nov 2026 12:53 NZDT) is the direct parent of the pin. The only change between them is two added lines in `README.md` (the badge link). Application code at the two commits is identical, so observations below hold for both.
- **Reviewed:** 26 Nov 2026 (NZDT) for v0.4.0; re-checked 26 Nov 2026 (NZDT) for v0.5.0 only where a requirement's wording changed what counts (see "Re-check for v0.5.0" at the end). Findings otherwise carried over unchanged.
- **Corpus at the pin:** Standing Orders of the House of Representatives 2023 and Speakers' Rulings 2023 (`data/sources/source-manifest.json`).
- **Not covered:** changes made after the pin, including the separate Open Order build workstream's privacy, edition and disclosure changes. Nothing here describes current production behaviour.

Pinned links take the form `https://github.com/KNIT-NZ/open-order/blob/a3f007e649ce6b203bbc2201aaba7ea15b349cac/<path>#L<line>`.

## Method labels

Each finding is labelled with how it was established:

- **[CI] code inspection:** reading source at the pin.
- **[ST] synthetic test:** running code from the pin on constructed inputs, in a separate copy outside the repository. This includes the repository's own test suite (`tests/assurance.test.ts`, 11 tests, all passing on 26 Nov 2026) and additional synthetic checks of individual functions (S1–S5 below).
- **[RC] runtime configuration:** observation of deployed configuration (models, providers, environment). **None was available for this review.**
- **[PO] production observation:** observation of the deployed service. **None was made for this review.**

Mechanism labels follow SPECIFICATION.md §3.2: deterministic; model-judged, code-enforced; prompt-only; human review; not implemented.

## Answer paths at the pin

The answer endpoint is `POST /api/ai/answer` (`app/api/ai/answer/route.ts`, 1,376 lines). It returns server-sent events. [CI]

- **Ordinary path.** Plan (`query.plan`, temperature 0.1) → retrieve → select (legacy selector, plus v40 adjudication on some questions, per `v40MustAdjudicate`, `lib/ai/scenario-adjudication.ts:191`) → draft (`answer.generate`, temperature 0.2) → deterministic pruning and citation checks → model claim validation (`answer.validate`, temperature 0) → deterministic same-unit exception veto → optional appeal → optional bottom-line reconstruction → final checks → one `answer_delta` event with the final text, then `done` (route lines ~1275–1291).
- **Streaming.** The draft is generated with a function named `streamText` but is awaited in full on the server (route line ~659). Answer text is sent to the client in a single `answer_delta` event only after the checks above, or as fallback text. No draft text was found to be sent to the client before checking. Stage labels are streamed during processing and shown in the interface (`hooks/useOpenOrderAssistant.ts:122–130`).
- **Fallback paths.** `buildFallbackAnswer` (`lib/procedural-reasoning.ts:2387`) is used when no authority is selected (route ~613–647), the draft is empty, the draft is empty after pruning, citations or authority mentions fail, no claims remain, the responsiveness gate fails, or semantic validation removes the bottom line (~1237–1258). Fallback text is deterministic: it states that a substantive answer was withheld and why, and lists up to four selected authorities with their headings and class labels as inspection points. It contains no model-generated conclusions.
- **Inner error path.** Exceptions during drafting or validation are caught (~1296–1332), classified by `failureDiagnostic`, and reported with `publicFailureReason` and a `drafting_unavailable` or `validation_unavailable` fallback.
- **Outer error path.** Exceptions before drafting (planning, retrieval, selection) reach the outer `catch` (~1340–1360), which sends an `error` event containing `error.message`. Provider errors (`AiProviderError`) carry curated messages and keep raw provider output in a separate `rawMessage` field that is not sent. Messages from other error types (for example database or schema errors) are forwarded as-is; their content was not assessed.

---

## R1. Generated output is a proposal, with a declared basis

- File header, `lib/ai/scenario-adjudication.ts:4`: "Model proposals are untrusted until validated against exact retrieved source text." [CI]
- `pruneValidatedAnswerContent` (`lib/procedural-reasoning.ts:2218`) removes lines without an allowed inline citation from the four answer sections it treats as substantive ("Bottom line:", "What this means:", "Your options:", "Risks or constraints:"). Deterministic. [CI; ST S1]
- `validateAnswerCitations` (`lib/procedural-reasoning.ts:2153`) rejects citations to authorities outside the selected set. It returns `ok` for text with no citations. Deterministic. [CI; ST S3]
- `extractAnswerClaims` (`lib/procedural-reasoning.ts:2288`) only treats cited lines in the four substantive sections as claims. Model claim validation, the exception veto and appeal apply only to those claims. [CI]
- Synthetic finding S2b: an uncited sentence placed **before** the first section heading survives `pruneValidatedAnswerContent` and is not extracted as a claim. S2c: text inside a "Best authorities to inspect or cite:" line survives pruning if it looks like an authority line, and is not extracted as a claim. Whether the drafting step produces such text in practice was not assessed. [ST]
- No declared evidential basis (quotation, paraphrase, synthesis, assumption, uncertainty) is recorded per claim. Not implemented. [CI]
- Mechanisms: deterministic (pruning, citation set); model-judged, code-enforced (claim validation).

## R2. Verbatim witness

- **Source admission (v40 path):** `validateV40Proposal` (`lib/ai/scenario-adjudication.ts:141`; check at line 164) rejects a proposed governing witness shorter than 24 characters or not found in the source body (`quote.length < 24 || !body.includes(quote)`). Deterministic. [CI; ST: repository tests at `tests/assurance.test.ts:27, 30`]
- **Appeal:** `corroborateClaimAppeal` (`lib/ai/claim-appeal.ts`; check at line 57) requires a 24–500 character quotation, after whitespace normalisation, for each cited authority of a disputed claim. Deterministic. [CI; ST: `tests/assurance.test.ts:45`]
- **Delivered claims (ordinary path):** the claim validation schema (`app/api/ai/answer/route.ts:110–123`) records only `id`, `supported` and `reason` for each claim. It does not require or check a witness. A delivered claim therefore has a machine-checked witness only if it passed through appeal, and the sources behind it have witnesses only if the question took the v40 adjudication path. [CI]
- **Assessment:** the witness mechanism is deterministic and strong where it applies, but it does not apply to every delivered substantive claim. **Partial.**

## R3. Normative fidelity

- `findOmittedSourceQualifications` (`lib/ai/qualification-guard.ts:116`): a deterministic veto using English-language patterns. Header (lines 4–8): "This is a narrow conservative check, not a replacement for semantic entailment. Only an explicit exception in the same numbered source subsection as an operative rule can veto a categorical claim about the same actor and action. Does not infer what a cross-referenced provision says or add authorities." Called at route lines 993 and 1155. [CI]
- Synthetic S5: a categorical claim omitting a same-subsection "unless" exception is vetoed. [ST]
- Synthetic S4: the speaking-time example (SPECIFICATION.md §3.3) is **not** caught by the veto, as expected: the error is a change of modal force, not an omitted exception. Detection relies on model claim validation. [ST]
- Modal-force instructions in `lib/ai/prompts.ts`. Prompt-only, with model claim validation. [CI]
- Unresolved cross-referenced qualifications: not detected, and nothing makes the conclusion conditional. A `GENERIC_ACKNOWLEDGEMENT` pattern lets a claim pass the veto if it acknowledges other exceptions ("subject to other provisions"), which is disclosure without resolution. Not implemented against R3 as worded since v0.4.0 (a material unresolved qualification requires a conditional or withheld conclusion). [CI]
- **Partial.**

## R4. Roles and allocated powers

- `lib/ai/prompts.ts:159`: "Distinguish who can APPLY for an action, who DECIDES it, and which requirements must be satisfied. A necessary condition is not automatically sufficient; permission to request is not authority to compel." Prompt-only, with model claim validation. [CI]
- No deterministic check; no representation of delegation or wider powers. [CI]
- **Partial.**

## R5. Applicability

- `validateV40Proposal` (`lib/ai/scenario-adjudication.ts:157–158`): an adjudicating model reports `actorMatches`, `settingMatches`, `actionMatches` and `stageMatches`; code rejects a source unless all four are affirmed (`scope-not-established`). Model-judged, code-enforced. Applies on the v40 path only. [CI; ST: `tests/assurance.test.ts:30`]
- `v40SourceScopeMismatch` (`lib/ai/scenario-adjudication.ts:122`; route line 478): three corpus-specific exclusion rules. Deterministic. [CI]
- `buildV40Dossier` (`lib/ai/scenario-adjudication.ts:80`): excludes duplicate and out-of-scope-corpus sources. Deterministic. [CI; ST: `tests/assurance.test.ts:40`]
- Jurisdiction is recorded in the source manifest but not checked (single jurisdiction). Period is not checked. Unresolved applicability is not a state: a source is admitted or rejected. Per-dimension mechanism and outcome are not exposed to the reader. [CI]
- **Partial.**

## R6. Separation and independence of checks

- Proposal and checking are separate functions: drafting (`answer.generate`) versus validation (`answer.validate`) and deterministic checks. [CI]
- Appeal (route ~1000–1057) is invoked only when model rejections would remove the entire bottom line, reviews at most two claims, requires deterministic quotation corroboration (`corroborateClaimAppeal`), and skips any claim with a qualification veto (`qualificationVetoIds`). Appeal errors preserve the original rejection. [CI]
- `lib/ai/claim-appeal.ts:3–5`: "A model cannot reverse its own rejection: an independent affirmative review must provide actual, contiguous source quotations for EACH cited authority. The production qualification veto remains decisive and is never appealed." [CI]
- Properties: (a) functional separation, yes; (b) independence of mechanism, yes for the deterministic vetoes and quotation corroboration, no for model validation and appeal judgement; (c) model or provider independence, not ensured: appeal uses the same `answer.validate` task routing as validation (`lib/ai/routes.ts`); actual deployed models were not observed [RC: none]; (d) human review, none at runtime. [CI]
- **Wording:** the user-facing stage label "Independently reviewing disputed source entailment" (route line 1023) describes a review that may use the same model and provider. Under v0.4 and v0.5 R6 that wording would need to name the kind of independence. [CI]
- **Partial.**

## R7. Classified uncertainty

- `appendEvidenceGapSection` (`lib/procedural-reasoning.ts:2355`; route line 1263): appends "Open Order did not retrieve authority establishing [gap]. That unresolved point should not be treated as proved either way." Deterministic rendering. [CI]
- Gaps come from missing required concept slots in the legacy selector and are suppressed whenever v40 adjudication admits any authority (route ~498–503). Heuristic, deterministic. [CI]
- `lib/ai/prompts.ts:225`: "never infer a prohibition" from missing evidence. Prompt-only. [CI]
- The wording expresses retrieval uncertainty, which is the cautious default under R7. The four classes are not distinguished. [CI]
- **Partial.**

## R8. Inspectable evidence and correction

- **Evidence:** the stream emits `stage`, `plan`, `authorities` and `diagnostics` events (`docs/interfaces.md`); diagnostics and authorities are shown in `components/open-order/AssistantPanel.tsx`. Retrieval provenance is typed as `QueryProvenance` (`lib/procedural-reasoning.ts:16`). [CI]
- **Links:** `buildSourceHref` (`lib/procedural-reasoning.ts:147`; also `lib/open-order/format.ts:73`) builds a link to the source URL with an anchor and a text fragment made from the **first ten words of the section**, not from the words relied on. (v0.3's evidence described this as pointing at the cited words; that was incorrect.) [CI]
- No per-claim assurance state; no published evidence-record schema; exclusions appear in diagnostics, not as a structured record. [CI]
- **Correction pathway:** the footer links to GitHub issues as "Feedback" (`components/open-order/Footer.tsx`). `SECURITY.md` says procedural accuracy concerns "can be submitted as corrections with public source references". No documented triage responsibility, correction process or correction record was found. Not implemented to the standard R8 has set since v0.4.0 (documented pathway, triage responsibility, correction record). [CI]
- **Partial.**

## R9. Citation at the institution's unit of authority

- `docs/architecture.md:38`: "Retrieval units derived from sections. Chunks support search. Sections support citation." [CI]
- Separate `sections` and `chunks` tables (`infra/sql/002_core_tables.sql:32, 69`). [CI]
- `buildAuthorityPayload` (`lib/procedural-reasoning.ts:175`) returns section-level identifiers and citation labels (`sectionId`, `sectionKey`, `citationLabel`); no chunk identifiers are cited. [CI]
- Full-text search weights citation label, section key and heading above body text (`infra/sql/003_text_search.sql`). [CI]
- No synthetic test of a chunk boundary splitting a section was run.
- **v0.5.0 re-check:** the stored citation label for a Standing Order is unit-level, `SO ${currentOrderNumber}` (`lib/standing-orders-html.ts:210`). No paragraph-level pinpoint (for example "SO 89(1)") is stored or checked. Whether drafted answers add paragraph pinpoints, and whether those would be checked, was not assessed. [CI]
- **Assessment:** chunk/unit separation is implemented; v0.5 R9's institution-native pinpoint at the granularity relied on is not. **Partial** (was Implemented under v0.4 wording).

## R10. Provenance, expression and temporal applicability

- `documents` table (`infra/sql/002_core_tables.sql:6–20`): `source_url`, `source_checksum`, `edition`, `published_date`, `language`, `metadata`; `builds` table (line 22); `build_id` on `sections` and `chunks`. [CI]
- Source manifest: edition "2023"; `publishedDate` 2023-09-09 (Standing Orders) and 2023-11-09 (Speakers' Rulings). [CI]
- No commencement, amendment or repeal dates; answers do not state the edition. [CI]
- The pinned corpus is the 2023 edition. Migration to the 2026 edition is planned and in progress in a separate workstream, and is not reflected here. [CI for the pin; migration status as reported by the author, not observed]
- **Partial.**

## R11. Authority roles and relations

- `buildAuthorityProfile` (`lib/procedural-reasoning.ts:557`) assigns `AuthorityClass` and `AuthorityFunction` from hand-coded heading and path matches specific to this corpus. Deterministic, corpus-specific. [CI]
- `CONCEPT_REGISTRY` (`lib/concept-registry.ts:59`), 10 concept slots. [CI]
- v40 adjudication: the model nominates each source's role (`governing`, `qualification`, `implementation`); code rejects other roles and requires an admitted governing witness (`lib/ai/scenario-adjudication.ts:34, 169, 178–184`). Model-judged, code-enforced. [CI; ST: `tests/assurance.test.ts:37`]
- Selection logic is largely hand-tuned in `lib/v5-17-semantic-selector.js` (6,148 lines). Relations between units are not represented. [CI]
- **Partial** (SHOULD-level requirement).

## R12. Assurance states and failing closed

- **Streaming:** no unchecked draft text was found to reach the client (see "Answer paths"). [CI]
- **Fallbacks:** every fallback path found withholds model conclusions and shows a deterministic explanation and a list of authorities. No fallback path was found that bypasses the deterministic citation or exception checks. [CI]
- The final ordinary answer is sent with `degraded: true` only when evidence gaps exist (route line ~1279). The client stores `degraded` and `fallbackReason` (`hooks/useOpenOrderAssistant.ts:208–255`), but no component was found that displays them. [CI]
- No per-claim assurance states; no answer-level state vocabulary. [CI]
- `classifyAiError`, `publicFailureReason`, `runClaimValidationWithRetry` (`lib/ai/provider-resilience.ts:73, 188, 155`). [CI; ST: `tests/assurance.test.ts:62`]
- Outer error path forwards `error.message` for non-provider errors (see "Answer paths"). [CI]
- No fault-injection test of the full route was run. [ST: not run]
- **Partial.**

## R13. Portable safeguards

- Per-task provider routing: `getAiCandidates` (`lib/ai/routes.ts:61`), `lib/ai/index.ts`; Gemini and OpenAI-compatible endpoints (`lib/ai/openai-compatible.ts`). [CI]
- Portable (deterministic): witness checks, citation and pruning checks, same-unit exception veto, fallbacks. Configuration-dependent: scope judgements, claim validation, appeal judgement, role nomination. [CI]
- Deployed models and providers not observed [RC: none]. No per-model results; no open-weight configuration tested. [CI]
- **Partial.**

## R14. Status disclosure

- **User-facing:** the site footer (`components/open-order/Footer.tsx`, rendered by `app/page.tsx`) reads: "Open Order is an independent experimental parliamentary procedural navigator developed by KNIT." [CI]
- **Developer documentation only:** `docs/interfaces.md:3` adds "not an official parliamentary ruling or legal advice… check the original authority and its currency before relying on an answer"; `SECURITY.md` says "Do not treat generated answers as authoritative procedural rulings or professional advice." No equivalent user-facing statement was found in `app/` or `components/`. [CI]
- Answers link to parliament.nz source pages (R8). [CI]
- The deployed interface was not observed [PO: none].
- **Assessment:** independence is disclosed to users; the "not an official ruling or advice" statement and the direction to the authoritative publication are not, on the evidence found. **Partial.**

## R15. Source licensing, access and data governance

- `data/sources/source-manifest.json`: no licence or access-terms fields. `LICENSE-SCOPE.md` excludes parliamentary texts and derived corpora from the Apache-2.0 grant. [CI]
- **Query retention at the pin (disclosed historical gap):** `app/api/search/route.ts:117–140` inserts each search into `query_logs` (`infra/sql/002_core_tables.sql:87–97`) with the full `query_text`, corpus, result limit, latency, result count and debug metadata. No visitor identifier column exists in that table. [CI] Whether the answer endpoint's questions were retained elsewhere (for example in hosting or provider logs) was not assessed [RC/PO: none].
- No published data statement found at the pin. [CI]
- Changes to data handling in the separate build workstream are not reflected here.
- **Partial.**

## R16. Conformance by published, bounded evidence

- `tests/assurance.test.ts`: 11 tests, run in CI, covering parts of R2, R5, R11 and R12 plus input validation, TLS, rendering safety and schema stability. All 11 passed in a local run of the pinned code. [ST]
- No conformance report, evaluation set or plain-RAG baseline. [CI]
- **Not yet implemented.**

## R17. Evidential sufficiency

- Concept-slot completeness in the legacy selector (`missingRequiredSlots`) is a narrow role-completeness signal. Deterministic, corpus-specific. [CI]
- No coverage statement, retrieval-recall evaluation, cross-reference dependency analysis, or "selected evidence only" disclosure. [CI]
- **Not yet implemented.**

---

## Synthetic checks S1–S5

Run on 26 Nov 2026 against a copy of the pinned code outside the repository (`node --import tsx --test`). No repository files were changed.

| ID | Input | Result |
|---|---|---|
| S1 | "Bottom line:" section with one uncited and one cited line | Uncited line removed by `pruneValidatedAnswerContent`. |
| S2b | Uncited sentence before the first section heading | Survives pruning; not extracted as a claim. |
| S2c | Text inside a "Best authorities to inspect or cite:" authority line | Survives pruning; not extracted as a claim. |
| S3 | Answer with no citations | `validateAnswerCitations` returns `ok`. |
| S4 | Speaking-time example (§3.3) | Not vetoed by `findOmittedSourceQualifications` (modal-force error, outside the guard's scope). |
| S5 | Categorical claim omitting a same-subsection "unless" exception | Vetoed. |

---

## Re-check for v0.5.0

Same pin, same method. Only points where v0.5.0 wording changes what counts were re-examined. [CI unless stated] Section and profile references in this table are to v0.5.0 (for example, v0.5.0 §8.5 restricted terms is §7.4 in 0.6.0, and the v0.5.0 profile P1 corresponds to the 0.6.0 domain "parliamentary and institutional procedure").

| Req. | v0.5.0 wording change | Observation at the pin | Effect on maturity |
|---|---|---|---|
| R1 | Hedged and soft-modal statements count as substantive claims; practice-description basis | Synthetic findings S2b/S2c (uncited text outside the four sections survives) bear directly on soft-modal claims. No practice-description basis. | Partial (unchanged) |
| R2 | Ingestion authenticity separate from witness matching; normalisation policy MUST be published | `documents` records `source_url` and `source_checksum` of the fetched page; no record of an official manifestation or official checksum (parliament.nz publishes none that was found). Appeal normalises whitespace; no published normalisation policy. | Partial (unchanged) |
| R5 | Period and actor MUST for P1; stage MUST for procedural corpora; non-governing comparator marking | Actor, setting, action and stage are model-judged, code-enforced on the v40 path only; period not checked; no comparator marking. | Partial (unchanged) |
| R7 | Interim rule: apparent silence MUST default to retrieval uncertainty or coverage gap; new classes | The deterministic gap text expresses retrieval uncertainty, consistent with the interim rule; no other classes, no who-decides wording. | Partial (unchanged) |
| R8 | Printed citation form; response band; correction record | Printed form `SO n` present; no response band, no correction record. | Partial (unchanged) |
| R9 | Institution-native pinpoint at the granularity relied on | Unit-level label only (above). | **Partial (was Implemented)** |
| R10 | Expression, official/editorial status, per-provision dates, temporal object | Edition "2023" and publication date only; no expression type or temporal-object statement. | Partial (unchanged) |
| R11 | Minimal relation set MUST where structured metadata exists | The corpus is ingested from HTML without structured relation metadata; no relations represented. | Partial (unchanged) |
| R12 | Plain-language answer states; "Supported" expansion; restricted terms (§8.5) | No answer-state vocabulary. User-facing strings found: tooltip "Open authoritative source" (`components/open-order/ResultsList.tsx:315`) refers to the parliament.nz publication, which §8.5 allows; fallback reason "The AI draft could not be validated after pruning unsupported content." (`app/api/ai/answer/route.ts:743`) uses "validated" negatively, not as a property claimed for an answer. Stage label "Independently reviewing disputed source entailment" (route line 1023) is restricted by R6 and §8.5 unless the kind of independence is named. | Partial (unchanged) |
| R14 | Status facts on every surface incl. share/export; who decides; not a ruling or advice | Footer states independence only. Internal deep links are described as shareable (`app/page.tsx:23`); whether shared views carry the status statement was not assessed. No who-decides statement. | Partial (unchanged) |
| R15 | Per-corpus access and AI-use terms; retention shown in the interface; legislator sensitivity | No licence, access or AI-use fields in the manifest; no data statement; no in-interface retention notice; full search-query retention at the pin (disclosed historical gap). | Partial (unchanged) |
| R17 | Coverage statement (§5), per-answer question scope | None. | Not yet implemented (unchanged) |
| §5 | Te reo Māori questions accepted? Tikanga posture | Not assessed. | — |

---

## Note for Working Draft 0.6.0

No new inspection was made; the pin, the method and every finding above are unchanged. The 0.6.0 changes were compared against the existing findings. None changes an implementation-maturity assessment:

| Req. | 0.6.0 change | Bearing on the findings at the pin | Effect on maturity |
|---|---|---|---|
| R1 | A factual assumption may supplement, never substitute for, evidence of the rule asserted; uncertainty statements distinguish system limits from institutional silence | No factual-assumption or uncertainty-statement basis was found at the pin. | Partial (unchanged) |
| R5 | Dimensions are those declared decisive in the coverage statement; markings bounded to the system's own output channels | No coverage statement; model-judged dimensions on the v40 path only (above). | Partial (unchanged) |
| R7 | Silence alone cannot support a permission or prohibition conclusion; a separately sourced residual rule is needed | The deterministic gap text expresses retrieval uncertainty; whether any answer path drew permission or prohibition from silence was not assessed. | Partial (unchanged) |
| R12 | Only progress, retrieval information and source excerpts may be streamed; a displayed-then-rejected conclusion is a failure | Answer text is sent in one `answer_delta` event after checks; no draft text was found to be sent before checking (Answer paths, above). Consistent with the 0.6.0 streaming rule on the code inspected. | Partial (unchanged) |
| R14 | Status disclosure bounded to surfaces the system generates | Whether shared views carry status wording was not assessed. | Partial (unchanged) |
| R3, R4, R11, R17, R7 class assignment | "Design obligation" renamed **provisional** (definition pending) | Conformance result remains *definition pending*. | Unchanged |

## Note for Working Draft 0.6.1

Working Draft 0.6.1 changes wording and references only. It has no bearing on any finding above, and the pin, method, maturity counts and conformance results are unchanged.
