# 953. Curvature-only geometric Sobolev inequalities beyond mean-convex level sets

**Area:** Geometric analysis and nonlinear elliptic PDEs
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^n`$ be smooth and bounded, $`v\in C_0^\infty(\overline\Omega)`$ in the notation of Castorina and Sanchón, and let $`1\le q<p`$ with $`n>q+1`$. At a regular point of a level set of $`|v|`$, write $`H_v`$ for its mean curvature, normalized so a sphere of radius $`r`$ has $`H_v=1/r`$. Set

```math
\widetilde I_{p,q}(v;\Omega)=\left(\int_\Omega |H_v|^q|\nabla v|^p\,dx\right)^{1/p}.
```


**Question (Castorina–Sanchón, Open Problem 1).** Do all three of the following estimates hold for general $`v`$, without assuming that its level sets are mean-convex, with constants independent of $`v`$ and $`\Omega`$?

1. If $`n<p+q`$, does $`\|v\|_{L^\infty(\Omega)}\le C_1|\Omega|^{(p+q-n)/(np)}\widetilde I_{p,q}(v;\Omega)`$ hold with $`C_1=C_1(n,p,q)`$?
2. If $`n>p+q`$, write $`p_q^*=np/(n-p-q)`$. For every $`1\le r\le p_q^*`$, does $`\|v\|_{L^r(\Omega)}\le C_2|\Omega|^{1/r-1/p_q^*}\widetilde I_{p,q}(v;\Omega)`$ hold with $`C_2=C_2(n,p,q,r)`$?
3. If $`n=p+q`$, writing $`p'=p/(p-1)`$, does $`\int_\Omega\exp\{(|v|/(C_3\widetilde I_{p,q}(v;\Omega)))^{p'}\}\,dx\le\frac{n}{n-1}|\Omega|`$ hold with $`C_3=C_3(n,p)`$?

The authors prove these three estimates with a larger functional $`I_{p,q}`$ that also contains a tangential-gradient term. They ask whether the mean-curvature term alone suffices in the range $`q<p`$. Their cited curvature-only results for $`q\ge p`$ and for mean-convex level sets do not cover the unrestricted question.

## Application

The inequalities would control a function using the curvature of its level sets without measuring tangential changes in $`|\nabla v|`$. Such geometric estimates are a tool in the paper's analysis of stable $`p`$-Laplace solutions. A counterexample would identify a setting where tangential-gradient control is essential.

## References

1. D. Castorina and M. Sanchón, [*Regularity of stable solutions of $`p`$-Laplace equations through geometric Sobolev type inequalities*](https://doi.org/10.4171/JEMS/576), *J. Eur. Math. Soc.* **17** (2015), no. 11, 2949–2975, Open Problem 1, printed p. 2952; [publisher PDF](https://ems.press/content/serial-article-files/33086). The [original arXiv v1](https://arxiv.org/html/1201.3486v1), §1.1, has the same question but numbers the theorem 1.2 and the curvature-only functional (1.4), rather than the published 1.3 and (1.6).
2. M. Qu and Z. Wang, [*Endpoint Morrey interior regularity of stable solutions to the $`p`$-Laplace equation*](https://doi.org/10.3934/era.2026210), *Electronic Research Archive* **34** (2026), 4765–4776. Its estimate is for stable PDE solutions, not the unrestricted curvature-only function inequalities above.

## Status review


**Known cases:** Curvature-only estimates for unrestricted functions with q<p are required. Stable-solution Morrey estimates, tangential-gradient terms and mean-convex restrictions do not cover the formulation.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Curvature-only estimates for unrestricted functions with q<p are required. Stable-solution Morrey estimates, tangential-gradient terms and mean-convex restrictions do not cover the formulation.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The published 2015 version retains the exact open problem. The later endpoint Morrey result concerns stable solutions and does not state any of the unrestricted curvature-only estimates. Targeted proof, counterexample, author and announcement searches through 2026-10-22 found no exact complete resolution; this is a bounded search, not a guarantee about inaccessible work. The related [AIM 444](444-subquadratic-p-laplace-extremal-critical-dimension.md) asks a different regularity question, and the checked AIM and `FURTHER_problems` pages contain no semantic duplicate. The [original-source receipt](../FURTHER_problems/_tracking/castorina-sanchon-curvature-only-original-2026-10-22.json) and [status audit](../FURTHER_problems/_tracking/castorina-sanchon-curvature-only-status-2026-10-22.json) record the exact scopes and search limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-bd24a5c1d58e5099**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
