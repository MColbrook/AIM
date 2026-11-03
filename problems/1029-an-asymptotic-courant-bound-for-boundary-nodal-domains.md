# 1029. An asymptotic Courant bound for boundary nodal domains

**Area:** Spectral geometry and elliptic boundary problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega`$ be a relatively compact, connected Lipschitz domain with nonempty boundary in a smooth Riemannian manifold $`(M,g)`$ of dimension $`n\ge2`$. Fix a real potential $`q\in L^\infty(\Omega)`$. The positive Laplacian is $`\Delta_g=-\mathrm{div}_g\nabla_g`$.

Consider the Steklov problem with potential

```math
(\Delta_g+q)u=0\quad\hbox{in }\Omega,
\qquad \partial_\nu u=\sigma u\quad\hbox{on }\partial\Omega.
```

Its weak meaning is that $`u\in H^1(\Omega)`$, its trace $`\phi=\mathrm{Tr}u`$ is nonzero, and

```math
\int_\Omega\bigl(\langle\nabla u,\nabla v\rangle_g+quv\bigr)\,dV_g
=\sigma\int_{\partial\Omega}\phi\mathrm{Tr}v\,dS_g
\qquad(v\in H^1(\Omega)).
```

List the real Steklov eigenvalues in nondecreasing order with multiplicity, starting with index $`1`$. They are bounded below and tend to $`+\infty`$. Choose corresponding real boundary eigenfunctions $`(\phi_k)`$ orthonormal in $`L^2(\partial\Omega,dS_g)`$, allowing any orthonormal choice inside a repeated eigenspace. Define $`M_k`$ to be the number of connected components of

```math
\partial\Omega\setminus\{x:\phi_k(x)=0\},
```

using the continuous representatives of the eigenfunction traces. Infinite counts, if any, are allowed in this definition.

Is it always true, for every fixed domain, metric, potential and such choice of eigenfunctions, that

```math
\limsup_{k\to\infty}\frac{M_k}{k}\le1?
```

This is Hassannezhad–Sher Conjecture 1.4. The domain and potential remain fixed as $`k\to\infty`$; the statement does not assert a uniform finite-index bound over varying geometries. An additional fixed real spectral parameter in the interior equation is already covered by replacing $`q`$ with $`q-\lambda`$.

The weak formulation also covers zero Dirichlet eigenvalues of $`\Delta_g+q`$. Equivalently, let $`K`$ be the finite-dimensional space of outward normal derivatives of its zero-Dirichlet solutions. The Dirichlet-to-Neumann operator acts on $`K^\perp\subset L^2(\partial\Omega)`$, with the normal derivative projected to that space; the eigenfunctions form an orthonormal basis of $`K^\perp`$. The formulation above specifies the Robin eigenfunction directly and does not choose an arbitrary interior extension at a Dirichlet resonance.

## Application

Steklov modes describe stationary fields whose normal flux is proportional to their boundary value. The question asks whether the number of separate positive and negative regions of a high-frequency boundary mode is asymptotically controlled by its spectral index. This concerns the spatial complexity of boundary measurements and boundary-driven modes.

## References

1. A. Hassannezhad and D. Sher, *Nodal count for Dirichlet-to-Neumann operators with potential*, [arXiv:2107.03370v3](https://arxiv.org/abs/2107.03370v3), 8 March 2022, Conjecture 1.4 on p.3; §2 for the weak problem and resonant operator. First submitted 7 July 2021. [AMS early-view identifier](https://doi.org/10.1090/proc/16207); no separate final body was verified.
2. A. Enciso, A. Pistoia and L. Provenzano, *Nonexistence of Courant-type nodal domain bounds for eigenfunctions of the Dirichlet-to-Neumann operator*, [arXiv:2404.07138v1](https://arxiv.org/abs/2404.07138v1), introduction and Theorems 1.1–1.2.
3. D. S. Grebenkov, M. Levitin and I. Polterovich, *Spectral properties of the Dirichlet-to-Neumann map for the Helmholtz equation*, [arXiv:2604.11526v1](https://arxiv.org/abs/2604.11526v1), §6.2.
4. R. Nittka, *Regularity of solutions of linear second order elliptic and parabolic boundary value problems on Lipschitz domains*, Journal of Differential Equations **251** (2011), 860–880. [DOI](https://doi.org/10.1016/j.jde.2011.05.019); [author manuscript](https://arxiv.org/abs/0906.5285), Theorem3.14(ii) in version1 supports the continuous-trace convention through the local coordinate argument recorded in the audit.

## Status review


**Known cases:** The geometry and potential remain fixed and the target is an asymptotic boundary nodal count. Finite-index examples over varying geometries and interior Courant bounds do not settle this boundary limsup.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The geometry and potential remain fixed and the target is an asymptotic boundary nodal count. Finite-index examples over varying geometries and interior Courant bounds do not settle this boundary limsup.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves the corresponding interior bound $`N_k\le k+d`$, where $`d`$ counts nonpositive Dirichlet eigenvalues. It does not bound the number of boundary nodal domains. Results counting only nodal domains above a fixed amplitude threshold also leave the question unanswered.

The 2024 construction gives arbitrarily many boundary nodal domains among finitely many low-index modes by changing the metric. Its introduction explicitly distinguishes the fixed-geometry asymptotic question. The April 2026 survey still records the weaker $`O(k)`$ asymptotic question as open.

Versions 1–2 of the source claimed a smooth-case proof. Version 3 explicitly withdraws that result because of a proof gap and states the conjecture instead. Old abstracts and an October 2021 seminar announcement retain the earlier claim; they do not establish a current solution. The AMS early-view body was inaccessible. The current [institutional accepted-record](https://research-information.bris.ac.uk/en/publications/nodal-count-for-dirichlet-to-neumann-operators-with-potential/) independently repeats the correction and points to version3; no separately repaired final publication was verified. This access gap remains explicit, and published/preprint parity is not assumed.

Current searches found no subsequent complete proof or counterexample. AIM012 asks for the sharp planar interior Dirichlet Pleijel constant, and AIM110 concerns the measure of the interior Steklov nodal set. Neither is this boundary count. An independent selected-primary audit confirmed the complete class, including continuous traces on Lipschitz boundaries and the resonant weak formulation. At a Dirichlet resonance the eigenfunctions form a basis of the projected boundary space, rather than all of boundary $`L^2`$. The current catalogue scan returned22 contexts; all were read and concerned other Courant terminology or full-operator conductivity data. No equivalent target or active resolution announcement was located in the bounded checks.

[Detailed review](../FURTHER_problems/_tracking/parallel/rough-filtering/nodal-asymptotic-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-nodal-asymptotic-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/nodal-asymptotic-prove2-0111-review.json) and [coordinator review](../FURTHER_problems/_tracking/nodal-coordinator-review-2026-10-17.json) record exact versions, reading extents and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e88cc0b1f8cd2dce**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
