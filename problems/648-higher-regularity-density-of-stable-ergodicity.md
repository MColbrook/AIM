# 648. Higher-regularity density of stable ergodicity

**Area:** Geometry, topology and smooth dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a compact connected smooth Riemannian manifold without boundary, of dimension at least three, with normalized volume measure $`m`$. A volume-preserving diffeomorphism $`g`$ is **stably ergodic** if some $`C^1`$ neighborhood $`U`$ of $`g`$ has the following property: every volume-preserving $`C^2`$ diffeomorphism $`h\in U`$ is ergodic for $`m`$. Ergodicity means that each invariant measurable set has measure zero or one.

Use the source's partially hyperbolic class. Thus $`f`$ admits a continuous nontrivial $`Df`$-invariant splitting
```math
TM=E^s\oplus E^c\oplus E^u
```

and continuous positive functions $`\nu,\widehat\nu,\gamma,\widehat\gamma`$, with
```math
\nu,\widehat\nu<1,\qquad
\nu<\gamma<\widehat\gamma^{-1}<\widehat\nu^{-1},
```

such that at every $`x\in M`$, for nonzero vectors in the indicated subbundles,
```math
\|D_xf(v^s)\|<\nu(x)\|v^s\|,\qquad
\gamma(x)\|v^c\|<\|D_xf(v^c)\|<\widehat\gamma(x)^{-1}\|v^c\|,\qquad
\widehat\nu(x)^{-1}\|v^u\|<\|D_xf(v^u)\|.
```


For every integer $`r\ge2`$, every volume-preserving partially hyperbolic $`C^r`$ diffeomorphism $`f:M\to M`$, and every $`C^r`$ neighborhood $`V`$ of $`f`$, must $`V`$ contain a volume-preserving partially hyperbolic $`C^r`$ diffeomorphism $`g`$ that is stably ergodic?

The approximation must occur in the $`C^r`$ topology. The robustness in the definition of stable ergodicity is measured in the $`C^1`$ topology among volume-preserving $`C^2`$ maps.

## Application

The question asks whether robust statistical indecomposability is typical in conservative partially hyperbolic dynamics even when perturbations must remain small in higher derivatives. It separates robust ergodicity from weaker orbit-complexity or entropy properties.

## Known progress

The one-dimensional-center case is established, as reviewed in the source. Avila, Crovisier and Wilkinson prove density in the $`C^1`$ topology for arbitrary center dimension; this does not provide $`C^r`$ approximation for $`r\ge2`$.

Leguil and Piñeyrúa's Theorem A gives $`C^r`$-density under a two-dimensional-center, strong-bunching, dynamical-coherence and plaque-expansiveness package. These extra hypotheses are not imposed in the general conjecture.

Feng and Ures' Theorem 1.3 proves ergodicity for every conservative $`C^2`$ partially hyperbolic diffeomorphism of a closed three-dimensional manifold with no periodic points. This restricted three-dimensional theorem does not establish higher-regularity density in the full class.

## Status review


**Known cases:** C1-density is known; higher-regularity results add center-bunching/coherence or center-dimension assumptions. The October expanding-on-average theorem is likewise restricted and does not prove general Cr-density for each r>=2.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The eligible and latest conjecture, the original partial-hyperbolicity definition and Theorem A, the $`C^2`$-perturbation definition in the ACW author manuscript, and Feng–Ures' actual latest main theorem were read. Current primary-source searches for a full proof or announcement found no matching unrestricted $`C^r`$-density result on 24 October 2026. Bounded Prove2Me searches returned no matching target.

All-status AIM/OpenAI and FURTHER checks distinguish the target from standard-map positive entropy, Shub's homological entropy conjecture, quantum unique ergodicity, smooth realization of probability transformations, and the Brownian queue transformation. This is a statement-level literature review, not a verification of every cited proof.



### Online recheck, 2026-10-30

C1-density is known; higher-regularity results add center-bunching/coherence or center-dimension assumptions. The October expanding-on-average theorem is likewise restricted and does not prove general Cr-density for each r>=2.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2610.24946); [status source 2](https://doi.org/10.1016/j.aim.2020.107496); [status source 3](https://doi.org/10.3934/jmd.2026017). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## References

1. M. Leguil and L. P. Piñeyrúa, [Accessibility for dynamically coherent partially hyperbolic diffeomorphisms with 2D center](https://arxiv.org/abs/2112.12762), Conjecture 1.1, Section 2.1 and Theorem A; eligible v1 and latest v2.
2. A. Avila, S. Crovisier and A. Wilkinson, [$`C^1`$ density of stable ergodicity](https://www.math.uchicago.edu/~wilkinso/papers/acw2-14Sept2017.pdf), author manuscript, introduction and main theorem; *Advances in Mathematics* **379** (2021), 107496, [DOI](https://doi.org/10.1016/j.aim.2020.107496).
3. Z. Feng and R. Ures, [Accessibility and ergodicity of partially hyperbolic diffeomorphisms without periodic points](https://arxiv.org/abs/2404.07062), latest v2, Theorem 1.3; *Journal of Modern Dynamics* **22** (2026), 643–694, [DOI](https://doi.org/10.3934/jmd.2026017).

## Collection provenance

Promoted from retained further problem **FURTHER-7d9554bef6df4e67** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
