# 961. Jump-set concentration of multidimensional scalar entropy dissipation

**Area:** PDEs, fluids and materials
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\geq2`$, $`T>0`$, and $`f\in C^2(\mathbb R;\mathbb R^d)`$. Assume the flux is linearly nondegenerate:

```math
\mathcal L^1\{v\in\mathbb R:\tau+\xi\cdot f'(v)=0\}=0
\qquad\text{for every }(\tau,\xi)\ne(0,0).
```


Put $`\Omega=(0,T)\times\mathbb R^d`$. Consider any bounded distributional solution of

```math
\partial_tu+\mathrm{div}_x f(u)=0
\quad\text{in }\Omega
```


with finite entropy production: for every $`\eta\in C^2(\mathbb R)`$, the distribution
$`\mu_\eta=\partial_t\eta(u)+\mathrm{div}_x q_\eta(u)`$, where $`q'_\eta=\eta'f'`$, is a locally finite signed Radon measure. No entropy-sign inequality is required.

Use its signed kinetic measure $`m`$, normalized by bounded velocity support, so that

```math
\partial_t\chi(v;u)+f'(v)\cdot\nabla_x\chi(v;u)=\partial_vm,
\qquad
\chi(v;u)=\mathbf1_{\{0<v<u\}}-\mathbf1_{\{u<v<0\}}.
```


Here $`m`$ is locally finite and supported in $`\Omega\times[-M,M]`$ for some finite $`M`$ containing the range of $`u`$ and zero. This support condition fixes the kinetic measure uniquely. Define

```math
\nu(A)=|m|(A\times\mathbb R),
\qquad
J=\left\{z\in\Omega:
\limsup_{r\downarrow0}\frac{\nu(B_r(z))}{r^d}>0\right\}.
```


Must $`\nu(\Omega\setminus J)=0`$ hold for every such solution?

This is concentration on the density jump set $`J`$ itself. Its rectifiability is known; the question excludes a diffuse remainder. Dafermos poses the entropy-concentration question in §6.8, p.214, with this kinetic definition of $`J`$ in (6.8.8) [1]. The modern multidimensional formulation remains explicitly open in [2, p.3].

## Application

Entropy-production measures describe dissipative interfaces in weak conservation-law solutions, including nonclassical shocks. Concentration would localize the associated costs on interfaces in diffusive-dispersive approximations and variational or large-deviation limits [2, Introduction].

## References

1. C. M. Dafermos, [*Hyperbolic Conservation Laws in Continuum Physics*](https://doi.org/10.1007/978-3-662-49451-6), fourth edition, Springer, 2016, §6.8, pp.212–214, Definition6.8.1 and equations(6.8.6)–(6.8.8). [Institutional library record](https://ndl.ethernet.edu.et/handle/123456789/74708).
2. F. Ancona, E. Marconi and L. Talamini, [*On the structure of entropy dissipation and regularity for quasi-entropy solutions to 1d scalar conservation laws and to isentropic Euler system with gamma=3*](https://arxiv.org/abs/2601.03739), v1, 7January2026, Introduction, pp.1–3.
3. L. Silvestre, [*Oscillation properties of scalar conservation laws*](https://doi.org/10.1002/cpa.21804), Communications on Pure and Applied Mathematics **72** (2019), 1321–1348, Theorem1.3 and the following paragraph: concentration outside the closure of $`J`$ leaves the full question unresolved. [Author version](https://arxiv.org/abs/1708.03401).

## Status review


**Known cases:** The target is concentration on J itself in d>=2, for signed finite entropy production. The October counterexample concerns non-Lebesgue points in one dimension rather than diffuse entropy mass; concentration outside the closure of J is weaker.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is concentration on J itself in d>=2, for signed finite entropy production. The October counterexample concerns non-Lebesgue points in one dimension rather than diffuse entropy mass; concentration outside the closure of J is weaker.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [bounded source, status and duplicate audit](../FURTHER_problems/_tracking/parallel/continuum/dafermos-entropy-concentration-status-2026-10-22.json) checks the original pages, native formulas, the explicit January2026 open-status statement and later announcements through22October2026. The one-dimensional concentration theorem and the October2026 counterexample concerning non-Lebesgue points outside $`J`$ do not resolve this multidimensional target. The [2019 jump-set scope comparison](../FURTHER_problems/_tracking/parallel/continuum/dafermos-entropy-concentration-ghoshal-jana-scope-2026-10-22.json) separates nonclosedness of $`J`$ from concentration on $`J`$. No exact AIM/FURTHER duplicate was located; AIM156 instead concerns the two-dimensional eikonal equation. This is a statement-level literature assessment, not a complete proof audit.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f513a686aa226e18**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
