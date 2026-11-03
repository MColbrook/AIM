# 917. Split products for time-dependent form-sum Schrödinger evolution

**Area:** Operators, matrices and computation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathcal H`$ be a complex Hilbert space, $`T>0`$, and $`H_0\ge0`$ self-adjoint. Put $`Q=D(H_0^{1/2})`$, $`q_0[u]=\|H_0^{1/2}u\|^2`$. For each $`t\in[0,T]`$, let $`V(t)`$ be self-adjoint with associated closed Hermitian form $`q_{V(t)}`$ defined on a domain containing $`Q`$. Assume, uniformly in $`t`$,

```math
|q_{V(t)}[u]|\le a q_0[u]+b\|u\|^2,
\qquad u\in Q,\quad 0\le a<1,\quad b\in\mathbb R.
```

The restricted forms induce $`\widetilde V(t):Q\to Q^*`$. Require strong differentiability in $`t`$ and

```math
|\langle\widetilde V'(t)u,u\rangle|
\le a q_0[u]+b\|u\|^2.
```

Use one-sided derivatives at the endpoints. Suppose also $`q_t=q_0+q_{V(t)}\ge c\|\cdot\|^2`$ for a fixed $`c>0`$. Let $`H(t)=H_0\dotplus V(t)`$ be the form sum and $`U(t,s)`$ its unitary form-evolution propagator for $`i\partial_tu=H(t)u`$.

For fixed $`0\le s<t\le T`$, set $`h=(t-s)/n`$ and $`t_j=s+jh`$. Do both products

```math
P_n^R=F_{n-1}^R\cdots F_0^R,
\qquad F_j^R=(I+ihH_0)^{-1}(I+ihV(t_j))^{-1},
```

```math
P_n^E=F_{n-1}^E\cdots F_0^E,
\qquad F_j^E=e^{-ihH_0}e^{-ihV(t_j)},
```

converge strongly to $`U(t,s)`$? These are two separate limit questions. Later times occur on the left; the $`V`$ factor acts first in each step. No common operator core, identification with the algebraic operator sum, convergence rate, or uniform-in-time limit is assumed.

Both products are contractions. Thus the source's weak-operator version for $`P_n^R`$ is equivalent here: if $`P_n\to U`$ weakly and $`U`$ is unitary, then $`\|P_nx-Ux\|^2\le2\|x\|^2-2\mathrm{Re}\langle P_nx,Ux\rangle\to0`$.

## Application

Splitting separates simpler parts of a quantum Hamiltonian. These limits would justify that approximation when the forms share a domain but the domains of the full operators can change with time.

## References

1. P.-A. Vuillermot and W. F. Wreszinski, [*Product approximations for solutions to a class of evolution equations in Hilbert space*](https://ems.press/content/serial-article-files/44680), *Portugaliae Mathematica* **68** (2011), 317–343, [doi:10.4171/PM/1894](https://doi.org/10.4171/PM/1894). Conditions (V), (V′), and Remark (3), equations (32)–(33), pp. 323–325; standing positivity (7).
2. A. Bátkai, P. Csomós, B. Farkas and G. Nickel, [*Operator splitting for non-autonomous evolution equations*](https://arxiv.org/abs/1002.0164), arXiv:1002.0164v4; *Journal of Functional Analysis* **260** (2011), 2163–2190, [doi:10.1016/j.jfa.2010.10.008](https://doi.org/10.1016/j.jfa.2010.10.008). Assumption 2.1 and Theorem 2.2.
3. V. A. Zagrebnov, H. Neidhardt and T. Ichinose, *Trotter-Kato Product Formulæ* (2024), [Chapter 12](https://doi.org/10.1007/978-3-031-56720-9_12), Assumptions 12.1.1, and [Chapter 13](https://doi.org/10.1007/978-3-031-56720-9_13), Sections 13.1–13.3.
4. S. Becker, N. Galke, L. van Luijk and R. Salzmann, [*Convergence Rates for the Trotter Splitting for Unbounded Operators*](https://doi.org/10.1007/s10208-025-09730-w), published online 2025; *Foundations of Computational Mathematics* **26** (2026), 2471–2524, Theorem 3.6.

## Status review


**Known cases:** Existing nonautonomous splitting theorems require generation by an algebraic operator-sum closure or stronger domain/commutator control. Parabolic form-sum results and time-integrated autonomous unitary limits do not establish both pointwise-in-time products under only the displayed form assumptions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Existing nonautonomous splitting theorems require generation by an algebraic operator-sum closure or stronger domain/commutator control. Parabolic form-sum results and time-integrated autonomous unitary limits do not establish both pointwise-in-time products under only the displayed form assumptions.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 26 October 2026. The original article explicitly poses the split formulas as open. Its proved formulas use the full $`H(t)`$ in each step. Hilbert-space contractivity alone does not supply the additional dual-space stability used by that proof.

The 2011 evolution-semigroup theorem requires generation by the closure of an algebraic operator sum. The 2024 time-dependent framework uses parabolic evolution and fractional operator-domain estimates; its unitary discussion includes autonomous results and convergence integrated over time. The 2025 theorem has additional autonomous energy, core and commutator assumptions. These statements do not establish the displayed form-only, time-dependent limits.

Bounded searches of current literature and announcements, with all-status AIM/FURTHER/OpenAI comparisons, found no complete resolution or duplicate. Original hypotheses and the actual product order were independently read, and selected later theorem statements were compared. Full 2020 preprint/publication parity and complete proofs of the cited results were not audited.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-9eef288061af8163**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
