# Changelog

Versions follow SPECIFICATION.md §10 (§18 in 0.5.0; §14 in 0.4.0 and earlier). Requirement identifiers are never reused.

## Reviews behind each version

| Version | Reviews that informed it |
|---|---|
| 0.6.1 | A source-verification review of 0.6.0 (AAI-02), plus the author's list of wording and reference fixes. |
| 0.6.0 | The author's final revision brief, informed by structured AI-assisted reviews of 0.5.0: a simulated practitioner panel and a standards and legal-informatics review. Their findings were triaged; only those within the brief's bounded correction pass were taken. |
| 0.5.0 | Two AI-assisted critiques of 0.4.0 and follow-up review responses; no independent human expert review is claimed. |
| 0.4.0 | The author's final editorial instructions. |
| 0.3.0 | The author's critique and an internal review of 0.2. |
| 0.2 | An internal review of 0.1. |

## 0.6.1 (Working Draft, first public release dated 26 November 2026)

Wording and reference fixes after verification review. Final release preparation incorporated the author’s preface, the reserved version DOI, two R12 fixture corrections aligning expected results with the unchanged normative text, clarified review provenance, and replaced the Standing Order 2 quotation with an attributed paraphrase. No change to scope, normative requirements, conformance status or historical implementation evidence. Requirement identifiers R1–R17 are unchanged. The specification is about 12,750 words, about 11,900 before the references.

- §5 coverage note: SO 4 is paraphrased instead of partly quoted. The earlier SO 2 quotation was subsequently replaced with a paraphrase for the first public release (matching NOTICE).
- §7.3: the per-property example table is labelled as a hypothetical illustration of the reporting format, not a result for any implementation.
- §1.4: the mapping to Magesh et al. (2025) now uses the paper's own terms (misgrounding; naive retrieval, inapplicable authority, reasoning error, sycophancy; fabricated provisions) and is stated to be this draft's mapping, not the authors'. The reference gains the arXiv preprint number.
- §2.1: "epistemic authority" is identified as this draft's term; Raz's distinction is between practical and theoretical authority. The Hart and Raz references are stated more modestly.
- R15: Te Mana Raraunga's *Principles of Māori Data Sovereignty* (2018) given with its title italicised; the reference gains its URL.
- References: full title of LegalBench-RAG; DOI added for Parasuraman and Manzey (2010); Hohfeld page range (16–59) and Magesh page range (216–242) confirmed unchanged.
- Front matter: the ORCID record's registered name (Brendan John McBryde) is noted beside the iD.
- conformance/README.md: the summary line names the three evidence categories instead of "structural conformance", consistent with Structural conformance being proposed, not currently claimable.
- Version references updated to 0.6.1 in the title block, CITATION.cff, .zenodo.json, README, LICENSE attribution, CONTRIBUTING, drafts/WD-0000.md, conformance documents and the implementation matrix; evidence/open-order.md gains a one-line 0.6.1 note.

## 0.6.0 (Working Draft, publication candidate; not released, superseded by 0.6.1)

One bounded correction pass and a deliberate subtractive edit of 0.5.0, under the author's final revision brief. Requirement identifiers R1–R17 are unchanged; no requirement was added, removed or renumbered, and no annex, domain profile or fixture was added. The text was reduced from about 18,100 words to about 12,600, of which about 11,800 precede the references. Relocated material is held privately for future publications and is not part of this draft.

### Name and status
- Single title form everywhere: **"KNIT WD-0000 — Authority-Aware AI"**, version **Working Draft 0.6.0**.
- Founding principle reordered: "Authority-aware AI may reason about institutional authority but must not misrepresent, usurp, or silently assume it." §2.2 states that only undisclosed assumption is cured by disclosure; misrepresentation and usurpation are prohibited whether disclosed or not.
- "Design obligation" renamed **provisional** (definition pending) for R3, R4, R11, R17 and R7 class assignment. Interim operational rules are now labelled interim test methods.
- Structural conformance is **proposed, not currently claimable**. Conformance profiles (Structural, Advisory-grade) and thresholds were removed from the draft; individual defined properties may be assessed and reported with no overall claim (§7.3).
- New short legal-effect statement: the draft does not purport to create a duty of care, establish a legal safe harbour or determine an implementer's liability; conformance does not establish legal compliance or confer institutional authority or permission to provide regulated services.

### Scope
- Scope profiles P1–P3 replaced by a domain table (§1.2): parliamentary and institutional procedure (primary evidence base); other bounded institutional rule systems (intended application); primary and delegated legislation (future portability investigation); case law and mixed legal research (future extension); automated consequential decisions, AI exercising delegated authority and judicial decisions (outside scope). No P4 was added. Guidance an institution issues about its own rules is a source with the authority role *guidance*, not a domain. The word "profile" is no longer used for scope or deployment.
- Jurisdiction-specific prescriptions removed from the requirements and §5, keeping the principles (R4 role list, R5 profile-keyed dimensions, R10 commencement detail, interpretation-statute examples, R15 privacy-law and Māori-data examples generalised).

### Structure
- New order: front matter; 1 Scope; 2 Foundations; 3 Assurance model; 4 Terminology; 5 Coverage; 6 Requirements; 7 Conformance; 8 Research agenda; 9 Implementation evidence; 10 Stewardship; references; acknowledgements; licence and notices.
- Removed from the draft (held privately for later work): Annex A (theory), Annex B (standards compatibility and OASIS statement of intent), Annex C (Rules as Code), Annex D (NZ/AU public-law failure modes), Annexes E and F (mappings and related-work map), the §3.4 statutory example, §10 office-holder deployment, §11 regulatory interface, the §12 experiment designs including the Welsh demonstrator detail, the R7 domain silence table, and Open Order launch, telemetry and retention plans. §1.4–§1.5, §3.4, §13, §14, §15, §16, §17 and §18 were condensed into the new structure.
- Added a "Licence and notices" section to the specification so that the standalone PDF carries the licence and attribution notices.

### Requirement changes
| ID | Change |
|---|---|
| R1 | A factual assumption may supplement, never substitute for, evidence of the institutional rule, power or consequence asserted (worked example). Uncertainty statements must distinguish "the system cannot establish X" from "the institution has left X unresolved". Application-mode facts treated as assumptions (moved from §9). |
| R2 | Normalisation may not treat different words, numbers or negation as matching (moved from a fixture into the requirement). |
| R3 | Provisional. Interim rule kept as an interim test method. Annex A template reference removed. |
| R4 | Provisional. Enumerated role list reduced to the request/decide principle; NZ-specific evidence examples removed. |
| R5 | Dimensions are those the coverage statement declares decisive (institution and jurisdiction always); profile- and statute-specific dimensions removed; markings bounded to the system's own output channels. |
| R6 | "Independently verified/checked" describes checks, never answers or claims. |
| R7 | Silence alone cannot support a conclusion about permission or prohibition, and disclosure does not cure this; such a conclusion needs a separately sourced residual rule or interpretive principle. Classification SHOULD; misclassification MUST NOT. Domain silence table removed; SO 2 kept as an illustration. |
| R10 | Comprehensive commencement and transitional semantics removed; separate dates of making, effect, amendment, cessation, compilation and ingestion kept. |
| R11 | Provisional; interim relation set restated as an interim test method (resolves the SHOULD/MUST conflict). |
| R12 | Streaming: only progress, retrieval information and source excerpts may be streamed; displaying a conclusion later rejected is a failure even if retracted; corrections of supported conclusions on new evidence allowed. "No fallback path may" restated as MUST NOT. Useful-partial-answer SHOULD moved in from §9. |
| R13 | Two-configuration evidence softened to match the normative text. |
| R14 | Bounded to surfaces the system generates and the operator's own materials; "allow itself to be presented" removed; not-legal-advice statement aligned with §7.4. |
| R15 | Licence and terms recorded and published per corpus; Māori data-sovereignty principles given as an example of Indigenous data-sovereignty principles; jurisdiction-specific privacy example removed. |
| R16 | Per-property results; profile claims removed; "full or overall" conformance. |
| R17 | Uses the R7 classes; no universal thresholds. |

### Coverage statement (§5)
- Kept as foundational. Fields generalised (domain of application; interpretation regime absorbs interpretation statutes; rulings and later treatment; higher instruments; applicability dimensions; Indigenous and custodial authority).
- Brief coverage note for procedural corpora: leave (SO 3), suspension of Standing Orders and other orders (SO 4), Business Committee determinations (for example SO 59(2)) and sessional orders, checked against the Standing Orders 2023.
- Indigenous authority: implementations must establish and disclose a legitimate basis for their treatment of tikanga, te reo Māori and Te Tiriti-related authorities. KNIT's conservative exclusion is stated as KNIT's own posture for its own implementations, not a universal rule, and not proposed for Māori-governed implementations. The custodial-comment placeholder was removed; the authorship note now says independent review has not been obtained.

### Conformance (§7)
- Reporting framework, evidence categories, no aggregate score, why no overall claim is available, restricted terms, definition-pending criteria (including claim segmentation), and limits.
- Restricted terms: "legal advice" only where the provider is permitted to give it under the requirements of the jurisdiction concerned; commissioning or professional supervision alone does not establish that permission. Obligations bound to implementers' own materials.

### Consistency fixes
- Contradictions identified in review resolved where the text survives: "legal advice" between R14 and the restricted terms; "verified" between R6 and the restricted terms; where requirement keywords appear (now only §5–§7 and conformance/); R7 SHOULD vs MUST; R7/R17 taxonomies; R11 SHOULD containing a MUST; fixtures exceeding normative text; lower-case "may" in R12.
- CHANGELOG 0.5.0 entry corrected (P3 was "mixed legal research", not "official guidance"); CONTRIBUTING updated.
- LICENSE: attribution now "KNIT WD-0000 — Authority-Aware AI"; reference to a non-existent `rfcs/` folder replaced by `drafts/`.
- NOTICE matched to what is actually reproduced: SO 2 (with Parliament's CC BY 4.0 attribution) and one quotation from *Ellis v R*; no New Zealand enactment is quoted.
- CITATION.cff, .zenodo.json and README: repository URL omitted until a repository exists. Standing Orders reference now points to a working parliament.nz URL.

### Conformance and evidence
- Fixtures (existing only): each expected result now separates the mechanism-level result from the claim-level result (for example, R2-03: R2 witness integrity Pass; R3/R17 treatment of the omitted qualifier Conclusion withheld or conditional). R12-02 now treats a conclusion streamed and then rejected as a failure, and any logging as content-free operational events or synthetic test records, consistent with R15. corpus.yaml: STA given the same expression, status and checksum fields as SAR; placeholder checksums replaced with computed ones; amended compilation text supplied for R10-01/R10-03; questions added where missing; R9-03 reworded so that a heading alone is not a sufficient basis.
- evidence/: historical pin `a3f007e` unchanged; wording "v0.4 R3" and "v0.4 standard" clarified; cross-references updated; a note records that 0.6.0 changes alter no maturity assessment. Matrix unchanged: 0 implemented, 15 partial, 2 not yet implemented; conformance 12 not assessed, 4 definition pending, 1 split (R7).

## 0.5.0 (Working Draft, subject to author approval; not yet released)

Revision of the unreleased 0.4.0 in response to two AI-assisted critiques and follow-up review responses. Requirement identifiers R1–R17 are unchanged; no requirement was added, removed or renumbered. New obligations were folded into existing requirements, the new coverage statement (§5) or non-requirement sections.

### Name and status
- **Renamed** from "KNIT RFC-0000: Authority-Aware AI: An open specification for AI systems reasoning over institutional authority" to **"KNIT WD-0000 — Authority-Aware AI (Working Draft 0.5.0)"**, in the series KNIT Working Drafts. The former number KNIT RFC-0000 applies to versions 0.1–0.4.0. `rfcs/RFC-0000.md` moved to `drafts/WD-0000.md`; change proposals are now numbered CP-NNNN.
- Status: a public working draft of requirements and a conformance framework, not a standard. **No implementation can be fully conformant to 0.5.0**: R3, R4, R11, R17 and R7 class assignment are design obligations and cannot be reported as conformant.
- Abstract and §1.3: the requirements were abstracted from one procedural corpus; use for statute, regulation and guidance is intended, not demonstrated. Judicial decision-support is out of scope.

### New sections (non-requirement unless stated)
- §1.4 scope profiles P1 (internal institutional rules), P2 (enacted law), P3 (mixed legal research). *[Corrected in 0.6.0: this entry originally described P3 as "official guidance", which did not match the 0.5.0 text. Official guidance had no profile of its own in 0.5.0. Profiles P1–P3 were replaced in 0.6.0 by a domain table.]*
- §2.4 disclosure is necessary, not sufficient (automation bias).
- §3.4 purposive twin of the §3.3 example (fictional tenancy Act; Legislation Act 2019, s 10).
- §5 **coverage statement** (normative): fields for profile, jurisdiction, contents, authority roles, who decides, interpretation regime and statutes, case-law, secondary-authority and higher-law posture, temporal object, sources not held, question scopes, languages, te reo Māori, tikanga and Te Tiriti, and source terms. Tikanga, te reo legal questions and Te Tiriti are excluded from generated answers; a held text that states the point may be quoted without expansion.
- §8.3 conformance profiles: Structural (claimable, with a mandatory label) and Advisory-grade (not claimable in 0.5.0). §8.4 reportability. §8.5 restricted user-facing terms.
- §9 answer modes and useful partial answers. §10 deployment profile for tools aimed at office-holders. §11 regulatory interface and liability.
- §12 Experiment 0 (plain-RAG baseline on the Magesh et al. pattern); Welsh demonstrator narrowed to intra-Act claims, with pre-commitments.
- §13 related-work map, misgrounding mapped to layers, revised contribution statement.
- Authorship note on tikanga, te reo Māori and Te Tiriti.
- Annexes A (Raz, Hart, Hohfeld), B (standards compatibility; OASIS statement of intent), C (official encodings and Rules as Code), D (NZ/AU public-law failure modes), E (Linna and Linna; Butler and Butler mappings).

### Requirement changes
| ID | Change |
|---|---|
| R1 | Hedged and soft-modal statements are substantive claims; practice-description basis; scheme-level readings count as synthesis. |
| R2 | Ingestion authenticity separated from witness matching; normalisation policy MUST be published; compiled rulings are their own expression. |
| R3 | Interim operational definition of operative-text scope, rules (a)–(g), known incomplete; breach forbids an unqualified conclusion. Not reportable as conformant. |
| R4 | Renamed "Roles and allocated powers". Not reportable as conformant (role vocabulary pending). |
| R5 | Time and actor MUST for P1/P2; stage MUST for procedural corpora; non-governing comparators marked; markings survive share/export. |
| R6 | "Independently verified" and similar restricted unless property (b), (c) or (d) holds. |
| R7 | Three classes added (authority conflict, higher-law tension, facts incomplete); interim rule that apparent silence defaults to retrieval uncertainty or coverage gap; domain silence table; SO 2 and who decides. Class assignment not reportable as conformant. |
| R8 | Printed citation form; best stable link; triage response band; definition of material correction; correction record. |
| R9 | Institution-native pinpoints at the granularity relied on; headings non-operative; SHOULD use AKN eIds and ELI. |
| R10 | Renamed "Provenance, expression and temporal applicability"; per-provision dates; assent, commencement, consolidation and ingest distinguished; temporal object; no silent mixing. |
| R11 | Interim MUST: minimal relation set where structured metadata exists. Not reportable as conformant. |
| R12 | Plain-language answer states; "Supported" must expand; restricted terms. |
| R13 | Procurement and self-hosting emphasis. |
| R14 | Independence, commissioning/endorsement and proceedings use stated separately, on every surface including share/export; who decides; not a ruling, official advice or legal advice. |
| R15 | Per-corpus access and AI-use terms MUST be recorded; evidence must not depend on prohibited collection; Te Mana Raraunga principles SHOULD be applied; retention shown in the interface; office-holders' questions SHOULD NOT be retained identifiably. |
| R16 | Conformance profiles; interim-rule outcomes reportable alongside "definition pending". |
| R17 | Coverage statement MUST be published; per-answer question scope; subsequent treatment disclosed as a coverage limit. Not reportable as conformant. |

### Conformance and evidence
- conformance/README.md updated for 0.5.0; new illustrative Category A fixture specifications in conformance/fixtures/ (R2, R9, R10, R12), synthetic text only, not a suite.
- evidence/ re-checked at the same pin only where wording changed what counts. R9 moves from Implemented to Partial (unit-level citation labels; no sub-paragraph pinpoints). Matrix: 0 implemented, 15 partial, 2 not yet implemented; conformance 12 not assessed, 4 definition pending, 1 split (R7).
- NOTICE: attribution for the quotation of Standing Order 2; status of *Parliamentary Practice in New Zealand*; New Zealand enactments and judgments.

## 0.4.0 (prepublication revision, subject to author approval; not yet released)

Normative and editorial revision of the unreleased 0.3.0 candidate, following the author's final editorial instructions. Requirement identifiers and the count of 17 requirements are unchanged; no requirement was added, removed or renumbered. Before 1.0.0, minor versions may include normative changes (§14).

### Requirements: names and normative changes from 0.3.0

| ID | Short name (0.3.0) | Short name (0.4.0) | Normative change |
|---|---|---|---|
| R1 | Model output is a proposal | Generated output is a proposal, with a declared basis | Every substantive institutional claim needs a declared evidential basis: quotation, paraphrase, multi-source synthesis, factual assumption or uncertainty statement. A claim with no basis is not displayed as a conclusion. Connective prose and the person's own facts need no quotation. Passing checks confers no institutional authority. |
| R2 | Verbatim witness | Verbatim witness | Applies to every substantive institutional claim resting on quotation, paraphrase or synthesis, not only to claims attributed to a source. A witness for each source relied on. |
| R3 | Normative fidelity | Normative fidelity | A material unresolved condition, exception or qualification that could change the answer prevents an unqualified conclusion: conditional or withheld. Disclosure alone no longer suffices. |
| R4 | Roles, powers and standing | Roles, powers and standing | Unchanged in substance. |
| R5 | Applicability | Applicability | A source of unresolved applicability may be shown as conditional, potentially relevant evidence, but is not treated as governing. Per-dimension mechanism and outcome recorded. |
| R6 | Separation and independence of verification | Separation and independence of checks | Separation of proposal and checking required; appeal optional. If present, no self-reversal and no override of non-appealable vetoes. "Independent" must name its kind; a second call to the same model is not independent or expert review. |
| R7 | Classified uncertainty | Classified uncertainty | Unchanged in substance; cross-referenced from R17. |
| R8 | Inspectable evidence records | Inspectable evidence and correction | Evidence record includes per-claim assurance states and meaningful exclusions; no requirement to publish private questions, hidden prompts, secrets or sensitive logs. New challenge-and-correction pathway: documented, accessible, triage responsibility identified, substantiated defects corrected, material corrections traceable; correction of software, not appeal of institutional decisions. |
| R9 | Citation at the institution's unit of authority | (unchanged) | Unchanged. |
| R10 | Provenance, edition and temporal applicability | (unchanged) | Unchanged. |
| R11 | Authority roles and relations | (unchanged) | Unchanged. |
| R12 | Fail closed, with differentiated assurance states | Assurance states and failing closed | Per-claim states (supported, conditional, provisional, unsupported, unchecked) with display rules and transition rules; answer states (supported, partial, not answered) consistent with claim states. The 0.3.0 "unverified" answer state is removed: labelling an unchecked conclusion does not permit display. Streaming rules; no fallback may bypass an ordinary-path check. |
| R13 | Portable safeguards | (unchanged) | Must distinguish portable mechanisms from configuration-dependent performance. |
| R14 | Status disclosure | (unchanged) | Disclosure must be user-facing. Official source status distinguished from officially commissioned software. |
| R15 | Source licensing, access and data governance | (unchanged) | Truthful data statement (whether question text is retained, how long, who can access). Evidence and conformance needs are not a reason to retain private questions. |
| R16 | Conformance by published, bounded evidence | (unchanged) | Per-requirement results: conformant, not conformant, not assessed, definition pending, not applicable. Pending definitions cannot be conformant. Maturity reported separately. No full-conformance claim while any applicable MUST is unmet or unassessed. Required report metadata extended. |
| R17 | Evidential sufficiency | (unchanged) | No claim or implication of exhaustive search. Must distinguish known omissions, coverage limits, retrieval uncertainty and interpretive uncertainty. Insufficient support means conditional or withheld, not categorical with a caveat. |

### Foundations and layers
- §1.3: requirements state outcomes, not architectures; assessable for systems with one model, several, or none.
- §2: the five behavioural constraints renamed to grounded, faithful, applicable, honest about uncertainty, inspectable and correctable.
- New §3.2, mechanisms: deterministic; model-judged, code-enforced; prompt-only; human review; not implemented. Not every layer can always be checked mechanically.
- §4: added "substantive institutional claim" and "evidential basis".

### Conformance
- conformance/README.md: per-requirement result states; maturity separate from results; fixture classes (uncited claims, fake and irrelevant witnesses, multi-source conclusions, cross-unit exceptions, missing instruments, unknown coverage, wrong jurisdiction/actor/stage/period, no-appeal eligibility, veto bypass, misleading independence claims, failures and partial success, streaming consistency, synthetic correction-pathway demonstration); extended report metadata.

### Evidence
- Re-examined at the same pin, `a3f007e`, whose application code is identical to its parent `4ce15ce` (runtime assurance commit). Every finding labelled by method (code inspection, synthetic test, runtime configuration, production observation). Ordinary, streaming, fallback and error paths described.
- Matrix now separates implementation maturity from conformance (all "not assessed"). Maturity: 1 implemented, 14 partial, 2 not yet (0.3.0: 3 / 12 / 2). R2 and R14 reassessed as partial.
- Corrected two 0.3.0 statements: uncited lines inside the four substantive answer sections are removed deterministically (0.3.0 said uncited claims were not caught); source-link text fragments use the first ten words of the section, not the cited words.
- Full search-query retention at the pin disclosed as a historical gap against R15. No claim that Open Order collects only aggregate data. Edition migration described as planned and in progress.

### Related work and status
- Literature search described as limited and non-exhaustive. Quotations and reference metadata rechecked against original sources.
- Welsh demonstrator conditional on source rights and temporal coverage, independent domain review and Welsh-language review.
- Status, version and archive fields made consistent; no publication date or DOI is stated until they exist.

### Repository
- NOTICE: Parliament attribution wording settled; no Parliament text is reproduced in this repository.
- Contact address added to CONTRIBUTING.md and CODE_OF_CONDUCT.md.

## 0.3.0 (unpublished prepublication candidate, 26 Nov 2026)

Prepared as the first public version; not released. Substantive conceptual and editorial revision of the unpublished v0.2 draft, following the author's critique and an internal review.

### Foundations
- **Withdrawn:** the v0.2 claim that a system "does not become an authority" when five conditions are met. The conditions cannot establish that; they constrain behaviour.
- **Added §2.1:** normative, interpretive and epistemic authority. A useful system will acquire epistemic authority; the aim is that it is never mistaken for, and never displaces, institutional authority.
- **Added §2.2, founding principle:** "Authority-aware AI may reason about institutional authority but must not silently assume, misrepresent or usurp it."
- **Recast §2.3:** the five conditions are now behavioural constraints (witnessed, faithful, applicable, honest about uncertainty, inspectable), not proof.
- **Added §1.3, scope:** this RFC covers advisory systems over institutional texts. Delegated authority and procedural standing are left to a later RFC, not excluded.
- **Added §1.4:** Open Order informs the specification but is not its canonical interpretation, stated as a deliberate parallel with working paper 2.

### Assurance layers
- **Added §3:** four layers: L1 textual integrity, L2 source admissibility, L3 semantic fidelity, L4 evidential sufficiency, each with what it establishes and how it is checked.
- **Added §3.2:** fictional speaking-time example showing an authentic quotation accompanying a wrong conclusion.
- **Added §3.3:** fidelity to selected evidence versus fidelity to the institution's complete applicable rules. Evidential sufficiency made both a requirement (R17) and an open research problem (§12 Q1).
- Every requirement is now tagged with layer(s), conformance category and evidence of conformance.

### Requirements: mapping from v0.2

| v0.3 | Short name (v0.3) | v0.2 | Short name (v0.2) | Change |
|---|---|---|---|---|
| R1 | Model output is a proposal | R1 | Model output is a proposal | Validation establishes admissibility under specified checks, never authority. |
| R2 | Verbatim witness | R2 | Verbatim witness | Added: a witness check must not be reported as claim support (L1 is not L3). |
| R3 | Normative fidelity | R3 | Fidelity to normative force, conditions and exceptions | Extended to material cross-references: resolve or disclose. "Power" added to normative forces. |
| R4 | Roles, powers and standing | R4 | Who may ask versus who decides | Generalised from request/decide to roles and powers (initiate, propose, object, decide, delegate, review). |
| R5 | Applicability | R5 | Scope check before admission | Institution and jurisdiction now MUST dimensions; period added; unresolved applicability must be withheld or disclosed; mechanism per dimension recorded. |
| R6 | Separation and independence of verification | R6 | Separation of roles and non-reversible rejection | Four distinct properties: functional separation, independence of mechanism, model/provider independence, institutional/human review. "Independent" must name which. |
| R7 | Classified uncertainty | R7 | Honest about silence | Four classes: corpus silence, coverage gap, retrieval uncertainty, interpretive uncertainty, each with its own disclosure. |
| R8 | Inspectable evidence records | R8 | Visible working and links to the official text | Now an evidence record of sources, exclusions and checks; explicitly does not require disclosure of internal model reasoning. |
| R9 | Citation at the institution's unit of authority | R9 | Citation at the institution's unit of authority | Kept as a core principle; rationale extended. |
| R10 | Provenance, edition and temporal applicability | R10 | Provenance and edition | Publication, commencement, amendment and repeal dates distinguished; date-specific applicability. |
| R11 | Authority roles and relations | R11 | Selection by authority role | Relational authority recognised (authorises, qualifies, overrides, amends, repeals, interprets, delegates, incorporates by reference, applies subject to, has equal authority with); full modelling is future work. |
| R12 | Fail closed, with differentiated assurance states | R12 | Fail closed, visibly | Four assurance states (supported, partial, unverified, not answered); partial answers defined. |
| R13 | Portable safeguards | R13 | Vendor independence | Safeguards must travel; performance reported per model and not assumed to transfer. |
| R14 | Status disclosure | R14 | No claim to official status | Distinguishes independent advisory systems from officially commissioned or authorised ones. |
| R15 | Source licensing, access and data governance | R15 | Honour source terms | Three distinct obligations; publish what is recorded about people who use the system. |
| R16 | Conformance by published, bounded evidence | R16 | Conformance by published evidence | Required report metadata; no aggregate score; every MUST to have an operational definition or say it has none. |
| R17 | Evidential sufficiency | — | (new) | Do not present fidelity to selected evidence as fidelity to the complete applicable rules; disclose the basis for sufficiency and known gaps. |

### Structure
- Open Order code traces moved out of the normative text into evidence/open-order.md and evidence/implementation-matrix.md, re-checked at `a3f007e` with line numbers.
- Conformance framework moved to conformance/README.md and named the Authority-Aware AI Conformance Suite. Three categories (A structural, B semantic fidelity, C institutional accountability), no aggregate score, required report metadata, and an explicit statement that passing the tests means passing those tests.
- Document designated KNIT RFC-0000 in the KNIT Specifications series, with an explicit statement that it is not an IETF RFC, not a standard and not peer reviewed.

### Generality
- "Clean-room build" replaced by a **cross-domain portability demonstration**. "Prove generality" replaced by "test generalisability".
- Three experiments: shared components (architectural portability); external developer from documentation and components (developer accessibility); specification-only implementation (implementation-independent generality; longer-term or stretch goal).
- Wales figures corrected: 177 sections in the current revised text (176 as enacted, plus s 115A); 1,245 cross-reference elements in the current revised English Akoma Ntoso.

### Related work
- Novelty claim narrowed to the integration of institutional authority, normative fidelity, evidence verification, contestability and implementation-independent conformance into one open specification. No claim to have coined "authority-aware AI".
- Added LegalBench-RAG, Legal RAG Bench, LegalCiteBench, Linna and Linna (2026), Ulizko et al. (2026), LegalRuleML, and a brief note on formal and computational legal reasoning.

### Language and status
- "Offered to every MP" described as a prospective launch population, not users or adoption.
- Opening for comment described as creating conditions for collaboration, not as collaboration.
- Added a visible Acknowledgement of AI assistance section.
- Kept: preface reserved for the author; "working papers in preparation"; no per-paper outputs or milestones.

### Repository
- Added README, CONTRIBUTING (30-day window, RFC process), GOVERNANCE (KNIT stewardship; transfer deferred until independent participation exists), CODE_OF_CONDUCT (Contributor Covenant 2.1), CITATION.cff with ORCID, .zenodo.json, LICENSE (CC BY 4.0), LICENSE-CODE (Apache-2.0), NOTICE (third-party source licences).

## 0.2 (unpublished internal draft, 26 Nov 2026)
Applied an internal review: R5/R13 determinism corrected; working papers described as in preparation; Rules as Code paragraph revised; RegLab JELS citation; February 2027 offer and data statement; how-to-comment section.

## 0.1 (unpublished internal draft, 26 Nov 2026)
First draft: definition, five conditions, R1–R16 with Open Order traces, conformance approach.
