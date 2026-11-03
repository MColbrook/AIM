# 995. A spectral gap for Brownian loops on the round two-sphere

**Area:** Geometric stochastic analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`S^2`$ have its unit round metric, fix the north pole $`o`$, and let $`\mu`$ be the law of the duration-one Brownian bridge from $`o`$ to $`o`$, where Brownian motion has generator $`\frac12\Delta_{S^2}`$. Thus $`\mu`$ is a probability measure on $`\{\sigma\in C([0,1];S^2):\sigma(0)=\sigma(1)=o\}`$.

For $`\mu`$-almost every path, let $`{\parallel}_t:T_oS^2\to T_{\sigma(t)}S^2`$ be stochastic Levi–Civita parallel translation. Write
```math
H_{00}=\{h\in H^1([0,1];T_oS^2):h(0)=h(1)=0\},\qquad
\|h\|_{H_{00}}^2=\int_0^1|\dot h(t)|^2\,dt .
```
For a real smooth cylindrical function
```math
F(\sigma)=f(\sigma(t_1),\ldots,\sigma(t_k)),\qquad
f\in C^\infty((S^2)^k),\quad 0<t_1<\cdots<t_k<1,
```
define its Bismut derivative by
```math
d_HF(\sigma)[h]=\sum_{i=1}^k
\langle\nabla_i f(\sigma(t_1),\ldots,\sigma(t_k)),
{\parallel}_{t_i}h(t_i)\rangle .
```
Use the dual norm on $`H_{00}^*`$. Equivalently, if
```math
a_i(\sigma)={\parallel}_{t_i}^{-1}
\nabla_i f(\sigma(t_1),\ldots,\sigma(t_k)),
```
then
```math
\|d_HF(\sigma)\|_{H_{00}^*}^2
=\sum_{i,j=1}^k(\min(t_i,t_j)-t_it_j)
\langle a_i(\sigma),a_j(\sigma)\rangle .
```

**Question.** Is there a finite constant $`C`$, independent of $`k`$, the evaluation times and $`f`$, such that
```math
\mathrm{Var}_{\mu}(F)
\le C\int \|d_HF(\sigma)\|_{H_{00}^*}^2\,\mu(d\sigma)
```
for every such smooth cylindrical $`F`$?

## Application

The inequality would control fluctuations of functions of Brownian loops by their energy under path perturbations. It is a basic test of how curvature affects analysis on an infinite-dimensional space, even when the underlying surface is the familiar round sphere.

## References

1. K. D. Elworthy and Xue-Mei Li, [*Geometric stochastic analysis on path spaces*](https://arxiv.org/abs/1911.09764v1), Section 4, physical pp. 18–19 of the inspected 22-page preprint, explicitly mention the sphere spectral-gap question. Related ICM 2006 chapter, vol. III, pp. 575–594, [DOI](https://doi.org/10.4171/022-3/30); final-edition body parity remains pending.
2. Xin Chen, Xue-Mei Li and Bo Wu, [*A concrete estimate for the weak Poincaré inequality on loop space*](https://www.xuemei.org/Concrete-Estimates.pdf), *Probability Theory and Related Fields* **151** (2011), 559–590, [DOI](https://doi.org/10.1007/s00440-010-0308-5). Its introductory definitions and formula (1.2) specify the bridge gradient above; Theorem 5.1 gives a weaker inequality.
3. Shigeki Aida, [*Asymptotics of spectral gaps on loop spaces over a class of Riemannian manifolds*](https://www.ms.u-tokyo.ac.jp/~aida/paper/preprint/asymptotics-sgap-corrected-final.pdf), [DOI](https://doi.org/10.1016/j.jfa.2015.09.023), Theorem 3.6 and its global-pole hypothesis; selected corrected author version inspected.

## Status review


**Known cases:** The fixed Brownian bridge on the round two-sphere and its specified H00 gradient require a strong Poincare inequality. Weak Poincare estimates, global-pole geometries and negative-curvature counterexamples do not cover this.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The fixed Brownian bridge on the round two-sphere and its specified H00 gradient require a strong Poincare inequality. Weak Poincare estimates, global-pole geometries and negative-curvature counterexamples do not cover this.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

This is the fixed round-sphere prototype of the broader question in [1]. The ordinary H1 norm is explicit here. On the unit sphere, the Ricci endomorphism is the identity, so the corresponding damped norm is uniformly equivalent on endpoint-zero tangent paths. Existence of a gap is unchanged by that norm comparison.

Reference [2] proves a weak inequality with an additional squared uniform-norm term and an energy coefficient that grows as that defect tends to zero. It does not give the finite constant requested here. Reference [3] proves a positive result under a global-pole assumption that the round sphere does not satisfy; its restricted-domain asymptotics also differ from the full-loop question.

Known counterexamples obtained by changing a sphere's metric, and inequalities for hyperbolic spaces, loop-group heat-kernel measures or ground-state reweightings, do not by their inspected statements settle this prototype. No matching complete positive or counterexample was located in the recorded bounded current checks. These checks do not certify that no resolution exists.

The cylindrical inequality is equivalent to a gap for its minimal closed Dirichlet form by closure. No assertion about uniqueness of all extensions of the loop operator is part of this question.

The [source review](../FURTHER_problems/_tracking/parallel/rough-filtering/round-sphere-loop-spectral-gap-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-round-sphere-loop-spectral-gap-review.json), [current comparisons](../FURTHER_problems/_tracking/sphere-loop-gap-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/sphere-loop-gap-duplicates-review-2026-10-19.json), [broader comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/round-sphere-loop-duplicates-review.json), [catalogue review](../FURTHER_problems/_tracking/sphere-loop-gap-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/sphere-loop-gap-coordinator-review-2026-10-19.json) record the evidence and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-2c34fb17a5e9ebf8**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
