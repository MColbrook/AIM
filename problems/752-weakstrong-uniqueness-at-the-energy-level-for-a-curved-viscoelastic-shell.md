# 752. Weak–strong uniqueness at the energy level for a curved viscoelastic shell

**Area:** Fluid–structure interaction
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Use the periodic curved-reference setting of Breit–Mensah–Schwarzacher–Su. Let $`\Omega\subset\mathbb R^3`$ be a bounded smooth reference domain whose boundary has a smooth regular embedding $`\varphi:\omega=\mathbb T^2\to\partial\Omega`$. Write $`n`$ for the reference outer unit normal and choose a tubular radius $`L>0`$. A displacement $`\eta`$ gives the normal graph

```math
\varphi_\eta(t,y)=\varphi(y)+\eta(t,y)n(y),\qquad
\partial\Omega_\eta(t)=\varphi_\eta(t,\omega).
```

Restrict to the admissible normal-graph regime $`\|\eta\|_{L^\infty((0,T)\times\omega)}<L`$, so the Hanzawa map defines the moving domain. The reference surface is curved; the flat-plate result is already known. All structure functions and tests are periodic, with the source's convention for periodic function spaces.

Set all positive physical constants to one. The system is

```math
v_t+(v\cdot\nabla)v=\Delta v-\nabla\pi+f,
\qquad \nabla\cdot v=0\quad\text{in }\Omega_\eta(t),
```

```math
\eta_{tt}-\partial_t\Delta_y\eta+\Delta_y^2\eta
=g-n^T\tau\circ\varphi_\eta\,n_\eta
 |\partial_1\varphi_\eta\times\partial_2\varphi_\eta|,
\qquad v\circ\varphi_\eta=\eta_t n,
\qquad \tau=\nabla v+\nabla v^T-\pi I.
```

The classical stress formula describes smooth solutions; the following pressure-free identity defines the coupled equations for weak solutions. Put $`I=(0,T)`$. A weak solution has

```math
\eta\in W^{1,\infty}(I;L^2(\omega))
\cap W^{1,2}(I;H^1(\omega))\cap L^\infty(I;H^2(\omega)),
\qquad
v\in L^\infty(I;L^2(\Omega_\eta))\cap L^2(I;H^1_{\rm div}(\Omega_\eta)),
```

the stated kinematic trace, and initial values $`(\eta_0,\eta_*,v_0)`$. For every smooth scalar test $`b`$ and smooth ambient divergence-free vector test $`\phi`$, both vanishing at $`T`$ and satisfying $`\phi\circ\varphi_\eta=bn`$, require

```math
\begin{aligned}
&-\int_0^T\!\int_{\Omega_\eta(t)}v\cdot\phi_t
-\int_0^T\!\int_\omega\eta_t b_t
-\int_0^T\!\int_{\Omega_\eta(t)}v\otimes v:\nabla\phi
+\int_0^T\!\int_{\Omega_\eta(t)}\nabla v:\nabla\phi\\
&\quad+\int_0^T\!\int_\omega\nabla_y\eta_t\cdot\nabla_y b
+\int_0^T\!\int_\omega\Delta_y\eta\,\Delta_y b\\
&=\int_{\Omega_{\eta_0}}v_0\cdot\phi(0)
+\int_\omega\eta_*b(0)
+\int_0^T\!\int_{\Omega_\eta(t)}f\cdot\phi
+\int_0^T\!\int_\omega gb .
\end{aligned}
```

Require also, for almost every $`t`$, the physical energy inequality

```math
E(t)+\int_0^t\!\int_{\Omega_\eta(s)}|\nabla v|^2
+\int_0^t\!\int_\omega|\nabla_y\eta_t|^2
\le E(0)+\int_0^t\!\int_{\Omega_\eta(s)}f\cdot v
+\int_0^t\!\int_\omega g\eta_t,
```

where

```math
E(t)=\tfrac12\int_{\Omega_\eta(t)}|v|^2
+\tfrac12\int_\omega(|\eta_t|^2+|\Delta_y\eta|^2).
```

Fix compatible common data as in the source's (2.15) and (3.1): $`\eta_0\in H^3(\omega)`$, $`\eta_*\in H^1(\omega)`$, $`v_0\in H^1_{\rm div}(\Omega_{\eta_0})`$ with $`v_0\circ\varphi_{\eta_0}=\eta_*n`$, $`g\in L^2(I;L^2(\omega))`$, and an ambient force $`f\in L^\infty(I;L^2_{\rm loc}(\mathbb R^3))\cap L^2(I;H^1_{\rm loc}(\mathbb R^3))`$. Suppose a strong solution $`(\eta_s,v_s,\pi_s)`$ exists on this interval, with

```math
\begin{aligned}
\eta_s&\in W^{1,\infty}(I;H^1)\cap W^{1,2}(I;H^2)
\cap L^\infty(I;H^3)\cap W^{2,2}(I;L^2)\cap L^2(I;H^4),\\
v_s&\in W^{1,2}(I;L^2(\Omega_{\eta_s}))
\cap L^2(I;H^2(\Omega_{\eta_s}))\cap L^\infty(I;H^1(\Omega_{\eta_s})),\\
\pi_s&\in L^2(I;H^1(\Omega_{\eta_s})).
\end{aligned}
```

The spaces for $`\eta_s`$ are on $`\omega`$; the strong solution satisfies the equations almost everywhere and is itself a weak solution in the stated sense.

**Must every weak solution $`(\eta_w,v_w)`$ with these same data coincide with $`(\eta_s,v_s)`$ throughout their common admissible interval?** No additional assumption $`\eta_w\in L^\infty(I;C^{0,1}(\omega))`$ is made. Equality means $`\eta_w=\eta_s`$ and therefore equality of the fluid domains and of their velocities almost everywhere.

## Application

This asks whether the physical energy class selects the regular fluid–shell motion whenever such a motion exists.

## Status review


**Known cases:** The missing hypothesis is spatial Lipschitz regularity of a weak curved-reference shell. Strong-strong uniqueness for perfectly elastic shells, compressible relative-energy results with C1 weak geometry, and two-dimensional fluid/one-dimensional structure results do not remove it in this model.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The missing hypothesis is spatial Lipschitz regularity of a weak curved-reference shell. Strong-strong uniqueness for perfectly elastic shells, compressible relative-energy results with C1 weak geometry, and two-dimensional fluid/one-dimensional structure results do not remove it in this model.

Additional comparison sources: [comparison source 1](https://doi.org/10.2422/2036-2145.202407_010); [comparison source 2](https://journals.sns.it/index.php/annaliscienze/article/download/7110/2598/5226); [comparison source 3](https://doi.org/10.1137/21M1443509); [comparison source 4](https://arxiv.org/abs/2605.14357v1); [comparison source 5](https://doi.org/10.4171/IFB/549); [comparison source 6](https://arxiv.org/abs/2605.04314v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves the conclusion when the weak shell is uniformly Lipschitz in space. Its paragraph after Theorem 1.1 explicitly asks to remove that extra condition for curved reference geometry. The energy bound $`H^2(\mathbb T^2)`$ does not provide spatial Lipschitz continuity.

The known flat-plate theorem does not impose that condition, but its geometry is different. The 2026 perfectly elastic-shell paper proves uniqueness between strong solutions. A 2026 Oldroyd-B paper proves unconditional weak–strong uniqueness for a **two-dimensional fluid and one-dimensional shell**. A 2026 compressible-shell announcement still explicitly assumes $`\eta_w\in L^\infty C^1`$ in its relative-energy theorem. None of those statements covers the question above.

## References

1. D. Breit, P. R. Mensah, S. Schwarzacher and P. Su, *Ladyzhenskaya-Prodi-Serrin condition for fluid-structure interaction systems*, Annali della Scuola Normale Superiore di Pisa, Classe di Scienze, online 6 October 2025, 43-page final PDF, [DOI](https://doi.org/10.2422/2036-2145.202407_010). Explicit question p. 4; Definitions 2.5–2.6, pp. 11–12; Theorem 5.1, p. 34. [Publisher PDF](https://journals.sns.it/index.php/annaliscienze/article/download/7110/2598/5226).
2. S. Schwarzacher and M. Sroczinski, *Weak-Strong Uniqueness for an Elastic Plate Interacting with the Navier–Stokes Equation*, SIAM J. Math. Anal. 54 (2022), 4104–4138, [DOI](https://doi.org/10.1137/21M1443509).
3. D. Breit, P. R. Mensah, S. Schwarzacher and P. Su, *Well-posedness theorems in fluid-structure interaction: perfectly elastic shells*, [arXiv:2605.14357v1](https://arxiv.org/abs/2605.14357v1), Theorems 2.5–2.6 and §3.3.
4. P. R. Mensah, *Weak and strong solutions for polymeric fluid-structure interaction of Oldroyd-B type*, Interfaces Free Bound. 28 (2026), 399–445, [DOI](https://doi.org/10.4171/IFB/549), Theorem 2.6 and §6, especially pp. 437–438.
5. P. R. Mensah and P. M. Ngougoue Ngougoue, *Blow-Up Criteria and Weak–Strong Uniqueness for Compressible Fluid–Viscoelastic Shell Interactions*, [arXiv:2605.04314v1](https://arxiv.org/abs/2605.04314v1), actual HTML manuscript dated 24 August 2026, equations (1.1) and Theorem 5.1.

Current literature and complete-announcement searches found no resolution of this exact question. The independent selected-primary audit passed. All 186 cached catalogue pages were checked with six target aliases, with no matches; this was a listing-description comparison, not a review of every mission proof.

[Owner review](../FURTHER_problems/_tracking/parallel/continuum/curved-shell-weak-strong-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-curved-shell-weak-strong-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/continuum/curved-shell-duplicate-query-receipt.json), [catalogue receipt](../FURTHER_problems/_tracking/parallel/continuum/curved-shell-prove2me0132-review.json) and [coordinator review](../FURTHER_problems/_tracking/curved-shell-coordinator-selected-review-2026-10-17.json) record the exact scope and limitations.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-dcc2e415d8c9da90**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
