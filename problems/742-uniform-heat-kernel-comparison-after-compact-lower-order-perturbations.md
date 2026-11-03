# 742. Uniform heat-kernel comparison after compact lower-order perturbations

**Area:** Diffusion, materials and variational problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a smooth, connected, noncompact Riemannian manifold with a fixed positive smooth measure $`d\mu`$. Let $`P_1,P_2`$ be real second-order elliptic operators with smooth coefficients and the same principal part. In local coordinates, write

```math
P_j=-\sum_{r,s=1}^N a^{rs}(x)\partial_r\partial_s
       +\sum_{r=1}^N b_j^r(x)\partial_r+c_j(x),\qquad j=1,2,
```


where the common symmetric matrix $`A=(a^{rs})`$ is positive definite and locally uniformly elliptic. Let $`k_j(x,y,t)`$ be the positive minimal heat kernel of $`\partial_t+P_j`$, relative to $`d\mu`$.

Assume that $`P_1=P_2`$ outside a compact subset of $`M`$, and that both operators have generalized principal eigenvalue zero:

```math
\lambda_0(P_j,1,M)
=\sup\{\lambda\in\mathbb R:\exists u\in C^2(M),\ u>0,\ (P_j-\lambda)u=0\}=0.
```


Assume also that both are **subcritical**, meaning

```math
\int_0^\infty k_j(x,y,t)\,dt<\infty\qquad(x\ne y).
```


Must there exist a constant $`C\ge1`$, depending on the pair of operators but independent of $`x,y,t`$, such that

```math
C^{-1}k_2(x,y,t)\le k_1(x,y,t)\le Ck_2(x,y,t)
\qquad\text{for every }x,y\in M,\ t>0?
```


This is the smooth, zero-threshold case of [1, Conjecture 1.1], including its explicit requirement that the principal parts coincide. Symmetry and on-diagonal doubling are not assumed. The zero-threshold restriction keeps subcriticality at the stated spectral threshold.

## Application

Heat kernels describe the propagation of heat and diffusion. Uniform comparison would quantify stability when drift and reaction terms change only in a bounded region, throughout space and time. The source also connects this problem with stability of the parabolic Martin boundary.

## References

1. D. Ganguly and Y. Pinchover, [*On the equivalence of heat kernels of second-order parabolic operators*](https://arxiv.org/html/1606.08601v2), arXiv:1606.08601v2 (6 July 2017), Conjecture 1.1, Section 2, Theorem 2.5(3) and Section 7.3(1); published in *Journal d'Analyse Mathématique* **140** (2020), 549–589, [DOI](https://doi.org/10.1007/s11854-020-0097-4).
2. Y. Pinchover, [*Some Aspects of Large Time Behavior of the Heat Kernel: An Overview with Perspectives*](https://link.springer.com/chapter/10.1007/978-3-0348-0591-9_6), in *Mathematical Physics, Spectral Theory and Stochastic Analysis*, edited by M. Demuth and W. Kirsch, Operator Theory: Advances and Applications **232**, Birkhäuser Basel (2013), 299–339. Definition 9.1 and Conjecture 9.2 appear at printed p. 333. This was the book discovery route; the requirement that the principal parts coincide follows the explicit later formulation [1].

## Status review


**Known cases:** The comparison is uniform for all points and times under arbitrary smooth compactly supported lower-order perturbations, without symmetry or doubling. Symmetric potential perturbations with on-diagonal doubling and critical/subcritical long-time ratios do not cover it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The comparison is uniform for all points and times under arbitrary smooth compactly supported lower-order perturbations, without symmetry or doubling. Symmetric potential perturbations with on-diagonal doubling and critical/subcritical long-time ratios do not cover it.

Additional comparison sources: [comparison source 1](https://arxiv.org/html/1606.08601v2); [comparison source 2](https://doi.org/10.1007/s11854-020-0097-4); [comparison source 3](https://link.springer.com/chapter/10.1007/978-3-0348-0591-9_6). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 23 October 2026. Theorem 2.5(3) of [1] proves comparison for symmetric operators differing by a compactly supported potential when **both** heat kernels satisfy its on-diagonal doubling condition. Section 7.3(1) asks whether that extra condition can be removed. Those hypotheses do not settle the target above.

The [coordinator review](../FURTHER_problems/_tracking/heat-kernel-compact-perturbation-coordinator-review-2026-10-23.json) and [independent source/status audit](../FURTHER_problems/_tracking/parallel/continuum/author-books-cue-breadth-20261022/d025-heat-kernel-equivalence-corrected-scope-status-hold-20261023.json) found no matching complete proof, counterexample or announced resolution in bounded dated searches. The latest arXiv statement was read; the 2020 publisher's subscription body was unavailable, so full published-version parity is not claimed.

Duplicate checks across all statuses include AIM 217, which compares a critical operator with a subcritical operator in a long-time ratio. Its recorded counterexample concerns a different class and conclusion. The [duplicate audit](../FURTHER_problems/_tracking/parallel/continuum/author-books-cue-breadth-20261022/d025-heat-kernel-equivalence-all-status-duplicate-audit-20261023.json) also covers pending, held, excluded and admitted FURTHER findings. These bounded searches do not prove that no resolution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-eb520a1e2d42f351**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
