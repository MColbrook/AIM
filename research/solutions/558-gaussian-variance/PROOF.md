# Increasing alpha can decrease optimized Gaussian marginal variances

**Target:** Problem 558 at `aa776a01d7d48a79f93251af11fde9454b0aea95`; [unchanged statement](statement.md).

**Status:** Solution claimed — complete counterexample, awaiting independent review.

**Prepared:** 2026-10-02 by OpenAI Codex. The proof, exact-arithmetic check and self-review are by the same AI agent; no independent or human review is claimed.

## Counterexample

Set $`d=3`$, $`\mu=0`$, and

```math
Q=\begin{pmatrix}1&4/5&4/5\\4/5&1&3/10\\4/5&3/10&1\end{pmatrix},
\qquad P=\frac{Q^{-1}+9I}{10},\qquad \Sigma=P^{-1}.
```

The leading principal minors of $`Q`$ are $`1,9/25,7/500`$, so $`Q`$ and $`P`$ are positive definite. Explicitly the admissible non-diagonal target covariance is

```math
\Sigma=\begin{pmatrix}
295/583&200/583&200/583\\
200/583&33910/42559&-6900/42559\\
200/583&-6900/42559&33910/42559
\end{pmatrix}.
```

We prove that the unique optimal covariance satisfies

```math
\Psi(10)=I,\qquad
\frac{d}{d\alpha}\bigl(\Psi_{11},\Psi_{22},\Psi_{33}\bigr)(10)
=\left(\frac{3392}{260905},-\frac{91}{521810},-\frac{91}{521810}\right).
```

Consequently, for every sufficiently small $`\varepsilon>0`$, choosing $`\alpha_1=10`$ and $`\alpha_2=10+\varepsilon`$ violates both the second and third coordinate inequalities in problem 558. A derivative with a rigorously negative sign suffices to produce actual ordered parameter pairs; no numerical finite-difference inference is used.

## Stationarity and differentiability

Write the diagonal precision as $`T=\mathrm{diag}(t_1,t_2,t_3)`$ and set

```math
M=\alpha P-(\alpha-1)T,\qquad V=M^{-1}.
```

The target's Gaussian minimization is equivalent to minimizing

```math
f_\alpha(t)=-\log\det M-(\alpha-1)\sum_i\log t_i
```

on $`t_i>0,M\succ0`$. Its stationarity equations are

```math
V_{ii}=\frac1{t_i}\qquad(i=1,2,3).
```

Indeed, $`\partial f_\alpha/\partial t_i=(\alpha-1)(V_{ii}-1/t_i)`$. The Jacobian of the parenthesized vector with respect to $`t`$ is

```math
\mathrm{diag}(t_i^{-2})+(\alpha-1)(V\circ V),
```

where $`\circ`$ denotes entrywise product. This is positive definite: the first summand is positive definite and the second is positive semidefinite by the Schur product theorem. Thus the objective is strictly convex. At $`\alpha=10,T=I`$ we have $`M=Q^{-1}`$ and $`V=Q`$, whose diagonal is one. This is a feasible stationary point and hence the unique global minimizer.

The stationarity map is smooth on its open feasibility domain. Its positive-definite Jacobian is invertible, so the implicit function theorem supplies a smooth feasible stationary branch near $`\alpha=10`$. Strict convexity makes every point on this branch the unique global minimizer at its corresponding parameter. Therefore differentiating this branch computes the derivative of the separately optimized covariances requested by the problem.

## Exact differentiation

Here $`P`$ is fixed as $`\alpha`$ varies. Differentiating $`V=M^{-1}`$ and the stationarity equations gives

```math
\left[\mathrm{diag}(t_i^{-2})+(\alpha-1)(V\circ V)\right]t'
=\mathrm{diag}\bigl(V(P-T)V\bigr).
```

At the constructed point, $`P-I=(Q^{-1}-I)/10`$. Put $`R=Q\circ Q`$ and $`\mathbf1=(1,1,1)^T`$. Since $`Q`$ is symmetric with unit diagonal,

```math
(I+9R)t'=\frac{\mathbf1-R\mathbf1}{10},\qquad
R=\begin{pmatrix}1&16/25&16/25\\16/25&1&9/100\\16/25&9/100&1\end{pmatrix}.
```

The solution is exactly

```math
t'=\left(-\frac{3392}{260905},\frac{91}{521810},\frac{91}{521810}\right)^T.
```

For example, by symmetry write $`t'=(a,b,b)^T`$. The first two equations reduce to

```math
10a+\frac{288}{25}b=-\frac{16}{125},\qquad
\frac{144}{25}a+\frac{1081}{100}b=-\frac{73}{1000}.
```

Substitution gives the displayed rational solution, and positive definiteness proves uniqueness. Finally $`\Psi_{ii}=1/t_i`$ and $`t_i=1`$ at alpha ten, so $`\Psi_{ii}'=-t_i'`$ there. The two negative derivatives prove the counterexample.

## Validation and audit

Run the dependency-free exact-arithmetic certificate:

```sh
python3 research/solutions/558-gaussian-variance/verify.py
```

It checks the positive principal minors, the explicit target covariance, stationarity, the differentiated linear system and the strict negative covariance derivatives using rational arithmetic. The analytic dependencies are Gaussian integration as in the target's objective reduction, the Schur product theorem, strict convexity and the finite-dimensional implicit function theorem. The certificate checks the finite algebra; the argument above proves why that algebra disproves the full assertion.

In the self-review, the target covariance was held fixed when differentiating; precision and covariance derivative signs were distinguished; feasibility and global, rather than merely local, optimality were verified. The example does not rely on degeneracy: $`Q`$, $`P`$, $`\Sigma`$ and $`M`$ are strictly positive definite. Some target correlations are negative, which is allowed. The conclusion claimed is failure of the universal coordinatewise variance ordering, not failure of existence or uniqueness of the optimizer.

## Source

C. C. Margossian, L. Pillaud-Vivien and L. K. Saul, [Variational Inference for Uncertainty Quantification: an Analysis of Trade-offs](https://www.jmlr.org/papers/v26/24-0878.html), JMLR 26 (2025), Remark 12; the [author manuscript](https://arxiv.org/html/2403.13748v5) retains the alpha-above-one ordering conjecture. The exact target here is the repository's coordinatewise formulation at the pinned revision. Independent review of this resolution is outstanding.
