# 010. The Mercedes-star partition of a disk

**Area:** Spectral partitions

**Status:** ✅ SOLVED

**Last checked:** 2026-10-21

## Problem statement

Let $`B=\{x\in\mathbb R^2:|x|<1\}`$. Among triples of pairwise disjoint nonempty connected open subsets $`(D_1,D_2,D_3)`$ of $`B`$, minimize $`\max_i\lambda_1(D_i)`$, where $`\lambda_1`$ is the first Dirichlet eigenvalue. Prove or disprove that the three sectors obtained by three radii separated by angles $`2\pi/3`$ attain the minimum. Equivalently, is

```math
\inf_{(D_1,D_2,D_3)}\max_i\lambda_1(D_i)=j_{3/2,1}^2?
```

Here $`j_{3/2,1}`$ is the first positive zero of the Bessel function $`J_{3/2}`$. The optimization is over all such triples, with no prescribed interface topology or symmetry.

## Application

This provides a concrete three-cell benchmark for partition algorithms used to balance fundamental modes. It isolates the finite-cell geometry behind asymptotic honeycomb design.

## References

1. V. Bonnaillie-Noël and B. Helffer, [On spectral minimal partitions: the disk revisited](https://www.math.ens.psl.eu/~bonnaillie/articles/BoHe13.pdf), Annals of the University of Bucharest, mathematical series (2013), introduction.
2. G. Berkolaiko, Y. Canzani, G. Cox and J. L. Marzuola, [Homology of spectral minimal partitions](https://doi.org/10.1112/jlms.70065), Journal of the London Mathematical Society 111 (2025), introduction and disk example; [preprint](https://arxiv.org/abs/2406.04225).
3. M. Sundqvist, [The Y-partition is the optimal three-partition for the disc and the harmonic oscillator](https://arxiv.org/abs/2609.21964), arXiv:2609.21964 (18 September 2026), Theorem 1.1.

## Status review

**Existing solution noted 2026-10-21:** The conjecture of Bernard Helffer and Thomas Hoffmann-Ostenhof is resolved in [Mikael Sundqvist's paper](https://arxiv.org/abs/2609.21964), posted on 18 September 2026. Theorem 1.1 gives the unrestricted three-cell disk partition minimum as $`j_{3/2,1}^2`$, attained by three equal sectors.

The previous local manuscript has been removed and replaced by a [note pointing to this existing solution](../research/solutions/010-mercedes-disk-partition/README.md). The earlier repository acceptance and AI review are [superseded](../research/solution_reviews/2026-10-13-yui-prs/010-review.md).
