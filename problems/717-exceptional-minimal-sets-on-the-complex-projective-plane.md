# 717. Exceptional minimal sets on the complex projective plane

**Area:** Holomorphic foliations; complex dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathcal F`$ be a singular holomorphic foliation of complex dimension one on $`\mathbf{CP}^{2}`$, with its usual saturated tangent sheaf. Must every regular leaf $`L`$ satisfy
```math
\overline L^{\,\mathbf{CP}^{2}}\cap\mathrm{Sing}(\mathcal F)\ne\varnothing?
```
Here saturation means that $`T_{\mathbf{CP}^{2}}/T_{\mathcal F}`$ is torsion-free. The singular locus is where this quotient fails to be locally free; on this surface it consists of finitely many isolated points. Leaves are taken in the regular locus.

Equivalently, must every **nonempty** closed $`\mathcal F`$-invariant subset of $`\mathbf{CP}^{2}`$ meet the singular locus? Invariance means that the set contains every leaf through each of its regular points. The equivalence follows because a leaf closure that avoids singularities is saturated, by local flow boxes; conversely, a closed invariant set avoiding singularities contains the closure of each of its leaves. Such a compact invariant set contains a minimal one.

No degree, genericity, hyperbolicity or nondicritical assumption is imposed.

## Application

This question concerns global complex dynamics: can a regular leaf accumulate entirely inside a compact set away from all singularities? Its negative formulation is the nonexistence of exceptional minimal sets on the complex projective plane.

## References

1. Denis Cerveau, *Minimaux des feuilletages algébriques de CP(n)*, Annales de l'Institut Fourier **43**(5) (1993), 1535–1543. [DOI](https://doi.org/10.5802/aif.1382); [primary PDF](https://www.numdam.org/item/10.5802/aif.1382.pdf), printed p.1535, definition and open question.
2. Jorge Vitório Pereira, *Holomorphic Foliations with Numerically Trivial Canonical Bundle*, Proceedings of the International Congress of Mathematicians 2026, vol. 3, 603–618, published online 13 July 2026. [DOI](https://doi.org/10.1137/25M1805813); [publisher full text](https://epubs.siam.org/doi/full/10.1137/25M1805813); [PDF](https://epubs.siam.org/doi/epdf/10.1137/25M1805813), §1.2, printed p.603; §2, printed p.605, definitions.
3. Masanori Adachi, Séverine Biard and Judith Brinkschulte, *A residue formula for meromorphic connections and applications to stable sets of foliations*, Journal of Geometric Analysis **33** (2023), article 338. [DOI](https://doi.org/10.1007/s12220-023-01385-9); [primary manuscript](https://arxiv.org/pdf/2210.09273), Theorems 5.1 and 5.3.

## Status review


**Known cases:** The July primary survey retains the unrestricted CP2 question. Results in ambient dimension at least three or with a transverse affine structure do not exclude every exceptional minimal set in the plane.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The July primary survey retains the unrestricted CP2 question. Results in ambient dimension at least three or with a transverse affine structure do not exclude every exceptional minimal set in the plane.

Additional comparison sources: [comparison source 1](https://doi.org/10.5802/aif.1382); [comparison source 2](https://www.numdam.org/item/10.5802/aif.1382.pdf); [comparison source 3](https://doi.org/10.1137/25M1805813); [comparison source 4](https://epubs.siam.org/doi/full/10.1137/25M1805813); [comparison source 5](https://epubs.siam.org/doi/epdf/10.1137/25M1805813); [comparison source 6](https://doi.org/10.1007/s12220-023-01385-9); [comparison source 7](https://arxiv.org/pdf/2210.09273). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Pereira's July 2026 survey explicitly presents the general plane question as open. The numerical-triviality restriction studied elsewhere in that survey does not restrict this introductory question.

Theorem 5.1 of [3] concerns ambient complex dimension at least three. Its surface theorem requires transverse affine structure near the hypothetical minimal set. Neither settles the unrestricted plane statement above.

Bounded current and announcement searches through 25 October 2026 identified no exact general resolution. All-status AIM, OpenAI-announcement and developing-collection comparisons found no equivalent target. The existing tangent-sheaf-splitting question on projective three-space is different. These checks are bounded literature review, not a certification that every online claim was inspected.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-bbdcbc48c8f041e3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
