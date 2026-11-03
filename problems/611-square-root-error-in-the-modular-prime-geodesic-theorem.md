# 611. Square-root error in the modular prime geodesic theorem

**Area:** Hyperbolic geometry / geodesic dynamics and spectral analysis
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\Gamma=\mathrm{PSL}_2(\mathbb Z)`$. A hyperbolic element has an eigenvalue of modulus $`\lambda>1`$; define its norm by $`N(P)=\lambda^2`$. Its $`\Gamma`$-conjugacy class is primitive if $`P`$ is not a power $`Q^k`$ with $`Q\in\Gamma`$ and integer $`k\ge2`$. Set
```math
\pi_\Gamma(x)=\#\{[P]_\Gamma:\ [P]_\Gamma\text{ primitive hyperbolic},\ N(P)\le x\},
\qquad
\mathrm{li}(x)=\int_2^x\frac{dt}{\log t}.
```

Is it true that, for every $`\varepsilon>0`$,
```math
\pi_\Gamma(x)=\mathrm{li}(x)+O_\varepsilon(x^{1/2+\varepsilon})
\quad\text{as }x\to\infty\,?
```

The estimate is pointwise for this fixed modular group. Conjugacy classes are counted with the source's convention; no additional identification of an element with its inverse is imposed.

## Application

This would quantify fluctuations in the count of primitive periodic geodesics on the modular hyperbolic surface. The same lengths and multiplicities encode regulators and class numbers of real quadratic fields.

## References

1. K. Soundararajan and M. P. Young, *The Prime Geodesic Theorem*, **Journal für die reine und angewandte Mathematik 676** (2013), 105–120. [DOI](https://doi.org/10.1515/crelle.2012.002); [eligible arXiv:1011.5486v1](https://arxiv.org/pdf/1011.5486v1), introduction p. 1 and Theorem 1.1.
2. A. Acosta Reche, *On the prime geodesic theorem*, [arXiv:2610.01998v2](https://arxiv.org/pdf/2610.01998v2), revised 14 October 2026, §1.2, Corollary 1.3.

## Status review

The original primary source explicitly poses the pointwise square-root error problem. The inspected October 2026 theorem improves a weighted counting estimate with exponent approximately $`0.69359`$, greater than $`1/2`$; it does not prove this target. Bounded current and announcement checks through 25 October 2026 found no full resolution. Smoothed, averaged, short-interval and other-group results require separate comparison.



### Online recheck, 2026-10-30

The October modular prime-geodesic improvement still has exponent above 1/2. Congruence-class, averaged, weighted and Bianchi-manifold estimates do not establish this fixed modular-group pointwise square-root error.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2610.01998); [status source 2](https://arxiv.org/abs/2606.25903); [status source 3](https://arxiv.org/abs/1011.5486). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Duplicate check

Compared with the current and all-status AIM/OpenAI statements, all 897 recorded finding decisions and 532 admitted pages. Resonance-window counting, essential spectral gaps, and existence of infinitely many closed geodesic images ask different questions.

## Review provenance

Found in the full recovered-body scan of arXiv:1011.5486v1. A separate reviewer read the source passages and checked later work. The coordinator independently checked the original definitions and target, the current theorem and version records, and semantic duplicates. This is a bounded literature review, not certification of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-2fc03334cb42a20d** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
