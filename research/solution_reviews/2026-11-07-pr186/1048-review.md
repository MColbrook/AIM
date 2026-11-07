# AIM 1048: independent mathematical review of PR #186

**Date:** 7 November 2026. **Reviewer:** Codex (AI), in a separate maintainer review from the submission workflow. **Decision:** Solved, affirmative resolution of the complete recorded target. No human peer review or formal verification is claimed.

[Problem](../../../problems/1048-can-neighboring-water-wave-bloch-bands-overlap.md) · [Proof PDF](../../solutions/siavash-sadeghi-1048/research_nonoverlap_proof.pdf) · [Proof source](../../solutions/siavash-sadeghi-1048/research_nonoverlap_proof.tex) · [PR #186](https://github.com/MColbrook/AIM/pull/186).

## Revision, scope and independence

Reviewed submission: `e9e846b886ada1710f4bfd1b40213b4b34eb0bff`. Current main used for integration: `cfcb114`. The supplied target snapshot pins `4f5b1659355cb61d194da94ef14615214e1363a8`; the current mathematical target is unchanged. Proof-source SHA-256: `cf679519556de61fb2e30caff19e49b8b078e7f308adbc11e5b94ae56e9e4e8f`.

I read the complete six-section proof and independently checked its construction and comparison argument. I subsequently compared the supplied audits and review guide. Their verdicts were not used as a substitute for checking the proof; this review was not fully blind, since the PR description and submission review were available. No additional agent team or human review was commissioned.

The argument covers every real periodic C¹ graph bottom of positive depth, the exact harmonic-extension Dirichlet–Neumann operator with zero bottom Neumann data, and physical surface mass dx. For every n >= 0 and every two phases it proves Lambda_n(theta_a) <= Lambda_(n+1)(theta_b), with eigenvalues ordered separately in each fiber and counted with multiplicity. Phase continuity makes this precisely the catalogue's max–min nonoverlap inequality. No smallness, parity, zero-mean, simple-eigenvalue or fundamental-period condition has been added. Touching is allowed. Endpoint localization, monotonicity and strict opening of gaps are separate questions.

## Checks of the complete argument

1. **Representation and energy.** Set k=m+theta and u_m=cosh(dk)v_m. Reflection of the holomorphic V across the middle line gives the complex harmonic extension with the required zero normal derivative. Direct integration for one Fourier mode gives Q=(P/2)k sinh(2dk)|v_m|²=P k tanh(dk)|u_m|². The zero-frequency contribution has energy zero and reconstruction multiplier one. Fourier truncation gives the stated H¹ analytic representation and H^(1/2) edge traces. Positive bounded mass and compact trace embedding justify the closed-form spectral realization.

2. **Complex mass identity.** In the cross term, k_n-k_m=n-m; the phase cancels. Conjugation and index interchange replace exp(d(n-m)) by cosh(d(n-m)), which converts rho_(n-m) to p_(n-m). Thus it is the real part of the cross integral, not the unsymmetrized integral, that equals the middle-line mass. This works for complex coefficients and non-even real weights. Bounded weights and L² trace convergence justify the passage from finite Fourier sums.

3. **Strip factor and character.** The disk automorphism has its only simple zero at iy. Its normalized product tails differ from one by O(exp(-2cjP)), uniformly on fixed compact sets extending through the edges; the summability proves a nonzero limit away from the prescribed zero lattice, not merely a bounded limit. Reindexing the symmetric product gives b_+/b_-=exp(i*pi*(1-y/d)). Hence division subtracts chi=(1-y/d)/2. Every nontrivial unitary character occurs for an interior y; coincident characters are handled by ordinary ordering. No uniform edge estimate as y approaches +/-d is needed.

4. **Admissible division and quotient direction.** Finite Fourier input V vanishing at one chosen zero vanishes at every translated zero. V/B therefore extends holomorphically across those apparent poles and is smooth through both edges. Reconstruction is injective because cosh(dk)>0. Equal edge moduli and p>0 give M(W)>=M(V). Independently, Delta|F|²=4|F'|² gives Q(F)=(1/8) times the boundary normal flux. The horizontal flux difference is 2 beta |W|², yielding exactly Q(V)-Q(W)=(1/4) sum integral beta |W|²>=0. Squared moduli are periodic, so lateral fluxes cancel even for distinct characters. The Rayleigh quotient can only decrease.

5. **Ordered min–max.** Approximate a basis of the first n+2 eigenvectors in the source fiber in H^(1/2). Convergence of the energy and mass Gram matrices preserves dimension and the upper quotient bound. One complex evaluation constraint removes at most one complex dimension. Division and reconstruction preserve the remaining dimension, giving at least n+1 target directions with quotient at most Lambda_(n+1)(theta_b)+epsilon. This is the correct index and comparison direction. Multiplicity requires no branch tracking. The argument fixes n and both phases before approximation and never divides an arbitrary rough trace.

6. **Physical geometry.** The exponential quotient of an analytic graph channel is an annulus with disjoint regular analytic boundary curves. Its conformal uniformization lifts with horizontal degree +1 and unchanged period. Local analytic reflection applies to the map and inverse, giving nonzero boundary derivatives. Writing the bottom derivative as X'(s)(1+i b'(X(s))) shows X' cannot vanish; its period integral is P, so X'>0. The same argument gives rho=Z'>0 on the top. Reality of the top derivative gives p_k=cosh(dk)rho_k. Thus the essential positivity of p is forced by graph geometry, not incorrectly inferred from an arbitrary positive rho. Conformal invariance preserves energy and zero Neumann data; surface mass is exactly dx=rho ds. Periodic densities make the choice of period-cell sides immaterial.

7. **C¹ limit and band extrema.** Recomputing y=H(x)z gives the matrix with entries H, -zH', and (1+z²H'²)/H; its determinant is one. C¹ approximation with a common positive depth gives uniform ellipticity and relative form comparison, uniformly for all covariant gradients. Infimizing over the same top-trace competitors and then applying min–max passes the ordered inequality to every stated C¹ graph. The vertical bulk-L² estimate, followed by the phase perturbation estimate with an added top mass, gives continuity of every ordered eigenvalue. Compactness of the phase circle gives attained extrema. Flat-bottom bands may touch at a common character, consistently with the non-strict conclusion.

No necessary mathematical repair or unresolved part of the canonical target was identified. The original proof source and both supplied PDFs are retained unchanged.

## Primary references and dated search

- [Craig, Gazeau, Lacave and Sulem, arXiv:1706.07417v2](https://arxiv.org/html/1706.07417v2), introduction after Definition 1.1; [published DOI](https://doi.org/10.1137/17M113561X), SIAM J. Math. Anal. 50(5) (2018), 5477–5501. The formulation distinguishes nonoverlap from locating band edges. The bibliographic data agree with the publisher.
- [Lacave, Ménard and Sulem, primary publisher PDF](https://ems.press/content/serial-article-files/50748), Section 4, printed p. 270; [DOI](https://doi.org/10.4171/EMSS/93), EMS Surv. Math. Sci. 12(1) (2025), 243–288. This develops perturbative gaps; its opening discussion does not supply the full general ordering theorem.
- Ahlfors, *Complex Analysis*, third edition, McGraw–Hill (1979), Chapter VI, Section 5.1, Theorem 10, printed pp. 255–256; Sections 1.3–1.4, Theorems 3–4, pp. 233–235. The [primary book scan](https://www.matem.unam.mx/~hector/%5BLars_Ahlfors%5D_Complex_Analysis_%28Third_Edition%29.pdf) was checked. Connectivity two leaves no circular slits; analytic boundary extension uses the local reflection argument, rather than applying a globally simply connected theorem verbatim to an annulus.
- Kato, *Perturbation Theory for Linear Operators*, second edition, corrected printing, Springer (1980), Chapter VI, Theorem 2.1 and its symmetric specialization, Theorem 2.6. The [primary book text](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kato1.pdf) supports the closed-form operator realization. The submitted proof supplies its own compact embedding, min–max dimension argument and phase estimates.

These are the background inputs actually needed; no missing substantive external theorem was identified. Searches on 7 November 2026 for the water-wave Bloch nonoverlap question and later resolutions, together with the primary-source comparisons above, found no conflicting matching resolution. This is a bounded check, not an exhaustive priority claim. Historical submission searches remain dated evidence of their own coverage.

## Reproduction and package checks

On Windows, Python 3.12.14 and NumPy 2.3.5:

```sh
python -B fresh_audit_diagnostics.py
python -B -O fresh_audit_diagnostics.py
python -B -m unittest test_diagnostics.py
python -B -O -m unittest test_diagnostics.py
```

All 21 diagnostic cases passed in both modes; all five regression tests passed in each mode, including negative controls and non-finite input. Both reruns produced the same results as each other. Results differ from the supplied JSON at floating-point roundoff level; exact JSON equality across numerical environments is not claimed. Maximum rerun relative mass-identity error: 2.81e-16; output mass-identity error: 4.21e-16; energy-identity error: 8.81e-15. The retained deep-strip bottom-relative reconstruction error reaches 2.53e-7, so these are diagnostics, not an interval proof or formal certificate. The top-relative reconstruction criterion also passed.

Both TeX documents compiled twice with `pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error`, into a temporary build directory. Their extracted PDF text matches the supplied PDFs after whitespace normalization. All six proof pages and four review-guide pages were rendered and inspected; no clipping or missing mathematical content was found. There are three harmless underfull-box warnings and no overfull boxes or compilation errors. Supplied PDFs were not replaced by machine-dependent rebuilds.

The original manifest's 22 entries all matched byte counts and SHA-256 hashes before editing. Integration only adds a current-status notice to the package README and updates that manifest entry; historical reports and the mathematical sources remain unchanged. See the [verification record](verification.json) for machine-readable results. Generated catalogue checks and final changed-path checks cover the integrated tree. The three local working folders FURTHER_problems, PROBLEM_SCORING and cut_problems are excluded from this change and from publication.
