# Prior-art audit of PRs 126–169

Audit date: **21 October 2026**. Scope: all 44 yuiyuiui manuscript targets in the inclusive range 126–169. Baseline checkout: `5af1f89`; each submission is separately pinned below.

**Result: no earlier independent complete match was verified for these 44 targets.** Each recommendation means that no replacement is justified by the evidence located in this search. It is not a guarantee of novelty, a proof certification, or a claim that no further source exists.

The original problem hypotheses and the submitted theorem were compared with the actual scope of the sources below. Earlier partial, related, special-case and technique-level results were not treated as a full solution. The contributor’s own earlier versioned note is not independent duplication. The existing partial status of AIM 423 is retained.

The closest tempting leads require particular care: Girouard–Polymerakis 2023 announces the Steklov transfer mechanism and circle case, but not every prescribed boundary; Rossi–Tough 2026 lacks the uniform-boundary hypothesis for its homogeneous-reaction domain examples; Jiang–Xu 2026 gives an x-dependent linear ABP counterexample; Ros-Oton–Weidner 2023 imposes stronger angular integrability in its global theorem; the stochastic regularity sources impose extra flow or smoothness restrictions. These distinctions are recorded per target.

The JSON companion additionally preserves the original statement, reference section, package bibliography and target-comparison text used in the audit. Prior AI reviews served only as source leads.

## PR 126 — AIM 162: proposed extreme solitary wave for the bidirectional Whitham system

Submitted **2026-10-14T21:39:54Z**; head `0537bbe23dca05b81c88df11e85b6c51a460e771`. [PR](https://github.com/MColbrook/AIM/pull/126) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/162-extreme-bidirectional-solitary-wave.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/0537bbe23dca05b81c88df11e85b6c51a460e771/research/solutions/162-extreme-bidirectional-solitary-wave).

**Claim compared.** Existence of a highest solitary solution for the bidirectional Whitham system, including the stated cubic scalar equation and crest.

**Fresh query terms.** `"Whitham" "extreme solitary" waves existence`; `"On the precise cusped behaviour" extreme Whitham pdf`.

**Primary-source evidence.**

- Mats Ehrnström; Ola I. H. Mæhlen; Kristoffer Varholm, [On the precise cusped behaviour of extreme solutions to Whitham-type equations](https://ems.press/content/serial-article-files/31101) (2023-02-17 preprint; 2023-11-22 online; 2025 volume). Locator: §4, Remark 4.8. Cusp asymptotics conditional on an extreme solution; solitary existence is distinguished.
- Tien Truong; Erik Wahlén; Miles H. Wheeler, [Global bifurcation of solitary waves for the Whitham equation](https://link.springer.com/article/10.1007/s00208-021-02243-1) (2021-08-07 online; 2022 volume). Locator: Theorems 1.3 and 4.8. Highest solitary waves for the unidirectional equation.

**Exact scope comparison.** The unidirectional multiplier/nonlinearity and crest c/2 differ from the target's bidirectional multiplier tanh(xi)/xi, cubic and crest c(1-1/sqrt(3)). The earlier bidirectional periodic highest-wave theorem and small solitary waves also do not supply a highest solitary wave. No earlier complete matching existence theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 127 — AIM 405: proposed half-power density rate for a quadratic kinetic mean-field game

Submitted **2026-10-14T22:08:15Z**; head `70f61fc9f49ac9ac53f07333308710e0984fc892`. [PR](https://github.com/MColbrook/AIM/pull/127) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/405-kinetic-mfg-vanishing-viscosity-rate.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/70f61fc9f49ac9ac53f07333308710e0984fc892/research/solutions/405-kinetic-mfg-vanishing-viscosity-rate).

**Claim compared.** An L2 density error of order sqrt(nu) for quadratic kinetic variational mean-field games, all dimensions, with terminal density cost.

**Fresh query terms.** `"kinetic mean field games" "vanishing viscosity" rate`.

**Primary-source evidence.**

- Wenpin Tang; Yuming Paul Zhang, [The Convergence Rate of Vanishing Viscosity Approximations for Mean Field Games](https://www.columbia.edu/~wt2319/VV.pdf) (2025). Locator: §7, problem 4(b). Lists kinetic rates as a further question.
- Megan Griffin-Pickering; Alpár R. Mészáros, [A variational approach to first order kinetic Mean Field Games with local couplings](https://arxiv.org/abs/2112.03141) (2021-12-06 v1; 2022-07-11 v3). Locator: Abstract and main existence/duality results. First-order kinetic existence and density-supported uniqueness.

**Exact scope comparison.** Tang–Zhang's rates concern their nonkinetic local/nonlocal systems; the kinetic rate is not one of their theorems. The variational kinetic existence theorem lacks the requested positive-noise error estimate. No verified earlier full match for this cost, velocity diffusion and rate.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 128 — AIM 400: proposed concentric-ball inequality for radiative insulation

Submitted **2026-10-14T22:41:07Z**; head `e9d45c98722999ecb5b4aeb19c2c4ba872631448`. [PR](https://github.com/MColbrook/AIM/pull/128) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/400-radiative-insulation-concentric-balls.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/e9d45c98722999ecb5b4aeb19c2c4ba872631448/research/solutions/400-radiative-insulation-concentric-balls).

**Claim compared.** Concentric-ball optimality for the precise Stefan–Boltzmann polynomial boundary energy, arbitrary outer volume bound.

**Fresh query terms.** `"thermal insulation" radiative "ball" Bucur Nahon`.

**Primary-source evidence.**

- Dorin Bucur; Mickaël Nahon; Carlo Nitsch; Cristina Trombetti, [Shape optimization of a thermal insulation problem](https://d-nb.info/127285647X/34) (2022-07-26). Locator: Equations (3)–(4), Theorems 1–3, Remark 4 and ensuing question. Identifies the radiative polynomial; full quadratic-convection optimization is separated from radiation.

**Exact scope comparison.** The source's completed convection theorem is for a quadratic boundary potential. Its other general-potential conclusions do not prove the requested concentric-ball minimum for every volume in the specified radiation polynomial. No earlier complete matching theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 129 — AIM 416: proposed global attraction of the positive catalytic equilibrium

Submitted **2026-10-14T22:46:09Z**; head `ab5d6f736be7486c9b57bf3ef27f0477bbfac3c5`. [PR](https://github.com/MColbrook/AIM/pull/129) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/416-catalytic-reaction-diffusion-positive-attractor.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/ab5d6f736be7486c9b57bf3ef27f0477bbfac3c5/research/solutions/416-catalytic-reaction-diffusion-positive-attractor).

**Claim compared.** Uniform global convergence of every strictly positive catalytic PDE trajectory in the mass regime M2<=M1<2M2, for unequal diffusivities.

**Fresh query terms.** `"Stability analysis" "irreversible chemical" Nguyen Tang 2026`.

**Primary-source evidence.**

- Thi Lien Nguyen; Bao Quoc Tang, [Stability analysis of irreversible chemical reaction-diffusion systems with boundary equilibria](https://link.springer.com/article/10.1007/s00033-026-02847-0) (2024-10-30 preprint; 2026-07-01 publication). Locator: Conjecture after Table 1; Theorems 2.4 and 2.7. Conjectural global attraction is distinct from local stability and other mass regimes.

**Exact scope comparison.** The earlier local stability and boundary-instability theorems do not force every positive orbit to converge to the positive equilibrium in the target mass window. The source's broad nonnegative formulation also admits boundary equilibria and cannot be substituted for the target's strictly positive formulation. No earlier full match verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 130 — AIM 396: proposed polynomial decay for KdV at length 14 pi

Submitted **2026-10-14T22:52:36Z**; head `0ca93304d829a56ae9970fde75c210f29f92e9f9`. [PR](https://github.com/MColbrook/AIM/pull/130) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/396-critical-kdv-odd-mode-polynomial-decay.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/0ca93304d829a56ae9970fde75c210f29f92e9f9/research/solutions/kdv-14pi-polynomial-decay).

**Claim compared.** Polynomial decay of all sufficiently small energy solutions at exactly L=14pi with three undamped linear modes.

**Fresh query terms.** `"KdV" "14" "pi" "decay" critical 2026`; `"KdV" "critical lengths" decay 2026 Niu Xiang`.

**Primary-source evidence.**

- Jingrui Niu; Shengquan Xiang, [Small-time local controllability of a KdV system for all critical lengths](https://arxiv.org/html/2501.13640v2) (2025-01-23 v1; 2025-12-16 v2). Locator: §2.4.5. Separates uncontrolled asymptotic stability from controllability.
- Jingrui Niu; Shengquan Xiang, [Stability of a Korteweg–de Vries equation close to critical lengths](https://arxiv.org/abs/2603.27605) (2026-03-29). Locator: Theorem 1.6 and critical-neighborhood hypotheses. Quantitative decay near critical lengths.

**Exact scope comparison.** Nguyen's 2021 decay theorem covers dimension one or specified even-dimensional undamped spaces. Here dim M=3. Near-critical exponential estimates exclude the exact three-mode critical length; boundary-control results are also different. No earlier full match verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 131 — AIM 404: proposed uniform convergence for a local quadratic mean field game

Submitted **2026-10-14T23:04:48Z**; head `2e20884b440d5804c1f2de740ae219239c8d4b0e`. [PR](https://github.com/MColbrook/AIM/pull/131) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/404-local-mfg-uniform-vanishing-viscosity.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/2e20884b440d5804c1f2de740ae219239c8d4b0e/research/solutions/local-mfg-uniform-vanishing-viscosity).

**Claim compared.** Whole-family interior uniform convergence of local quadratic MFG value functions in dimensions 1–3, permitting initial vacuum.

**Fresh query terms.** `"mean field games" "uniform convergence" "vacuum" vanishing viscosity`; `"Uniform convergence" "local" "mean field games" vanishing`.

**Primary-source evidence.**

- Wenpin Tang; Yuming Paul Zhang, [The Convergence Rate of Vanishing Viscosity Approximations for Mean Field Games](https://www.columbia.edu/~wt2319/VV.pdf) (2025). Locator: Theorem 5.5 and §7 problem 2(a). Weighted/weak estimates do not themselves give this local uniform convergence.
- Winston Yu; Qiang Du; Wenpin Tang, [Beyond separability: convergence rate of vanishing viscosity approximations to mean field games via FBSDE stability](https://www.sciencedirect.com/science/article/pii/S0304414926001936) (2026 publication). Locator: Conclusion and nonlocal Hamiltonian hypotheses. Uniform compact convergence for a nonlocal MFG setting.

**Exact scope comparison.** The newer FBSDE result concerns a nonlocal measure-dependent setting. Its regularity assumptions do not contain the local density coupling with vacuum. Older comparison/first-order regularity and weighted estimates require an additional bridge to whole-family uniform convergence here. No verified earlier complete match.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 132 — AIM 413: proposed quarter-Sobolev norm inflation for the defocusing Gabitov-Turitsyn equation

Submitted **2026-10-14T23:43:44Z**; head `44a397b2c3577679229767a914922db8c8ddf390`. [PR](https://github.com/MColbrook/AIM/pull/132) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/413-intercritical-dispersion-managed-norm-inflation.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/44a397b2c3577679229767a914922db8c8ddf390/research/solutions/413-intercritical-dispersion-managed-norm-inflation).

**Claim compared.** Norm inflation at homogeneous H^(1/4) for the defocusing quintic three-dimensional Gabitov–Turitsyn equation, allowing either time direction.

**Fresh query terms.** `"Gabitov–Turitsyn" "norm inflation"`; `"Gabitov-Turitsyn" "ill-posedness" 2026`.

**Primary-source evidence.**

- Matthew Kowalski, [On ill-posedness for the Gabitov–Turitsyn equation](https://arxiv.org/html/2510.11887v1) (2025-10-13). Locator: §6.4; Theorems 1.6–1.7. Mass/energy regimes are distinguished from the unresolved inter-critical defocusing case.

**Exact scope comparison.** The source explicitly leaves inter-critical norm inflation unresolved; its energy-supercritical and focusing results do not include this positive H^(1/4) defocusing target. Scattering theorems for other data regimes are not a matching counterexample. No earlier full match verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 133 — AIM 367: proposed counterexample to the universal small-BV error bound

Submitted **2026-10-14T23:49:52Z**; head `92de46d2190e6af89c3ac751be6746b3b429b17f`. [PR](https://github.com/MColbrook/AIM/pull/133) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/367-universal-hyperbolic-error-rate.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/92de46d2190e6af89c3ac751be6746b3b429b17f/research/solutions/367-hyperbolic-error-counterexample).

**Claim compared.** A fixed small-BV Burgers datum and admissible approximate trajectories violate the universal sqrt(epsilon)|log epsilon| rate.

**Fresh query terms.** `"Bressan" "universal" "error" counterexample approximation small BV 2026`.

**Primary-source evidence.**

- Alberto Bressan; Graziano Guerra, [Unique Solutions to Hyperbolic Conservation Laws with a Strictly Convex Entropy](https://boa.unimib.it/retrieve/79c2ef59-fa1a-478f-b11e-fb0cfd5abd9c/Guerra-2024-J%20Differential%20Equations-VoR.pdf) (2023-05-18 preprint; 2024 publication). Locator: Corollary 4.1 and final paragraph. Qualitative universal convergence modulus; suggested rate left open.

**Exact scope comparison.** A qualitative modulus and quantitative rates for particular viscosity/Glimm schemes do not settle the universal residual-defined approximation class. No earlier counterexample with the target's fixed datum and every residual/time/entropy hypothesis verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 134 — AIM 390: proposed local planar Monge-Ampere Hessian integrability

Submitted **2026-10-15T00:02:55Z**; head `a8adb802e6890282b62c5118ae84d8f54ffcde89`. [PR](https://github.com/MColbrook/AIM/pull/134) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/390-planar-monge-ampere-sharp-hessian-integrability.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/a8adb802e6890282b62c5118ae84d8f54ffcde89/research/solutions/390-planar-monge-ampere-sharp-hessian-integrability).

**Claim compared.** Local strong Hessian integrability at p_lambda=(1+lambda²)/(1-lambda²) for the complete planar Alexandrov class, implying its weak endpoint.

**Fresh query terms.** `"Agazzi" "Monge" "2026" sharp integrability`; `"Quasiconvexity of the Burkholder function on symmetric matrices" Monge`.

**Primary-source evidence.**

- Andrea Agazzi and 19 coauthors (v2 author list), [Sharp Higher Integrability Theory, Part I: The Lp-norm of the Beurling–Ahlfors transform](https://arxiv.org/html/2609.28311v2) (2026-09-23 v1; 2026-10-08 v2). Locator: §1 final two paragraphs; Lemmas 3–4. Calibration/projection ideas; explicitly defers Monge–Ampère applications.
- André Guerra, [Quasiconvexity of the Burkholder function on symmetric matrices](https://arxiv.org/html/2608.23388v1) (2026-08-24). Locator: Introduction and main quasiconvexity theorem. Symmetric-matrix integral inequalities, not the local Alexandrov Hessian theorem.

**Exact scope comparison.** Neither the Beurling-transform norm theorem nor quasiconvexity on symmetric matrices states the original-class local endpoint Hessian estimate. The required localization and nonsmooth Hessian transformation are substantive additional claims. No complete earlier local theorem verified; do not treat a credited technique as duplication.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 135 — AIM 112: proposed resolution — large Steklov eigenvalues with prescribed embedded boundary

Submitted **2026-10-15T00:46:02Z**; head `2d843e8dc4c0ce3b341bbcf44a9d7fc36c744bfa`. [PR](https://github.com/MColbrook/AIM/pull/135) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/112-fixed-embedded-boundary-steklov.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/2d843e8dc4c0ce3b341bbcf44a9d7fc36c744bfa/research/solutions/112-fixed-embedded-boundary-steklov).

**Claim compared.** Arbitrarily large first positive induced-metric Steklov eigenvalue for every admissible prescribed embedded boundary, including curves and filling codimension one.

**Fresh query terms.** `"Steklov" "prescribed boundary" "Polymerakis"`; `Steklov prescribed boundary arbitrarily large embeddings Girouard Polymerakis 2026`.

**Primary-source evidence.**

- Alexandre Girouard; joint work with Panagiotis Polymerakis, [Manifolds with arbitrarily large Steklov eigenvalues (joint work with P. Polymerakis)](https://ems.press/content/serial-article-files/47475) (2023-08-20 to 2023-08-25 workshop; Report 36/2023). Locator: Printed p.2075 (PDF p.59), relative Nash–Kuiper paragraph. Announces transfer mechanism and a round-circle application.
- Alexandre Girouard; Panagiotis Polymerakis, [Large Steklov eigenvalues under volume constraints](https://arxiv.org/abs/2403.08925) (2024-03-13 preprint; 2024 publication). Locator: Abstract and main warped-product theorem. Intrinsic fixed-boundary metrics on specified product topologies.

**Exact scope comparison.** The 2023 announcement already deserves attribution for the mechanism and circle example, as the submission does. It does not state the universal every-embedded-boundary theorem, and the 2024 result is intrinsic/product-topology constrained. No earlier complete matching theorem located; insufficient basis to remove the entire manuscript.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 136 — AIM 423: proposed domain clarification for the printed Sobolev restriction

Submitted **2026-10-15T01:38:37Z**; head `fb98d423513524bc2a4443454e5401a80a55d4c9`. [PR](https://github.com/MColbrook/AIM/pull/136) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/423-magnetic-airy-half-plane-spectrum.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/fb98d423513524bc2a4443454e5401a80a55d4c9/research/solutions/423-ordinary-sobolev-magnetic-airy-domain-clarification).

**Claim compared.** Domain clarification: the printed ordinary H1_0 restriction is nonclosed; no all-field theorem for the natural closed magnetic realization.

**Fresh query terms.** `"magnetic" "Airy" "nonclosed" spectrum Almog`.

**Primary-source evidence.**

- Yaniv Almog; Bernard Helffer, [On the spectrum of non-selfadjoint Schrödinger operators with compact resolvent](https://arxiv.org/abs/1410.5122) (2014-10-19). Locator: Dirichlet-realization construction and magnetic form-domain discussion. Closed magnetic realizations and spectral results for a class of operators.

**Exact scope comparison.** A theorem about a closed covariant magnetic realization does not prove nonclosedness of the different ordinary-H1_0 restriction. Conversely the submitted clarification is not a full solution of the intended intermediate-field spectrum problem. No earlier identical clarification verified; retain its existing partial classification.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Partially resolved**); do not infer a novelty guarantee.

## PR 137 — AIM 441: proposed counterexample to global smooth propagation with ionization

Submitted **2026-10-15T01:44:14Z**; head `2588b6e13e0d21cc0ab51545d89c79fa4d057f0a`. [PR](https://github.com/MColbrook/AIM/pull/137) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/441-ionization-laser-envelope-global-regularity.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/2588b6e13e0d21cc0ab51545d89c79fa4d057f0a/research/solutions/441-ionization-blowup).

**Claim compared.** One admissible positive-ionization coupled three-dimensional model has finite-time gradient blowup from smooth compact optical data and zero density.

**Fresh query terms.** `"ionization" "blowup" "Lannes" Szeftel global`; `"ionization" "blow-up" nonlinear Schrödinger plasma mathematical`.

**Primary-source evidence.**

- Roland Donninger; Birgit Schörkhuber, [Self-similar blowup for the cubic Schrödinger equation](https://arxiv.org/abs/2406.16597) (2024-06-24 v1; 2025-12-09 v3). Locator: Main self-similar solution theorem. Scalar focusing cubic NLS, with no coupled density/positive ionization.
- Éric Dumas; David Lannes; Jérémie Szeftel, [Variants of the focusing NLS equation: derivation, justification, and open problems](https://david-lannes.perso.math.cnrs.fr/wp-content/uploads/2019/01/dumaslannesszeftel.pdf) (2016). Locator: §4.1.2, equation (54), Open Problem 3. The coupled ionization regularity question.

**Exact scope comparison.** Scalar cubic NLS blowup and fixed-profile stability do not by themselves construct a blowup solution for positive ionization and dynamic electron density. Numerical saturation/blowup studies also lack the requested analytic witness. No earlier complete matching coupled theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 138 — AIM 376: proposed full kinetic FENE zero spatial diffusion limit

Submitted **2026-10-15T02:05:40Z**; head `3a7c9c8907582924bf038c24b6225b0685943bc2`. [PR](https://github.com/MColbrook/AIM/pull/138) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/376-fene-vanishing-center-of-mass-diffusion.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/3a7c9c8907582924bf038c24b6225b0685943bc2/research/solutions/376-fene-vanishing-center-of-mass-diffusion).

**Claim compared.** A global zero spatial-diffusion subsequence for the full noncorotational 3D kinetic FENE system with no stress/transport defect.

**Fresh query terms.** `"FENE" "vanishing" "diffusion" Masmoudi 2026`; `"FENE" "zero-diffusion" limit Dębiec Süli`.

**Primary-source evidence.**

- Tomasz Dębiec; Endre Süli, [On a Class of Generalised Solutions to the Kinetic Hookean Dumbbell Model for Incompressible Dilute Polymeric Fluids: Existence and Macroscopic Closure](https://link.springer.com/article/10.1007/s00205-025-02115-x) (2025-07-02). Locator: §1, FENE comparison and zero-diffusion discussion. Separates Hookean generalised solutions from FENE unresolved limit.
- Nader Masmoudi, [Global existence of weak solutions to the FENE dumbbell model of polymeric flows](https://arxiv.org/abs/1004.4015) (2010 preprint; 2013 publication). Locator: Final open-problem discussion: zero diffusion in x. Existence directly without spatial diffusion is not a zero-diffusion convergence theorem.

**Exact scope comparison.** No-diffusion existence, local/near-equilibrium limits, corotational models and FENE-P closures do not establish the target's global full-gradient kinetic limit and defect-free fluxes. No earlier complete match verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 139 — AIM 424: proposed real-spectrum theorem for separated spherical Robin operators

Submitted **2026-10-15T02:18:20Z**; head `2fe247eaa2e8a2b96f41343ee7138013a70e1e56`. [PR](https://github.com/MColbrook/AIM/pull/139) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/424-spherical-pt-robin-real-spectrum.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/2fe247eaa2e8a2b96f41343ee7138013a70e1e56/research/solutions/424-spherical-pt-robin-real-spectrum).

**Claim compared.** Purely real full spectrum for every spherical strip width, real Robin parameter and integer separated mode.

**Fresh query terms.** `"spherical" "PT-symmetric" "real spectrum" Siegl 2026`.

**Primary-source evidence.**

- David Krejčiřík; Petr Siegl, [PT-symmetric models in curved manifolds](https://arxiv.org/pdf/1001.2988v1) (2010-01-11 preprint; 2010 publication). Locator: §4.4.2, equations (4.32)–(4.33), Proposition 4.4 and Remark 4.6. Correct spherical potential; only restricted/high-energy conclusions.

**Exact scope comparison.** Flat-interval Robin reality in Proposition 4.3 omits the spherical potential. Proposition 4.4 leaves possible complex low eigenvalues and therefore does not contain the full target. No later complete matching theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 140 — AIM 366: proposed counterexample to literal rapid-decay continuation

Submitted **2026-10-15T02:56:51Z**; head `42bc75eb7969fa727113d0fb216c8083ea36b39f`. [PR](https://github.com/MColbrook/AIM/pull/140) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/366-cutoff-boltzmann-continuation.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/42bc75eb7969fa727113d0fb216c8083ea36b39f/research/solutions/366-cutoff-boltzmann-rapid-decay).

**Claim compared.** A pointwise jointly smooth hard-sphere solution from Gaussian data develops a positive inverse-sixth-power tail, disproving literal rapid-decay continuation in the broad class.

**Fresh query terms.** `"Boltzmann" "rapid decay" "energy-increasing" solutions`; `"Lu" "Wennberg" "Solutions" "energy" 2002 Boltzmann`.

**Primary-source evidence.**

- Xuguang Lu; Bernt Wennberg, [Solutions with increasing energy for the spatially homogeneous Boltzmann equation](https://research.chalmers.se/publication/21400) (2002). Locator: Abstract/publisher identity only; full theorem hypotheses not accessible in this search. Earlier increasing-energy solutions; not verified as the same smooth tail construction.
- Giada Basile; Dario Benedetto; Lorenzo Bertini; Emanuele Caglioti, [Asymptotic probability of energy increasing solutions to the homogeneous Boltzmann equation](https://arxiv.org/pdf/2202.07311v2) (2022-02-15 v1; 2022-03-30 v2). Locator: §§1 and 7. Weak increasing-energy solutions and their probabilistic interpretation.

**Exact scope comparison.** A weak increasing-energy solution or an initial energy jump does not verify joint pointwise smoothness, all Gaussian initial jets, prescribed r^-6 tails and every hydrodynamic hypothesis. Lu–Wennberg's full hypotheses were not verified, so it cannot justify replacement. No earlier complete match verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 141 — AIM 141: finite-jet controllability counterexample

Submitted **2026-10-15T03:31:05Z**; head `bc5fd6bac773c5e925e18853bfc4b647fe22a090`. [PR](https://github.com/MColbrook/AIM/pull/141) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/141-finite-jet-small-time-control.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/bc5fd6bac773c5e925e18853bfc4b647fe22a090/research/solutions/141-finite-jet-control-counterexample).

**Claim compared.** One fixed 5D polynomial STLC system has, at every Taylor order, a same-jet polynomial non-STLC perturbation with the same bounded controls.

**Fresh query terms.** `"finite jet" "controllability" counterexample Jafarpour`; `"finite-jet" "counterexample" "small-time" analytic 2026`; `"finite-jet conjecture" "disproved"`.

**Primary-source evidence.**

- Saber Jafarpour, [On small-time local controllability](https://arxiv.org/abs/1604.02432) (2016-04-08 v1; 2019-11-19 v7; 2020 publication). Locator: Conjecture 1.1; Theorem 7.1 and Corollary 7.2. Finite-jet conjecture and a sufficient polynomial-growth condition.

**Exact scope comparison.** Finite-dimensional Lie-bracket obstruction criteria and sufficient polynomial growth do not settle the universal finite-jet conjecture. The author's earlier AIM 417 system is an acknowledged dependency, not an independent prior solution of this perturbation claim. No earlier complete matching counterexample verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 142 — AIM 429: proposed sharp transmission Weyl remainder

Submitted **2026-10-15T05:35:57Z**; head `6cfcf05e1f41032113617cc16e174569d19ae9bb`. [PR](https://github.com/MColbrook/AIM/pull/142) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/429-transmission-eigenvalue-sharp-weyl-remainder.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/6cfcf05e1f41032113617cc16e174569d19ae9bb/research/solutions).

**Claim compared.** Exact O(r^(d-1)) remainder for all nonzero complex transmission energies, counted with maximal-domain Riesz algebraic multiplicities on arbitrary smooth bounded domains.

**Fresh query terms.** `"transmission eigenvalues" "Weyl" "O(r" remainder 2026 Vodev`; `transmission eigenvalues Weyl remainder sharp isotropic site:arxiv.org`.

**Primary-source evidence.**

- Vesselin Petkov; Georgi Vodev, [Asymptotics of the number of the interior transmission eigenvalues](https://arxiv.org/abs/1403.3949) (2014-03-16 preprint; 2017 publication). Locator: Theorem 1.1. Remainder O_epsilon(r^(d-kappa+epsilon)), 0<kappa<=1.
- Jean Fornerod; Hoai-Minh Nguyen, [The Weyl law of transmission eigenvalues and the completeness of generalized transmission eigenfunctions without complementing conditions](https://arxiv.org/abs/2301.05851) (2023-01-14). Locator: Main Weyl-law theorem. Leading Weyl law for degenerate anisotropic coefficients.

**Exact scope comparison.** Removing an epsilon loss to obtain exact boundary order is not supplied by a leading Weyl law, nor by eigenvalue-free strips alone. Vodev's 2017 Conjecture 1 requests the stronger remainder. No earlier complete arbitrary-domain boundary-order theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 143 — AIM 193: proposed solution of the Gaussian polymer moment spectrum

Submitted **2026-10-15T05:45:25Z**; head `a2832f5f06a368e44102573e64db48fc80cca2db`. [PR](https://github.com/MColbrook/AIM/pull/143) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/193-directed-polymer-moment-spectrum.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/a2832f5f06a368e44102573e64db48fc80cca2db/research/solutions).

**Claim compared.** A continuous strictly decreasing Gaussian directed-polymer moment spectrum onto [5/3,infinity), including left continuity and value at beta_c.

**Fresh query terms.** `"polymer" "moment exponent" "strictly" Gaussian continuity 2026`; `"polymer" "p*" "continuity" Junk Lacoin moment`; `"Conjecture 3.32" polymer`.

**Primary-source evidence.**

- Quentin Berger, [Random polymers in random environment: an introduction to disordered systems](https://www.math.univ-paris13.fr/~quentin.berger/documents/Disordered-Polymers.pdf) (2026-04-16). Locator: §3.3.2, Theorems 3.28–3.29 and Conjecture 3.32. Records one-sided/low-order continuity and the remaining spectrum conjecture.
- Stefan Junk; Hubert Lacoin, [Coincidence of critical points for directed polymers for general environments and random walks](https://arxiv.org/html/2502.04113v2) (2025-02-06 v1; 2025-11-10 v2). Locator: Theorem 2.1 and Corollary 2.5. Critical-point and endpoint facts, not the entire strictly monotone Gaussian spectrum.

**Exact scope comparison.** Finite-support strictness cannot be applied unchanged to unbounded Gaussian disorder. Existing endpoint and continuity results do not fill high-moment right continuity and strict monotonicity throughout the requested interval. No earlier complete matching spectrum theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 144 — AIM 185: proposed resolution — CO phase selection for a stirred catalytic surface model

Submitted **2026-10-15T05:49:04Z**; head `189bc466d46e119d7c7765bce1d41618746062fd`. [PR](https://github.com/MColbrook/AIM/pull/144) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/185-catalytic-carbon-monoxide-poisoning.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/189bc466d46e119d7c7765bce1d41618746062fd/research/solutions/185-catalytic-carbon-monoxide-poisoning).

**Claim compared.** Almost-sure sitewise CO fixation, hence every finite-set CO probability tends to one, for all finite positive stirring/reaction rates, p>q and iid positive-CO data.

**Fresh query terms.** `"carbon monoxide" "poisoning" "p>q" Durrett Swindle`; `"carbon monoxide" "Durrett" "fixation" catalysts`.

**Primary-source evidence.**

- Rick Durrett; Glen Swindle, [Coexistence results for catalysts](https://sites.math.duke.edu/~rtd/reprints/paper84.pdf) (1994). Locator: Theorem 1; its proof's signed-density estimate. Vacancy and unlike-neighbor probabilities vanish for translation-invariant data.
- Rick Durrett, [Interacting Particle Systems: Ideas, Techniques, Applications](https://sites.math.duke.edu/~rtd/PASTA/PASTA0902.pdf) (2026-09-02 manuscript). Locator: §5.4, Open Problem 5.4.6. CO phase-selection question; original target citation, PDF access limited.

**Exact scope comparison.** Vanishing vacancies and unlike pairs permits a mixture of the two homogeneous colors and is weaker than the target's selection of CO from every iid positive-CO law. The 1994 theorem does not contain the fixation/color-selection step. No earlier complete matching result verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 145 — AIM 328: proposed counterexample for Fitch reconstruction under a molecular clock

Submitted **2026-10-15T05:50:54Z**; head `54df545617bc9696104d2802bc3a91eb903445b2`. [PR](https://github.com/MColbrook/AIM/pull/145) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/328-fitch-ultrametric-ancestral-accuracy.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/54df545617bc9696104d2802bc3a91eb903445b2/research/solutions/fitch-ultrametric-counterexample).

**Claim compared.** A three-leaf ultrametric twenty-state counterexample: Fitch accuracy 38829/400000 is below the one-leaf accuracy 39/400.

**Fresh query terms.** `"parsimony" "ultrametric" "counterexample" "r" 2026`.

**Primary-source evidence.**

- Lina Herbst; Mareike Fischer, [On the accuracy of ancestral sequence reconstruction for ultrametric trees with parsimony](https://arxiv.org/abs/1706.06085) (2017-06-19 preprint; 2018 publication). Locator: Theorems 1–2; §5. Affirmative results for three/four states; leaves r>4 open.
- Guoliang Li; Mike Steel; Louxin Zhang, [More Taxa Are Not Necessarily Better for the Reconstruction of Ancestral Character States](https://www2.gwu.edu/~clade/bisc%20207/LiEtAl2008.pdf) (2008). Locator: p.652 final paragraph before acknowledgments. The molecular-clock conjecture; nonclock examples are different.

**Exact scope comparison.** Earlier counterexamples lacking ultrametricity do not refute the clock-constrained question. The affirmative two-, three- and four-state theorems do not include r=20. No earlier ultrametric r>=5 counterexample matching the universal target verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 146 — AIM 191: proposed resolution — strong disorder and critical-point shift for Gaussian pinning

Submitted **2026-10-15T06:00:19Z**; head `b2f9fc098cd461dc364b7b62f4760c6f1143072c`. [PR](https://github.com/MColbrook/AIM/pull/146) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/191-pinning-strong-disorder-critical-shift.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/b2f9fc098cd461dc364b7b62f4760c6f1143072c/research/solutions/191-pinning-strong-disorder-critical-shift).

**Claim compared.** For the exact normalized n^(-5/4) renewal and iid Gaussian environment, martingale extinction at the annealed field implies a strictly positive critical-field shift for every beta.

**Fresh query terms.** `"pinning" "strong disorder" "critical" Gaussian 2026 renewal`; `"pinning" "strong disorder implies" critical`; `"pinning" "martingale" "critical point" "Gaussian" Lacoin`.

**Primary-source evidence.**

- Quentin Berger, [Random Interfaces and Pinning Models](https://www.math.univ-paris13.fr/~quentin.berger/documents/Random-Interfaces.pdf) (2026-03-04). Locator: §4.2, Conjecture 4.9. Strong-disorder/critical-shift implication is distinguished from weak-disorder irrelevance.
- Hubert Lacoin, [The martingale approach to disorder irrelevance for pinning models](https://arxiv.org/abs/1002.4753) (2010-02-25 preprint; 2010 publication). Locator: Theorem 1.1. Small-disorder irrelevance for return exponent alpha in (0,1/2).

**Exact scope comparison.** Irrelevance below a small beta threshold and critical-point shift for sufficiently large disorder do not rule out all intermediate martingale-extinction regimes or the strong-disorder boundary. Directed-polymer coincidence theorems concern a different path model. No earlier full implication for every beta with this renewal law verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 147 — AIM 217: proposed counterexample to critical–subcritical heat-kernel comparison

Submitted **2026-10-15T06:55:07Z**; head `96149f92d7f66bfb1772aec423a32f676e2dc1d1`. [PR](https://github.com/MColbrook/AIM/pull/147) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/217-critical-subcritical-heat-ratio.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/96149f92d7f66bfb1772aec423a32f676e2dc1d1/research/solutions/217-critical-subcritical-heat-ratio).

**Claim compared.** One fixed smooth bounded-potential pair on the line meets null-critical/subcritical hypotheses but has infinite limsup of its diagonal heat-kernel quotient.

**Fresh query terms.** `"critical" "subcritical" "heat kernels" counterexample ratio limit`; `"Fraas" "Pinchover" "conjecture" "counterexample"`.

**Primary-source evidence.**

- Martin Fraas; David Krejčiřík; Yehuda Pinchover, [On some strong ratio limit theorems for heat kernels](https://arxiv.org/abs/0912.4337) (2009-12-22 v1; 2010-05-17 v3). Locator: Conjecture 1, Theorem 3.1 and Corollary 1. Conjecture and conditional symmetric/ordered-perturbation cases.

**Exact scope comparison.** Results using pointwise ordering or comparability of the potentials do not contain the target's unordered pair. General counterexamples to other ratio-limit conjectures must also meet both criticality integrals, spectral bottom zero and absence of an L2 ground state; none meeting these exact conditions verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 148 — AIM 383: proposed resolution — continuity at the onset of Flory gelation

Submitted **2026-10-15T07:57:50Z**; head `09b60bb381c35eb5567fb251c6cf6a33f13ba220`. [PR](https://github.com/MColbrook/AIM/pull/148) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/383-flory-gelation-mass-continuity.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/09b60bb381c35eb5567fb251c6cf6a33f13ba220/research/solutions/383-flory-gelation-mass-continuity).

**Claim compared.** Continuity of finite-cluster mass at every finite positive onset time for all Flory weak solutions in the specified alpha-kernel class.

**Fresh query terms.** `"Flory" "gelation" "continuity" mass 2026`; `"Flory" "continuity" "gelation time" Fournier Laurentot`; `"Flory" "gelation" "onset" continuity mathematics`.

**Primary-source evidence.**

- Nicolas Fournier; Philippe Laurençot, [Marcus–Lushnikov processes, Smoluchowski's and Flory's models](https://arxiv.org/html/0706.2057v1) (2007-06-14 preprint; 2009 publication). Locator: Assumption (A_alpha), Proposition 2.3 and following question. Distinguishes continuity after onset from continuity at onset.
- Daniel Heydecker; Robert I. A. Patterson, [Bilinear Coagulation Equations](https://arxiv.org/abs/1902.07686) (2019). Locator: Theorem 1; §7.1. Results for bilinear conserved-type kernels.

**Exact scope comparison.** Bilinear kernels are a narrower structural class than all continuous kernels comparable to x^alpha y+xy^alpha. Smoluchowski gelation criteria are a different equation, and post-gelation continuity leaves the onset jump question. No earlier complete matching theorem verified. The primary full text was subsequently accessed in HTML and PDF: Proposition 2.3 states continuity only on (T_gel,infinity), and its following paragraph explicitly leaves continuity at T_gel open.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 149 — AIM 379: proposed counterexample on a uniformly smooth unbounded KPP domain

Submitted **2026-10-15T08:11:13Z**; head `a9c98123bb0710a93ebaf1422f62b631e776189a`. [PR](https://github.com/MColbrook/AIM/pull/149) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/379-strong-kpp-unbounded-uniqueness.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/a9c98123bb0710a93ebaf1422f62b631e776189a/research/solutions/379-uniform-kpp-multiplicity).

**Claim compared.** Two bounded positive logistic Dirichlet equilibria on one connected unbounded uniformly C^(2,1/2) domain in dimension21.

**Fresh query terms.** `"strong-KPP" "uniformly" "Rossi" "Tough"`.

**Primary-source evidence.**

- Luca Rossi; Oliver Tough, [Sharp dimension threshold for unique FKPP steady states and BBM recurrence](https://arxiv.org/html/2610.17121v1) (2026-10-12). Locator: Theorems 1.7–1.8; §7. Variable-potential whole-space examples and locally analytic perforated domains.
- Henri Berestycki; Cole Graham, [The steady states of strong-KPP reactions in general domains](https://arxiv.org/html/2212.06611v1) (2022-12-13 preprint; 2025 online publication). Locator: Conjecture 1.3; Theorem 1.1. Spectral-nondegeneracy uniqueness; general uniform-domain conjecture.

**Exact scope comparison.** Rossi–Tough predates submission by three days but its locally analytic shrinking-obstacle domains lack the common-radius uniform boundary condition; its whole-space example uses spatially varying c(x). Neither is a verified counterexample in the target's homogeneous-reaction, uniformly smooth domain class. No earlier complete match verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 150 — AIM 463: proposed counterexample to uniform nonlocal Sobolev estimates

Submitted **2026-10-15T08:11:46Z**; head `3f046208c5834b548da08c6253c1508c25c90644`. [PR](https://github.com/MColbrook/AIM/pull/150) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/463-concave-nonlocal-calderon-zygmund.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/3f046208c5834b548da08c6253c1508c25c90644/research/solutions/463-concave-nonlocal-sobolev-counterexample).

**Claim compared.** Counterexamples to the kernel-uniform full-order W^(2s,p) estimate, for arbitrarily large p and strict ellipticity pairs, including the order-one convention.

**Fresh query terms.** `"concave" "nonlocal" "Sobolev" "counterexample" estimates 2026`.

**Primary-source evidence.**

- Xavier Fernández-Real; Xavier Ros-Oton, [Integro-Differential Elliptic Equations](https://arxiv.org/pdf/2411.12455v1) (2024-11-19 arXiv author draft; 2024 book). Locator: Chapter 3, Open Question 3.2. General concave nonlocal Sobolev estimate posed with kernel-uniform constants.
- Shuhei Kitano, [W^(sigma,p) a priori estimates for fully nonlinear integro-differential equations](https://arxiv.org/abs/2207.06728) (2022-07-14). Locator: Introduction and kernel hypotheses. Positive estimates for a restricted kernel class.
- Yongsheng Jiang; Lei Xu, [A counterexample to integral Aleksandrov–Bakelman–Pucci estimates for a nonlocal operator](https://arxiv.org/html/2610.16162v1) (2026-10-12). Locator: Abstract; Theorem 1.1 and coefficient condition(C). Fixed x-dependent linear operator and an integral maximum-estimate counterexample.

**Exact scope comparison.** Restricted near-fractional/regular kernels and bounds with stronger forcing norms do not establish or refute the uniform general-kernel estimate here. A linear isotropic equality case is excluded from the submission's negative claim and cannot refute it. No earlier complete matching counterexample verified. Jiang–Xu predates the PR by three days, but its coefficient a(x,y) depends on x and its conclusion concerns a maximum estimate; it does not provide the target's translation-invariant concave operator and full-order Sobolev counterexample.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 151 — AIM 380: proposed counterexample to critical KPP nonexistence

Submitted **2026-10-15T08:33:42Z**; head `0f1a72e90159ed4a58c53276e05ffd91632d2936`. [PR](https://github.com/MColbrook/AIM/pull/151) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/380-strong-kpp-critical-extinction.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/0f1a72e90159ed4a58c53276e05ffd91632d2936/research/solutions/380-critical-kpp-counterexample).

**Claim compared.** A uniformly smooth dimension21 Dirichlet domain with lambda1=1 has a positive bounded logistic equilibrium, refuting universal critical nonexistence.

**Fresh query terms.** `"KPP" "criticality" "uniformly smooth" domain counterexample Rossi`.

**Primary-source evidence.**

- Luca Rossi; Oliver Tough, [Sharp dimension threshold for unique FKPP steady states and BBM recurrence](https://arxiv.org/html/2610.17121v1) (2026-10-12). Locator: Theorem 1.7, Example1.9; §7. Critical whole-space variable-potential and locally analytic domain examples.
- Henri Berestycki; Cole Graham, [The steady states of strong-KPP reactions in general domains](https://arxiv.org/html/2212.06611v1) (2022-12-13 preprint; 2025 online publication). Locator: Conjecture1.7 and Proposition 1.6. Original criticality question and restricted results.

**Exact scope comparison.** The fixed target requires a homogeneous f and a uniformly C^(2,gamma) domain. Rossi–Tough's variable c(x) and shrinking-hole domain alternatives do not verify both requirements together. Their dimension threshold theorem is related but cannot replace the uniformly smooth witness. No earlier complete match verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 152 — AIM 384: proposed counterexample to two-obstacle equilibrium uniqueness

Submitted **2026-10-15T08:38:39Z**; head `f42708c58003e4f7663f6f9edda17626921cd27f`. [PR](https://github.com/MColbrook/AIM/pull/152) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/384-reaction-two-obstacle-uniqueness.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/f42708c58003e4f7663f6f9edda17626921cd27f/research/solutions/384-two-disk-monostable-counterexample).

**Claim compared.** A positive monostable reaction and the exterior of two equal disjoint planar disks admit two bounded positive full-domain Dirichlet equilibria.

**Fresh query terms.** `"two balls" "positive" "uniqueness" Berestycki Graham elliptic`.

**Primary-source evidence.**

- Henri Berestycki; Cole Graham, [A Stable-Compact Method for Qualitative Properties of Semilinear Elliptic Equations](https://arxiv.org/html/2309.16642v3) (2023-09-28 v1; 2026 publication). Locator: §8.5, Open Question 7(ii); Theorem 1.1. Two-ball exterior question distinguished from strongly exterior-star uniqueness.

**Exact scope comparison.** The excluded union of two disjoint balls is disconnected, so it does not satisfy the strongly exterior-star geometry in the available uniqueness theorem. General dumbbell/pocket nonuniqueness does not imply multiplicity on this exact two-obstacle exterior. No earlier complete matching theorem or counterexample verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 153 — AIM 467: proposed counterexample to fractional-pressure continuity

Submitted **2026-10-15T08:39:39Z**; head `e8620ac7479efe6ff3de2e8fe2b963325886f82d`. [PR](https://github.com/MColbrook/AIM/pull/153) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/467-fractional-pressure-superquadratic-continuity.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/e8620ac7479efe6ff3de2e8fe2b963325886f82d/research/solutions/467-fractional-pressure-continuity-counterexample).

**Claim compared.** A bounded energy weak-solution witness for N=2,m=3,s=3/4 disproves universal joint continuity, with a broader obstruction for s>1/2.

**Fresh query terms.** `"porous medium" "nonlocal pressure" "continuity" "m>2"`.

**Primary-source evidence.**

- Diana Stan; Félix del Teso; Juan Luis Vázquez, [Porous medium equation with nonlocal pressure](https://arxiv.org/abs/1801.04244) (2018-01-12). Locator: Theorems 5.1–5.5; Remark7 and §7. Existence/propagation theory; superquadratic continuity distinguished from m=2.
- Félix del Teso; Espen R. Jakobsen, [A Convergent Finite Difference-Quadrature Scheme for the Porous Medium Equation with Nonlocal Pressure](https://link.springer.com/article/10.1007/s10208-026-09752-y) (2026-06-01). Locator: §2 PDE-theory review. Existence and one-dimensional comparison/numerics, not the requested all-dimensional continuity.

**Exact scope comparison.** Continuity for mobility m=2 and uniqueness of a one-dimensional integrated model do not cover m>2,N>=2 across the free boundary. Numerical convergence also does not provide the submission's analytic counterexample. No earlier complete matching discontinuity result verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 154 — AIM 461: proposed counterexample — relaxed infinity fractional comparison

Submitted **2026-10-15T08:48:22Z**; head `70a827b3bf2a2a810f7f378d6945dcce7e84def3`. [PR](https://github.com/MColbrook/AIM/pull/154) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/461-infinity-fractional-evolution-comparison.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/70a827b3bf2a2a810f7f378d6945dcce7e84def3/research/solutions).

**Claim compared.** For the precise relaxed zero-gradient envelopes, bounded radial sub/supersolutions with the same smooth data cross; no claim of two full solutions.

**Fresh query terms.** `"infinity fractional" "comparison" counterexample evolution`.

**Primary-source evidence.**

- Félix del Teso; Jørgen Endal; Espen R. Jakobsen; Juan Luis Vázquez, [Evolution Driven by the Infinity Fractional Laplacian](https://arxiv.org/html/2210.06414v1) (2022-10-12 preprint; 2023 publication). Locator: Definitions 4.1/4.3, Theorem 2.6, §§7/9. Relaxed viscosity convention; restricted classical–viscosity comparison.
- Clayton Bjorland; Luis Caffarelli; Alessio Figalli, [Non-local tug-of-war and the infinity fractional Laplacian](https://arxiv.org/abs/1011.1966) (2010 preprint; 2012 publication). Locator: Elliptic comparison/nonuniqueness discussion. Related elliptic zero-gradient issue.

**Exact scope comparison.** An elliptic example does not itself supply time-dependent bounded continuous sub/supersolutions meeting the target's patched-test convention. The classical–viscosity comparison theorem has a different regularity interface. No earlier complete matching evolution counterexample verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 155 — AIM 469: proposed resolution — superlinear SKT localization

Submitted **2026-10-15T08:51:54Z**; head `13ab904c45cb6205f534546826d0b88208834692`. [PR](https://github.com/MColbrook/AIM/pull/155) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/469-superlinear-skt-nonlocal-to-local-limit.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/13ab904c45cb6205f534546826d0b88208834692/research/solutions/superlinear-skt-localization).

**Claim compared.** The full superlinear multispecies nonlocal-to-local limit, with strong pressure/reaction convergence and original no-flux/initial terms.

**Fresh query terms.** `"superlinear" "nonlocal" "local limit" "cross-diffusion" 2026`.

**Primary-source evidence.**

- Peter Hirvonen; Ansgar Jüngel; Annamaria Pollino, [Superlinear nonlocal diffusion systems for multispecies populations: well-posedness and discrete chain rules](https://arxiv.org/html/2609.09921v1) (2026-09-09). Locator: Theorem 1, assumptions(A1)–(A5a), numerical-limit discussion. Fixed-nonlocal global strong existence; limit illustrated numerically.
- Gonzalo Galiano; Julián Velasco, [Convergence of solutions of a rescaled evolution nonlocal cross-diffusion problem to its local diffusion counterpart](https://doi.org/10.1007/s13398-022-01231-7) (2022). Locator: Main convergence theorem. Two-species s=1 limit.

**Exact scope comparison.** Fixed-epsilon well-posedness and numerical localization do not establish compactness and flux passage as epsilon vanishes. The earlier two-species linear-power theorem does not include every n>=2 and s>1. No earlier complete matching theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 156 — AIM 460: singular stable cone uniqueness

Submitted **2026-10-15T09:08:22Z**; head `21242c912966a018dfa8f0f48f61f493b67f1cda`. [PR](https://github.com/MColbrook/AIM/pull/156) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/460-singular-stable-cone-positive-solution-uniqueness.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/21242c912966a018dfa8f0f48f61f493b67f1cda/research/solutions/460-singular-stable-cone-positive-solution-uniqueness).

**Claim compared.** Positive proportionality for continuous stable-harmonic profiles outside every convex cone, with separate growth below2s and possibly atomic spectral measure.

**Fresh query terms.** `"singular" "stable" "cone" "uniqueness" harmonic 2026`.

**Primary-source evidence.**

- Xavier Fernández-Real; Xavier Ros-Oton, [Integro-Differential Elliptic Equations](https://arxiv.org/pdf/2411.12455v1) (2024-11-19 author draft; 2024 book). Locator: General spectral-measure class; cone uniqueness open question. Distinguishes measure ellipticity from stronger density classes.
- Xavier Ros-Oton; Marvin Weidner, [Obstacle problems for nonlocal operators with singular kernels](https://arxiv.org/html/2308.01695v1) (2023-08-03 preprint; 2026 volume). Locator: §4 and Lemma 4.8; angular Lp hypotheses. Related cone/blowup classification under stronger angular integrability.

**Exact scope comparison.** Density Lp comparison does not contain finitely supported spectral measures. A result assuming homogeneous or monotone profiles also does not prove proportionality of both arbitrary sub-2s growth profiles. No earlier theorem with all target quantifiers verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 157 — AIM 474: proposed existence proof for point-source fractional diffusion on manifolds

Submitted **2026-10-15T09:24:18Z**; head `8a377b721755a4909aa7608b893abf0cc9c03c41`. [PR](https://github.com/MColbrook/AIM/pull/157) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/474-manifold-fractional-pme-point-source.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/8a377b721755a4909aa7608b893abf0cc9c03c41/research/solutions/474-manifold-fractional-pme-point-source).

**Claim compared.** Existence of a point-source fractional PME solution on every stated lower-Ricci/Faber–Krahn manifold, with strong positive-time L1 continuity and bounded-continuous-test point trace.

**Fresh query terms.** `"fractional porous medium" "manifolds" "fundamental" "solution" 2026`.

**Primary-source evidence.**

- Elvise Berchio; Matteo Bonforte; Gabriele Grillo; Matteo Muratori, [The fractional porous medium equation on noncompact Riemannian manifolds](https://arxiv.org/pdf/2109.10732v2) (2021 preprint; 2023-09-21 v2; 2024 volume). Locator: Theorem 2.6, Proposition 5.1 and §7. Integrable-data semigroup/smoothing; fundamental solutions listed separately.
- Gabriele Grillo, [The Fractional Porous Medium Equation on noncompact Riemannian manifolds](https://ems.press/content/serial-article-files/51358?nt=1) (2025, Oberwolfach Report 14/2025). Locator: Printed pp.597–598, contribution's final paragraph. Fundamental-solution existence remains a stated question.

**Exact scope comparison.** Euclidean measure-data theorems and bounded/integrable manifold-data existence omit the general point-mass limit and tight initial trace. The newer nonnegative-Ricci potential theory also does not include all lower-Ricci manifolds and this Dirac statement. No earlier complete matching result verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 158 — AIM 473: proposed resolution of fractional PME mass conservation

Submitted **2026-10-15T09:32:19Z**; head `60a2396440ccdeab2c3a0090c91d1164433845a5`. [PR](https://github.com/MColbrook/AIM/pull/158) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/473-manifold-fractional-pme-mass-conservation.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/60a2396440ccdeab2c3a0090c91d1164433845a5/research/solutions/473-manifold-fractional-pme-mass-conservation).

**Claim compared.** Mass conservation at every finite time for every spatially integrable weak dual solution in the specified Green-weighted class on all lower-Ricci/Faber–Krahn manifolds.

**Fresh query terms.** `"fractional porous medium" "mass conservation" manifold 2026`.

**Primary-source evidence.**

- Elvise Berchio; Matteo Bonforte; Gabriele Grillo; Matteo Muratori, [The fractional porous medium equation on noncompact Riemannian manifolds](https://arxiv.org/pdf/2109.10732v2) (2021 preprint; 2023-09-21 v2; 2024 volume). Locator: §7, mass-conservation question. All-solution conservation distinguished from existence/upper bounds.
- Dorothea-Enrica von Criegern; Gabriele Grillo; Dario Daniele Monticelli, [Fractional porous medium equation on manifolds with nonnegative Ricci curvature: existence of solutions and smoothing effects via potential methods](https://arxiv.org/html/2609.12954v1) (2026-09-11). Locator: Assumptions and main existence/smoothing theorems. Nonnegative-Ricci potential theory for constructed solutions.

**Exact scope comparison.** Ricci>=0 is stronger than the allowed negative lower bound, and existence/smoothing for constructed solutions does not establish an equality for every integrable WDS without uniqueness. Time-fractional or Euclidean mass-conservation results concern different settings. No earlier complete matching theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 159 — AIM 402: proposed logarithmic convexity for two subdiffusion orders

Submitted **2026-10-15T10:49:41Z**; head `404bb40f6a5f795b8c61ff2abc0b3914dd003e0b`. [PR](https://github.com/MColbrook/AIM/pull/159) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/402-mixed-order-fractional-logarithmic-convexity.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/404bb40f6a5f795b8c61ff2abc0b3914dd003e0b/research/solutions).

**Claim compared.** Product-L2 logarithmic convexity with exactly t/T exponents, arbitrary initial data, all unequal subdiffusion orders and all bounded smooth domains.

**Fresh query terms.** `"mixed-order" "logarithmic convexity" "Chorfi"`.

**Primary-source evidence.**

- Salah-Eddine Chorfi, [Logarithmic convexity of evolution equations and application to inverse problems](https://arxiv.org/html/2506.19954v1) (2025-06-24). Locator: §5, Open Problem 1. Displays the exact unequal-order coupled system.
- Salah-Eddine Chorfi; Lahcen Maniar; Masahiro Yamamoto, [The backward problem for time-fractional evolution equations](https://arxiv.org/abs/2211.16493) (2022 preprint; 2024 publication). Locator: Logarithmic-convexity theorem. Single/common Caputo-order framework.

**Exact scope comparison.** A common-order spectral expansion cannot be applied after diagonalizing a coupling matrix when the two Caputo orders differ. Existing forward well-posedness and backward stability estimates also do not imply the precise product-norm t/T inequality. No earlier complete matching theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 160 — AIM 403: a lower control-cost exponent excluding L^2/4

Submitted **2026-10-15T11:10:08Z**; head `1957fa687fa60c26c51fd16017b91f43c4e60e14`. [PR](https://github.com/MColbrook/AIM/pull/160) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/403-schrodinger-sharp-fast-control-exponent.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/1957fa687fa60c26c51fd16017b91f43c4e60e14/research/solutions/403-schrodinger-control-lower-bound).

**Claim compared.** For one-end Dirichlet control of complex Schrödinger evolution, C_S>=c_L T^(7/2) exp(L²/(pi T)), disproving the proposed L²/4 coefficient.

**Fresh query terms.** `"Schrödinger" "control cost" "1/pi" "Lissy"`.

**Primary-source evidence.**

- Pierre Lissy, [Effective multipliers for weights whose log are Hölder continuous. Application to the cost of fast boundary controls for the 1D Schrödinger equation](https://arxiv.org/html/2502.04859v1) (2025-02-07). Locator: §§3.1–3.2, conjecture before Theorem 3.1. States best-known L²/4 lower bound and conjectured optimality.
- Pierre Lissy, [Explicit lower bounds for the cost of fast controls for some 1-D parabolic or dispersive equations, and a new lower bound concerning the uniform controllability of the 1-D transport-diffusion equation](https://cermics.gitlab.enpc.fr/lissy/Publi/chal.pdf) (2015). Locator: Historical lower-bound comparison; primary 2025 paper confirms its scope. Full direct-host text not available during this audit.

**Exact scope comparison.** A lower bound L²/4 leaves the conjecture possible; it is not the stronger L²/pi obstruction. Control-norm versus squared-norm conventions and heat-equation exponents must not be interchanged. No earlier full matching stronger lower bound verified; the 2015 access limitation is explicit.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 161 — AIM 042: proposed fixed-format selected bidiagonal SVD construction

Submitted **2026-10-15T13:29:44Z**; head `951b78861d0a47ad35322f10454e51614d7691dd`. [PR](https://github.com/MColbrook/AIM/pull/161) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/042-accurate-bidiagonal-svd.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/951b78861d0a47ad35322f10454e51614d7691dd/research/solutions/042-selected-bidiagonal-directions).

**Claim compared.** A fixed-format selected bidiagonal SVD theorem with both coupling residuals and separate left/right gap-independent orthogonality, using very large protected internal precision.

**Fresh query terms.** `"bidiagonal" "SVD" "O(nk)" accurate 2026`.

**Primary-source evidence.**

- Noah Amsel and coauthors, [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394) (2026-02-05 v1; 2026-08-21 v3). Locator: Problem 3.8, §3.4. Exact coupling/orthogonality problem remains posed in v3.
- Paul R. Willems; Bruno Lang; Christof Vömel, [Computing the Bidiagonal SVD Using Multiple Relatively Robust Representations](https://www.netlib.org/lapack/lawnspdf/lawn166.pdf) (2005 technical report; 2006 publication). Locator: Abstract and implementation/accuracy analysis. O(nk) design; not a universal guarantee for every difficult matrix.
- Maximilian Behr / OpenTorus contributors, [OpenTorus: Simons eigenvalue problem notes](https://github.com/maximilianbehr/OpenTorus/blob/main/examples/simons-eigenvalue-problems/notes.md) (2026; current page accessed 2026-10-21). Locator: Problem 3.8 section. Records that earlier implementations were ruled unreliable for LAPACK.

**Exact scope comparison.** An O(nk) implementation headline alone does not prove all requested ordered-value, two-residual and two-orthogonality guarantees independently of gaps. The 2026 workshop and primary project notes distinguish unresolved reliability. No earlier complete theorem for the submission's declared precision/output model verified; no replacement justified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 162 — AIM 411: full continuity solution claim for bounded admissible inputs

Submitted **2026-10-15T13:35:07Z**; head `b9b2b7c64b7a18bc805acca39e40aca6c0ab53b9`. [PR](https://github.com/MColbrook/AIM/pull/162) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/411-bounded-input-state-continuity.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/b9b2b7c64b7a18bc805acca39e40aca6c0ab53b9/research/solutions/411-bounded-input-state-continuity).

**Claim compared.** Every Bochner L-infinity-admissible control operator on arbitrary Banach state/input spaces has continuous state trajectories; a uniform small-horizon norm limit is additionally claimed.

**Fresh query terms.** `"bounded input" "state continuity" admissibility Weiss problem solved 2026`; `"Weiss" "Problem 2.4" admissibility continuity solved`.

**Primary-source evidence.**

- Philip Preußler; Felix L. Schwenninger, [Implications of structured continuous maximal regularity](https://arxiv.org/html/2605.12121v1) (2026-05-12). Locator: §4.4, Corollary 4.10 and following paragraph. Continuity under specified state-space/input-space geometry.

**Exact scope comparison.** Corollary 4.10 assumes reflexivity, nontrivial type, a c0/property(V) alternative, or a WCG/Grothendieck alternative. None is in the original arbitrary-Banach target. Earlier analytic-Hilbert/finite-dimensional-input theorems are also narrower. No complete earlier arbitrary-Banach result verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 163 — AIM 482: proposed counterexample for a reversible cubic reaction-diffusion system

Submitted **2026-10-15T13:38:42Z**; head `9aabeaaf7407f10ca578391fa632de4f2b1d3c32`. [PR](https://github.com/MColbrook/AIM/pull/163) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/482-entropy-reaction-diffusion-renormalized-uniqueness.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/9aabeaaf7407f10ca578391fa632de4f2b1d3c32/research/solutions).

**Claim compared.** Two distinct full-class renormalized solutions of reversible A+2B<->3B on the 3D ball, with equal diffusion and common singular finite-entropy initial data.

**Fresh query terms.** `"entropy" "reaction diffusion" "nonuniqueness" reversible 2026`; `"renormalized" "reaction-diffusion" "non-uniqueness"`.

**Primary-source evidence.**

- Julian Fischer, [Weak-strong uniqueness of solutions to entropy-dissipating reaction-diffusion equations](https://arxiv.org/abs/1703.00730) (2017-03 preprint; 2017 publication). Locator: Definition 2 and Theorem 7. Uniqueness in comparison with an existing bounded strong solution.
- Antonio Agresti; Michael Kniely; Bao Quoc Tang, [Global classical solutions by transport noise for reaction–diffusion systems with entropy dissipation](https://arxiv.org/abs/2608.13332) (2026-08 preprint). Locator: §1.1. Discusses unresolved deterministic renormalized uniqueness.

**Exact scope comparison.** Weak–strong uniqueness assumes a bounded strong comparator and does not include two singular-data renormalized solutions in the target class. Scalar semilinear heat nonuniqueness is a possible mechanism but does not verify entropy-dissipating reversible mass-action kinetics and all cutoff identities. No earlier complete matching counterexample verified. PR 177 changes attribution, not this theorem.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 164 — AIM 252: proposed resolution of self-ball Minkowski integrability

Submitted **2026-10-15T13:49:27Z**; head `ec0a45a8a976049a4fdd6f52af3f618868f414ed`. [PR](https://github.com/MColbrook/AIM/pull/164) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/252-self-ball-minkowski-integrability.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/ec0a45a8a976049a4fdd6f52af3f618868f414ed/research/solutions/252-self-ball-minkowski-integrability).

**Claim compared.** Every smooth strongly convex planar norm whose billiard inside its own unit ball is totally integrable must be an inner-product norm, with no extra rotational symmetry.

**Fresh query terms.** `"Minkowski" "self" "integrability" "Ostrover" 2026`.

**Primary-source evidence.**

- Misha Bialy; Andrey E. Mironov, [Integrable Billiards and Related Topics](https://arxiv.org/html/2510.03790v1) (2025-10 preprint; ICM2026 proceedings). Locator: §9.5, Question 1. Exact Ostrover self-ball question.
- Misha Bialy; Daniel Tsodikovich, [Billiard tables with rotational symmetry](https://arxiv.org/abs/2106.06956) (2021-06 preprint; 2023 publication). Locator: Minkowski-billiard rigidity theorem. Requires a finite linear symmetry of order at least3.
- Luca Baracco; Olga Bernardi, [Totally integrable symplectic billiards are ellipses](https://arxiv.org/abs/2305.19701) (2023-05 preprint). Locator: Main theorem. One-table symplectic billiards, not the general alternating self-ball Minkowski setting.

**Exact scope comparison.** A norm has only mandatory central symmetry, of order2; an order>=3 rigidity theorem cannot be applied universally. Correspondence with alternating symplectic tables does not meet a one-table theorem's hypotheses without an additional argument. No earlier full matching rigidity theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 165 — AIM 485: proposed optimal obstacle regularity for integrable angular densities

Submitted **2026-10-15T14:57:10Z**; head `5c6c10c9a57fed12f0c6e703029d6c7c50e4c289`. [PR](https://github.com/MColbrook/AIM/pull/165) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/485-general-stable-obstacle-optimal-regularity.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/5c6c10c9a57fed12f0c6e703029d6c7c50e4c289/research/solutions/485-general-stable-obstacle-optimal-regularity).

**Claim compared.** Global C^(1,s) estimate for every finite-energy obstacle minimizer with only even L1 angular density and the target's mass/moment bounds.

**Fresh query terms.** `"obstacle" "angular" "L1" "regularity" Ros-Oton Weidner 2026`.

**Primary-source evidence.**

- Xavier Ros-Oton; Marvin Weidner, [Obstacle problems for nonlocal operators with singular kernels](https://arxiv.org/html/2308.01695v1) (2023-08-03 preprint; 2026 volume). Locator: Theorem 1.3 and following open paragraph; Proposition 5.8. Global theorem assumes angular Lp with p>n/(2s); local flatness proposition is broader.
- Florian Grube; Xavier Ros-Oton, [Boundary regularity for general elliptic operators of order2s](https://arxiv.org/html/2605.18711v1) (2026-05 preprint). Locator: Theorem 1.1. Linear boundary/half-line regularity, not the global obstacle estimate.
- Xavier Ros-Oton; Marvin Weidner, [Optimal regularity for nonlocal elliptic equations and free boundary problems](https://arxiv.org/abs/2403.07793) (2024-03-12). Locator: Equations(1.1)–(1.2), Theorem 1.3. Kernels pointwise comparable to the fractional Laplacian.

**Exact scope comparison.** The source explicitly leaves the p=1 blowup classification unresolved. A broad local flatness criterion still needs a global classification/compactness argument before it gives the estimate for all L1 densities. No earlier complete matching global theorem verified. The 2024 optimal theorem imposes pointwise two-sided bounds, absent from the merely integrable angular-density target.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 166 — AIM 455: deterministic Hölder exponent for smooth transport SPDEs

Submitted **2026-10-15T15:44:34Z**; head `cfac7195abf3194016de5c355177b472df8859f2`. [PR](https://github.com/MColbrook/AIM/pull/166) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/455-smooth-transport-spde-deterministic-holder-exponent.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/cfac7195abf3194016de5c355177b472df8859f2/research/solutions).

**Claim compared.** One deterministic positive parabolic Hölder exponent for scalar variational SPDEs with measurable diffusion and general smooth progressive noncommuting transport noise.

**Fresh query terms.** `"transport noise" "deterministic" "Hölder exponent" Agresti`.

**Primary-source evidence.**

- Antonio Agresti; Max Sauerbrey; Mark Veraar, [A stochastic flow approach to De Giorgi–Nash–Moser estimates for SPDEs with smooth transport noise](https://arxiv.org/html/2511.12692v1) (2025-11-16 preprint; HTML manuscript dated 2026-08-24). Locator: §1.2; Theorem 3.4; Proposition 4.3. General pathwise/localized exponents; deterministic exponent under bounded flow distortion/constant or special commuting flows.

**Exact scope comparison.** Proposition 4.3's deterministic distortion bound does not follow from deterministic Cj coefficient bounds for arbitrary noncommuting stochastic flows. Its special cases are explicitly excluded as extra assumptions in the target. No earlier theorem with the requested general deterministic exponent verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 167 — AIM 457: proposed resolution of transport-noise Navier-Stokes at negative-half smoothness

Submitted **2026-10-15T16:11:29Z**; head `b673e462dea5019dccd17d70a2f292501c6e6958`. [PR](https://github.com/MColbrook/AIM/pull/167) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/457-stochastic-navier-stokes-negative-half-critical-data.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/b673e462dea5019dccd17d70a2f292501c6e6958/research/solutions/transport-noise-navier-stokes-negative-half-data).

**Claim compared.** Local heat-mild well-posedness at inhomogeneous B^(-1/2)_(6,4) for all admitted smooth compactly supported transport fields, including full-class pathwise uniqueness and stopped stability.

**Fresh query terms.** `"Navier Stokes" "transport noise" "negative" "half" Besov 2026`.

**Primary-source evidence.**

- Antonio Agresti; Mark Veraar, [Nonlinear SPDEs and Maximal Regularity: An Extended Survey](https://arxiv.org/html/2501.18561v3) (2025-09-01 publication; arXiv v3 accessed2026-10-21). Locator: Theorem 8.26; Problem 10. Explicitly asks for critical smoothness at most−1/2.
- Antonio Agresti, [On the absence of blow-up in the3D Navier–Stokes equations with transport noise](https://arxiv.org/abs/2607.15140) (2026-07-16 v1; 2026-09-09 v4). Locator: Abstract and local/noise-selection assumptions. Suitably chosen noise and initial data of positive subcritical smoothness.

**Exact scope comparison.** The linear stochastic Stokes theorem is not the endpoint nonlinear theorem with L4L6 uniqueness. High-probability global regularization for selected noises and positive-smoothness data also does not include all prescribed fields and arbitrary negative-half data. No earlier full matching endpoint theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 168 — AIM 478: critical stochastic SQG

Submitted **2026-10-15T16:59:03Z**; head `8b2504c4a03a1097ea45cec49d2bbc5ef057dce9`. [PR](https://github.com/MColbrook/AIM/pull/168) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/478-critical-stochastic-sqg-global-regularity.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/8b2504c4a03a1097ea45cec49d2bbc5ef057dce9/research/solutions/478-critical-stochastic-sqg-global-regularity).

**Claim compared.** Global pathwise-unique H3 solutions of the critically dissipative stochastic SQG equation for every finite smooth globally Lipschitz state-dependent coefficient family, without smallness.

**Fresh query terms.** `"critical" "stochastic" "SQG" global "multiplicative" 2026`; `"critical stochastic" "quasi-geostrophic" "global" "nonlinear" noise`.

**Primary-source evidence.**

- Antonio Agresti; Mark Veraar, [Nonlinear SPDEs and Maximal Regularity: An Extended Survey](https://arxiv.org/html/2501.18561v3) (2025-09-01 publication; arXiv v3 accessed2026-10-21). Locator: Theorem 8.22; Remark8.23. Global theorem excludes alpha=1/2 and explicitly labels stochastic critical case open.
- Tongtong Liang; Yejuan Wang, [Sub-critical and critical stochastic quasi-geostrophic equations with infinite delay](https://www.aimsciences.org/article/doi/10.3934/dcdsb.2020309) (2020-10-22 online; 2021 volume). Locator: Abstract and critical local pathwise theorem. Critical dissipation: local solutions for s>1.

**Exact scope comparison.** Global deterministic critical SQG or subcritical stochastic SQG does not supply the nonlinear multiplicative critical stochastic theorem. Local critical pathwise theory and special additive/affine-noise results are narrower. No earlier complete matching global theorem verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## PR 169 — AIM 481: full-target finite propagation proof for fourth-order aggregation-diffusion

Submitted **2026-10-15T17:23:39Z**; head `b6b71783ccda5a22cefcc844c321ecfd85d89a74`. [PR](https://github.com/MColbrook/AIM/pull/169) · [Original target](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/481-fourth-order-aggregation-finite-propagation.md) · [Submitted package](https://github.com/yuiyuiui/AIM/tree/b6b71783ccda5a22cefcc844c321ecfd85d89a74/research/solutions/481-fourth-order-aggregation-finite-propagation).

**Claim compared.** A global finite-propagation weak solution in every d>=2 for arbitrary compact H1 probability data and any chi>0, with the exact narrow/H1/H2/all-endpoint identity.

**Fresh query terms.** `"fourth-order" "aggregation" "finite propagation" Carrillo`; `"thin film" "backwards second order" "multidimensional" propagation`; `"finite speed" "unstable thin film" dimensions`.

**Primary-source evidence.**

- José Antonio Carrillo; Antonio Esposito; Carles Falcó; Alejandro Fernández-Jiménez, [Competing effects in fourth-order aggregation-diffusion equations](https://arxiv.org/html/2307.14706v1) (2023-07-27 preprint; 2024 publication). Locator: Definition 2.1, Theorem 2.2 and §4. Global gradient-flow existence and regularity; finite propagation is an extra target.
- Roman M. Taranets; John R. King, [On an unstable thin-film equation in multi-dimensional domains](https://www.researchgate.net/publication/257318859_On_an_unstable_thin-film_equation_in_multi-dimensional_domains) (2013-06-09 online; 2014 volume). Locator: Theorem 1; dimension/exponent hypotheses; §5. Bounded-domain existence with dimension/exponent restrictions. [Publisher record](https://link.springer.com/article/10.1007/s00030-013-0240-3). Author-uploaded full manuscript read; publisher identity confirmed at DOI10.1007/s00030-013-0240-3.
- Marina Chugunova; Mary C. Pugh; Roman M. Taranets, [Research Announcement: Finite-time Blow Up and Long-wave Unstable Thin Film Equations](https://arxiv.org/abs/1008.0385) (2010-08-02). Locator: Abstract and equation. One-dimensional finite-propagation theory.

**Exact scope comparison.** Existing JKO existence omits support preservation. One-dimensional unstable thin-film propagation does not prove arbitrary d>=2, while bounded-domain existence in restricted dimensions is not a whole-space finite-support result. No earlier complete theorem meeting all dimension/data/weak-formulation requirements verified.

**Recommendation:** `no_verified_earlier_complete_match`. Retain the hosted submission and current status (**Solved**); do not infer a novelty guarantee.

## Evidence limits

- Date precision is stated as available: exact version/publication days where verified, otherwise bibliographic year or month. No replacement is recommended from an incompletely accessed source.
- No-match findings retain current status; AIM 423 is a domain clarification already classified Partially resolved. These findings neither reprove nor recertify any accepted manuscript.
- Own earlier versioned work is treated as an acknowledged dependency rather than an independent duplicate.
- Current package references were read for leads; previous AI novelty statements were not used as evidence. Fresh target-specific web queries and primary-source scope checks were performed on 21 October 2026.
- The inventory fixes submission timestamps and head SHAs. The exact original targets and mathematical package claims are the comparison baseline; AIM 482 later authorship correction does not change its mathematical claim.
