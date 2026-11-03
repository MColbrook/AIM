# 724. Is polynomial local mass almost necessary for regular orthogonal polynomials?

**Area:** Orthogonal polynomials and logarithmic potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mu`$ be a nonzero finite positive Borel measure on $`\mathbb C`$ with compact support $`S`$ and positive logarithmic capacity $`\mathrm{cap}(S)`$. Let $`p_n(z)=\kappa_n z^n+\cdots`$ be its orthonormal polynomials, normalized by $`\kappa_n>0`$. Assume that $`\mu`$ is regular in the Stahl–Totik sense:

```math
\lim_{n\to\infty}\kappa_n^{1/n}=\frac{1}{\mathrm{cap}(S)}.
```

Write $`B(z,r)=\{w\in\mathbb C:|w-z|<r\}`$. For $`L>0`$ and $`0<r<1`$, put

```math
C_L(r)=\mathrm{cap}\bigl(\{z\in\mathbb C:\mu(B(z,r))\ge r^L\}\bigr),
```

using logarithmic capacity for Borel sets. Must every such measure satisfy

```math
\lim_{L\to\infty}\;\liminf_{r\downarrow0} C_L(r)
=\mathrm{cap}(S)?
```

This is the explicit question in the notes to Chapter 4 of [1], printed p. 238. The order of the limits is part of the target. It does not require a single finite $`L`$ for which the full limit as $`r\downarrow0`$ equals $`\mathrm{cap}(S)`$. No absolute continuity, interval support, or Dirichlet regularity of $`S`$ is assumed.

## Application

Regularity controls the leading exponential scale of orthogonal polynomials and appears in polynomial and rational approximation. The question asks whether this global asymptotic behavior forces an almost full-capacity set of locations with polynomially large local measure.

## References

1. Herbert Stahl and Vilmos Totik, [*General Orthogonal Polynomials*](https://doi.org/10.1017/CBO9780511759420), Cambridge University Press, 1992, Encyclopedia of Mathematics and its Applications 43. Theorem 3.1.1 and Definition 3.1.2, pp. 60–61; disk definition and criterion $`\Lambda^*`$, pp. 108–109; explicit open question, p. 238. The inspected native publisher units belong to the 2010 digital publication of this work.
2. Thomas Bloom, Norman Levenberg, Federico Piazzon and Franck Wielonsky, [*Bernstein-Markov: a survey*](https://doi.org/10.14658/PUPJ-DRNA-2015-Special_Issue-8), *Dolomites Research Notes on Approximation* **8**, Special Issue (2015), 75–91. Theorem 3.3 and Remark 3, p. 81; Example 8.1, p. 88; Question 1, p. 90. [Published PDF](https://drna.padovauniversitypress.it/system/files/papers/Bloom_etal_10YPDPTS.pdf).
3. Vilmos Totik, [*Erdős on polynomials*](https://publicatio.bibl.u-szeged.hu/3299/1/Erdos.pdf), author version dated 7 July 2013, pp. 15–16.

## Status review


**Known cases:** The required necessary condition uses polynomial local-mass thresholds and an iterated limit. Fixed-exponent sufficient Bernstein-Markov criteria, exponential-threshold necessity and unbounded spectral regularity do not establish it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The required necessary condition uses polynomial local-mass thresholds and an iterated limit. Fixed-exponent sufficient Bernstein-Markov criteria, exponential-threshold necessity and unbounded spectral regularity do not establish it.

Additional comparison sources: [comparison source 1](https://doi.org/10.1017/CBO9780511759420); [comparison source 2](https://doi.org/10.14658/PUPJ-DRNA-2015-Special_Issue-8); [comparison source 3](https://drna.padovauniversitypress.it/system/files/papers/Bloom_etal_10YPDPTS.pdf); [comparison source 4](https://publicatio.bibl.u-szeged.hu/3299/1/Erdos.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

For Dirichlet-regular supports, the stronger fixed-exponent criterion $`\Lambda^*`$ is sufficient for regularity [1, Theorem 4.2.3]. The question above asks for a necessary condition with the weaker iterated-limit conclusion. The polynomial threshold $`r^L`$ must not be replaced by an exponential threshold such as $`e^{-\eta/r}`$: the latter appears in known weaker necessary conditions on interval supports [1; 3].

The survey [2] still asks whether a measure with regular support and the polynomial Bernstein–Markov property can fail every fixed-exponent full-limit condition. That is a stronger question in a restricted setting, rather than an equivalent restatement of the displayed target. Its counterexample separating polynomial from subharmonic Bernstein–Markov properties (Example 8.1) concerns a different condition and does not assert a counterexample here.

The 2025 continuum Schrödinger regularity theory of Eichinger–Lukić uses Martin functions for unbounded spectra, and Kroó's 2025 multivariate Bernstein–Markov theorem supplies sufficient geometric conditions for positive almost-everywhere weights. Their inspected statements do not settle the necessary local-mass condition for all regular compactly supported scalar measures.

Recorded exact-formulation, author, later-proof, counterexample and announced-solution searches through the check date located no matching resolution. The all-status AIM/OpenAI snapshot and existing further-problem comparisons found no matching target. In particular, the matrix-valued Stahl–Totik local-mass implication already in the further list asks a different implication under different mass and set-size hypotheses. These are bounded literature and model checks, not a proof of openness or a certification of the cited proofs.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-dc64a8796d3460b7**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
