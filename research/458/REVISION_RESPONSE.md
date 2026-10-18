# AIM458: response to the 15 October 2026 review

Revision: 19 October 2026. Author: Kaiwen Jin.

The [review of PR171](../solution_reviews/2026-10-15-active-prs/458-review.md) correctly identified a missing hypothesis. The old argument checked fractional projection images but did not establish the compatible fractional right inverses required by Kunstmann--Weis (2013), Theorem 1.3. This is a substantive repair; adding an erratum citation alone would not suffice. The revised manuscript supplies the estimates and requests renewed independent review of the complete claim. The historical review remains unchanged.

## 1. Correct the theorem signature

Section 3.3 now states both projection-image identities (3.19) and the compatible right-inverse estimates (3.20), following the [2013 author erratum, Theorem 1.3, p.802](https://kaltonmemorial.missouri.edu/assets/docs/ma2006a.pdf). The obsolete image-only formulation of 2006 Theorem 8.2 is removed. The corrected physical-domain input is separately cited as the erratum's Theorem 2.1; a smooth physical boundary satisfies its C^(2+mu) assumption for 0<mu<1. That Euclidean theorem is not used directly on the periodic channel.

## 2. Prove the missing channel regularity

Let S_p=-P_O Delta be the **unit-viscosity reference** channel Stokes operator, L_p the componentwise Dirichlet Laplacian, and i_p the inclusion of solenoidal fields. The physical viscosity nu in the original equation is unchanged. Define one compatible family

    mathcal J_p = L_p i_p S_p^{-1}.

The strong-domain bounds from the preceding Fourier argument give its base-space bound and P_O mathcal J_p=I. Lemma 3.1 (PDF p.10, equations 3.22--3.24) supplies the extra regularity:

    ||S_2^{-1} P_O f||_{H3} + ||p||_{H2} <= C ||f||_{H1}.

Tangential difference quotients preserve the channel, wall values and mean-zero pressure. Apply the existing H2 velocity/H1 pressure bound to them. Incompressibility then determines u3_zzz, the normal momentum equation determines p_zz, and the horizontal equations determine uh_zzz. These are distributional identities. No boundary trace is imposed on f, Delta u or p.

## 3. Construct both fractional right inverses

Lemma 3.2 (PDF p.11) performs the endpoint checks before any Banach-space channel calculus is claimed:

| Corrected hypothesis | Actual verification |
| --- | --- |
| Compatible base right inverses | mathcal J_p is bounded on the base space, P_O mathcal J_p=I, and common elliptic solutions give consistency. |
| Positive fractional endpoint | The Hilbert gradient form gives D(S_2^(1/2))=V_2 independently of the disputed Lp calculus. Lemma 3.1 gives mathcal J_2:V_2->H1; interpolate this same operator with its base L2 bound. |
| Scalar fractional target | Odd reflection below the trace threshold gives D(L_2^s)=H^(2s) for 0<s<1/4. Thus mathcal J_2:D(S_2^s)->D(L_2^s). We use s=1/8. |
| Negative full-step endpoint | Dualize the strong retraction S_p'^{-1} P_O L_p'. Its restriction to the solenoidal strong domain is the identity. This gives a consistent right inverse between the dual strong domains. |
| Both onto images | The bounded positive projection plus its right inverse gives the positive image; restriction of dual functionals plus the negative right inverse gives the negative image. |
| Correct signs and interpolation couple | Apply the theorem to L_p^{-1},S_p^{-1}, with alpha=-1/8, beta=1, p0=2 and p1=8 or 8/7. At theta=2/3 the spaces are H4 and H_(4/3). |
| Sectoriality, scalar calculus, consistency | These are supplied by the earlier channel resolvent/multiplier argument and scalar doubled-torus calculus, before applying the comparison theorem. |

The calculus-angle comparison is used only after calculus existence has been obtained. The new right inverse uses mathcal J, distinct from the weak-scale inverse-root map J in Section 2. All constants may depend on the fixed lattice and height; no degenerating-geometry uniformity is asserted.

## 4. Recheck the descendants and preserve the target

The manuscript's abstract and Theorem 1.1 are byte-identical to the previously reviewed version. There is no noise-amplitude smallness assumption, planar interior restriction, smaller class of domains, stronger convergence norm or weaker common-stop conclusion.

The changed input feeds the weak channel scale and additive estimate in Section 3.3, the translation formula in Section 3.4, the localization estimates in Section 4, physical linear construction in Section 5, and nonlinear existence/dependence in Section 6. These were rechecked as one dependency chain. The independent entire-class uniqueness proof in Section 6.2 remains unchanged. The revision includes the actual linear homotopy construction, the full trace estimate and both common-stop probability conclusions; an a priori estimate alone is not substituted for existence.

## 5. Review status and reproducibility

The complete revised argument underwent an author-context natural-language audit, including all internal proof obligations and cited source interfaces. This is a same-context self-review. It is **not** a new independent referee report, human review or Lean verification. The earlier two Codex reader/referee reports concern an earlier version and are not represented as independent validation of these new lemmas.

The 22-page PDF was rebuilt from the submitted TeX, every page was read and visually inspected, and all typed references were checked. The build has no unresolved citations/references or layout warnings. These artifact checks do not establish mathematical correctness. The complete source and PDF, target comparison, manifest and checksums are provided; no private proof archive or orchestration records are included.

Requested action: independently assess the repaired theorem application and its descendants against the unchanged AIM458 target. The historical catalogue decision is retained pending that assessment. Publication of this revision and any PR merge must not themselves be represented as acceptance of the complete result.
