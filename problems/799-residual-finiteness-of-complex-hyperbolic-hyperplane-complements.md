# 799. Residual finiteness of complex hyperbolic hyperplane complements

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge2`$, let $`M`$ be a connected complete finite-volume complex hyperbolic manifold of complex dimension $`n`$, and let $`S\subset M`$ be a compact, possibly disconnected, embedded totally geodesic complex submanifold of complex dimension $`n-1`$.

Must $`G=\pi_1(M\setminus S)`$ be residually finite? Explicitly, for every $`g\in G\setminus\{1\}`$, must there exist a finite group $`F`$ and a homomorphism $`\rho:G\to F`$ such that $`\rho(g)\ne1`$?

The ambient manifold may be compact or noncompact; no arithmetic hypothesis is imposed. Components of $`S`$ are disjoint, as required for an embedded submanifold. The question asks for a proof for every such pair or a counterexample within this class.

## Application

This asks whether finite covering spaces can detect every nontrivial loop after drilling compact complex hypersurfaces from a negatively curved manifold. It connects the geometry of these complements with their finite quotients and covering spaces.

## References

1. I. Belegradek, [Complex hyperbolic hyperplane complements](https://arxiv.org/html/0711.5001v2), arXiv:0711.5001v2, Introduction and Question 1.5, attributed there to Toledo; definitions on physical page 1 and question on page 4 of the PDF.
2. M. Stover and D. Toledo, [Residual finiteness for central extensions of lattices in $`\mathrm{PU}(n,1)`$ and negatively curved projective varieties](https://arxiv.org/pdf/2108.12404v2), Theorems 1.1-1.2 and Corollary 1.4.
3. OpenAI, [A torsion-free hyperbolic group that is not residually finite](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/paper.pdf), September 2026, Theorem 1.1 and construction in Section 2; a related announcement with different scope.

## Status review


**Known cases:** Residual nonfiniteness of central extensions and unrelated hyperbolic groups does not realize a complement of the specified embedded totally geodesic complex hypersurface. The unrestricted complement target remains unmatched in bounded current searches.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Residual nonfiniteness of central extensions and unrelated hyperbolic groups does not realize a complement of the specified embedded totally geodesic complex hypersurface. The unrestricted complement target remains unmatched in bounded current searches.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 26 October 2026. Belegradek proves relative and residual hyperbolicity, which do not establish residual finiteness. Stover-Toledo prove results for specified central extensions and punctured line-bundle total spaces; these are different from $`M\setminus S`$.

The OpenAI manuscript announces a non-residually-finite word-hyperbolic group built from a finite triangle complex. Its statement and construction do not identify that group with a complement in the class above. A negative example in this geometric class would have implications for hyperbolic groups; the reverse implication is not justified.

Current literature, version, announcement and all-status duplicate checks found no matching complete resolution. Selected primary statements were checked independently; no certification of every cited proof or Lean replay is claimed. Detailed review receipts are retained in the research ledger.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-74633e0876d01b60**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
