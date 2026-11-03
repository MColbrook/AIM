# 978. Does dyadic lower decoupling imply general lower decoupling?

**Area:** Probability in Banach spaces and stochastic integration
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a separable Banach space and $`0<p<\infty`$, with
$`\|Z\|_p=(\mathbb E\|Z\|_X^p)^{1/p}`$.
Define $`D_p(X)`$ as the least constant in
```math
\left\|\sum_{n=1}^N r_n a_{n-1}\right\|_p
\le D_p(X)\left\|\sum_{n=1}^N r'_n a_{n-1}\right\|_p,
```

for all finite lengths, independent Rademacher sequences $`r,r'`$, and predictable coefficients
$`a_0\in X`$, $`a_{n-1}=h_{n-1}(r_1,\ldots,r_{n-1})`$.

Define $`D_p^{\mathrm{gen}}(X)`$ analogously by
```math
\left\|\sum_{n=1}^N d_n\right\|_p
\le D_p^{\mathrm{gen}}(X)\left\|\sum_{n=1}^N e_n\right\|_p,
```

uniformly over finite $`L^p(X)`$ sequences $`d,e`$ adapted to the same filtration $`(\mathcal F_n)`$, where $`e`$ is a decoupled tangent sequence of $`d`$: some $`\mathcal H\supseteq\sigma(d_1,\ldots,d_N)`$ makes the $`e_n`$ conditionally independent and satisfies
```math
\mathcal L(d_n\mid\mathcal F_{n-1})
=\mathcal L(e_n\mid\mathcal F_{n-1})
=\mathcal L(e_n\mid\mathcal H)
\quad\text{almost surely}.
```


For every such $`X,p`$, must
```math
D_p(X)<\infty\quad\Longrightarrow\quad D_p^{\mathrm{gen}}(X)<\infty?
```

This asks for finiteness; a uniform comparison constant is a stronger question.

## Application

This tests whether estimates for binary-noise martingales already control general dependent Banach-valued noise, clarifying hypotheses for stochastic integration.

## References

1. S. Cox and S. Geiss, [*On Decoupling in Banach Spaces*](https://doi.org/10.1007/s10959-021-01085-6), *Journal of Theoretical Probability* **34** (2021), 1179-1212. Open Problem 1.1, Definitions 1.5 and 2.5, and Remark 5.6(b).
2. [Author preprint](https://arxiv.org/abs/1805.12377), v1 (2018), Definitions 2.6 and 6.3, Section 9.4(b).

## Status review


**Known cases:** Dyadic lower decoupling must transfer to arbitrary tangent conditional laws. Filtration enlargement and fixed-law restrictions in the source, and subsequent Wiener-space results, do not establish the general transfer.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Dyadic lower decoupling must transfer to arbitrary tangent conditional laws. Filtration enlargement and fixed-law restrictions in the source, and subsequent Wiener-space results, do not establish the general transfer.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The published article retains this implication as unresolved. Its filtration-enlargement and restricted conditional-law results, including Brownian integration estimates, do not establish transfer to arbitrary laws. No matching proof, counterexample or complete-resolution announcement was located in bounded checks through the date above.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-63dcea83def42a81**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
