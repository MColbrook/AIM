# AIM 1007: independent review of PR #181

**Decision:** Solved — Counterexample.

**Reviewer:** Codex (AI), 3 November 2026. This review was performed separately from the submission-stage audit included in the PR. It is not human peer review or Lean verification.

**Author:** Siavash Sadeghi.

**Submission:** [PR #181](https://github.com/MColbrook/AIM/pull/181), pinned head `9491e1e3d3ac403100ce5ff6b8b663d0998fc922`.

**Target reviewed:** [AIM 1007](../../../problems/1007-embedded-eigenvalues-in-asymptotically-flat-twisted-strips.md), current main revision `c661dce4e5da54acf669b8f5d554bde72916fa69`. Its mathematical statement agrees with the statement at the submission's base revision `ee5c5c52f527db2f310cb0734bbebc9f7b95aac8`. The current ID and statement are preserved.

**Proof:** [PDF](../../solutions/siavash-sadeghi-1007/twisted-strip-counterexample.pdf) and [TeX](../../solutions/siavash-sadeghi-1007/twisted-strip-counterexample.tex). The submitted proof files are unchanged.

## Verdict and exact scope

The proof gives a complete counterexample to the universal absence of embedded eigenvalues asked in AIM 1007. No substantive gap was found after reading the complete source and checking its estimates, boundary conditions, normalization, geometry and correspondence to the published question. The existence of a suitable sufficiently large scale and a matching phase is proved; numerical values are not required or supplied.

For unit half-width, define

```math
m=\frac13-\frac2{\pi^2},\qquad k=(2m)^{-1/2},\qquad
\lambda_* = \frac{\pi^4}{4(\pi^2-6)}.
```

For every sufficiently large $`S`$, the proof selects a phase in the twist profile

```math
q(s)^2=\frac{16k}{S+|s|}\left(1+\frac12\cos(2k|s|+\delta)\right)
```

so that the all-Dirichlet strip has a nonzero eigenfunction at $`\lambda_*`$. The strict inequalities $`E_1<\lambda_*<E_2`$ hold. This refutes the proposed absence assertion. It does not concern the source's separate resonance question.

## Primary source and target comparison

The published [Krejčiřík–Zahradová paper](https://files.ele-math.com/articles/oam-14-41.pdf), *Operators and Matrices* 14 (2020), 635–665, [DOI 10.7153/oam-2020-14-41](https://doi.org/10.7153/oam-2020-14-41), was checked directly. The title, authors, journal details and [arXiv identifier 1906.02431](https://arxiv.org/abs/1906.02431) agree with the submission's bibliography. Assumption 1, the metric and form, condition (3.1), Theorems 3.1 and 5.1, Corollary 5.3 and Open Problem 5.6 were compared with the construction. The proof uses elementary transform, Sobolev, trace, integral-operator and closed-form representation facts in addition to this reference; no missing specialized external theorem was identified.

| Target condition | Check |
| --- | --- |
| Unit-speed reference curve and relatively parallel normal frame | A straight line and its constant normal frame meet the required regularity. |
| Lipschitz unit twisting vector and pure twisting | Integrating bounded $`q`$ gives $`\Theta=(\cos\theta,\sin\theta,0,\ldots,0)`$ with $`|\Theta'|=q`$; the curvature vector is zero. |
| Nonzero, bounded, asymptotically vanishing twist | $`0<q^2\le24k/(S+|s|)`$; increasing the scale to at least $`12k`$ enforces the unit-width amplitude bound. |
| Same all-Dirichlet operator | The induced metric is $`\mathop{\mathrm{diag}}(1+t^2q^2,1)`$; the proof uses its exact divergence equation, weighted norm and quadratic form. |
| Embedded eigenfunction in the operator domain | Both contractions solve the exact equation, the phase supplies the full Neumann trace at the join, and the reflected weak form establishes operator-domain membership. |
| Every allowed dimension and width | The embedding extends by zero coordinates; unitary dilation scales the eigenvalue by $`a^{-2}`$. |

## Independent checks of the analytic argument

1. **Closed-channel inverse and its boundary condition.** The transverse projection is in auxiliary unweighted transverse $`L^2`$, not asserted to be orthogonal in the physical weighted norm. All modes above the first are retained. The cosine transform in the longitudinal variable, together with the transverse eigenbasis and the positive gap $`E_2-\lambda_*`$, bounds the free inverse from $`L^2`$ to $`H^2`$, including the mixed derivative. For the weighted estimate, $`w=S+\sqrt{1+s^2}`$ preserves the Neumann condition because $`w'(0)=0`$. Smooth bounded truncations give the commutator $`-2w_N'v_s-w_N''v`$; the unweighted bound, product rule and Fatou's lemma yield a constant independent of large $`S`$.

2. **Exact elimination rather than a mode truncation.** The perturbation coefficients and the required coefficient derivatives are uniformly $`O((S+s)^{-1})`$. On the weighted closed domain the feedback map has norm $`O(S^{-1})`$, so its Neumann inverse exists. The forcing from the scalar component requires no longitudinal boundary condition on that component. The returned closed component has zero derivative at the join. Applying the perturbation a second time places the scalar feedback in the twice-weighted forcing space, with a bound independent of the scale. Phase continuity follows in these operator norms.

3. **Scalar normalization, sign and remainder.** Direct transverse integration gives $`m=\int t^2\chi^2`$ and $`\int t^2\chi'^2=E_1m+1`$. With $`y=\sqrt\alpha u`$, direct differentiation gives

   ```math
   W=-\frac\beta\alpha-\frac{\alpha''}{2\alpha}
     +\frac{(\alpha')^2}{4\alpha^2}.
   ```

   Its first-order expansion is $`k^2+(mk^2-1/2)b+(m/4)b''`$. The choice $`mk^2=1/2`$ cancels the nonoscillatory term. Differentiating the full profile leaves the resonant term $`-4k\cos(2ks+\delta)/(S+s)`$ and a uniformly twice-decaying remainder. The omitted Taylor expressions contain $`b^2`$, $`bb''`$ and $`(b')^2`$, all of that order. The closed-channel feedback remains in the exact equation as a bounded, generally nonlocal map from $`H^2`$ into the twice-weighted space; it is not replaced by a scalar potential or dropped.

4. **Normal form and a small right inverse.** Rotating the scalar equation gives the stated mean matrix $`M_\delta`$, a symmetric involution, and a zero-mean periodic remainder with a bounded primitive. Expanding the exact change $`a=(I+Z/\rho)x`$, where $`\rho=S+s`$, gives

   ```math
   D=\rho^{-2}(I+Z/\rho)^{-1}([M,Z]+NZ+Z).
   ```

   The stable integral kernel after inserting the forcing weight is $`1_{r\le s}/(\rho(s)\rho(r))`$; its squared Hilbert–Schmidt norm is $`1/(2S^2)`$. The unstable kernel is $`1_{r\ge s}\rho(s)/\rho(r)^3`$; its row and column integrals are at most $`1/(2S)`$. These estimates prove the needed $`O(S^{-1})`$ inverse bound. The normal-form remainder is then a contraction. Reconstructing the two-component equation yields $`v_1'=kv_2`$ and an $`L^2`$ right-hand side for $`v_2'`$, which supplies scalar $`H^2`$ regularity without differentiating the forcing.

5. **Nonzero normalization and phase selection.** Both changes of variables equal the identity at zero. The integral solution has zero stable trace, while the homogeneous seed has stable trace $`e_\delta/S`$. The final exact contraction therefore preserves $`\ell_\delta(y)=1/S`$ and cannot return zero. All operator coefficients are periodic in phase; the chosen real stable vector is antiperiodic. Consequently the real derivative trace $`u_\delta'(0)`$ is continuous and changes sign over a full phase turn. The intermediate value theorem provides a zero. This argument does not rely on a numerical phase or on an assumed sign estimate.

6. **Reflection, flux and the physical eigenvalue.** At the selected phase both the open and closed derivatives vanish at zero. Even reflection is thus $`H^2`$ on the full strip. The even coefficient is continuous and Lipschitz, and a derivative jump there is admissible. The longitudinal flux has zero joining trace, so integration by parts on the two halves leaves no interface term. Density extends the resulting identity to the form domain. Since the metric weight and its inverse are bounded, the eigenfunction is nonzero in physical weighted $`L^2`$ and belongs to the operator domain. The verified geometry permits application of the source's essential-spectrum theorem, placing its eigenvalue in the continuum. The known Hardy inequality excludes the bottom threshold and does not prohibit this higher eigenvalue.

7. **Quantifiers and scaling.** All lower bounds on the scale are finite and uniform in phase, so one scale can satisfy every contraction and amplitude bound. The strict gaps are

   ```math
   \lambda_*-E_1=\frac{3\pi^2}{2(\pi^2-6)}>0,\qquad
   E_2-\lambda_*=\frac{3\pi^2(\pi^2-8)}{4(\pi^2-6)}>0.
   ```

   The map $`(s,t)\mapsto(s,t\cos\theta(s),t\sin\theta(s),0,\ldots,0)`$ realizes the metric and is injective. For arbitrary half-width, $`q_a(s)=a^{-1}q(s/a)`$ and $`U_a\psi=a^{-1}\psi(s/a,t/a)`$ preserve the weighted norm and multiply the quadratic form by $`a^{-2}`$. Thus the construction satisfies the entire current target, not only a restricted case.

## Reproduction and integration

The supplied 15-entry checksum manifest and every downloaded Git blob were verified at the pinned PR head. [Submission receipt](submission-receipt.json) preserves those original digests. During incorporation, the solution README was updated to link this acceptance, and the resolution report's diagonal-matrix notation was changed to the repository's supported Markdown math syntax. The checksum manifest was regenerated. The submission-stage reports remain as dated records, and the proof PDF, TeX and checker are unchanged.

The safe symbolic checker was inspected before execution. With Python 3.12.14, SymPy 1.14.0 and mpmath 1.3.0, all 28 exact identities passed in both normal and optimized Python. Both modes also rejected all three deliberately incorrect test expressions; see [reproduction output](reproduction.log). These checks support the algebra, not the functional-analytic existence proof. The nine-page supplied PDF was rendered and visually inspected; the document is legible and its reference agrees with the TeX. No new PDF build is claimed in this review.

The PR's successful Lean workflow selects an existing, unrelated AIM 114 project. It is not formal verification of AIM 1007. No Lean status or verification record is added.

The local integration preserves the contributor's commits, uses the current catalogue as its base, updates only AIM 1007's status and evidence, and regenerates the current indexes. Its original Problem statement is preserved byte-for-byte as normalized text. IDs, selection decisions and the local working folders are not changed. The catalogue check and the frozen-selection verifier are run before committing.
