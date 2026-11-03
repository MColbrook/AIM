# 699. Does positive Favard length force positive analytic capacity?

**Area:** Complex analysis and geometric measure theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`E\subset\mathbb C`$ be compact. For $`0\le\theta<\pi`$, let $`P_\theta`$ be orthogonal projection onto the line $`\{re^{i\theta}:r\in\mathbb R\}`$. Define its Favard length by
```math
\mathrm{Fav}(E)=\int_0^\pi \mathcal H^1(P_\theta(E))\,d\theta.
```

Define its analytic capacity by
```math
\gamma(E)=
\sup\left\{
\left|\lim_{z\to\infty}z\bigl(f(z)-f(\infty)\bigr)\right|:
f\text{ is holomorphic on }\mathbb C\setminus E,\quad |f|\le1
\right\}.
```

The limit $`f(\infty)`$ exists for such bounded functions.

Prove or disprove that every compact planar set satisfies
```math
\mathrm{Fav}(E)>0\quad\Longrightarrow\quad\gamma(E)>0.
```


No length, rectifiability or regularity assumption is imposed on $`E`$. The target is this qualitative implication; a uniform lower estimate $`\gamma(E)\ge c\,\mathrm{Fav}(E)`$ is a stronger, separate question.

## Application

A compact set has zero analytic capacity precisely when it is removable for bounded holomorphic functions: for every open $`\Omega\supset E`$, every bounded holomorphic function on $`\Omega\setminus E`$ extends holomorphically to $`\Omega`$. The question asks whether positive average projection length always detects failure of removability. It connects a geometric quantity visible in planar projections with analytic continuation and approximation.

## References

1. A. Chang and X. Tolsa, [*Analytic capacity and projections*](https://doi.org/10.4171/JEMS/1004), *Journal of the European Mathematical Society* **22** (2020), 4121–4159. Introduction; [arXiv:1712.00594v2](https://arxiv.org/abs/1712.00594v2), pp. 1–3, definitions (1.1)–(1.2), the explicit open implication on p. 2, and Theorem 1.1.
2. X. Tolsa, [*Interactions between Quantitative Rectifiability, Singular Integrals, and Boundary Value Problems for Harmonic Functions*](https://doi.org/10.1137/25M1804054), *Proceedings of the International Congress of Mathematicians 2026, Volume 2: Plenary Lectures*, 313–340. Question 5.5 and Theorems 5.6–5.8; [author version](https://arxiv.org/html/2607.16457v2#S5).
3. A. Chang, D. Dąbrowski and G. Del Nin, [*Favard length of non-homogeneous random disc-like Cantor sets*](https://arxiv.org/abs/2609.33557), preprint (2026), §1.5, equation (1.14), Theorem 1.14 and Corollaries 1.15–1.16.

## Status review


**Known cases:** The September random-Cantor paper and ICM survey retain the arbitrary compact-set implication. Counterexamples with zero Favard length and positive analytic capacity concern the converse. Sigma-finite length and extra projection-density hypotheses are absent here.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The September random-Cantor paper and ICM survey retain the arbitrary compact-set implication. Counterexamples with zero Favard length and positive analytic capacity concern the converse. Sigma-finite length and extra projection-density hypotheses are absent here.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

This is the remaining direction of Vitushkin's original equivalence. Counterexamples to the opposite implication have positive analytic capacity and zero Favard length; they do not answer the question above.

The pre-2022 source [1] explicitly states this implication as open and proves a positive result under an additional averaged $`L^2`$ projection-density assumption. Its discussion also explains why positive Favard length alone is weaker than that hypothesis.

The implication is known for sets of $`\sigma`$-finite $`\mathcal H^1`$ measure [3]. Tolsa's 2026 survey [2] retains exactly the arbitrary-compact-set question as Question 5.5. Its results for sets with plenty of big projections and for Ahlfors regular sets require additional geometric hypotheses. The September 2026 paper [3] again states the general implication as open while establishing it almost surely for its particular random Cantor models. Its examples disproving the converse have the opposite signs from a counterexample to the present target.

Current searches found no matching later theorem, counterexample, announced solution or repository duplicate. Selected primary statements and hypotheses were read; the cited proofs were not fully audited. The [FavardLength announcement](https://github.com/CoolRmal/FavardLength) concerns decay exponents of four-corner Cantor approximants, a different target; its Lean development was not independently built here. The current OpenAI manuscript catalogue and constituent abstracts contain no matching description under the recorded queries; not all linked PDFs were read.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-7c22fa2893111528**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
