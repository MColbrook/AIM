# 955. Weak comparison for singular p-Laplacian evolution

**Area:** PDEs, fluids and materials
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^N`$ be bounded, connected and Lipschitz, $`T>0`$, $`1<p<2`$, and
```math
0<\lambda\leq\lambda_{1,p}(\Omega)
:=\inf_{0\neq w\in W^{1,p}_0(\Omega)}
\frac{\int_\Omega |\nabla w|^p}{\int_\Omega |w|^p}.
```

Take $`0\leq f\leq g`$ in $`L^\infty(\Omega\times(0,T))`$ and $`0\leq u_0\leq v_0`$ in $`W^{1,p}_0(\Omega)\cap L^2(\Omega)`$. Consider
```math
u_t-\Delta_pu=\lambda|u|^{p-2}u+f,\qquad
 v_t-\Delta_pv=\lambda|v|^{p-2}v+g,
```

with those initial values and zero lateral Sobolev traces.

Must **every** such weak pair satisfy $`u\leq v`$ almost everywhere?
Here each solution $`z`$ belongs to
$`C([0,T];L^2(\Omega))\cap L^p(0,T;W^{1,p}_0(\Omega))`$, takes its initial value in $`L^2`$, and satisfies
```math
\left[\int_\Omega z\phi\right]_0^\tau+
\int_0^\tau\!\int_\Omega
\left(-z\phi_t+|\nabla z|^{p-2}\nabla z\cdot\nabla\phi\right)
=\int_0^\tau\!\int_\Omega(\lambda|z|^{p-2}z+h)\phi
```

for every $`0<\tau\leq T`$ and
$`\phi\in W^{1,2}(0,\tau;L^2(\Omega))\cap L^p(0,\tau;W^{1,p}_0(\Omega))`$, with $`h=f`$ or $`g`$.

## Application

Order preservation would give stability under increases in forcing and initial data; applying it in both directions to equal data would also give uniqueness in this weak class.

## References

- V. Bobkov and P. Takáč, *On maximum and comparison principles for parabolic problems with the p-Laplacian*, RACSAM **113** (2019), 1141–1158, [DOI](https://doi.org/10.1007/s13398-018-0536-6). The question is **Remark 2.3**; the weak formulation is in §2. [Primary text, arXiv v1](https://arxiv.org/html/1803.09562v1).
- V. Bobkov, [author’s comparison-principles talk](https://smath.ru/upload/iblock/002/TAF-70_Bobkov.pdf), 3–4 June 2025, slides 11–16.

## Status review


**Known cases:** The endpoint lambda=first eigenvalue and every weak solution pair with nonnegative data are included. Sign-changing-forcing and larger-lambda counterexamples do not cover this range; author publications reveal no matching new theorem.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The endpoint lambda=first eigenvalue and every weak solution pair with nonnegative data are included. Sign-changing-forcing and larger-lambda counterexamples do not cover this range; author publications reveal no matching new theorem.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Open in the stated nonnegative-data range; checked 28 October 2026.** The source proves nonnegativity, but leaves pairwise weak comparison open. Its counterexamples require sign-changing forcing or $`\lambda>\lambda_{1,p}`$. The 2025 talk presents those established parameter ranges. Searches found no complete resolution or announced solution; one-dimensional stationary-versus-evolution strong comparison and fractional elliptic comparison have different hypotheses.

The formulation preserves the endpoint $`\lambda=\lambda_{1,p}`$. It adds no strict positivity or classical-solution assumption. Semantic comparison with all-status AIM and private records found no equivalent question; AIM 427 concerns stationary strong comparison.

Review evidence: [owner](../FURTHER_problems/_tracking/focused-parabolic-singular-p-Laplacian-WCP-C215-A-20261028/OWNER-EXACT-NONNEGATIVE-DATA-SUBQUADRATIC-PARABOLIC-WEAK-COMPARISON-PRIMARY-CURRENT-DUPLICATE-PROPOSAL.json), [independent model review](../FURTHER_problems/_tracking/focused-parabolic-singular-p-Laplacian-WCP-C215-A-20261028/C-INDEPENDENT-EXACT-WEAK-CLASS-NONNEGATIVE-DATA-REACTION-SIGN-AND-EIGENVALUE-RANGE-MODEL-PEER-PASS.json), [coordinating review](../FURTHER_problems/_tracking/focused-parabolic-singular-p-Laplacian-WCP-C215-A-20261028/ROOT-EXACT-SINGULAR-WCP-PRIMARY-CURRENT-AND-SEMANTIC-FINAL-REVIEW.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c5988173ecc2dbcb**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
