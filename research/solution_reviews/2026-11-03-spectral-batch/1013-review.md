# AIM 1013: final review and scope

**Author and submitter:** Matthew J. Colbrook.

**Disposition:** Solved — Affirmative proof.

**Reviewed:** 3 November 2026, by Codex (AI). An independent reviewer read the complete argument; the coordinator checked the target mapping, applied the editorial corrections, verified the final manuscripts and repository consistency, and independently audited the torus and Heun arguments. This does not assert human peer review or Lean verification.

**Proof:** [Standalone manuscript](../../solutions/1013-multiset-concentration-gap/aim1013.pdf), [TeX](../../solutions/1013-multiset-concentration-gap/aim1013.tex), and [source receipt](../../solutions/1013-multiset-concentration-gap/SOURCE_RECEIPT.json).

**Target:** [Current AIM 1013](../../../problems/1013-spectral-lower-bounds-from-multi-set-concentration.md) at base `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Its Problem statement is preserved.

The stated multiset concentration hypothesis implies a variational spectral gap with an explicit coefficient depending only on the number of sets, without a discrete-spectrum assumption.

The editorial and citation refinements recommended below have been applied. They do not change the construction or the claimed theorem. This record distinguishes each proved theorem from the full catalogue question.

# AIM 1013: independent mathematical audit

Date: 3 November 2026. Reviewer: Codex AI, lane b. Author and submitter: Matthew J. Colbrook. This is an AI mathematical audit, not human peer review or formal verification.

Repository target inspected at HEAD 3fa50884d129a08fec3c09cb4765e8ecad97d6ee: problems/1013-spectral-lower-bounds-from-multi-set-concentration.md and the ID 1013 row of data/spectral.json. Supplied source snapshot: b014a51815ffd025d2b1abc4a3954205dfbf61e0.

## Verdict and exact scope

**PASS: a complete affirmative answer to the current target. No fatal mathematical gap found.**

The proof gives

```math
\lambda^{(k)}\ge\lambda^{(1)}
\ge \frac{a}{64k^2(k-1)^2\log 2}.
```

The constant depends only on k, as requested. The same a, probability normalization, Delta_k condition, prefactor 1-mu(A), and half-separation radius range are used. The argument applies to the complete setting with smooth positive density and Ric+Hess V>=0, including nondiscrete spectrum. It does not replace the target with a compact-manifold or fixed-dimension version.

The proof and this documented AI audit support Solved under CONTRIBUTING.md once integrated, preserving ID 1013.

## Hypotheses of the geometric inputs

The main concerns were attainment of the half-volume isoperimetric problem on a noncompact manifold, singular-boundary normal coordinates, and whether profile concavity needs stronger curvature or compactness. The primary texts support the required finite-measure, smooth CD(0,infinity) statements.

There is one citation-scope distinction to retain: the cited Milman formulations are written for oriented manifolds of dimension at least two. The submission expressly handles dimension one and explains why densities, BV sets and the outward normal of a region remove the orientation requirement. Those extensions should be credited as part of the supplied argument, rather than asserted to be literally in the cited theorem statements.

For completeness, I checked that these extensions work:

- In local charts a positive smooth density is bounded above and below on compact sets. A minimizing sequence with bounded weighted perimeter has BV compactness on each compact set. A diagonal subsequence converges locally in L^1. Since its characteristic functions differ by at most one, finite total measure makes the tail error at most mu(M outside K); this gives global L^1 convergence and preserves the prescribed measure. Lower semicontinuity gives a minimizer.
- The boundary regularity is local for sets of locally finite perimeter. It does not need an orientation of the ambient manifold. The regular boundary of a region has its own globally defined outward unit normal. First and second variation, including their scalar density factors, patch in coordinate charts independently of ambient orientation.
- The inward normal Jacobian calculation and the regular-nearest-point argument are likewise local. Completeness ensures distance minimizers to the closed boundary exist. The complement has nonempty interior up to its null boundary, so every interior point has finite boundary distance.
- Concavity can be obtained through the same weighted second-variation argument using the normal of the region; no ambient volume form is required. Alternatively, the weaker monotonicity of I(v)/v proved by Milman's normal-ray method is already enough for the Cheeger identity used here.

Thus the manuscript's nonorientable extension is justified; imposing orientability or compactness on the catalogue target is unnecessary.

## Reconstruction of the argument

### 1. Cheeger profile

Symmetry is immediate from complementing a finite-perimeter set. For 0<v<=1/2, concavity and nonnegativity give I(v)>=2v I(1/2). One can obtain this without assuming endpoint continuity: apply concavity between delta and 1/2 and let delta decrease to zero, discarding the nonnegative I(delta) term. A half-volume minimizer attains equality in the infimum defining h_mu, so h_mu=2I.

I is finite because finite-perimeter competitors of measure 1/2 exist, and positive because an attained zero-perimeter indicator on a connected manifold with positive smooth density would be constant almost everywhere.

### 2. Selection of the side and inward layers

The complement of a half-volume minimizer is another minimizer and reverses the weighted mean curvature. Selecting the side with H>=0 is legitimate; the proof does not assume differentiability of the isoperimetric profile at 1/2.

With the submission's trace-of-second-fundamental-form convention, the inward weighted logarithmic Jacobian has initial derivative -H. Before the cut time,

```math
(\log J)''=-|B_t|^2-(\mathrm{Ric}+\mathrm{Hess}V)(\dot\gamma,\dot\gamma)\le0.
```

Consequently J(t)<=exp(-Ht)<=1. Nearest points on the boundary lie in its regular part; cut loci and the singular set do not supply missing positive measure. Integrating only those rays for which t is before the cut time gives a bound on every interval of distances, not merely the first boundary layer:

```math
\mu\{s<f<t\}\le I(t-s).
```

This also rules out atoms at positive distance values. The pushforward measure on positive distances has total mass 1/2. Every finite distance value is well-defined even on a noncompact manifold.

For a one-dimensional line, V is convex and a half-line at a median is isoperimetric. Choose the side into which the density is nonincreasing, according to the sign of V' at that median. For a circle, integration of V''>=0 forces V constant; the two normal rays of an arc give the stated layer density. These cases match the same I normalization.

### 3. Masses, thresholds, and Delta_k

Let b=1/(2k), g=b/(k-1). The Lipschitz cumulative distance distribution G takes all the target values below 1/2. Distinct target values force strictly ordered thresholds, even if G has flat intervals.

Each omitted gap has measure g. Each of the k-1 retained positive-distance pieces has measure b; the other piece has measure 1/2. The final retained tail has measure

```math
\tfrac12-[(k-1)g+(k-2)b]=b.
```

Thus mu(A)=1-b and every individual piece has measure at least b. This is exactly a_i+sum_j a_j>=1. The tuple genuinely belongs to Delta_k and the concentration hypothesis is not being applied to inadmissible tiny sets.

Each gap width is at least g/I. Since f is globally 1-Lipschitz, this is a lower bound for the distances between neighboring retained sets. Alternative geometric paths cannot defeat this conclusion. The sets need not be connected, which is permitted by the target.

### 4. Concentration test and numerical constant

At r=g/(4I), the radius is less than half the guaranteed separation. A point in a gap which joins A_r must have f-value within r of one of the gap endpoints. Each endpoint layer has measure at most Ir. Therefore

```math
\mu(A_r\setminus A)\le 2(k-1)Ir=b/2,
\qquad 1-\mu(A_r)\ge b/2.
```

The target hypothesis, with its exact prefactor b=1-mu(A), forces

```math
\min(ar^2,\sqrt a\,r)\le\log2.
```

Set x=sqrt(a)r. If x>=1 the left side is at least one, impossible; for x<1 it is x^2. Hence

```math
a\le16(\log2)I^2/g^2
=64k^2(k-1)^2(\log2)I^2.
```

There is no reversed inequality or missing factor of two here. The k=2 case has no middle pieces and satisfies the same construction.

### 5. Functional Cheeger inequality and nondiscrete spectrum

For any H^1(mu) function, choose a median and apply the coarea inequality to the squares of the positive and negative parts about that median. Their positive level sets have measure at most 1/2. Cauchy-Schwarz gives the energy bound h_mu^2/4 times the squared L^2 distance to the median, which is at least the variance. This is a form inequality and needs neither an eigenfunction nor compact resolvent.

Every two-dimensional subspace in the stated min-max definition has a nonzero mean-zero member. Therefore lambda^(1)>=h_mu^2/4=I^2. Monotonicity of the variational levels then proves the target for every k>=2. Finite measure puts constant functions in H^1(mu); completeness also permits the usual compact-support approximations if that Sobolev-space convention is adopted.

## Gaps and optional refinements

No required mathematical repair was found. For maximum citation precision, keep the manuscript's separate discussion of nonorientability and dimension one. Do not describe Milman 2015 Theorem 2.3 as literally stated for nonorientable one-dimensional manifolds.

The dependence k^4 is not claimed sharp. This argument does not establish a bound independent of k, nor a dimension-free uniform adjacent-eigenvalue-ratio theorem. Neither is requested by the current target.

## Verified primary sources and current-relevance search

- Gozlan-Herry, [primary preprint](https://arxiv.org/pdf/1804.06133), Section 5.2, pp. 15-16, especially the question on p. 16. The target is the inverse question with the min(ar^2,sqrt(a)r) profile, not the forward Gaussian-profile question in Section 5.1. [DOI](https://doi.org/10.1007/s11118-018-9743-1).
- Milman, [2010 primary final preprint](https://arxiv.org/pdf/0902.1560), Section 2.2, p. 9: finite-measure existence and regularity; Section 2.4, pp. 10-11: singular-boundary extension; Theorem 3.2 and Corollary 3.3, pp. 11-12: concavity and Cheeger identity. Its baseline assumptions are complete, smooth, oriented, positive C^2 density; the smooth convexity condition is Ric+Hess V>=0. [DOI](https://doi.org/10.1215/00127094-2010-038).
- Milman, [2015 published primary text](https://ems.press/content/serial-article-files/32036), Theorem 2.3 and Corollary 2.5, printed pp. 1051-1052, and Proposition 2.9, p. 1053 with proof pp. 1054-1055. These give the regular boundary, weighted perimeter equality, and regularity of nearest boundary points in a geodesically convex support. Set the support to M and dimension parameter to infinity. Theorem 2.1, pp. 1047-1049, supplies weighted normal comparison. [DOI](https://doi.org/10.4171/JEMS/526).
- Milman, [2008 published primary note](https://www.numdam.org/item/10.1016/j.crma.2008.07.022.pdf), Theorem 4.2 and the following paragraph, printed p. 993, verify the profile concavity/Cheeger identity in the convexity setting. [DOI](https://doi.org/10.1016/j.crma.2008.07.022).

Bounded searches on 3 November 2026 included multi-set concentration/converse/lower eigenvalue bounds, the exact Gozlan-Herry title and question, and the authors' current research pages. No later matching complete converse was located. Existing subset comparisons and higher-order Poincare upper estimates run in a different direction. This search is not a literature-priority certificate; the full-target verdict comes from the proof audit.
