# 902. Do small independent perturbations preserve Fourier uniqueness at square-root nodes?

**Area:** Fourier analysis and stable signal reconstruction
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Does there exist a constant $`0<\theta<1`$ with the following property? For every pair of real sequences $`(\varepsilon_n)_{n\geq1}`$ and $`(\delta_n)_{n\geq1}`$ satisfying

```math
|\varepsilon_n|+|\delta_n|<\theta\qquad(n\geq1),
```


the samples

```math
f(0),\quad f\bigl(\sqrt{n+\varepsilon_n}\bigr),\quad
\widehat f(0),\quad \widehat f\bigl(\sqrt{n+\delta_n}\bigr)
\qquad(n\geq1)
```


determine every real-valued even Schwartz function $`f`$ on $`\mathbb R`$ uniquely? Equivalently, if all displayed samples of such an $`f`$ vanish, must $`f\equiv0`$? The spatial and Fourier perturbation sequences are independent. This is the uniform zero-kernel formulation of Ramos and Sousa's Conjecture 6.2.

## Application

The Radchenko–Viazovska formula reconstructs even Schwartz functions from their values and Fourier-transform values at the unperturbed square-root nodes. This conjecture asks whether the uniqueness part survives bounded errors in the squared sampling locations, a stability question at critical sampling density relevant to signal reconstruction.

## References

1. J. P. G. Ramos and M. Sousa, [*Perturbed interpolation formulae and applications*](https://msp.org/apde/2023/16-10/apde-v16-n10-p03-s.pdf), *Analysis & PDE* **16** (2023), no. 10, 2327–2384, [DOI](https://doi.org/10.2140/apde.2023.16.2327), Section 6C, printed p. 2381, Conjecture 6.2.
2. G. Cassese and J. P. G. Ramos, [*On the regularity of Fourier interpolation formulas*](https://arxiv.org/pdf/2503.15733), arXiv:2503.15733v1 (2025), Theorem 1.2.
3. T. K. Lysen, [*Critical and asymmetric Fourier uniqueness pairs*](https://arxiv.org/pdf/2509.17600), arXiv:2509.17600v2 (2025), Section 2.1 and its sufficient conditions.
4. D. Berghaus, A. Bondarenko, D. Radchenko, K. Seip and Q. Sun, [*The basis functions of Fourier interpolation*](https://arxiv.org/pdf/2512.18677), arXiv:2512.18677v1 (2025), Section 1.

## Status review


**Known cases:** Cassese–Ramos Theorem 1.2 treats a common sequence of radicand perturbations under a polynomial decay assumption; the target allows two independent uniformly bounded radicand sequences. Critical-pair density conditions and deleting an exact node do not cover all these perturbations. The target is uniqueness, not a reconstruction-rate requirement.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Cassese–Ramos Theorem 1.2 treats a common sequence of radicand perturbations under a polynomial decay assumption; the target allows two independent uniformly bounded radicand sequences. Critical-pair density conditions and deleting an exact node do not cover all these perturbations. The target is uniqueness, not a reconstruction-rate requirement.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2025 result in Reference 2 treats one common sequence of **radicand** perturbations: its nodes are $`\sqrt{n+\varepsilon_n}`$, with $`|\varepsilon_n|<c(1+n)^{-5/4-\eta}`$ for some $`\eta>0`$ and sufficiently small $`c>0`$. It does not cover two independent uniformly bounded radicand sequences. Ramos and Stoller's [Theorem 1](https://arxiv.org/html/2103.12015v5) permits independent radicand sequences, but also requires polynomial decay. Reference 3 gives sufficient conditions for certain critical pairs, but its density condition does not apply to every admissible perturbation sequence here. Reference 4 obtains nonuniqueness after deleting an exact sampling node and adding extraneous zeros, a different configuration. A targeted search through 2026-10-22 found no proof, counterexample or announced complete resolution of Conjecture 6.2, and no matching AIM, FURTHER or Prove2Me problem was found in the bounded duplicate checks. The original wording puts $`f`$ before $`\theta`$; linearity makes its zero-kernel statement equivalent to one radius working for every $`f`$. The [scope and status audit](../FURTHER_problems/_tracking/fourier-maximal-perturbations-status-2026-10-22.json) records this reasoning and the search limits. The neighboring Conjecture 6.3 is not part of this problem.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-4d3dad6b33b3d4b5**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
