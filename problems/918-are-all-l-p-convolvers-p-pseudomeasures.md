# 918. Are all $`L^p`$-convolvers $`p`$-pseudomeasures?

**Area:** Functional analysis and operator algebras
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`G`$ be a locally compact group with left Haar measure, and let $`1<p<\infty`$, $`p\ne2`$. Left convolution gives a representation $`\lambda_p:L^1(G)\to\mathcal B(L^p(G))`$. Inside $`\mathcal B(L^p(G))`$, set

```math
PF_p(G)=\overline{\lambda_p(L^1(G))}^{\|\cdot\|},\qquad
PM_p(G)=\overline{\lambda_p(L^1(G))}^{\mathrm{WOT}},\qquad
CV_p(G)=\lambda_p(L^1(G))''.
```


Here $`\mathrm{WOT}`$ is the weak operator topology, and the double prime means the bicommutant. One always has $`PM_p(G)\subseteq CV_p(G)`$. **Must $`PM_p(G)=CV_p(G)`$ for every locally compact $`G`$ and every such $`p`$?** Equivalently, is every $`L^p`$-convolver a weak-operator limit of left-convolution operators from $`L^1(G)`$?

This is the unresolved core of Gardella's Question 4.12, which states the question for all $`p\in[1,\infty)`$.

## Application

The equality would make two natural descriptions of operators invariant under group translation coincide. It is a Banach-space analogue of the Hilbert-space bicommutant phenomenon, relevant to harmonic analysis and $`L^p`$ operator algebras.

## Known results and scope

The cases $`p=1`$ and $`p=2`$ are known, as are all $`p`$ when $`G`$ has the approximation property; this includes amenable groups. Gardella and Thiel's later paper solves an **isomorphism** problem for these algebras but explicitly retains their equality as an open problem. The question here imposes no amenability, approximation property, discreteness, or second-countability assumption on $`G`$.

## References

1. E. Gardella, [*A modern look at algebras of operators on $`L^p`$-spaces*](https://arxiv.org/abs/1909.12096v1), *Expositiones Mathematicae* **39** (2021), 420–453, [DOI:10.1016/j.exmath.2020.10.003](https://doi.org/10.1016/j.exmath.2020.10.003). Definition 4.3, Proposition 4.9 and Question 4.12 in the [arXiv full text](https://arxiv.org/html/1909.12096v1).
2. E. Gardella and H. Thiel, [*Isomorphisms of algebras of convolution operators*](https://smf.emath.fr/sites/default/files/2022-12/ens_ann-sc_55_1433-1471__sample.pdf), *Annales Scientifiques de l'École Normale Supérieure* **55** (2022), 1433–1471, [DOI:10.24033/asens.2520](https://doi.org/10.24033/asens.2520), introduction, printed p. 1435.

## Status review


**Known cases:** The approximation-property case and p=1,2 are known. Isomorphisms of convolution-operator algebras do not identify WOT-closed pseudomeasures with all bicommutant convolvers. No all-group, all-nonHilbert-p resolution was located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The approximation-property case and p=1,2 are known. Isomorphisms of convolution-operator algebras do not identify WOT-closed pseudomeasures with all bicommutant convolvers. No all-group, all-nonHilbert-p resolution was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The later published paper still calls this equality open, while distinguishing it from the isomorphism result it proves. Targeted source, theorem, counterexample and announcement searches through 23 October 2026 found no general resolution. A semantic search found no matching AIM or admitted FURTHER problem. These are bounded checks, and the publisher's native PDF of Reference 1 was not obtained. The [review audit](../FURTHER_problems/_tracking/arxiv2239-convolvers-pseudomeasures-review-2026-10-23.json) records evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a13830d8fb26a65f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
