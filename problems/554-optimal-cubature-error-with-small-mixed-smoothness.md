# 554. Optimal cubature error with small mixed smoothness

**Area:** Numerical integration and approximation theory
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`d\ge3`$ and real parameters
```math
1<\theta<p<\infty,\qquad \frac1p<s<\frac1\theta.
```

Let $`F^s_{p,\theta}(\mathbb R^d)`$ be the Triebel–Lizorkin space of dominating mixed smoothness. To fix a norm, choose an even real $`\eta\in C_c^\infty(\mathbb R)`$ with $`\eta=1`$ on $`[-1,1]`$ and $`\eta=0`$ outside $`[-2,2]`$, put $`\eta_0=\eta`$ and
```math
\eta_j(\xi)=\eta(2^{-j}\xi)-\eta(2^{-(j-1)}\xi)\quad(j\ge1),\qquad
\Delta_{\boldsymbol j}f=\mathcal F^{-1}\!\left[\left(\prod_{k=1}^d\eta_{j_k}(\xi_k)\right)\widehat f(\boldsymbol\xi)\right],
```

and use the norm
```math
\|f\|_{F^s_{p,\theta}}=
\left\|\left(\sum_{\boldsymbol j\in\mathbb N_0^d}
2^{s\theta|\boldsymbol j|_1}|\Delta_{\boldsymbol j}f|^\theta\right)^{1/\theta}\right\|_{L_p(\mathbb R^d)}.
```

Here $`|\boldsymbol j|_1=\sum_kj_k`$, $`\mathbb N_0=\{0,1,\ldots\}`$, and $`\widehat f(\xi)=\int f(x)e^{-2\pi i x\cdot\xi}\,dx`$ in the distributional sense when needed. Other admissible dyadic cutoffs give equivalent norms. Let
```math
\mathcal B=\{f\in F^s_{p,\theta}(\mathbb R^d):\mathrm{supp}f\subset[0,1]^d,\ \|f\|_{F^s_{p,\theta}}\le1\}.
```

The strict inequality $`s>1/p`$ supplies continuous representatives, so point evaluations are defined. Functions may be complex-valued.

For each integer $`n\ge2`$, define the optimal deterministic cubature error
```math
e_n=\inf_{x_1,\ldots,x_n\in[0,1]^d}\ \inf_{\lambda_1,\ldots,\lambda_n\in\mathbb R}
\sup_{f\in\mathcal B}\left|\int_{[0,1]^d}f(x)\,dx-\sum_{i=1}^n\lambda_i f(x_i)\right|.
```

The nodes and weights are fixed before receiving the function values; weights may be signed. **Does there always exist $`c=c(d,p,\theta,s,\eta)>0`$ such that**
```math
e_n\ge c\,n^{-s}(\log n)^{(d-1)(1-s)}\qquad(n\ge2)?
```


A matching upper bound is known from Frolov cubature. The general lower bound currently quoted in the source has the smaller logarithmic exponent $`(d-1)(1-1/\theta)`$. The question is the missing minimax lower bound over all cubature formulas, including formulas unrelated to lattices. The two-dimensional case is outside this formulation. In the Sobolev subcase $`\theta=2`$, it includes every $`p>2`$ and $`1/p<s<1/2`$. The critical endpoint $`s=1/\theta`$ is excluded here.

## Application

This asks how many function evaluations are needed to integrate a multivariate function whose mixed derivatives have limited regularity. A sharp lower bound would determine whether a better arrangement of nodes and signed weights can improve the known logarithmic loss, and whether Frolov's construction is optimal in this regime.

## References

1. M. Ullrich and T. Ullrich, [The role of Frolov's cubature formula for functions with bounded mixed derivative](https://arxiv.org/abs/1503.08846), arXiv:1503.08846v2, especially equation(1.1), Theorem1.2 and the surrounding conjecture on p3, Definitions4.2–4.3/Remarks4.5–4.6 on pp11–12, supported class(4.2) on p13, and Theorem7.3/Remark7.4 on pp20–21. Related publication: [SIAM Journal on Numerical Analysis54(2)(2016),969–993](https://doi.org/10.1137/15M1014814).
2. V. Temlyakov and T. Ullrich, [Bounds on Kolmogorov widths and sampling recovery for classes with small mixed smoothness](https://arxiv.org/abs/2012.09925), arXiv:2012.09925v1, §5, pp16–21, especially the different integration and sampling bounds; related publication [Journal of Complexity67(2021),101575](https://doi.org/10.1016/j.jco.2021.101575).
3. B. Käßemodel and T. Ullrich, [Quantum integration in Besov spaces with mixed smoothness](https://arxiv.org/html/2610.17204v1), arXiv:2610.17204v1,12October2026, introduction. It explicitly retains an unresolved part of the classical small-smoothness optimality question; its quantum Besov-space estimates use a different model.

## Status review

Reviewed18October2026. The latest listed arXiv revision of [1] is v2,6April2016; the currently served PDF is internally dated1March2022. Its exact definitions and conjecture were read, and no historical PDF-body parity is asserted. The final25-page journal body has not been compared with this23-page preprint; the official publisher abstract also states that small-smoothness optimality is open. The12October2026 primary comparison [3] retains that distinction.

The inspected2021 sampling bounds do not improve the Frolov integration upper bound. Theorem2 of Bazarkhanov (2020), printed108, gives one-sided upper bounds of this form; its following remark loosely calls the two-dimensional Fibonacci rule optimal, without a new unrestricted lower theorem. To avoid treating that disputed wording as an open case, the entire two-dimensional case is held outside the proposed problem. This does not provide a matching lower bound in dimensions $`d\ge3`$. Known sharp errors for the particular Fibonacci formula alone do not establish a lower bound for all formulas. Bounds for Besov classes, randomized algorithms, quantum queries, or sparse grids with restricted nodes do not by themselves settle this deterministic Triebel–Lizorkin minimax question.

Current searches and semantic comparisons with all AIM statuses found no matching complete solution or equivalent existing entry. AIM536 concerns infinitely many prefixes of one infinite sequence and star discrepancy; it is a different target. The cached Prove2Me comparison validated all186 listing pages and allsix target aliases, with zero returned contexts. This is a description-level comparison, not a review of every mission proof. An independent selected formulation audit passed. The [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/continuum/cross-frolov-small-smoothness-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/frolov-small-smoothness-prove2-0172-review.json) and [coordinator review](../FURTHER_problems/_tracking/frolov-small-smoothness-coordinator-review-2026-10-18.json) passed at their recorded extents. These checks retain the dimensional restriction and source-version limits; they do not certify every referenced proof.

Additional comparisons: D. B. Bazarkhanov, [Optimal numerical integration on classes of smooth functions of several variables](https://math.kz/media/journal/journal2021-01-1925456.pdf), *Kazakh Mathematical Journal*20(3)(2020),101–110, Theorem2 and Remark4; D. Krieg and J. Vybíral, [New Lower Bounds for the Integration of Periodic Functions](https://doi.org/10.1007/s00041-023-10021-7), *Journal of Fourier Analysis and Applications*29(2023),41, §4.2; D. Krieg and M. Ullrich, [Approximation of functions: Optimal sampling and complexity](https://doi.org/10.1017/S0962492925100287), *Acta Numerica*35(2026),273–457, compared at selected [preliminary-version](https://arxiv.org/abs/2602.02066v2) passages. Their inspected results do not settle the stated dimensions-three-and-higher lower bound.


### Online recheck, 2026-10-30

Searches retain the small-mixed-smoothness lower-bound gap. Frolov upper bounds, two-dimensional optimality, quantum Besov integration and particular-rule estimates do not settle unrestricted deterministic cubature in dimensions >=3.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1503.08846); [status source 2](https://arxiv.org/abs/2012.09925); [status source 3](https://arxiv.org/abs/2610.17204). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-8600775c7f3b8a37** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
