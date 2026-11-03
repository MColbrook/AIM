# 1060. Does the Pearcey critical profile satisfy the Benjamin–Ono string equation?

**Area:** Nonlinear dispersive waves; Benjamin–Ono equation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Blackstone, Miller and Mitchell define a Pearcey integral $`\tau(T,X)`$ in their equation (1.52) and the real profile

```math
U(T,X)=-2\mathrm{Im}\,\partial_X\log\tau(T,X).
```


Assume their separate **Conjecture 1.9**: $`\tau(T,X)\ne0`$ for all real $`(T,X)`$. Prove **Conjecture 1.10**: for every real $`T`$, this globally defined $`U`$ satisfies the nonlocal Benjamin–Ono string equation

```math
X-2UT+4U^3-6U|D_X|U-3|D_X|(U^2)-4U_{XX}=0,
```


where $`|D_X|`$ is the Fourier multiplier $`|\xi|`$, with the principal-value interpretation specified by the cited paper. Its $`X\to\pm\infty`$ behavior is given in equation (1.53). This is the normalized form of the string equation proposed by Masoero, Raimondo and Antunes in 2015; the zero-free assertion is an explicit prerequisite, not a proved fact.

## Application

The proposed string equation describes the universal critical profile near a Benjamin–Ono dispersive shock. A 2026 theorem identifies the Pearcey profile as a scaling limit for a class of rational initial data away from zeros of $`\tau`$. Showing that this profile obeys the predicted nonlocal equation would connect that rigorous limit to the earlier string-equation picture. The 2026 paper checks the identity numerically and derives a related coupled local system, but leaves the nonlocal identity unproved.

## References

1. D. Masoero, A. Raimondo and P. R. S. Antunes, [*Critical behaviour for scalar nonlinear waves*](https://arxiv.org/html/1312.3880), arXiv:1312.3880v3 (2015); *Physica D* **292–293** (2015), 1–7, [doi:10.1016/j.physd.2014.09.007](https://doi.org/10.1016/j.physd.2014.09.007). Section IV, equations (15) and (18), and “A new Painlevé equation?”
2. E. Blackstone, P. D. Miller and M. D. Mitchell, [*Universality in the Small-Dispersion Limit of the Benjamin–Ono Equation*](https://link.springer.com/article/10.1007/s00220-025-05506-z), *Communications in Mathematical Physics* **407** (2026), article 60, [doi:10.1007/s00220-025-05506-z](https://doi.org/10.1007/s00220-025-05506-z). Equations (1.51)–(1.53), Theorem 1.7, Conjectures 1.9–1.10, and equation (1.60).

## Status review


**Known cases:** The zero-free Pearcey assertion is an explicit premise, while the remaining target is the exact nonlocal string equation. Limiting-profile theorems, numerical tests and a coupled local system do not establish that identity.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The zero-free Pearcey assertion is an explicit premise, while the remaining target is the exact nonlocal string equation. Limiting-profile theorems, numerical tests and a coupled local system do not establish that identity.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The later paper explicitly calls this equation-verification claim Conjecture 1.10 and says that numerical checks and a coupled local system do not constitute a proof. Its theorem for rational initial data establishes a limiting profile under stated hypotheses, not the nonlocal string equation or the zero-free premise. The original paper's separate meromorphic-continuation and isomonodromic-linearization questions are outside this entry. A bounded search through 2026-10-21 located no exact-scope proof or announcement. The [source-bound arXiv packet](../FURTHER_problems/_tracking/parallel/rough-filtering/arxiv-body-secondpass-0184-review.json), [independent status review](../FURTHER_problems/_tracking/benjamin-ono-pearcey-string-status-2026-10-21.json), and [duplicate snapshot](../FURTHER_problems/_tracking/benjamin-ono-pearcey-string-duplicates-2026-10-21.json) record the limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c6f3e9dfbda61171**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
