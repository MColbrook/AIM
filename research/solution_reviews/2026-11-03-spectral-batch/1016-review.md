# AIM 1016: final review and scope

**Author and submitter:** Matthew J. Colbrook.

**Disposition:** Partially resolved — checked partial progress.

**Reviewed:** 3 November 2026, by Codex (AI). An independent reviewer read the complete argument; the coordinator checked the target mapping, applied the editorial corrections, verified the final manuscripts and repository consistency, and independently audited the torus and Heun arguments. This does not assert human peer review or Lean verification.

**Proof:** [Standalone manuscript](../../solutions/1016-inradius-critical-asymptotics/aim1016.pdf), [TeX](../../solutions/1016-inradius-critical-asymptotics/aim1016.tex), and [source receipt](../../solutions/1016-inradius-critical-asymptotics/SOURCE_RECEIPT.json).

**Target:** [Current AIM 1016](../../../problems/1016-the-sharp-inradius-bound-for-superhomogeneous-dirichlet-frequencies.md) at base `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Its Problem statement is preserved.

The critical large-q asymptotic is determined uniformly over convex domains; a separate explicit supremum-norm lower bound holds for p at least N+1.

**Remaining target:** Determine the exact optimal constant at fixed finite parameters and in the other admissible regimes. The supremum-norm bound is not proved sharp and does not cover $`N<p<N+1`$.

The editorial and citation refinements recommended below have been applied. They do not change the construction or the claimed theorem. This record distinguishes each proved theorem from the full catalogue question.

# AIM 1016: independent mathematical audit

Date: 3 November 2026. Reviewer: Codex AI, lane b. Author and submitter: Matthew J. Colbrook. This is independent AI mathematical checking, not human peer review or formal verification.

Repository target inspected at HEAD 3fa50884d129a08fec3c09cb4765e8ecad97d6ee: problems/1016-the-sharp-inradius-bound-for-superhomogeneous-dirichlet-frequencies.md and the ID 1016 row of data/spectral.json. Supplied source snapshot: b014a51815ffd025d2b1abc4a3954205dfbf61e0.

## Verdict and target match

**PASS for both stated partial results; NOT a complete resolution of AIM 1016.**

The current target asks for the exact optimal shape constant for all admissible N,p,q with q>p. The submission proves:

1. For p=N and finite q tending to infinity,

```math
\lim_{q\to\infty}q^{N-1}C_{\mathrm{opt}}(N,N,q)
=|S^{N-1}|\left(\frac{eN^2}{N-1}\right)^{N-1}.
```

2. For q=infinity and p>=N+1, the explicit universal lower bound

```math
C_{\mathrm{opt}}(N,p,\infty)\ge
2\left(\frac{p-N}{p-1}\right)^{p-1}
\frac{\pi^{(N-1)/2}\Gamma((p-N+1)/2)}{\Gamma(p/2)}.
```

Neither assertion determines an exact constant at a fixed finite q. The second is not claimed sharp and has no matching optimizer or upper construction. Keep the current entry **Partially resolved** and preserve its ID, with nonempty Known cases and Remaining target notes as required by CONTRIBUTING.md.

## Critical-exponent argument

### 1. Scaling and boundary hypotheses

For p=N the shape exponent is N^2/q, exactly as in the current page. Dilation to ordinary Euclidean inradius one is legitimate. For every bounded open convex set, d(x)=dist(x,boundary Omega) is concave, 0<d<=1, and |grad d|=1 almost everywhere. No smooth boundary assumption is needed.

The distributional divergence inequality used for Hardy is valid. For full precision, use the locally BV vector field grad d/(d+epsilon)^(N-1), whose singular divergence part is nonpositive because d is concave. Its absolutely continuous part is at most -(N-1)/(d+epsilon)^N. Test against |u|^N with compact support and let epsilon decrease to zero.

Integration by parts and Holder give

```math
(N-1)\int |u/d|^N
\le N\left(\int |u/d|^N\right)^{(N-1)/N}\|\nabla u\|_N.
```

This proves the claimed Hardy estimate and the uniform bound

```math
\|u\|_N^N\le [N/(N-1)]^N\|\nabla u\|_N^N.
```

All constants are independent of volume and diameter, including degenerating long convex sets. This uniformity is essential because the infimum over shapes is taken before the q limit.

### 2. Adachi-Tanaka input

The exact subcritical whole-space inequality quoted is valid for every N>=2:

```math
\int_{\mathbb R^N}\Phi_N\left(\alpha |u/\|\nabla u\|_N|^{N/(N-1)}\right)
\le A_{N,\alpha}\frac{\|u\|_N^N}{\|\nabla u\|_N^N},
\quad 0<\alpha<N|S^{N-1}|^{1/(N-1)}.
```

The submission uses it only at a fixed strictly subcritical alpha and normalized gradient one. Zero extension of a C_c-infinity domain test is a permissible whole-space Sobolev function. Combining with Hardy supplies one bound uniform over all normalized convex domains. The proof does not make an unsupported use of the critical endpoint alpha=alpha_N.

### 3. Moments and the real-q limit

The mth nonnegative term in Phi_N is present for every integer m>=N-1. Retaining it gives

```math
\int |u|^{N'm}\le D\,m!\,\alpha^{-m},
\qquad D=A_{N,\alpha}[N/(N-1)]^N.
```

After taking the power (N-1)/m and reciprocating, the displayed lower bound for C_opt is correct. Stirling gives

```math
\liminf_m(N'm)^{N-1} C_{\mathrm{opt}}(N,N,N'm)
\ge (eN'\alpha)^{N-1}.
```

For q between the moment exponents, choose r=N'ceil(q/N'). Interpolation with the uniform L^N bound has

```math
\theta=\frac{N(r-q)}{q(r-N)}=O(q^{-2}).
```

The logarithm of the upper bound for the normalized L^r norm is O(log q); multiplying it by theta changes the asymptotic by o(1). Also r/q tends to one. Thus the same lower limit holds along all real q, uniformly over all shapes and tests. Taking alpha up to alpha_N only after that limit is valid.

The numerical coefficient simplifies to

```math
(eN'\alpha_N)^{N-1}
=|S^{N-1}|\left(\frac{eN^2}{N-1}\right)^{N-1}.
```

In particular N=2 gives 2pi times 4e, namely 8pi e. I found no missing N or factor of two.

### 4. Matching upper test and admissibility

The logarithmic Moser test has derivative magnitude |S^(N-1)|^(-1/N)L^(-1/N)/r on the annulus. Radial integration gives energy exactly L^(-1) times the logarithmic interval length L, hence one. Its inner plateau yields

```math
C_{\mathrm{opt}}\le
\sigma_{N-1}(N/\sigma_{N-1})^{N/q}
\exp(N^2 L/q)L^{-(N-1)}.
```

Minimizing this expression in L gives L=(N-1)q/N^2, reproducing the lower coefficient. The test is in W_0^(1,N) of the unit ball. For each finite q, smooth approximation is valid in that space and in L^q by the critical Sobolev embedding on the ball. No uniform approximation in q is required. The infimum over all convex shapes is at most the value obtained from the unit ball, so this is the correct direction of comparison.

## Additional supremum-norm bound

### 1. Supporting-plane balance

Boundedness ensures an incenter exists. At an inradius-one incenter, zero belongs to the convex hull of the unit contact normals: otherwise strict separation supplies a small displacement increasing every active support distance, while continuity and compactness protect the nonactive directions. This would produce a larger ball. Caratheodory supplies at most N+1 contacts with positive weights after zero weights are discarded.

For any maximum point x_* of the compactly supported test, all a_i=1-n_i dot x_* are positive, and

```math
\sum\lambda_i a_i=1,\quad
\rho_i=\lambda_i a_i,\quad
\sum\rho_i=1,\quad
\sum\rho_i v_i=0,\quad v_i=n_i/a_i.
```

The maximum is not assumed to occur at the incenter. This change of weights correctly avoids that common error.

### 2. Support-function inequalities

Let s=p-N>=1. Mean zero places zero between -B and A. The chord bound for the convex function |x|^s gives

```math
\sum\rho_i |X_i|^s
\le\frac{AB^s+BA^s}{A+B}
\le \frac{A^s+B^s}{2}.
```

The last difference has the sign of (A-B)(A^s-B^s), so its direction is correct. Sphere integration, followed by Jensen for a^(1-s), gives

```math
\int_{S^{N-1}}h^s
\ge\kappa_{N,s}\sum\lambda_i a_i^{1-s}
\ge\kappa_{N,s}.
```

The beta integral is

```math
\kappa_{N,s}
=2\pi^{(N-1)/2}\Gamma((s+1)/2)/\Gamma((N+s)/2).
```

This argument permits the supporting polyhedron to be unbounded; directions where h=0 cause no problem. The condition s>=1 is genuinely used, so the stated restriction p>=N+1 must be retained.

### 3. Radial energy and the example

Convexity makes Omega star-shaped about x_* and supplies R(omega)<=1/h(omega). The compactly supported test vanishes before exiting the domain. Weighted Holder along each ray gives

```math
\int_0^{R(\omega)} |\partial_r f|^p r^{N-1}\,dr
\ge [(p-N)/(p-1)]^{p-1}M^p R(\omega)^{N-p}.
```

Since N-p=-s, the exit-length comparison bounds this below by the same coefficient times M^p h^s. Polar integration and the support-function estimate prove the stated lower bound.

For N=2,p=4, kappa_(2,2)=pi and [(p-N)/(p-1)]^(p-1)=8/27, giving exactly 8pi/27.

Angular derivatives were discarded, so equality in the support-function calculation alone would not prove sharpness for the original functional. The submission correctly makes no such inference.

## Gaps and remaining target

No fatal mathematical gap was found in either restricted result. No extra boundary regularity should be added to the canonical problem: the distance-function and supporting-plane arguments work for the given bounded open convex class.

The exact value of C_opt at finite q, the other p regimes, and sharpness even in the covered q=infinity regime remain unsettled by this manuscript. The range N<p<N+1 is outside the second argument. A correct asymptotic must not be promoted to a full exact-constant solution.

Optional exposition refinement: at the Hardy step, explicitly keep the distributional interpretation when using d+epsilon; merely adding epsilon does not make d smooth. The inequality itself is valid.

## Verified primary sources and current-relevance check

- Adachi-Tanaka, [1999 primary manuscript](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1102-11.pdf), Theorem 0.1, printed p. 149, PDF p. 2; alpha_N is defined on printed p. 148. This is exactly the normalized whole-space estimate needed. Theorem 0.2 on p. 150 excludes the endpoint, which the submission does not use. The 2000 journal [DOI](https://doi.org/10.1090/S0002-9939-99-05180-1) was not directly fetchable in the web tool; the earlier primary full theorem was read.
- Brasco, [published primary text](https://mathematicalanalysis.unibo.it/article/download/8945/8866/28804), Proposition 6.3 and equation (15), printed p. 99, and Open problems 1, p. 100. The target is the sharp constant in the superhomogeneous inradius inequality, not a volume- or perimeter-corrected functional. [DOI](https://doi.org/10.6092/issn.2240-2829/8945).
- Bozzola-Brasco, [primary author manuscript](https://cvgmt.sns.it/media/doc/paper/6357/bozbra_final.pdf), Corollary 3.8, pp. 17-18, includes the fixed planar-domain large-q limit q lambda_(2,q)(Omega)=8pi e for its finite-inradius topology class. This is relevant prior asymptotic context. A fixed-domain statement alone does not permit exchanging the q limit with an infimum over all convex domains; the supplied uniform Hardy/Adachi-Tanaka argument supplies that missing uniformity.
- Pisante-Prinari, [2026 primary text](https://arxiv.org/html/2604.11973), Theorem 1.1 and Section 1.4: its sharp Makai-type lower bound assumes q<p and uses perimeter and volume. Its q<=p geometric discussion does not determine the present ordinary-inradius-only superhomogeneous constant.
- Brasco-Briani-Prinari, [March 2026 primary author manuscript](https://cvgmt.sns.it/media/doc/paper/7123/brabripri_steiner_final_rev.pdf), main result and Appendix A, studies existence of extremals on prescribed Steiner symmetric domains, including q=infinity. It does not provide the requested shape infimum over every bounded convex domain.

Bounded searches on 3 November 2026 covered the precise sharp-inradius superhomogeneous question, large-q/Moser asymptotics, the 8pi e limit, and recent Poincare-Sobolev shape bounds. No full matching determination of C_opt over the entire parameter range was found. No bibliographic priority claim is made for either partial result.

## Standalone reference completion

The final manuscript explicitly cites the original problem source. For AIM 1016 it also credits the known fixed-domain planar asymptotic, with the published and author-version numbering kept distinct. These additions do not change the proof or verdict.
