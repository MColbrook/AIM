# 007. Pólya–Szegő conjecture for the first buckling load

**Area:** Elastic stability

**Status:** 🏆 LEAN VERIFIED

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

**Resolution update (3 November 2026):** Affirmative proof by Quanyu Tang and Haiqi Zhang, with the formal theorem recorded as **Lean verified** on the basis of [Palomar's version 1 registration](https://palomar-registry.org/entry?id=PALOMAR-2026-10-18-000008&version=1) and an AIM statement-and-assumption review. The declaration `BucklingChallenge.polya_szego_buckling` proves the equal-area disk comparison for every planar open set of finite positive area, using the buckling Rayleigh quotient on the closure of smooth compactly supported functions in the full second-order Sobolev graph. It imposes no sign condition on the eigenfunction and includes the bounded smooth-domain target above.

[Manuscript](https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar/blob/3b3417486b092363b411ed25ee2edb5e6f87f0ed/manuscript/PS_dim2_v5.pdf) · [Registered formal proof](https://github.com/QuanyuTang/polya-szego-planar-unconditional-palomar/blob/5311f47821b5da92e81e75b7da5091d176c8deb9/PlanarBucklingSolution.lean) · [Lean verification record and statement comparison](../research/solution_reviews/2026-11-03-lean-007/README.md).

Palomar's successful report is tied to the registered source hashes and records acceptance by Lean, NanoDa and con-ron with only `propext`, `Classical.choice` and `Quot.sound` permitted. AIM reviewed the concrete definitions, hypotheses, proof bridges and recorded checks; it relies on Palomar for kernel replay. This designation concerns the formal theorem, without claiming human peer review or a line-by-line verification of the working manuscript. The [earlier announcement-only review](../research/solution-status-audit-2026-11-03/lane-a/007.json) is retained as history and is superseded by this verification record.

### Earlier status record


**Literature check:** Open in cited literature; no later resolution located.

Antunes explicitly states the conjecture without a ground-state sign assumption. The 2025 numerical study says that only partial buckling results are established. The clamped-plate vibration theorem concerns a different denominator and cannot be substituted for this buckling statement.

**Search audit:** “buckling ball conjecture first eigenvalue 2025 2026”; “Pólya Szegő buckling conjecture solved”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
