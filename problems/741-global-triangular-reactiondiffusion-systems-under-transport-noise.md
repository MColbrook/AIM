# 741. Global triangular reaction–diffusion systems under transport noise

**Area:** Stochastic reaction–diffusion equations; mathematical chemistry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\ge2`$, $`N\ge2`$ and $`K\ge1`$ be integers, and let $`\nu_i>0`$. On the torus $`\mathbb T^d`$, consider the Itô system

```math
du_i=(\nu_i\Delta u_i+f_i(u))\,dt+
\sum_{k=1}^K\bigl[b_{ki}(x)\cdot\nabla u_i+g_{ki}(u)\bigr]\,dW^k_t,
\qquad i=1,\ldots,N.
```

Here $`W^1,\ldots,W^K`$ are independent real Brownian motions. The vector fields $`b_{ki}`$ are smooth and divergence free, may differ between species, are not all zero, and satisfy, for some $`\eta>0`$,

```math
\nu_i I-\frac12\sum_{k=1}^K b_{ki}(x)\otimes b_{ki}(x)\ge\eta I
\qquad(x\in\mathbb T^d,\ i=1,\ldots,N).
```

The functions $`f_i:\mathbb R^N\to\mathbb R`$ and $`g_i=(g_{ki})_{k=1}^K:\mathbb R^N\to\mathbb R^K`$ are smooth. Each $`g_i`$ is globally Lipschitz, and for $`y\in[0,\infty)^N`$ with $`y_i=0`$,

```math
f_i(y)\ge0,\qquad g_i(y)=0.
```

Assume that some finite $`h\ge3`$ and $`C,c_0,c_1\ge0`$ satisfy, for nonnegative $`y,z`$,

```math
|f_i(y)-f_i(z)|
\le C(1+|y|^{h-1}+|z|^{h-1})|y-z|,
\qquad
\sum_{i=1}^N f_i(y)\le c_0+c_1\sum_{i=1}^N y_i.
```

Assume also that there are an invertible lower triangular matrix $`R`$ with nonnegative entries and a vector $`r\in\mathbb R^N`$ such that

```math
Rf(y)\le\left(1+\sum_{i=1}^N y_i\right)r
\qquad(y\in[0,\infty)^N),
```

componentwise. For every deterministic smooth nonnegative initial condition, **is the unique maximal local strong solution global almost surely**, with

```math
\sup_{0\le t\le T}\|u(t)\|_{L^\infty(\mathbb T^d;\mathbb R^N)}<\infty
\quad\text{almost surely for every finite }T?
```

Local solutions are the spatially regular parabolic solutions satisfying the integrated Itô system, continuous in space and time up to their lifetime. Smooth coefficients and initial data give spatial regularity before that lifetime; the question excludes finite-time concentration blowup. All diffusivities and transport fields satisfying the displayed conditions are allowed.

## Application

The components model concentrations of interacting, diffusing species subject to random transport. Triangular control bounds successive combinations of reaction rates even when individual rates have high polynomial growth. The question asks whether this structure still prevents concentration blowup when species experience different random transport.

## References

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, NoDEA **32**, 123 (2025), published PDF pp. 96–100 and Open Problem 7 on p. 131. [Article](https://doi.org/10.1007/s00030-025-01090-2), [published PDF](https://link.springer.com/content/pdf/10.1007/s00030-025-01090-2.pdf).
2. A. Agresti and M. Veraar, *Reaction-Diffusion Equations with Transport Noise and Critical Superlinear Diffusion: Global Well-Posedness of Weakly Dissipative Systems*, SIAM J. Math. Anal. (2024), §1.4, Assumption 2.1(3) and §2. [Article](https://doi.org/10.1137/23M1562482). Section 1.4 distinguishes triangular systems from the quadratic mass-control problem.
3. D. Milesis and M. Salins, *Global in time solutions to stochastic reaction-diffusion systems with superlinear reactions satisfying a triangular control of mass*, [arXiv:2604.06645v2](https://arxiv.org/html/2604.06645v2), §3 and Theorem 5.2.
4. A. Agresti, M. Kniely and B. Q. Tang, *Global classical solutions by transport noise for reaction–diffusion systems with entropy dissipation*, [arXiv:2608.13332v1](https://arxiv.org/html/2608.13332v1), §1.1 and Theorem 3.4.

## Status review


**Known cases:** The current triangular stochastic theorem has state-dependent multiplicative noise, rather than species-dependent spatial transport derivatives. Special common random translations and suitably selected high-probability regularizing noise do not establish almost-sure global existence for every admissible fixed transport field.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current triangular stochastic theorem has state-dependent multiplicative noise, rather than species-dependent spatial transport derivatives. Special common random translations and suitably selected high-probability regularizing noise do not establish almost-sure global existence for every admissible fixed transport field.

Additional comparison sources: [comparison source 1](https://doi.org/10.1007/s00030-025-01090-2); [comparison source 2](https://link.springer.com/content/pdf/10.1007/s00030-025-01090-2.pdf); [comparison source 3](https://doi.org/10.1137/23M1562482); [comparison source 4](https://arxiv.org/html/2604.06645v2); [comparison source 5](https://arxiv.org/html/2608.13332v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

This is a precisely stated subquestion of the survey's Open Problem 7, restricted to a torus, smooth finite noise, and smooth deterministic initial data. The source's rough or infinite-dimensional noise, other domains and superlinear state-dependent noise are not included. Its polynomial growth assumption extends beyond quadratic reactions. AIM456 instead allows general quadratic mass-control systems without triangular control; neither whole class is identified with the other.

A special pure-transport case reduces to a deterministic triangular system: if all species share constant transport fields with covariance a scalar multiple of the identity and $`g=0`$, a common random translation gives a deterministic system with positive adjusted diffusivities. Such a reduction does not treat all prescribed, spatially varying, species-dependent fields above.

The May 2026 triangular-system theorem treats state-dependent multiplicative noise without derivatives of the solution. Its coefficient $`\sigma(a)`$ depends on concentrations, and does not include the transport term $`b\cdot\nabla u`$. The August 2026 theorem gives high-probability global existence for suitably chosen transport noise in complex-balanced networks under additional hypotheses. Its conclusion does not assert almost-sure global existence for every admissible transport field in the class above.

Source note: the printed survey Assumption 8.4(2) on p. 97 displays the reverse inequality to the positive parabolicity residual stated here. Our explicit condition follows the independent 2024 primary, Assumption 2.1(3); it is not silently substituted into the printed assumption.

Bounded searches on 27 October 2026 found no matching full proof or counterexample announcement. The recorded comparison includes every-status local findings and current public AIM/OpenAI descriptions and abstracts. It does not certify all cited proofs or unpublished work. No formal verification is claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e8059098b0909dd9**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
