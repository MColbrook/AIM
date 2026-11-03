# 826. Classifying rotation-equivariant Minkowski valuations

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge3`$, and let $`\mathcal K^n`$ be the nonempty compact convex subsets of $`\mathbb R^n`$, equipped with the Hausdorff metric and Minkowski addition
$`K+L=\{x+y:x\in K,\ y\in L\}`$.

Classify all continuous maps $`\Phi:\mathcal K^n\to\mathcal K^n`$ satisfying

```math
\Phi(K\cup L)+\Phi(K\cap L)=\Phi(K)+\Phi(L)
```


whenever $`K,L,K\cup L\in\mathcal K^n`$, together with

```math
\Phi(K+x)=\Phi(K),\qquad \Phi(RK)=R\Phi(K)
\quad(x\in\mathbb R^n,\ R\in SO(n)).
```


These are continuous, translation-invariant, rotation-equivariant **Minkowski valuations**. The problem concerns the entire class, without an added monotonicity or affine-equivariance hypothesis. The 2014 BIRS report asks for a description of this class and, separately, its homogeneous subspaces [1, printed p.78]. The 2026 paper retains the complete classification problem and explains its relation to characterizing admissible generating functions [2, §4.2].

Here classification means an effective necessary-and-sufficient description of the allowed operators or their generating data. An existing convolution representation alone does not determine which generating data are admissible [2,4].

## Application

Minkowski valuations organize geometric operators on shapes, including projection and mean-section constructions. Understanding the full class would clarify which operators and convolution kernels preserve convexity, and support integral-geometric formulas and inequalities involving these operators [2,4].

## References

1. BIRS, [*Proceedings 2014*](https://www.birs.ca/files/publications/proceedings/birs_2014_proceedings.pdf), report *Geometric Tomography and Harmonic Analysis (14w5085)*, printed p.78 (native PDF p.90), Franz Schuster's presentation: definition of $`\mathrm{MVal}^{SO(n)}`$, the class-description question and Open problem2 on homogeneous subspaces.
2. L. Brauner, G. C. Hofstätter and O. Ortega-Moreno, [*Lefschetz Operators on Convex Valuations*](https://doi.org/10.1093/imrn/rnag031), *International Mathematics Research Notices* **2026**(4), rnag031, §4.2 immediately after Eq.(4.8). This explicitly states that the complete classification is unknown.
3. F. Dorrek, [*Minkowski Endomorphisms*](https://doi.org/10.1007/s00039-017-0405-z), *Geometric and Functional Analysis* **27** (2017), 466–488, Theorem1.9.
4. F. E. Schuster and T. Wannerer, [*Minkowski valuations and generalized valuations*](https://doi.org/10.4171/JEMS/801), *Journal of the European Mathematical Society* **20** (2018), 1851–1884. This establishes a convolution representation.

## Status review


**Known cases:** The 2026 Lefschetz-operators paper explicitly retains the complete rotation-equivariant Minkowski-valuation classification. Convolution representations leave admissibility of generating functions unresolved. Affinely contravariant function-valued and lattice-polytope classifications have stronger symmetry or different domains.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2026 Lefschetz-operators paper explicitly retains the complete rotation-equivariant Minkowski-valuation classification. Convolution representations leave admissibility of generating functions unresolved. Affinely contravariant function-valued and lattice-polytope classifications have stronger symmetry or different domains.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

A [bounded source, later-result and semantic-duplicate audit](../FURTHER_problems/_tracking/minkowski-valuation-classification-status-20261023.json), through 23 October2026, found no complete classification of the stated class or matching AIM/FURTHER entry. The 2026 published source explicitly retains the problem. Classifications with stronger affine symmetry, different additions or restricted domains do not cover it.

The nearby 2014 homogeneous-decomposition question has a negative answer for $`n\ge3`$: Dorrek constructs an even valuation in this class that is not a sum of homogeneous Minkowski valuations [3]. No such decomposition is assumed here.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a730341c269a4ab4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
