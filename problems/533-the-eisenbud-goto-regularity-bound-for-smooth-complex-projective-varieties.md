# 533. The Eisenbud-Goto regularity bound for smooth complex projective varieties

**Area:** Algebraic geometry and syzygies
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X\subsetneq\mathbb P^r_{\mathbb C}`$ be a smooth integral nondegenerate projective variety of degree $`d`$ and codimension $`e\ge1`$. Must its ideal sheaf satisfy
```math
\mathrm{reg}(\mathcal I_X)\le d-e+1?
```

Here $`\mathrm{reg}(\mathcal I_X)`$ is Castelnuovo-Mumford regularity on $`\mathbb P^r`$. Equivalently, the question asks whether
```math
H^i\!\left(\mathbb P^r,\mathcal I_X(d-e+1-i)\right)=0
\qquad\text{for every }i>0.
```

The embedding is arbitrary: linear normality and projective normality are not assumed. This concerns the ideal sheaf, not the structure sheaf $`\mathcal O_X`$.

## Application

The bound would control the degrees needed for equations and syzygies of smooth embedded varieties in terms of their degree and codimension.

## References

1. S. Kwak and J. Park, [*Classification and syzygies of smooth projective varieties with 2-regular structure sheaf*](https://doi.org/10.1002/mana.201900345), *Mathematische Nachrichten* **293** (2020), 1378-1389. [Preprint v1](https://arxiv.org/abs/1803.01127), Introduction, especially the definitions and paragraph before Theorem 1.4.
2. J. I. Han, [*The Eisenbud-Goto conjecture for projectively normal varieties with mild singularities*](https://arxiv.org/abs/2601.16103), v2 (9 February 2026). Introduction, Conjecture 1.1, the smooth residual class and Theorem A.
3. J. McCullough, [*Regularity of Prime Ideals*](https://faculty.sites.iastate.edu/jmccullo/files/inline-files/Regularity_of_Primes.pdf), April 2023 lecture notes, Theorem 3.13 and Corollary 3.15.

## Status review


**Known cases:** The 2026 projectively-normal theorem has extra embedding/singularity hypotheses. Singular counterexamples and Ulrich-sheaf counterexamples are not smooth ideal-sheaf regularity counterexamples to this precise arbitrary-embedding question.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The structure-sheaf bound $`\mathrm{reg}(\mathcal O_X)\le d-e`$ is known for smooth varieties. Completing the ideal-sheaf bound requires the relevant normality of the embedding. Smoothness does not itself imply projective normality. The smooth projectively normal case is known; the 2026 result cited above retains additional hypotheses and explicitly distinguishes the general smooth question.

Counterexamples for singular varieties, and results about the separately named Eisenbud-Green-Harris or Ulrich-bundle conjectures, do not settle this target. No matching complete proof, smooth counterexample or complete-resolution announcement was located in bounded checks through the date above.


### Online recheck, 2026-10-30

The 2026 projectively-normal theorem has extra embedding/singularity hypotheses. Singular counterexamples and Ulrich-sheaf counterexamples are not smooth ideal-sheaf regularity counterexamples to this precise arbitrary-embedding question.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2601.16103); [status source 2](https://arxiv.org/abs/2610.12078); [status source 3](https://arxiv.org/abs/1803.01127). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-bc9107527674d480** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
