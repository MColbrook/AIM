# 098. A universal bound on excess molecular charge

**Area:** Many-electron quantum mechanics

**Status:** ✅ SOLVED

**Last checked:** 2026-11-03

## Problem statement

For distinct nuclei $`R_1,\ldots,R_M\in\mathbb R^3`$ with charges $`Z_a\in\mathbb N`$, put $`Z=\sum_aZ_a`$ and let

```math
H_N=\sum_{j=1}^N\left(-\frac12\Delta_{x_j}-\sum_{a=1}^M\frac{Z_a}{|x_j-R_a|}\right)+\sum_{i<j}\frac1{|x_i-x_j|}
```

act on $`\bigwedge^N L^2(\mathbb R^3;\mathbb C^2)`$. Let $`N_{\max}`$ be the largest $`N`$ for which $`\inf\sigma(H_N)`$ is an eigenvalue, including a possible threshold eigenvalue. Prove or disprove that a universal finite constant $`C`$ satisfies

```math
N_{\max}\le Z+CM
```

for all choices of charges and nuclear positions.

## Application

The inequality would give a mathematically uniform limit on how many additional electrons a molecule can bind.

## References

1. M. Lewin, [Some open mathematical problems concerning charged quantum particles](https://doi.org/10.5802/crphys.249), Comptes Rendus Physique 26 (2025), Open Problem 1 and §2.1.2: exact target and known bounds.
2. E. H. Lieb, [Bound on the maximum negative ionization of atoms and molecules](https://doi.org/10.1103/PhysRevA.29.3018), Physical Review A 29 (1984), main bound: a general estimate proportional to total nuclear charge.
3. J. P. Solovej, [Mathematics of complex atoms and the periodic table](https://www.math.uci.edu/node/38671), research colloquium abstract (15 May 2026): explicitly distinguishes the open full many-body problem from Hartree–Fock theory.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf), result family 263 (2026). Statement locator: `build/sections/01-introduction.tex, thm:main and following threshold caveat`.

## Status review

**Resolution update (3 November 2026):** Affirmative proof. The printed theorem only covers strict binding. The recorded extension supplies a threshold eigenfunction above the uniform strict-binding cutoff, hence a ground state at the minimum across all particle sectors on the energy plateau. Lemma2.2 uses the eigen-equation and EN<=EN-1, including equality, to give N<=3Z. The state then satisfies the global-minimum hypotheses used in§§3–9, without a strict adjacent gap; their charge contradiction applies directly. The threshold case follows by applying the proof interfaces in §§2–9; Theorem 1.1 itself is stated for strict binding.

[Proof](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf) · [Dated statement comparison](../research/solution-status-audit-2026-11-03/lane-a/098.json). Source locator: Theorem1.1 plus supplied-state proof interface in§§2–9; prior threshold comparison.

### Earlier status record


Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Result: the full molecular charge bound, including the threshold extension.

[Proof or source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-root.md). The linked review records the target comparison.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-098). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-10-13)

**Known cases:** The stated excess-charge bound holds for strictly bound molecular sectors: $`E_N<E_{N-1}`$ implies $`N\le Z+CM`$ with a universal constant.

**Remaining target:** Control ground-state eigenvalues at the ionization threshold as well. The original definition of maximal charge includes such threshold eigenvalues.

**Statement comparison:** Same full fermionic Coulomb Hamiltonian with kinetic term $`-\Delta/2`$ and two spin states. The theorem proves $`N\le Z+CM`$ under strict binding $`E_N<E_{N-1}`$, for real charges at least one and all distinct positions. It expressly leaves threshold eigenstates outside its assertion, while the AIM Nmax includes them.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-098) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/263.md). docs/263 formalizes generalized large-ionization asymptotics and radii, not this strict-binding excess-charge bound. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/098-maximal-molecular-ionization.md).
