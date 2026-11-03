# 828. Can bounded complementary components of balls be controlled uniformly under nonnegative Ricci curvature?

**Area:** Geometric analysis and Riemannian geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For each dimension $`m`$, does there exist a constant $`\mu_m\in(0,1)`$ with the following property? For every complete, connected, noncompact $`m`$-dimensional Riemannian manifold $`M`$ with $`\mathrm{Ric}_M\geq0`$, every basepoint $`o\in M`$, and every $`r>0`$, each **bounded connected component** of $`M\setminus B_o(r)`$ lies in an **unbounded connected component** of $`M\setminus B_o(\mu_m r)`$.

The constant must depend on the dimension alone, not on the manifold, basepoint or radius. The question concerns the depth of bounded components of a ball's complement; having only one end does not itself give this uniform quantitative containment.

## Application

Remark 4.18 of Bianchini, Mari, Pucci and Rigoli explains that this containment would turn a qualitative decay theorem for the nonparabolic $`p`$-Green kernel into an explicit volume-growth-based bound, without imposing their extra lower volume-growth condition.

## Known results and scope

The authors cite a sufficient condition of Minerbe: together with nonnegative Ricci curvature, a lower volume-growth estimate with exponent greater than one gives such containment with a constant that may also depend on the growth parameters. This does not establish a dimension-only constant for every Ricci-nonnegative manifold. The separately listed [endwise relative-annuli question](848-relative-connectedness-of-annuli-in-ricci-nonnegative-ends.md) allows a space-dependent constant at large radii and has a different target.

## References

1. B. Bianchini, L. Mari, P. Pucci and M. Rigoli, [*Geometric Analysis of Quasilinear Inequalities on Complete Manifolds*](https://air.unimi.it/retrieve/handle/2434/1027528/2356572/final_version_forFrontiers_07_09.pdf), Birkhäuser, Frontiers in Mathematics, 2021, [doi:10.1007/978-3-030-62704-1](https://link.springer.com/book/10.1007/978-3-030-62704-1). See first-party author manuscript, Chapter 4, Remark 4.18, physical page 82 (printed page 77).
2. V. Minerbe, [*Weighted Sobolev inequalities and Ricci flat manifolds*](https://perso.imj-prg.fr/vincent-minerbe/wp-content/uploads/minerbe-pub/Articles/Ricciflat.pdf), *Geometric and Functional Analysis* **18** (2009), 1696–1749. See the relatively connected annuli result under additional volume-growth assumptions.

## Status review


**Known cases:** Minerbe requires reverse volume growth with an exponent greater than one and obtains a constant depending on that data. One-endedness alone does not control depths of bounded complementary components by a dimension-only factor. No matching unrestricted result was located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Minerbe requires reverse volume growth with an exponent greater than one and obtains a constant depending on that data. One-endedness alone does not control depths of bounded complementary components by a dimension-only factor. No matching unrestricted result was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The cited author-manuscript passage explicitly calls the unrestricted Ricci-nonnegative case open. Targeted searches through 23 October 2026 found no matching complete proof, counterexample or announcement, and a semantic review of AIM and admitted FURTHER pages found no duplicate with the dimension-uniform target. The publisher's final chapter text was subscription-gated, so no exact published-page parity is claimed. The [audit](../FURTHER_problems/_tracking/ricci-bounded-ball-components-audit-2026-10-23.json) records source and search limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ac40a0ad6608b045**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
