# 965. Must every global subcritical heat flow vanish in energy norm?

**Area:** Nonlinear parabolic equations; reaction–diffusion
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For an integer $`N\ge1`$, set

```math
p_S(N)=\begin{cases}(N+2)/(N-2),&N\ge3,\\+\infty,&N=1,2.\end{cases}
```

Fix $`1<p<p_S(N)`$ and define the real energy space

```math
\mathcal E_{N,p}=\{v\in L^{p+1}(\mathbb R^N;\mathbb R):\nabla v\in L^2(\mathbb R^N;\mathbb R^N)\},
\qquad
\|v\|_{\mathcal E_{N,p}}=\|v\|_{L^{p+1}}+\|\nabla v\|_{L^2},
```

where the gradient is weak. Let $`u_0\in\mathcal E_{N,p}`$ and suppose its canonical maximal forward solution to

```math
\partial_tu-\Delta u=|u|^{p-1}u\quad\text{on }\mathbb R^N\times(0,\infty),
\qquad u(0,\cdot)=u_0,
```

exists globally. Here the solution belongs to $`C([0,\infty);\mathcal E_{N,p})`$, satisfies the usual heat-semigroup Duhamel formula, and is classical for positive times. There is no spatial boundary. Must

```math
\lim_{t\to\infty}\bigl(\|u(t)\|_{L^{p+1}(\mathbb R^N)}+\|\nabla u(t)\|_{L^2(\mathbb R^N)}\bigr)=0?
```

The data may change sign and need not be radial. Global existence is assumed; no uniform decay rate, smallness, finite number of sign changes, exponential spatial tail, or uniform bound over all positive times is assumed.

## Application

This asks whether diffusion eventually removes every globally regular finite-energy state despite the focusing reaction. The decreasing energy functional is different from the positive norm appearing in the question.

## Known progress

The question is stated after(1.18) in[1]. That paper proves sufficient one-dimensional cases with finitely many sign changes of both the initial profile and its derivative, and recalls results for exponentially decreasing initial data. Its general question is broader than those cases.

The later overview[2] discusses restricted pointwise decay and weighted-data results; this is not a statement that the exact energy-norm question has been resolved. The optimal Liouville theorem[3] concerns positive solutions. The energy-critical, ground-state-threshold theorem[4], the potential-well theorem for a subcritical equation with an additional linear absorption term[5], and the recent small-data global-existence theorem[6] have different hypotheses or conclusions. The singular self-similar solutions in[7] are outside this global energy-solution class.

## References

1. T. Bartsch, P. Poláčik and P. Quittner, [*Liouville-type theorems and asymptotic behavior of nodal radial solutions of semilinear heat equations*](https://ems.press/journals/jems/articles/1949), J. Eur. Math. Soc.13(1)(2011),219–247, DOI10.4171/JEMS/250. Definition(1.5), equation(1.10), question after(1.18), and Proposition5.4; printed pp.221–224,239–241.
2. P. Quittner, [*A priori estimates of solutions to local and nonlocal superlinear parabolic problems*](https://arxiv.org/abs/2412.05855v2), v2(22January2025), §1.1, especially Remark1.1.
3. P. Quittner, [*Optimal Liouville theorems for superlinear parabolic problems*](https://arxiv.org/abs/2003.13223v2), v2(30September2020), Theorem1 and §1.2.
4. S. Gustafson and D. Roxanas, [*Global, decaying solutions of a focusing energy-critical heat equation in $`\mathbb R^4`$*](https://arxiv.org/abs/1707.07644v1), v1(24July2017), equation(1.1) and Theorem1.1.
5. M. Ikeda and K. Taniguchi, [*Global well-posedness, dissipation and blow up for semilinear heat equations in energy spaces associated with self-adjoint operators*](https://arxiv.org/abs/1902.01016v3), v3(26September2019), equation(1.1) and Theorem2.2.
6. G. Y. Diebou and N. C. Phuc, [*Optimal global well-posedness for semilinear heat equations*](https://arxiv.org/html/2610.27365v1), v1(19October2026), Theorem1.1.
7. Y. Naito, [*Existence of infinitely many singular self-similar solutions for the semilinear heat equation*](https://arxiv.org/abs/2609.36821v1), v1(29September2026), Theorem1.1 and(1.4)–(1.7).

## Status review


**Known cases:** The target allows sign changes and asks energy-norm decay of every global energy-subcritical solution. Critical infinite-time blowup, bounded-domain finite-time blowup rates and sign/radial restricted decay have different hypotheses.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target allows sign changes and asks energy-norm decay of every global energy-subcritical solution. Critical infinite-time blowup, bounded-domain finite-time blowup rates and sign/radial restricted decay have different hypotheses.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked against the selected original and later primary statements on24October2026. No matching resolution was located in bounded published/announced-result searches. The all-status repository comparisons are recorded separately. Prove2Me indexed searching found no observed match; a direct live-site request timed out, so live mission coverage remains a gap. The independent source/current and repository checks are recorded in the research ledger; they do not certify every proof in the cited literature.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-feac7347a94ee8a6**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
