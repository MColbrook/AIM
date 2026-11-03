# Fresh mathematical audit: AIM 1007

**Reviewer:** Codex (AI), 3 November 2026.

**Author and submitter:** Siavash Sadeghi.

**Scope:** Complete supplied TeX argument, checked against the current pinned repository target and the published source. This is a fresh derivation-based AI audit, not an independent human review, a second reviewer in this session, or a formal verification.

## Verdict

No substantive mathematical defect was identified. The argument establishes the proposed counterexample provided the displayed standard Sobolev, transform and trace facts are used as specified below. The supporting symbolic checker independently recomputes sensitive algebraic identities; it does not certify the infinite-dimensional argument. The appropriate submitted status remains **Solution claimed** pending further independent review.

## Audit of the complete proof

1. **Target and geometry.** For the straight reference curve the metric induced by $`(s,t)\mapsto(s,t\cos\theta(s),t\sin\theta(s))`$ is exactly the stated metric. Bounded twist gives a Lipschitz unit normal. The construction satisfies Assumption 1, (3.1), and (5.1) of Krejcirik-Zahradova; no stronger smoothness assumption from the thin-strip section is required. The absolute value at the joining section is allowed by these hypotheses. The polished proof makes the embedding and dimension extension explicit.

2. **Unweighted auxiliary decomposition.** The projection onto $`\chi=\cos(\pi t/2)`$ is taken in unweighted transverse $`L^2`$, as required for the divergence-form pencil. It is not asserted to be orthogonal in physical weighted space. All higher modes remain in the complementary space. Projection commutes with the free operator and the longitudinal weights and preserves the required transverse Sobolev estimates.

3. **Free closed inverse and domain.** The longitudinal cosine transform and transverse Dirichlet expansion diagonalize the Neumann/Dirichlet operator. Since $`E_2-\lambda_*>0`$, the multiplier ratio controls two longitudinal derivatives, two transverse derivatives and the mixed derivative uniformly in every mode. Even extension at the Neumann edge gives the stated $`H^2`$ domain, including the corner compatibility implicit in the trace conditions. No finite-mode approximation enters.

4. **Weighted estimate.** The weight $`w=S+\sqrt{1+s^2}`$ is comparable to $`S+s`$, has uniformly bounded first and second derivatives, and satisfies $`w'(0)=0`$. Bounded smooth truncations preserve Neumann data. The commutator is exactly $`-2w_N'v_s-w_N''v`$. The unweighted inverse estimate, product rule and Fatou's lemma yield the weighted two-derivative estimate with constants independent of large $`S`$. This avoids applying a non-boundary-preserving linear weight directly to the Neumann inverse.

5. **Exact elimination of closed channels.** Expanded perturbation coefficients are $`O((S+s)^{-1})`$, including the first longitudinal derivative of the coefficient. Thus the feedback inverse has norm $`O(S^{-1})`$ on the weighted closed domain. The forcing from $`u\chi`$ is bounded by $`\|u\|_{H^2}`$ without imposing a condition on $`u'(0)`$. The reconstructed closed component has zero derivative at the interface. A second multiplication by the perturbation yields feedback in $`(S+s)^{-2}L^2`$. The fixed-point inverse is exact and depends continuously and periodically on phase in operator norm.

6. **Scalar normalization and resonance.** Direct integration gives the two transverse moments and the Taylor coefficients of $`A`$ and $`B`$. Differentiating $`y=\sqrt\alpha\,u`$ gives the displayed sign of $`W`$. The coefficient of the nonoscillatory first-order term is $`mk^2-1/2=0`$. Independently differentiating the full profile gives

   ```math
   \frac{m}{4}b''+\frac{4k\cos(2ks+\delta)}{S+s}
   =\frac{4\sin(2ks+\delta)}{(S+s)^2}
    +\frac{4+2\cos(2ks+\delta)}{k(S+s)^3}.
   ```

   Taylor remainders involve only $`b^2,bb'',(b')^2`$, hence are uniformly $`O((S+s)^{-2})`$. Multiplication by $`\alpha^{-1/2}`$ preserves $`H^2`$ uniformly. The exact nonlocal right-hand side is therefore bounded from $`H^2`$ into the twice-weighted forcing space, rather than being discarded as a formal error.

7. **Rotation and normal form.** Averaging the exact rotated matrix yields the stated real symmetric involution $`M_\delta`$. Its stable vector has eigenvalue minus one and changes sign after a full phase turn. The periodic zero-mean remainder has a bounded primitive $`Z`$ with $`Z(0)=0`$. Direct matrix multiplication verifies the exact remainder after $`a=(I+Z/\rho)x`$. The remainder is $`O(\rho^{-2})`$ with constants uniform in phase and large scale.

8. **Right inverse and its small norm.** Differentiation of both integral kernels gives $`x'=M_\delta x/\rho+F`$. The stable kernel has squared Hilbert-Schmidt norm $`1/(2S^2)`$. The unstable kernel has row and column integrals at most $`1/(2S)`$. These prove the $`O(S^{-1})`$ bound from twice-weighted forcing to unweighted $`L^2`$. The normal-form remainder is then a contraction. The reconstructed vector equation gives $`v_1'=kv_2`$, so the scalar output has two derivatives in $`L^2`$ even when the forcing has no derivative. It also establishes the asserted $`H^2`$ operator-norm continuity.

9. **Normalization, nonzero solution and phase.** At zero both changes of variables are the identity. The integral operator has zero stable trace; the homogeneous seed has stable trace $`e_\delta/S`$. Thus $`\ell_\delta(h_\delta)=1/S`$ and $`\ell_\delta(G_\delta g)=0`$ exactly. The final contraction retains this normalization and cannot give the zero function. All coefficients and inverse maps are periodic, while the seed is antiperiodic; the resulting real derivative trace is continuous and antiperiodic. The intermediate value theorem supplies the matching phase without assuming a numerical sign estimate or prescribing one in advance.

10. **Reflection and operator domain.** At the selected phase the complete half-strip derivative trace vanishes, not only the open component. Even reflection therefore belongs to full-strip $`H^2`$. The coefficient is continuous and Lipschitz even though its derivative can jump. Zero joining flux eliminates any interface distribution. Integration by parts and density yield the form identity against every $`H_0^1`$ test, which places the nonzero weighted-$`L^2`$ function in the associated operator domain.

11. **Admissibility, embeddedness and scaling.** Positivity, nontriviality, amplitude and uniform decay follow from the profile envelope. Choose the scale larger than every contraction bound and $`12k`$; all these bounds are finite and uniform in phase. The energy is strictly between the first two thresholds. The source's essential-spectrum theorem applies under the verified geometry. The unitary dilation preserves weighted norm and scales the form by $`a^{-2}`$, proving every-width claims without changing the operator.

## Changes made during review

- Added Siavash Sadeghi as author and in PDF metadata; identified the repository problem and pinned revision.
- Replaced references to an unspecified question with the exact target and stated the review status.
- Expanded the geometric realization and unitary scaling already used by the supplied proof.
- Corrected minor wording and added reproducible exact algebra checks and repository submission documents.
- Preserved the construction, energy, profile, functional spaces, and existence-based phase selection. No numerical spectral experiment was substituted for the argument.

## Provenance and limits

The user-supplied ZIP SHA256 is `ebeef2307475e0b8d46e3783256d605ed1787e404bc0a46e7915f68bbf980813`; its original TeX SHA256 is `7f311d2eae12cf6c2ca2e4a80c4acda1290840f5edaf8257e71861f9c35601a9`. The accompanying research-state note reports previous agent reviews. Their underlying transcripts were not supplied and are not counted as independent evidence here. This review read and re-derived the argument directly.

The proof does not provide an effective numerical value of the minimum scale, a certified numerical phase, a computed eigenfunction, or Lean verification. None is required by the existence question. The source's separate resonance problem and behavior outside the specified strip class are not claimed to be resolved.
