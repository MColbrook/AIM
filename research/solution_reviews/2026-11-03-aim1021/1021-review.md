# Independent mathematical review: AIM 1021

**Decision:** Solved — Counterexample.

**Author and submitter:** Matthew J. Colbrook.

**Reviewer:** Codex (AI), 3 November 2026. The complete supplied proof was read and its central calculations and estimates were re-derived. This is an AI mathematical audit, not human peer review or Lean verification.

**Target:** [AIM 1021](../../../problems/1021-must-limit-periodic-discrete-schrodinger-operators-have-pure-spectral-type.md) at repository revision `b014a51815ffd025d2b1abc4a3954205dfbf61e0`.

**Proof:** [PDF](../../solutions/1021-limit-periodic-mixed-spectrum/limit_periodic_mixed_spectrum.pdf) and [TeX](../../solutions/1021-limit-periodic-mixed-spectrum/limit_periodic_mixed_spectrum.tex). The [receipt](../../solutions/1021-limit-periodic-mixed-spectrum/SOURCE_RECEIPT.json) records the original submission's hash, and the [source diff](../../solutions/1021-limit-periodic-mixed-spectrum/source_changes.diff) shows the packaging changes.

## Conclusion and target comparison

No substantive gap was found. The proof constructs one bounded real uniform limit of periodic sequences whose scalar, nearest-neighbor discrete Schrödinger operator has two nonzero spectral subspaces, absolutely continuous and singular continuous, and has no eigenvalues. One example answers the universal purity question negatively. The proof retains the exact operator and all quantifiers in the current AIM statement.

| Current target | What the proof establishes |
| --- | --- |
| A bounded real potential on the whole integer lattice | The periodic approximants converge uniformly; the sum of perturbation amplitudes is less than 0.002, and the potential norm is less than 100.002. |
| Limit-periodic, rather than a different class of aperiodic potentials | Each approximant is periodic with nested integer periods tending to infinity. |
| Scalar discrete Schrödinger operator with both hoppings equal to one | The transfer matrices, spectral measures and Gordon argument all use this exact operator. |
| More than one nonzero basic spectral subspace in one operator | A fixed positive-measure compact set supports a nonzero absolutely continuous submeasure; an isolated nonempty cluster has zero Lebesgue measure and continuous spectral measures. |
| Singularity is continuous, not merely singular | Exact local three-block repetitions exclude every eigenvalue. |
| A single operator, rather than changing hull element or coupling | Both continuous types occur simultaneously, even in the measure of the same vector. No answer to the separate AIM 1018 or 1020 questions is claimed. |

## Audit of the full argument

1. **Periodic local measure and indexing.** With monodromy transferring the pair at sites zero and minus one across a period, the Bloch multipliers give the diagonal density

   ```math
   \rho_W(E)=\frac{|(M_W(E))_{12}|}{\pi\sqrt{4-D_W(E)^2}}.
   ```

   The Wronskian computation uses the upper-right entry with this convention. The free case has the usual arcsine density; enlarging an unchanged period leaves the local density unchanged. There is no factor dividing this measure by the period. Strict ellipticity, rather than the interior of the spectral support, correctly excludes closed Floquet gaps.

2. **Elliptic coordinates and phase monotonicity.** The explicit lower-triangular determinant-one conjugacy is smooth on each elliptic component; its upper-right entry cannot vanish there. Differentiating the transfer product gives the stated nonnegative, nonzero matrix $`C`$. In conjugate coordinates the trace with $`J`$ cancels the derivative of the conjugacy, leaving

   ```math
   \theta_E=-\tfrac12\mathop{\mathrm{tr}}(B^{\mathsf T}CB)<0.
   ```

   Its magnitude is bounded above and below on the fixed compact parameter set. Positivity requires only that $`C`$ be nonzero and nonnegative, since $`B`$ is invertible; positive definiteness is not silently assumed.

3. **Adiabatic normal form.** The trace-free matrix $`B^{-1}B_s`$ splits into a multiple of $`J`$ and a symmetric trace-free part. On the latter two-dimensional space, rotation conjugacy has angle twice the Floquet phase. The homological equation is invertible with denominator bounded away from zero by ellipticity. Expanding the proposed correction gives a one-step remainder of order $`N^{-2}`$ and removes the first-order symmetric part with the stated sign. Products over at most $`N`$ steps are uniformly bounded; telescoping gives a full-period error of order $`N^{-1}`$. The zero plateau makes both endpoint corrections trivial. Bounds for subproducts and inverses follow as well, including the finitely many extra site transfers within an old cell.

4. **Density cores and their quantitative margins.** The explicitly summed corrected phase has derivative comparable to minus $`N`$; this uses bounded derivatives of its summands, not a derivative estimate on the telescoping error. The phase change of variables bounds the measure removed near its sine zeros. The trace and upper-right-entry estimates give the density error $`O((N\eta^2)^{-1})`$ on the retained cores. Differentiating the exact site-transfer product gives $`|D'|\le Cq`$, because left and right partial products are uniformly bounded. A trace margin of order $`\eta^2`$ therefore gives an energy margin of order $`\eta^2/q`$ from every nonelliptic point. This is the margin needed for the next perturbation, including near closed gaps.

5. **Barrier and band widths.** At each target-cluster energy, at least one of the two shifted old operators is a positive distance from that energy. The associated plateau has length proportional to the new period. Cutting off the normalized Bloch function produces at most four bounded boundary sources. Conjugating the resolvent by a clipped monotone exponential weight with $`2\sinh\gamma=d/2`$ gives the stated Combes–Thomas decay at the plateau center. Conservation of current and the boundary Hellmann–Feynman identity make the Floquet-band derivative exponentially small there. Floquet eigenvalues are simple for phase strictly between zero and pi; nonvanishing current gives monotonicity. Integrating only over the part of a branch in the fixed interval proves the band-portion bound. There are at most $`q`$ bands. None of this requires multiplying estimates for hyperbolic and elliptic transfer blocks as though their expanding directions agreed.

6. **Shift selection and initial constants.** The difference set of at most $`p`$ disjoint interval components has length at most $`2p\mathop{\mathrm{Leb}}(S)`$; the stated inequality therefore supplies a separating shift in the required open interval. Compactness and the fixed isolation gaps turn disjointness into a uniform positive barrier distance. The period-three discriminant, both factorizations, the two rational endpoint values, the upper-band derivative bound, and the separating initial shift were recomputed exactly. They give the required two separated energy regions at the first step.

7. **Inductive parameter order.** At a given stage the old potential, period, retained cores and amplitude are fixed before choosing the new period. Fixing the measure-loss tolerance first leaves constants independent of the new integer $`N`$. The new margin is at least a positive stage constant divided by the new period, whereas its target-cluster measure is exponentially small in $`N`$. Thus

   ```math
   p_N\mathop{\mathrm{Leb}}(S_N)<r_N,\qquad
   r_N=\min\{g_N/8,\ 2^{-j-1}/p_N,\ \delta_j/8\}
   ```

   is feasible: the required comparison reduces to $`N^3e^{-c_jN}\to0`$. A separating next shift then lies below the new margin, below $`2^{-j}/p_j`$, and below one quarter of the preceding amplitude. All constants for the following stage are finite and are fixed before its new period is chosen. This addresses the main potential circularity in combining the two spectral mechanisms.

8. **Absolutely continuous spectrum survives.** The retained compact sets are nested and lose a summable amount of measure, so their intersection has positive measure. Telescoping the density losses gives the same positive density lower bound on this fixed intersection for every approximant. Their spectral measures therefore dominate one fixed nonzero absolutely continuous measure. Operator-norm convergence implies weak convergence of the local measures on a common bounded energy interval; testing against nonnegative continuous functions preserves this domination in the limit. No assertion about mass on moving exceptional sets or convergence at moving band edges is needed.

9. **Nonzero singular cluster survives.** The tail perturbation has size at most four thirds of the next amplitude, and its product with the old period tends to zero. Hausdorff spectral continuity and the fixed gaps at the interval endpoints place the limiting upper cluster inside neighborhoods of at most $`p_j`$ old intervals. Their total length is bounded by the old cluster length plus twice the period times the tail size; this tends to zero. The cluster is nonempty by spectral continuity from the initial isolated upper band. Moreover, the origin is untouched by every update. Its exact second spectral moment around 100 is two; the distant lower cluster then gives the stated strictly positive mass in the upper interval for the same vector that detects the absolutely continuous part.

10. **No eigenvalues and final conclusion.** The zero plateau at every update fixes three full old-period blocks around the origin. Later cell lengths are large enough to preserve that same interval; negative indices are handled by periodicity of the profile near the integers. The determinant-one transfer matrix across those identical blocks satisfies the two Cayley–Hamilton identities. According to the trace size, one of them gives a norm lower bound of one half at one of the three distant block endpoints. Since the periods tend to infinity, every nonzero solution fails to be square summable. Thus the nonzero singular restriction is singular continuous, completing the counterexample. A rapid uniform approximation rate is not an unstated hypothesis of this exact local repetition argument.

## References and current-source check

All four references in the proof were checked in their primary texts:

- [Damanik–Fillman, arXiv:1802.05794v1](https://arxiv.org/pdf/1802.05794v1): the operator in the introduction and Question 10.1 on printed page 36 match AIM 1021. Section 6.2 contains the Gordon background. The published chapter details agree with the repository's primary-source record; the precise question and section locators here refer to the linked preprint.
- [Teschl's author-hosted book](https://www.mat.univie.ac.at/~gerald/ftp/book-jac/jacop.pdf): title, author, AMS series volume 72 and publication year 2000 are correct. Chapter 7 covers periodic Floquet theory; Chapter 2 supplies Weyl functions and Green-function spectral formulas. Conventions were compared with the proof's explicit indexing rather than copied without translation.
- [Avila, arXiv:1210.6325v1](https://arxiv.org/pdf/1210.6325v1): Section 2.6 and Lemmas 2.11–2.12 are the cited slow-deformation background. The submission proves its own discrete estimate and quantitative margin; it does not attribute its mixed-spectrum theorem to Avila.
- [Remling, arXiv:0706.1101v2](https://arxiv.org/pdf/0706.1101v2): Proposition 4.1(d) gives compactness of the uniformly bounded reflectionless class on a fixed positive-measure set, and part (b) gives half-line absolute continuity. The optional remark was expanded to explain the passage through Weyl functions to the full-line operator. The direct measure proof does not depend on that alternative.

No missing specialized theorem needed by the main proof was identified. The Combes–Thomas estimate, current identity, phase correction and Gordon calculation are derived in the document rather than left to an unspecified citation.

Bounded searches on 3 November 2026 used the title, limit-periodic spectral purity, mixed spectrum, both continuous spectral types, Damanik–Fillman Question 10.1 and the author's name. The local solution packages and current open submissions contained no matching solution. The relevant recent primary papers located were [Gomez Solis, arXiv:2610.19416v1](https://arxiv.org/html/2610.19416v1), which assumes a specific exponential approximation class, and [arXiv:2611.01303v1](https://arxiv.org/html/2611.01303v1), a continuum transport result with a quantitative rate hypothesis. Their assumptions and conclusions do not supply this unrestricted discrete mixed-spectrum construction. These searches do not establish publication priority; the decision rests on the submitted proof.

## Packaging and verification

The submitted source's SHA256 is `b4ce95bf20873d9aae170b7039e25d82a791471e08de735ce2906251a8882190`. The original input remains unchanged. The packaged source adds the requested author and verified Cambridge contact, a suitable title and PDF metadata, the exact AIM target and pinned revision, more precise bibliographic links, and the explanation of the optional reflectionless remark. The construction, quantitative estimates, parameter order and main proof are unchanged.

The supporting checker passed 35 exact identities and inequalities in both normal and optimized Python, and both modes rejected two deliberately incorrect inputs. Its output is linked from the [reproduction record](../../solutions/1021-limit-periodic-mixed-spectrum/REPRODUCTION.md). These finite checks support sensitive algebra and constants; they do not constitute a formal verification of the infinite construction.

The saved source compiled successfully in the built-in document compiler. The exported nine-page PDF was rendered and visually inspected; its final log has no unresolved citations or references, LaTeX warnings, or box warnings. The local catalogue and selection-preservation checks are required before publication. The original AIM statement, all problem IDs and the local working folders are preserved.
