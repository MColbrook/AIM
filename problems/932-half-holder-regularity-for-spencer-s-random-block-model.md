# 932. Half-Hölder regularity for Spencer's random block model

**Area:** Operators, matrices and computation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`d\ge1`$ and numbers $`a,g>0`$. Let $`(v_n)_{n\in\mathbb Z^d}`$ be independent uniform random variables on $`[-1,1]`$. Define the bounded self-adjoint operator on $`\ell^2(\mathbb Z^d;\mathbb C^2)`$
```math
(H_\omega\psi)(n)=
\begin{pmatrix}v_n&a\\a&-v_n\end{pmatrix}\psi(n)
+g^{-1}\sum_{|m-n|_1=1}\psi(m).
```

Let $`e_1,e_2`$ be the standard basis of $`\mathbb C^2`$ and define the normalized integrated density of states by
```math
N(E)=\frac12\,\mathbb E_\omega
\sum_{j=1}^2
\left\langle\delta_0\otimes e_j,\,
\mathbf1_{(-\infty,E]}(H_\omega)
(\delta_0\otimes e_j)\right\rangle .
```

Does there always exist $`C=C(d,a,g)<\infty`$ such that
```math
N(E+\varepsilon)-N(E-\varepsilon)
\le C\varepsilon^{1/2}
\qquad(E\in\mathbb R,\ 0<\varepsilon\le1)?
```

This is a concrete bounded-density specialization of Spencer's conjecture recorded in [1]. Both internal components have the same nearest-neighbor hopping sign. Constants need not be uniform in $`a`$ or $`g`$.

## Application

The bound limits the expected fraction of energy levels in a small interval for a disordered two-component quantum system. It asks whether the square-root singularity permitted by an isolated block remains the worst possible concentration after sites are coupled.

## References

1. Alexander Elgart, Mira Shamis and Sasha Sodin, [*Localisation for non-monotone Schrödinger operators*](https://doi.org/10.4171/JEMS/451), *Journal of the European Mathematical Society* **16** (2014), no. 5, 909–924. The conjecture and partial progress are on p. 911; the operator and IDS conventions are in §1.2, especially Corollary 1.2 on p. 914. [Published text](https://ems.press/content/serial-article-files/31961?nt=1).
2. John Z. Imbrie and Rajinder Mavi, [*Level Spacing for Non-Monotone Anderson Models*](https://arxiv.org/abs/1506.06692), v3 (2016), §1.2 and Theorems 1.1–1.3.
3. Werner Kirsch, Bernd Metzger and Peter Müller, [*Random block operators*](https://arxiv.org/abs/1009.3795), v1 (2010), Eq. (1.2), Proposition 3.1 and Theorem 5.1: a related block model with different hopping signs and additional hypotheses.

## Status review


**Known cases:** Uniformly random diagonal blocks with the same hopping sign and every fixed coupling require the exact one-half Holder exponent. Quasiperiodic block results, smaller Holder exponents at large disorder and opposite-sign hopping models do not cover this.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Uniformly random diagonal blocks with the same hopping sign and every fixed coupling require the exact one-half Holder exponent. Quasiperiodic block results, smaller Holder exponents at large disorder and opposite-sign hopping models do not cover this.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

For every exponent $`0<s<1/2`$, [1] gives an $`s`$-Hölder estimate at sufficiently large $`g`$, with a threshold depending on the exponent. This does not give the endpoint for a fixed coupling.

For $`a=1`$ and small hopping, [2] supplies a stretched-logarithmic eigenvalue-counting bound and level-spacing estimates; it explicitly distinguishes these from Hölder regularity. The square-root spectral mapping in [3] uses opposite hopping signs, so it does not settle the displayed model.

Bounded literature and announcement searches through 24 October 2026 located no matching complete resolution. All-status AIM/OpenAI comparisons, the developing collection and available Prove2Me listings revealed no matching target. These are source and statement checks, without a claim to certify every cited proof or exhaust the literature.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e7793527d7b46adb**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
