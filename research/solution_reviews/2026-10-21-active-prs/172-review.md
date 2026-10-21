# Independent review of PR #172: partial resolution of AIM 541

**Date:** 21 October 2026
**Reviewer:** independent Codex AI reviewer, separate from the authoring process
**Reviewed head:** 71ed609ac0d213f399348e2bf6669767b8444ca0
**Submission:** Kaiwen Jin, *Linear failure and cubic convergence for surface evolution with relaxed minimal deformation*
**Decision:** **Partially resolved: degree-one failure and degree-three convergence are accepted.** The quadratic case remains open.

This is an independent analytical review, not a formal proof or a human referee report. The decision combines complementary independent Codex reviews: the present reviewer reconstructed Section 6 and checked the linear construction, algebra, initial forcing and final nonconvergence deduction; a second reviewer independently reconstructed the common analytic interval and its operator estimates in Sections 2–5. Their verification scopes are distinguished below.

## Sources and scope

The reviewed [manuscript source](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex) and [27-page PDF](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.pdf) agree in their theorem and equation locators. The complete source, original problem statement, target comparison and AI-use statement were examined. All 27 PDF pages were rendered and inspected on contact sheets; pages 4, 12, 16, 18, 19, 20, 24, 25, 26 and 27 were additionally inspected individually for readable theorems and critical formulas, with a separate individual check of page 21. Every declared payload byte count and SHA-256 hash matched, and all seven package files matched their raw Git blobs at the pinned head. No LaTeX rebuild was performed.

The manuscript contains two separate results:

- **Theorem 2.2:** a degree-one counterexample on a fixed torus with a tangential rigid rotation and an admissible alternating mesh family. Its essential additional requirement is a mesh-independent nondegenerate existence interval.
- **Theorem 6.1:** degree-three convergence for every mesh family and smooth exact solution allowed by AIM 541, including full-time unique solvability and nondegenerate elements. Its lifted map bound is $`C_T h^3\sqrt{1+|\log h|}`$.

Both concern the original position-gradient RMD equations, exact integration on the fixed initial mesh and raw geometric current normals. Neither substitutes a projected-normal or velocity-gradient MDR method. Degree two is expressly left unresolved in Remark 6.2. All source line links below refer to the exact pinned revision.

## Literature and attribution check

The primary reference is G. Gao, B. Li and R. Tang, *Convergent finite element approximations of surface evolution with relaxed minimal deformation*, **Numerische Mathematik 158** (2026), 671–714, [DOI](https://doi.org/10.1007/s00211-026-01529-3), [author manuscript](https://libuyang.com/NM-15.pdf). Its Theorem 2.1 proves convergence for $`k\ge4`$. Equations (2.1)–(2.2) match the original mesh assumptions and numerical method. Section 7, author-manuscript page 26, explicitly identifies $`k=1,2,3`$ as challenging unresolved cases, with the degree restriction used in (4.20), (4.26) and (4.27). The [institutional publication record](https://research.polyu.edu.hk/en/publications/convergent-finite-element-approximations-of-surface-evolution-wit/) confirms the published restriction.

An earlier [2024 AIMS abstract by Buyang Li](https://aimsconference.org/AIMS-Conference/conf-reg2024/ts/detail1.php?abs_no=14), *Convergent finite element approximations of surface evolution with artificial tangential motion*, announces convergence for $`k\ge3`$ using harmonic-map tangential motion. This earlier announcement is relevant to originality. It supplies neither the precise scheme nor a proof, and the later full RMD manuscript explicitly leaves cubic convergence open. It therefore does not establish a prior proved cubic solution of AIM 541.

T. Huang, B. Li and R. Tang, [*A convergent finite element method with minimal deformation rate for mean curvature flow*](https://arxiv.org/abs/2602.14405), [primary text](https://arxiv.org/html/2602.14405v1), studies a different fully discrete MDR method with a velocity-gradient equation and projected normal. It does not establish this RMD cubic case. Quan Zhao's [2026 constrained Onsager framework](https://arxiv.org/abs/2608.07244) also concerns a different relaxed-MDR curvature-flow formulation and energy law.

Checks of the [Buyang Li](https://libuyang.com/) and [Rong Tang](https://ronglotus.github.io/) author pages, together with exact-title and subject searches for subsequent low-degree RMD results, found no matching prior proved resolution of the full question or either new theorem. This records the search outcome, rather than proving absence.

The manuscript's other reference, Terence Tao's [Fourier-transform lecture notes, Theorem 43](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/), supplies Plancherel's identity for the logarithmic inequality. It is not a reference for the new linear analytic estimates.

## Independent reconstruction of the cubic proof

Section 6 was independently reconstructed through the auxiliary estimates, geometric boundary terms, nonlinear bookkeeping, coupled bootstrap and ODE continuation. No unresolved central estimate or mismatch with the original hypotheses remains in this part of the review. This verification is sufficient to accept Theorem 6.1 as mathematical partial progress.

Write $`e=X_h-Y=z+\mathcal T^*\psi`$, where $`Y`$ is the nodal interpolant of the lifted exact map, $`\mathcal T v=\Pi_h(m\cdot v)`$, $`m`$ is the known smooth exact normal and $`z\in\ker\mathcal T`$. Use

```math
E=\|e\|_2,\qquad F=\|\psi\|_2,\qquad Z=\|z\|_2,\qquad
D=\|\nabla z\|_2,\qquad \ell=1+|\log h|.
```

### Geometry, superapproximation and weak tangency

[Source lines 1635–1776](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex#L1635), PDF pages 20–22.

The original $`W^{3,\infty}`$ parametrization bounds and cubic degree of $`F_K`$ give uniformly bounded fourth derivatives of a fixed smooth ambient function composed with $`F_K`$. Nodal interpolation has value error $`O(h^4)`$ and differential error $`O(h^3)`$. Applying this argument to initial signed distance gives initial distance $`O(h^4)`$ and normal error $`O(h^3)`$. Closest-point metric and area errors are $`O(h^4)`$, consistent with a displacement contribution $`O(h^4)`$ and squared normal-slope contribution $`O(h^6)`$.

Adjacent elements share their polynomial edge tangent. Their normal accuracy makes the sum of outward conormals $`O(h^3)`$. This controls the jumps of known smooth coefficient fluxes in later elementwise integrations by parts. The inverse estimates have the correct surface-dimension powers: $`h^{-1}`$ from $`L^2`$ to $`L^\infty`$, $`h^{-1}`$ for one $`L^2`$ derivative, $`h^{-2}`$ for an $`L^\infty`$ derivative and $`h^{-1/2}`$ for a summed edge trace.

Smooth-product superapproximation gives

```math
\|bw-I_h(bw)\|_2+h\|\nabla(bw-I_h(bw))\|_2
\le Ch^2\|w\|_{H^1}.
```

For a unit field $`b`$, mass orthogonality yields the exact Schur identity

```math
(\mathcal S_b\chi,\chi)_h
=\|\chi\|_2^2-\|(I-\Pi_h^3)(b\chi)\|_2^2,\qquad
\mathcal S_b=\mathcal T_b\mathcal T_b^*.
```

Thus $`\mathcal S_m\ge1-Ch^2`$, the weak normal decomposition is uniformly conditioned, and $`E^2\asymp Z^2+F^2`$. Differentiating the known normal and Schur inverse gives bounded $`Q_t`$, without differentiating the unknown numerical normal.

Since $`\Pi_h(m\cdot z)=0`$, superapproximation and an inverse estimate imply

```math
\|m\cdot z\|_2\le Ch^2(D+Z),\qquad
\|\nabla(m\cdot z)\|_2\le Ch(D+Z).
```

Expanding $`a_h(z,m\chi)`$ and integrating its middle term elementwise gives

```math
|a_h(z,\mathcal T^*\chi)|\le C(D+Z)\|\chi\|_2.
```

Its edge contribution is $`O(h^2)\|\chi\|_2Z`$: an $`O(h^3)`$ flux jump times two $`h^{-1/2}`$ inverse traces. Adjoint testing gives $`\|QL_h\mathcal T^*\psi\|_2\le Ch^{-1}F`$, and Young's inequality gives $`a_h(e,z)\ge\tfrac12D^2-CE^2`$.

### Discrete logarithmic estimate

[Source lines 1778–1798](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex#L1778), PDF page 22.

A local polynomial evaluation dual has $`L^1`$ norm $`O(1)`$ and $`L^2`$ norm $`O(h^{-1})`$. After pullback into a fixed smooth chart, splitting its Fourier $`H^{-1}`$ norm at frequency $`h^{-1}`$ bounds the low-frequency integral by $`O(\ell)`$ and, by Plancherel, the high-frequency integral by $`Ch^2\|\delta_h\|_2^2=O(1)`$. Duality and uniform chart bounds give

```math
\|z\|_\infty\le C\sqrt\ell(D+Z).
```

The logarithm follows from dimension two; the argument does not assume a false $`H^1`$-to-$`L^\infty`$ embedding.

### Actual mixed system and residual

[Source lines 1800–1925](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex#L1800), PDF pages 22–23.

On the bootstrap interval $`E\le h^{11/4}`$, set

```math
\rho=C_1(h^3+h^{-2}E),\qquad \alpha=h+\rho.
```

Then $`\rho=O(h^{3/4})`$, $`\alpha^2=O(h^{3/2})`$, and $`\alpha^2\le h`$ for small $`h`$. The first variation of the normal, weak leakage and inverse estimates give

```math
\|N-m\|_\infty\le C\rho,\qquad
\|N-m\|_2\le C(h^{-1}F+E+\alpha D+h^3).
```

The Schur identity remains valid for the discontinuous actual normal:

```math
\mathcal S_N\ge[1-(Ch+C\rho)^2]I,\qquad
\|Q_N-Q\|_{2\to2}\le C\rho.
```

The lifted smooth weak equation and interpolation give defect bounds $`Ch^3`$ in the discrete $`H^{-1}`$ norm, $`Ch^2`$ in the force $`L^2`$ norm and $`Ch^3`$ for the normal-constraint defect. Exact saddle elimination gives

```math
\|\mu\|_2\le C(h^{-2}F+\alpha h^{-1}D+E+h^2),
```

```math
\|e_t\|_2\le C(h^{-1}D+\alpha h^{-2}F+E+h^2).
```

The improved normal coefficient in the second bound uses the projection before estimating the normal stiffness. For $`q=(v_h-u(X_h))\cdot N`$, the scheme gives only $`\Pi_hq=0`$. Applying the projection defect to its FE velocity part and comparing its smooth reference-tangent part gives

```math
\|q\|_2\le C(h^{-1}F+\alpha h^{-1}D+E+\alpha h^2).
```

The additional intermediate term $`\alpha^2h^{-2}F`$ is absorbed using $`\alpha^2\le h`$. No pointwise zero-residual assumption is made.

### Relative volume and the area-weighted test

[Source lines 1927–2030](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex#L1927), PDF pages 24–25.

The signed-distance weighted interior difference

```math
\mathcal B=\int(\mathbf1_{\Omega_h}-\mathbf1_\Omega)d\,dx
```

is nonnegative and comparable to $`\|f\|_2^2`$, where $`f=d(X_h,t)`$, on a close normal graph. Treating components separately avoids cancellation for nested components. For the closed piecewise-smooth numerical boundary, common moving-edge traces cancel side fluxes in the transport formula. There is no free boundary term or numerical-normal derivative.

The volume transport term is bounded by $`C\mathcal B`$, because $`d_t+u\cdot\nabla d=O(d)`$. With $`J`$ the current area ratio from the fixed initial mesh, the weak constraint gives exactly

```math
\mathcal B'\le C\mathcal B+(q,(I-\Pi_h)(fJ))_h.
```

Keeping $`J`$ is essential because the constraint uses the fixed reference measure.

Let $`j`$ be the smooth exact-flow area ratio. Taylor expansion gives $`f=m\cdot e+\mathcal R_f`$, with $`\|\mathcal R_f\|_2\le C(h^4+h^{-1}E^2)`$ and $`\|f\|_\infty\le C(h^4+h^{-1}E)`$. Write $`e=z+m\psi+r`$, where $`\|r\|_{H^1}\le CF`$. At the exact differential, the area derivative annihilates $`m\otimes\nabla\psi`$. Its other linear terms cost $`C(D+E)`$ and its quadratic remainder costs $`C\rho(D+h^{-1}F)`$. Thus

```math
\|J-j\|_2\le C\{h^3+D+E+\rho(D+h^{-1}F)\}.
```

Combining the smooth $`jf`$ projection defect with $`f(J-j)`$, while retaining $`h^{-1}E^2`$ until using $`E/h\le Ch\rho`$, gives

```math
\|(I-\Pi_h)(fJ)\|_2
\le C\{hF+h\alpha(D+E)+h^4\}.
```

The same decomposition gives

```math
F^2\le C\mathcal B+Ch^2E^2+Ch^{-2}E^4+Ch^8.
```

Pairing the residual and projection-defect bounds, including all source terms, yields

```math
\mathcal B'\le C\mathcal B+C\alpha^2(D^2+E^2)+Ch^6.
```

No term of order one multiplying the tangent-gradient energy is omitted.

### Tangent energy and nonlinear powers

[Source lines 2032–2130](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex#L2032), PDF pages 25–26.

Testing the error equation by $`z`$ gives tangent coercivity and a bounded $`Q_t`$ term. The linear normal variation is integrated by parts with known smooth coefficients; their $`O(h^3)`$ conormal jumps and inverse traces leave edge terms bounded by $`CE^2`$.

For the nonlinear normal variation, write the normalized perturbed differential in a reference tangent frame as $`\mathsf V A+\nu b^{\mathsf T}`$. After subtracting the first variation, the tangential remainder is $`O(|A-I||b|+|b|^3)`$ and the normal remainder is $`O(|b|^2)`$. Tangential projection removes $`m\nabla\psi`$ up to the known $`O(h^3)`$ reference-normal error. Weak tangency controls the normal remainder pairing. The decisive small quantity is $`\rho^2/h=O(h^{1/2})\to0`$.

The multiplier contribution is bounded by

```math
C\sqrt\ell\,(h^{-2}F+\alpha h^{-1}D+E+h^2)
(h^{-1}F+E+\alpha D+h^3)(D+E).
```

Its critical term is $`\sqrt\ell\,h^{-3}F^2(D+E)`$. Young's inequality leaves $`\ell h^{-6}F^4`$ and an arbitrarily small fraction of $`D^2`$. The remaining products have the listed positive coefficient powers $`h^{3/4},h^{3/2},h^{5/2},h^{9/4},h^{11/4},h,h^{11/4},h^2`$ under $`F\le CE`$, $`D\le Ch^{-1}E`$ and $`E\le h^{11/4}`$. They stay small after multiplication by $`\sqrt\ell`$. The final pure source is $`Ch^{10}\ell`$, smaller than $`Ch^6`$. Thus

```math
(Z^2)'+cD^2\le CE^2+Ch^6+C\ell h^{-6}F^4.
```

The fourth power is correctly retained as the weak normal error $`F^4`$, rather than the whole map error $`E^4`$.

### Closure and continuation of the actual solution

[Source lines 2132–2217](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex#L2132), PDF pages 26–27.

Initially $`e=0`$ and $`\mathcal B(0)=O(h^8)`$. Under the second bootstrap $`\mathcal B\le Mh^6`$, with $`M`$ fixed before $`h`$, the shape-normal estimate gives $`F^2\le C(M+1)h^6`$. Tangent energy then gives

```math
\sup_{s\le t}E(s)^2+\int_0^tD(s)^2\,ds
\le C_{M,T}h^6\ell.
```

Inserting this into the bulk estimate costs only $`C_{M,T}h^{15/2}\ell`$ beyond its $`C_Th^6`$ source. The latter constant is independent of $`M`$. Choosing $`M`$ first and $`h`$ afterwards strictly improves both bootstraps.

The improved error gives $`W^{1,\infty}`$ closeness $`O(h\sqrt\ell)\to0`$. Local graph charts and the exact embedding's uniform differential lower bound preserve local injectivity and element rank. Compactness and uniform value closeness preserve separation of nonlocal parameter pairs. For fixed $`h`$, the Schur lower bound, bounded nodal positions and positive element differentials keep the trajectory inside a compact safe part of the smooth ODE domain. Local existence continues to $`T`$; uniqueness includes velocity and multiplier.

The original closest-point lift and $`O(h^4)`$ interpolation error give

```math
\sup_{0\le t\le T}\|X_h^\ell(t)-X(t)\|_{L^2(\Gamma^0)}
\le C_Th^3\sqrt{1+|\log h|}.
```

The bulk estimate also gives the $`O(h^3)`$ signed-distance bound. Shape and map errors remain distinguished throughout.

## Linear theorem: complementary verification and scope

The present reviewer checked that the torus and ambient rotation meet the smooth-data assumptions and make the continuous identity map stationary. The alternating spacings are fixed multiples of the mesh width, limiting tangent directions are independent, flat $`P_1`$ parametrizations meet the original bounds, and the explicit closest projection supports admissibility. Periodicity introduces no boundary.

The local full-system weak-normal rank argument gives a smooth mixed ODE whose uniqueness justifies the cyclic representation. The relative-velocity equation, multiplier split, ordered Schur elimination and weak-connection identities were checked algebraically. The label normalization and orthogonality identity are consistent, including extension through $`F=0`$.

An independent exact-integral $`P_1`$ assembly of the original cyclic saddle system corroborated the initial optical forcing. For $`n=8,16,32,64,128`$, the row $`L^2`$ difference between the normalized optical normal rate and $`-\cos\theta/6`$ was respectively $`0.0445214,0.0108134,0.00268887,0.000671408,0.000167803`$. Constraint residuals were at roundoff level. This supports the sign and coefficient; it does not by itself prove persistence beyond a fast initial layer.

The present reviewer checked the final label modulus, fixed-time label growth, edge-gradient lower bound, exact rotation-work identity and conversion to a uniform $`L^2`$ map-error lower bound conditional on Proposition 4.1's common interval. This first pass did not personally certify all four dependencies below. They were addressed by the separate second independent Codex review dated 21 October 2026:

- [Lines 437–591 and 646–735](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex#L437), PDF pages 6–10: curved projection/graph types, moment tables and coefficient-difference orders through global inverses.
- [Lemma 3.1, lines 737–768](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex#L737), PDF page 10: the lower bound for all divided frozen symbols, including zero phase.
- [Lemma 4.2, lines 941–1016](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex#L941), PDF pages 12–13: the same-radius covariant-jet and tame half-weight comparisons for nonlocal kernels.
- [Lines 1106–1304](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex#L1106), PDF pages 14–16: the mesh-uniform common-jet energy estimate, including the extra $`N\overline M^{-1}`$ application to macro commutator forces, the stiff fast commutator in the high metric and time insertions involving $`\Gamma_t`$.

The second review reconstructed these dependencies and found no concrete gap. It checked inverse conditioning before exponential localization, the state/dual scaling, variable-coefficient moment and adjoint formulas, and the row-supported optical-test cancellation. It recovered the divided principal-block gap from the exact frozen $`P_1`$ gradient and a fixed-window localization error $`C/L+CL\delta`$.

For the same-radius comparison, that reviewer reconstructed the modular identity $`\lambda_{k+l}-\lambda_k=e^{iks}\lambda_l`$, transported coefficient algebra, ordered interaction ODE and gain of one coefficient derivative. For common-jet energy, it checked low-band absorption of the third-order-looking coupling, high-band coercivity in the original physical metric, the retained high-mass cross term, finite-offset treatment of stiff commutators, cutoff factors, time-derivative counts and the half-weight estimate balancing one lost derivative against a decreasing analytic radius. The closed geometry/velocity bootstrap gives a fixed positive time and lower radius, followed by continuation of the original full ODE.

That separate reconstruction, combined with the present reviewer's initial-forcing check and final label/energy argument, supports acceptance of Theorem 2.2. This report does not attribute the second reviewer's common-interval reconstruction to the first reviewer.

A minor wording issue remains: the blanket exponential-kernel assertion in lines 384–385 does not cover general smooth strictly supported spectral cutoffs in lines 1078–1082. Those cutoffs have the sufficiently summable polynomial distance moments used subsequently. This wording does not invalidate the estimates or either theorem.

## Recorded mathematical status

The accepted original cases, attributed to **Kaiwen Jin**, are:

- **$`k=1`$:** Theorem 2.2 gives an admissible counterexample with a mesh-independent nondegenerate existence interval and a fixed positive lower bound for uniform lifted $`L^2`$ map error. Acceptance combines the two complementary independent reviews described above.
- **$`k=3`$:** Theorem 6.1 gives the quantitative $`h^3\sqrt{1+|\log h|}`$ map estimate, full-time unique solvability and nondegeneracy. Its proof was independently reconstructed in the present review.

These results support **Partially resolved** status for AIM 541. The original **$`k=2`$** case remains open; the manuscript claims neither a quadratic counterexample nor quadratic convergence. The accepted partial results do not constitute a complete solution of the three-degree question, a formal proof or human specialist verification.
