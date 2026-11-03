# 937. Perron resolutivity for the porous medium equation on general spacetime sets

**Area:** PDEs, fluids and materials
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`n\ge2`$, an exponent $`m>1`$, a nonempty bounded open set $`\Theta\subset\mathbb R^n\times\mathbb R`$, and $`f\in C(\partial\Theta;[0,\infty))`$. Consider

```math
\partial_t h=\Delta(h^m).
```

Use the comparison-based definitions in Björn–Björn–Gianazza–Siljander, Definitions 3.1 and 6.1. A function $`u:\Theta\to[0,\infty]`$ is superparabolic if it is lower semicontinuous, finite on a dense subset, and obeys comparison with nonnegative continuous weak solutions on every spatial cylinder $`K=U\times(a,b)\Subset\Theta`$: $`h\le u`$ on $`\partial_pK`$ implies $`h\le u`$ in $`K`$. Here $`U`$ is bounded with $`C^{2,\alpha}`$ boundary, $`0<\alpha<1`$, and $`h`$ is continuous on $`\overline K`$ and

```math
\partial_p K=(\overline U\times\{a\})\cup(\partial U\times[a,b]).
```

A subparabolic function $`v:\Theta\to[0,\infty)`$ is upper semicontinuous and has the reversed comparison property. The comparison solutions satisfy $`h\in C_{\mathrm{loc}}((a,b);L_{\mathrm{loc}}^{m+1}(U))`$, $`h^m\in L_{\mathrm{loc}}^2((a,b);W_{\mathrm{loc}}^{1,2}(U))`$, and

```math
\int_K\left(\nabla(h^m)\cdot\nabla\varphi-h\,\partial_t\varphi\right)\,dx\,dt=0
\quad(\varphi\in C_c^\infty(K)).
```

Define the original, nonstrict Perron classes

```math
\begin{aligned}
\mathcal U_f&=\{u\text{ superparabolic}:
 \liminf_{\Theta\ni z\to\xi}u(z)\ge f(\xi)
 \text{ for every }\xi\in\partial\Theta\},\\
\mathcal L_f&=\{v\text{ subparabolic and bounded above}:
 \limsup_{\Theta\ni z\to\xi}v(z)\le f(\xi)
 \text{ for every }\xi\in\partial\Theta\}.
\end{aligned}
```

Must their pointwise envelopes

```math
\overline P_\Theta f(z)=\inf_{u\in\mathcal U_f}u(z),
\qquad
\underline P_\Theta f(z)=\sup_{v\in\mathcal L_f}v(z)
```

coincide everywhere in $`\Theta`$ for every such choice? The datum is prescribed on the full topological boundary. Equality does not require boundary attainment at irregular points.

## Application

The porous medium equation models nonlinear diffusion with finite propagation. Resolutivity would make its two comparison constructions select the same interior solution even for irregular spacetime geometry.

## References

1. J. Kinnunen, P. Lindqvist and T. Lukkari, [*Perron's method for the porous medium equation*](https://doi.org/10.4171/JEMS/658), Journal of the European Mathematical Society 18 (2016), 2953–2969. Introduction, Definition 4.1 and Theorem 5.1.
2. A. Björn, J. Björn, U. Gianazza and J. Siljander, [*Boundary regularity for the porous medium equation*](https://arxiv.org/abs/1801.08005v1), preprint (2018); published in Archive for Rational Mechanics and Analysis 230 (2018), 493–538, [DOI](https://doi.org/10.1007/s00205-018-1251-3). Definitions 2.1, 3.1 and 6.1, Remark 6.3, Theorem 11.2 and Proposition 11.4. The definitions here follow the eligible arXiv version.
3. U. G. Abdulla, [*Well-posedness of the Dirichlet problem for the non-linear diffusion equation in non-smooth domains*](https://doi.org/10.1090/S0002-9947-04-03464-6), Transactions of the American Mathematical Society 357 (2005), 247–265. Domain class, Definition 1.1, Assumptions A, B and M, Theorems 2.1–2.4.
4. B. Avelin and M. Parviainen, [*Wiener's criterion and resolutivity for the p-parabolic equation*](https://arxiv.org/abs/2610.26466v1), preprint (2026), Theorem 1.3.
5. L. Schätzler, C. Scheven, J. Siltakoski and C. Stanko, [*Existence of variational solutions to doubly nonlinear systems in general noncylindrical domains*](https://doi.org/10.1016/j.jde.2026.114139), Journal of Differential Equations 462 (2026), 114139. Introduction, Definition 2.1 and Theorems 2.2–2.4.
6. J. Liu, J. Wang and M. Zhou, [*Free boundary regularity for the porous medium equation*](https://arxiv.org/abs/2610.25740v1), preprint (2026), Theorems 1.1 and 1.3.

## Status review


**Known cases:** The original nonstrict Perron envelopes on every bounded spacetime open set are required. Cylinders, finite unions, boundary-regular classes, p-parabolic resolutivity and free-boundary results do not give this general porous-medium assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The original nonstrict Perron envelopes on every bounded spacetime open set are required. Cylinders, finite unions, boundary-regular classes, p-parabolic resolutivity and free-boundary results do not give this general porous-medium assertion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Kinnunen–Lindqvist–Lukkari prove resolutivity for arbitrary spatial cylinders and explicitly leave general spacetime domains open. Björn–Björn–Gianazza–Siljander restate the question in Remark 6.3 and obtain resolutivity for certain finite unions of cylinders. Their strict comparison principles do not establish equality of the original nonstrict envelopes on every bounded open set.

Abdulla imposes a locally graph-like lateral boundary and additional geometric modulus assumptions; the compared solutions already attain continuous boundary data. The 2026 variational existence theorem assumes a boundary of spacetime measure zero and time-independent Sobolev boundary data, and explicitly leaves uniqueness outside its scope.

Avelin–Parviainen prove general resolutivity for the different equation $`h_t=\mathrm{div}(|\nabla h|^{p-2}\nabla h)`$. Liu–Wang–Zhou address smoothness of the moving interface of specified whole-space Cauchy solutions. Bounded current searches located no matching proof, counterexample or announcement for the stated Perron question. These scope checks do not certify the complete proofs of the cited preprints.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-082db04fa1752c1b**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
