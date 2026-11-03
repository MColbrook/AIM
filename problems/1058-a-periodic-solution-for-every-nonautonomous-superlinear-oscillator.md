# 1058. A periodic solution for every nonautonomous superlinear oscillator

**Area:** Nonlinear waves, fluids and kinetic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`T>0`$. Let $`f:\mathbb R^2\to\mathbb R`$ and $`p:\mathbb R^3\to\mathbb R`$ be $`T`$-periodic in their first variable and satisfy the Carathéodory conditions: measurability in time, continuity in the state variables for almost every time, and an integrable bound on each compact state set over one period. Assume local uniqueness for every Cauchy problem of

```math
x''+f(t,x)+p(t,x,x')=0.
```

Suppose that

```math
\lim_{|x|\to\infty}\frac{f(t,x)}x=+\infty
\quad\text{uniformly for }t\in[0,T],
\qquad
|p(t,x,v)|<\gamma(t)+C|x|\quad\text{for every }(t,x,v),
```

where $`C>0`$ and $`\gamma>0`$ is $`T`$-periodic and integrable over one period. The perturbation may depend on velocity, but its bound is uniform over all velocities. The displayed pointwise bounds use representatives satisfying Gidoni's (A3)–(A4).

Must there be a real $`T`$-periodic solution $`x\in W^{2,1}_{\mathrm{loc}}(\mathbb R)`$ satisfying the equation almost everywhere? Use its $`C^1`$ representative; both $`x`$ and $`x'`$ must match after one period. Constants and solutions whose least period divides $`T`$ count. No global-flow, trapping, equilibrium-at-zero, or additional continuation hypothesis is imposed.

## Application

This is a periodically forced nonlinear oscillator with a strongly restoring force. The question asks whether some periodic response must survive even when other trajectories may escape in finite time.

## References

1. P. Gidoni, [*Existence of a periodic solution for superlinear second order ODEs*](https://arxiv.org/abs/2108.13722), arXiv:2108.13722v1 (2021), Sections 2–3, assumptions (A1)–(A4), Corollary 5 and Remark 3. Published in *Journal of Differential Equations* **345** (2023), 401–417, [doi:10.1016/j.jde.2022.11.054](https://doi.org/10.1016/j.jde.2022.11.054).
2. S. Wang, F. Chen and D. Qian, [*The existence of periodic solution for superlinear second order ODEs by a new fixed point approach*](https://doi.org/10.1016/j.jde.2024.07.031), *Journal of Differential Equations* **410** (2024), 481–512, Theorem 1.1 and assumption (A3′).
3. S. Wang, F. F. Chen and C. Liu, [*The existence of periodic solutions for nonconservative superlinear second order ODEs: a rotation number and spiral analysis approach*](https://doi.org/10.3934/era.2025003), *Electronic Research Archive* **33** (2025), 50–67, Theorem 1.1 and (H2).
4. A. Cagnetta and P. Gidoni, [*Existence of a periodic solution for superquadratic Hamiltonian systems with possible finite-time blow-up*](https://arxiv.org/abs/2604.22707), arXiv:2604.22707v1 (2026), Theorem 3.1 and assumption (A3).

## Status review


**Known cases:** No continuation/reference-curve premise is allowed. The April 2026 Hamiltonian theorem imposes additional structural/rotation conditions; earlier periodic-solution criteria do not show they hold automatically for every allowed oscillator.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

No continuation/reference-curve premise is allowed. The April 2026 Hamiltonian theorem imposes additional structural/rotation conditions; earlier periodic-solution criteria do not show they hold automatically for every allowed oscillator.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 26 October 2026. Gidoni explicitly asks whether the reference-curve continuation condition (A5*) always follows from (A1)–(A4); Corollary 5 makes that equivalent to the existence question above. This entry concerns the general perturbed equation and makes no separate openness claim for the Hamiltonian subclass $`p=0`$.

The 2024 and 2025 existence theorems retain a bounded-set continuation condition. The 2026 planar theorem also retains an origin-crossing continuation assumption. These conditional results do not establish the displayed universal claim. Bounded current searches and all-status AIM/FURTHER/OpenAI comparisons located no complete resolution or duplicate.

The exact primary formulation and selected later theorem hypotheses were independently checked. Full 2023 publication/preprint parity and the complete 2024 article body remain access limits; the precise 2021 primary statement was available. Complete proofs of the cited results were not audited.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b5b48d85f5c3bf5b**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
