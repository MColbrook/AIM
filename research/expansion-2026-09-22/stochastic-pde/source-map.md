# Stochastic and nonlocal PDE source map — 22 September 2026

36 additions, all involving PDEs or their variational or stochastic formulations. Principal sources include Fernández-Real and Ros-Oton’s *Integro-Differential Elliptic Equations* (2024), Vázquez’s *The Porous Medium Equation* (2007), and the extended Agresti–Veraar survey (2025), together with specific SIAM papers and current primary preprints. Each entry identifies its unresolved assertion and relevant later partial results. The final obstacle candidate was researched by the PDE agent and read against the book and singular-kernel paper by the root agent.

## 1. Bounded-Hessian Liouville rigidity in dimensions three and four

Admitted page: [fully-nonlinear-bounded-hessian-liouville](../../../problems/452-fully-nonlinear-bounded-hessian-liouville.md)

1. C. Mooney, *Bernstein theorems for nonlinear geometric PDEs* (2024), §2, equation (4) and the discussion following it. [Author manuscript](https://arxiv.org/abs/2407.11903).
2. D. Li and L. Liang, *A new proof for the Liouville theorem of fully nonlinear elliptic equations*, Discrete Contin. Dyn. Syst. B **30** (2025), 4643–4650, Theorem 1.1. [Article](https://doi.org/10.3934/dcdsb.2025071); [preprint](https://arxiv.org/abs/2501.19075).
3. L. Liang, *Liouville theorem for fully nonlinear elliptic equations with the small oscillation and the periodicity in $`x`$ and the periodic right hand term* (2026 preprint), Theorem B and the subsequent hypotheses. [Preprint](https://arxiv.org/abs/2603.10797).

Mooney explicitly identifies dimensions three and four as open, with dimension two known and counterexamples in higher dimensions. Searches on 2026-09-22 located the 2025 and March 2026 Liouville papers. Reading their hypotheses confirms convexity/concavity restrictions in dimension at least three; their titles alone could misleadingly suggest a resolution. No matching result for smooth, general uniformly elliptic $`F`$ was found.

## 2. Bourgain–Spencer accuracy for random elliptic media at finite contrast

Admitted page: [bourgain-spencer-nonperturbative-homogenization](../../../problems/453-bourgain-spencer-nonperturbative-homogenization.md)

1. M. Duerinckx, *Non-perturbative approach to the Bourgain–Spencer conjecture in stochastic homogenization*, J. Math. Pures Appl. **176** (2023), 183–225, Conjecture 1 and Definition 3.3. [Article](https://doi.org/10.1016/j.matpur.2023.06.005); [author manuscript](https://arxiv.org/abs/2102.06319).
2. M. Duerinckx, M. Lemm and F. Pagano, *On Bourgain's approach to stochastic homogenization*, Arch. Ration. Mech. Anal. **249**, 81 (2025), §2.3 and Remark 2.3. [Author manuscript](https://arxiv.org/abs/2406.09909).

The statement specializes Conjecture 1 to smooth finite-range Gaussian-generated coefficients and spells out its higher-order proxy, avoiding an ill-posed truncated high-order PDE. The 2025 paper still requires small contrast and explicitly leaves the non-perturbative improvement open. Searches on 2026-09-22 for Bourgain–Spencer, non-perturbative ensemble averages, proofs and counterexamples, including the authors' publication lists, found no full finite-contrast resolution. The $`d-\eta`$ non-perturbative accuracy and contrast-dependent $`2d-\delta K-\eta`$ results do not give the assertion above.

## 3. Hölder continuity for parabolic SPDEs with merely bounded transport noise

Admitted page: [rough-transport-spde-holder](../../../problems/454-rough-transport-spde-holder.md)

1. A. Agresti, M. Sauerbrey and M. Veraar, *A stochastic flow approach to De Giorgi–Nash–Moser estimates for SPDEs with smooth transport noise* (2025 preprint, manuscript dated August 2026), Theorem 1.1, §1.2 and §4. [Full manuscript](https://arxiv.org/html/2511.12692v1).

The first open question in §1.2 asks to remove the spatial regularity of the transport coefficients while retaining boundedness and stochastic parabolicity. The source proves Hölder regularity for sufficiently smooth transport fields and explains why earlier pointwise-probability continuity does not imply the requested simultaneous pathwise regularity. Searches on 2026-09-22 for rough-transport stochastic De Giorgi estimates and later work of the authors found no matching theorem. The random exponent is allowed here; this is distinct from obtaining a deterministic exponent for smooth noise.

## 4. A deterministic Hölder exponent for smooth-transport parabolic SPDEs

Admitted page: [smooth-transport-spde-deterministic-holder-exponent](../../../problems/455-smooth-transport-spde-deterministic-holder-exponent.md)

1. A. Agresti, M. Sauerbrey and M. Veraar, *A stochastic flow approach to De Giorgi–Nash–Moser estimates for SPDEs with smooth transport noise* (2025 preprint, manuscript dated August 2026), Theorem 1.1, §1.2 and §4. [Full manuscript](https://arxiv.org/html/2511.12692v1).

This is the second open question of §1.2. Theorem 1.1 gives positive sample-dependent exponents; Proposition 4.3 obtains deterministic ones only with extra structure. The example of an unbounded ellipticity ratio after the stochastic-flow transformation is an obstruction to that method, not a counterexample to the assertion. Searches on 2026-09-22 for uniform stochastic Hölder exponents and later De Giorgi–Nash–Moser results found no theorem for the full stated class. This keeps the smooth-noise hypothesis, unlike the separate rough-noise regularity problem.

## 5. Global quadratic reaction–diffusion systems with general transport noise

Admitted page: [quadratic-mass-controlled-rd-transport-noise](../../../problems/456-quadratic-mass-controlled-rd-transport-noise.md)

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), Open Problem 8 and §8.2. [Article](https://doi.org/10.1007/s00030-025-01090-2).
2. A. Agresti and M. Veraar, *Reaction-Diffusion Equations with Transport Noise and Critical Superlinear Diffusion: Global Well-Posedness of Weakly Dissipative Systems*, SIAM J. Math. Anal. (2024). [Article](https://doi.org/10.1137/23M1562482).
3. A. Agresti, M. Kniely and B. Q. Tang, *Global classical solutions by transport noise for reaction–diffusion systems with entropy dissipation* (2026 preprint), Introduction. [Preprint](https://arxiv.org/abs/2608.13332).
4. D. Milesis and M. Salins, *Global in time solutions to stochastic reaction-diffusion systems with superlinear reactions satisfying a triangular control of mass* (2026 preprint). [Preprint](https://arxiv.org/abs/2604.06645).

The survey explicitly poses this quadratic mass-control extension. Searches on 2026-09-22 checked the subsequent stochastic De Giorgi paper and the two 2026 global-existence papers. The August result selects a special transport noise and gives arbitrarily high probability, while the desired assertion quantifies over every admissible noise and asks probability one. Milesis–Salins impose triangular mass control and noise without spatial derivatives. Neither covers these species-dependent transport fields and general quadratic reactions. Deterministic quadratic mass-control global existence is already known and is not counted as open here.

## 6. Transport-noise Navier–Stokes at critical smoothness minus one half

Admitted page: [stochastic-navier-stokes-negative-half-critical-data](../../../problems/457-stochastic-navier-stokes-negative-half-critical-data.md)

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), Open Problem 10 and Theorem 8.26. [Article](https://doi.org/10.1007/s00030-025-01090-2).
2. A. Agresti, *On the absence of blow-up in the 3D Navier–Stokes equations with transport noise* (2026 preprint), local theory and noise-selection hypotheses. [Preprint](https://arxiv.org/abs/2607.15140).

This fixes an endpoint case of Open Problem 10, rather than asking vaguely for the largest critical space. The existing result covers smoothness strictly above $`-1/2`$ (spatial integrability below six); the requested $`B^{-1/2}_{6,4}`$ and $`L^4_tL^6_x`$ norms have the Navier–Stokes critical scaling at high frequencies. Searches on 2026-09-22 checked critical Besov transport-noise theory and recent global-noise results. Results for lower-order multiplicative noise, including general $`L^3`$ initial data, do not treat the derivative noise above. No matching endpoint theorem was found.

## 7. Local no-slip Navier–Stokes theory under non-small transport noise

Admitted page: [stochastic-navier-stokes-no-slip-local](../../../problems/458-stochastic-navier-stokes-no-slip-local.md)

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), Open Problem 9. [Article](https://doi.org/10.1007/s00030-025-01090-2).
2. D. Goodair, *Navier-Stokes Equations with Navier Boundary Conditions and Stochastic Lie Transport: Well-Posedness and Inviscid Limit*, discussion of the no-slip obstruction. [Author manuscript](https://arxiv.org/abs/2308.04290).
3. D. Goodair, *Anisotropic Inviscid Limit for the Navier-Stokes Equations with Transport Noise Between Two Plates* (2026 preprint). [Preprint](https://arxiv.org/abs/2603.13199).

Open Problem 9 requests a non-small-noise local theory for no-slip domains; the statement specifies one subcritical maximal-regularity solution class. Searches on 2026-09-22 checked Goodair's boundary results and 2026 transport-noise papers. Navier-slip strong solutions do not impose the displayed zero trace, and the 2026 no-slip inviscid-limit theorem uses weak martingale solutions rather than this pathwise unique local class. Perturbative small-noise arguments do not establish the full parabolicity range.

## 8. Higher regularity for concave stable nonlocal equations

Admitted page: [concave-nonlocal-higher-regularity](../../../problems/459-concave-nonlocal-higher-regularity.md)

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. X. Ros-Oton, C. Torres-Latorre and M. Weidner, *Semiconvexity estimates for nonlinear integro-differential equations*, Comm. Pure Appl. Math. (2025), Introduction. [Article](https://doi.org/10.1002/cpa.22237).

Open Question 3.1 in the book asks whether smooth kernels give $`C^{1+s+\alpha}`$ regularity. The displayed homogeneous equation is its translation-invariant, zero-source formulation. The 2025 paper discusses the remaining gap beyond the established $`C^{\max\{1,2s\}+\varepsilon}`$ estimates. Searches on 2026-09-22 for concave nonlocal higher regularity and smooth stable kernels found no general theorem reaching the target. Linear Schauder estimates and the classical second-order Evans–Krylov theorem concern different operators.

## 9. Uniqueness of positive harmonic profiles for singular stable operators in cones

Admitted page: [singular-stable-cone-positive-solution-uniqueness](../../../problems/460-singular-stable-cone-positive-solution-uniqueness.md)

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. X. Ros-Oton and M. Weidner, *Obstacle problems with singular kernels*, Ann. Scuola Norm. Sup. Pisa Cl. Sci. **27** (2026), 535–588, Introduction and angular integrability assumptions. [Article](https://doi.org/10.2422/2036-2145.202309_010); [preprint](https://arxiv.org/abs/2308.01695).

This is the integrable-growth version of Open Question 4.4. The published 2026 paper obtains results under an $`L^p`$ angular-density hypothesis with $`p>n/(2s)`$ and explicitly identifies the general stable class as unresolved. Its preprint dates from 2023; publication in 2026 is not a new resolution for singular spectral measures. Searches on 2026-09-22 for positive cone profiles and singular stable boundary Harnack principles found no general uniqueness result. Interior Harnack inequalities themselves may fail in this class.

## 10. Comparison for viscosity solutions of infinity-fractional diffusion

Admitted page: [infinity-fractional-evolution-comparison](../../../problems/461-infinity-fractional-evolution-comparison.md)

1. F. del Teso, J. Endal, E. R. Jakobsen and J. L. Vázquez, *Evolution driven by the infinity fractional Laplacian*, Calc. Var. PDE **62**, 136 (2023), viscosity definition, Theorem 2.6 and §§7, 9. [Article](https://doi.org/10.1007/s00526-023-02475-w); [preprint](https://arxiv.org/abs/2210.06414).

The paper constructs viscosity solutions but leaves their general uniqueness/comparison unresolved. Its comparison theorem requires one solution to be classical, and its explicit classical families have special symmetry or monotonicity. Searches on 2026-09-22 for infinity-fractional parabolic comparison, uniqueness and later work of the authors found no result covering two arbitrary viscosity solutions with the stated zero-gradient convention. The local infinity heat equation and the stationary nonlocal equation are different problems.

## 11. A finite-integrability ABP estimate for general nonlocal Pucci operators

Admitted page: [nonlocal-pucci-finite-integrability-abp](../../../problems/462-nonlocal-pucci-finite-integrability-abp.md)

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. N. Guillén and R. Schwab, *Aleksandrov–Bakelman–Pucci type estimates for integro-differential equations*, Arch. Ration. Mech. Anal. **206** (2012), 111–157, structured-kernel estimates. [Author preprint](https://arxiv.org/abs/1101.0279).
3. S. Kitano, *$`W^{\sigma,p}`$ a priori estimates for fully nonlinear integro-differential equations* (2022), the restricted matrix-kernel setting. [Preprint](https://arxiv.org/abs/2207.06728).

This is Open Question 3.3 in §3.6.2 of the book, with the extremal operator expanded explicitly. Searches on 2026-09-22 checked nonlocal ABP estimates, finite $`L^p`$ data and Kitano's later work. The located finite-integrability theorems impose matrix-angular structure on kernels; they do not cover the full Pucci class above. Existing $`L^\infty`$ source estimates do not imply a bound tending to zero with $`\|f_-\|_p`$.

## 12. Calderón–Zygmund estimates for general concave nonlocal equations

Admitted page: [concave-nonlocal-calderon-zygmund](../../../problems/463-concave-nonlocal-calderon-zygmund.md)

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. S. Kitano, *$`W^{\sigma,p}`$ a priori estimates for fully nonlinear integro-differential equations* (2022), Introduction and kernel hypotheses. [Author preprint](https://arxiv.org/abs/2207.06728).

Open Question 3.2 in §3.6.2 asks for this nonlocal $`W^{2s,p}`$ theory at sufficiently large $`p`$. The smooth-source estimate is a precise necessary form of that proposed theory and avoids ambiguity about viscosity solutions with discontinuous right sides. Searches on 2026-09-22 found restricted matrix-kernel and linear-operator estimates, but no estimate uniform over the general concave class. The separate ABP entry controls the maximum of a subsolution; here the target is a full-order Sobolev norm of solutions.

## 13. Hölder regularity under directional nonlocal ellipticity alone

Admitted page: [rough-jump-kernel-holder-regularity](../../../problems/464-rough-jump-kernel-holder-regularity.md)

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. R. W. Schwab and L. Silvestre, *Regularity for parabolic integro-differential equations with very irregular kernels*, Analysis & PDE **9** (2016), 727–772. [Article](https://doi.org/10.2140/apde.2016.9.727).

The statement is Open Question 3.4, with equations (3.6.3)–(3.6.5), in §3.6.4 of the book. Searches on 2026-09-22 checked directional ellipticity, singular jump kernels and rough-coefficient Hölder estimates. Located theorems require positive-measure directional lower bounds, comparable energy forms, or small spatial oscillation. New regularity from a coercive Hamiltonian does not apply to this homogeneous linear equation. No matching resolution was found.

## 14. Does directional ellipticity force a fractional energy bound?

Admitted page: [nonlocal-directional-ellipticity-coercivity](../../resolved/658-nonlocal-directional-ellipticity-coercivity.md)

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. J. Chaker and L. Silvestre, *Coercivity estimates for integro-differential operators*, Calc. Var. PDE **59**, 106 (2020). [Article](https://doi.org/10.1007/s00526-020-01764-y).

The book poses this precise coercivity question immediately after Open Question 2.1 in §2.8.1 and explains its link to divergence-form regularity. Searches on 2026-09-22 checked coercivity under annular second-moment bounds and later work on singular kernels. Known results require additional thickness or energy-comparability assumptions. This entry concerns the symmetric quadratic form, unlike the separate nondivergence-form pointwise equation.

## 15. Optimal nonlocal obstacle regularity with a minimally smooth obstacle

Admitted page: [nonlocal-obstacle-minimal-smoothness](../../../problems/465-nonlocal-obstacle-minimal-smoothness.md)

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. X. Ros-Oton, C. Torres-Latorre and M. Weidner, *Semiconvexity estimates for nonlinear integro-differential equations*, Comm. Pure Appl. Math. (2025), Theorem 1.3. [Article](https://doi.org/10.1002/cpa.22237).

This is Open Question 4.1 in §4.6.1. The cited theorem proves the estimate with $`\beta>1+2s`$; lowering that threshold to every $`\beta>1+s`$ is the gap. Searches on 2026-09-22 checked optimal obstacle regularity, low-regularity obstacles and later work of the authors. Results for the fractional Laplacian, smooth obstacles, or higher regularity of an already regular free boundary do not cover this anisotropic local estimate. No matching extension was located.

## 16. Multidimensional weak uniqueness for porous-medium flow with fractional pressure

Admitted page: [fractional-pressure-pme-multidimensional-uniqueness](../../../problems/466-fractional-pressure-pme-multidimensional-uniqueness.md)

1. D. Stan, F. del Teso and J. L. Vázquez, *Porous medium equation with nonlocal pressure* (2018), Definition 2.1, Theorems 5.1–5.5, Remark 7 and §7. [Author preprint](https://arxiv.org/abs/1801.04244).
2. D. Stan, F. del Teso and J. L. Vázquez, *Existence of weak solutions for a general porous medium equation with nonlocal pressure*, Arch. Ration. Mech. Anal. (2019), existence and energy estimates. [Author preprint](https://arxiv.org/abs/1609.05139).
3. F. del Teso and E. R. Jakobsen, *A Convergent Finite Difference-Quadrature Scheme for the Porous Medium Equation with Nonlocal Pressure*, Found. Comput. Math. (2026), §2's review of the PDE theory. [Article](https://doi.org/10.1007/s10208-026-09752-y).

4. G. Foghem, D. Padilla-Garza and M. Schmidtchen, *Gradient flow solutions for porous medium equations with nonlocal Lévy-type pressure*, Calc. Var. PDE **64**, 88 (2025). [Article](https://doi.org/10.1007/s00526-025-02942-6).

The survey explicitly distinguishes multidimensional weak uniqueness from the one-dimensional theorem and local smooth theory. Searches on 2026-09-22 checked subsequent uniqueness and gradient-flow results. The 2025 paper constructs gradient-flow solutions and proves uniqueness of discrete minimizers, which is not uniqueness of the continuous PDE. The 2026 paper's uniqueness theorem is one-dimensional. No matching theorem for the above multidimensional energy class was located.

## 17. Continuity for degenerate fractional-pressure porous-medium flow

Admitted page: [fractional-pressure-superquadratic-continuity](../../../problems/467-fractional-pressure-superquadratic-continuity.md)

1. D. Stan, F. del Teso and J. L. Vázquez, *Porous medium equation with nonlocal pressure* (2018), Definition 2.1, Theorems 5.1–5.5, Remark 7 and §7. [Author preprint](https://arxiv.org/abs/1801.04244).
2. D. Stan, F. del Teso and J. L. Vázquez, *Existence of weak solutions for a general porous medium equation with nonlocal pressure*, Arch. Ration. Mech. Anal. (2019), existence and energy estimates. [Author preprint](https://arxiv.org/abs/1609.05139).
3. F. del Teso and E. R. Jakobsen, *A Convergent Finite Difference-Quadrature Scheme for the Porous Medium Equation with Nonlocal Pressure*, Found. Comput. Math. (2026), §2's review of the PDE theory. [Article](https://doi.org/10.1007/s10208-026-09752-y).

Section 7 of the survey identifies continuity of weak solutions beyond $`m=2`$ as unresolved. Searches on 2026-09-22 for continuity, Hölder regularity and superquadratic mobility found no theorem covering this class. The known $`m=2`$ Hölder theory and regularity of $`u_t+(-\Delta)^s(u^m)=0`$ do not apply: the latter places the nonlinearity inside a different operator. This is a regularity question rather than another uniqueness or existence entry.

## 18. Instantaneous spreading for fractional-pressure flow in several dimensions

Admitted page: [fractional-pressure-multidimensional-instantaneous-spread](../../../problems/468-fractional-pressure-multidimensional-instantaneous-spread.md)

1. D. Stan, F. del Teso and J. L. Vázquez, *Porous medium equation with nonlocal pressure* (2018), Definition 2.1, Theorems 5.1–5.5, Remark 7 and §7. [Author preprint](https://arxiv.org/abs/1801.04244).
2. D. Stan, F. del Teso and J. L. Vázquez, *Existence of weak solutions for a general porous medium equation with nonlocal pressure*, Arch. Ration. Mech. Anal. (2019), existence and energy estimates. [Author preprint](https://arxiv.org/abs/1609.05139).
3. F. del Teso and E. R. Jakobsen, *A Convergent Finite Difference-Quadrature Scheme for the Porous Medium Equation with Nonlocal Pressure*, Found. Comput. Math. (2026), §2's review of the PDE theory. [Article](https://doi.org/10.1007/s10208-026-09752-y).

Remark 7 of the survey explicitly leaves the multidimensional extension of infinite propagation open. The 2026 PDE review still states the infinite-propagation result only for dimension one. Searches on 2026-09-22 checked higher-dimensional spreading and later pressure-model papers; no whole-space result for the stated class was located. Infinite spreading of self-similar profiles, results on a torus, and finite propagation for $`m\ge2`$ do not answer this question. The weak formulation uses positive exterior mass because continuity is not being assumed.

## 19. The local limit of superlinear multispecies nonlocal diffusion

Admitted page: [superlinear-skt-nonlocal-to-local-limit](../../../problems/469-superlinear-skt-nonlocal-to-local-limit.md)

1. P. Hirvonen, A. Jüngel and A. Pollino, *Superlinear nonlocal diffusion systems for multispecies populations: well-posedness and discrete chain rules* (September 2026 preprint), §1.1, assumptions (A1)–(A5a), and Theorem 1. [Full preprint](https://arxiv.org/html/2609.09921v1).
2. G. Galiano and J. Velasco, *Convergence of solutions of a rescaled evolution nonlocal cross-diffusion problem to its local diffusion counterpart*, Rev. R. Acad. Cienc. Exactas Fís. Nat. Ser. A Math. **116**, 93 (2022), the two-species $`s=1`$ result. [Article](https://doi.org/10.1007/s13398-022-01231-7).

The September 2026 source explicitly calls extension of the localization argument to $`s\ne1`$ open. Its global nonlocal theorem uses the stronger coefficient condition written here; merely copying the weaker condition for the local equation would not justify the approximating solutions. Searches on 2026-09-22 for superlinear SKT localization and the paper title found no subsequent resolution. Local limits for convolution inside the pressure or triangular diffusion matrices are different models or restrictions.

## 20. Instantaneous strict separation for three-dimensional local Cahn–Hilliard

Admitted page: [local-cahn-hilliard-three-dimensional-separation](../../../problems/470-local-cahn-hilliard-three-dimensional-separation.md)

1. C. G. Gal and A. Poiatti, *Unified framework for the separation property in binary phase-segregation processes with singular entropy densities*, European J. Appl. Math. **36** (2025), 40–67, §§6.1.1–6.3. [Article](https://doi.org/10.1017/S0956792524000196).
2. C. Hurm, P. Knopf and A. Poiatti, *Nonlocal-to-local convergence rates for strong solutions to a Navier–Stokes–Cahn–Hilliard system with singular potential*, Comm. Partial Differential Equations **49** (2024), 832–871, Introduction's discussion of the missing uniform separation bound. [Article](https://doi.org/10.1080/03605302.2024.2401445).
3. A. Poiatti, *The 3D strict separation property for the nonlocal Cahn–Hilliard equation with singular potential*, Analysis & PDE **18** (2025), 109–139. [Article](https://doi.org/10.2140/apde.2025.18.109).

The first two sources distinguish this open local three-dimensional problem from proved separation in two dimensions, at sufficiently late times, or near an energy minimizer. The third source resolves the nonlocal equation, whose chemical potential has an integral interaction operator instead of $`-\Delta u`$. Searches on 2026-09-22 for local three-dimensional logarithmic Cahn–Hilliard instantaneous separation found no matching theorem. Numerical separation, stronger singular potentials, and eventual separation do not settle the stated quantifier “every $`\tau>0`$.”

## 21. Flatness of three-dimensional fractional minimizing cones for every interaction order

Admitted page: [fractional-minimizing-cones-three-dimensional](../../../problems/471-fractional-minimizing-cones-three-dimensional.md)

1. L. Caffarelli, J.-M. Roquejoffre and O. Savin, *Nonlocal minimal surfaces*, Comm. Pure Appl. Math. **63** (2010), 1111–1144, minimizing cones and dimension reduction. [Article](https://doi.org/10.1002/cpa.20331).
2. X. Cabré, E. Cinti and J. Serra, *Stable $`s`$-minimal cones in $`\mathbb R^3`$ are flat for $`s\sim1`$*, J. Reine Angew. Math. (2020). [Preprint](https://arxiv.org/abs/1710.08722).
3. R. Tsiamis, *Stable $`s`$-minimal cones in $`\mathbb R^3`$ are flat for $`s`$ close to zero* (August 2026 preprint), Theorem 1.1 and Introduction. [Full preprint](https://arxiv.org/html/2608.21340v1).

The August 2026 theorem was included in the check: it proves flatness only for sufficiently small $`s`$, complementing the near-one theorem. Searches on 2026-09-22 for three-dimensional minimizing cones and all fractional orders located no result closing the intervening orders. This entry uses minimizing cones, a stronger assumption than stationarity or stability; nonflat stationary cones do not disprove it. It also differs from the catalogue's local one-phase cone and Allen–Cahn questions.

## 22. Uniqueness of all weak dual solutions of fractional porous-medium flow

Admitted page: [manifold-fractional-pme-weak-dual-uniqueness](../../../problems/472-manifold-fractional-pme-weak-dual-uniqueness.md)

1. E. Berchio, M. Bonforte, G. Grillo and M. Muratori, *The fractional porous medium equation on noncompact Riemannian manifolds*, Math. Ann. **389** (2024), 3603–3651, Assumption 2.1, Definition 2.1 and §7. [Article](https://doi.org/10.1007/s00208-023-02731-6); [accepted manuscript](https://iris.polito.it/retrieve/handle/11583/2984889/691780).
2. G. Grillo, *The Fractional Porous Medium Equation on noncompact Riemannian manifolds*, Oberwolfach Reports 14/2025, contribution on weak dual solutions and unresolved uniqueness/fundamental solutions. [Workshop report](https://ems.press/content/serial-article-files/51358?nt=1).

The 2024 paper proves uniqueness only within its monotone approximation construction and explicitly asks for uniqueness in the full weak dual class in §7. The 2025 Oberwolfach contribution repeats the unresolved uniqueness issue. Searches on 2026-09-22 for weak dual uniqueness, fractional porous-medium manifolds, and later work of the authors found no full-class theorem. Euclidean very-weak uniqueness and local-in-space porous-medium uniqueness on manifolds concern different operators or geometries.

## 23. Mass conservation for fractional porous-medium flow on noncompact manifolds

Admitted page: [manifold-fractional-pme-mass-conservation](../../../problems/473-manifold-fractional-pme-mass-conservation.md)

1. E. Berchio, M. Bonforte, G. Grillo and M. Muratori, *The fractional porous medium equation on noncompact Riemannian manifolds*, Math. Ann. **389** (2024), 3603–3651, Assumption 2.1, Definition 2.1 and §7. [Article](https://doi.org/10.1007/s00208-023-02731-6); [accepted manuscript](https://iris.polito.it/retrieve/handle/11583/2984889/691780).
2. G. Grillo, *The Fractional Porous Medium Equation on noncompact Riemannian manifolds*, Oberwolfach Reports 14/2025, contribution on weak dual solutions and unresolved uniqueness/fundamental solutions. [Workshop report](https://ems.press/content/serial-article-files/51358?nt=1).

Mass conservation under these geometric assumptions is explicitly listed in §7 of the final paper; the difficulty is constructing cutoffs with suitable fractional Laplacian bounds. Searches on 2026-09-22 checked conservation, stochastic completeness, and subsequent fractional diffusion papers. Results for compact manifolds, the ordinary Laplace–Beltrami operator, or fast diffusion do not settle this assertion. The separate uniqueness entry asks whether solutions coincide; this entry asks for a quantitative conservation law for each admissible solution.

## 24. Point-source solutions of fractional porous-medium diffusion on manifolds

Admitted page: [manifold-fractional-pme-point-source](../../../problems/474-manifold-fractional-pme-point-source.md)

1. E. Berchio, M. Bonforte, G. Grillo and M. Muratori, *The fractional porous medium equation on noncompact Riemannian manifolds*, Math. Ann. **389** (2024), 3603–3651, Assumption 2.1, Definition 2.1 and §7. [Article](https://doi.org/10.1007/s00208-023-02731-6); [accepted manuscript](https://iris.polito.it/retrieve/handle/11583/2984889/691780).
2. G. Grillo, *The Fractional Porous Medium Equation on noncompact Riemannian manifolds*, Oberwolfach Reports 14/2025, contribution on weak dual solutions and unresolved uniqueness/fundamental solutions. [Workshop report](https://ems.press/content/serial-article-files/51358?nt=1).

Both §7 of the 2024 paper and the 2025 Oberwolfach report explicitly leave existence for Dirac initial data open on this manifold class. Searches on 2026-09-22 checked fundamental solutions, measure data and later manifold diffusion publications. Known measure-data results for Euclidean fractional diffusion and nonfractional negatively curved diffusion do not cover this combination of geometry and operator. Only existence is requested; no unsupported universal asymptotic profile on arbitrary manifolds is asserted.

## 25. Uniqueness for a point source in time-fractional porous-medium flow

Admitted page: [time-fractional-pme-dirac-uniqueness](../../../problems/475-time-fractional-pme-dirac-uniqueness.md)

1. D. Gómez-Castro, Ł. Płociniczak and J. L. Vázquez, *Self-similar solutions to the time-fractional Porous-Medium Equation* (2026 preprint), §1 and §8, “Uniqueness of weak solutions with Dirac initial data” and “Asymptotic behavior for general initial data.” [Full preprint](https://arxiv.org/html/2604.09281v1).
2. J. Caballero, H. Okrasińska-Płociniczak, Ł. Płociniczak and K. Sadarangani, *Barenblatt solutions for the time-fractional porous medium equation: approach via integral equations*, Fract. Calc. Appl. Anal. (2026), construction of the self-similar profiles. [Article](https://doi.org/10.1007/s13540-026-00514-9).
3. J. L. Vázquez, *The Porous Medium Equation: Mathematical Theory*, Oxford University Press (2007), classical fundamental solutions and large-time asymptotics. [Book](https://doi.org/10.1093/acprof:oso/9780198569039.001.0001).

The April 2026 preprint constructs and characterizes self-similar solutions but lists general weak uniqueness for Dirac data separately in §8. Searches on 2026-09-22 checked measure-data uniqueness, the paper title and subsequent citations. Uniqueness of the profile equation and results for regular one-dimensional initial-boundary data do not imply the assertion here. The weak formulation retains the initial measure inside the memory equation rather than restarting the equation at positive time.

## 26. Barenblatt attraction for porous-medium diffusion with time memory

Admitted page: [time-fractional-pme-barenblatt-attraction](../../../problems/476-time-fractional-pme-barenblatt-attraction.md)

1. D. Gómez-Castro, Ł. Płociniczak and J. L. Vázquez, *Self-similar solutions to the time-fractional Porous-Medium Equation* (2026 preprint), §1 and §8, “Uniqueness of weak solutions with Dirac initial data” and “Asymptotic behavior for general initial data.” [Full preprint](https://arxiv.org/html/2604.09281v1).
2. J. Caballero, H. Okrasińska-Płociniczak, Ł. Płociniczak and K. Sadarangani, *Barenblatt solutions for the time-fractional porous medium equation: approach via integral equations*, Fract. Calc. Appl. Anal. (2026), construction of the self-similar profiles. [Article](https://doi.org/10.1007/s13540-026-00514-9).
3. J. L. Vázquez, *The Porous Medium Equation: Mathematical Theory*, Oxford University Press (2007), classical fundamental solutions and large-time asymptotics. [Book](https://doi.org/10.1093/acprof:oso/9780198569039.001.0001).

Section 8 of the 2026 preprint explicitly asks whether its profiles attract general solutions. Searches on 2026-09-22 for nonlinear time-fractional Barenblatt attraction and long-time asymptotics found no matching convergence theorem. The classical case $`\alpha=1`$, linear case $`m=1`$, bounded-domain decay, and asymptotics of the profile itself are different results. The $`L^1`$ conclusion avoids imposing uniform convergence to a profile that can be spatially singular in higher dimensions.

## 27. A bounded critical norm continuation criterion for stochastic Navier–Stokes

Admitted page: [stochastic-navier-stokes-bounded-critical-norm](../../../problems/477-stochastic-navier-stokes-bounded-critical-norm.md)

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), Theorems 8.26–8.27 and Open Problem 11. [Article](https://doi.org/10.1007/s00030-025-01090-2).
2. A. Agresti and M. Veraar, *Stochastic Navier–Stokes equations for turbulent flows in critical spaces*, Commun. Math. Phys. (2024), critical local theory and continuation criteria. [Preprint](https://arxiv.org/abs/2107.03953).
3. A. Agresti, *On the absence of blow-up in the 3D Navier–Stokes equations with transport noise* (2026 preprint). [Current preprint](https://arxiv.org/abs/2607.15140).

This fixes the survey's parameters to $`(p,\delta,\kappa,q)=(4,-1/2,1/2,4)`$ and asks for its explicitly open improvement from existence of a critical-space limit to boundedness. The 2026 preprint proves high-probability global smoothness for suitably chosen noise, rather than this continuation criterion for arbitrary admissible spatial fields. Searches on 2026-09-22 for stochastic endpoint Serrin criteria and bounded critical Besov norms found no matching resolution. Constant transport fields, removable by translation, do not settle the spatially varying case.

## 28. Global regularity for critical SQG with state-dependent noise

Admitted page: [critical-stochastic-sqg-global-regularity](../../../problems/478-critical-stochastic-sqg-global-regularity.md)

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), equation (8.23), Theorem 8.22 and Remark 8.23. [Article](https://doi.org/10.1007/s00030-025-01090-2).
2. T. Liang and Y. Wang, *Sub-critical and critical stochastic quasi-geostrophic equations with infinite delay*, Discrete Contin. Dyn. Syst. B **26** (2021), 4697–4726, local pathwise theory at critical dissipation. [Article](https://doi.org/10.3934/dcdsb.2020309).

The survey explicitly leaves global existence and uniqueness at dissipation exponent $`\alpha=1/2`$ open; the statement selects smooth finite-dimensional Lipschitz noise to make the solution class concrete. Searches on 2026-09-22 checked critical stochastic SQG, nonlinear multiplicative forcing, and global regularity. Located results concern subcritical dissipation, local critical solutions, restricted noise, or modified SQG with Kraichnan transport noise; none settles the full class here. This is distinct from deterministic supercritical SQG already in the catalogue.

## 29. Global classical Maxwell–Stefan diffusion with arbitrary pair friction

Admitted page: [maxwell-stefan-arbitrary-friction-global-classical](../../../problems/479-maxwell-stefan-arbitrary-friction-global-classical.md)

1. E. S. Daus, A. Jüngel and B. Q. Tang, *Exponential time decay of solutions to reaction-cross-diffusion systems of Maxwell–Stefan type*, Arch. Ration. Mech. Anal. **235** (2020), Remark 2. [Full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7021190/).
2. D. Bothe, *Global strong solutions for Maxwell–Stefan diffusion with additive friction coefficients* (2026 preprint), §1 and its main theorem. [arXiv:2609.06732](https://arxiv.org/abs/2609.06732).

The older existence theory gives weak solutions and local classical solutions, with a general classical continuation problem remaining. The search on 2026-09-22 located Bothe’s September 2026 preprint and checked its coefficient assumptions: its global theorem requires additive pair friction. The statement above retains arbitrary positive symmetric pair friction and $`N\ge4`$, where additivity is a genuine restriction. Neither that theorem nor near-equilibrium global results settle this formulation. The recent result is cited as a preprint, rather than silently treating its special case as still open.

## 30. Weak uniqueness for fourth-order aggregation–diffusion

Admitted page: [fourth-order-aggregation-weak-uniqueness](../../../problems/480-fourth-order-aggregation-weak-uniqueness.md)

1. J. A. Carrillo, A. Esposito, C. Falcó and A. Fernández-Jiménez, *Competing effects in fourth-order aggregation–diffusion equations*, Proc. Lond. Math. Soc. **129**, e12623 (2024), Introduction, Definition 2.1 and Theorem 2.2. [Article](https://doi.org/10.1112/plms.12623).
2. C. Falcó, R. E. Baker and J. A. Carrillo, *A nonlocal-to-local approach to aggregation-diffusion equations*, SIAM Review **67** (2025), 353–372, §4. [Article](https://doi.org/10.1137/25M1726248).

The formulation is the $`m=2`$ subcritical model and weak solution class of the first paper, which proves existence. The SIAM Review article still identifies uniqueness as unresolved. Searches on 2026-09-22 for fourth-order aggregation–diffusion weak uniqueness, cell-adhesion uniqueness, and the authors’ later papers found no theorem covering this class with vacuum. Classical uniqueness while the mobility stays uniformly positive is insufficient. This is separate from the catalogue’s cubic thin-film positivity problem: both the mobility and the attractive second-order term differ.

## 31. Full-space minimizers for subcritical fourth-order aggregation energy

Admitted page: [fourth-order-aggregation-full-space-minimizer](../../../cut_problems/research/resolved/659-fourth-order-aggregation-full-space-minimizer.md)

1. J. A. Carrillo, A. Esposito, C. Falcó and A. Fernández-Jiménez, *Competing effects in fourth-order aggregation–diffusion equations*, Proc. Lond. Math. Soc. **129**, e12623 (2024), Introduction, Theorem 2.1 and §3. [Article](https://doi.org/10.1112/plms.12623).
2. C. Falcó, R. E. Baker and J. A. Carrillo, *A nonlocal-to-local approach to aggregation-diffusion equations*, SIAM Review **67** (2025), 353–372, §4. [Article](https://doi.org/10.1137/25M1726248).

The source proves a lower energy bound in this subcritical range and treats critical optimizers, but explicitly leaves full-space subcritical minimizers open; the 2025 review repeats the gap. Searches on 2026-09-22 for this energy, the paper title, and subcritical minimizer existence found no later matching attainment result. Compact-domain minimizers, critical Gagliardo–Nirenberg optimizers, and minimizers with quadratic confinement have different compactness assumptions. This stationary variational problem is distinct from uniqueness of the associated time-dependent PDE.

## 32. Finite propagation in fourth-order aggregation–diffusion

Admitted page: [fourth-order-aggregation-finite-propagation](../../../cut_problems/problems/481-fourth-order-aggregation-finite-propagation.md)

1. J. A. Carrillo, A. Esposito, C. Falcó and A. Fernández-Jiménez, *Competing effects in fourth-order aggregation–diffusion equations*, Proc. Lond. Math. Soc. **129**, e12623 (2024), Introduction, Definition 2.1 and Theorem 2.2. [Article](https://doi.org/10.1112/plms.12623).
2. C. Falcó, R. E. Baker and J. A. Carrillo, *A nonlocal-to-local approach to aggregation-diffusion equations*, SIAM Review **67** (2025), 353–372, §4. [Article](https://doi.org/10.1137/25M1726248).

The 2024 paper constructs weak solutions and explicitly identifies preservation of compact support as an unresolved free-boundary question, supported there by computations. The $`m=2`$ case above lies in its globally existing subcritical range in every finite dimension. Searches on 2026-09-22 for fourth-order aggregation–diffusion finite propagation and compact support found no later resolution for this model and class of initial data. Propagation results for other thin-film mobilities or for purely attractive second-order equations do not answer this statement.

## 33. Unconditional uniqueness for entropy-dissipating reaction–diffusion

Admitted page: [entropy-reaction-diffusion-renormalized-uniqueness](../../../problems/482-entropy-reaction-diffusion-renormalized-uniqueness.md)

1. J. Fischer, *Weak-strong uniqueness of solutions to entropy-dissipating reaction-diffusion equations*, Nonlinear Analysis **159** (2017), 181–207, Definition 2 and Theorem 7. [Author manuscript](https://arxiv.org/abs/1703.00730).
2. K. Fellner, J. Fischer, M. Kniely and B. Q. Tang, *Global renormalised solutions and equilibration of reaction–diffusion systems with nonlinear diffusion*, J. Nonlinear Sci. **33**, 66 (2023), Remark 1.4. [Article](https://doi.org/10.1007/s00332-023-09926-w).
3. A. Agresti, M. Kniely and B. Q. Tang, *Global classical solutions by transport noise for reaction–diffusion systems with entropy dissipation* (2026 preprint), §1.1. [Preprint](https://arxiv.org/abs/2608.13332).

Fischer proves uniqueness conditional on a strong solution, while the 2023 discussion and the August 2026 preprint explicitly retain unconditional uniqueness as unresolved. Searches on 2026-09-22 for renormalized reaction–diffusion uniqueness found further weak–strong results, including interface problems, but no unconditional theorem for this entropy class. This question fixes linear diffusion and concerns uniqueness; it does not restate the separate smooth-existence question for high-order mass-action reactions.

## 34. Automatic conservation laws for renormalized nonlinear diffusion

Admitted page: [nonlinear-diffusion-renormalization-mass-conservation](../../../problems/483-nonlinear-diffusion-renormalization-mass-conservation.md)

1. K. Fellner, J. Fischer, M. Kniely and B. Q. Tang, *Global renormalised solutions and equilibration of reaction–diffusion systems with nonlinear diffusion*, J. Nonlinear Sci. **33**, 66 (2023), Definition 1.1, identities (1.4)–(1.6), and Remark 1.2. [Article](https://doi.org/10.1007/s00332-023-09926-w).
2. J. Fischer, *Weak-strong uniqueness of solutions to entropy-dissipating reaction-diffusion equations*, Nonlinear Analysis **159** (2017), 181–207, linear-diffusion renormalization arguments. [Preprint](https://arxiv.org/abs/1703.00730).

Remark 1.2 explicitly asks whether the truncated identity entails the conservation and entropy laws for nonlinear diffusion. The present entry isolates conservation as one definite assertion and retains the source’s exponent interval. For linear diffusion, or for bounded solutions, the implication is known; neither restriction is imposed here. Searches on 2026-09-22 for nonlinear diffusion, renormalized solutions, and automatic mass conservation found no later resolution. Existence of solutions constructed to satisfy conservation does not establish the implication for every solution of the truncated identity.

## 35. Global attraction for complex-balanced reaction–diffusion with boundary equilibria

Admitted page: [complex-balanced-pde-global-attractor](../../../problems/484-complex-balanced-pde-global-attractor.md)

1. L. Desvillettes, K. Fellner and B. Q. Tang, *Trend to equilibrium for reaction-diffusion systems arising from complex balanced chemical reaction networks*, SIAM J. Math. Anal. **49** (2017), 2666–2709, §3 and Remark 3.6. [Article](https://doi.org/10.1137/16M1073935); [author manuscript](https://imsc.uni-graz.at/fellnerk/preprints/DFT.pdf).
2. K. Fellner and B. Q. Tang, *Convergence to equilibrium of renormalised solutions to nonlinear chemical reaction-diffusion systems*, Z. Angew. Math. Phys. **69**, 54 (2018), discussion of boundary equilibria. [Author manuscript](https://imsc.uni-graz.at/fellnerk/preprints/FTRenorm.pdf).
3. T. L. Nguyen and B. Q. Tang, *Stability analysis of irreversible chemical reaction-diffusion systems with boundary equilibria*, Z. Angew. Math. Phys. **77**, 199 (2026), Introduction. [Article](https://doi.org/10.1007/s00033-026-02847-0).

The SIAM paper explicitly leaves general systems with boundary equilibria open. The 2018 and July 2026 papers explain why the absence-of-boundary-equilibria theory does not settle this regime. Searches on 2026-09-22 also found convergence for selected networks, a single reversible reaction with bounded solutions, near-equilibrium data, and sufficiently large diffusivity; these restrictions do not imply the statement for arbitrary complex-balanced networks and diffusion constants. The question assumes global boundedness to separate asymptotic selection from global existence. It is a spatial PDE problem; catalogue problem 276 concerns general weakly reversible ODE persistence without complex balance.

## 36. Optimal obstacle regularity for stable jump kernels with only angular integrability

Admitted page: [general-stable-obstacle-optimal-regularity](../../../problems/485-general-stable-obstacle-optimal-regularity.md)

1. X. Fernández-Real and X. Ros-Oton, [*Integro-Differential Elliptic Equations*](https://doi.org/10.1007/978-3-031-54242-8), Progress in Mathematics 350, Birkhäuser (2024), §4.6.2, Open Question 4.3, and Theorem 4.5.1; [author draft](https://arxiv.org/abs/2411.12455), pp. 297 and 302.
2. X. Ros-Oton and M. Weidner, [*Obstacle problems for nonlocal operators with singular kernels*](https://arxiv.org/abs/2308.01695), Annali della Scuola Normale Superiore di Pisa, Classe di Scienze 27 (2026), 535–588, Theorem 1.3 and the open-problem paragraph immediately following it; DOI [10.2422/2036-2145.202309_010](https://doi.org/10.2422/2036-2145.202309_010).
3. X. Ros-Oton and M. Weidner, [*Optimal regularity for nonlocal elliptic equations and free boundary problems*](https://arxiv.org/abs/2403.07793), preprint (2024), equations (1.1)–(1.2) and Theorem 1.3.

Checked on 22 September 2026 using general stable obstacle regularity, angular $`L^1`$ kernels, and later 2025–2026 optimal-regularity results. The book explicitly asks for the general stable class. The singular-kernel paper proves the stated type of estimate under $`a\in L^p(\mathbb S^{n-1})`$ with $`p>n/(2s)`$ and expressly leaves mere $`L^1`$ ellipticity unresolved. Its 2026 journal publication is the publication of that result, not a removal of the angular-integrability hypothesis. The third paper allows nonhomogeneous radial behavior but retains two-sided pointwise comparison with the fractional-Laplacian kernel. That assumption excludes the angular concentrations here. No result removing the stronger angular assumption was located. This target uses a smooth obstacle and rough angular intensity; it is distinct from lowering the obstacle's smoothness for a pointwise elliptic kernel, and from the auxiliary positive-harmonic-profile classification in cones.
