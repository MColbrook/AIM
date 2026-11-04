# AIM 897: mathematical review

**Final status:** Solved. **Reviewed:** 3 November 2026, by Codex (AI), separately from the author.

[Canonical problem](../../../problems/897-pedersen-s-sharp-fractional-power-commutator-inequality.md) · [PDF manuscript](../../solutions/897-fractional-power-intertwining/aim897.pdf) · [source and reproduction](../../solutions/897-fractional-power-intertwining/README.md).

The audit compares the complete supplied argument with the current target at revision 5d7e26e8444eb98de91988454564e45e011107c4. The original archive's earlier review assertions were not accepted as evidence.

## AIM 897 independent proof review

**Verdict: PASS FULL TARGET.** The submitted proof establishes the stated constant-one operator-norm inequality for every finite dimension, every pair of positive semidefinite complex matrices, every matrix $`X`$, and every exponent $`0<r<1`$. I found no mathematical gap in the core proof or the additional claims in the supplied operator-monotone supplement. This is a verdict on the supplied argument, not a claim that it has already appeared in the literature.

Review date: 3 November 2026 UTC. Input: the full original `report/sections/897.tex`, including `897_operator_monotone.tex`, and the current canonical problem. Exact input hashes are in `verdicts.json`. Line locators below refer to those original TeX files.

### Exact target and scope

The target norm is the operator norm, not the Hilbert–Schmidt norm or an arbitrary unitarily invariant norm. The proof neither bounds the dimension nor restricts $`X`$ to be self-adjoint, unitary, invertible, or a contraction without accounting for normalization. Singular $`A,B`$, zero original commutators, and $`X=0`$ are covered. Its scalar equality case proves optimality of one uniformly in dimension and exponent.

### The extremal vector estimate

The novel step is the lemma at lines 23–75. Put $`H=[M,K]`$, where $`M=M^*\ge m_0I`$ and $`K^*=-K`$, and write $`h=\|H\|>0`$, $`k=\|K\|>0`$. Then $`H=H^*`$. Replacing $`K`$ by its negative if necessary makes $`h`$ an eigenvalue. If $`Hw=hw`$, $`\|w\|=1`$, and $`P=ww^*`$, the inequality

```math
H\ge h(2P-I)
```

is correct: $`w^\perp`$ reduces $`H`$, and $`H|_{w^\perp}\ge-hI`$. In particular, the order direction in this decisive step is correct even if the extremal eigenvalue has multiplicity greater than one.

For $`L=-iK`$, $`U_t=e^{tK}=e^{itL}`$, one has $`\sigma(L)\subset[-k,k]`$. On the interval $`|t|\le\pi/(4k)`$, scalar monotonicity of cosine on $`[0,\pi/4]`$ gives

```math
\mathop{\mathrm{Re}}\langle w,U_tw\rangle
=\langle w,\cos(tL)w\rangle\ge\cos(k|t|)>0.
```

Consequently

```math
\langle U_tw,HU_tw\rangle
\ge h(2|\langle w,U_tw\rangle|^2-1)
\ge h\cos(2kt).
```

This estimate uses the operator norm of $`K`$; there is no unjustified estimate on individual matrix entries. If $`F(t)=\langle U_tw,MU_tw\rangle`$, direct differentiation gives $`F'(t)=\langle U_tw,[M,K]U_tw\rangle`$, with the sign used in the submission. Integrating from $`-\pi/(4k)`$ to zero and using $`F(t)\ge m_0`$ yields exactly

```math
\langle w,Mw\rangle\ge m_0+\frac{h}{2k}.
```

There is no assumption that $`w`$ is an eigenvector of $`M`$, and none is needed.

### From the lemma to the sharp square root bound

At lines 77–98, the identity $`[M^2,K]=MH+HM`$ and $`Hw=hw`$ give

```math
\|[M^2,K]\|\ge |\langle w,(MH+HM)w\rangle|
=2h\langle w,Mw\rangle
\ge2m_0h+h^2/k.
```

Solving this scalar quadratic gives (897.4), with exactly the displayed coefficient. The $`h=0`$ case is explicitly separated. Changing the sign of $`K`$ has no effect on any norm in this argument.

The block reduction at lines 112–127 is also exact. For $`P_A=\sqrt{A+sI}`$, $`P_B=\sqrt{B+sI}`$,

```math
M=\mathop{\mathrm{diag}}(P_A,P_B),\qquad
K=\begin{pmatrix}0&X\\-X^*&0\end{pmatrix},
```

one obtains $`[M,K]=\left(\begin{smallmatrix}0&Y\\Y^*&0\end{smallmatrix}\right)`$ with $`Y=P_AX-XP_B`$. Its norm is $`\|Y\|`$. The identical construction for $`M^2`$ has upper right block (AX-XB), because the two (sX) terms cancel. Also $`\|K\|=\|X\|`$ and $`M\ge\sqrt{s}I`$. Thus (897.5) follows with $`\delta=\|AX-XB\|/\|X\|`$, including $`s=0`$ and $`\delta=0`$. This proves the full square-root case, not only the special commutator-size range in Loring–Vides.

### Integration and all exponents

For $`1/2<r<1`$, the integral defining $`C_r^{-1}`$ converges: the two endpoint majorants are $`s^{r-3/2}`$ at zero and $`\tfrac12s^{r-2}`$ at infinity. Substitution $`s=tu`$ gives (897.8), including the factor $`t^r`$. The displayed beta-function value is correct: integrating first in $`s`$ after the $`u\in[0,1]`$ representation gives $`C_r^{-1}=B(r-1/2,1-r)/(2r)`$.

The operator-valued integrals at lines 166–180 converge in norm by the displayed endpoint bounds. The subtraction of the scalar $`\sqrt{s}I`$ terms precedes integration, so no divergent integral is being canceled after the fact. Applying (897.5) under the positive weight gives $`k\delta^r`$ exactly. If $`\delta=0`$, the bound on every shifted commutator is zero and the integral is zero.

The composition argument (lines 198–211) preserves the homogeneous factors: the exponent on $`\|X\|`$ becomes $`1-\alpha\beta`$. Every $`0<r\le1/2`$ can be written $`r=\alpha2^{-j}`$ with (\alpha\in(1/2,1]). The endpoint (\alpha=1) is an equality, so it does not require an unproved limiting case of the integral formula. The case (X=0) is separately included. The scalar triple (A=1,B=0,X=1) attains the bound for every (r).

### Bounded operators and other ancillary claims

The unital $`C^*`$-algebra extension at lines 228–239 correctly removes norm attainment by a Hilbert-space vector. Choose the sign of $`H`$ so $`h\in\sigma(H)`$, and extend evaluation at that spectral point from $`C^*(H,I)`$ to a state $`\varphi`$. Since $`0\le hI-H\le2hI`$, one has $`\varphi((hI-H)^2)=0`$. In the GNS representation its cyclic unit vector is therefore an eigenvector of the represented $`H`$. The represented $`K`$ has norm at most the original $`k`$, which suffices for the same cosine bound with $`k`$. Finally $`\varphi(MH+HM)=2h\varphi(M)`$. Neither faithfulness nor norm attainment for $`K`$ is required. Matrix amplification and continuous functional calculus then carry the rest of the argument over. This covers bounded operators on arbitrary Hilbert spaces; it makes no claim about unbounded $`A,B`$.

The positive spectral-floor refinement (897.10) follows by using $`\sqrt{a+s}`$ in the quadratic bound. Subtracting two copies of the convergent integral representation gives the exact scalar increment. Composition preserves this increment because $`A^\alpha,B^\alpha\ge a^\alpha I`$ and the outer scalar function is increasing. For $`a>0`$, $`(A^r-I)/r\to\log A`$ in norm on the bounded spectrum, so dividing by $`r`$ and taking $`r\downarrow0`$ proves (897.11). Scalar choices $`A=a+\delta,B=a,X=1`$ give the asserted sharpness.

The real-matrix reduction at lines 296–319 is valid. Diagonal phase changes preserve both real Schur multipliers and all three norms. Entrywise real part cannot increase these operator norms; the nonnegative real singular-vector witness preserves the numerator exactly. This observation is independent of the main proof and is not used to replace the complex target by an unproved real restriction.

### Operator monotone supplement

All steps in `897_operator_monotone.tex` are valid under its stated continuity and nonnegativity hypotheses. Admissibility is preserved by composition because the inner function takes positive elements to positive elements and the outer scalar function is increasing. Positive linear combinations and uniform limits on bounded intervals also preserve it.

The shifted-root estimate, scaled by (4h) and divided by (2h), proves admissibility of $`g_h(t)=(\sqrt{1+4ht}-1)/(2h)`$. The recurrence $`x_{j-1}=x_j+hx_j^2`$ gives

```math
1/x_j-1/x_{j-1}=h/(1+hx_j).
```

Summation yields both displayed bounds on the iterates. Their difference is exactly the expression at supplement lines 49–50, and it tends to zero uniformly on every ([0,R]). Thus $`t/(1+\tau t)`$, and then (t/(t+s)), are admissible.

The cited integral representation has the required hypotheses. More explicitly, if $`\nu`$ is Chansangiam's finite measure on $`[0,\infty]`$, its atom at zero contributes (f(0)), its atom at infinity contributes (bt), and $`d\mu(s)=(1+s)d\nu(s)`$ on $`(0,\infty)`$. Hence the asserted integrability condition on $`\mu`$ follows. The integrand majorant is integrable, so integration in norm and the triangle inequality prove (897.12). The spectral-floor translation remains continuous, nonnegative after subtracting its value at the floor, and operator monotone. No claim for all unitarily invariant norms follows from this proof.

### Primary references and current status check

- [Loring and Vides, arXiv 1301.4252v3](https://arxiv.org/html/1301.4252v3): Conjecture 1.6 and Lemma 1.7 are both on printed p. 4 of the [versioned preprint PDF](https://arxiv.org/pdf/1301.4252v3). They state respectively the square-root target and the range $`\|[H,X]\|\ge1/4`$. The [current arXiv record](https://arxiv.org/abs/1301.4252) confirms v3 and the journal metadata *Experimental Mathematics* 24(1) (2015), 106–122.
- [Herrera, arXiv 2311.17448v1](https://arxiv.org/html/2311.17448v1): equation (7), printed p. 5; Conjectures 1.8–1.9, pp. 5–6; Theorems 1.11 and 1.12, pp. 7 and 8. The two latter bounds have factors below 1.01975 and 1.00891. These are progress toward, rather than proofs of, one. The PDF gives the homogeneous square-root formula; the abstract has a missing exponent in one displayed formula, so the theorem is the appropriate locator. The [current record](https://arxiv.org/abs/2311.17448) still lists v1.
- [Chansangiam, arXiv 1304.7936v1](https://arxiv.org/html/1304.7936v1): Proposition 1.1 and equation (1.1), printed p. 2 of the [PDF](https://arxiv.org/pdf/1304.7936v1), directly support the supplement's integral representation.
- The canonical Bhatia reference is *Matrix Analysis*, GTM 169 (1997), Problem X.5.3 p. 317 and the Chapter X notes p. 321. The [publisher chapter record](https://link.springer.com/chapter/10.1007/978-1-4612-0653-8_10) verifies the chapter and book metadata but exposes only a subscription preview. Those two individual book pages were not independently accessible in this review; the later primary statements above independently identify the target.

Bounded searches on 3 November 2026 under Pedersen, sharp square-root and fractional-power commutators, and commutator moduli found no separate primary announcement resolving the full operator-norm target. That search does not establish priority or universal absence of an unindexed result. The mathematical pass rests on the supplied proof.

### Required corrections and remaining target

No substantive mathematical correction is required. Pinning Herrera explicitly to v1 would improve citation stability. No part of the canonical target remains open within this submitted argument. The stronger all-unitarily-invariant-norm conjectures remain outside its proved scope.
