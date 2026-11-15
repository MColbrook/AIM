# 632. Classifying Costas polynomials over extension fields

**Area:** Finite-field signal design

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-11-16

## Problem statement

Let $`q=p^r`$, where $`p`$ is prime and $`r\ge2`$. Suppose $`f:\mathbb F_q\to\mathbb F_q`$ satisfies $`f(0)=0`$ and, for every $`d\in\mathbb F_q\setminus\{1\}`$, the map

```math
x\longmapsto f(dx)-f(x)
```

is a permutation of $`\mathbb F_q`$. Must there exist a positive integer $`s`$ with $`\gcd(s,q-1)=1`$ and an invertible $`\mathbb F_p`$-linear map $`L:\mathbb F_q\to\mathbb F_q`$ such that

```math
f(x)=L(x^s)\qquad\text{for every }x\in\mathbb F_q?
```

Equivalently, representing functions by polynomials modulo $`x^q-x`$, must every Costas polynomial be a permutation monomial followed by a linearized permutation polynomial $`L(x)=\sum_{j=0}^{r-1}a_jx^{p^j}`$?

## Application

Costas polynomials generate circular correlation patterns over finite fields and complete families of mutually orthogonal Latin squares. A classification would determine whether the standard finite-field construction exhausts these signal and experimental-design structures.

## References

1. A. Muratović-Ribić, A. Pott, D. Thomson, and Q. Wang, [On the characterization of a semi-multiplicative analogue of planar functions over finite fields](https://doi.org/10.1090/conm/632/12635), *Topics in Finite Fields*, Contemporary Mathematics **632** (2015), 317–325. [Author version](https://www.academia.edu/79639197/On_the_characterization_of_a_semi_multiplicative_analogue_of_planar_functions_over_finite_fields), Corollary 4.2 and Conjecture 4.4.
2. J. Torres and I. Rubio, [Circular Costas maps: a multidimensional analog of circular Costas sequences](https://doi.org/10.1007/s12095-023-00654-2), *Cryptography and Communications* **15** (2023), 941–958. [Preprint v1](https://arxiv.org/abs/2210.16661v1), Remark 30 and Theorem 38 (preprint author order: Rubio–Torres).
3. A. Muratović-Ribić and A. Balašev-Samarski, [Note on the Equivalence of Costas Polynomials and Orthomorphisms](https://arxiv.org/abs/2606.07097), 2026, Sections 1–3.

## Status review

**Solution claim:** Kaiwen Jin, [Classification of Costas polynomials over finite extension fields](../research/solutions/aim-632-costas-classification/paper/costas-classification.pdf), Theorem 1.1, claims the complete original classification for every prime and every extension degree at least two, including the zero multiplier and without a shifting hypothesis.

**Review scope:** The proof was developed with OpenAI Codex and received automated natural-language logical/source checking. One fresh-context AI reader pass and one fresh-context AI referee pass read the same draft, followed by one revision and final artifact checks. [The package records the scope and target comparison](../research/solutions/aim-632-costas-classification/README.md). Independent mathematical review is requested; human referee review, Lean verification and upstream acceptance are not claimed.

**Known cases before this claim:** The analogous prime-field classification is proved. The 2026 source reports exhaustive computational verification for field orders at most 30. The proposed classification also holds under the stronger shifting condition that, for each $`d\ne1`$, there is $`a\ne0`$ with $`f(dx)-f(x)=f(ax)`$ for all $`x`$.

**Review pending:** Independent assessment of the complete submitted argument. The original statement above is unchanged. The June 2026 source retains the unrestricted conjecture and gives its orthomorphism formulation.
