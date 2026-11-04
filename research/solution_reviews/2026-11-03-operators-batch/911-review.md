# AIM 911: mathematical review

**Final status:** Partially resolved. **Reviewed:** 3 November 2026, by Codex (AI), separately from the author.

[Canonical problem](../../../problems/911-the-sharp-constant-in-the-critical-dirac-norm-inequality.md) · [PDF manuscript](../../solutions/911-dirac-radial-bounds-stability/aim911.pdf) · [source and reproduction](../../solutions/911-dirac-radial-bounds-stability/README.md).

The audit compares the complete supplied argument with the current target at revision 5d7e26e8444eb98de91988454564e45e011107c4. The original archive's earlier review assertions were not accepted as evidence.

## AIM 911: independent proof audit

Reviewed on 3 November 2026 by Codex (AI), separately from the manuscript author.

**Verdict: Partially resolved.** Both submitted theorems are correct in their stated scope. The radial-class theorem and the full tangent-space Hessian inequality do not determine the global infimum in the canonical problem. A second independent reviewer also checked both arguments.

### Target and known scalar competitor

The current target is the infimum of $`\|D_d\psi\|_p/\|\psi\|_q`$ over the full distributional graph domain, for every integer $`d\ge3`$, with $`p=2d/(d+1)`$ and $`q=2d/(d-1)`$. In Frank--Loss the power-normalized constant is $`C_d^p`$. The canonical definition and all its quantifiers are preserved.

The scalar competitor $`f(r)=(1+r^q)^{-(d-1)/2}`$ and its quotient $`K_d=dI_d^{1/d}`$ are already in Bieganowski--Mederski, Theorem 4.1. They are not presented as a newly discovered competitor. The submitted restricted theorem and stability proof are independently checked below, without a priority claim.

### Restricted radial class

Hermiticity of the Clifford matrices makes $`v=iu`$ an admissible unit-spinor pair: every $`\langle u,\gamma_j u\rangle`$ is real. The specified real orthogonality condition removes both cross terms, giving exactly
```math
|\psi|^2=f^2+g^2,\qquad |D_d\psi|^2=f'^2+(g'+(d-1)g/r)^2.
```
The Kelvin substitution $`h(r)=r^{1-d}g(1/r)`$ preserves the $`L^q`$ norm and sends the derivative norm to that of $`g'+(d-1)g/r`$, because $`(d-1)q=(d+1)p=2d`$. Thus the same sharp scalar Sobolev constant applies to both channels.

The first mixed-norm step is the triangle inequality in $`L^{q/2}`$. The reverse placement of the two-channel norm in the final step is justified by Minkowski in the finite-dimensional space $`\ell^{2/p}`$; its direction is correct because $`p\le2`$. No angular channel outside the stated class is covered.

The graph-domain density argument works at both zero and infinity: the cutoff error is at most $`\|\nabla\chi\|_d\|\psi\|_{L^q(\mathrm{supp}\nabla\chi)}`$, with uniformly bounded first factor and vanishing second factor. On a fixed annulus the two real orthogonal projections recover the distributional profile derivatives in $`L^p`$, so one-dimensional smoothing is legitimate. No boundary regularity or unstated pointwise differentiability assumption is imposed.

For the scalar optimizer the beta integrals give $`\int f^q=I_d`$ and $`\int|\nabla f|^p=d^p I_d`$, hence exactly $`K_d`$. At $`d=3`$, $`I_3=2\pi/3`$ and $`K_3=(18\pi)^{1/3}`$. This proves both the inequality and its optimality on the specified class.

### Stationarity and differentiating the full quotient

The identities $`|f'|^{p-2}f'=-d^{p-1}rf`$ and $`df+rf'=d f^{q-1}`$ give the displayed Euler--Lagrange equation with multiplier $`d^p`$. Differentiation on the normalization tangent space yields exactly the stated Hessian with its stated factor.

Since $`p<2`$, differentiation at the zero of $`D\psi_0`$ needs justification. The second Taylor remainder for a nonzero vector $`a`$ is bounded by $`C_p|a|^{p-2}|b|^2t^2`$. Here $`|D\psi_0|^{p-2}=O(r^{2-q})`$, which is locally integrable against a smooth compactly supported variation in every stated dimension. The exceptional origin has measure zero. Dominated convergence justifies the second derivative. The final manuscript states this explicitly.

### Angular decomposition and high degrees

The polar Dirac identity has the correct sign:
```math
D=-i\Gamma(\partial_r-K/r).
```
The monogenic decomposition of homogeneous harmonic spinors gives the two eigenvalues $`\ell`$ and $`-\ell-d+2`$ of $`K`$, with only zero in degree zero. The real projection onto the line spanned by the constant spinor preserves harmonic degree, so the displayed Hessian is an orthogonal sum by degree.

The scalar ground-state identity is exact. For the nonnegative branch, $`w'/w-\kappa=-(d+2\kappa)z`$; for the negative branch it is $`(-2\kappa-a)(1-z)`$. Substitution into the weighted scalar operator gives the claimed squared constants without an unproved spectral assertion.

For every degree at least two the smaller constant is $`((d+2\ell+q-4)/d)^2`$, at least $`\nu^2`$, where $`m=p-1`$ and $`\nu=1/m=q-1`$. The matrix bounds $`M\ge mI`$, $`N\le\nu I`$ then give $`m\nu^2-\nu=0`$. This proves nonnegativity for all high angular modes, not just finitely many tested degrees.

### Degree-one blocks and Riccati identity

For the normalized real angular vectors $`a_j`$, the identity $`PKa_j=0`$ follows from skew-Hermiticity of $`\gamma_i\gamma_j`$ when $`i\ne j`$. The relation $`K^2+(d-2)K=(d-1)I`$ proves that the $`a_j,b_j=Ka_j/\sqrt{d-1}`$ are orthonormal. Each pair is invariant under $`K,M,N`$; the orthogonal complement has $`P=0`$ and is covered by the scalar estimate. This establishes the entire decomposition, rather than merely exhibiting some invariant pairs.

For the two-dimensional blocks put $`t=1-dz`$, $`k^2=d-1`$, $`S=tI-K_1`$. Dividing the proposed Riccati identity by $`A`$, the two diagonal entries reduce to
```math
t'+(a+qz)t+\nu t^2-k^2+\nu d^2z(1-z),
```
```math
t'+(a+qz)(t+d-2)+t^2+(\nu-2)k^2-(d-2)^2+d^2z(1-z).
```
The off-diagonal entry divided by $`k`$ is
```math
-(a+qz)+(1-\nu)t+d-2.
```
Each coefficient vanishes using $`a=d-q`$, $`q(d-1)=2d`$, and $`\nu=q-1`$. For example the first constant coefficient is $`1-q+\nu`$, and its linear coefficient is $`q-d^2+\nu d(d-2)`$, both identically zero. This verifies the matrix identity for every dimension analytically. Integration by parts then yields the claimed nonnegative factorization.

### Degree zero, approximation and scope

Real spin directions perpendicular to the constant spinor are covered by the scalar identity with $`\kappa=0`$. The remaining real component is the scalar Sobolev second variation, subject to the single normalization constraint. Independently, the stated Jacobi-weight calculation gives eigenvalues $`j(j+d-1)`$, and the first positive eigenvalue is $`d`$. The transformed quadratic form and its mean-zero constraint have the correct weights and coefficients.

Finite spherical-harmonic sums approximate smooth variations in the displayed quadratic forms. To remove the puncture, the logarithmic cutoff contributes $`O(1/|\log\varepsilon|)`$ at $`d=3`$, and still less for $`d>3`$, since the radial derivative error has weight $`r^{d-q-1}`$. Restoring the tangent constraint by a vanishing multiple of a fixed radial test direction is valid.

The result is a nonnegative constrained Hessian. It proves neither nonlinear local coercivity nor global minimality. The remaining target is the exact global $`C_d`$ for arbitrary spinors and all $`d\ge3`$. The submitted unsupported numerical-search anecdote was omitted; no numerical search is used as evidence.

### Verified references and current comparison

- [Frank--Loss, January 2022 primary text](https://arxiv.org/html/2201.03610v1), “Relation to Sobolev inequalities”, equation (8), defines the power-normalized norm problem. The published numbering differs.
- [Bieganowski--Mederski, primary text](https://arxiv.org/html/2610.15787v1), Theorem 4.1 and Section 7, provides the scalar competitor and explicitly distinguishes it from a determination of the exact global constants.
- [Talenti, original article](https://math.jhu.edu/~js/Math646/talenti.sobolev.pdf), Theorem and equations (1)--(3), printed p. 353, gives the scalar sharp inequality and optimizer for every $`1<p<d`$. [Publisher record](https://doi.org/10.1007/BF02418013) confirms volume, pages and year.
- [Wang--Zhang v2](https://arxiv.org/abs/2508.09047v2), Introduction and Theorem 1.5, printed p. 5, treats instability of the older conformal critical family. The norm quotient is numbered (1.10) in its PDF and (1.15) in the HTML. Its spinorial Yamabe stability theorem is a different quotient and does not give the present global constant.

Bounded searches on 3 November 2026 covered the exact critical Dirac norm constant, scalar Talenti spinors and recent stability results. No matching complete determination was found. Neither priority nor exhaustive absence of other work is certified.

### Second independent check

## AIM 911: independent second proof check

Reviewer lane: c. Date: 2026-11-03.

**Verdict: accept both results as partial results only.** I found no fatal mathematical gap in the restricted-class sharp inequality or the nonnegative second-variation theorem. In particular, the degree-one real orthogonal blocks, differentiation for `p<2`, harmonic approximation and origin cutoff pass this independent check. Neither result determines the unrestricted canonical constant `C_d`. No novelty claim is made or certified.

### Reviewed material and scope

Read the canonical `problems/911-the-sharp-constant-in-the-critical-dirac-norm-inequality.md`, both original sections `911_partial.tex` and `911_stability.tex` under `.cache/operators-batch/_sources/submission/report/sections/`, and the assembled `research/solutions/911-dirac-radial-bounds-stability/aim911.tex`. The assembly I read includes the explicit `p<2` differentiation explanation, while its mathematical formulas agree with the original sections.

Snapshot SHA-256:

- `911_partial.tex`: `e6c3db5a9efe12b2394c2e2aacadbd7458e6350c43fff9a8ded3755596c88e1a`.
- `911_stability.tex`: `0347b1ca3d18fbe5a2bf1aee0ec9ccbd29e197e162a7577ea9b17af14379a091`.
- Assembled `aim911.tex` when read: `c69681b365610c2f8676482a6d1a020120828f545dfb017eeb0c58012cdbbc77`. Citation clarification may subsequently change this assembled-file hash.

The exact canonical target is the infimum over the entire distributional graph domain `psi in L^q`, `D psi in L^p`, with no angular or two-channel restriction. The first theorem proves equality with `K_d` on its explicitly stated class of real profiles and constant spinors satisfying the real Clifford orthogonality conditions. The second proves stationarity and a nonnegative Hessian in every smooth compactly supported real tangent direction at the scalar Talenti spinor. It supplies no global lower bound `C_d >= K_d`, no complete kernel classification, and no nonlinear or quantitative stability inequality. Nonnegativity of a Hessian alone also does not establish nonlinear local minimality.

### Primary references and one citation-number clarification

- [Talenti, *Best constant in Sobolev inequality*, primary article scan](https://math.jhu.edu/~js/Math646/talenti.sobolev.pdf), the unnumbered main Theorem, printed p. 353, equations (1)--(3), supplies the sharp scalar inequality and its optimizer for `1<p<d`, `q=dp/(d-p)`. Substituting `p=2d/(d+1)` gives exactly the exponent and radial profile used here.
- [Bieganowski--Mederski, arXiv:2610.15787v1 PDF](https://arxiv.org/pdf/2610.15787), Theorem 4.1, printed pp. 7--8, equations (4.8)--(4.13), already computes this constant-direction Talenti competitor and its quotient. The submission correctly attributes this known competitor. That theorem supplies an upper bound, not a determination of the global infimum.
- [Wang--Zhang, arXiv:2508.09047v2 PDF](https://arxiv.org/pdf/2508.09047v2), Introduction, printed p. 5, Theorem 1.5, concerns the conformal Killing-spinor critical family, which is different from the scalar Talenti critical point treated here. The following paragraph leaves the global norm-quotient constant undetermined. The spinorial Yamabe stability theorem is a different variational statement. **Numbering detail:** the arXiv HTML version labels the norm quotient (1.15), but the actual v2 PDF labels it **(1.10)** on p. 5. Cite both conventions explicitly, or use Theorem 1.5 and the Introduction's norm quotient, to avoid a broken locator. This is a citation issue, not a proof defect.
- [Frank--Loss, January 2022 primary PDF](https://arxiv.org/pdf/2201.03610v1), printed pp. 6--7, equation (8), states the full norm-constant question; the source uses the power normalization `S_d^s=C_d^p`.

I did not audit the full proofs of those papers or make a priority determination. The mathematical checks below are independent of the root reviewer's conclusions and of numerical experiments.

### Restricted two-channel theorem

The identities `Gamma^2=I` and `sum gamma_j partial_j(g Gamma)=g'+(d-1)g/r` are correct. The stated real orthogonality eliminates both cross terms: `Re<u,Gamma v>=0` also gives `Re<Gamma u,v>=0`. Since `Gamma` is unitary, the pointwise norm identities follow. Taking `v=iu` is legitimate because every `<u,gamma_j u>` is real. Real-valued profiles and real, rather than complex, orthogonality are essential to this argument.

For the second channel, differentiating `h(r)=r^(1-d)g(1/r)` gives

`h'(r)=-r^(-d-1) (Lg)(1/r)`.

Changing variables `s=1/r`, the `L^q` density has exponent `(d-1)q-d-1=d-1`, and the derivative density has exponent `(d+1)p-d-1=d-1`. Thus both norm equalities in the Kelvin step are exact. No incorrect use of the ordinary Kelvin transform for a different Sobolev exponent is involved.

The mixed-norm inequalities have the correct directions. The first is Minkowski in `L^(q/2)`, since `q>=2`. For the last, Minkowski in the finite-dimensional space `ell^(2/p)` gives

`(||a||_p^2+||b||_p^2)^(p/2) <= integral (|a|^2+|b|^2)^(p/2)`

because `p<=2`; taking the `p`th root yields the claimed inequality. Thus no two-channel mixture in this class beats the scalar bound.

The graph-domain approximation is valid. For the cutoffs, `1/p=1/q+1/d`, `||(gamma dot grad chi)psi||_p <= ||grad chi||_d ||psi||_(L^q(support grad chi))`, and dilated cutoffs have uniformly bounded gradient `L^d` norm. The final factor vanishes at both zero and infinity; the main cutoff terms converge by integrability. On a fixed annulus, the real projections of `iD psi` onto the pointwise orthogonal unit vectors `Gamma u` and `v` recover `f'` and `Lg` distributionally. Hence these are locally `L^p`. Also `g/r` is locally `L^p`, so `g'=Lg-(d-1)g/r` is locally `L^p`, and both profiles are one-dimensional `W^(1,p)` there. Real profile mollification then converges in the indicated graph norm and preserves the class. Possible singular behavior at the origin is handled by the cutoff estimate, not silently omitted.

Finally `q=dp/(d-p)=p/(p-1)`, and `f_0=(1+r^q)^(-(d-1)/2)` is the appropriate scalar optimizer. The beta integrals have arguments `(d-1)/2` and `(d+1)/2` in opposite order for the function and derivative integrals. They give `integral f_0^q=I_d`, `integral |grad f_0|^p=d^p I_d`, and quotient `d I_d^(1/d)`. In dimension three this is `(18pi)^(1/3)`. The restricted-class sharpness statement follows, while the full canonical consequence is only the already known upper bound `C_d<=K_d`.

### Stationarity and rigorous second differentiation when `p<2`

The pointwise identities

`|f'|^(p-2)f'=-d^(p-1) r f`,

`|D psi_0|^(p-2)D psi_0=i d^(p-1)(gamma dot x) f`

are correct. Applying `D` produces `d^(p-1)(d f+r f')xi=d^p f^(q-1)xi`. The weighted field is regular at the origin; no delta term is introduced there. Integration by parts against a compactly supported variation therefore proves stationarity. The scalar profile need not be globally `C^infinity` for this calculation.

The Hessian formula is legitimate despite the isolated zero of `D psi_0`. Here is an explicit justification for the added differentiation paragraph. For `1<p<2`, `a != 0`, and a vector increment `v`,

`| |a+v|^p-|a|^p-p|a|^(p-2) Re<a,v> | <= C_p |a|^(p-2)|v|^2`.

If `|v|<=|a|/2`, integrate the ordinary vector Hessian along the segment; its norm is at most a constant times `|a|^(p-2)`. In the complementary case, use `|a|<=2|v|` and `p<2` to bound each term by the same right side. Thus this domination holds uniformly even when `a+v` crosses zero. The analogous bound for the difference of first derivatives also follows by the same split, so one obtains the actual second derivative, not merely a formal pointwise Hessian or an unjustified inference from pointwise differentiability.

Set `a=D psi_0(x)`, `v=t D eta(x)`. Since `eta` is smooth and compactly supported, `D eta` is bounded, and

`|D psi_0|^(p-2)=d^(p-2)r^(2-q)(1+r^q)`.

Near zero the candidate dominating density has radial integral bounded by a constant times `integral_0^1 r^(d+1-q) dr`, which is finite for every `d>=3` (in dimension three the exponent is `1`). Away from zero on the support it is bounded. Dominated convergence therefore proves the stated numerator Hessian. The denominator poses no issue because `f>0` on the compact support. Under the displayed tangent condition both first variations of the two norms vanish, and differentiation of the quotient gives exactly `p (integral f^q)^(-p/q) H(eta)`.

### Angular operator and cylinder form

The rotation fields and constant Clifford bivectors commute with each other in each summand defining `K`; each factor is skew-adjoint, so their product is self-adjoint on each finite harmonic space. Rotations preserve spherical harmonic degree. The polar formula has the stated sign. Decomposing a homogeneous harmonic spinor polynomial into a monogenic part and `(gamma dot x)Q` gives eigenvalues `ell` and `-ell-d+2`; the identity for the Clifford derivative of `(gamma dot x)Q` has coefficient `d+2ell-2`. Degree zero is separately `K=0`. These statements require no completeness claim about an unconstructed eigenspinor basis on a curved manifold.

Because multiplication by `-i Gamma` is unitary in the real spinor inner product, the numerator Hessian is represented by `M=I+(p-2)P` acting on `h'-Kh`. Its eigenvalues are `m=p-1` and `1`. The denominator matrix `N=I+(q-2)P` has eigenvalues `nu=q-1` and `1`; `m nu=1`, so `N=M^(-1)`. Direct radial substitution gives precisely the displayed weights `A` and `C`. The projection onto the fixed real line `R xi` preserves harmonic degree, ensuring orthogonality of different degrees in the quadratic form.

For the scalar ground-state identities, writing `t=(log w_kappa)'` gives, respectively,

`t-kappa=-(d+2kappa)z` and `t-kappa=(-2kappa-a)(1-z)`.

Substituting `z'=qz(1-z)`, `A'/A=a+qz` into the scalar differential expression gives respectively `(d+2kappa)^2 z(1-z)` and `(-2kappa-a)^2 z(1-z)`. This verifies both constants and the ground-state identity by integration by parts. For `ell>=2`, the negative eigenvalue gives the smaller constant; at `ell=2` it equals `nu^2`. The bounds `M>=mI` and `N<=nu I` are sufficient even though `M` need not commute with `K`. The resulting lower bound is nonnegative.

### Degree-one blocks: no missing coupled directions

This was checked explicitly over the **real** angular Hilbert space. The vectors `a_j` are orthonormal. The identity

`K a_j = a_j - sqrt(d/|S^(d-1)|) Gamma gamma_j xi`

gives `P K a_j=0` pointwise, since the off-diagonal Clifford products are skew-Hermitian and their expectations have zero real part. Consequently every `<a_i,K a_j>` vanishes. The minimal polynomial on degree one is `K^2+(d-2)K=(d-1)I`. With `k=sqrt(d-1)` and `b_j=K a_j/k`, self-adjointness gives

`<b_i,b_j> = (1/(d-1)) <a_i,K^2 a_j> = delta_ij`,

and `<a_i,b_j>=0`. Thus all `2d` displayed vectors are genuinely orthonormal; no assertion about vanishing complex Hermitian inner products is needed.

Also `K a_j=k b_j`, `K b_j=k a_j-(d-2)b_j`, `P a_j=a_j`, and `P b_j=0`. Each real two-dimensional block is invariant under both `K` and `P`, with exactly the three printed matrices. Their mutually orthogonal complement is invariant under these self-adjoint operators. The range of `P` on the entire degree-one space is precisely `span_R{a_j}`, so `P=0` on that complement. This verifies that the blocks and the complement exhaust all degree-one spinor variations, including the remaining imaginary spin directions. On the complement the smaller scalar constant `((d+q-2)/d)^2` is strictly larger than one, as used.

The Riccati identity can be verified especially transparently without a computer algebra system. Put `t=1-dz`, `k^2=d-1`, `S=tI-K_1`, `N_1=diag(nu,1)`, `nu=q-1`, `a=d-q`, and divide its residual by `A`. A direct entrywise expansion gives exactly

`z [q(d-1)-2d] [[d-1,k],[k,1]]`.

Thus every entry vanishes by the required exponent relation. Moreover `R=K_1+N_1 S` has the stated upper triangular entries because `(1-nu)k=-2/k`. Since `S=M_1(R-K_1)` is symmetric, expansion of the proposed square and integration by parts give exactly the displayed factorization, with no leftover antisymmetric cross term or boundary term for compact radial support. The two printed profiles also solve `h'=Rh`; they provide consistency checks, not the basis of the nonnegativity proof.

### Degree zero and its normalization constraint

Real spin directions orthogonal to `xi` use the scalar ground-state identity with `kappa=0`, `w_0=f` and constant one. In the remaining real direction, setting `h=f y(z)` yields `A f^2=w=z^(c-1)(1-z)^c` and `C f^2 ds=(d^2/q)w dz`. The tangent condition becomes `integral w y=0`, and the quadratic form is exactly

`m q [integral z(1-z)w |y'|^2 - d integral w |y|^2]`.

The Jacobi operator is symmetric with the stated coefficients. On degree `j` its leading coefficient is `j(j+d-1)`. Orthogonal polynomials therefore diagonalize it. For the initially compactly supported `y` inside `(0,1)`, integration by parts gives `integral z(1-z)w y' P_j' = j(j+d-1)<y,P_j>`. Applying Bessel to the normalized derivative polynomials, then completeness in weighted `L^2`, proves the energy bound. One does not need to assume that polynomials are already dense in the energy norm. Mean zero eliminates the constant polynomial and the first remaining eigenvalue is `d`. The stated equality direction `y proportional to c-dz` is correct for this scalar radial component; it is not asserted to classify the kernel of the full spinor Hessian.

### Harmonic and origin-cutoff limits in the quadratic form

For a variation supported on a fixed annulus, componentwise spherical-harmonic projections commute with radial differentiation, with `K`, and with the constant real-spin projection `P`. Smoothness gives convergence in radial derivative and angular `K` graph norm. Both radial weights are bounded on the fixed annulus, so these convergences imply convergence of all terms in the displayed quadratic form. The projections retain degree zero and therefore preserve the tangent constraint. This justifies summing the finite-degree inequalities; the negative potential term cannot produce an unaccounted loss in this limit.

For a general smooth compactly supported variation, let the logarithmic radial cutoff change on `(epsilon^2,epsilon)`, with `|grad chi|<=C/(r|log epsilon|)`. The extra weighted derivative energy is bounded by

`C/|log epsilon|^2 * integral_(epsilon^2)^epsilon r^(d-q-1) dr`.

For `d=3`, `d-q=0` and this is `O(1/|log epsilon|)`. For `d>3` it is `O(epsilon^(d-q)/|log epsilon|^2)`. Both tend to zero. The discarded original derivative energy tends to zero by its integrability, and cross terms tend to zero by weighted Cauchy--Schwarz. The discarded potential term also vanishes. Therefore `chi eta` tends to `eta` in the form norm controlled by

`integral |D psi_0|^(p-2)|D eta|^2 + integral f^(q-2)|eta|^2`.

To restore tangency choose the fixed correction spinor smooth, radial and supported in an annulus, with nonzero normalization integral. The required coefficient tends to zero because the removed normalization integral tends to zero. This correction tends to zero in the same form norm and does not reintroduce support at zero. Continuity of the quadratic form in that norm then passes the inequality to the original variation. Thus the borderline origin and the normalization adjustment are both accounted for.

### Final assessment

Both original results survive the second proof check. The assembled differentiation clarification is mathematically sound; the harmonic and cutoff sentences are concise but can be expanded exactly as above without adding a new hypothesis. The only concrete editorial issue found is the Wang--Zhang HTML/PDF equation-number mismatch, which has been sent to the parent reviewer.

Keep the status **PARTIAL**. The global inequality for arbitrary spinors and the exact unrestricted `C_d` remain unproved here. The known scalar competitor must retain its BM2026 attribution. Neither the partial radial theorem nor the Hessian calculation should be described as new without a separate literature assessment.
