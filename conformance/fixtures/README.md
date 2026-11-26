# Illustrative Category A fixture specifications

> **Illustrative, not a suite.** These files show, on paper, what Category A tests for R2, R9, R10 and R12 would check, so that those requirements can be argued about concretely. They are not executable, they are not a conformance suite, and passing them proves nothing. No code is included. They create no obligations of their own: where a fixture states an expectation, it applies the text of SPECIFICATION.md.

All text is **synthetic**. The fixtures use an invented instrument, the *Synthetic Assembly Rules 2030* ("SAR", with an official expression and a 2032 editorial compilation), and an invented *Synthetic Tenancy Act 2031* ("STA"). Neither exists, and nothing here is quoted from any real Standing Order, statute or ruling. This keeps the fixtures free of licensing questions (R15) and stops anyone mistaking them for statements about real law. Checksums in corpus.yaml are computed over the synthetic text by the method stated in that file.

| File | Requirement | Classes covered |
|---|---|---|
| [corpus.yaml](corpus.yaml) | — | The synthetic corpus the fixtures refer to |
| [r02-verbatim-witness.yaml](r02-verbatim-witness.yaml) | R2 | Invented quotation; altered quotation; truncated quotation that drops a qualifier; right words, wrong unit; multi-span witness; normalisation; chunk boundary; ingested text differing from the official manifestation |
| [r09-citation-unit.yaml](r09-citation-unit.yaml) | R9 | Sub-paragraph pinpoint; whole-unit citation for a sub-paragraph claim; heading relied on as authority; chunk identifier shown as a citation |
| [r10-provenance-temporal.yaml](r10-provenance-temporal.yaml) | R10 | Wrong expression; provision not yet in force; compilation date mistaken for the date of effect; silent mixing of expressions; temporal object |
| [r12-states-failing-closed.yaml](r12-states-failing-closed.yaml) | R12 | Fallback that bypasses checks; conclusion streamed and then rejected; provider failure; claim/answer state consistency; restricted user-facing terms |

Each fixture states an **input** (a question and, where relevant, a candidate answer or system event) and the **failure** it is designed to catch. Its expected result is given at two levels, reported separately:

- **mechanism**: the result of the check the fixture targets (for example, R2 witness matching: Pass);
- **claim**: the result for the claim as displayed, which can depend on other requirements (for example, R3/R17 treatment of an omitted qualifier: Conclusion withheld or conditional).

A passing mechanism does not imply a supported claim (SPECIFICATION.md §3.3). Where the claim-level result depends on a provisional requirement (R3, R4, R11, R17, R7 class assignment), it is reported as an interim-rule outcome alongside "definition pending", not as conformance. "Expected" describes outcomes, not architecture: an implementation may meet them by any mechanism, and must say which (SPECIFICATION.md §3.2).

Licence: Apache-2.0 (see LICENSE-CODE), as original fixtures.
