# 007. Pólya–Szegő conjecture for the first buckling load

**Area:** Elastic stability

**Status:** ✅ SOLVED

**Last checked:** 2026-11-03

## Problem statement

For every bounded smooth planar domain $`\Omega`$, define its first clamped buckling eigenvalue by

```math
\Lambda_1(\Omega)=\inf_{0\ne u\in H^2_0(\Omega)}\frac{\int_\Omega|\Delta u|^2\,dx}{\int_\Omega|\nabla u|^2\,dx}.
```

Thus $`\Delta^2u=-\Lambda\Delta u`$ with $`u=\partial_\nu u=0`$ on the boundary. If $`B`$ is a disk of the same area, prove or disprove $`\Lambda_1(\Omega)\ge\Lambda_1(B)`$. No sign condition is imposed on a first eigenfunction.

## Application

The eigenvalue is proportional to the compressive load at which a clamped plate buckles. The conjecture identifies the most easily buckled shape of prescribed area.

## References

1. P. R. S. Antunes, [On the buckling eigenvalue problem](https://doi.org/10.1088/1751-8113/44/21/215205), Journal of Physics A 44 (2011), 215205, §3.2.1.
2. A. Chakib, I. Khalil and A. Sadik, [On numerical resolution of shape optimization bi-Laplacian eigenvalue problems](https://doi.org/10.1016/j.matcom.2024.11.007), Mathematics and Computers in Simulation 230 (2025), 149–164, introduction.

3. Quanyu Tang and Haiqi Zhang, *Proof of the Planar Pólya–Szegő Buckling Conjecture*, working draft v5, 18 October 2026. [Manuscript PDF](https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar/blob/3b3417486b092363b411ed25ee2edb5e6f87f0ed/manuscript/PS_dim2_v5.pdf); [source](https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar/blob/3b3417486b092363b411ed25ee2edb5e6f87f0ed/manuscript/PS_dim2_v5.tex). [Palomar registration, version 1](https://palomar-registry.org/entry?id=PALOMAR-2026-10-18-000008&version=1).

## Status review

**Resolution update (3 November 2026):** Solved on the basis of an **unverified announcement**. The manuscript claims the sharp area inequality for every planar open set of finite positive area, using the same buckling Rayleigh quotient on H02, without a sign condition on the eigenfunction. Its Corollary 1.3 therefore includes the full bounded smooth-domain target.

[Claimed solution](https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar/blob/3b3417486b092363b411ed25ee2edb5e6f87f0ed/manuscript/PS_dim2_v5.pdf) · [Dated statement comparison](../research/solution-status-audit-2026-11-03/lane-a/007.json). Corollary 1.3; formal declaration BucklingChallenge.polya_szego_buckling. The full external proof has not been independently verified here; no local Lean kernel replay or human peer review is asserted. This label records the complete announcement under the requested status policy.

### Earlier status record


**Literature check:** Open in cited literature; no later resolution located.

Antunes explicitly states the conjecture without a ground-state sign assumption. The 2025 numerical study says that only partial buckling results are established. The clamped-plate vibration theorem concerns a different denominator and cannot be substituted for this buckling statement.

**Search audit:** “buckling ball conjecture first eigenvalue 2025 2026”; “Pólya Szegő buckling conjecture solved”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
