# 945. Stochastic homogenization for ordered stable min-max Hamiltonians

**Area:** PDEs, fluids and materials
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix arbitrary integers $`d\ge1`$ and $`\ell\ge1`$. On a probability space $`(\Omega,\mathcal F,\mathbb P)`$ with a measure-preserving ergodic $`\mathbb R^d`$ -action $`(\tau_y)`$, let $`C_i,D_i:\mathbb R^d\times\mathbb R^d\times\Omega\to\mathbb R`$, $`1\le i\le\ell`$, be random Hamiltonians. In the momentum variable, $`C_i`$ has convex sublevel sets and $`D_i`$ has convex superlevel sets. Require the pointwise ordering
```math
C_1\ge\cdots\ge C_\ell,\qquad D_1\le\cdots\le D_\ell,
```

and define
```math
H_1=\max\{C_1,D_1\},\qquad
H_k=\max\{C_k,\min\{D_k,H_{k-1}\}\},\quad 2\le k\le\ell.
```

All these operations are pointwise in $`(p,x,\omega)`$.

For every branch $`G\in\{C_i,D_i:1\le i\le\ell\}`$ impose:

1. **Stationarity:** $`G(p,x,\tau_y\omega)=G(p,x+y,\omega)`$ for every $`p,x,y,\omega`$, using the common ergodic action.
2. **Printed branch coercivity:**
 ```math
\liminf_{|p|\to\infty}\mathrm*{ess\,inf}_{(x,\omega)\in\mathbb R^d\times\Omega}|G(p,x,\omega)|=+\infty.
```

3. **Continuity and bounds:** for every compact $`K\subset\mathbb R^d`$, $`G`$ is bounded on $`K\times\mathbb R^d\times\Omega`$. For each $`(\omega,K)`$, there exists a modulus $`\rho_{\omega,K}`$, shared by the finite family, such that
 ```math
|G(p,x,\omega)-G(q,y,\omega)|\le\rho_{\omega,K}(|p-q|+|x-y|),\quad p,q\in K,\ x,y\in\mathbb R^d.
```

4. **Stable pairing:** at each $`(x,\omega)`$, every pair $`(C_i,D_i)`$ and every adjacent pair $`(C_j,D_{j+1})`$, $`1\le j<\ell`$, is stable in the following sense. For quasiconvex $`V`$ and quasiconcave $`\Lambda`$, put $`\Delta=\{p:\Lambda(p)\ge V(p)\}`$. Stability means either $`\Delta=\varnothing`$, or there is a real $`c`$ with $`V=c`$ on $`\partial\Delta`$ and $`V>c`$ on $`\Delta^c`$.

Carry explicitly the ambient hypothesis from the discovery source's Section1.1: ** $`H_\ell`$ is positively coercive in momentum, uniformly in $`(x,\omega)`$ **. Equivalently,
```math
\lim_{R\to\infty}\inf_{\substack{|p|\ge R\\x\in\mathbb R^d,\ \omega\in\Omega}}H_\ell(p,x,\omega)=+\infty.
```

This ambient hypothesis is separately stated, not asserted to follow from the absolute-value branch condition.

Does every such $`H_\ell`$ stochastically homogenize? Precisely, does there exist a deterministic continuous $`\overline H_\ell:\mathbb R^d\to\mathbb R`$ such that, for every $`u_0\in\mathrm{BUC}(\mathbb R^d)`$, the viscosity solutions of
```math
\partial_tu^\epsilon+H_\ell(Du^\epsilon,x/\epsilon,\omega)=0,\qquad u^\epsilon(\cdot,0,\omega)=u_0,
```

converge almost surely, locally uniformly on $`\mathbb R^d\times(0,\infty)`$, to the viscosity solution of
```math
\partial_t\overline u+\overline H_\ell(D\overline u)=0,\qquad\overline u(\cdot,0)=u_0?
```

No contact-monotonicity hypothesis, rate, corrector-existence conclusion or explicit formula for $`\overline H_\ell`$ is included.

## Application

This asks whether fine stationary random heterogeneity produces deterministic large-scale front dynamics for this structured nonconvex Hamiltonian class.

## References

- H. Gao, *Stochastic homogenization of certain nonconvex Hamilton-Jacobi equations*, J. Differential Equations **267** (2019), 2918-2949, [DOI](https://doi.org/10.1016/j.jde.2019.03.036), [primary v1](https://arxiv.org/html/1803.08633v1), Section 1.1, equations (1.1)-(1.2), assumptions (A1)-(A4), Definition 1 and **Conjecture 1**.
- H. Gao, *Random homogenization of coercive Hamilton-Jacobi equations in 1d*, Calc. Var. Partial Differential Equations **55** (2016), article 30, [primary](https://arxiv.org/abs/1507.07048). Known one-dimensional case.
- A. Davini, R. Saona and B. Ziliotto, *Stochastic homogenization of HJ equations: a differential game approach*, [primary v2](https://arxiv.org/html/2406.18404v2), Theorem 2.2 and Remark 2.3. Its finite-range and oriented-dynamics assumptions differ.

## Status review


**Known cases:** Stable ordered pairings without contact monotonicity are the target. The finite-range oriented differential-game theorem and the one-dimensional theorem impose restrictions absent here. No general announcement found.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Stable ordered pairings without contact monotonicity are the target. The finite-range oriented differential-game theorem and the one-dimensional theorem impose restrictions absent here. No general announcement found.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Partial progress; checked 29 October 2026.** Gao proves the target with the additional contact-monotonicity condition (M); the one-dimensional case is also known. No matching full result, counterexample, announcement or AIM/private duplicate was located.

The ambient positive coercivity is explicit because absolute-value branch growth alone does not imply it. This carries the source's Section 1.1 hypothesis; it does not restrict the dimension or add (M). Final published-body parity was unavailable; the sole archived primary and published abstract were checked.

Review evidence: [owner](../FURTHER_problems/_tracking/B-180308633-Hamilton-Jacobi-exact-hypotheses-independent-peer-20261028/OWNER-PROPOSAL.json), [mathematical peer](../FURTHER_problems/_tracking/B-180308633-Hamilton-Jacobi-exact-hypotheses-independent-peer-20261028/PEER.json), [coordinating review](../FURTHER_problems/_tracking/B-180308633-Hamilton-Jacobi-exact-hypotheses-independent-peer-20261028/ROOT-EXACT-COERCIVE-STABLE-MINMAX-CURRENT-AND-SEMANTIC-FINAL-REVIEW.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6b522f12046bcadc**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
