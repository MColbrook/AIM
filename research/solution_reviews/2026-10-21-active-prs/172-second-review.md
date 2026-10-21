# AIM541 / PR #172 independent audit of the linear uniform interval

**Review date:** 21 October 2026
**Submission:** [PR #172](https://github.com/MColbrook/AIM/pull/172)
**Pinned head:** 71ed609ac0d213f399348e2bf6669767b8444ca0
**Reviewer role:** Independent OpenAI Codex mathematical second review, focused on Sections 2–5 and separate from the submission's author context. This is an AI review, not human peer review or formal verification.

**Conclusion:** I found no concrete gap in the linear nonconvergence argument on this second pass. The uniform analytic interval is supported by the displayed operator gaps and analytic-energy mechanism; it is not inferred from a fixed-mesh ODE or the initial optical rate. The inverse operators are nonlocal, but the argument supplies uniform conditioning and localization before using them.

This audit addresses the degree-one result, especially the common interval, row kernels, coercivity, and derivative loss. It does not reassess the cubic proof or provide a separate broad literature search.

## Materials and locators

I read Sections 2–5 of the complete [pinned manuscript source](https://github.com/MColbrook/AIM/blob/71ed609ac0d213f399348e2bf6669767b8444ca0/research/solutions/541-linear-failure-cubic-convergence/paper/manuscript.tex). Source-line locators below refer to that file; equation labels provide additional stable locators. No submitted code was executed.

The target method is the position-gradient formulation with exact fixed-reference integrals and raw geometric normals, as in Gao, Li, and Tang's [author manuscript](https://libuyang.com/NM-15.pdf). The present audit checks the proposed argument for this original system.

## Full system, graph, and inverse conditioning

Section 2 retains the exact mass, stiffness, and weak-normal saddle system with discontinuous full geometric normals. The full-mesh normal-column argument precedes cyclic reduction. The operator $`TN_{\rm ref}`$ has a positive weighted scalar-mass Hermitian part: all current normals retain a positive component in the smooth reference normal, while replacing its varying nodal values on a face costs $`O(\delta)`$. Thus $`T`$ has full row rank and $`TM^{-1}T^*`$ is uniformly invertible in the normalized mass norm on the geometric neighborhood.

Local existence and uniqueness are first justified for every fixed mesh. Symmetry then gives the cyclic representation. This order avoids importing a uniqueness assumption from the reduced system.

Section 3, source lines 425–435, gives an actual uniform inverse argument. For a localized order-zero matrix $`A`$ with a uniform inverse bound, conjugation by $`\exp(\gamma\mathrm{dist}(i,j))`$ changes $`A`$ by $`O(\gamma)`$ in operator norm. Choosing $`\gamma`$ from the fixed inverse gap permits a Neumann argument. One-row inputs then give exponential inverse-kernel decay at a rate independent of the mesh. The exact inverse coefficient-difference identity propagates higher coefficient estimates. Nonlocal inverses are therefore not treated as banded matrices; their periodized tails and distance moments are retained.

State and dual scaling are distinguished correctly. Physical primal coordinates are $`(q_b,\delta q_c)`$, so their dual force is $`(F_b,\delta F_o)`$. Source lines 636–645 apply this dual scaling before estimating the alternating multiplier.

The normal graph

```math
E=C_{\rm all}-R_NTC_{\rm all}
```


satisfies $`TE=0`$, $`L_{\rm ref}E=I`$, and $`E'[h]=-R_NT'[h]E`$ exactly. Its mixed type has mean-to-scaled-optical order one and scaled-optical-to-mean $`\delta^2`$ times order one. This agrees with the physical projection: coherent mean/optical cross kernels vanish at zero row phase, and the actual freezing remainder has a further $`\delta`$. Conjugation by $`\mathrm{diag}(d_\delta,\delta^{-1})`$ turns those zeros into a bounded mixed operator. Neither the graph nor its inverse loses an unaccounted power of $`\delta`$.

## Moments, coercivity, and Schur inverses

The row-moment calculus at source lines 396–423 includes the shifts of varying output coefficients. For example, multiplying a class-two operator by a class-zero coefficient requires expanding the right coefficient: its first variation uses the class-two first moment $`O(\delta)`$, while its second remainder contributes $`s^2=16\delta^2`$. Class two is therefore preserved in both orders. Two class-one factors give class two by the same argument. The adjoint identity has the correct sign for the forward difference and retains its coefficient-difference remainder. A scalar Fourier-symbol zero alone would not have been sufficient for these variable kernels.

The rectangle cancellations match the P1 tests. On a coherently frozen affine rectangle, the alternating species function is affine azimuthally, has integral zero, and has square integral equal to one third of the area. The macro row shape is affine in the independent meridional coordinate. Hence the whole-rectangle optical/macro integral vanishes regardless of the diagonal. The connection table separately uses the row-supported optical test and does not replace it by the bilinear product. Neighboring row assembly supplies the additional patch difference needed in the optical-output/macro-input entry. These cancellations produce second macro order while retaining only one derivative loss on the mixed scale.

For the tangent force form, the alternating multiplier obeys

```math
\|\lambda\|_{H^3}=O(\eta+\delta^2).
```


Its curved moment table bounds its form by $`C\|\lambda\|_{H^3}`$ times the mixed $`H^1`$ norm squared. The mean multiplier contributes the lower-order bound $`C\|k_b\|_\infty\|v\|_{L^2}\|v\|_{H^1}`$. Choosing $`\beta,\eta,\delta`$ in that order therefore gives a positive tangent form $`B`$. Its fast block $`H`$ consequently has a uniform gap, so the localized-inverse argument applies to $`H`$ with an established inverse bound.

The stronger principal-block gap in the lemma labelled global-gap, source lines 737–768, is also reconstructible. In a frozen reference product strip, the exact P1 gradient controls the independent macro gradient and optical coordinate. A zero gradient forces the optical coordinate and then the macro gradient to vanish. At zero phase this is understood after removing the macro phase difference. Compactness of phase and of the nondegenerate reference shapes gives a uniform gap. Small geometric and alternating-form perturbations preserve it.

A fixed-length row partition transfers this gap to variable kernels with errors $`C/L+CL\delta`$. Choosing $`L`$ first and $`\delta`$ second gives the global gap. This is a global operator estimate, rather than an inverse of a frozen symbol used as though it were the actual inverse.

Testing the principal block on $`(\xi,-H^{-1}C_s\xi)`$ sets its lower row to zero and gives the coercive Schur coefficient

```math
a_0=A-C_fH^{-1}C_s.
```


Thus $`a_0^{-1}`$ is also a uniformly localized global inverse.

## Independent algebra checks

### Relative velocity

I derived the relative-velocity equation directly from the original saddle system. With $`W=V-\varepsilon\Omega X`$, equivariance gives

```math
(K-H_\kappa)\Omega X=-\Omega MV.
```


After projecting the differentiated force equation, the two explicit rotation terms cancel. Differentiating $`QW=W`$ gives the remaining normal component $`Q_tW`$. The result is exactly the equation labelled relative-equation:

```math
W_t=-QM^{-1}(K-H_\kappa)W+Q_tW.
```


Writing $`W=E\mathbf a`$ and using $`E'[V]=-R_NT'[V]E`$ yields the displayed source containing $`(R_N-R_M)T'[V]W`$, with the stated sign. The moving weak constraint is retained.

### Ordered mass elimination

For

```math
G=\begin{pmatrix}G_{ss}&\delta^2M_{sf}\\\delta^2M_{fs}&\delta^2M_{ff}\end{pmatrix},
\qquad C=H^{-1}B_{fs},\qquad z=\omega+Cu,
```


subtracting $`M_{sf}M_{ff}^{-1}`$ times the fast mass equation gives

```math
\overline M u_t+Su+Lz=\overline M\mathcal N_u.
```


Substituting this into the $`z`$ equation gives precisely

```math
z_t+\delta^{-2}A_fz-N\overline M^{-1}(Su+Lz)
=\mathcal N_\omega+C\mathcal N_u+C_tu.
```


No independent source receives an extra $`\delta^{-2}`$.

### Connection and high-mass square

The weak-connection identity remains exact for noncommuting operators. With $`\Gamma=a_0^{-1}r_0`$, expansion of $`(D+\Gamma)^*a_0(D+\Gamma)`$, followed by the two displayed lower terms, gives

```math
D^*a_0D+D^*r_0+l_0D+v_0.
```


This places a strong second graph derivative inside the connection instead of estimating it as an independent low coefficient.

The high-energy square is also exact:

```math
\delta^{-2}\langle\mathbf a_H,G\mathbf a_H\rangle
=\delta^{-2}\langle u_H,\overline M u_H\rangle
+\langle z_H+Nu_H,M_{ff}(z_H+Nu_H)\rangle.
```


It gives the extra $`N`$ application to a macro force in the high metric. The estimates retain that application; the macro force is not paired as though this cross term vanished.

## Same-radius analytic comparison

The lemma labelled same-radius, source lines 941–1016, can be reconstructed without reducing the radius. For the forward difference, the exact modular identity

```math
\lambda_{k+l}-\lambda_k=e^{iks}\lambda_l
```


holds, including aliasing. Conjugating a coefficient by $`e^{\zeta D}`$ therefore multiplies its $`(l,k)`$ entry by $`e^{\zeta e^{iks}\lambda_l}`$. The circle norm produces precisely $`W_p(\rho|\lambda_l|)`$; the input phase rotates the circle and does not change its norm.

The coefficient norm with an $`H^r`$ row weight and an $`H^p`$ circle weight is an algebra for $`r,p>1/2`$. Its product uses $`A_{l-m}(k+m)B_m(k)`$, so the supremum over input frequency and weighted convolution give the required order of bounds.

For

```math
\mathcal H(\zeta)=e^{\zeta\nabla}e^{-\zeta D},
```


the ordered ODEs

```math
\mathcal H'=\mathcal H\Gamma_\zeta,
\qquad(\mathcal H^{-1})'=-\Gamma_\zeta\mathcal H^{-1}
```


give uniform algebra bounds from the transported connection norm. The identity

```math
[D,\mathcal H]=\mathcal H\Gamma_\zeta-\Gamma\mathcal H
```


gains one coefficient row derivative: its $`(l,k)`$ entry is $`e^{iks}\lambda_l\mathcal H_l(k)`$. This supplies row $`H^3`$ from the connection's $`H^2`$ without another radius loss.

Circle Parseval then compares ordinary and covariant analytic jets with an $`H^3`$ base at the same radius. The finite offset comparison through three differentiates $`\Gamma`$ only twice; its highest $`L^2`$ coefficient acts on an $`H^1`$ vector, which is valid in the one-dimensional uniform discrete algebra. At $`p+1/2`$, the product and interaction-ODE estimates are tame with one high coefficient factor. Squaring the comparison adds high geometry energy times a low velocity bound, rather than a product of two uncontrolled high energies.

## Energy and derivative loss

The low/high split controls the third-order-looking $`NSu`$ term. In the low band, its extra first derivative is bounded by $`d_0/\delta`$. Thus $`Lz`$ and $`NSu`$ pair jointly as

```math
C(d_0/\delta+1)\|u\|_{H^2}\|z\|_0.
```


Choosing $`d_0`$, then $`\delta`$, small absorbs this into macro $`H^2`$ dissipation and $`\delta^{-2}\|z\|_0^2`$. The high band uses the original physical tangent-form coercivity and the equivalence of $`\delta^{-1}\|u_H\|_0`$ with its $`H^1`$ norm. Combining the macro gradient and optical energy also controls $`z_H=\omega_H+Cu_H`$. The proof does not request a low-band third derivative with a mesh-independent constant.

The explicit stiff commutator is $`\delta^{-2}[\nabla^m,A_f]z`$. The finite offset levels $`\ell=0,1,2`$ are triangular: finite reference coefficient derivatives multiply lower offset jets. Successively smaller fixed weights $`\vartheta_\ell`$ absorb these terms into lower fast dissipations. Positive analytic derivatives carry factors $`\rho`$ or $`\eta`$, making their weighted convolutions small in those same dissipations.

Cutoff commutators have the additional $`\delta`$ because the cutoff varies on the phase scale. The stiff cutoff pairing is bounded by a small part of the global fast dissipation plus a multiple of the energy; it leaves no $`\delta^{-1}`$ energy coefficient.

The nonstiff derivative counts match the geometry spaces. At top offset $`\ell=2`$, the macro force uses $`D^{j+4}y,D^{j+3}w`$, the same $`\mathcal X_0`$ geometry level. The additional $`N`$ application can raise this to $`D^{j+5}y,D^{j+4}w`$, exactly one $`\mathcal X_1`$ factor, paired with the fast energy root. The formulas for $`C_t`$ and $`\Gamma_t`$ use the differentiated multiplier identity and avoid an uncontrolled $`\kappa_t`$. Low metric derivatives require $`V_b`$ in $`W^{2,\infty}`$ and $`V_c`$ in $`W^{1,\infty}`$, available from $`\mathcal A_0`$ by the one-dimensional embeddings.

### Half-weight summation

The half-weight inequality at source lines 1239–1269 is arithmetically correct. With $`j=k+m-1`$, the exact residual weight is

```math
\frac m\rho\frac{(k+m)^p}{(k+1)^p(m+1)^p}.
```


The estimate $`m\leq\sqrt{j+1}\sqrt{m+1}`$ divides the single lost derivative between the energy-root and high-source factors. The residual polynomial kernels are summable for $`p=4`$. A source linear in $`\mathcal X_1`$ or $`\mathcal A_1`$ consequently contributes half-weight energy, rather than the square of an entire extra spatial derivative. The radius derivative contributes exactly $`2\rho'/\rho`$ times the extra-$`j`$ energy.

The geometry equation uses the same one-high-factor graph estimate. The combined energy inequality therefore has fixed mesh-independent coefficients on the small analytic ball. A decreasing radius with speed above its polynomial coefficient cancels the extra-$`j`$ terms. The independently large geometry weight keeps $`E_x`$ strictly inside the same small ball. This closes the bootstrap; it does not assume a solution already known to remain smooth.

## Continuation and the fixed-time effect

The analytic energy starts from $`E_x(0)=0`$ and uniformly bounded $`E_v(0)`$, including the scaled optical initial layer. It gives a fixed positive lower radius and fixed time $`T_0`$. For each fixed mesh, an earlier ODE endpoint can be crossed: physical positions have limits, while scaled element cross products and the full weak-normal block retain strict gaps. The continuation uses the full-system gap established before cyclic reduction.

A positive lower analytic radius supplies an ordinary extra row derivative, making $`\mathbf e_t`$ uniformly bounded in $`\mathcal X_0`$. The macro equation bounds $`u_t`$ in $`H^1`$ without differentiating $`z`$ in time. The physical mean relative velocity contains only a $`\delta^2`$ times first-order fast correction. Its time modulus therefore survives the potentially fast optical layer.

The label equation retains its spatial and moving-frame terms. Together with its nonzero initial rate, this supplies a fixed-time label effect, and the rotation-energy argument converts the resulting fixed gradient effect into a positive $`L^2`$ map-error bound. The argument has the common interval and time control needed beyond an initial-velocity calculation.

## Assessment and limits

No concrete mathematical gap was identified in this second pass. The compressed kernel and energy estimates have consistent conditioning, orders, and analytic closure, with the reconstruction given above. This is a natural-language AI mathematical audit, not a machine-checked proof or human peer review.
