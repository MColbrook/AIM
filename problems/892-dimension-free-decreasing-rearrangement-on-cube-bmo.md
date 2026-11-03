# 892. Dimension-free decreasing rearrangement on cube BMO

**Area:** Operators, matrices and computation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a real locally integrable function $`f`$ on $`\mathbb R^n`$, write
```math
f_Q=\frac1{|Q|}\int_Q f,\qquad
\|f\|_{\mathrm{BMO}(\mathbb R^n)}
=\sup_Q\frac1{|Q|}\int_Q|f-f_Q|,
```
where $`Q`$ ranges over finite open cubes with sides parallel to the coordinate axes. On $`(0,\infty)`$, use the same seminorm with all finite open intervals contained in this half-line, including $`(0,b)`$.

Call $`f`$ rearrangeable when
```math
\mu_f(a)=|\{x:|f(x)|>a\}|\longrightarrow0
\quad(a\longrightarrow\infty),
```
and define its decreasing rearrangement by
```math
f^*(s)=\inf\{a\ge0:\mu_f(a)\le s\},\qquad s>0.
```

Does there exist one finite constant $`C`$, independent of $`n`$ and $`f`$, such that
```math
\|f^*\|_{\mathrm{BMO}(0,\infty)}
\le C\|f\|_{\mathrm{BMO}(\mathbb R^n)}
```
for every integer $`n\ge1`$ and every real rearrangeable $`f\in\mathrm{BMO}(\mathbb R^n)`$?

The question asks for a uniform bound, without prescribing the best constant.

## Known progress and scope

Dimension-dependent bounds are known. Burchard, Dafni and Gibara improve the growth to $`O(\sqrt n)`$, and explicitly leave dimension independence open [1,2].

The sharp bound for the stronger seminorm based on all axis-parallel rectangles does not give this cube-seminorm bound. Sharp dimension growth for dyadic BMO measured with quadratic mean oscillation also concerns a different space and seminorm [2].

The more recent rearrangement contraction for quantitative VMO uses an interval and a quadratic Campanato-type norm [3, Theorem 1.3]. Its higher-dimensional Remark 1.2 concerns the preceding criterion for existence of nonconstant functions, rather than a higher-dimensional rearrangement theorem. The averaging-class contraction in [4] also starts from an interval and uses an infimum over centers in its seminorm.

## Application

Rearrangement reduces distributional questions about functions of many variables to one variable. A uniform bound would remove dimensional loss in this reduction for mean oscillation and improve corresponding John–Nirenberg constants [2].

## References

1. A. Burchard, G. Dafni and R. Gibara, *Vanishing mean oscillation and continuity of rearrangements*, Advances in Mathematics **437** (2024), 109379. [DOI](https://doi.org/10.1016/j.aim.2023.109379); [arXiv:2201.05130v1](https://arxiv.org/abs/2201.05130v1), Introduction and §2.
2. A. Burchard, G. Dafni and R. Gibara, *Mean oscillation bounds on rearrangements*, Transactions of the American Mathematical Society **375** (2022), 4429–4444. [DOI](https://doi.org/10.1090/tran/8629); [arXiv:2011.09111v2](https://arxiv.org/abs/2011.09111v2), Theorem 1.1 and the discussion following it.
3. L. Slavin and P. Zatitskii, *Monotone rearrangement does not increase generalized Campanato norm in VMO*, Journal of Functional Analysis **288** (2025), no. 7, 110828. [DOI](https://doi.org/10.1016/j.jfa.2025.110828); [arXiv:2301.01846v2](https://arxiv.org/abs/2301.01846v2), §1 and Theorem 1.3.

4. M. Abdrakhmanov, L. Slavin and P. Zatitskii, *Monotone rearrangement in averaging classes*, Proceedings of the American Mathematical Society, Series B **11** (2024), 489–498. [DOI](https://doi.org/10.1090/bproc/239); [arXiv:2306.16690v1](https://arxiv.org/abs/2306.16690v1), equations (1.1)–(1.5) and Theorem 1.2.

## Status review


**Known cases:** The current cube-BMO rearrangement bound grows as square root of dimension. Rectangle-seminorm bounds and one-dimensional quadratic Campanato or VMO contraction use other averaging families or norms; they do not give the all-dimensional cube mean-absolute-oscillation estimate.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current cube-BMO rearrangement bound grows as square root of dimension. Rectangle-seminorm bounds and one-dimensional quadratic Campanato or VMO contraction use other averaging families or norms; they do not give the all-dimensional cube mean-absolute-oscillation estimate.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The eligible preprints and the published 2024 introduction explicitly leave this question open. Checks through 24 October 2026 found no matching announced solution. The interval VMO result above does not settle the stated arbitrary-dimensional cube-BMO question.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0e0d4e35a99834fd**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
