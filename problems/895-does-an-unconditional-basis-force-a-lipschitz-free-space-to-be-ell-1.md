# 895. Does an unconditional basis force a Lipschitz-free space to be $`\ell_1`$?

**Area:** Functional analysis and Lipschitz-free Banach spaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M,d,0)`$ be a pointed metric space, and let $`\mathcal F(M)`$ be the real Lipschitz-free Banach space: the closed linear span of the evaluation vectors $`\delta_x`$ in $`\mathrm{Lip}_0(M)^*`$, where $`\mathrm{Lip}_0(M)`$ consists of real Lipschitz functions vanishing at $`0`$. If $`\mathcal F(M)`$ admits an **unconditional Schauder basis**, must it be linearly isomorphic to $`\ell_1`$?

This is Open problem 1 in Novotný's paper. The word *unconditional* applies to any Schauder basis of $`\mathcal F(M)`$, not just one obtained from retractions or extension operators on $`M`$.

**Editorial clarification:** State explicitly that the Schauder basis is an infinite sequence, so the intended infinite-dimensional question is not confused with the elementary finite-metric case.

## Application

Lipschitz-free spaces turn Lipschitz maps into linear operators. The question asks whether the strong linear coordinate structure of an unconditional basis rigidly determines the space up to isomorphism.

## Known results and scope

Novotný proves that certain nets in $`\mathbb R^n`$, $`n\geq2`$, have no **retractional** unconditional basis. This does not rule out another unconditional basis for their free spaces and does not answer the general question. If $`M`$ contains a line segment, $`\mathcal F(M)`$ contains an isomorphic copy of $`L_1[0,1]`$ and so cannot have an unconditional basis. These observations leave the source's converse open.

## References

1. M. Novotný, [*Some Remarks on Schauder Bases in Lipschitz Free Spaces*](https://arxiv.org/pdf/1905.13188v2), *Bulletin of the Belgian Mathematical Society – Simon Stevin* **27** (2020), 111–126, [DOI:10.36045/bbms/1590199307](https://doi.org/10.36045/bbms/1590199307), Open problem 1 (arXiv v2, printed p. 14). [Institutional bibliographic record](https://intranet.fel.cvut.cz/en/research/13101/publication/2020.html).
2. R. J. Aliaga, [*Lipschitz-free spaces and purely 1-unrectifiable metric spaces*](https://arxiv.org/pdf/2606.02918), arXiv:2606.02918v2 (2026), introduction. This exposition studies different structural properties; it does not state the requested unconditional-basis implication.

## Status review


**Known cases:** The question is about existence of an unconditional Schauder basis in the infinite-dimensional sense, not a selected retractional basis. Negative retractional-basis results and structural claims about other properties do not settle the existence implication for arbitrary Lipschitz-free spaces.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The question is about existence of an unconditional Schauder basis in the infinite-dimensional sense, not a selected retractional basis. Negative retractional-basis results and structural claims about other properties do not settle the existence implication for arbitrary Lipschitz-free spaces.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The latest arXiv version retains Open problem 1. Targeted later-primary, proof, counterexample and announcement searches through 23 October 2026 found no result settling this general implication. A semantic check found no matching AIM or admitted FURTHER problem. These are bounded checks. The published article's identity was verified, but its native PDF was not obtained, so exact publication-text parity is not claimed. The [source and status audit](../FURTHER_problems/_tracking/arxiv2139-two-candidate-independent-audit-2026-10-23.json) records the locators and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-20752392e6f922bb**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
