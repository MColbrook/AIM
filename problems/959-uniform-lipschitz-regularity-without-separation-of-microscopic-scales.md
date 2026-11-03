# 959. Uniform Lipschitz regularity without separation of microscopic scales

**Area:** PDEs and materials
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix integers $`d\ge2`$ and $`n\ge1`$. Let
```math
A:\mathbb R^d\times(\mathbb R^d)^n\longrightarrow\mathbb R^{d\times d}
```

satisfy the source's conditions (1.4)–(1.6): for some $`\Lambda\in(0,1]`$, $`L>0`$, and $`\gamma\in(0,1]`$,
```math
\Lambda|\xi|^2\le \xi\cdot A(x,y_1,\ldots,y_n)\xi
 \le\Lambda^{-1}|\xi|^2,
```

$`A`$ is one-periodic in each microscopic vector $`y_i`$, and
```math
|A(x,y)-A(x',y')|
 \le L\left(|x-x'|+\sum_{i=1}^n|y_i-y_i'|\right)^\gamma.
```

For arbitrary $`\varepsilon=(\varepsilon_1,\ldots,\varepsilon_n)\in(0,1]^n`$, put
```math
A_\varepsilon(x)=A(x,x/\varepsilon_1,\ldots,x/\varepsilon_n).
```

Let $`B_r`$ denote the ball of radius $`r`$ about the origin. Suppose $`u_\varepsilon\in H^1(B_1)`$ solves
```math
-\mathrm{div}(A_\varepsilon\nabla u_\varepsilon)=0
\quad\text{weakly in }B_1.
```


Does the endpoint $`\alpha=1`$ of the source's estimate (1.8) hold? Namely, is there a finite constant $`C`$, independent of all scale parameters and of the solution, such that
```math
|u_\varepsilon(x)-u_\varepsilon(y)|
 \le C|x-y|\,\|u_\varepsilon\|_{L^2(B_1)}
\qquad(x,y\in B_{1/2})?
```


No relation, separation, rationality or Diophantine condition is imposed on the scale ratios. The coefficient and its fixed regularity and ellipticity data may enter the constant. The pointwise estimate is for a continuous representative of the weak solution. This is an interior Lipschitz estimate; a finite-$`p`$ gradient bound is a weaker conclusion.

## Application

The coefficient describes diffusion in a material with several interacting microscopic structures. A scale-uniform gradient bound would control local concentration of fields even when neighboring microscopic lengths become comparable or nearly resonant.

## Known progress

The source proves the displayed estimate for every fixed $`\alpha<1`$, and proves the Lipschitz endpoint for a variable-separated laminate structure. It also reviews well-separated and special reperiodizable scale configurations.

For coefficients without the slow $`x`$ variable, Niu and Zhuge's later work proves uniform Calderón–Zygmund estimates for every finite $`p`$, without separation, and some mesoscopic Lipschitz estimates. Niu, Xu and Zhuge's 2026 work obtains the full interior Lipschitz estimate for real-analytic coefficients under a double-logarithmic separation condition. Its introduction and Theorem 1.2 explicitly leave complete removal of that condition open.

The 2026 extension to infinitely many scales retains a scale-separation condition in its Lipschitz theorem. None of these results establishes the unrestricted endpoint above.

## Status review


**Known cases:** The endpoint requires a scale-independent microscopic Lipschitz estimate with no separation at all. Current finite-p bounds, mesoscopic estimates, double-log separation and infinitely-many-scale theorems do not give that endpoint.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The endpoint requires a scale-independent microscopic Lipschitz estimate with no separation at all. Current finite-p bounds, mesoscopic estimates, double-log separation and infinitely-many-scale theorems do not give that endpoint.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The eligible assumptions, estimate (1.8), Section 1.4 question and laminate theorem were read, together with the actual latest finite-$`p`$, double-logarithmic and infinite-scale main statements. Official version histories and the author's current publication list were checked. Primary-source searches for full proofs, counterexamples and announcements, including bounded Prove2Me searches, found no matching unrestricted resolution on 24 October 2026.

Catalogue comparisons distinguish this deterministic multiscale regularity problem from stochastic Bourgain–Spencer approximation, local approximation widths for arbitrary rough elliptic operators, elastic G-closure, conductivity bounds, and boundary diffusion kernel estimates. This is a statement-level status review, not a verification of each cited proof.

## References

1. W. Niu and J. Zhuge, [Compactness and stable regularity in multiscale homogenization](https://arxiv.org/abs/2112.02400), Theorems 1.1–1.2 and Section 1.4; [published article](https://doi.org/10.1007/s00208-022-02378-9), *Mathematische Annalen* (2023).
2. W. Niu and J. Zhuge, [Uniform Calderón–Zygmund estimates in multiscale elliptic homogenization](https://arxiv.org/abs/2405.15149), latest v2 (28 January 2026), introduction and Theorem 1.1.
3. W. Niu, Y. Xu and J. Zhuge, [Optimal convergence rates in multiscale elliptic homogenization](https://arxiv.org/abs/2509.09410), introduction and Theorem 1.2; *Communications on Pure and Applied Mathematics* **79** (2026), 2158–2222, [DOI](https://doi.org/10.1002/cpa.70047).
4. Z. Shen, Y. Xu and J. Zhuge, [Quantitative homogenization of elliptic equations with infinitely many scales](https://arxiv.org/abs/2605.02561), v1 (4 May 2026), Theorem 1.5 and Remark 1.7.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e971f49470a88189**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
