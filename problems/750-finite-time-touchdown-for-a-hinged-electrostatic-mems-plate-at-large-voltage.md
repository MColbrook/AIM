# 750. Finite-time touchdown for a hinged electrostatic MEMS plate at large voltage

**Area:** Free-boundary PDEs and electrostatic actuators
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix a bounded convex domain $`D\subset\mathbb R^2`$ with $`C^{4,\gamma}`$ boundary for some $`0<\gamma<1`$, and parameters
```math
\varepsilon>0,\qquad\beta>0,\qquad\tau\ge0,\qquad-1<\sigma<1.
```

Here $`\nu`$ is the exterior unit normal on $`\partial D`$ and $`\kappa`$ is its curvature, with the convention $`\kappa\ge0`$ for convex domains. For $`k=3,4`$, write
```math
H^k_B(D)=\{v\in H^k(D):v=0,\ \Delta v-(1-\sigma)\kappa\partial_\nu v=0\text{ on }\partial D\}.
```

For each voltage parameter $`\lambda>0`$, consider the unique maximal solution with the fixed rest initial condition $`u(0,x)=0`$. Its plate displacement $`u(t,x)>-1`$ satisfies
```math
\partial_tu+\beta\Delta_x^2u-\tau\Delta_xu
=-\lambda\left(\varepsilon^2|\nabla_x\psi_u(t,x,u(t,x))|^2+|\partial_z\psi_u(t,x,u(t,x))|^2\right),
```

with $`u=\Delta_xu-(1-\sigma)\kappa\partial_\nu u=0`$ on $`\partial D`$. For each $`t`$, the potential $`\psi_u(t)`$ is determined on
```math
\Omega(u(t))=\{(x,z):x\in D,\ -1<z<u(t,x)\}
```

by
```math
\varepsilon^2\Delta_x\psi_u+\partial_z^2\psi_u=0\quad\text{in }\Omega(u(t)),\qquad
\psi_u(t,x,z)=\frac{1+z}{1+u(t,x)}\quad\text{on }\partial\Omega(u(t)).
```

The maximal time $`T_\lambda\in(0,\infty]`$ is for the locally unique solution class
```math
u\in C([0,T_\lambda);H^3_B(D))\cap C((0,T_\lambda);H^4_B(D))\cap C^1((0,T_\lambda);L^2(D)),
\qquad\psi_u(t)\in H^2(\Omega(u(t))).
```

The plate equation holds in $`L^2(D)`$ for positive times, and the elliptic equation and boundary traces have their Sobolev meanings.

**Is there a finite $`\Lambda=\Lambda(D,\varepsilon,\beta,\tau,\sigma)>0`$ such that $`T_\lambda<\infty`$ for every $`\lambda>\Lambda`$?** By the source's continuation theorem, such a finite maximal time would necessarily satisfy
```math
\liminf_{t\uparrow T_\lambda}\min_{x\in\overline D}u(t,x)=-1.
```


This is the rest-initial-data subcase of the source's explicitly stated large-voltage question. It does not ask for a sharp pull-in voltage or equality with a stationary threshold. The aspect ratio $`\varepsilon`$ remains fixed and positive.

## Application

The model couples the bending of a hinged conducting plate to the electric field in the gap above a rigid ground plate. Finite-time touchdown describes loss of the gap under sufficiently high applied voltage, a design limit for electrostatic actuators and a useful switching mechanism.

## References

1. K. Nik, [On a Free Boundary Model for Three-Dimensional MEMS with a Hinged Top Plate II: Parabolic Case](https://arxiv.org/abs/2103.06776), sole arXiv:2103.06776v1,11March2021, equations(1.1)–(1.5), Theorems1.1–1.3 and explicit questions on pp4 and24. Related publication: [Communications on Pure and Applied Analysis20(10)(2021),3395–3417](https://doi.org/10.3934/cpaa.2021110).
2. K. Nik, [On a Free Boundary Model for Three-Dimensional MEMS with a Hinged Top Plate I: Stationary Case](https://arxiv.org/abs/2103.06772), arXiv:2103.06772v1, Theorems3.3–3.4 and Lemma5.1. Related publication: Portugaliae Mathematica78(2021),211–232.
3. Ph. Laurençot and Ch. Walker, [Finite Time Singularity in a MEMS Model Revisited](https://ems.press/content/serial-article-files/35977), Zeitschrift für Analysis und ihre Anwendungen37(2018),209–219, DOI10.4171/ZAA/1610, model(1.3)–(1.4) and Theorem1.1. This is a second-order membrane evolution on an interval.

## Status review


**Known cases:** The moving-domain electrostatic potential, hinged fourth-order plate, fixed positive aspect ratio and rest initial data are essential. Stationary nonexistence, second-order membranes and inverse-gap-force quenching do not show finite maximal time for this free-boundary evolution. Access to the newly indexed higher-order quenching article was rate limited; its title is not accepted as an exact resolution.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The moving-domain electrostatic potential, hinged fourth-order plate, fixed positive aspect ratio and rest initial data are essential. Stationary nonexistence, second-order membranes and inverse-gap-force quenching do not show finite maximal time for this free-boundary evolution. Access to the newly indexed higher-order quenching article was rate limited; its title is not accepted as an exact resolution.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2103.06776); [comparison source 2](https://doi.org/10.3934/cpaa.2021110); [comparison source 3](https://arxiv.org/abs/2103.06772); [comparison source 4](https://ems.press/content/serial-article-files/35977). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Reviewed18October2026. The exact source's only listed arXiv version was fully read. It proves global existence at small voltage and proves that touchdown is the only possible finite-time obstruction; it explicitly leaves large-voltage finiteness open. The actual author-uploaded journal-formatted text retains that question and the same model. The final23-page publisher PDF was not compared with the25-page preprint, so full final-edition parity is not asserted.

The stationary companion's large-voltage nonexistence theorem is distinct: a global evolution might approach contact only at infinite time. Its electric-field lower bound uses spatial subharmonicity of a stationary displacement and does not automatically apply to the evolution. Known finite-time results for second-order membrane equations, inverse-gap-force reductions, or an integral-coupled radial MEMS model do not state the displayed hinged fourth-order moving-domain problem.

AIM438 asks regularity of extremal stationary solutions of a second-order singular semilinear Dirichlet equation in dimensions3–6; it is a different target. All-status AIM/OpenAI navigation and FURTHER comparisons found no equivalent target. The independent selected audit passed. Six targeted aliases returned no matches across all186 cached all-status Prove2Me listing pages; this is a description comparison, not a review of every mission proof. The [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-nik-hinged-mems-touchdown-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/continuum/nik-mems-prove2me0173-review.json) and [coordinator review](../FURTHER_problems/_tracking/nik-hinged-mems-coordinator-review-2026-10-18.json) passed at their recorded extents. The current-status checks preserve the stated model and version limits; they do not certify every referenced proof.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c2ecd10db9b1b9c9**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
