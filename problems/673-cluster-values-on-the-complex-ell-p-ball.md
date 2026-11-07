# 673. Cluster values on the complex $`\ell_p`$ ball

**Area:** Complex analysis and potential theory
**Status:** ✅ SOLVED
**Last checked:** 2026-11-07

## Problem statement

Let $`1<p<\infty`$, $`p\ne2`$, and let $`B`$ be the open unit ball of $`X=\ell_p(\mathbb N;\mathbb C)`$. Let $`A_u(B)`$ be the Banach algebra of holomorphic functions on $`B`$ that are uniformly continuous in the norm of $`X`$, with the supremum norm. Its spectrum $`M`$ consists of nonzero continuous multiplicative linear functionals. For $`z\in B`$, define

```math
M_z=\{\varphi\in M:\varphi(x^*)=x^*(z)\text{ for every }x^*\in X^*\}.
```

For $`f\in A_u(B)`$ let $`Cl_B(f,z)`$ consist of all limits of $`f(x_\alpha)`$ along nets $`x_\alpha\in B`$ converging weakly to $`z`$. Is it true that, for every $`f\in A_u(B)`$ and every $`z\in B`$ with $`z\ne0`$,

```math
Cl_B(f,z)=\{\varphi(f):\varphi\in M_z\}?
```

The inclusion from left to right always holds. Equality is known at $`z=0`$, and for all points when $`p=2`$. The unit-sphere case is also known; the question concerns nonzero interior points for the non-Hilbert spaces.

## Application

This is a weak corona problem in infinite-dimensional complex analysis. It asks whether every scalar value supplied by an abstract character can be approached by values of the original function along weakly converging points. The source connects this property with a weak analytic Nullstellensatz and solvability of certain Bézout equations.

## References

- D. Carando, D. García, M. Maestre and P. Sevilla-Peris, *On the spectra of algebras of analytic functions*, Contemporary Mathematics **561** (2012), 165–198, [DOI](https://doi.org/10.1090/conm/561/11114). Question 8, p. 14 of the [author manuscript](https://riunet.upv.es/server/api/core/bitstreams/91e84467-fcf4-4ea8-b14c-24f0fc4daa0b/content); definitions and known cases in §3.
- D. Carando, D. Galicer, S. Muro and P. Sevilla-Peris, *Corrigendum to “Cluster values for algebras of analytic functions”*, Advances in Mathematics **329** (2018), 1307–1309, [DOI](https://doi.org/10.1016/j.aim.2018.03.019). The initial general theorem does not follow from the original arguments; corrected statements retain an enlarged-radius result for entire functions of bounded type.
- V. Dimant, S. Lassalle and M. Maestre, *Fibers and Gleason parts for the maximal ideal space of $`\mathcal A_u(B_{\ell_p})`$*, Banach Journal of Mathematical Analysis **19** (2025),4, [DOI](https://doi.org/10.1007/s43037-024-00388-0), introduction, for the distinction between corona and cluster-value properties and the known origin/Hilbert cases.

## Status review

### Reviewed manuscript, 2026-11-07

Matthew J. Colbrook provides the following AI-found [manuscript](../research/solutions/673-cluster-values-on-the-complex-ell-p-ball/main.pdf). Cluster-value equality at every interior point of the complex ell-p ball, for all 1<p<infinity.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

**Review:** The [separate Codex AI audit](../research/solution_reviews/2026-11-07-complex-analysis/673-review.md) checks the complete argument against this exact target and records the primary-source comparisons. No unresolved mathematical gap was identified in the complete resolution. The results were found by AI; human peer review and formal verification are not claimed.

### Earlier status record (historical)

The following dated record describes the pre-submission state.



### Online recheck, 2026-10-30

The same-ball cluster equality at nonzero interior points of complex ell-p for p different from 2 remains distinct from origin, sphere, Hilbert and enlarged-radius bounded-type results. The prior all-space positive proof was invalidated by its published corrigendum. Fresh author/subject searches surfaced fibre geometry and corrected older statements, not a matching new complete theorem.

Additional comparison sources: [comparison source 1](https://doi.org/10.1016/j.aim.2018.03.019); [comparison source 2](https://doi.org/10.1007/s43037-024-00388-0); [comparison source 3](https://people.tamu.edu/~w-johnson/Sofia-The%20cluster%20value%20problem%20for%20Banach%20spaces%20062713.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 17 October 2026. The 2017 arXiv version contains a general positive claim, but its authors explicitly invalidated that proof in their published 2018 corrigendum. The corrected enlarged-radius result for entire functions of bounded type does not settle the displayed same-ball question. The 2025 fibre/Gleason results concern the size and geometry of fibres. A separate 2025 polynomial-cluster reduction uses a stronger convergence topology and a different fibre, and supplies no full resolution here.

Current proof, counterexample and announcement searches found no complete resolution. Semantic checks against every AIM status, the current OpenAI overview and FURTHER found no duplicate; the more general source Question7 is not added as a second problem. The Prove2Me Gamelin match concerned complex dynamics. Exact reading and version/access limits are retained in the [source packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/cluster-lp-review.json) and [independent review](../FURTHER_problems/_tracking/cluster-lp-coordinator-review.json). Negative searches do not certify openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0d2203fd7e84c633**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
