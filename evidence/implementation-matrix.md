# Open Order implementation matrix (KNIT WD-0000 · Authority-Aware AI, Working Draft 0.6.1)

Pinned commit: `a3f007e649ce6b203bbc2201aaba7ea15b349cac` (application code identical to its parent, the runtime assurance commit `4ce15ce78d0c47d5b43cf466a8237f89d30a4a9b`). Reviewed 26 Nov 2026 (NZDT); re-checked for v0.5.0 wording the same day; compared with 0.6.0 wording without new inspection (open-order.md, "Note for Working Draft 0.6.0"). Detail: [open-order.md](open-order.md).

**Read this table as implementation maturity, not conformance.** Implementation maturity is a reviewer's observation of how far Open Order's code at the pin attempts a requirement. Conformance result is the per-requirement result defined in R16. No conformance assessment has been carried out, so every conformance result is *not assessed* or, where the requirement is provisional in 0.6.0, *definition pending*.

Method labels: CI code inspection; ST synthetic test; RC runtime configuration; PO production observation. No RC or PO evidence was available.

| ID | Short name | Mechanism(s) at the pin | Implementation maturity | Method | Conformance result | Status in 0.6.1 |
|---|---|---|---|---|---|---|
| R1 | Generated output is a proposal, with a declared basis | Deterministic; model-judged, code-enforced | Partial | CI, ST | Not assessed | Reportable |
| R2 | Verbatim witness | Deterministic | Partial | CI, ST | Not assessed | Reportable |
| R3 | Normative fidelity | Deterministic (narrow); prompt-only; model-judged | Partial | CI, ST | **Definition pending** | **Provisional** (definition pending) |
| R4 | Roles and allocated powers | Prompt-only; model-judged | Partial | CI | **Definition pending** | **Provisional** (definition pending) |
| R5 | Applicability | Model-judged, code-enforced (v40 path); deterministic (corpus rules) | Partial | CI, ST | Not assessed | Reportable |
| R6 | Separation and independence of checks | Functional separation; deterministic vetoes; same task routing for validation and appeal | Partial | CI | Not assessed | Reportable |
| R7 | Classified uncertainty | Deterministic rendering; heuristic gaps; prompt-only | Partial | CI | Disclosure: not assessed. **Class assignment: definition pending** | Disclosure reportable; class assignment **provisional** |
| R8 | Inspectable evidence and correction | Deterministic (evidence display); correction pathway not implemented | Partial | CI | Not assessed | Reportable |
| R9 | Citation at the institution's unit of authority | Deterministic | **Partial** (was Implemented) | CI | Not assessed | Reportable |
| R10 | Provenance, expression and temporal applicability | Deterministic (provenance fields) | Partial | CI | Not assessed | Reportable |
| R11 | Authority roles and relations | Deterministic (corpus-specific); model-judged, code-enforced | Partial | CI, ST | **Definition pending** | **Provisional** (definition pending) |
| R12 | Assurance states and failing closed | Deterministic fallbacks; no claim states | Partial | CI, ST | Not assessed | Reportable |
| R13 | Portable safeguards | Deterministic checks portable; others configuration-dependent | Partial | CI | Not assessed | Reportable |
| R14 | Status disclosure | Deterministic (footer) | Partial | CI | Not assessed | Reportable |
| R15 | Source licensing, access and data governance | — | Partial: full search-query text retained at the pin (disclosed historical gap) | CI | Not assessed | Reportable |
| R16 | Conformance by published, bounded evidence | — | Not yet implemented | CI, ST | Not assessed | Reportable |
| R17 | Evidential sufficiency | Deterministic (narrow, corpus-specific) | Not yet implemented | CI | **Definition pending** | **Provisional** (definition pending) |

**Implementation maturity:** 0 implemented, 15 partial, 2 not yet implemented (R16, R17).
**Conformance results:** 12 not assessed; 4 definition pending (R3, R4, R11, R17); 1 split (R7: disclosure not assessed, class assignment definition pending). 0 conformant, 0 not conformant.
**Overall claim:** none. No overall conformance claim is available in 0.6.1, and Structural conformance is proposed, not currently claimable (SPECIFICATION.md §7.3).

Changes from the v0.4.0 matrix (1 implemented / 14 partial / 2 not yet), made at v0.5.0 and unchanged in 0.6.0 and 0.6.1:

- **R9** moves from Implemented to Partial. The code is unchanged; v0.5 R9 now asks for the institution's pinpoint at the granularity relied on, and the stored citation label is unit-level ("SO n").
- **R3, R4, R11, R17** and R7 class assignment are now recorded as *definition pending* rather than *not assessed*, because v0.5.0 made them non-reportable as conformant (called "provisional" from 0.6.0).
- R4 and R10 renamed. No other maturity changes: the remaining v0.5 wording changes were re-checked at the pin and did not change any assessment.
