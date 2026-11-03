# 853. The bounded-isometry conjecture for closed symplectic manifolds

**Area:** Symplectic geometry and Hamiltonian dynamics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a closed connected smooth manifold of dimension $`2n`$, $`n\ge1`$, and let $`\omega`$ be a symplectic form. Write $`\mathrm{Symp}_0(M,\omega)`$ for the smooth identity component of the symplectic diffeomorphism group and $`\mathrm{Ham}(M,\omega)`$ for its Hamiltonian subgroup.

For $`h\in\mathrm{Ham}(M,\omega)`$, define its Hofer norm by
```math
\|h\|_{\mathrm H}
=\inf_{\phi_H^1=h}
 \int_0^1\left(\max_{x\in M}H_t(x)-\min_{x\in M}H_t(x)\right)\,dt,
```

where the infimum ranges over smooth time-dependent Hamiltonians generating $`h`$. For $`\phi\in\mathrm{Symp}_0(M,\omega)`$, put
```math
r(\phi)=\sup_{h\in\mathrm{Ham}(M,\omega)}
 \|\phi h\phi^{-1}h^{-1}\|_{\mathrm H}.
```


Does $`r(\phi)<\infty`$ imply $`\phi\in\mathrm{Ham}(M,\omega)`$, for every such $`(M,\omega)`$ and $`\phi`$? The converse follows from $`r(\phi)\le2\|\phi\|_{\mathrm H}`$ for Hamiltonian $`\phi`$. Equivalently, every non-Hamiltonian element of the identity component should have unbounded commutator norm.

## Application

This asks whether bounded displacement under conjugation, measured in Hofer's geometry of Hamiltonian dynamics, detects precisely the Hamiltonian transformations.

## Known progress

The conjecture is due to Lalonde and Polterovich. Han's Theorems 1.3–1.4 establish the standard Kodaira–Thurston case and all linear symplectic forms on the four-torus. Campos-Apanco–Pedroza prove it under a punctured-torus/cohomology hypothesis. Pedroza subsequently relaxes that hypothesis; his Theorem 1.1 still assumes condition (H), rather than covering every closed symplectic manifold.

## References

1. Z. Han, *The bounded isometry conjecture for the Kodaira-Thurston manifold and 4-Torus*, [arXiv:0705.0762v1](https://arxiv.org/pdf/0705.0762v1), 5 May 2007, Definition 1.1, Conjecture 1.2 and Theorems 1.3–1.4. [Version record](https://arxiv.org/abs/0705.0762).
2. C. Campos-Apanco and A. Pedroza, *Bounded symplectic diffeomorphisms and split flux groups*, [arXiv:1005.5722v2](https://arxiv.org/pdf/1005.5722v2), 31 March 2011, hypothesis (H) and Theorem 1.1. [Version record](https://arxiv.org/abs/1005.5722).
3. A. Pedroza, *On the bounded isometry conjecture*, *Comptes Rendus Mathématique* **349** (2011), 1097–1100, [doi:10.1016/j.crma.2011.08.016](https://doi.org/10.1016/j.crma.2011.08.016), condition (H) and Theorem 1.1; [publisher PDF](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2011.08.016.pdf).

## Status review


**Known cases:** The full bounded-isometry conjecture is distinct from versions for the spectral metric. The Kodaira-Thurston, linear four-torus and condition-(H) theorems cover specified manifolds, not all closed symplectic manifolds.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The full bounded-isometry conjecture is distinct from versions for the spectral metric. The Kodaira-Thurston, linear four-torus and condition-(H) theorems cover specified manifolds, not all closed symplectic manifolds.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The coordinating review independently read the defining conjecture and the hypotheses of the later partial results. Current arXiv histories list Han v1 and Campos-Apanco–Pedroza v2. Bounded searches on 25 October 2026 found no matching unrestricted proof, counterexample or complete announcement.

Comparison covered all 1,703 pinned AIM/OpenAI statements and all 904 preceding local findings. Hamiltonian periodic-orbit growth, Arnold fixed-point bounds, nearby-Lagrangian questions and local closing problems have different targets. Generic boundedness of a norm on the Hamiltonian group also differs from the quantified commutator condition above. No equivalent target was located. These dated checks do not certify the cited proofs or establish exhaustive literature coverage.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e01f2666c7e983b4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
