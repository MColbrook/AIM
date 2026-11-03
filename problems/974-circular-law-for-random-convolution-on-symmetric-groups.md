# 974. Circular law for random convolution on symmetric groups

**Area:** Probability and random operator spectra
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix a complex random variable $`\xi`$ with

```math
\mathbb E\xi=0,\qquad \mathbb E\xi^2=0,\qquad \mathbb E|\xi|^2=1.
```

For each $`N`$, take independent copies $`\{\xi_N(s):s\in S_N\}`$, where $`S_N`$ is the symmetric group. Form the $`N!\times N!`$ convolution matrix

```math
A_N(h,g)=\frac{\xi_N(hg^{-1})}{\sqrt{N!}},\qquad h,g\in S_N,
\qquad \mu_N=\frac1{N!}\sum_{j=1}^{N!}\delta_{\lambda_j(A_N)}.
```

Eigenvalues are counted with algebraic multiplicity. **Does $`\mu_N`$ converge weakly in probability to the uniform probability measure on the unit disk?** Explicitly, for every bounded continuous $`\varphi:\mathbb C\to\mathbb R`$, is

```math
\int\varphi\,d\mu_N\xrightarrow{\mathbb P}
\frac1\pi\int_{|z|\le1}\varphi(z)\,dA(z)?
```

This is the symmetric-group component of [1, §7 II]. No higher moments, density or independence between different $`N`$ is assumed. Coefficients indexed by group elements are independent; the full matrix entries are dependent. Singular-value convergence is a separate assertion.

## Application

The question tests spectral universality for structured, highly dependent random operators. It asks whether a macroscopic planar eigenvalue law survives replacing Gaussian coefficients by any fixed complex law satisfying the displayed moments.

## References

1. R. Adamczak, *Random non-Abelian G-circulant matrices. Spectrum of random convolution operators on large finite groups*, [arXiv:1712.04772v2](https://arxiv.org/pdf/1712.04772v2), 20 December 2017; Theorems 1.5 and 1.10, §7 II. [Official version history](https://arxiv.org/abs/1712.04772).
2. M. Gerspach, *Spectra of random non-Abelian real-valued G-circulant matrices*, [author manuscript, Theorems 6–7](https://www.maximgerspach.com/wp-content/uploads/2021/01/NonAbelianGCirculants2.pdf).

## Status review


**Known cases:** The non-Gaussian convolution eigenvalues are needed with only the stated second moments. Gaussian circular laws and non-Gaussian singular-value laws do not imply this nonnormal eigenvalue limit.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The non-Gaussian convolution eigenvalues are needed with only the stated second moments. Gaussian circular laws and non-Gaussian singular-value laws do not imply this nonnormal eigenvalue limit.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The Gaussian eigenvalue case and universal singular-value results do not establish this nonnormal eigenvalue statement. Reference [2] treats real Gaussian coefficients for eigenvalues and non-Gaussian coefficients for singular values. A real Gaussian law does not satisfy $`\mathbb E\xi^2=0`$.

Bounded current-resolution and announcement searches found no matching complete claim. The exact latest preprint is cited; unconfirmed published date/body parity is not asserted. Full nearest-statement comparisons covered 1,146 private findings and 1,704 retained public all-status entries, followed by the distinct transport, CMC and C258 additions. Ginibre couplings, GOE crossings, tensor-column singular values and representation-theoretic tensor squares have different targets. See the [owner and semantic review](../FURTHER_problems/_tracking/focused-Adamczak-symmetric-group-circular-law-C248-A-20261029/OWNER-EXACT-COMPLEX-FINITE-VARIANCE-SN-CIRCULAR-LAW-PRIMARY-CURRENT-AND-FULL-NEAREST-SEMANTIC-PROPOSAL.json) and [independent model peer](../FURTHER_problems/_tracking/focused-Adamczak-symmetric-group-circular-law-C248-A-20261029/C-INDEPENDENT-SYMMETRIC-GROUP-CONVOLUTION-FACTORIAL-NORMALIZATION-COMPLEX-LAW-AND-EIGENVALUE-MODEL-PEER-PASS.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-393bf2d525efcf96**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
