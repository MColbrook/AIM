# 923. Rapid decay for cocompact lattices in semisimple Lie groups

**Area:** Harmonic analysis / convolution operators and operator algebras
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`G`$ be a connected, noncompact semisimple real Lie group with finite centre, and let $`\Gamma<G`$ be a discrete cocompact lattice, so $`G/\Gamma`$ is compact. Fix a finite symmetric generating set $`S`$ of $`\Gamma`$ and write $`|\gamma|_S`$ for word length. For a finitely supported $`f:\Gamma\to\mathbb C`$, let $`\lambda_\Gamma(f)`$ act on $`\ell^2(\Gamma)`$ by
```math
\bigl(\lambda_\Gamma(f)\xi\bigr)(x)=\sum_{\gamma\in\Gamma}f(\gamma)\xi(\gamma^{-1}x).
```

Does every such lattice have the rapid decay property: do constants $`C>0`$ and $`s\ge0`$ exist such that every finitely supported $`f`$ satisfies
```math
\|\lambda_\Gamma(f)\|_{\ell^2\to\ell^2}
\le C\left(\sum_{\gamma\in\Gamma}|f(\gamma)|^2(1+|\gamma|_S)^{2s}\right)^{1/2}\,?
```

The constants may depend on the lattice and its generating set. This is the real Lie group case of Valette's conjecture; no particular exponent is prescribed.

## Application

The inequality bounds a group convolution operator by a weighted square-summability norm. It connects harmonic analysis and random walks with smooth subalgebras of reduced group $`C^*`$-algebras and their topological $`K`$-theory.

## References

1. A. Valette, *On the Haagerup inequality and groups acting on $`\widetilde A_n`$-buildings*, **Annales de l'Institut Fourier 47** (1997), 1195â€“1208, pp. 1195â€“1197. [DOI](https://doi.org/10.5802/aif.1596); [primary text](https://www.numdam.org/item/10.5802/aif.1596.pdf).
2. I. Chatterji, *Introduction to the Rapid Decay property*, **Contemporary Mathematics 691** (2017), 53â€“72, Conjecture 1.1, p. 56; Proposition 4.1, p. 66. [DOI](https://doi.org/10.1090/conm/691/13893); [author offprint](https://chatterj.perso.math.cnrs.fr/papers/IntroRDSurvey.pdf).
3. A. Boyer, A. Pinochet Lobos and C. Pittet, *Radial rapid decay does not imply rapid decay*, **Annales de l'Institut Fourier 73** (2023), 1421â€“1452, introduction p. 1422 and Definitions 2.1â€“2.4. [DOI](https://doi.org/10.5802/aif.3552); [primary text](https://www.numdam.org/item/10.5802/aif.3552.pdf).
4. B.-O. Battseren, *On the growth of Fourier multipliers*, **Journal of Noncommutative Geometry 18** (2024), 1209â€“1228, p. 1211. [DOI](https://doi.org/10.4171/JNCG/551); [primary text](https://ems.press/content/serial-article-files/48451).

## Status review


**Known cases:** The lattice is cocompact and the target is full rapid decay. Rank-one and selected higher-rank results, radial rapid decay and the publicly posted coefficient-sampling reduction leave the general lattice-descent step open.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The lattice is cocompact and the target is full rapid decay. Rank-one and selected higher-rank results, radial rapid decay and the publicly posted coefficient-sampling reduction leave the general lattice-descent step open.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2023 and 2024 primary texts explicitly retain the general conjecture. Bounded checks through 25 October 2026 found no full solution, counterexample or announced solution for the target above. Known special cases and radial rapid decay do not establish the general inequality. The nonuniform higher-rank counterexamples do not meet the cocompact hypothesis.

## Duplicate check

Compared with the current and all-status AIM/OpenAI statements, all 896 recorded finding decisions and 531 admitted pages. The existing semisimple comparison-map problem concerns cohomology; the OpenAI Baumâ€“Connes counterexamples concern a different assertion and group class.

## Review provenance

Located in the recovered-body review of DOI 10.5802/aif.1596. A separate reviewer checked the formulation and current literature; the coordinator read the primary definitions, explicit openness passages and equivalent norm formulation, and completed the semantic comparison. This is a bounded status review without a claim to verify every cited proof.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ab2e51856d3b8681**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
