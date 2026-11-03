# 914. Sharp multiparameter Haar small-ball inequality in dimensions at least three

**Area:** Harmonic analysis and approximation theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`d\ge3`$. For each dyadic interval $`I\subset[0,1)`$, let
$`h_I=\mathbf1_{I_{\rm right}}-\mathbf1_{I_{\rm left}}`$, and for a dyadic rectangle
$`R=I_1\times\cdots\times I_d`$ put $`h_R(x)=\prod_{j=1}^d h_{I_j}(x_j)`$.
These Haar functions have $`L^\infty`$ norm one.

Does a constant $`C_d`$ exist such that, for every integer $`n\ge1`$ and every
choice of real coefficients $`\alpha_R`$ indexed by **all** dyadic rectangles
$`R\subset[0,1)^d`$ with $`|R|\ge2^{-n}`$,
```math
2^{-n}\sum_{\substack{R\subset[0,1)^d\\|R|=2^{-n}}}|\alpha_R|
\le C_d n^{(d-2)/2}
 \left\|\sum_{\substack{R\subset[0,1)^d\\|R|\ge2^{-n}}}
          \alpha_R h_R\right\|_{L^\infty([0,1)^d)}\,?
```


The norm includes the coarser rectangles; their coefficients are unrestricted.

## Application

This bound would sharpen estimates for approximation classes with bounded mixed derivatives and for small deviations of the Brownian sheet. These applications do not identify this statement with every conjecture involving small-ball probabilities.

## Known progress

Orthogonality and Cauchy--Schwarz give the weaker exponent $`(d-1)/2`$.
Reference [1], Theorem 1.5, improves that exponent to $`(d-1)/2-\eta(d)`$ for some positive $`\eta(d)`$, leaving the conjectured exponent unresolved. The two-dimensional case is established. Reference [2] obtains a signed, restricted three-dimensional estimate.

## References

1. D. Bilyk, M. T. Lacey and A. Vagharshakyan, *On the Small Ball Inequality in All Dimensions*, Journal of Functional Analysis **254** (2008), 2470--2502, [doi:10.1016/j.jfa.2007.09.010](https://doi.org/10.1016/j.jfa.2007.09.010); [arXiv:0705.4619v3](https://arxiv.org/pdf/0705.4619v3), Conjecture 1.1 and Theorem 1.5. [Version record](https://arxiv.org/abs/0705.4619).
2. D. Bilyk, M. T. Lacey, I. Parissis and A. Vagharshakyan, *A three-dimensional signed small ball inequality*, [author manuscript](https://www-users.cse.umn.edu/~dbilyk/papers/lnsBiLaPaVa.pdf), abstract and p.3, equation (1.5) and its scope clarification.

## Status review


**Known cases:** The dimensional exponent improvement and signed restricted three-dimensional estimates do not reach the conjectured exponent for all coefficients, including unrestricted coarser rectangles. Brownian-sheet and discrepancy results with different norms or hypotheses do not directly establish this Haar sup-norm inequality.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The dimensional exponent improvement and signed restricted three-dimensional estimates do not reach the conjectured exponent for all coefficients, including unrestricted coarser rectangles. Brownian-sheet and discrepancy results with different norms or hypotheses do not directly establish this Haar sup-norm inequality.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The coordinator checked the displayed conjecture in the actual latest v3, its Haar normalization and the hypotheses of the cited partial results. Bounded searches on 25 October 2026 found no matching proof, counterexample or complete announcement. This is a dated search finding, not exhaustive literature coverage or certification of the cited proofs.

The duplicate comparison used all 1,703 pinned AIM/OpenAI statements and all 905 preceding local findings. AIM 536 concerns infinite-sequence star discrepancy; AIM 660 concerns product-prior probability ratios. Local Brownian-sheet level-set and posterior-mode questions also have different targets. No equivalent target was located.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-9126dcde4ff29aa5**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
