# AIM458 / PR #175 independent proof review

**Review date:** 21 October 2026
**Submission:** [PR #175](https://github.com/MColbrook/AIM/pull/175)
**Pinned head:** a9e2073c1da1a576c699b0a71661068013c43ab7
**Reviewer role:** Independent OpenAI Codex mathematical review, separate from the submission's author context. This is an AI review, not human peer review or formal verification.

**Recommendation: Resolved for the exact stated AIM458 target.** I found no substantive remaining gap after reconstructing the complete proof, checking the repaired comparison theorem, and following its downstream uses. The result concerns finitely many smooth, divergence-free, wall-tangent noise fields on every bounded smooth three-dimensional domain, with only stochastic parabolicity as the amplitude restriction. It does not establish every rough or infinite-noise formulation of the broader survey problem.

No earlier full solution of this exact target was located in the primary-literature searches described below. That negative search result is not a proof of literature completeness.

## Materials and scope

I read the complete [revised manuscript source](https://github.com/MColbrook/AIM/blob/a9e2073c1da1a576c699b0a71661068013c43ab7/research/458/paper/paper.tex), its full dependency chain, README, target comparison, revision response, and public manifest. I compared the revision with the repository's earlier manuscript and read the complete [15 October review](https://github.com/MColbrook/AIM/blob/24edaadc6bb272737d8da0745c662c992db07b22/research/solution_reviews/2026-10-15-active-prs/458-review.md). The pinned branch SHA was checked directly. Original-byte payload lengths and SHA256 digests match all five manifest entries.

I extracted all 22 pages of the [submitted PDF](https://github.com/MColbrook/AIM/blob/a9e2073c1da1a576c699b0a71661068013c43ab7/research/458/paper/paper.pdf), rendered every page, inspected complete contact sheets, and inspected the revised pp.10–11 at readable scale. The PDF contains the revised lemmas; these checks found no clipping or formula-layout defect. No submitted program or TeX build command was executed. Artifact checks do not establish the theorem.

Source-line locators below refer to the pinned paper.tex. Equations and PDF pages provide additional locators.

## The repaired comparison theorem

The previous gap was substantive: surjective fractional projection images alone do not meet the corrected comparison theorem. Revised source lines 689–714, PDF p.10, equations (3.19)–(3.20), state both the projection-image requirements and the compatible fractional right-inverse requirements. They agree with Kunstmann–Weis 2013, Theorem 1.3, p.802. The physical-domain citation is separately corrected to that erratum's Theorem 2.1, whose boundary hypothesis is satisfied by smooth domains. The Euclidean theorem is not applied directly to the periodic channel. [Author erratum](https://kaltonmemorial.missouri.edu/assets/docs/ma2006a.pdf).

The proposed right inverse is the single compatible family

```math
\mathcal J_p=L_p i_p A_{0,p}^{-1},
```


where $`L_p`$ is the componentwise Dirichlet Laplacian and $`A_{0,p}`$ is the unit-viscosity reference channel Stokes operator. This does not change the physical viscosity. Strong resolvent and domain estimates established before this step make $`\mathcal J_p`$ bounded on the base spaces and give $`P\mathcal J_p=I`$. The definitions are consistent across exponents because they use the same elliptic solution.

### Extra channel regularity

Lemma 3.1, source lines 732–776, PDF p.10, equations (3.22)–(3.24), supplies the extra derivative. Starting from the already proved $`H^2`$ velocity and $`H^1`$ pressure estimate, horizontal difference quotients preserve the periodic geometry, both zero wall values, and the mean-zero pressure normalization. They control every third velocity derivative containing a horizontal derivative and every second pressure derivative containing one.

The remaining derivatives follow in order from the distributional identities

```math
\partial_z^3u_3=-\mathrm{div}_h\partial_z^2u_h,
\qquad
\partial_z^2p=\partial_zf_3+\Delta\partial_zu_3,
```


and

```math
\partial_z^3u_h=-\partial_zf_h-\Delta_h\partial_zu_h
                 +\nabla_h\partial_zp.
```


Their right sides are controlled in $`L^2`$ in that order. Thus $`H^1`$ forcing gives $`H^3`$ velocity and $`H^2`$ pressure without imposing an unjustified boundary trace on $`f`$ or $`\Delta u`$.

### Both compatible right inverses

Lemma 3.2, source lines 778–849, PDF p.11, is not circular. The positive selfadjoint channel Stokes operator on $`H_2`$ is independently identified from its coercive gradient form. Hence

```math
D(A_{0,2}^{1/2})=V_2
```


is available before the desired Banach-space calculus. The base estimate gives $`\mathcal J_2:H_2\to L^2`$, and Lemma 3.1 gives $`\mathcal J_2:V_2\to H^1`$. Interpolating this same operator at parameter $`2s`$ gives

```math
\mathcal J_2:D(A_{0,2}^{s})\longrightarrow H^{2s}.
```


For $`0<s<1/4`$, the scalar Dirichlet domain $`D(L_2^s)`$ is $`H^{2s}`$, with no boundary-trace restriction. Odd reflection below the trace threshold justifies that identity. In particular $`s=1/8`$ is admissible.

For the negative full-step endpoint, dualizing

```math
\widetilde Q_{p'}=A_{0,p'}^{-1}P L_{p'}
```


gives a consistent $`\mathcal J_p`$ between the dual strong domains. The operator $`\widetilde Q_{p'}`$ maps the scalar strong domain into the Stokes strong domain and restricts to the identity on that solenoidal domain. Restriction of functionals therefore gives $`P\mathcal J_p=I`$ on the negative endpoint. This constructs a bounded right inverse; it is stronger than a Hahn–Banach surjectivity argument.

The image requirements are checked separately at source lines 851–862. The base extension of $`\widetilde Q_2`$ is bounded by adjointness of $`L_2A_{0,2}^{-1}P`$; it maps scalar strong domains into Stokes strong domains and fixes solenoidal fields. Interpolation, the subtrace $`H^{2s}`$ bound on $`P`$, and $`\widetilde Q_2P=P`$ give the bounded positive image. The constructed right inverse makes it onto. Restriction to the dual strong domain and the negative right inverse give the other image.

The signs and interpolation parameters are correct. For the inverse operators $`L^{-1},A_0^{-1}`$, $`\alpha=-1/8`$ corresponds to the positive original-operator fractional domain, while $`\beta=1`$ corresponds to the negative full-step scale. At $`\theta=2/3`$, the couples $`p_0=2,p_1=8`$ and $`p_0=2,p_1=8/7`$ give $`p=4`$ and $`p=4/3`$. Scalar calculus, consistent resolvents, and $`R`$-sectoriality precede the application. The calculus angle is reduced only after calculus existence is established.

These arguments close the particular missing-hypothesis finding recorded on 15 October.

## Complete proof chain

### Physical weak scale and stochastic trace

Section 2, PDF pp.3–4, uses the dual of zero-vector-trace solenoidal $`W^{1,q'}`$ test fields as the weak Stokes space. It does not assume that Helmholtz projection preserves tangential zero trace. The inverse isotropic root identifies $`Y_q`$ with $`H_q`$, carries $`V_q`$ to the strong Stokes domain, and gives

```math
\mathcal E=(Y_4,V_4)_{3/4,4}.
```


At smoothness $`1/2`$ and exponent $`4`$, the boundary trace is defined. The additive stochastic theorem applies because $`Y_4`$ is isomorphic to a closed $`L^4`$ subspace and the corrected isotropic calculus has angle below $`\pi/2`$. Its temporal-regularity argument uses $`3/8`$ in time and the interpolation arithmetic

```math
5/8+(1/3)(3/8)=3/4.
```


This supplies the actual continuous Besov norm, with constants obtained on one fixed interval. The weak scale and no-slip interpolation interfaces are consistent with Prüss–Wilke, Section 5 and Proposition 5.1. [Author manuscript](https://arxiv.org/pdf/1703.08714v1).

### Flat anisotropic channel

Sections 3.1–3.2, PDF pp.5–9, eliminate pressure to obtain a clamped fourth-order normal-velocity equation. I checked its sign, longitudinal reconstruction, zero horizontal mode, and pressure equation. Heat and pressure roots can collide at positive resolvent parameters; the divided differences and confluent determinant remove this singularity.

The six-dimensional boundary matrix is bounded both ordinarily and with normal-component weight $`a/k`$. The limiting reflected product has its only possible nonzero eigenvalue $`e^{-2kh}`$, uniformly separated from one by the fixed nonzero lattice gap. The essential weighted lower-left block $`k/a`$ is retained.

The full-line kernel solves the eliminated equation, including the distributional delta term in the second velocity derivative. The root, angular, exponential, and divided-difference formulas cover pure and mixed horizontal derivatives through order two. Fast/slow Poisson sizes and the smaller normal forcing trace give the reflected Hardy-kernel bounds.

Diagonal Hilbert-index uniformity and the vector-valued maximal and Hardy estimates give the asserted $`R`$-bounds. In horizontal dimension two, the multiplier derivative count is sufficient at every finite exponent used. The explicit window argument transfers these bounds to the periodic lattice, including the separately treated zero mode. Thus the strong domains and deterministic maximal regularity are established before the repaired calculus application. The cited multiplier and maximal-function interfaces match Girardi–Weis, Corollary 4.4, and Deleaval–Kriegler, Theorem 1. [Girardi–Weis](https://people.math.sc.edu/girardi/papers/22.pdf), [Deleaval–Kriegler](https://arxiv.org/pdf/1703.08327v1).

### General anisotropy and frozen transport

Sections 3.3–3.4, PDF pp.12–13, identify both weak endpoint scales from the isotropic channel calculus. General-$`Q`$ deterministic maximal regularity is interpolated from strong and one-step extrapolated estimates. No general anisotropic square-root theorem is assumed.

The general-$`Q`$ additive stochastic estimate corrects the isotropic stochastic solution through a deterministic general-$`Q`$ equation. A full three-dimensional torus separately handles arbitrary-rank interior noise and the constant spatial mode. Random translation removes constant transport while retaining the necessary drift correction

```math
-\sum_k T_kU_t^{-1}g_k.
```


Omitting this term would change the equation; it is present in the submission. The additive theorem and deterministic-correction mechanism agree with the interfaces in Agresti–Veraar's survey. [Published survey](https://link.springer.com/article/10.1007/s00030-025-01090-2).

### Localizers and pressure

Sections 4.1–4.2, PDF pp.13–15, define the cross-form localizer

```math
T=M_O^{-1/2}CM_D^{-1/2}.
```


Its adjoint form gives boundedness on both positive zero-trace spaces and weak dual spaces. The full-vector chart and cutoff, and their adjoints, preserve the required value traces. The elliptic projection $`Q_O`$ extends to $`L^q`$ by the adjoint strong estimate, fixes solenoidal fields, and acts on the strong domains.

Divergence correction uses one consistent supported operator on fixed convex Euclidean boxes at the required positive and negative orders. It does not import an unproved periodic Bogovskii theorem. This is within Costabel–McIntosh's formula (3.13), Theorem 3.2, Corollary 3.4, and Remark 3.5. [Author version](https://costabel.perso.math.cnrs.fr/publis/PoiBogdeRhv2.pdf).

The Stokes pressure is estimated at order $`-\eta`$, $`\eta=1/8`$, using the ordinary Neumann gradient projection. The source windows are strict at both $`q=4`$ and $`q=4/3`$. The defect retains the nonorthogonal pressure coefficient $`(G^{\mathsf T}-R)\nabla p`$. Its sign and the index structure of the second-order coefficient $`GG^{\mathsf T}-I`$ follow by expanding the chart Laplacian and adding a flat gradient.

The coefficients have $`O(r)`$ supremum and $`O(1)`$ Lipschitz bounds, hence $`C^\zeta`$ size $`O(r^{13/16})`$ for $`\zeta=3/16>\eta`$. Negative-order multiplication, composition, and canonical extension stay within the stated windows. The relevant fixed-version interfaces are Breit–Gaudin, Theorem 4.38, Proposition 4.39, and the cited subtrace and extension results. [Version 1](https://arxiv.org/pdf/2511.19091v1).

### Both defects and quantitative square roots

Section 4.3, PDF pp.15–17, source lines 1194–1205, proves the two norms in (4.11), corresponding to two separate relative estimates. Lower-order terms gain $`\rho^{-d}`$, with $`d=1/16`$ and $`\theta=15/16`$.

The root comparison uses a triangular off-diagonal perturbation $`zK`$ of $`\mathrm{diag}(M_D+\rho,M_O+\rho)`$. The range condition is automatic for the invertible shift. Taking $`|z|`$ of order $`a(r)^{-1}`$ in uniform calculus and graph bounds gives the normalized root commutator of size $`O(a(r))`$. I checked the exact identity (4.12), which also gives its positive-space bound, needed for trace reconstruction.

Fixed-shift root differences are compact at the claimed levels and can enter Ehrling absorption. The proof does not assert uniform compactness as $`\rho\to\infty`$. Both relative bounds needed by Kalton–Kunstmann–Weis, Theorem 6.1 and Lemma 6.2, are retained. The calculus-angle comparison uses Theorem 4.1 and Corollary 4.4 after calculus existence. [Author version](https://kaltonmemorial.missouri.edu/assets/docs/ma2006.pdf).

### Reconstruction and physical linear existence

Sections 4.4–5, PDF pp.17–19, retain the bounded lower-order physical pressure term in the exact noise commutator. The drift-commutator normalization is consistent with $`T=M_O^{1/2}SM_D^{-1/2}`$.

Bounded-overlap reconstruction and the explicit patch count give

```math
N^{1/4}a(r)=O(r^{1/16})\longrightarrow0.
```


Compact and lower-order terms reduce through Ehrling's inequality to the physical $`L^2`$ norm. The homogeneous transport energy martingale vanishes by solenoidality and wall tangency. Helmholtz orthogonality and stochastic parabolicity leave positive gradient coercivity; the forcing and additive-noise cross terms are absorbable. This closes a uniform a priori estimate for $`sB`$, $`0\leq s\leq1`$.

A finite contraction continuation from the additive $`s=0`$ equation constructs existence. The manuscript does not infer existence from an estimate alone. Causality and stopped restrictions are preserved.

### Nonlinear conclusions

Section 6, PDF pp.19–21, uses the embedding $`B^{1/2}_{4,4}\hookrightarrow L^8`$ to obtain a locally Lipschitz quadratic convection map into $`Y_4`$. The state cutoff is bounded, globally Lipschitz, and predictable on continuous adapted paths. The $`T^{1/4}`$ factor gives contraction, and continuity makes its exit time positive.

Whole-class uniqueness is independent of the linear construction: stopping the actual norms justifies the variational Itô identity, and pathwise Gronwall uses the finite time integral of $`\|v\|_\infty^2`$. No probability-moment assumption is added to competing solutions.

Continuous dependence uses distinct base and perturbed thresholds. Failure to reach the fixed base stop forces a fixed-size full-interval path difference, whose probability tends to zero. This establishes both common-stop conclusions requested by AIM458; it does not assume positivity of an infinite infimum of stopping times.

## Prior-art checks

Searches included the exact title, combinations of no-slip, local, non-small transport, and stochastic parabolicity, and 2026 work involving Agresti, Veraar, and Goodair. The following plausible matches do not establish the exact target:

- Goodair, *Weak and Strong Solutions to Nonlinear SPDEs with Unbounded Noise*, version 3, Section 5.1: Theorem 5.1 supplies weak martingale no-slip solutions, followed by a two-dimensional statement. Its final subsection discussion identifies the zero-trace obstruction to stronger solution theory. Its broad abstract therefore does not establish AIM458. [Actual full text](https://arxiv.org/html/2401.10076v3).
- Goodair, *Anisotropic Inviscid Limit for the Navier–Stokes Equations with Transport Noise Between Two Plates*, version 2, revised 17 March 2026: periodic plates, transport-stretching noise, weak martingale solutions, and anisotropic inviscid convergence have different equation, domain, and solution quantifiers. [Version 2](https://arxiv.org/abs/2603.13199v2).
- Agresti–Veraar, *Stochastic Navier–Stokes Equations for Turbulent Flows in Critical Spaces*, CMP 405 (2024), article 43: the principal strong theory is on the torus; the bounded-domain material does not establish this three-dimensional non-small no-slip target. [Published article](https://link.springer.com/article/10.1007/s00220-023-04867-7).
- Li–Zhou, *Numerical Analysis of the 2D Stochastic Navier–Stokes Equations*, and the numerical and large-deviation search matches concern two-dimensional problems. [Preprint](https://arxiv.org/abs/2512.03483).

The Teschl author URL returned HTTP 502 during this audit. I independently checked the Hilbert form and spectral argument used in Lemma 3.2; its correctness does not depend on access to that textbook edition or on the disputed $`L^p`$ calculus. This is a source-access limitation, not an identified mathematical gap.

## Assessment and limits

The revised compatible right inverses close the previously recorded channel-calculus gap, and the complete downstream argument supports local existence, uniqueness in the asserted class, and continuous dependence after common stopping for the exact AIM458 target. No substantive unresolved finding was identified in this audit.

This conclusion is a natural-language AI proof assessment of a substantial analytic manuscript, with independently reconstructed arguments and checked primary-source interfaces. Mathematical error remains possible. It is not human peer review, a formal certificate, or a guarantee that no earlier theorem exists.
