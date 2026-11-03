# 1000. An invariant law for a stochastic compressible fluid with pure power pressure

**Area:** Stochastic fluid dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

On $`I=(0,1)`$, consider the Itô system
```math
\begin{aligned}
d\rho+(\rho u)_x\,dt&=0,\\
d(\rho u)+(\rho u^2+p(\rho))_x\,dt
&=u_{xx}\,dt+\rho\sum_{k\ge1}\sigma_k(x)\,dW_t^k,
\end{aligned}
```

with $`u(t,0)=u(t,1)=0`$ and total mass $`\int_0^1\rho\,dx=1`$.
The $`W^k`$ are independent standard real Brownian motions. Fix any deterministic noise coefficients satisfying
```math
\sigma_k\in H^2(I)\cap H^1_0(I),\qquad
\sum_{k\ge1}\|\partial_{xx}\sigma_k\|_{L^2(I)}^2<\infty.
```

Use the strong-solution phase space
```math
\mathcal X=\left\{(\rho,u)\in H^1(I)\times H^1_0(I):
\rho(x)>0\text{ for every }x\in[0,1],\quad\int_0^1\rho\,dx=1\right\},
```

with its $`L^2(I)\times L^2(I)`$ metric and Borel sigma-algebra. Positivity refers to the continuous representative of $`\rho`$; no single lower bound is imposed on every state in $`\mathcal X`$.

For every fixed $`\gamma>1`$, set $`p(\rho)=\rho^\gamma`$. Does the strong-solution Markov semigroup possess an invariant Borel probability measure $`\mu`$ on $`\mathcal X`$, satisfying
```math
\int_{\mathcal X}P_t\varphi\,d\mu=\int_{\mathcal X}\varphi\,d\mu
\quad(t\ge0)
```

for every bounded Borel test function $`\varphi`$? No uniqueness assertion is included.

## Application

This would provide a stationary statistical state for a randomly forced viscous compressible gas with a standard nonlinear pressure law.

## References

1. M. Coti Zelati, N. Glatt-Holtz and K. Trivisa, [*Invariant Measures for the Stochastic One-Dimensional Compressible Navier-Stokes Equations*](https://doi.org/10.1007/s00245-019-09594-x), *Applied Mathematics & Optimization* **83** (2021), 1487-1522. Sections 1, 1.1 and 2, especially the noise assumption (2.1); [preprint](https://arxiv.org/abs/1802.04000).
2. G.-Q. G. Chen, M. Coti Zelati and C. C. Yeung, [*Vanishing Mach Number Limit of Stochastic Compressible Flows*](https://arxiv.org/abs/2311.14660), v1 (2023), Introduction, main results and Section 5.
3. D. Donatelli, L. Pescatore and S. Spirito, [*Invariant measures for the one-dimensional stochastic Navier-Stokes-Korteweg equations*](https://arxiv.org/abs/2606.07423), v2 (26 October 2026), Remark 1.2 and Sections 1.1 and 2.3. This is a comparison model with capillarity.

## Status review


**Known cases:** Pure power pressure near vacuum and the interval strong phase space are essential. The October 26 Korteweg revision assumes capillarity; the original linear-near-zero construction and vanishing-Mach finite-time results do not provide this invariant law.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Pure power pressure near vacuum and the interval strong phase space are essential. The October 26 Korteweg revision assumes capillarity; the original linear-near-zero construction and vanishing-Mach finite-time results do not provide this invariant law.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Section 1.1 of the published source leaves pure power pressure unresolved. Its invariant-measure construction covers pressure linear near zero, including linear pressure itself; arbitrary polynomial growth at large density does not remove that small-density condition.

The 2023 vanishing-Mach work treats finite-time solutions for $`\gamma\ge1`$, but its invariant-measure result uses $`\gamma=1`$. The 2026 power-pressure existence theorem for Korteweg fluids has nonzero capillarity, periodic boundary conditions and damping. Stationary weak solutions on trajectory space also differ from an invariant law for this interval strong-solution semigroup. No matching complete or announced resolution was located in bounded current checks through the date above.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a0b296d0442ec9c0**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
