# Contributing

This specification is a public working draft. Comment and criticism are the most useful contributions at this stage, especially from people who have built, evaluated or relied on AI systems over institutional rules, and from people who work inside the institutions whose texts such systems use.

The initial comment window runs from 26 November to 26 December 2026 (New Zealand dates). Please do not include confidential queries, personal information or other sensitive material in public issues or discussions.

## How to comment

- **Open an issue** for a specific problem, gap or proposed wording. Name the section or requirement (for example "R7" or "§3.3").
- **Use Discussions** for broader questions about scope, foundations or direction.
- **Open a pull request** for small editorial fixes (typos, broken links, unclear sentences).

Each version is open for comment for **30 days from its publication**. Comments after that are still welcome and roll into the next version's window.

At the close of each window, the maintainers publish a summary of the comments received and what was decided about each, with reasons. Comments are recorded as received; a comment is not counted as agreement, and opening a window is not, by itself, evidence of collaboration.

## Feedback most wanted on Working Draft 0.6.1

1. The coverage statement (§5): whether its fields are the right ones, and whether a short form can be shown with every answer.
2. The domain table (§1.2): whether the requirements hold for other bounded institutional rule systems, and counter-examples from legislation, case law or mixed legal research. Guidance an institution issues about its own rules is treated as a source with the authority role *guidance*, not as a separate domain; tell us if that is wrong for your corpus.
3. The interim test methods for R3 (material qualifications), R7 (apparent silence) and R11 (relations), and the definition-pending criteria (§7.5).
4. Conformance reporting (§7): per-property reporting with no overall claim, and the restricted user-facing terms (§7.4).
5. The treatment of tikanga, te reo Māori and Te Tiriti (§5) and the authorship note. Comment from Māori legal and data practitioners is sought and should be paid for.
6. The illustrative fixture specifications in conformance/fixtures/.

## Proposing a change: change proposals (CP)

Substantive changes (anything that adds, removes or changes a requirement, or changes the foundations) go through a numbered KNIT change proposal (CP).

1. **Open an issue** describing the problem, so it can be discussed before anyone writes text.
2. **Write the proposal** as `drafts/CP-NNNN-short-title.md`, numbered sequentially from CP-0001. It states:
   - the motivation;
   - the proposed normative text;
   - the compatibility impact (does a previously conforming implementation stop conforming?);
   - the evidence, ideally a conformance case that fails under current text.
3. **Open a pull request.** The comment period of at least 30 days starts when the pull request is announced in the issue.
4. **Decision.** The maintainers accept, reject or defer the proposal and record the reasons in the pull request and in CHANGELOG.md. Accepted text is merged into SPECIFICATION.md.

Versioning follows the rules in SPECIFICATION.md §10. Requirement identifiers are never reused.

## Conformance reports

If you have evaluated an implementation against the draft, open an issue first. Reports follow [conformance/README.md](conformance/README.md); there is no certification and no fee.

## Conduct

Participation is covered by the [Code of Conduct](CODE_OF_CONDUCT.md). Report concerns to admin@knit.nz.

## Licensing of contributions

By contributing, you agree that text contributions are licensed under CC BY 4.0 and code or fixtures under Apache-2.0, as set out in [LICENSE](LICENSE) and [LICENSE-CODE](LICENSE-CODE). Do not contribute third-party source texts unless their licence permits it, and say what that licence is.
