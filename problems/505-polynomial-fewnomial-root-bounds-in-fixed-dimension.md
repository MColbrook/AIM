# 505. Polynomial fewnomial root bounds in fixed dimension

**Area:** Numerical analysis; approximation and complexity
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`n\geq2`$. For real polynomials $`f_1,\ldots,f_n`$ in $`n`$ variables, let
```math
A=\bigcup_{i=1}^n\mathrm{supp}(f_i)\subset\mathbb N_0^n,
\qquad t=|A|,
```

and count the nondegenerate positive solutions by
```math
N_+(f)=\#\{x\in(0,\infty)^n:
 f_1(x)=\cdots=f_n(x)=0,\ \det Df(x)\ne0\}.
```


Do constants $`C_n,d_n>0`$ exist such that
```math
N_+(f)\le C_n t^{d_n}
```

for every such system? The constants may depend only on $`n`$. Degrees, coefficients and exponent vectors are unrestricted. The count is unsigned and excludes degenerate roots; it does not count algebraic multiplicities or complex roots.

This is Question 1.1 of Bürgisser–Ergür–Tonelli-Cueto [1]. Allowing integer Laurent exponents gives an equivalent question: multiplying each equation by a monomial preserves positive roots and Jacobian nondegeneracy there. The univariate case already has a linear bound from Descartes' rule.

## Application

Sparse polynomial systems describe positive steady states of chemical reaction networks and occur in nonlinear root finding. A bound depending on the number of terms, rather than degrees, would measure an important aspect of their complexity [2,3].

## References

1. P. Bürgisser, A. A. Ergür and J. Tonelli-Cueto, *On the Number of Real Zeros of Random Fewnomials*, SIAM Journal on Applied Algebra and Geometry **3**(4) (2019), [doi:10.1137/18M1228682](https://doi.org/10.1137/18M1228682). [Author preprint, v4](https://arxiv.org/abs/1811.09425v4), Question 1.1 and Theorem 1.2.
2. A. A. Ergür, M. L. Telek and J. Tonelli-Cueto, *On the Number of Real Zeros of Random Sparse Polynomial Systems*, [arXiv:2306.06784v3](https://arxiv.org/abs/2306.06784v3), introduction and Theorem 1.1.
3. B. El-Hilany and S. Tavenas, *Improved fewnomial upper bounds from Wronskians and dessins d'enfant*, [arXiv:2409.01651](https://arxiv.org/abs/2409.01651), introduction.
4. F. Bihan, *Descartes' rule of signs for arbitrary fewnomial systems*, [arXiv:2610.06435v2](https://arxiv.org/abs/2610.06435v2), Theorem A and Section 8.
5. F. Bihan, *Topological degree of fewnomial maps*, [arXiv:2610.29808v1](https://arxiv.org/abs/2610.29808v1), Theorem D and its discussion.

## Status review

Checked **30 October 2026**. The latest version of [2] explicitly retains the general question, including its bivariate case. Its polynomial expectation bound and that of [1] concern random Gaussian coefficients. Result [3] treats a trinomial paired with a $`t`$-nomial. These leave the stated worst-case question open.

The October 2026 results were checked specifically. Reference [4] gives recursive bounds using signs and hyperplane chambers; no uniform polynomial bound in $`t`$ for fixed $`n`$ is asserted. The polynomial bound in [5] controls absolute topological degree, a signed root count. Its discussion explicitly distinguishes this from the unsigned positive count. Neither supplies a full resolution of the target above.

Current resolution and announcement searches found no matching full solution. Semantic checks against the AIM list, all-status public solution records and the developing FURTHER_problems collection found no duplicate. The detailed review and search record are [retained here](../FURTHER_problems/_tracking/ROOT-FINAL-polynomial-fewnomial-fixed-dimension-admission-20261030.json).


### Online recheck, 2026-10-30

The October Descartes recursion and topological-degree bounds do not yield a worst-case polynomial bound for the unsigned number of nondegenerate positive roots at fixed dimension. Random-coefficient expectations and the disproved product bound are different targets.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2610.06435); [status source 2](https://arxiv.org/abs/2610.29808); [status source 3](https://arxiv.org/abs/2306.06784). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-ec58af82e6441b04** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
