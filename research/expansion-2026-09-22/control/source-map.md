# Control, transport and geometric PDE source audit

Checked through 22 September 2026. The35 entries contain31 PDE-related questions and4 broader control/geometry questions. Existing titles and nearby statements were screened before drafting. All formulation sources were read at the cited section level; references to partial results establish which hypotheses remain outside available theorems. An unsuccessful resolution search is evidence of no located resolution, not proof that none exists.

## Per-entry source map

### 1. Observability of an acoustic shell at equal bulk and surface speeds

Admitted page: [equal-speed-wentzell-wave-observability](../../../cut_problems/problems/385-equal-speed-wentzell-wave-observability.md)

1. L. Baudouin, J. Dardé, S. Ervedoza and A. Mercado, *A unified strategy for observability of waves in an annulus with various boundary conditions*, Mathematical Reports 24 (2022), 59–112, §2 and Theorem 2.4. [Journal PDF](https://imar.ro/journals/Mathematical_Reports/Pdfs/2022/1-2/5.pdf).
2. S. E. Chorfi, L. Maniar and R. Morales, *Controllability and Inverse Problems for Hyperbolic and Dispersive Equations with Dynamic Boundary Conditions*, preprint (2025), §3.1 and §5.1. [arXiv:2505.14795](https://arxiv.org/abs/2505.14795).

Review: The 2025 review explicitly leaves equal bulk and surface coefficients unresolved. Faster surface propagation is covered by its observability theorem; slower surface propagation has a counterexample in the annular wave setting. Searches through 22 September 2026 for equal-speed Wentzell/Ventcel wave observability and the authors’ subsequent work located no theorem or counterexample at equality. Results for one-dimensional dynamic endpoints do not settle a boundary with tangential propagation.

### 2. Boundary observation of a Schrödinger field with slower surface dispersion

Admitted page: [slow-surface-schrodinger-observability](../../../cut_problems/problems/386-slow-surface-schrodinger-observability.md)

1. A. Mercado and R. Morales, *Exact Controllability for a Schrödinger Equation with Dynamic Boundary Conditions*, SIAM Journal on Control and Optimization 61 (2023), 3501–3525, main observability and controllability theorems. [DOI](https://doi.org/10.1137/21M1439407); [author preprint](https://arxiv.org/abs/2301.02573).
2. S. E. Chorfi, L. Maniar and R. Morales, *Controllability and Inverse Problems for Hyperbolic and Dispersive Equations with Dynamic Boundary Conditions*, preprint (2025), equations (4.1)–(4.4) and §5.1. [arXiv:2505.14795](https://arxiv.org/abs/2505.14795).

Review: The SIAM theorem assumes the surface coefficient exceeds the bulk coefficient. Section 5.1 of the 2025 review expressly distinguishes the unresolved Schrödinger regime below that threshold from the negative result for waves. Searches through 22 September 2026 included “Schrödinger dynamic boundary delta less than d observability”, Wentzell control and Mercado–Morales follow-ups. The 2026 inverse-potential reconstruction paper retains the faster-surface hypothesis; no resolution of the stated slower-surface case was located.

### 3. The sharp local maneuvering time for a shallow-water tank

Admitted page: [shallow-water-tank-sharp-control-time](../../../cut_problems/problems/387-shallow-water-tank-sharp-control-time.md)

1. J.-M. Coron, *Time for local controllability of a 1-D tank containing a fluid modeled by the shallow water equations*, Problem 7.1, pp. 247–250, in V. D. Blondel and A. Megretski (eds.), *Unsolved Problems in Mathematical Systems and Control Theory*, Princeton University Press (2004). [Publisher book](https://doi.org/10.1515/9781400826155).
2. J.-M. Coron, A. Koenig and H.-M. Nguyen, *Lack of local controllability for a water-tank system when the time is not large enough*, Annales de l’Institut Henri Poincaré C (2024 online), §1 and main noncontrollability theorem. [DOI](https://doi.org/10.4171/AIHPC/123); [publisher PDF](https://ems.press/content/serial-article-files/47556).

Review: The book conjectures the threshold $`2`$ in this normalization. The 2024 paper proves the corresponding lower-time obstruction using the quadratic dynamics; it does not give local controllability for every time above the threshold. Searches through 22 September 2026 included tank Saint-Venant sharp/minimal control time and Coron–Koenig–Nguyen continuations. Large-time local controllability and feedback stabilization were distinguished from a proof for all $`T>2`$.

### 4. Global smooth evolution of small semigeostrophic perturbations

Admitted page: [semigeostrophic-small-data-global-smoothness](../../../problems/388-semigeostrophic-small-data-global-smoothness.md)

1. G. Loeper, *A Fully Nonlinear Version of the Incompressible Euler Equations: The Semigeostrophic System*, SIAM Journal on Mathematical Analysis 38 (2006), 795–823, local regularity and uniqueness results. [DOI](https://doi.org/10.1137/050629070).
2. G. De Philippis and A. Figalli, *The Monge–Ampère Equation and Its Link to Optimal Transportation*, Bulletin of the AMS 51 (2014), 527–580, §2.5 and §5.2(3). [Publisher PDF](https://www.ams.org/journals/bull/2014-51-04/S0273-0979-2014-01459-4/S0273-0979-2014-01459-4.pdf).
3. A. Figalli, *Global existence for the semigeostrophic equations*, concluding open questions, item 2. [Author manuscript](https://cvgmt.sns.it/media/doc/paper/2665/MA_semigeo.pdf).

Review: The concluding question in Figalli’s survey explicitly singles out initial densities sufficiently close to one in a strong norm. The formulation above makes that qualification existential in the differentiability order. Searches through 22 September 2026 covered small-amplitude semigeostrophic global regularity, Loeper and Silini, and the semigeostrophic–Euler limit. Silini’s SIAM JMA 55 (2023), 6554–6579 result is local in time; lifespan lower bounds and global weak-solution constructions do not establish the requested global smooth flow.

### 5. Uniqueness of bounded semigeostrophic potential vorticity

Admitted page: [semigeostrophic-bounded-vorticity-uniqueness](../../../problems/389-semigeostrophic-bounded-vorticity-uniqueness.md)

1. D. P. Bourne, C. P. Egan, B. Pelloni and M. Wilkinson, *Semi-discrete optimal transport methods for the semi-geostrophic equations*, Calculus of Variations and PDE 61 (2022), article 39, §1, equations (1)–(2), and §3. [Full text](https://doi.org/10.1007/s00526-021-02133-z).
2. T. Lavier, *A semi-discrete optimal transport scheme for the 3D incompressible semi-geostrophic equations*, IMA Journal of Applied Mathematics 90 (2025), 443–464, Remark 1.1. [Full text](https://doi.org/10.1093/imamat/hxaf023).

Review: Both sources distinguish available existence results from unresolved weak uniqueness. The ball and bounded-density assumptions select a concrete subclass of their question and make the transport velocity unambiguous almost everywhere. Searches through 22 September 2026 included semigeostrophic bounded-vorticity uniqueness, weak–strong uniqueness and entropic approximation. Local Hölder uniqueness and uniqueness relative to a uniformly convex strong solution do not prove uniqueness between two arbitrary bounded weak solutions.

### 6. Sharp weak integrability of planar Monge–Ampère Hessians

Admitted page: [planar-monge-ampere-sharp-hessian-integrability](../../../problems/390-planar-monge-ampere-sharp-hessian-integrability.md)

1. G. De Philippis and A. Figalli, *The Monge–Ampère Equation and Its Link to Optimal Transportation*, Bulletin of the AMS 51 (2014), 527–580, §5.2(2). [Publisher PDF](https://www.ams.org/journals/bull/2014-51-04/S0273-0979-2014-01459-4/S0273-0979-2014-01459-4.pdf).
2. G. De Philippis, A. Figalli and O. Savin, *A note on interior $`W^{2,1+ε}`$ estimates for the Monge–Ampère equation*, Mathematische Annalen 357 (2013), 11–22, Theorem 1.1. [DOI](https://doi.org/10.1007/s00208-012-0895-9); [preprint](https://arxiv.org/abs/1202.5566).

Review: The survey explicitly proposes this exponent using planar quasiconformal theory. Searches through 22 September 2026 covered sharp planar Hessian integrability, the stated exponent, and subsequent work by De Philippis, Figalli, Savin and Mooney. Higher integrability with a non-sharp positive epsilon is established; the upper-bound-only degenerate problem has counterexamples, but those remove the positive lower bound essential here. No endpoint resolution was located.

### 7. Affine Bernstein rigidity in dimensions three through nine

Admitted page: [affine-bernstein-entire-low-dimensions](../../../problems/391-affine-bernstein-entire-low-dimensions.md)

1. N. S. Trudinger and X.-J. Wang, *The Monge–Ampère equation and its geometric applications*, Handbook of Geometric Analysis, vol. I (2008), 467–524, §6.3, conjecture following Theorem 6.4. [Author chapter](https://maths-people.anu.edu.au/~wang/publications/MA.pdf).
2. Y. Sun, C. Xing and R. Xu, *New non-quadratic Euclidean complete affine maximal type hypersurfaces via Calabi affine geometry*, preprint (26 August 2026), §1, equations (1.1)–(1.3) and Theorem 1.3. [arXiv:2608.25330](https://arxiv.org/abs/2608.25330).

Review: The August 2026 paper explicitly says the affine maximal conjecture remains open even in dimension three. Its new counterexamples have exponent a at least -n/(n+1), which does not include the affine maximal exponent -(n+1)/(n+2). The older dimension-ten example is nonsmooth and also outside the requested dimension range. Searches through 22 September 2026 for higher-dimensional Chern/affine Bernstein proofs and counterexamples found no matching resolution.

### 8. Regularity of transport interfaces for nonconvex polyhedral targets

Admitted page: [polyhedral-transport-singular-interface](../../../problems/392-polyhedral-transport-singular-interface.md)

1. S. Chen, Y. Li and J. Liu, *Optimal (partial) transport to non-convex polygonal domains*, preprint, version 4 (17 May 2026), Conjecture 5.1. [Full text](https://arxiv.org/html/2311.15655v4).
2. S. Chen and J. Liu, *Regularity of singular set in optimal transportation*, Inventiones Mathematicae 242 (2025), 1–44, introduction and principal regularity theorems. [DOI](https://doi.org/10.1007/s00222-025-01353-w); [preprint](https://arxiv.org/abs/2210.13841).

Review: Conjecture 5.1 is posed after the authors prove the planar polygonal case. The 2025 Inventiones theorem treats a target made of two disjoint convex domains, not a general nonconvex polyhedral target. Searches through 22 September 2026 for higher-dimensional polyhedral transport interfaces and later versions of both papers located no proof or counterexample. This concerns the structure of the full-transport singular set, rather than the free boundary in partial transport.

### 9. Singular-set dimension of polyhedral partial-transport free boundaries

Admitted page: [polyhedral-partial-transport-free-boundary](../../../problems/393-polyhedral-partial-transport-free-boundary.md)

1. S. Chen, Y. Li and J. Liu, *Optimal (partial) transport to non-convex polygonal domains*, preprint, version 4 (17 May 2026), Conjecture 5.2 and §1 definition of the active regions. [Full text](https://arxiv.org/html/2311.15655v4).
2. L. A. Caffarelli and R. J. McCann, *Free boundaries in optimal transport and Monge–Ampère obstacle problems*, Annals of Mathematics 171 (2010), 673–730, formulation and free-boundary regularity theory. [DOI](https://doi.org/10.4007/annals.2010.171.673).

Review: The 2026 source proves the two-dimensional polygonal result and explicitly leaves this higher-dimensional free-boundary conjecture. Searches through 22 September 2026 for partial transport nonconvex polytopes, Chen–Li–Liu Conjecture 5.2, and subsequent free-boundary regularity papers located no matching resolution. Smooth-target and convex-target results do not cover the stated nonconvex polyhedral geometry.

### 10. Villani’s convex-injectivity-domain conjecture

Admitted page: [villani-mtw-convex-injectivity-domains](../../../problems/394-villani-mtw-convex-injectivity-domains.md)

1. A. Figalli, T. Gallouët and L. Rifford, *On the convexity of injectivity domains on nonfocal manifolds*, SIAM Journal on Mathematical Analysis 47 (2015), 969–1000, Definition 1.1, Theorem 1.7 and the following Villani conjecture. [Author manuscript](https://cvgmt.sns.it/media/doc/paper/2531/MTWTCLNF_final.pdf).
2. G. Khan and J. Zhang, *When Optimal Transport Meets Information Geometry*, preprint (2022), Conjecture 3. [arXiv:2206.14791](https://arxiv.org/abs/2206.14791).

Review: The SIAM theorem proves the conclusion under the additional nonfocal assumption; the 2022 survey retains the general statement as a conjecture. Searches through 22 September 2026 included Villani MTW convexity, injectivity domains, focal cut loci, and the authors’ later work. Special manifolds and stability results for already regular transport do not resolve the unrestricted implication.

### 11. Exact null control of a harmonically confined kinetic equation from a wedge

Admitted page: [harmonic-kolmogorov-wedge-null-control](../../../cut_problems/problems/395-harmonic-kolmogorov-wedge-null-control.md)

1. K. Beauchard, M. Egidi and K. Pravda-Starov, *Geometric conditions for the null-controllability of hypoelliptic quadratic parabolic equations with moving control supports*, Comptes Rendus Mathématique 358 (2020), 651–700, preprint §2.4, Proposition 2.4(iii). [DOI](https://doi.org/10.5802/crmath.79); [arXiv:1908.10603](https://arxiv.org/abs/1908.10603).
2. P. Alphonse and J. Martin, *Approximate Null Controllability with Uniform Cost for the Hypoelliptic Ornstein–Uhlenbeck Equations*, SIAM Journal on Control and Optimization 61 (2023), 1679–1711, §2.3, Example 2.7. [DOI](https://doi.org/10.1137/22M1487412); [arXiv:2201.01516](https://arxiv.org/abs/2201.01516).

Review: The 2020 source explicitly leaves null controllability above the rotation threshold open. The SIAM paper proves approximate null control with uniform cost above that threshold and noncontrollability at the threshold; it explicitly distinguishes the remaining exact question. Searches through 22 September 2026 for harmonic Kolmogorov cone control, integral thickness and subsequent work by these authors located no exact positive result or counterexample.

### 12. Polynomial decay for KdV with three critical linear modes

Admitted page: [critical-kdv-odd-mode-polynomial-decay](../../../cut_problems/problems/396-critical-kdv-odd-mode-polynomial-decay.md)

1. J. Niu and S. Xiang, *Small-time local controllability of a KdV system for all critical lengths*, preprint, version 2 (16 December 2025), §2.4.5. [arXiv:2501.13640](https://arxiv.org/abs/2501.13640).
2. H.-M. Nguyen, *Decay for the nonlinear KdV equations at critical lengths*, Journal of Differential Equations 295 (2021), 249–291, main decay theorems and discussion of the dimension of the undamped subspace. [DOI](https://doi.org/10.1016/j.jde.2021.05.057); [arXiv:2012.08792](https://arxiv.org/abs/2012.08792).

Review: The December 2025 paper expressly identifies polynomial decay for odd undamped dimension greater than one as open. The length 14π is a concrete instance with dimension three. Its completed classification of small-time controllability does not establish uncontrolled polynomial decay. Searches through 22 September 2026 for this length, odd critical modes and later decay results located no resolution.

### 13. Approximate velocity control of a viscoelastic fluid with prescribed transport

Admitted page: [oseen-oldroyd-approximate-boundary-control](../../../cut_problems/problems/397-oseen-oldroyd-approximate-boundary-control.md)

1. E. Fernández-Cara, *Remarks on control and inverse problems for PDEs*, SeMA Journal 82 (2025), 267–288, §7, equation (25), Theorem 7 and Problem 14. [Full text](https://doi.org/10.1007/s40324-024-00363-7).
2. A. Doubova and E. Fernández-Cara, *On the control of viscoelastic Jeffreys fluids*, Systems & Control Letters 61 (2012), 573–579, approximate controllability result for the linear memory system. [DOI](https://doi.org/10.1016/j.sysconle.2012.02.003).
3. E. Fernández-Cara, J. L. F. Machado and D. A. Souza, *Non null controllability of Stokes equations with memory*, ESAIM: Control, Optimisation and Calculus of Variations 26 (2020), article 72. [DOI](https://doi.org/10.1051/cocv/2019067).

Review: Problem 14 asks whether the approximate velocity-control theorem survives the added prescribed transport term. Smooth divergence-free backgrounds and compatible controls make the model unambiguous. The negative null-control result concerns exact arrival and does not answer this approximate question. Searches through 22 September 2026 for Oseen–Oldroyd, Jeffreys memory and time-dependent drift controllability found no resolution.

### 14. Boundary control to equilibrium for a parabolic obstacle problem

Admitted page: [parabolic-obstacle-boundary-control](../../../cut_problems/problems/398-parabolic-obstacle-boundary-control.md)

1. B. Geshkovski, *Control in moving interfaces and deep learning*, doctoral thesis, Universidad Autónoma de Madrid (2021), §1.5.1, pp. 37–39, equations (1.5.1)–(1.5.3). [Thesis](https://repositorio.uam.es/bitstream/10486/696540/1/geshkovski_borjan.pdf).
2. D. Pighin and E. Zuazua, *Controllability under positivity constraints of semilinear heat equations*, Mathematical Control and Related Fields 8 (2018), 935–964, §7, discussion of controllability of the obstacle problem. [DOI](https://doi.org/10.3934/mcrf.2018041); [arXiv:1711.07678](https://arxiv.org/abs/1711.07678).

Review: The thesis expressly poses boundary exact control to the stationary obstacle solution, including the one-dimensional case. The 2018 paper explains why controllability of penalized equations does not settle the obstacle limit. The statement fixes a concrete admissible control class and asks large-time reachability, without assuming arbitrary-time control. Searches through 22 September 2026 for exact parabolic obstacle controllability and boundary control to stationary contact states found no resolution.

### 15. Best convex shape for insulation of fixed thickness and perimeter

Admitted page: [fixed-thickness-insulation-convex-perimeter](../../../cut_problems/problems/399-fixed-thickness-insulation-convex-perimeter.md)

1. F. Della Pietra, C. Nitsch and C. Trombetti, *An optimal insulation problem*, Mathematische Annalen 382 (2022), 745–759, §5, Open Problem 1 and the preceding compactness discussion. [Full text](https://doi.org/10.1007/s00208-020-02058-6).
2. D. Bucur, M. Nahon, C. Nitsch and C. Trombetti, *Shape optimization of a thermal insulation problem*, Calculus of Variations and Partial Differential Equations 61 (2022), article 186, introduction and Theorem 1. [Full text](https://doi.org/10.1007/s00526-022-02298-1).

Review: Open Problem 1 asks precisely for this convex planar minimum; the source allows degenerate segments in its compact convex class. Its disk theorem concerns the maximum. The later two-body volume-constrained result allows the insulation boundary to vary independently and does not answer the fixed-thickness perimeter problem. Searches through 22 September 2026 for the exact problem title, convex perimeter minima and constant-thickness insulation found no resolution.

### 16. Concentric-ball optimality for thermal insulation with radiative heat transfer

Admitted page: [radiative-insulation-concentric-balls](../../../problems/400-radiative-insulation-concentric-balls.md)

1. D. Bucur, M. Nahon, C. Nitsch and C. Trombetti, *Shape optimization of a thermal insulation problem*, Calculus of Variations and Partial Differential Equations 61 (2022), article 186, equations (1), (3), (4), Theorems 1–3 and the open question after Remark 4. [Full text](https://doi.org/10.1007/s00526-022-02298-1).
2. F. Della Pietra, C. Nitsch and C. Trombetti, *An optimal insulation problem*, Mathematische Annalen 382 (2022), 745–759, §1 energy formulation and §5 open shape questions. [Full text](https://doi.org/10.1007/s00208-020-02058-6).

Review: The primary source singles out radiative heat transfer as an unresolved instance of its constrained-volume concentric-ball question. It proves the quadratic convection law, all penalized-volume problems, and some inactive-constraint cases; those results do not establish the displayed inequality for the radiative law under an arbitrary volume budget. Searches through 22 September 2026 for nonlinear radiative insulation shape optimization and later work by the authors found no resolution.

### 17. Continuity of manifold transport under MTW and convex injectivity domains

Admitted page: [mtw-convex-domains-transport-continuity](../../../problems/401-mtw-convex-domains-transport-continuity.md)

1. G. De Philippis and A. Figalli, *The Monge–Ampère equation and its link to optimal transportation*, Bulletin of the American Mathematical Society 51 (2014), 527–580, §5.2, open problem (7). [Author manuscript](https://arxiv.org/abs/1310.6167).
2. A. Figalli, L. Rifford and C. Villani, *Necessary and sufficient conditions for continuity of optimal transport maps on Riemannian manifolds*, Tohoku Mathematical Journal 63 (2011), 855–876, introduction and continuity criteria. [Journal full text](https://www.jstage.jst.go.jp/article/tmj/63/4/63_855/_pdf/-char/ja).

Review: The cited sources establish necessity and sufficiency in dimension two and pose higher-dimensional sufficiency. The 2026 paper “A quantitative stability result for regularity of optimal transport on compact manifolds” (DOI 10.1007/s00526-026-03367-5, Theorem 1) requires smooth densities close in Wasserstein distance, so does not resolve this global assertion. Searches through 22 September 2026 for MTW, convex injectivity domains and higher-dimensional continuity found no resolution.

### 18. Logarithmic convexity for subdiffusion with non-gradient drift

Admitted page: [fractional-drift-logarithmic-convexity](../../../cut_problems/research/resolved/655-fractional-drift-logarithmic-convexity.md)

1. S.-E. Chorfi, *Logarithmic convexity of evolution equations and application to inverse problems*, preprint (2025), §4, Theorem 6 and §5, open problem 2. [Full text](https://arxiv.org/html/2506.19954v1).
2. S.-E. Chorfi, L. Maniar and M. Yamamoto, *Logarithmic convexity of non-symmetric time-fractional diffusion equations*, Mathematical Methods in the Applied Sciences 48 (2025), 2011–2021, gradient-drift assumption and main logarithmic convexity theorem. [DOI](https://doi.org/10.1002/mma.10421).

Review: The 2025 primary sources explicitly leave removal of the gradient-drift assumption open. Classical time derivatives and operators conjugate to self-adjoint ones are covered by other results, but those do not include general fractional drift diffusion. Searches through 22 September 2026 for non-gradient fractional logarithmic convexity and later papers by the authors found no matching proof or counterexample.

### 19. Logarithmic convexity for two coupled subdiffusion orders

Admitted page: [mixed-order-fractional-logarithmic-convexity](../../../cut_problems/problems/402-mixed-order-fractional-logarithmic-convexity.md)

1. S.-E. Chorfi, *Logarithmic convexity of evolution equations and application to inverse problems*, preprint (2025), §5, open problem 1, displaying this mixed-order system. [Full text](https://arxiv.org/html/2506.19954v1).
2. S.-E. Chorfi, L. Maniar and M. Yamamoto, *The backward problem for time-fractional evolution equations*, Applicable Analysis 103 (2024), 2194–2212, logarithmic convexity and conditional stability theorems. [DOI](https://doi.org/10.1080/00036811.2023.2290273); [arXiv:2211.16493](https://arxiv.org/abs/2211.16493).

Review: The recent source poses this exact coupled system. Its two distinct time orders prevent reduction to the single-order self-adjoint theorem. Searches through 22 September 2026 for mixed-order coupled diffusion, logarithmic convexity and backward recovery found no matching resolution. This concerns coupling of distinct memory laws, separate from nonsymmetric spatial drift.

### 20. Sharp exponential cost of fast boundary quantum control

Admitted page: [schrodinger-sharp-fast-control-exponent](../../../problems/403-schrodinger-sharp-fast-control-exponent.md)

1. P. Lissy, *Effective multipliers for weights whose log are Hölder continuous. Application to the cost of fast boundary controls for the 1D Schrödinger equation*, preprint (2025), §§3.1–3.2, conjecture preceding Theorem 3.1. [Full text](https://arxiv.org/html/2502.04859v1).
2. P. Lissy, *On the cost of fast controls for some families of dispersive or parabolic equations in one space dimension*, SIAM Journal on Control and Optimization 52 (2014), 2651–2676, §1.2 and control-cost bounds. [Author manuscript](https://cermics.enpc.fr/~lissyp/Publi/KdV.pdf).
3. M. Tucsnak and G. Weiss, *Observation and Control for Operator Semigroups*, Birkhäuser (2009), §7.1 and Corollary 8.2.4, boundary Schrödinger control framework. [Book DOI](https://doi.org/10.1007/978-3-7643-8994-9).

Review: The 2025 source explicitly conjectures the displayed coefficient and improves the upper coefficient to 27^(1/4)/4. Nguyen’s January 2026 preprint arXiv:2601.12810 gives fractional-order cost bounds, not this sharp classical coefficient; its Theorem 1.1 assumes 1/2<s<1. Lissy’s August 2026 arXiv:2608.08041 concerns the heat equation. Searches through 22 September 2026 located no resolution for the Schrödinger assertion.

### 21. Uniform convergence of value functions in local mean-field games

Admitted page: [local-mfg-uniform-vanishing-viscosity](../../../problems/404-local-mfg-uniform-vanishing-viscosity.md)

1. W. Tang and Y. P. Zhang, *The Convergence Rate of Vanishing Viscosity Approximations for Mean Field Games*, SIAM Journal on Mathematical Analysis 57 (2025), 3217–3254, §2 assumption (H3*), Theorem 5.5 and §7, problem 2(a). [DOI](https://doi.org/10.1137/24M1640008); [Author PDF](https://www.columbia.edu/~wt2319/VV.pdf).
2. P. J. Graber and A. R. Mészáros, *Sobolev regularity for first order mean field games*, Annales de l’Institut Henri Poincaré C, Analyse non linéaire 35 (2018), 1557–1576, Theorem 1.2. [DOI](https://doi.org/10.1016/j.anihpc.2018.01.002).

Review: The SIAM source asks for local uniform convergence beyond its weighted L2 results. The displayed quadratic Hamiltonian and linear local coupling form an explicit case with possible vacuum, avoiding ambiguities about a weak value function outside the density support by asking directly for convergence of the viscous family. The July 2026 paper “Beyond separability” (DOI 10.1016/j.spa.2026.105061) assumes nonlocal measure dependence. Searches through 22 September 2026 located no resolution for this local-coupling assertion.

### 22. An algebraic vanishing-noise rate for kinetic mean-field games

Admitted page: [kinetic-mfg-vanishing-viscosity-rate](../../../cut_problems/problems/405-kinetic-mfg-vanishing-viscosity-rate.md)

1. W. Tang and Y. P. Zhang, *The Convergence Rate of Vanishing Viscosity Approximations for Mean Field Games*, SIAM Journal on Mathematical Analysis 57 (2025), 3217–3254, §7, problem 4(b). [DOI](https://doi.org/10.1137/24M1640008); [Author PDF](https://www.columbia.edu/~wt2319/VV.pdf).
2. M. Griffin-Pickering and A. R. Mészáros, *A variational approach to first order kinetic mean field games with local couplings*, Communications in Partial Differential Equations 47 (2022), 1945–2022, equation (1.1), §3.2 and existence/uniqueness theorems. [DOI](https://doi.org/10.1080/03605302.2022.2101003); [arXiv:2112.03141](https://arxiv.org/abs/2112.03141).

Review: The SIAM source explicitly asks for kinetic vanishing-viscosity rates. This formulation selects the quadratic acceleration and linear local-congestion case and defines the density through a strictly convex variational problem, including the inviscid density. The 2022 work establishes the underlying first-order variational theory, not a noise-dependent approximation rate. Searches through 22 September 2026 for kinetic MFG viscosity rates and acceleration-control convergence found no matching result.

### 23. Stationarity of Lipschitz weak solutions of the minimal-surface system

Admitted page: [lawson-osserman-stationarity](../../../problems/406-lawson-osserman-stationarity.md)

1. C. Mooney, *Bernstein theorems for nonlinear geometric PDEs*, survey (2024), §3, equations (7)–(8) and Remark 3.2. [Author PDF](https://www.math.uci.edu/~mooneycr/BernsteinTheorems_v5.pdf); [arXiv:2407.11903](https://arxiv.org/abs/2407.11903).
2. J. Hirsch, C. Mooney and R. Tione, *On the Lawson–Osserman conjecture*, Inventiones mathematicae (2026), §1, Theorem 1.1 and Remark 1.2. [DOI and full text](https://doi.org/10.1007/s00222-026-01442-4).
3. C.-J. Tsai and M.-T. Wang, *Calibrating Forms for Minimal Graphs in Arbitrary Codimension*, preprint (2026), §5, results under two-dilation assumptions. [Full text](https://arxiv.org/html/2604.04336v1).

Review: The 2026 Inventiones paper solves two-dimensional domains, and explicitly leaves higher-dimensional outer-critical maps unresolved. The April 2026 calibration paper assumes bounds on products of singular values of Du. These restrictions are absent here. Searches through 22 September 2026 for the higher-dimensional Lawson–Osserman conjecture located no general resolution.

### 24. Polynomial growth of every entire minimal graph

Admitted page: [entire-minimal-graphs-polynomial-growth](../../../problems/407-entire-minimal-graphs-polynomial-growth.md)

1. C. Mooney, *Bernstein theorems for nonlinear geometric PDEs*, survey (2024), §7.1, first open question on entire graphs. [Author PDF](https://www.math.uci.edu/~mooneycr/BernsteinTheorems_v5.pdf); [arXiv:2407.11903](https://arxiv.org/abs/2407.11903).
2. L. Simon, *Entire solutions of the minimal surface equation*, Journal of Differential Geometry 30 (1989), 643–688, introduction and construction of entire graphs asymptotic to cylinders. [DOI](https://doi.org/10.4310/jdg/1214443827).

Review: The survey distinguishes this growth question from the existence of exact polynomial solutions. Dimensions at most seven are excluded because Bernstein rigidity gives affine solutions there. Searches through 22 September 2026 found no result bounding every entire graph by a solution-dependent power. Guo’s April 2026 polynomial-solution paper studies exact polynomial solutions, rather than growth of all smooth solutions.

### 25. Polynomial anisotropic minimal graphs in dimensions four and five

Admitted page: [polynomial-anisotropic-minimal-graphs](../../../problems/408-polynomial-anisotropic-minimal-graphs.md)

1. C. Mooney, *Bernstein theorems for nonlinear geometric PDEs*, survey (2024), §7.2, polynomial solutions in lower dimensions. [Author PDF](https://www.math.uci.edu/~mooneycr/BernsteinTheorems_v5.pdf).
2. C. Mooney, *Entire solutions to equations of minimal surface type in six dimensions*, Journal of the European Mathematical Society 24 (2022), 4353–4361, §1 and Theorem 1.1. [DOI](https://doi.org/10.4171/JEMS/1202); [Author PDF](https://www.math.uci.edu/~mooneycr/Bernstein_6D_JEMS.pdf).
3. C. Mooney and Y. Yang, *The anisotropic Bernstein problem*, Inventiones mathematicae 235 (2024), 211–232, construction of nonpolynomial four-dimensional examples. [Publisher manuscript](https://par.nsf.gov/servlets/purl/10511787).

Review: The six-dimensional polynomial construction uses a C2,1 integrand, so that regularity is fixed explicitly here. The four-dimensional Bernstein counterexamples have subquadratic growth and do not supply a polynomial. September 2026 arXiv:2609.08972 proves a lower growth gap; August 2026 arXiv:2608.29117 concerns integrands close to isotropic area. Neither settles polynomial existence for arbitrary uniformly elliptic integrands in dimensions four or five. No matching resolution was located through 22 September 2026.

### 26. Continuous selection of small-time null controls for analytic systems

Admitted page: [analytic-controls-continuous-selection](../../../problems/409-analytic-controls-continuous-selection.md)

1. F. Marbach, *Time-iteration methods for controllability*, lecture notes (2026), Definition 4.16 and Open Problem 4.17. [Full text](https://arxiv.org/html/2602.19272v1).
2. J.-M. Coron, *Control and Nonlinearity*, Mathematical Surveys and Monographs 136, AMS (2007), Chapter 11, Proposition 11.22. [Book DOI](https://doi.org/10.1090/surv/136).
3. J.-M. Coron, *Links Between Local Controllability and Local Continuous Stabilization*, IFAC Proceedings Volumes 25(13) (1992), 165–171. [DOI](https://doi.org/10.1016/S1474-6670(17)52276-4).

Review: The February 2026 notes state the analytic implication as an open problem and explain why available sufficient conditions give continuous controls without proving the implication in full. Searches through 22 September 2026 found no later theorem resolving it. This asks for continuity of an actual control selection, distinct from finite-jet tests for controllability.

### 27. Quadratic-growth rigidity for the complex Monge–Ampère equation

Admitted page: [complex-monge-ampere-quadratic-growth](../../../problems/410-complex-monge-ampere-quadratic-growth.md)

1. C. Mooney, *Bernstein theorems for nonlinear geometric PDEs*, survey (2024), §7.4. [Author PDF](https://www.math.uci.edu/~mooneycr/BernsteinTheorems_v5.pdf).
2. Y. Wang, *A Liouville Theorem for the Complex Monge–Ampère Equation*, preprint (2013), main theorem assuming a quadratic asymptote with an o(|z|²) error. [arXiv:1303.2403](https://arxiv.org/abs/1303.2403).
3. H. Chen, J. Hu and L. Sheng, *Pogorelov interior estimates and a Liouville theorem for the complex Monge–Ampère equation*, preprint (16 September 2026), §1 discussion of Székelyhidi’s quadratic-growth question and Theorem 1.3. [Full text](https://arxiv.org/html/2609.18265v1).

Review: The September 2026 source records the exact two-sided growth question and distinguishes known results requiring metric completeness. Its new rigidity theorem assumes real convexity, which is stronger than plurisubharmonicity and absent here. Searches through 22 September 2026 located no resolution under the displayed growth condition alone.

### 28. Continuity of states driven by bounded admissible inputs

Admitted page: [bounded-input-state-continuity](../../../problems/411-bounded-input-state-continuity.md)

1. G. Weiss, *Admissibility of Unbounded Control Operators*, SIAM Journal on Control and Optimization 27 (1989), 527–545, Problem 2.4. [DOI](https://doi.org/10.1137/0327028).
2. F. Marbach, *Time-iteration methods for controllability*, lecture notes (2026), Remark 2.32. [Full text](https://arxiv.org/html/2602.19272v1).
3. P. Preußler and F. L. Schwenninger, *Implications of structured continuous maximal regularity*, preprint (2026), §4.4, Corollary 4.10 and following discussion. [Full text](https://arxiv.org/html/2605.12121v1).

Review: The May 2026 source explicitly describes its answer to Weiss’s question as partial: it covers reflexive spaces and several further Banach-space classes. The statement here retains arbitrary Banach state and input spaces. Searches through 22 September 2026 located no unrestricted proof or counterexample. This concerns continuity in time, not the disproved L2 resolvent-characterization version of the Weiss conjecture.

### 29. Sharp vanishing-viscosity control time for downstream transport

Admitted page: [positive-transport-sharp-uniform-control-time](../../../problems/412-positive-transport-sharp-uniform-control-time.md)

1. J.-M. Coron and S. Guerrero, *Singular optimal control: A linear 1-D parabolic–hyperbolic example*, Asymptotic Analysis 44 (2005), 237–257, introduction and conjecture on optimal times. [DOI](https://doi.org/10.3233/ASY-2005-707).
2. C. Laurent and M. Léautaud, *On uniform controllability of 1D transport equations in the vanishing viscosity limit*, Comptes Rendus Mathématique 361 (2023), 265–312, §1.1 and §4.4. [DOI](https://doi.org/10.5802/crmath.405); [Full PDF](https://www.numdam.org/item/10.5802/crmath.405.pdf).
3. P. Lissy, *Explicit lower bounds for the cost of fast controls for some 1-D parabolic or dispersive equations, and a new lower bound concerning the uniform controllability of the 1-D transport-diffusion equation*, Journal of Differential Equations 259 (2015), 5331–5352, Theorem 1.3 and comparison with positive transport. [Author PDF](https://cermics.enpc.fr/~lissyp/Publi/chal.pdf).

Review: The negative-velocity part of the original Coron–Guerrero conjecture has been disproved and is deliberately absent from this formulation. The 2023 treatment still records a gap between the positive-velocity lower and upper times. Searches through 22 September 2026 found no matching resolution for T>L/M; Lissy’s August 2026 arXiv:2608.08041 establishes a heat-control cost coefficient, not the displayed transport limit.

### 30. Intercritical norm inflation for the dispersion-managed Schrödinger equation

Admitted page: [intercritical-dispersion-managed-norm-inflation](../../../cut_problems/problems/413-intercritical-dispersion-managed-norm-inflation.md)

1. M. Kowalski, *On ill-posedness for the Gabitov–Turitsyn equation*, preprint (2025), equation (GT), Definition 1.3 and §6.4. [Full text](https://arxiv.org/html/2510.11887v1).
2. J. Kawakami and J. Murphy, *Small and large data scattering for the dispersion-managed NLS*, Discrete and Continuous Dynamical Systems 47 (2026), 256–285, introduction and scattering theorems. [DOI](https://doi.org/10.3934/dcds.2025118).
3. M.-R. Choi, Y. Hong and Y.-R. Lee, *Global existence versus finite time blowup dichotomy for the dispersion managed NLS*, Nonlinear Analysis 251 (2025), 113696, introduction and virial analysis. [DOI](https://doi.org/10.1016/j.na.2024.113696).

Review: Kowalski explicitly leaves the intercritical regime unresolved. Failure of differentiability of the solution map, proved there, is weaker than the displayed norm inflation. The homogeneous norm and two-sided short time follow Definition 1.3; choosing s=1/4 avoids the conserved mass endpoint. Searches through 22 September 2026 found no proof or counterexample for this fixed defocusing model.

### 31. Existence of a nonaffine polynomial minimal graph

Admitted page: [isotropic-polynomial-minimal-graph](../../../problems/414-isotropic-polynomial-minimal-graph.md)

1. Y. Guo, *On polynomial solutions to the minimal surface equation*, Calculus of Variations and Partial Differential Equations 65 (2026), 141, §1.1, Definition 1 and Theorems 1.1–1.3. [DOI](https://doi.org/10.1007/s00526-026-03316-2); [revised full text](https://arxiv.org/html/2404.00115v2).
2. C. Mooney, *Bernstein theorems for nonlinear geometric PDEs*, survey (2024), §7.1, polynomial-solution question. [Author PDF](https://www.math.uci.edu/~mooneycr/BernsteinTheorems_v5.pdf).
3. L. Simon, *The minimal surface equation*, in *Geometry V*, Encyclopaedia of Mathematical Sciences 90 (1997), 239–266, discussion of entire graphs and polynomial solutions. [Chapter DOI](https://doi.org/10.1007/978-3-662-03484-2_5).

Review: The March 2026 revision explicitly reports that no nonaffine scalar polynomial example is known. It rules out degrees two and three, homogeneous polynomials, and several possible tangent cones without resolving existence. Searches through 22 September 2026 found no later construction or general nonexistence theorem. Polynomial growth of all smooth entire graphs is a separate open assertion.

### 32. Uniform control of Neumann advection–diffusion for non-gradient flows

Admitted page: [nongradient-neumann-uniform-control](../../../problems/415-nongradient-neumann-uniform-control.md)

1. F. Et-Tahri, J. A. Bárcena-Petisco, I. Boutaayamou and L. Maniar, *On uniform null controllability of transport-diffusion equations with vanishing viscosity limit*, Mathematical Methods in the Applied Sciences 48 (2025), 6531–6552, equation (1), Definition 1.3, Theorem 1.5 and Remark 1.6. [DOI](https://doi.org/10.1002/mma.10693); [full text](https://arxiv.org/html/2412.16660v1).
2. J. A. Bárcena-Petisco, *Cost of null controllability for parabolic equations with vanishing diffusivity and a transport term*, ESAIM: Control, Optimisation and Calculus of Variations 27 (2021), 106, introduction and main control-cost results. [DOI](https://doi.org/10.1051/cocv/2021103).

Review: Remark 1.6 explicitly identifies removal of the gradient-field assumption as open. The statement specializes to autonomous smooth drift while retaining strict outward flux and the uniform neighborhood version of the flushing condition. The available Neumann theorem requires gradient drift; Dirichlet and tangential-boundary results do not provide this conclusion. Searches through 22 September 2026 located no resolution.

### 33. Positive equilibrium attraction for an irreversible catalytic reaction

Admitted page: [catalytic-reaction-diffusion-positive-attractor](../../../cut_problems/problems/416-catalytic-reaction-diffusion-positive-attractor.md)

1. T. L. Nguyen and B. Q. Tang, *Stability analysis of irreversible chemical reaction-diffusion systems with boundary equilibria*, Zeitschrift für angewandte Mathematik und Physik 77 (2026), 199, equation (1.1), the conjecture after Table 1, Theorem 2.1 and §2.3. [DOI and full text](https://doi.org/10.1007/s00033-026-02847-0).
2. K. Fellner, J. Morgan and B. Q. Tang, *Uniform-in-time bounds for quadratic reaction-diffusion systems with mass dissipation in higher dimensions*, Discrete and Continuous Dynamical Systems, Series S 14 (2021), 635–651, main boundedness theorem. [DOI](https://doi.org/10.3934/dcdss.2020334).

Review: The July 2026 paper proves boundedness, local stability of the positive equilibrium and instability of the boundary equilibrium, but states global attraction as a conjecture. Its printed nonnegative-data wording includes a stationary boundary equilibrium; the present formulation explicitly restricts to strictly positive data, removing that immediate obstruction. The irreversible network is not complex balanced, so the complex-balanced global-attractor question is distinct. Searches through 22 September 2026 located no resolution.

### 34. Polynomial growth of reachable neighborhoods for analytic control systems

Admitted page: [analytic-reachable-set-polynomial-growth](../../../problems/417-analytic-reachable-set-polynomial-growth.md)

1. S. Jafarpour, *On Small-Time Local Controllability*, SIAM Journal on Control and Optimization 58 (2020), 425–446, Conjecture 1.2 and its relation to finite-jet robustness. [DOI](https://doi.org/10.1137/16M1068797); [full preprint, Conjecture 2](https://arxiv.org/html/1604.02432).
2. F. Marbach, *Time-iteration methods for controllability*, lecture notes (2026), §4.7, equation (4.29) and Open Problem 4.24, the related norm-budget formulation. [Full text](https://arxiv.org/html/2602.19272v1).

Review: Jafarpour separately states this quantitative growth conjecture and the finite-jet determination conjecture. The known implication from polynomial growth to finite-jet robustness does not prove polynomial growth from controllability. The 2026 notes continue to identify the quantitative issue as open. Searches through 22 September 2026 found no general proof or counterexample; results for particular polynomial systems give sufficient conditions only.

### 35. Uniqueness of the zero-average dispersion-managed soliton

Admitted page: [zero-dispersion-soliton-uniqueness](../../../problems/418-zero-dispersion-soliton-uniqueness.md)

1. D. Hundertmark and Y.-R. Lee, *On non-local variational problems with lack of compactness related to non-linear optics*, Journal of Nonlinear Science 22 (2012), 1–38, §1.1, equations (1.1) and (1.3), Theorem 1.1, and Appendix C on translations and boosts. [DOI](https://doi.org/10.1007/s00332-011-9106-1); [full preprint](https://arxiv.org/pdf/1008.4631).
2. D. Hundertmark and R. Schnaubelt, *Dispersion Management*, KIT Collaborative Research Centre 1173, archived Project B2 (2015–2019; page last changed 2023), project summary identifying uniqueness modulo natural invariances as open. [Primary research-program description](https://www.waves.kit.edu/B2.php).
3. M.-R. Choi, S. Jin and Y.-R. Lee, *Uniqueness of a Minimizer for a Variational Problem Related to the Dispersion Managed Nonlinear Schrödinger Equation*, SIAM Journal on Mathematical Analysis 55 (2023), 2595–2614, introduction and small-parameter uniqueness result for positive average dispersion. [DOI](https://doi.org/10.1137/22M1499972).

Review: The archived primary research-program description identifies ground-state uniqueness as open, and the 2012 paper supplies the precise zero-average variational model and continuous symmetries. Reflection and dispersion-time reversal are included explicitly to quotient all evident symmetries of this uniform-profile functional. The SIAM uniqueness theorem assumes positive average dispersion and a sufficiently small perturbation parameter; it does not apply to the zero-average functional here. Searches through 22 September 2026 for zero-dispersion ground-state uniqueness found no resolution. Setwise orbital stability and uniqueness of evolution for a fixed initial state are different results.

## Formulation safeguards

The zero-dispersion uniqueness question explicitly quotients phase, translations, modulations, reflection and dispersion-time reversal; its open-status source is an archived primary investigator program description, not a claimed new2026 assessment. The catalytic reaction formulation corrects the published conjecture’s overly broad nonnegative-data wording by requiring strictly positive initial data.

Distinct pairs were checked explicitly: exact polynomial minimal-graph existence versus growth of arbitrary entire graphs; MTW injectivity-domain convexity versus transport continuity with that convexity assumed; bounded-input trajectory continuity versus the separate resolvent Weiss conjecture; analytic control selection versus quantitative reachable radii versus existing finite-jet robustness.
