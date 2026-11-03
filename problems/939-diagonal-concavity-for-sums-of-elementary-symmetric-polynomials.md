# 939. Diagonal concavity for sums of elementary symmetric polynomials

**Area:** Nonlinear analysis and curvature equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`1\le p\le n`$ and let $`a_0,\ldots,a_p\ge0`$ be not all zero. On the positive orthant $`\Gamma_n=(0,\infty)^n`$, set
```math
\sigma_0(x)=1,\qquad
\sigma_k(x)=\sum_{1\le i_1<\cdots<i_k\le n}x_{i_1}\cdots x_{i_k},\qquad
f_a(x)=\sum_{k=0}^p a_k\sigma_k(x).
```

Its diagonal restriction is
```math
P_a(t)=f_a(t,\ldots,t)=\sum_{k=0}^p a_k\binom nk t^k.
```

Prove or disprove: if $`t\mapsto P_a(t)^{1/p}`$ is concave on $`(0,\infty)`$, then $`x\mapsto f_a(x)^{1/p}`$ is concave on all of $`\Gamma_n`$.

The reverse implication follows by restriction to the diagonal. Equivalently, does the scalar condition
```math
P_a(t)P_a''(t)-\left(1-\frac1p\right)P_a'(t)^2\le0\qquad(t>0)
```

suffice for full concavity? No real-rootedness assumption is imposed. The exponent remains $`1/p`$ if $`a_p=0`$.

## Application

An exact one-variable concavity test would simplify checking structural assumptions for nonlinear curvature equations, including combinations of elementary symmetric curvatures in Lovelock constraint equations.

## References

1. X. Lachaume, [*On the concavity of a sum of elementary symmetric polynomials*](https://arxiv.org/abs/1712.10327), v1 (2017), Definition 1.1, Conjecture 1 on pp.3 and 8, and Theorem 3.3.
2. X. Lachaume, [*The constraint equations of Lovelock gravity theories: a new $`\sigma_k`$-Yamabe problem*](https://arxiv.org/html/1712.04528), v2 (2018), Definition 2.4 and Theorem 2.7(d); *Journal of Mathematical Physics* **59** (2018), 072501. [DOI](https://doi.org/10.1063/1.5023758).

## Status review


**Known cases:** The scalar hypothesis is diagonal concavity, not real-rootedness. Quadratic cases and derivative-convolution announcements do not prove this general implication.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The scalar hypothesis is diagonal concavity, not real-rootedness. Quadratic cases and derivative-convolution announcements do not prove this general implication.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reference 1 proves the quadratic case. Reference 2 shows that real-rootedness of $`P_a`$ implies concavity of $`f_a^{1/p}`$. That sufficient condition is stronger than the diagonal-concavity hypothesis here and does not settle the general question.

A 2026 public announcement concerning derivative convolution addresses different conjectures in reference 1 and explicitly does not claim this one. The [coordinating review](../FURTHER_problems/_tracking/focused-C198-Steklov-Lachaume-two-precise-gates-C-20261028/ROOT-LACHAUME-FINAL-SCIENTIFIC-REVIEW.json) records source and comparator checks, current-resolution and announcement searches, semantic duplicate comparisons and independent model review. It also preserves an inconsistent implication in the source's summary without relying on it. Bounded searches do not prove continued openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-292951d1c43dcebb**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
