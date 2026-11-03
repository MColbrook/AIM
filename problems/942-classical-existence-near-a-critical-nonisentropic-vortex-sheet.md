# 942. Classical existence near a critical nonisentropic vortex sheet

**Area:** Compressible flow and free boundaries
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Consider two-dimensional compressible Euler flow with
```math
(\partial_t+\mathbf u\cdot\nabla)p+2p\,\nabla\cdot\mathbf u=0,
\qquad \rho(\partial_t+\mathbf u\cdot\nabla)\mathbf u+\nabla p=0,
\qquad(\partial_t+\mathbf u\cdot\nabla)s=0,
\qquad\rho=p^{1/2}e^{-s/2}.
```

Fix the planar states
```math
\bar U^+=(1,3/\sqrt2,0,2\log2),\qquad
\bar U^-=(1,-3/\sqrt2,0,-2\log2),
\quad U=(p,u_1,u_2,s).
```

Their sound speeds are $`c_+=2`$ and $`c_-=1`$. Thus the tangential velocity parameter is the critical value $`\bar v=(c_++c_-)/\sqrt2`$, lying strictly inside the supersonic stable region
```math
2\bar v>(c_+^{2/3}+c_-^{2/3})^{3/2}.
```


Is there an integer $`m\ge13`$ and a number $`\delta>0`$ with the following property? Every smooth initial graph $`\varphi_0`$ and smooth upper/lower initial states, expressed on the half-plane $`\mathbb R^2_+=\{(y_1,y_2):y_2>0\}`$, whose perturbations have compact support in the closed unit half-disk and satisfy
```math
\sum_{\pm}\|U_0^\pm-\bar U^\pm\|_{H^{m+1/2}(\mathbb R^2_+)}
+\|\varphi_0\|_{H^{m+1}(\mathbb R)}<\delta,
```

and the all-order compatibility conditions described below, admit a classical vortex-sheet solution on $`[0,1]`$?

Here a solution consists of a graph $`x_2=\varphi(t,x_1)`$, Euler solutions on its two sides, and orientation-preserving/reflected straightening maps $`x_2=\Phi^\pm(t,y_1,y_2)`$ with
```math
\Phi^\pm(t,y_1,0)=\varphi(t,y_1),\qquad
\pm\partial_{y_2}\Phi^\pm>0.
```

The pulled-back states $`U^\pm`$ and maps satisfy
```math
U^\pm-\bar U^\pm,\ \Phi^\pm\mp y_2\in
H^4((0,1)\times\mathbb R^2_+),\qquad
\varphi\in H^5((0,1)\times\mathbb R),
```

have the specified initial traces and positive pressure, and obey Euler on each side and the vortex-sheet conditions
```math
p^+=p^-,\qquad
\partial_t\varphi=\mathbf u^+\cdot(-\partial_1\varphi,1)
=\mathbf u^-\cdot(-\partial_1\varphi,1).
```

The straightening maps obey the usual eikonal gauge
$`\partial_t\Phi^\pm+u_1^\pm\partial_1\Phi^\pm-u_2^\pm=0`$.

Compatibility means the smooth version of Definition 4.1 of Morando–Trebeschi–Wang: there are smooth initial extensions $`\dot\Phi_0^\pm:=\Phi_0^\pm\mp y_2`$ of $`\varphi_0`$, supported in the closed half-disk of radius $`\sqrt2`$, satisfying
```math
\|\dot\Phi_0^\pm\|_{H^{m+3/2}(\mathbb R^2_+)}\le C_m\|\varphi_0\|_{H^{m+1}(\mathbb R)},\qquad
\pm\partial_2\Phi_0^\pm\ge7/8,
```

where $`C_m`$ is fixed independently of the data, such that the formal time derivatives determined recursively by pulled-back Euler and the eikonal equations satisfy the source's pressure and map matching conditions to every order. Explicitly, if $`\dot\Phi_k^\pm=\partial_t^k(\Phi^\pm\mp y_2)|_{t=0}`$ and $`\dot p_k^\pm=\partial_t^k(p^\pm-1)|_{t=0}`$ are these formal jets, require
```math
\partial_2^j(\dot\Phi_k^+-\dot\Phi_k^-)|_{y_2=0}=0,
\qquad
\partial_2^j(\dot p_k^+-\dot p_k^-)|_{y_2=0}=0
\quad(j,k\ge0).
```

For smooth compactly supported jets these all-order equalities also ensure the weighted Hardy integrability conditions in that definition. Perturbations supported away from the initial interface with $`\varphi_0=0`$ give nontrivial compatible data.


This is an existence-only prototype of the critical case explicitly left open in [1, Introduction] and [2, p. 572]. The specified initial traces include a choice of the controlled extensions in the compatibility condition. Their constant $`C_m`$ is fixed before the data are chosen. The graph has initial support in $`[-1,1]`$.

## Application

A vortex sheet separates two gas flows with continuous pressure and normal velocity, while tangential velocity and entropy can jump. The question tests whether a critical velocity inside the linearly stable region still permits a classical evolution for small compatible disturbances.

## References

1. A. Morando, P. Trebeschi and T. Wang, [*Two-Dimensional Vortex Sheets for the Nonisentropic Euler Equations: Nonlinear Stability*, latest arXiv v2](https://arxiv.org/abs/1808.09290v2), 31 October 2018, Theorem 1.1, the following critical-case discussion, and Section 4. Published in *Journal of Differential Equations* **266** (2019), 5397–5430, [DOI](https://doi.org/10.1016/j.jde.2018.10.029).
2. A. Morando, P. Trebeschi and T. Wang, *Existence and stability of nonisentropic compressible vortex sheets*, in [*Hyperbolic Problems: Theory, Numerics, Applications*, proceedings of HYP2018](https://www.aimsciences.org/aimsmath-upload/book/202172319108234.pdf), 2020, pp. 569–576, especially p. 572.
3. A. Morando, P. Secchi, P. Trebeschi and D. Zhang, [*Two-dimensional nonisentropic compressible vortex sheets*](https://doi.org/10.3934/dcdss.2025138), *Discrete and Continuous Dynamical Systems – S* **19** (2026), 157–197, Theorem 4.2(ii) and Remark 4.3.

## Status review


**Known cases:** The specified nonisentropic critical Euler background needs nonlinear classical existence. Current-vortex magnetic models and the 2026 constant-coefficient linear front result do not cover it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The specified nonisentropic critical Euler background needs nonlinear classical existence. Current-vortex magnetic models and the 2026 constant-coefficient linear front result do not cover it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The nonlinear theorem in [1] excludes the displayed critical value. Its input and compatibility conditions motivate this fixed-background prototype, which asks for an unspecified finite input regularity and only classical output. It does not prescribe the original theorem's exact derivative loss or ask for uniqueness or global stability.

The critical theorem in [3] treats a constant-coefficient linear front equation with prescribed forcing. It has an additional derivative loss and does not supply the variable-coefficient estimates or nonlinear existence required here. Remark 4.3 explicitly discusses a possible future nonlinear resolution.

The complete eight-page proceedings chapter and pinned 30-page original v2 were read for question discovery. The exact formulation, compatibility conditions and relevant 2026 theorems were separately inspected; an independent audit required and checked the initial extension bound now included above. The 34-page final journal body has not been compared throughout. No matching complete solution or announcement was located in the recorded bounded searches and semantic duplicate checks. These checks do not establish exhaustive absence of a solution or certify every cited proof.

The [source review](../FURTHER_problems/_tracking/parallel/continuum/critical-vortex-sheet-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-critical-vortex-sheet-review.json), [duplicate comparison](../FURTHER_problems/_tracking/critical-vortex-sheet-duplicates-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/critical-vortex-sheet-coordinator-review-2026-10-19.json) record the evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-49e34272a6a8d95e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
