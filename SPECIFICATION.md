# KNIT WD-0000 · Authority-Aware AI

**Working Draft 0.6.1 · Public working draft: requirements and a conformance reporting framework**

*Requirements for advisory AI systems that answer from bounded, declared corpora of institutional texts. Not a standard.*

| | |
|---|---|
| **Document** | KNIT WD-0000 (numbered KNIT RFC-0000 in versions 0.1–0.4.0; see CHANGELOG) |
| **Title** | KNIT WD-0000 · Authority-Aware AI |
| **Series** | KNIT Working Drafts |
| **Version** | Working Draft 0.6.1 |
| **Status** | Public working draft for comment; not a standard. |
| **Release date** | 26 November 2026 |
| **Author** | Brendan McBryde, KNIT ([ORCID 0009-0004-0425-7214](https://orcid.org/0009-0004-0425-7214), registered as Brendan John McBryde) |
| **Licence** | Specification text: CC BY 4.0. Code and test fixtures: Apache-2.0. Quoted third-party texts keep their own terms (see Licence and notices, and NOTICE). |
| **Canonical discussion** | [KNIT-NZ/authority-aware-ai](https://github.com/KNIT-NZ/authority-aware-ai) |
| **Archived version** | [10.5281/zenodo.24546015](https://doi.org/10.5281/zenodo.24546015) |
| **Evidence base** | One implementation (Open Order) over one procedural corpus (Standing Orders and Speakers' Rulings of the New Zealand House of Representatives, 2023), at commit `a3f007e649ce6b203bbc2201aaba7ea15b349cac` |

---

## Preface

This specification has emerged, as if by its own volition, from my attempts to rectify some of the institutional deficiencies that I believe are constraining our democratic representation. What began as a straightforward experiment in natural language interaction with procedural documentation has become a fascinating and generalisable set of technical principles governing how AI interacts with authority in ways that break down barriers without creating new kinds of obfuscation.

Some legal and institutional paths cannot be imagined until their predecessors exist, and indeed until some deprecated precedents are superseded.

This draft is one step on a path without a clear destination.

---

## Status of this document

**This is a public working draft. It is not a standard.** It has not been through any standards process, peer review or ratification. "WD" is KNIT's own series label. Earlier drafts were numbered KNIT RFC-0000; they were never IETF RFCs, and the label was dropped to avoid any suggestion that they were.

**No overall conformance claim is currently available.** R3, R4, R11, R17 and the assignment of uncertainty classes under R7 are **provisional**: their outcomes are stated, but the operational definitions needed to report them as conformant are pending. Structural conformance is **proposed, not currently claimable**. Individual defined properties can still be assessed and reported (§7).

**Evidence base.** The requirements were abstracted from one implementation over one procedural corpus: the Standing Orders and Speakers' Rulings of the New Zealand House of Representatives. They are written to be general, but their application to legislation, case law and mixed legal research has not been demonstrated (§1.2).

**Legal effect.** This draft does not purport to create a duty of care, establish a legal safe harbour or determine an implementer's liability. Conformance with it does not establish legal compliance, and does not confer institutional authority or permission to provide regulated services.

The initial public comment window runs from 26 November to 26 December 2026 (New Zealand dates; see CONTRIBUTING.md). An invitation to comment is not evidence that anyone has participated. Any influence comments have on later versions will be recorded in CHANGELOG.md.

---

## Abstract

AI systems that answer questions from institutional texts acquire a form of authority through usefulness. The risk is that this authority is mistaken for, or displaces, the authority of the institutions whose texts they read.

This draft specifies **authority-aware AI**: AI that may reason about institutional authority but must not misrepresent, usurp, or silently assume it. Its central user-facing implication is simple: **an answer that is faithful to the text a system retrieved is not thereby faithful to the rules that apply** (R17).

The draft distinguishes normative, interpretive and epistemic authority; sets out four layers of assurance (textual integrity, source admissibility, semantic fidelity and evidential sufficiency); requires a published coverage statement declaring what a corpus holds, how it is to be read and who decides (§5); and states seventeen requirements (R1–R17) for advisory systems, each tagged by layer and evidence category. Conformance is reported through published, bounded evidence, in three separately reported categories, with no aggregate score.

The requirements were abstracted from one implementation, Open Order, over the Standing Orders and Speakers' Rulings of the New Zealand House of Representatives. Application to other bounded institutional rule systems is intended; application to legislation, case law and mixed legal research is not demonstrated.

---

## 1. Scope

### 1.1 The problem

Retrieval-augmented generation (RAG) retrieves passages that look relevant and asks a language model to answer from them. Retrieval narrows what the model sees; it does not check what the model then says. For institutional texts the characteristic failures concern how the answer relates to the authority of its sources:

1. **Altered or invented quotations.** Words presented as quoted that are not in the source.
2. **Dropped conditions and exceptions.** "X must do Y" where the source says "unless Z", or another provision qualifies the rule.
3. **Changed normative force.** "May" rendered as "must"; a discretion rendered as an entitlement.
4. **Collapsed roles.** A right to request reported as a power to decide; one office's power attributed to another.
5. **Applicability errors.** A rule for a different forum, actor, stage or period applied as if it governed.
6. **Inference from silence.** The absence of a provision treated as permission or prohibition.
7. **Temporal drift.** An answer resting on a superseded or not-yet-effective text without saying so.
8. **Opaque working.** No way for the person relying on the answer to see what was considered, admitted or excluded, or to report an error.

The problem is documented. A preregistered evaluation of commercial AI legal research tools found that they "each hallucinate between 17% and 33% of the time", counting a response as hallucinated "if it is either incorrect or misgrounded" (Magesh et al., 2025). POPVOX Foundation added scope-limited refusals to its assistant for US congressional staff: "This is an attempt to ensure StaffLink will not guess when it lacks authority" (POPVOX Foundation, 2025). Grounding is necessary but not sufficient: a grounded answer can still claim more than its sources give.

### 1.2 Domain of application

This draft applies to **advisory systems reasoning over bounded, declared corpora of institutional texts**: systems that answer questions about what a defined body of authoritative texts provides, for a person who will make their own judgement or decision. The requirements state outcomes, not architectures, and are intended to be assessable in systems that use one model, several models, or no model at all.

| Domain | Standing in this draft |
|---|---|
| Parliamentary and institutional procedure | **Primary evidence base.** One implementation over one corpus. |
| Other bounded institutional rule systems | **Intended application.** Not demonstrated. |
| Primary and delegated legislation | **Future portability investigation.** Not demonstrated. |
| Case law and mixed legal research | **Future extension.** Not demonstrated. |
| Automated consequential decisions; AI exercising delegated authority; judicial decisions | **Outside scope.** |

Guidance that an institution issues about its own rules is not a separate domain: where held, it is a source with the authority role *guidance* (§5) within whichever domain its corpus falls. The excluded systems are not excluded on principle; requirements for them would be later work. This draft does not define how to interpret any law or rule, replace courts, presiding officers, officials, clerks or professional advice, ensure correctness, prescribe an architecture, or define custodial or Indigenous data-sovereignty terms or the content of tikanga, which belong to their custodians (§5).

### 1.3 Relationship to Open Order

Open Order is the implementation from which these requirements were first abstracted. It informs the specification. It is **not** its canonical interpretation. Where Open Order and this document disagree, this document governs, and the disagreement is a defect in Open Order, in this document, or in both, to be resolved in public. The normative text does not refer to Open Order's code. Implementation evidence is summarised in §9.

### 1.4 Related work and contribution

The search behind this section was limited and non-exhaustive. Related work includes citators and point-in-time legislation services; document and identifier standards (Akoma Ntoso, FRBR, ELI), which R9 and R10 use where present; rule representation (for example LegalRuleML), which offers stronger L3 and L4 mechanisms; legal RAG evaluation (Magesh et al., 2025; Pipitone and Houir Alami, 2024; Butler and Butler, 2026); and requirements for AI in adjudication (Linna and Linna, 2026), which concern judicial AI, outside this draft's scope.

Magesh et al. (2025) count a cited response as misgrounded where its sources are misinterpreted or inapplicable, and classify contributing causes as naive retrieval, inapplicable authority, reasoning error and sycophancy; they also report fabricated provisions. In this draft's terms, fabricated or misquoted text is an L1 failure (R2, R9), inapplicable authority an L2 failure (R5, R10), misinterpretation and reasoning error L3 failures (R3, R4), and a failure to retrieve the governing source an L4 failure (R7, R17). This mapping is this draft's own, not the authors'.

This draft's proposed contribution is to **bind retrieval, citation checking and rule representation to institutional standing** (who holds which authority, and who decides), **to fail-closed display** (what may not be shown as a conclusion), **to a declared coverage statement**, and **to published, non-aggregable conformance reporting**, in one set of requirements that implementations of any architecture can be assessed against. It claims integration, not priority, and does not claim to have coined the term "authority-aware AI".

---

## 2. Foundations

### 2.1 Three kinds of authority

| Kind | Meaning | Who holds it in the cases this draft covers |
|---|---|---|
| **Normative authority** | The legitimate power to establish binding rules, confer rights or impose obligations. | Legislatures, rule-making bodies, delegated rule-makers; for a legislature's internal rules, the house itself. |
| **Interpretive authority** | The recognised institutional competence to determine what those rules mean in particular circumstances. | Different offices in different settings: for parliamentary procedure, typically the presiding officer, guided by previous rulings and practice; for enacted law, courts and tribunals, and designated officials for the powers they administer. |
| **Epistemic authority** | The credibility or influence a person or system acquires through perceived knowledge and reliability. | Anyone, or anything, people come to rely on: clerks and advisers, practice texts, citators, and AI systems. |

Interpretive authority is not one thing: offices that advise carry weight without ruling, and a procedural ruling is not the same kind of act as a court's construction of a statute. The coverage statement records which offices decide which questions (§5).

An advisory AI system holds neither normative authority nor official interpretive authority. If it is useful and reliable, it will acquire epistemic authority. That is not in itself a fault. The fault this draft addresses is narrower: epistemic authority being **mistaken for** institutional authority (the system's reading is taken to be the institution's), or **displacing** it (people stop consulting the institution's text or its decision-makers because the system's reading seems sufficient). "Epistemic authority" is this draft's term. The distinction is informed by Raz's distinction between practical and theoretical authority (Raz, 1986; 2009) and, loosely, by Hart's account of the rule of recognition (Hart, 2012); the vocabulary of roles and powers in R3 and R4 is informed by Hohfeld (1913). Nothing here depends on a particular reading of their work.

### 2.2 Founding principle

> **Authority-aware AI may reason about institutional authority but must not misrepresent, usurp, or silently assume it.**

The words "may" and "must" in this sentence are used in their ordinary sense, not as requirement keywords. Each prohibited act corresponds to a failure:

- **Misrepresent:** stating that a source says, permits, requires or empowers something it does not, or omitting what qualifies it.
- **Usurp:** presenting the system's output as a ruling, a decision or official advice, or standing in for the person or body who decides.
- **Silently assume:** acting, without saying so, as though an interpretive question is settled when it is not, or as though a fact about the situation holds.

**Only undisclosed assumption is cured by disclosure.** An advisory system will often need to reason about authority: which provision governs, whether an exception applies, who decides. Doing so on a stated assumption is permitted, provided the assumption is visible and the rest of the answer meets the requirements (an assumption may supplement, but never substitute for, evidence of the rule asserted: R1). Misrepresentation and usurpation are prohibited whether disclosed or not. A caveat does not make a misstatement of the source faithful, and a label does not make it acceptable to present the system's reading as carrying the institution's weight.

### 2.3 Five behavioural constraints

The requirements apply five constraints to every substantive institutional claim. The claim should be:

1. **grounded:** resting on a declared evidential basis, with verbatim text from each source relied on, checked against the stored text;
2. **faithful:** preserving the source's normative force, conditions, exceptions, and the roles and powers it assigns;
3. **applicable:** within the source's scope, or presented as conditional where applicability is unresolved;
4. **honest about uncertainty:** withheld or made conditional, with the kind of uncertainty stated, when the admitted sources do not settle the point;
5. **inspectable and correctable:** presented with an evidence record the person can check against the official text, and open to challenge through a correction pathway.

These are constraints on behaviour. They do not prove that a system has not acquired authority, and they do not establish that its conclusions are correct.

### 2.4 Disclosure is necessary, not sufficient

Labels, status statements and assurance states are necessary. They do not prevent reliance. People use the tool that answers fastest, and over-reliance on automated aids is well documented (Parasuraman and Manzey, 2010). This draft does not claim that disclaimers prevent displacement of institutional authority. Its main safeguards are therefore behavioural rather than presentational: what a system declines to display as a conclusion (R3, R7, R12, R17), and what it must route to the person who decides (R7, R14).

---

## 3. Assurance model

### 3.1 Four layers

An answer can be right in one respect and wrong in another. This draft separates four things an implementation might establish about a claim, because they are established by different means and fail in different ways.

| Layer | What is established | Typical method |
|---|---|---|
| **L1 Textual integrity** | The quoted words exist, exactly, in the identified source unit and expression, and the stored text is traceable to the manifestation it was ingested from. | Deterministic comparison against stored text; ingestion authenticity records (R2). |
| **L2 Source admissibility** | The source has the requisite authority and applies to the circumstances: institution, jurisdiction, actor, setting, action, stage and period. | Structured rules over source metadata, plus interpretive assessment where structure runs out. |
| **L3 Semantic fidelity** | The conclusion preserves the meaning and normative implications of the source, read as the declared interpretation regime requires (§5): force, conditions, exceptions, discretion, roles and powers. | Formal checks where possible; otherwise model-based or expert judgement. |
| **L4 Evidential sufficiency** | The relevant sources, taken together, support the conclusion within the declared question scope, with no material omission. | Retrieval evaluation, dependency analysis and expert assessment. |

Each layer depends on those before it but is not implied by them. Only L1 can, in general, be established mechanically. L2 can be partly so where sources carry structured metadata, but recognising a valid source is ultimately practised by officials, not only encoded in data. L3 and L4 generally require judgement, and no current method establishes L4 in general (§3.5).

### 3.2 Mechanisms

Implementations and conformance reports describe each check by mechanism:

| Label | Mechanism |
|---|---|
| **Deterministic** | Code whose result does not depend on a model's judgement. |
| **Model-judged, code-enforced** | A model makes the judgement; code acts on the result (for example, by rejecting a source the model did not affirm). |
| **Prompt-only** | An instruction to a model, with no separate check of whether it was followed. |
| **Human review** | A person assesses the output, at runtime or in evaluation. |
| **Not implemented** | No mechanism exists for the property. |

A model-judged check is only as reliable as the judgement behind it, and **a prompt-only measure is not a check**. Neither may be described as deterministic (R6, R16). A checker built on a formal rule representation is deterministic for what it encodes, and its encoding is itself an interpretation with its own provenance.

### 3.3 An authentic quotation can accompany a wrong conclusion

Consider an entirely fictional provision:

> *A member may request an extension of speaking time. The chair may grant the request if satisfied that exceptional circumstances exist.*

And a generated claim:

> *A member is entitled to an extension of speaking time in exceptional circumstances.*

| Check | Result |
|---|---|
| The source exists | Yes |
| The quotation is authentic (L1) | Yes |
| The citation identifies the correct provision | Yes |
| The question concerns the correct institutional setting (L2) | Yes |
| The claim preserves the source's normative force (L3) | **No.** "May request" has become "is entitled". |
| The claim preserves the decision-maker's discretion (L3) | **No.** The chair's discretion, and the chair's role as decider, have disappeared. |
| The claim is semantically supported | **No** |

Every structural check passes and the conclusion is wrong. Verbatim quotation (R2) is a strong safeguard at L1 and no safeguard at L3. Requirements are tagged by layer so that an implementation cannot claim assurance at one layer on the strength of checks at another.

### 3.4 Interpretation regime

A reading that is faithful to one unit's words can still be unfaithful to how the institution requires its texts to be read: together with a purpose provision, a definition elsewhere, an emergency exception, or a higher instrument. This draft does not prescribe how any institution or jurisdiction interprets its texts. It requires a system to declare the interpretation regime it assumes (§5), assesses L3 relative to that declaration, and forbids presenting a unit-level reading as settled where the declared regime leaves the point open (R3).

### 3.5 Evidential sufficiency, fidelity to what, and question scope

A system can faithfully interpret every source it retrieves and still give a wrong answer, because a governing exception, a later amendment or a qualifying ruling sits somewhere it did not retrieve. That is a failure at L4. This leads to a distinction this draft treats as basic:

- **Fidelity to the selected evidence:** the answer is faithful to the sources the system admitted.
- **Fidelity to the institution's complete applicable rules:** the answer is faithful to everything the institution has made applicable.

Most checking techniques establish at most the first. Implementations must not present the first as the second (R17).

Establishing sufficiency in general is an **open research problem**; an unbounded test would push almost every answer into conditionality. This draft therefore makes sufficiency relative to a **declared question scope** (§5): the bounded question the system is answering, such as "within the Standing Orders and Speakers' Rulings held, not including practice texts". Sufficiency within a declared scope is assessable; sufficiency without one is not claimed.

### 3.6 Answer modes and useful partial answers

Answers that **describe texts** ("what does the rule on points of order say?") and answers that **apply texts to a person's situation** ("can I raise this point of order now?") carry different risks. Application is closer to advice, depends on facts the system may not have, and is where reliance does most harm. R1 and R12 therefore treat the facts an application turns on as declared assumptions or incomplete facts, and favour a conditional conclusion over a qualified categorical one.

Failing closed must not become failing empty: over-refusal pushes people toward unconstrained tools. A withheld conclusion that comes with the relevant source excerpts and links, the bounded conclusions that are supported, the classified uncertainty, the coverage limits, and who decides is a useful answer (R12). An apology without them is not.

### 3.7 Tagging

Each requirement in §6 carries:

- **Layer(s):** L1–L4, or **X** (cross-cutting: properties of the system rather than of a single claim).
- **Category:** **A** structural, **B** semantic fidelity, **C** institutional accountability (§7.2).
- **Status:** **reportable** (a conformant result can be reported against it), or **provisional** (the outcome is stated but its operational definition is pending, so results are reported as "definition pending", optionally with interim test-method outcomes; §7.5).
- **Evidence of conformance:** what a report must show, or a statement that the definition is pending.

---

## 4. Conventions and terminology

**Requirement keywords.** The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY and OPTIONAL are to be interpreted as described in BCP 14 (RFC 2119, RFC 8174) when, and only when, they appear in all capitals. They appear only in §5, §6 and §7 and in conformance/; elsewhere, lower-case words carry their ordinary meaning. Their use does not make this document a standard.

| Term | Meaning |
|---|---|
| **Institutional text** | A text issued by an identifiable institution with normative or interpretive authority. |
| **Corpus** | The bounded, declared set of institutional texts an implementation answers from. |
| **Domain of application** | One of the rows of the table in §1.2. |
| **Coverage statement** | The published declaration of what a corpus holds, how it is to be read, who decides, and what it does not hold (§5). |
| **Question scope** | The bounded question an answer addresses, relative to the coverage statement (§3.5). |
| **Source unit** | The unit the issuing institution itself cites (section, standing order, article, ruling), with its institution-native sub-units (subsection, paragraph, item). |
| **Chunk** | A retrieval unit derived from a source unit. Not citable on its own. |
| **Expression** | A particular version of a source unit's text: as made, as amended at a date, or as compiled by an editor (FRBR *expression*). |
| **Manifestation** | A particular published embodiment of an expression: an official PDF, an XML file, a web page (FRBR *manifestation*). |
| **Authority role** | The role a source plays: rule, exception, ruling, guidance, extrinsic aid, secondary commentary, official encoding, practice record (§5). |
| **Substantive institutional claim** | A statement about what an institutional text provides, permits, requires, prohibits or empowers; about whether it applies; about how the institution applies it in practice; or a conclusion drawn from such statements. Includes hedged and soft-modal statements ("members usually need leave"); excludes restatements of the person's own facts and navigational prose. Segmentation for scoring is definition-pending (§7.5). |
| **Evidential basis** | The declared ground for a substantive institutional claim (R1). |
| **Witness** | A verbatim quotation from a source unit, offered in support of a claim: either one contiguous span or an explicitly enumerated set of spans from the same unit. |
| **Ingestion authenticity** | The traceability of stored text to an official or declared manifestation (R2). Distinct from witness matching. |
| **Proposal** | Any generated output before the checks that apply to it have run. |
| **Veto** | A deterministic check whose rejection cannot be overturned. |
| **Evidence record** | The inspectable record of how an answer was produced (R8). |
| **Assurance state** | The label attached to a claim, and summarised for an answer (R12). |
| **Answer mode** | Description of texts, or application to a situation (§3.6). |
| **Surface the system generates** | The system's own interface, share links, exports and print views. Copies made by others are not. |
| **Provisional requirement** | A requirement, or part of one, whose outcome is stated but whose operational definition is pending, so that it cannot yet be reported as conformant (§7.5). |

---

## 5. Coverage statement

The coverage statement is foundational: it makes "sufficient" and "who decides" mean something bounded, and is the reference point for R5, R7, R10, R14, R15 and R17. An implementation MUST publish a coverage statement for each corpus, and MUST make a short form of it available on every surface the system generates where answers appear. It MUST declare at least the following. Where a field is unknown, the statement MUST say so; "unknown" is a declaration, not a gap to be filled by inference.

| Field | What must be declared |
|---|---|
| **Domain of application** | The row of §1.2 the corpus falls in. |
| **Institution and jurisdiction** | Who issues the texts, and where they apply. |
| **Contents** | Each instrument held, with its expression, official manifestation (where one exists) and checksum (R10). |
| **Authority-role catalogue** | The roles sources play (§4) and how each is displayed. Secondary commentary and official encodings are never displayed as governing unless the institution has adopted them. |
| **Who decides** | The offices that decide which kinds of question for this corpus. Used in R7 and R14 disclosures. |
| **Interpretation regime** | How the corpus is to be read (for example textual, purposive or mixed); whether extrinsic materials are in or out; and the interpretation rules and definition provisions that govern it, and whether they are always retrieved. L3 is assessed relative to this declaration. |
| **Rulings and later treatment** | Whether rulings, decisions or case law are excluded, held as editorial summaries only, or held as a distinct authority role; and, where they are held without a record of later treatment, that subsequent treatment is a declared coverage limit. |
| **Secondary authority, convention and practice** | Which practice texts, manuals and commentaries are held or not held, and whether unwritten convention and established practice are represented, with the user-facing disclosure used when they are not. |
| **Higher instruments** | Whether instruments that may require the corpus to be read in a particular way are held. If not, a declared coverage limit (R7, R17). |
| **Temporal object** | In force today; point in time (as at a stated date); or as made. A corpus MUST NOT silently mix temporal objects (R10). |
| **Applicability dimensions** | The dimensions decisive for applicability in this corpus (for example period, actor, setting, action and procedural stage), each of which R5 requires to be assessed. |
| **Sources not held** | Classes of source that a competent human researcher would check for questions in scope and that the system does not hold. Feeds R7 and R17. |
| **Question scopes** | The bounded question types the system answers, against which sufficiency is assessed (§3.5). |
| **Languages** | Which language texts are held and their stated authority relation (equal status, prevailing text, translation); which language each witness is checked in; which languages questions are accepted in. |
| **Indigenous and custodial authority** | Whether the corpus engages Indigenous law, language or treaty-related authorities (in Aotearoa New Zealand: tikanga, te reo Māori and Te Tiriti o Waitangi), the treatment adopted, and its basis (below). |
| **Source terms** | Licence, access terms and AI-use terms per corpus (R15). |

**Coverage note for procedural corpora.** Procedural rules are often varied outside the standing text. In the primary evidence base, the Standing Orders of the House of Representatives 2023 define leave (SO 3), allow Standing Orders and other orders of the House to be suspended, in whole or in part, on motion (SO 4), and in places let the Business Committee determine how business is conducted (for example, SO 59(2)). Leave, Business Committee determinations, sessional and other orders of the House, and suspensions are therefore classes of source a coverage statement would ordinarily declare as held or not held. Where they are not held, a point they could change is a coverage gap (R7, R17).

**Indigenous and custodial authority.** An implementation MUST establish, and MUST disclose in its coverage statement, a legitimate basis for its treatment of tikanga, te reo Māori and Te Tiriti-related authorities (and of comparable Indigenous authorities in other jurisdictions), for example terms set by, or agreed with, the people and bodies with standing to set them, or governance of the implementation by them. The Supreme Court was unanimous that tikanga is recognised in the development of the common law where relevant, and forms part of New Zealand law through its incorporation into statutes and regulations (*Ellis v R* [2022] NZSC 114 at [19]); Winkelmann CJ cautioned that "the task for the courts is limited. It is not to pronounce on or develop the content of tikanga" (at [181]). An advisory AI system has less standing still.

KNIT adopts a conservative exclusion for **its own** implementations. It is not a universal rule, and this draft does not propose it for Māori-governed implementations or for implementations operating on terms set by custodians. Under KNIT's exclusion, an implementation treats tikanga, and the meaning of te reo Māori texts, as a declared coverage exclusion; does not generate its own statements of tikanga or its own legal readings of te reo Māori texts; may quote, without expanding on it, a held source unit that itself states the point, with a witness; and otherwise withholds the point or discloses it as a coverage gap, naming who decides.

**Failure.** Extending answers beyond the declared domain, interpretation regime or question scope without saying so is a Category C failure. An implementation that ignores custodial terms it has itself declared fails R15.

---

## 6. Requirements

Requirement identifiers are stable. R1–R16 keep their v0.2 numbers; R17 was added in v0.3. Identifiers are never reused, and no requirement was added or removed in this version. Open Order's status against each requirement is recorded in evidence/, not here (§9).

> **Provisional requirements.** R3, R4, R11 and R17, and the assignment of uncertainty classes under R7, are **provisional** in version 0.6.1. Their outcomes are stated and implementations are asked to meet them, but they are reported as "definition pending" until operational definitions exist (§7.5). Where an interim test method is given, it is labelled, known to be incomplete, and testable; meeting it is reported as an interim-rule outcome, not as conformance.

The obligations below apply to what the system itself does and to the surfaces the system generates (§4).

### R1. Generated output is a proposal, with a declared basis

*Layers: L1–L4. Category: A. Status: reportable.*

**A system MUST treat generated output (from a model or any other generator) as a proposal until the checks that apply to it have run. Every substantive institutional claim MUST have a declared evidential basis of one of the following kinds:**

| Basis | Meaning | What it needs |
|---|---|---|
| **Quotation** | The claim reproduces source text. | A witness from that source (R2). |
| **Paraphrase** | The claim restates one source in other words. | A witness (R2) and an L3 check. |
| **Multi-source synthesis** | A conclusion drawn from several sources, including a reading of a set of provisions as a whole. | A witness from each source relied on (R2), identification as synthesis, and an L3/L4 check. |
| **Practice description** | A non-normative statement of how the institution has applied its rules, drawn from a held source that records the practice (for example, a ruling). | A witness from that source; identification as practice. Never displayed as a rule. Where no held source records the practice, the point is a coverage gap (R7). |
| **Factual assumption** | The claim rests on a fact about the situation (stated by the person, or assumed for the answer). | Identification as an assumption. No witness for the fact; the institutional rule, power or consequence the claim asserts still needs its own basis. |
| **Uncertainty statement** | The claim states that a point is not settled. | Its uncertainty disclosure (R7). No witness. |

**A factual assumption MAY supplement, but MUST NOT substitute for, evidence of the institutional rule, power or consequence asserted.** "Assuming you are a member of the committee, you are entitled to move the motion" assumes the membership; the entitlement still needs a quotation, paraphrase or synthesis basis with its witness. **An uncertainty statement MUST distinguish "the system cannot establish X" (a limit of the system's sources or search) from "the institution has left X unresolved" (a property of the institution's rules), using the classes in R7.** In application mode (§3.6), any fact the answer turns on MUST be treated as a factual assumption or disclosed as facts incomplete (R7).

**A substantive institutional claim with no declared basis MUST NOT be displayed as a conclusion. Passing the checks establishes only what those checks establish, and MUST NOT be presented as conferring legal or institutional authority on the claim.**

*Rationale.* A generator can produce plausible text with no reliable connection to the source; a declared basis closes the gap through which an unattributed assertion could pass unchecked. An assumption is a legitimate way to answer an application question, but it settles only the facts, never the rule.

*Evidence of conformance.* Fixtures with uncited claims, including claims hidden in connective prose and soft modals or placed outside checked sections; practice descriptions with and without a held source; assumed facts carrying an unsupported rule; uncertainty statements that confuse a system limit with institutional silence.

### R2. Verbatim witness

*Layer: L1. Category: A. Status: reportable.*

**Witness matching. For every substantive institutional claim whose basis is quotation, paraphrase, synthesis or practice description, each source relied on MUST be supported by at least one witness machine-checked against the stored text of that unit and expression. A witness MAY consist of explicitly enumerated non-contiguous spans from the same unit, each checked. Implementations MUST publish their normalisation policy (for example, for whitespace, punctuation, quotation marks, macrons and editorial square brackets), and a policy MUST NOT treat differences in words, numbers or negation as matching. Implementations SHOULD publish a minimum witness length. A passing witness check MUST NOT be reported as establishing that the claim is supported (L3).**

**Ingestion authenticity. Separately from witness matching, each stored unit MUST be traceable to the manifestation it was ingested from, with that manifestation's identifier and the checksum of the ingested bytes. Where the institution publishes an official manifestation or an official checksum, the system MUST record whether the stored text was derived from it. A compiled or editorial text (for example, a published compilation of presiding officers' rulings) MUST be declared as its own expression, with its own provenance.**

*Rationale.* An invented or quietly paraphrased quotation is the most direct way for a system to put its own words in the source's place, and the easiest to detect mechanically. But a witness check is only as good as the stored text, and quotation integrity is not claim entailment (§3.3).

*Evidence of conformance.* Fixtures with invented, altered and truncated quotations; right words, wrong unit; wrong expression; multi-span witnesses; normalisation edge cases; an ingestion record. Evidence MUST cover every path by which substantive claims reach the person, including fallbacks. Illustrative fixtures: conformance/fixtures/.

### R3. Normative fidelity

*Layers: L3, L4. Category: B. Status: **provisional** (definition pending); interim test method below.*

**A system MUST preserve the normative force of each source (obligation, permission, prohibition, power, discretion, and weaker forms such as a duty to have regard to), and MUST NOT state a categorical claim where the source unit states a condition or exception to it. Where a material condition, exception or qualification is unresolved and could change the answer, the system MUST NOT give an unqualified conclusion: it MUST either give a conditional conclusion that states the unresolved point, or withhold the conclusion. Disclosing the unresolved point does not by itself permit a categorical conclusion. Fidelity is assessed relative to the interpretation regime declared in the coverage statement (§5).**

> **Interim test method (provisional). Known to be incomplete; not a theory of materiality.** For testing, a qualification is treated as material if it is reached by (a)–(d):
>
> - **(a) Same unit (MUST).** All conditions and exceptions within the same source unit, including its internal sub-paragraphs.
> - **(b) Explicit operators within the instrument (MUST).** Cross-references introduced by explicit operators (for example *subject to*, *except as provided in*, *despite*, *notwithstanding*, *in accordance with*, *within the meaning of*, *as defined in*), followed within the same instrument until a unit with no further operator or a cycle is reached, **capped at three hops**. If the cap is reached, the conclusion MUST be conditional.
> - **(c) Definitions (MUST).** Definition and interpretation units declared in the coverage statement are always in scope.
> - **(d) Named instruments not held (MUST).** Where a unit in scope names an instrument the system does not hold, no unqualified conclusion may be given on any point that instrument could change.
> - **(e) Other held instruments (SHOULD).** One hop into other held instruments by the operators in (b).
> - **(f) Not followed.** "See also" references, comparative notes, topical similarity and model-judged links.
> - **(g) Disclosure (MUST).** Any truncation of a chain (by the cap, a missing instrument or a cycle) is disclosed with the answer.

*Rationale.* An omitted "unless" or "subject to" can reverse what a provision means. A caveat on a categorical answer still leaves the categorical answer as what most people take away, so the conclusion itself has to change form. The interim method is deliberately mechanical, so it can be tested and failed.

*Evidence of conformance.* Definition pending. Interim-rule outcomes: fixtures with same-unit exceptions; operator chains of one to four hops, with cycles; definition units; missing instruments; "see also" decoys; modal-force changes; checks that answers are conditional or withheld; independent domain review.

### R4. Roles and allocated powers

*Layer: L3. Category: B. Status: **provisional** (role vocabulary pending).*

**Where a source assigns different roles to different actors (for example, one may request and another decide), a system MUST preserve those assignments. It MUST NOT attribute a power to an actor the source does not give it, and MUST NOT present a right to request as a power to decide.**

*Rationale.* Many rules give one party the ability to ask and another the power to grant. Collapsing the two misleads people about what they can do. This requirement concerns roles and powers allocated by the text, not standing in the public-law sense.

*Evidence of conformance.* Definition pending. Fixtures pairing request and decision provisions, concurrent powers, delegated exercise, and different offices within one institution; independent review.

### R5. Applicability

*Layer: L2. Category: A (declared dimensions and records), B (judgements). Status: reportable for declared dimensions and records; judgements as assessed.*

**Before treating a source unit as governing, a system MUST assess its applicability to the question across the dimensions declared in its coverage statement (§5). Institution and jurisdiction MUST be among them for every corpus; any dimension the coverage statement declares decisive (for example period, actor or procedural stage) MUST be assessed; other dimensions SHOULD be assessed where the corpus makes them relevant.**

**A system MUST NOT treat a source whose applicability conflicts as governing. A source whose applicability is unresolved MAY be presented as potentially relevant evidence, clearly marked as conditional. A source shown for comparison that does not govern MUST be marked as a non-governing comparator. These markings MUST accompany the source in every output channel the system provides, including its own share and export functions. For each dimension, the system MUST record the mechanism used (§3.2) and the outcome (applies, does not apply, unresolved).**

*Rationale.* A provision about a different forum, office or stage can look relevant on topic while not governing at all. People promote a yellow flag to a rule, so the marking has to travel with the source wherever the system sends it.

*Evidence of conformance.* Fixtures failing on each declared dimension; unresolved applicability; comparators; markings surviving share and export; the per-dimension record.

### R6. Separation and independence of checks

*Layer: X. Categories: A, C. Status: reportable.*

**A system MUST separate the function that proposes a claim from the function that checks it. Appeal or reconsideration of a rejection is OPTIONAL. If implemented, it MUST NOT allow the rejecting function to reverse its own decision unilaterally, and MUST NOT override a designated non-appealable veto. A system MUST describe, for each check, which of the following properties it has, and MUST NOT describe a check as independent without naming the kind of independence:**

- **(a) functional separation:** the check is a distinct step with its own inputs and outputs;
- **(b) independence of mechanism:** the check uses a different mechanism from the one that produced the claim (for example, deterministic code checking model output);
- **(c) model or provider independence:** the check uses a different model, or a different provider;
- **(d) human or institutional review:** the check involves a person or body outside the system's own pipeline.

**A separate call to the same model, or to a model of the same configuration, MUST NOT be described as independent review or expert review. User-facing text MUST NOT describe a check as "independently verified", "independently checked" or equivalent unless property (b), (c) or (d) holds for that check, and then MUST say which. These phrases describe checks, never answers or claims (§7.4).**

*Rationale.* Calling the same model three times is functional separation, not independent judgement; a deterministic check inside the same application can be genuinely independent of the model it checks.

*Evidence of conformance.* A per-check table of properties (a)–(d); tests of self-reversal and veto bypass; review of user-facing wording, including progress messages; for (d), the reviewer's role and relationship to the implementer.

### R7. Classified uncertainty

*Layers: L2, L4. Categories: B, C. Status: disclosure duties reportable; class assignment **provisional** (definition pending); interim test method below.*

**When the admitted sources do not settle a point the question raises, a system MUST say so.**

**Silence alone MUST NOT be treated as supporting a conclusion that something is permitted or prohibited, and disclosing such an inference does not make it permissible. A conclusion about permission or prohibition on a point the texts do not address MUST rest on a separately sourced residual rule or interpretive principle, held in the corpus and supported by a witness (for example, a standing order giving the presiding officer power to decide cases not otherwise provided for). A residual rule of one domain MUST NOT be applied in another.**

**A system SHOULD classify the uncertainty as one of the following. Where it classifies, it MUST NOT present one class as another.**

| Class | Meaning | Disclosure |
|---|---|---|
| **Corpus silence** | The applicable texts, as far as the corpus covers them, do not resolve the question. | The rules held do not settle this; say who decides. |
| **Coverage gap** | The implementation does not hold all potentially applicable texts or records of practice. | This system's sources may be incomplete; name what is missing if known. |
| **Retrieval uncertainty** | Governing authority may be in the corpus but was not identified. | The system did not find authority on this point; that is not evidence that none exists. |
| **Interpretive uncertainty** | The authority was found but admits competing reasonable readings. | Set out the readings and who decides. |
| **Authority conflict** | Two or more applicable authorities point different ways and their precedence is unresolved. | Name the authorities and who decides precedence. |
| **Higher-law tension** | A held unit may need to be read subject to, or may be inconsistent with, a higher instrument. | Name the instrument, or the coverage limit if it is not held. |
| **Facts incomplete** | The answer turns on facts about the person's situation that are not known. Not a property of the corpus. | Say which facts matter and how the answer changes. |

Coverage gaps and retrieval uncertainty are cases of "the system cannot establish X"; corpus silence, interpretive uncertainty and authority conflict are cases of "the institution has left X unresolved" (R1). Unpublished practice is a coverage gap; officially ambiguous texts in more than one language are interpretive uncertainty, or an authority conflict where the texts have equal authority (R11).

> **Interim test method (provisional).** Corpus silence can rarely be shown. Until operational criteria exist (§7.5), an apparent silence MUST be disclosed as retrieval uncertainty, or as a coverage gap where the coverage statement declares relevant sources not held, and MUST NOT be disclosed as corpus silence.

*Illustration (primary evidence base; not a prescription).* Under Standing Order 2 of the Standing Orders of the House of Representatives 2023, the presiding member rules on interpretation and application of the Standing Orders and determines cases for which they make no specific provision. Previous rulings and established House practice guide the Speaker (paraphrase; see References). That is a separately sourced residual rule about who decides. It does not settle what the Speaker would decide. A system holding the Standing Orders and rulings but not *Parliamentary Practice in New Zealand* or unpublished practice would disclose an apparent gap along these lines:

> *The Standing Orders held here do not settle this. Under SO 2 the Speaker (or member presiding) decides, guided by Speakers' Rulings and established practice. This system does not hold Parliamentary Practice in New Zealand or unpublished practice; ask the Clerk or raise a point of order.*

*Rationale.* Each class points to a different next step. Silence is not a rule; at most it is the occasion for one.

*Evidence of conformance.* Disclosure: fixtures for each class, including permission or prohibition inferred from silence with and without a sourced residual rule; who-decides wording. Class assignment: definition pending, with interim-rule outcomes.

### R8. Inspectable evidence and correction

*Layer: X. Categories: A, C. Status: reportable.*

**Evidence record. A system MUST make available, with each answer, an evidence record sufficient for the person relying on the answer to check it. The record MUST include the admitted sources and their witnesses, the assurance state of each substantive institutional claim (R12), and meaningful exclusions with the reason. Each citation MUST give the institution's printed citation form and the best available stable link to the authoritative publication of the cited unit, at the finest granularity the publisher supports. Conformance MUST NOT depend on disclosure of a model's internal reasoning, and this requirement does not require publishing private user questions, hidden prompts, secrets or sensitive logs.**

**Challenge and correction. A system MUST provide a documented, accessible pathway through which a person can report a suspected interpretation error or missing evidence. The pathway MUST identify who is responsible for triage and the expected response band (a statement such as "best effort, single volunteer maintainer, usually within ten working days" is acceptable if true). Substantiated defects MUST be able to lead to correction, and material corrections MUST be recorded in a public, versioned correction record that does not disclose private questions or identify reporters without consent. A correction is material if it changes, withdraws or makes conditional a substantive institutional claim the system would otherwise give, or changes the coverage statement.**

*Notes.* The pathway corrects the advisory software; it is not an appeal against any institutional decision. Because R15 discourages retaining identifiable questions, corrected answers generally cannot be re-issued to earlier recipients; the public correction record is the substitute, and the system SHOULD say so.

*Evidence of conformance.* An evidence-record schema and sample; link and citation checks; documentation of the pathway; the correction record; a synthetic report taken through to a traceable correction. A link to a general issue tracker is not, on its own, sufficient.

### R9. Citation at the institution's unit of authority

*Layer: L1. Category: A. Status: reportable.*

**A system MUST cite at the issuing institution's own unit of authority, using the institution's own pinpoint form at the granularity the claim relies on, and MUST keep citable source units distinct from retrieval chunks. Headings, notes and examples MUST be identified as such where the institution treats them as non-operative. Where the source publishes stable element identifiers (for example, Akoma Ntoso eIds) or legislation identifiers (for example, ELI), the system SHOULD use them.**

*Rationale.* Chunks are an engineering convenience. Authority attaches to the institution's units and their relations (R11), not to the retrieval index.

*Evidence of conformance.* Data model showing the separation; fixtures in which a chunk boundary splits a source unit, and in which the claim relies on one sub-paragraph of a multi-paragraph unit; checks of pinpoint form.

### R10. Provenance, expression and temporal applicability

*Layers: L1, L2. Category: A. Status: reportable.*

**Every source unit MUST carry provenance: the manifestation it was ingested from, the expression it represents (as made; as amended to a stated date; or an editorial compilation), whether that expression is official or editorial, a content checksum, and the ingestion build. Where the source makes them available, a system MUST record separately the dates on which a unit's text was made, took effect, was amended and ceased to have effect, and the compilation date of any consolidation. These dates and the ingestion date MUST NOT be treated as interchangeable, and a compilation date MUST NOT be presented as the date from which the compiled text has effect.**

**Answers MUST identify the expression they rest on and the temporal object served (in force today, point in time, or as made). Where the question concerns a particular date, the system MUST assess applicability for that date, or say that it cannot. A system MUST NOT silently mix temporal objects in one answer.**

*Rationale.* Questions are often "what applied on the day?", not "what does today's reprint say?". Fidelity to an editorial consolidation is not fidelity to the rules: the consolidation is itself an expression, and its status depends on the institution's own rules. Software provenance (which file, which build) is necessary but is not the institution's provenance.

*Evidence of conformance.* Provenance fields; fixtures with superseded, amended and not-yet-effective provisions, compilation dates and editorial expressions; expression and temporal-object statements in answers.

### R11. Authority roles and relations

*Layers: L2, L4. Category: B. Status: **provisional** (definition pending); interim test method below.*

**A system SHOULD select sources by the role they play for the question (for example rule, exception, discretion, decision-maker, mechanism, interpretation, precedent), not by topical similarity alone, and SHOULD display each source's role (§5), not only its citation. Where a governing rule has a stated exception or limit, the system SHOULD retrieve both.**

> **Interim test method (provisional).** Where the source or its structured metadata states them, a system is tested on whether it represents at least the relations *amends*, *repeals*, *commences*, *subject to / qualifies*, *interprets* (for example, a ruling interpreting a rule) and *has equal authority with* (for example, equally authentic language texts). An implementation that claims to meet this method MUST represent all six. Other stated relations SHOULD be represented. Precedence between competing authorities is definition-pending (§7.5).

*Rationale.* A provision does not carry the same authority in every context. Its relations to other provisions can determine whether it applies, which prevails, and what it means. Formal relation models already exist and are compatible with this draft (§1.4).

*Evidence of conformance.* Definition pending. Interim-rule outcomes: description of the role and relation vocabulary; fixtures in which topical similarity and role point to different sources; fixtures with structured amendment, commencement and equal-authority metadata.

### R12. Assurance states and failing closed

*Layer: X. Categories: A, C. Status: reportable.*

**Claim states. A system MUST attach one of the following states to each substantive institutional claim:**

| State | Meaning | What may be displayed |
|---|---|---|
| **Supported** | The claim passed every check applicable to it, at the layers stated. | The claim, with its layers and evidence record. |
| **Conditional** | The claim passed its applicable checks but depends on a stated unresolved point. | The claim, phrased conditionally, with the unresolved point. |
| **Provisional** | Checks have not yet completed. | Not as a conclusion. An in-progress indication only. |
| **Unsupported** | The claim failed a check. | Not as a conclusion. The system may say that a point was withheld and why. |
| **Unchecked** | A check necessary for the claim failed to run or did not complete. | Not as a conclusion. The system may say that checking did not complete and why. |

**Transitions.** A provisional claim takes another state when its checks complete. An unsupported claim becomes supported or conditional only through a new check that meets R6 (never by the rejecting function or past a veto); an unchecked claim, only when the necessary checks complete. A supported claim may be corrected to conditional or unsupported on a later check, new evidence or a substantiated correction (R8). No state changes by relabelling alone.

**Answer states. A system MUST summarise each answer as one of the following. Implementations MAY use the plain-language labels shown, or equivalents that are no stronger:**

| Answer state | Plain-language label | Meaning |
|---|---|---|
| **supported** | Answered from the texts held | Every displayed substantive claim is supported, and no material point was withheld. |
| **partial** | Conditional answer | At least one substantive claim is conditional or was withheld, and each withheld point is stated. |
| **not answered** | Refer to the decision-maker | No substantive conclusion is displayed; the system names who decides and where to look. |

**The answer state MUST be consistent with its claim states and MUST NOT be stronger than they support. Wherever "supported" or its label is shown, the system MUST make available, in the same view, what it means: which layers were checked, by which mechanisms, and that it is not an institutional ruling or advice.**

**Failing closed. A substantive conclusion whose necessary checks failed or did not complete MUST NOT be displayed as a conclusion, and labelling it "unchecked" or "unverified" does not make display permissible. A system MAY still display identified source excerpts, links to the authoritative publication, an explanation of the failure, and bounded partial conclusions that passed their applicable checks, and SHOULD do so when it withholds a conclusion (§3.6). A fallback path MUST NOT bypass a check that the ordinary path applies.**

**Streaming. Where output is streamed, a system MAY stream progress information, retrieval information and identified source excerpts, and MUST release a substantive conclusion only once its checks have completed. Displaying a conclusion that its checks then reject is a failure of this requirement, even if the conclusion is later retracted.**

**Restricted terms.** User-facing text MUST NOT use the terms in §7.4 except as §7.4 allows.

*Rationale.* A useful answer is often partly supported. But a label is not a safeguard, and a conclusion shown and then withdrawn has already been read.

*Evidence of conformance.* Fault injection (provider failure, timeouts, all candidates rejected, partial success); fallback-bypass attempts; streaming tests that no conclusion appears before its checks complete; state consistency; wording review against §7.4. Illustrative fixtures: conformance/fixtures/.

### R13. Portable safeguards

*Layer: X. Category: A. Status: reportable.*

**The safeguards required by this specification MUST be implemented so that they continue to operate when the model or provider is changed. A system SHOULD be operable with self-hosted models. A system MUST distinguish, in its documentation and reports, mechanisms whose behaviour does not depend on the model (portable mechanisms) from checks whose performance depends on the model or configuration. Results MUST be reported per model and configuration, and MUST NOT be assumed to transfer between them.**

*Rationale.* Implementers, including public bodies with procurement and data-residency constraints, should be able to choose or host their own models without losing the safeguards. Portability of a safeguard is not equality of performance.

*Evidence of conformance.* A list of safeguards classified by mechanism (§3.2); results for each model configuration reported, preferably including one openly available configuration.

### R14. Status disclosure

*Layer: X. Category: C. Status: reportable.*

**A system MUST disclose, on every surface the system generates where answers appear (including its own share links, exports and print views), its status as a set of separate facts: whether it is independent of the institution whose texts it uses; whether the institution has commissioned, procured or endorsed it, and the scope of any such arrangement; and whether the institution permits or restricts its use in official proceedings. It MUST state that its answers are not rulings or official advice and, unless it is a service permitted to give legal advice (§7.4), that they are not legal advice. It MUST state in plain language who actually decides questions of the kind asked (from the coverage statement, §5), and MUST direct people to the authoritative publication.**

**An independent system MUST NOT present itself, in any surface it generates or any material its operator publishes, as an official source, a ruling, or advice from the institution. A commissioned or authorised system MUST state the scope and limits of that commissioning, and MUST NOT imply that its outputs carry the institution's interpretive authority unless the institution has conferred it. Commissioned software is not an authorised interpretation; authorised software does not mean authorised answers; and neither means the output may be relied on in proceedings.**

*Rationale.* Independence and commissioning are both legitimate, with different obligations. Naming who decides gives the person somewhere to go (§2.4).

*Evidence of conformance.* The status statements on every surface the system generates; where relevant, a jurisdiction-specific review of the wording by someone qualified to give it.

### R15. Source licensing, access and data governance

*Layer: X. Category: C. Status: reportable.*

**A system MUST record and publish, per corpus, how it meets: (a) the licence of each source, including the attribution it requires; (b) the access terms under which it was obtained, including robots directives, API terms and any restrictions on automated access or AI use; and (c) the data-governance obligations that apply to the texts and to people's use of the system, including custodial or cultural terms set by the texts' custodians. Conformance evidence MUST NOT depend on collection that the source's terms prohibit. Where Indigenous data-sovereignty principles apply (for example, Te Mana Raraunga's *Principles of Māori Data Sovereignty* (2018), in Aotearoa New Zealand), implementations SHOULD apply them unless custodians have set other terms.**

**A system MUST publish a truthful statement of what it records about the people who use it, including whether question text is retained, for how long, and who can access it, and MUST show the retention position where questions are entered, not only in documentation. The evidence record (R8) and conformance evidence (R16) MUST NOT be used as a reason to retain private questions beyond what that statement discloses. Where the intended users include members of a legislature or their staff, the statement MUST address the political sensitivity of their questions and any parliamentary privilege that may attach to them, and identifiable questions SHOULD NOT be retained.**

*Rationale.* Licensing, access and data governance are different obligations. Auditability is a reason to keep records of sources and checks, not of people's questions.

*Evidence of conformance.* Per-corpus terms records; the data statement and its in-interface form; evidence that both match the deployed system.

### R16. Conformance by published, bounded evidence

*Layer: X. Category: C. Status: reportable.*

**A claim of conformance MUST be supported by a published conformance report (§7) that identifies: the pinned implementation version; the model(s), provider(s) and configuration for each role; the corpus, expression and checksum; the coverage statement; the fixture and suite versions; the date; any thresholds applied and who set them; the reviewer method; and material limitations. Each requirement, or each defined property assessed, MUST be reported with one of: conformant (under the stated configuration), not conformant, not assessed, definition pending, or not applicable (with reasons). A provisional requirement, or part of one, MUST NOT be reported as conformant; interim-rule outcomes MAY be reported alongside "definition pending". Implementation maturity MUST be reported separately from results. An implementation MUST NOT claim full or overall conformance while any applicable MUST-level requirement is not conformant, not assessed or definition pending. Results MUST NOT be expressed as a single aggregate score.**

*Rationale.* Claims about trustworthiness are useful only when others can inspect, reproduce and bound them. The same discipline applies to KNIT's own claims.

*Evidence of conformance.* The report itself.

### R17. Evidential sufficiency

*Layer: L4. Category: B. Status: **provisional** (definition pending).*

**A system MUST NOT present fidelity to the evidence it selected as fidelity to the institution's complete applicable rules, and MUST NOT claim or imply that its search was exhaustive. It MUST publish a coverage statement (§5) and MUST state, with each answer, the question scope it answered within. It MUST disclose the basis on which it treats its admitted sources as sufficient for that scope (for example: coverage statement, retrieval method, dependency checks performed) and the known limits of that basis, using the classes in R7 where they apply (in particular, coverage gaps including the classes of source not held, retrieval uncertainty and interpretive uncertainty) and identifying known omissions. Where the corpus holds rulings or case law without a record of later treatment, it MUST disclose subsequent treatment as a coverage limit. Where support remains insufficient for a conclusion, R3 and R12 apply: the conclusion is conditional or withheld, not categorical with a caveat.**

*Rationale.* §3.5. The requirement is limited to what can be done today: honest disclosure, a bounded question scope, and no categorical conclusions from insufficient support.

*Evidence of conformance.* Definition pending. Useful evidence: per-answer scope statements; retrieval evaluation against reviewer-labelled *governing* units; fixtures with a distant governing exception, a missing instrument or unknown coverage. This draft sets no universal thresholds; any threshold used is published with the report (R16).

---

## 7. Conformance

### 7.1 Reporting framework

Conformance is reported, not certified. A report follows R16 and conformance/README.md, and its results are bounded by its stated configuration, corpus, expression, mechanisms and reviewer method; they do not transfer elsewhere (R13).

| ID | Short name | Layer(s) | Cat. | Status in 0.6.1 |
|---|---|---|---|---|
| R1 | Generated output is a proposal, with a declared basis | L1–L4 | A | Reportable |
| R2 | Verbatim witness | L1 | A | Reportable |
| R3 | Normative fidelity | L3, L4 | B | **Provisional** (interim test method) |
| R4 | Roles and allocated powers | L3 | B | **Provisional** |
| R5 | Applicability | L2 | A, B | Reportable |
| R6 | Separation and independence of checks | X | A, C | Reportable |
| R7 | Classified uncertainty | L2, L4 | B, C | Disclosure reportable; class assignment **provisional** (interim test method) |
| R8 | Inspectable evidence and correction | X | A, C | Reportable |
| R9 | Citation at the institution's unit of authority | L1 | A | Reportable |
| R10 | Provenance, expression and temporal applicability | L1, L2 | A | Reportable |
| R11 | Authority roles and relations | L2, L4 | B | **Provisional** (interim test method) |
| R12 | Assurance states and failing closed | X | A, C | Reportable |
| R13 | Portable safeguards | X | A | Reportable |
| R14 | Status disclosure | X | C | Reportable |
| R15 | Source licensing, access and data governance | X | C | Reportable |
| R16 | Conformance by published, bounded evidence | X | C | Reportable |
| R17 | Evidential sufficiency | L4 | B | **Provisional** |

"Provisional" is a statement about this draft, not a judgement on any implementation.

### 7.2 Evidence categories and why there is no aggregate score

| Category | Covers | Primary evidence |
|---|---|---|
| **A. Structural** | Declared bases, witnesses, ingestion records, source identifiers, provenance, expressions, assurance states, failure behaviour, non-bypassable checks. | Mainly deterministic tests. |
| **B. Semantic fidelity** | Normative force, exceptions, roles and powers, applicability judgements, relations, sufficiency. | Benchmark results with independent domain assessment. |
| **C. Institutional accountability** | Inspectability, correction, uncertainty disclosure, status disclosure, independence claims, source terms, data statements, coverage statements. | Operational and governance evidence. |

Results are reported per category and per requirement or property. There is no aggregate score, and reports MUST NOT compute one: an implementation can be structurally strong and semantically weak, and one number would hide exactly that.

### 7.3 Why no overall claim is currently available

An overall claim would need every applicable MUST-level requirement to be conformant (R16). While R3, R4, R11, R17 and R7 class assignment are provisional, that is impossible. **Structural conformance** (a bounded claim covering Category A properties only) is **proposed, not currently claimable**: its scope and the evidence it would need are not yet settled. Individual defined properties MAY still be assessed and reported, with no overall claim. The following table is a **hypothetical illustration** of the reporting format only. It is not a result for Open Order or any other implementation:

| Property (hypothetical) | Illustrative result |
|---|---|
| Witness matching (R2) | Passed, under the stated configuration and fixtures |
| Claim coverage (R1) | Not assessed |
| Evidential sufficiency (R17) | Definition pending |
| Overall conformance | No claim |

### 7.4 Restricted user-facing terms

Implementers MUST NOT use the following, in user-facing text, documentation, reports or marketing that they publish, to describe the system, its answers or its checks, except as allowed:

| Term | Allowed only if |
|---|---|
| verified, validated (of an answer or claim) | Never. Use the assurance state and its expansion (R12). |
| independently verified, independently checked (of a check) | Only where R6 property (b), (c) or (d) holds for that check, naming which. Never of an answer or claim. |
| hallucination-free | Never. |
| authoritative, official | Never of the system or its answers. "The authoritative publication" may be used of the institution's own text. |
| exhaustive, complete (of search or coverage) | Never (R17). |
| certified, "authority-aware certified", "certified authority-aware" | Never, in this version. There is no certification. |
| legal advice | Only where the provider is permitted to give legal advice under the requirements of the jurisdiction concerned, and then only for that service. Commissioning or professional supervision alone does not establish that permission. |
| conformant, compliant (with this draft) | Only of a named requirement or defined property, with a published report and the version. Never as an overall claim in this version. |

### 7.5 Definition-pending criteria

A provisional requirement becomes reportable when this draft supplies an operational definition that two independent assessors could apply to the same evidence and expect to reach the same result. The definitions needed are:

| Item | What is pending |
|---|---|
| R3 material qualifications | What should replace the interim test method: deeper chains, implied qualifications, purposive reading, higher-law reading-down. |
| R4 roles | A role vocabulary for fixtures and assessment. |
| R7 class assignment | Operational criteria that distinguish corpus silence from retrieval uncertainty, and authority conflict from interpretive uncertainty. |
| R11 relations and precedence | A minimal relation model, including precedence between competing authorities, and how it maps to existing rule and document standards. |
| R17 sufficiency | How an implementation can show, within a declared question scope, that it has not missed a material source. |
| Claim segmentation | How answers are divided into substantive institutional claims for per-claim states and scoring, and how agreement between segmenters is reported. |

Until then, results against these items are reported as "definition pending", optionally with interim-rule outcomes.

### 7.6 What passing means

Passing the suite means passing the suite: under the stated configuration, on the stated corpus and expression, against any stated thresholds. It does not establish that a system cannot produce an unsupported conclusion, that results transfer to another model or corpus, or that the system has any standing with the institution whose texts it uses. Conformance does not establish legal compliance or confer institutional authority or permission to provide regulated services, and this draft does not purport to create a duty of care, establish a legal safe harbour or determine an implementer's liability.

---

## 8. Research agenda

Whether the requirements generalise is an empirical question, and the definition-pending items in §7.5 are the research agenda, not gaps to hide. The aim is defensible operational criteria within bounded domains, not a general solution to evidential sufficiency or semantic fidelity.

- **Methodological:** operational definitions for the items in §7.5; executable conformance tests from the illustrative fixtures; evaluation methods for Category B, including reviewer-labelled sets of governing units; and reproducible reporting.
- **Engineering:** reusable components that demonstrably satisfy the reportable requirements; declarative authority registries; adapters; guidance.
- **Empirical:** an assessment of Open Order against this draft; a statutory demonstrator over a bilingual Welsh Act, limited to intra-Act questions and reported only after independent domain and Welsh-language review; and evaluation by an external developer. **Same-author portability is not external validity**: a demonstrator built by KNIT from Open Order components tests portability, not independence.
- **Applying the taxonomy to existing systems:** applying the layers, fixtures and misgrounding categories to a plain-RAG baseline that KNIT would build itself, to open tools, and to commercial tools only where their terms permit, with manual entry and no scraping. Vendors would be contacted before anything about their tool is published, results would be framed as applying a taxonomy, not as conformance findings, and no named comparison would be published without legal advice first.

This draft is the engineering counterpart to three KNIT working papers in preparation (on accountability for automated decisions, publicly verifiable fidelity to enacted law, and delegated authority and procedural standing). They are unpublished and follow their own timetable.

---

## 9. Implementation evidence

Open Order is a single working proof of concept, published under Apache-2.0, that answers questions about the Standing Orders of the New Zealand House of Representatives and Speakers' Rulings. The evidence in this draft is **pinned to a historical commit**, `a3f007e649ce6b203bbc2201aaba7ea15b349cac`, over the 2023 Standing Orders and Speakers' Rulings, and is not updated as Open Order evolves. It is recorded in evidence/open-order.md and evidence/implementation-matrix.md.

At the pin, by code inspection and synthetic tests, Open Order's implementation maturity is: 0 requirements implemented, 15 partial, 2 not yet implemented (R16, R17). These are implementation-maturity observations, not conformance results. Conformance status at the pin: 12 requirements not assessed; 4 definition pending (R3, R4, R11, R17); 1 split (R7: disclosure not assessed, class assignment definition pending); 0 conformant; 0 not conformant. No overall claim is made, and no conformance report has been published. The pinned evidence also records a disclosed gap against R15 (retention of search-query text at the pin). None of this describes current production behaviour; later changes to Open Order, including migration to the 2026 Standing Orders, are not reflected in the pinned evidence. Testing and use to date are the author's own; no other implementation exists.

---

## 10. Stewardship

KNIT stewards this draft for now (GOVERNANCE.md). Changes are proposed as numbered KNIT change proposals (CP-NNNN), each stating motivation, proposed text, compatibility impact and evidence (ideally a failing conformance case). Substantive changes have a public comment period of at least 30 days, and decisions and reasons are recorded in CHANGELOG.md. Versioning is semantic: major for changes that make a previously conforming implementation non-conforming; minor for new recommendations, options or clarifications; patch for editorial changes. Before version 1.0.0, minor versions may also contain normative changes. Transfer of stewardship is deferred until there is independent participation to transfer it to. The conformance suite is versioned separately from this draft.

---

## References

*Institutional texts and cases*

- Standing Orders of the House of Representatives 2023 (New Zealand), SO 2, SO 3, SO 4 and SO 59(2). Published with the authority of the House of Representatives. https://www3.parliament.nz/media/10573/standing-orders-2023.pdf (accessed 26 November 2026).
- *Parliamentary Practice in New Zealand* (2023; fifth edition). Editor David Wilson, Assistant Editor David Bagnall. Wellington: Clerk of the House of Representatives. ISBN 978-0-473-67872-2. Cited, not held or reproduced.
- *Ellis v R* [2022] NZSC 114, at [19] and [181].

*Theory*

- Hart, H. L. A. (2012). *The Concept of Law*. 3rd ed., ed. P. A. Bulloch and J. Raz, introduction by L. Green. Oxford: Oxford University Press.
- Hohfeld, W. N. (1913). Some Fundamental Legal Conceptions as Applied in Judicial Reasoning. *Yale Law Journal* 23: 16–59.
- Raz, J. (1986). *The Morality of Freedom*. Oxford: Clarendon Press. Raz, J. (2009). *The Authority of Law: Essays on Law and Morality*. 2nd ed. Oxford: Oxford University Press.

*Standards*

- Bradner, S. (1997). RFC 2119; Leiba, B. (2017). RFC 8174 (together, BCP 14).
- Council of the European Union (2012). Council conclusions inviting the introduction of the European Legislation Identifier (ELI). OJ C 325, 26.10.2012, pp. 3–11.
- IFLA Study Group (1998). *Functional Requirements for Bibliographic Records: Final Report*.
- OASIS (2018). *Akoma Ntoso Version 1.0*. OASIS Standard.
- OASIS (2021). *LegalRuleML Core Specification Version 1.0*. OASIS Standard.

*AI evaluation, practice and governance*

- Butler, A.-R. and Butler, U. (2026). *Legal RAG Bench: an end-to-end benchmark for legal RAG*. arXiv:2603.01710.
- Linna, E. and Linna, T. (2026). Challenges for generative AI in legal reasoning. *Discover Artificial Intelligence* 6, article 170. doi:10.1007/s44163-026-00902-3.
- Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D. and Ho, D. E. (2025). Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. *Journal of Empirical Legal Studies* 22(2): 216–242. doi:10.1111/jels.12413. Preprint: arXiv:2405.20362 (2024), whose §6.3 sets out the typology of contributing causes.
- Parasuraman, R. and Manzey, D. H. (2010). Complacency and bias in human use of automation: an attentional integration. *Human Factors* 52(3): 381–410. doi:10.1177/0018720810376055.
- Pipitone, N. and Houir Alami, G. (2024). *LegalBench-RAG: A Benchmark for Retrieval-Augmented Generation in the Legal Domain*. arXiv:2408.10343.
- POPVOX Foundation (13 May 2025). *Beta Takeaways: Key Lessons on StaffLinkBot.org*. https://www.popvox.org/blog/stafflink-beta-takeaways.
- Te Mana Raraunga (2018). *Principles of Māori Data Sovereignty*. Brief #1, October 2018. https://www.temanararaunga.maori.nz/principles-of-maori-data-sovereignty (accessed 26 November 2026).
- KNIT-NZ/open-order, commit `a3f007e649ce6b203bbc2201aaba7ea15b349cac`. https://github.com/KNIT-NZ/open-order.

---

## Acknowledgement of AI assistance

This specification was developed with the assistance of AI tools. They were used to analyse the Open Order codebase, check references and citations, organise review comments, carry out structured reviews of drafts, and draft and revise text. The concepts, requirements and editorial decisions are the author's, and the author has reviewed the text and is responsible for it. Implementation claims were checked against the Open Order source code at the commit cited.

## Authorship note on tikanga, te reo Māori and Te Tiriti

The author is not Māori and claims no competence in tikanga. The treatment of tikanga, te reo Māori and Te Tiriti in this draft (§5, R15) is a requirement to establish and disclose a legitimate basis, together with a conservative exclusion that KNIT adopts for its own implementations. It is not a position on their place in law, and it will not be extended by AI-generated text. Independent review of this treatment by people with standing to give it has not been obtained. The absence of consultation, or of comment from Māori individuals or organisations, is not consent, and is not to be read as endorsement of anything in this draft.

---

## Licence and notices

This specification text is licensed under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/. Suggested attribution: "KNIT WD-0000 · Authority-Aware AI (Working Draft 0.6.1) by Brendan McBryde, KNIT, licensed under CC BY 4.0". Original code, schemas and test fixtures in the accompanying repository are licensed under the Apache License 2.0. Third-party texts keep their own licences and terms; neither licence applies to them, and neither implies endorsement by any institution whose texts are cited. Full notices are in the NOTICE file.

**Parliamentary material.** §6 (R7) paraphrases Standing Order 2 of the Standing Orders of the House of Representatives 2023, published with the authority of the House of Representatives; see References. No verbatim Standing Orders or Speakers’ Rulings text is reproduced in the specification. The speaking-time example in §3.3 and all text in the illustrative fixtures are fictional. No licence or endorsement of this draft by Parliament is implied.

*Parliamentary Practice in New Zealand* is cited by title only; no text from it is reproduced. **Judgment.** A brief quotation from *Ellis v R* [2022] NZSC 114 is reproduced with attribution; judgments of New Zealand courts are not subject to copyright (Copyright Act 1994 (NZ), s 27(1)(g)). Brief quotations from other published works listed in the references are used for criticism and review, with attribution.
