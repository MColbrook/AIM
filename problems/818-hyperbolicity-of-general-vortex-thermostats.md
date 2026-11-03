# 818. Hyperbolicity of general vortex thermostats

**Area:** Geometric dynamics / nonequilibrium statistical mechanics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M,g)`$ be any connected closed oriented smooth Riemannian surface with $`\chi(M)<0`$. Write $`SM`$ for its unit tangent bundle, $`X`$ for the geodesic vector field, $`V`$ for positive rotation of the unit vector, and $`H=[V,X]`$.

Choose positive coprime integers $`m,n`$, put $`\ell=m/n`$, and choose an $`n`$-th root $`P\to M`$ of $`SM`$. Explicitly, $`P`$ is a principal circle bundle and $`\rho:P\to SM`$ is an $`n`$-fold covering over $`M`$ satisfying

```math
\rho(p\cdot e^{it})=\rho(p)\cdot e^{int}.
```

Lift $`X,H,V`$ to $`P`$ using $`d\rho`$. In particular, the lifted $`V`$ is $`1/n`$ times the infinitesimal generator of the principal circle action on $`P`$.

For a smooth real one-form $`\theta`$ on $`M`$, let $`\vartheta(p)=\theta_x(v)`$ when $`\rho(p)=(x,v)`$. Let $`a\in C^\infty(P;\mathbb R)`$ satisfy, with $`K_g`$ pulled back to $`P`$,

```math
VVa=-(1+\ell)^2a,
```

```math
K_g=-1-X\vartheta-HV\vartheta
 +\ell\left(a^2+\frac{(Va)^2}{(1+\ell)^2}\right),
```

```math
\frac{XVa}{1+\ell}
 =Ha+\frac{\ell\vartheta Va}{1+\ell}-\ell aV\vartheta.
```

These are the real equations for the general vortex thermostats of Mettler and Paternain, after normalizing the Hermitian metric by a real gauge transformation. They allow fractional differentials of degree $`1+\ell`$.

**Is the flow $`\phi_t`$ of every vector field**

```math
F=X+(a-V\vartheta)V
```

**in this class Anosov?** Precisely, must there exist continuous $`d\phi_t`$-invariant line bundles $`E^s,E^u`$ with

```math
TP=\mathbb RF\oplus E^s\oplus E^u
```

and constants $`C,c>0`$ such that, for every $`t\ge0`$,

```math
\|d\phi_t|_{E^s}\|\le Ce^{-ct},\qquad
\|d\phi_{-t}|_{E^u}\|\le Ce^{-ct}?
```

The constants may depend on all the chosen data. The question includes arbitrary $`\theta`$; it does not assume that all closed orbits are already hyperbolic saddles.

## Application

Thermostats describe particles subject to velocity-dependent forces perpendicular to their velocity, providing deterministic models in nonequilibrium statistical mechanics. This question asks whether a family constructed from geometric vortex equations always has uniform hyperbolicity, strengthening the established dominated splitting of its derivative cocycle.

## References

1. T. Mettler and G. P. Paternain, *Vortices over Riemann surfaces and dominated splittings*, Ergodic Theory and Dynamical Systems **42** (2022), 1781–1806, [DOI](https://doi.org/10.1017/etds.2020.142); [arXiv:2002.03684v3](https://arxiv.org/abs/2002.03684v3), unnumbered question in §1.4, p.4; root bundle §2.2; real formulation (5.2)–(5.3), p.20. The [currently served author version](https://www.mettler.xyz/docs/articles/A20_print.pdf) retains the question in §1.4.
2. T. Mettler and G. P. Paternain, *Holomorphic differentials, thermostats and Anosov flows*, Mathematische Annalen **373** (2019), 553–580, [DOI](https://doi.org/10.1007/s00208-018-1712-x); [arXiv:1706.03554v5](https://arxiv.org/abs/1706.03554v5), Remark 5.4. This asks the preceding integral-degree instance.
3. J. Echevarría Cuesta and J. Marshall Reber, *Thermostats without conjugate points*, Ergodic Theory and Dynamical Systems **46** (2026), 1494–1520, [published paper](https://api.repository.cam.ac.uk/server/api/core/bitstreams/d36a92a8-f0d7-43bd-8514-7ffee7d52b76/content), §1.3 and Lemma 4.3. Its non-Anosov examples are on the two-torus.

## Status review


**Known cases:** The published 2026 quasi-Fuchsian paper treats holomorphic integral-degree differentials with zero theta, rather than all root-bundle vortex thermostats with arbitrary theta. The general source still gives dominated splitting and conditional Anosovness. Non-Anosov torus thermostats fail the negative-Euler and vortex hypotheses.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The published 2026 quasi-Fuchsian paper treats holomorphic integral-degree differentials with zero theta, rather than all root-bundle vortex thermostats with arbitrary theta. The general source still gives dominated splitting and conditional Anosovness. Non-Anosov torus thermostats fail the negative-Euler and vortex hypotheses.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Every vortex thermostat has a dominated splitting. The source proves the Anosov property if $`\theta=0`$, and also if all closed orbits are hyperbolic saddles. The zero-differential case is another known hyperbolic case. None of these hypotheses is imposed on a general competitor here.

The 2026 non-Anosov examples with dominated splitting use a torus base and do not satisfy the required negative Euler characteristic. The same paper explicitly leaves open whether a general projectively Anosov thermostat on a genus-at-least-two surface can fail to be Anosov. Its theorem characterizing transverse Green bundles gives dominated splitting, rather than the uniform contraction and expansion requested here.

Current checks through 18 October 2026 located no matching complete proof or counterexample. The full pinned preprint and selected currently served author model/question were read; full final published-version parity remains a gap. AIM 070 concerns a boundary inverse problem for simple Gaussian thermostats, and AIM 228 concerns heat transport in an anharmonic chain; neither is this assertion. The selected independent review passed, and the refreshed 186-page Prove2Me listing comparison found none of the six target aliases; this is not a review of every mission proof. Exact sources, versions and limits are in the [review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/vortex-anosov-review.json).


[Independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-vortex-anosov-review.json), [catalogue comparison](../FURTHER_problems/_tracking/catalogue-combined-review-2026-10-18.json) and [coordinator review](../FURTHER_problems/_tracking/vortex-anosov-coordinator-review-2026-10-18.json) retain the precise scope and version limits. The current listing comparison covered all186pages under six aliases and returned no contexts; complete mission proofs were not certified.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-9796630f3987038e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
