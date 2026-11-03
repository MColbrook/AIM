# AIM 1028: final review and scope

**Author and submitter:** Matthew J. Colbrook.

**Disposition:** Partially resolved — checked partial progress.

**Reviewed:** 3 November 2026, by Codex (AI). An independent reviewer read the complete argument; the coordinator checked the target mapping, applied the editorial corrections, verified the final manuscripts and repository consistency, and independently audited the torus and Heun arguments. This does not assert human peer review or Lean verification.

**Proof:** [Standalone manuscript](../../solutions/1028-eigenvalue-torsion-upper-constant/aim1028.pdf), [TeX](../../solutions/1028-eigenvalue-torsion-upper-constant/aim1028.tex), and [source receipt](../../solutions/1028-eigenvalue-torsion-upper-constant/SOURCE_RECEIPT.json).

**Target:** [Current AIM 1028](../../../problems/1028-sharp-convex-polya-functional-bounds-in-dimensions-three-and-higher.md) at base `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Its Problem statement is preserved.

The sharp convex upper constant pi squared over twelve is established in every dimension; the lower constant remains open.

**Remaining target:** Prove or disprove the proposed lower constant $`\inf F=\pi^2/[2(d+1)(d+2)]`$ for every $`d\ge3`$. The appended lower-route obstruction concerns test functions that are not torsion functions and is not a counterexample to this target.

The editorial and citation refinements recommended below have been applied. They do not change the construction or the claimed theorem. This record distinguishes each proved theorem from the full catalogue question.

# AIM 1028: independent mathematical audit

Date: 2026-11-03. Reviewer: Codex AI, geometric-constants review lane C. This is an independent AI audit, not human peer review or proof-assistant verification.

Canonical revision inspected: `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Authoritative target: `problems/1028-sharp-convex-polya-functional-bounds-in-dimensions-three-and-higher.md` and row 1028 in `data/spectral.json`. Both complete forms of the supplied argument, `submission/sections/1028.md` and `.tex`, were read, as was `submission/notes/1028_lower_bound_obstruction.md`. TeX SHA-256: `64de75a7ef9bbd795b49eae3a06837575aba7176d33aedba1928f92718944c74`.

## Verdict and exact scope

**PARTIAL: the sharp upper constant is proved in every dimension d>=2, including all d>=3 required by the canonical entry. No substantive mathematical gap found.** For each individual nonempty bounded open convex domain,

lambda_1 T/|Omega| < pi^2/12,

and the supremum over that class is pi^2/12. The proof does not establish the proposed lower constant pi^2/[2(d+1)(d+2)] for d>=3. Keep the combined entry `Partially resolved`.

Recommended catalogue scope:

- Known cases: the sharp upper constant pi^2/12 is established for all d>=3, is not attained by a bounded convex domain, and is approached by elongated boxes. The prior planar result is outside the residual dimension range but can remain as context.
- Remaining target: prove or disprove that the convex infimum equals pi^2/[2(d+1)(d+2)] for every d>=3.

Attribution is essential: the one-dimensional proof is Deng's Section 5 mechanism. The manuscript correctly supplies an explicit dimension check and geometric proof rather than attributing an all-dimensional theorem statement to Deng.

## Proof checks

1. **All-dimensional torsion-perimeter input.** Inner parallel bodies remain convex, V'=-P(s) a.e., and surface area is monotone for nested convex bodies in every dimension. For 0<s<r, D_s+sB is contained in D, and adding a positive-radius ball strictly increases the surface area of a convex body with interior when d>=2. Thus P(s)<P. The proposed web function is Lipschitz, has zero boundary trace, and its two variational quantities both equal integral V(s)^2/P(s) ds. The substitution v=V(s) gives the strict inequality T(D)>V^3/(3P^2). No planar perimeter formula is used here.

2. **Convex and regular torsion levels.** Kennington's square-root concavity is available in R^d. A segment of maximizers would make u constant on that segment, and real analyticity restricted to the entire interior chord would contradict continuous zero boundary values at its endpoints. The maximum is therefore unique. At any critical point of u, the concave differentiable function sqrt(u) has horizontal tangent plane, so that point is a global maximizer. Consequently every intermediate level is a compact smooth hypersurface inside Omega, including when the original convex boundary is nonsmooth. This justifies the flux and coarea steps without assuming smoothness of the original domain.

3. **Scale cancellation.** The level domain has volume A S and torsion A M I. The exact inequalities are

   P_t^2 <= (A^2/M) S(-S'),
   A M I > A^3 S^3/(3P_t^2).

   Combining them gives I(-S')>S^2/3. The cancellation is correct in arbitrary d; perimeter has not been normalized by a dimension-specific square root. Differentiation then gives (I^(2/3))''>0.

4. **Moment factor and strictness.** The endpoint data are I(0)=Phi, I'(0+)=-1, I(1)=0. The tangent inequality gives Phi<=2/3 and integral I>3Phi^2/5, hence T^2/(A integral u^2)<5/6. Strictness survives for an arbitrary bounded convex domain because the strict web inequality was applied to the smooth interior superlevels. An outer-approximation argument alone would only preserve a weak inequality; it is not needed for this strictness step.

5. **Weighted change of variables.** Differentiation of I=Phi y^3 gives dt/dy=-y/a and S=3Phi ya. Convexity with reversed orientation makes a nondecreasing. The Stieltjes measure transformation has the correct orientation. The numerator and denominator in the trial quotient each acquire the same factor 3Phi, and m2/m1=2 integral y^4/a. The original-coordinate trial H is Lipschitz since H'=sin(pi y/2)/y<=pi/2, so there is no hidden endpoint admissibility problem when a(0)=0.

6. **One-dimensional weighted inequality.** I independently differentiated the displayed R and G. The identities R'=r and G'''=z(sin z-z cos z) are correct. Three integrations from zero give G>=0, hence q is decreasing and R>=0. With w=1/a decreasing, integral r w=-integral R dw>=0. The endpoint estimate y^2 w(y)/2<=integral_0^y s w(s) ds establishes the required vanishing boundary term. Also r=O(y^4), which is integrable against w since integral y w=1. Thus the denominator bound and the factor pi^2/10 follow. Multiplication with the strict 5/6 factor gives exactly pi^2/12.

7. **Sharpness.** The box eigenvalue formula is exact. Each summand of the harmonic barrier has Laplacian zero, and the boundary domination is correct. More explicitly, one may choose C=1/4: concavity of sin on [0,pi/2] gives sin(pi y)>=2 min(y,1-y), so w(y)<=sin(pi y)/4. Direct integration then gives

   0 <= 1/12-T(Omega_L)/|Omega_L|
      <= (d-1)/(pi^2 L) tanh(pi L/2).

   This independently verifies the claimed O(1/L) asymptotic and the sharp supremum in every fixed dimension.

## Lower-bound obstruction note

The note's conclusion is appropriately limited. The 2018 torsion-efficiency estimate specializes to 2/[d(d+2)], not 1/[d(d+2)], and together with lambda_1 M>=pi^2/8 gives pi^2/[4d(d+2)]. The proposed lower target exceeds that by the factor 2d/(d+1).

The independent calculus check of v_L is successful. At r=2/L, its values are 1-2/L^2 and its derivatives are -2/L on both sides. The square-root radial derivatives also match and are nonincreasing; the tangential Hessian eigenvalues are nonpositive. The gradient inequality holds with equality inside and the stated upper bound outside. The normalized integral tends to the beta integral 2/[(d+1)(d+2)], exactly half the proposed efficiency target. The displayed nonconstant and partly negative -Delta v_L is correct. Therefore this is an obstruction to a proof using only the two listed shape inequalities, not a counterexample involving actual torsion functions.

The Payne supersolution calculation also checks: p'>0, p''>0 and p'-2(M-t)p''=(pi^2/(8M))p. For a nonsmooth convex domain the cited smooth-domain gradient bound can be extended by smooth convex approximation and interior C1 convergence, with maxima controlled by a scaling sandwich. Add this standard approximation sentence if the lower-bound discussion is promoted into the standalone manuscript.

## Verified primary references

- [Deng, arXiv:2609.13221v1](https://arxiv.org/html/2609.13221v1), Section 5: Lemma 5.1, coordinate equations (58)-(64), Lemma 5.2, and Proposition 5.3 were read through the final factorization. The stated theorem is planar. The supplied all-dimensional extension has been checked above and should retain this distinction. Section 4 uses planar Airy stresses and mixed area for the lower bound; that is not an all-dimensional input.
- [Amato, Masiello, Paoli and Sannipoli](https://link.springer.com/article/10.1007/s00030-022-00822-y), *NoDEA* 30 (2023), article 12, Theorem 1.1 and the normalization preceding it: n>=2, f=1, p=q=2 gives T>=|Omega|^3/(3P^2). The more quantitative Theorem 1.2 also confirms strictness for any fixed convex domain. The paper's dimension restriction and normalization match the manuscript.
- [Kennington, DOI 10.1512/iumj.1985.34.34036](https://doi.org/10.1512/iumj.1985.34.34036), *Indiana University Mathematics Journal* 34(3) (1985), 687-704. The precise input is **Theorem 4.1(ii)**, pp. 695-696, valid for bounded convex domains in R^n, n>=2, with positive constant forcing. The original theorem and its approximation paragraph were checked in the [primary paper copy](https://math.jhu.edu/~js/Math646/kennington.pdf). Add this theorem locator and DOI to the manuscript.
- [van den Berg, Buttazzo and Pratelli, arXiv:1910.14593v2](https://arxiv.org/html/1910.14593v2), Conjecture 4.2: both constants and the full convex dimension-dependent target match. Correct the bibliographic title to *On the relations between principal eigenvalue and torsional rigidity* (insert "the"). The listed 2021 journal citation and [DOI 10.1142/S0219199720500935](https://doi.org/10.1142/S0219199720500935) are the cited version of record.
- For the supplemental lower note, [Della Pietra, Gavitone and Guarino Lo Bianco, arXiv:1705.03330v1](https://arxiv.org/html/1705.03330v1), Theorems 1.1(i), 3.2 and 4.2, Remark 4.6, support the claimed estimates. Theorem 3.2 initially assumes a bounded C2 domain with nonnegative anisotropic mean curvature; convex-domain approximation handles the general convex class. [Briani and Bucur](https://link.springer.com/article/10.1007/s00526-023-02530-6), Remark 5.2, confirms the same p-torsion bound and its unresolved sharp lower constant at that publication date.

## Dated search and integration

On 2026-11-03 I checked the current arXiv records for Deng and searched `Polya functional higher dimensions upper bound 2026`, `Polya functional upper bound dimension 2026 convex`, and `Polya functional higher-dimensional 2026`. No matching complete higher-dimensional lower-bound resolution was located. This is a bounded search, not a proof that no such work exists, and no novelty claim is certified.

Accept the all-dimensional upper theorem as a checked partial advance, retain attribution to Deng, and narrow the remaining target to the lower constant. No mathematical repair to the upper-bound argument is required. The theorem locator, article-title correction and optional approximation sentence are editorial/completeness improvements.
