# AIM 458 / PR 175: second audit of the repaired channel-calculus input

**PR:** [175](https://github.com/MColbrook/AIM/pull/175). **Reviewed head:** `a9e2073c1da1a576c699b0a71661068013c43ab7`. **Review date:** 2026-10-21. **Finding:** The revision supplies the compatible fractional right inverses missing from the earlier argument. No unresolved mathematical gap was found in this repaired interface.

Independent OpenAI Codex AI review, conducted without another current reviewer's verdict. This report checks the new channel regularity estimate, both right-inverse endpoints, projection images, domain compatibility, interpolation and the corrected comparison theorem. The locators below refer to the pinned manuscript's TeX source. This scoped audit does not replace a complete review of the remaining manuscript; it is not human peer review or Lean verification.

## Corrected theorem interface

Kunstmann–Weis (2013), Theorem 1.3, requires compatible base-space surjections and right inverses, their bounded compatible extensions at both fractional endpoints, the corresponding projection images, and the stated calculus/sectoriality assumptions. The right-inverse estimates are additional hypotheses. The revision states them separately at **lines 689–714** and then constructs one family

```math
\mathcal J_p=L_p i_p A_{0,p}^{-1},
```

where $`A_{0,p}`$ is the unit-viscosity reference Stokes operator and $`L_p`$ is the componentwise Dirichlet Laplacian. This is the type of lift used in the erratum's own Stokes application. [Kunstmann–Weis, Theorem 1.3, p. 802, and its Stokes application, p. 803](https://kaltonmemorial.missouri.edu/assets/docs/ma2006a.pdf).

The following reconstruction checks the newly supplied hypotheses on the periodic channel directly.

## Extra derivative and pressure estimate

**Lines 732–776, Lemma 3.1.** Let $`f\in H^1`$, $`u=A_{0,2}^{-1}\mathbb P_Of`$, and normalize the periodic pressure by its mean. The already constructed strong solution satisfies

```math
-\Delta u+\nabla p=f,\qquad \nabla\cdot u=0,\qquad u|_{\partial O}=0.
```

The strong-domain estimate controls $`u`$ in $`H^2`$. The Helmholtz decomposition controls $`\nabla p`$ in $`L^2`$, and mean-zero Poincaré controls $`p`$ in $`H^1`$.

Horizontal translations preserve the channel, velocity wall values, divergence and pressure mean. Applying this base estimate to horizontal difference quotients yields every third velocity derivative containing a horizontal derivative and every second pressure derivative containing one. Weak compactness identifies the quotient limits with the distributional derivatives.

Write $`u=(u_h,u_3)`$ and let $`z`$ denote the normal coordinate. The remaining derivatives follow in this order:

```math
\partial_z^3u_3=-\nabla_h\cdot\partial_z^2u_h,
\qquad
\partial_z^2p=\partial_zf_3+\Delta\partial_zu_3,
```

then

```math
\partial_z^3u_h
=-\partial_zf_h-\Delta_h\partial_zu_h+\nabla_h\partial_zp.
```

Each right-hand side is controlled by the preceding derivatives and $`\|f\|_{H^1}`$. These identities account for all pure-normal derivatives still needed, with the signs dictated by the momentum equation. Thus

```math
\|u\|_{H^3}+\|p\|_{H^2}\leq C\|f\|_{H^1}.
```

No trace of $`f`$, $`\Delta u`$ or $`p`$ is prescribed. In particular, the proof does not differentiate an unavailable pressure wall condition.

## Positive fractional right inverse

**Lines 778–831, Lemma 3.2.** Write $`A=A_{0,2}`$, $`L=L_2`$, and $`\mathcal J=L i A^{-1}`$. The strong-domain estimate gives $`\mathcal J:H_2\to L^2`$ and $`\mathbb P_O\mathcal J=I`$.

The closed gradient form on $`V_2`$ identifies $`A`$ as positive selfadjoint with $`D(A^{1/2})=V_2`$. Its form resolvent agrees with the constructed strong resolvent by integration by parts and uniqueness. This Hilbert argument is independent of the desired Banach-space calculus.

For $`f\in V_2`$, the new estimate gives $`A^{-1}f\in H^3`$, hence $`\mathcal Jf\in H^1`$. Interpolation of this same operator, using the Hilbert spectral theorem, gives

```math
\mathcal J:
[H_2,D(A^{1/2})]_{2s}=D(A^s)
\longrightarrow [L^2,H^1]_{2s}=H^{2s},
\qquad 0<s<1/2.
```

The scalar identity $`D(L^s)=H^{2s}`$ is only invoked for $`0<s<1/4`$, below the wall trace threshold $`2s=1/2`$. Odd reflection and the sine-series representation are valid there. The manuscript uses full-vector $`H^1`$ as an intermediate target, which imposes no unwanted zero trace on $`\mathcal Jf`$.

The cited indicator-multiplier theorem allows Sobolev order $`-1+1/p<r<1/p`$. At $`p=2`$, the order used here is $`r=2s\in(0,1/2)`$, strictly within that interval. [Breit–Gaudin, arXiv:2511.19091v1, Proposition 2.4, p. 45](https://arxiv.org/pdf/2511.19091v1).

Consequently, the positive endpoint $`\mathcal J_2:D(A_{0,2}^s)\to D(L_2^s)`$ is established for the required $`s=1/8`$ without assuming the disputed calculus.

## Negative endpoint and compatibility

**Lines 833–848.** The strong retraction

```math
\widetilde Q_{p'}=A_{0,p'}^{-1}\mathbb P_OL_{p'}
:D(L_{p'})\longrightarrow D(A_{0,p'})
```

is bounded and fixes the solenoidal strong domain. For

```math
Z_{A,p}=D(A_{0,p'})^*,\qquad Z_{\Delta,p}=D(L_{p'})^*,
```

define

```math
\langle\mathcal J_p\ell,v\rangle
=\langle\ell,\widetilde Q_{p'}v\rangle.
```

This bounds $`\mathcal J_p:Z_{A,p}\to Z_{\Delta,p}`$. On base functions, adjointness and integration by parts identify this transpose with the original $`L_pi_pA_{0,p}^{-1}`$. It is therefore an extension of the chosen lift.

The domain inclusion $`D(A_{0,p'})\subset D(L_{p'})`$ permits extension of the projection by restriction of functionals. For every strong solenoidal test field $`v`$,

```math
\langle\mathbb P_O\mathcal J_p\ell,v\rangle
=\langle\ell,\widetilde Q_{p'}v\rangle
=\langle\ell,v\rangle.
```

Thus $`\mathbb P_O\mathcal J_p=I`$ on the negative space. Common elliptic solutions and their distributional formulas give compatibility across $`p=2,8,8/7`$. The necessary strong-domain inclusion uses the same zero velocity trace on both realizations.

## Projection images

**Lines 851–862.** Interpolation of the Hilbert retraction's base and strong-domain bounds gives $`\widetilde Q_2:D(L_2^s)\to D(A_{0,2}^s)`$. Independently, reflected Helmholtz projection is bounded on $`H^{2s}`$ for $`2s<1/2`$.

For $`f\in D(L_2^s)`$, it follows that $`\mathbb P_Of\in D(L_2^s)`$. The base identity $`\widetilde Q_2\mathbb P_O=\mathbb P_O`$ then places $`\mathbb P_Of`$ in $`D(A_{0,2}^s)`$. This supplies the justification behind the terse image argument at line 856. The positive right inverse proves surjectivity. The negative image follows directly from the explicit transpose construction. Neither argument assumes the Banach-space calculus being established.

## Inversion, interpolation and calculus angle

**Lines 864–880.** Passing to inverse operators reverses fractional signs. Hence $`\alpha=-1/8`$ corresponds to the original positive $`1/8`$ domains, while $`\beta=1`$ corresponds to the original negative full-step completions. Invertibility identifies those completions with the dual strong-domain spaces used above, with equivalent norms. The endpoint assignments are correct.

The ambient $`L^p`$ couples are reflexive and B-convex; compatible Helmholtz projections identify their interpolated solenoidal spaces. At $`\theta=2/3`$,

```math
\frac{1-\theta}{2}+\frac{\theta}{8}=\frac14,
\qquad
\frac{1-\theta}{2}+\frac{\theta}{8/7}=\frac34.
```

The corrected theorem therefore yields calculus on $`H_4`$ and $`H_{4/3}`$. Scalar inverse calculus and Stokes R-sectoriality follow from their original-operator versions. Inversion then transfers the resulting Stokes calculus back.

Only after existence of calculus is established does the manuscript identify its angle with the almost-R-sectorial angle. That angle comparison, combined with the previously proved R-sectorial angle zero, gives an angle below $`\pi/2`$. The invocation is correctly ordered. [Kalton–Kunstmann–Weis (2006), Corollary 4.4, p. 758](https://kaltonmemorial.missouri.edu/assets/docs/ma2006.pdf).

## Consequence and scope

The new estimates supply the channel isotropic calculus at both exponents required by the weak scale and additive stochastic channel argument, **lines 882–924**. The former missing-hypothesis objection no longer blocks that dependency chain. The repair introduces no extra noise-amplitude smallness, forcing wall trace, restriction of smooth physical domains, or weakening of the requested path topology.

This finding concerns the repaired input and its stated interfaces. A complete acceptance decision also requires the remaining flat-model, localization, linear construction and nonlinear arguments to be covered by the full proof review. The earlier independent uniqueness result remains available in its original scope. The historical PR 171 report should continue to record the earlier gap, accompanied by the dated finding that the missing hypothesis is now supplied.
