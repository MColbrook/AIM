# AIM 921: mathematical review

**Final status:** Solved. **Reviewed:** 3 November 2026, by Codex (AI), separately from the author.

[Canonical problem](../../../problems/921-generic-backward-uniqueness-for-linear-retarded-equations.md) · [PDF manuscript](../../solutions/921-generic-retarded-backward-uniqueness/aim921.pdf) · [source and reproduction](../../solutions/921-generic-retarded-backward-uniqueness/README.md).

The audit compares the complete supplied argument with the current target at revision 5d7e26e8444eb98de91988454564e45e011107c4. The original archive's earlier review assertions were not accepted as evidence.

## AIM 921: independent mathematical audit

Reviewer lane: c. Date: 2026-11-03. Repository base observed: `5d7e26e`.

**Verdict: accept as a complete positive resolution of the current canonical residuality question, for every fixed `n>=1` and `r>0`.** I found no fatal mathematical gap in the enlarged Hilbert-space construction, parameter continuity, gap-family density or all-real-time Baire argument. The proof uses the actual compact operator-norm `C^1` topology in the problem, not a weaker coefficient topology or a restricted discrete-delay class.

### Material and primary reference

Reviewed `.cache/operators-batch/_sources/submission/report/sections/921.tex`, its bibliography entry, and `problems/921-generic-backward-uniqueness-for-linear-retarded-equations.md`.

SHA-256 of the reviewed section: `2e46cee5a3835470d965a5a677536728866916cb769bf94cb6d72a0207d49029`.

Directly checked [Hale--Oliva, author institutional PDF](https://repositorio.usp.br/directbitstream/e2db4023-5223-4344-8a90-cb614512aaec/3189103.pdf): the coefficient norm and compact `C^1` topology are defined on printed pp. 28--29; local/restricted residual statements are Corollaries 3.1--3.2, p. 32; the full-space density result is Theorem 4.1, pp. 34--35; and Section 5 opens on p. 35 by leaving full residuality unresolved. Its density proof uses an atom at the maximal delay and a gap before the remaining delay measure. The submission independently establishes injectivity of that family on its enlarged phase space; it does not misquote the source as already proving residuality. The 1993 book was not needed for the proof and its page 380 was not directly verified in this audit.

### 1. The common measure really follows from the stated regularity

Riesz representation entry by entry identifies `B_r=L(C_r,R^n)` with matrices of finite real signed measures. The sum of entrywise variation norms is equivalent to the operator norm, with constants depending only on the fixed dimension. Thus an operator-norm `C^1` path of functionals is a variation-norm `C^1` path of measure matrices, and its derivative has the same interpretation.

For compact `[a,b]`, define

`nu = sum_(ij) (|mu_(a,ij)| + integral_a^b |mu'_(s,ij)| ds)`.

This is a finite positive measure. The variation map is Lipschitz in variation norm; therefore the integrand is norm continuous and Bochner integrable. The Banach-space fundamental theorem of calculus and the measure-order triangle inequality give `sum |mu_(t,ij)| <= nu` for every `t` in the interval, as a measure inequality, not just a bound on total mass.

The Radon--Nikodym identification with `L^1(nu)` is isometric entry by entry. Consequently the density path is continuous in `L^1`, has a jointly measurable representative, and satisfies `sum |R_ij(t,theta)| <= 1` for `dt dnu` almost every pair. This is the correct common envelope needed for Fubini. Compactness of a general continuous measure-valued path alone would not justify this particular finite envelope; the proof correctly uses its `C^1` dependence.

For a difference path its envelope mass is at most the initial variation-norm difference plus `(b-a)` times the supremum derivative difference. Hence it tends to zero in the stipulated compact `C^1` topology. This is the key quantitative point that would be missing in an argument based only on uniform weak convergence of measures.

### 2. Well-defined evolution on `E=R^n + L^2`

The current value and the `L^2` history are independent components; assigning an endpoint value to the `L^2` class is unnecessary. With a Borel representative of that class, the common density kernel makes the forcing measurable. For each fixed delay `theta`, translation in the time variable preserves Lebesgue-null sets. Fubini for `ds dnu(theta)` therefore proves independence of the representative despite allowing atoms and singular distributed measures.

The forcing estimate is valid: apply the matrix-density bound, Minkowski's integral inequality, and then the translation estimate

`||1_(s+theta<sigma) phi(s+theta-sigma)||_(L^2_s) <= ||phi||_2`.

This yields `||F_(L,phi)||_2 <= nu([-r,0]) ||phi||_2`. There is no attempt to evaluate an arbitrary `L^2` history at a fixed point as a bounded functional.

For the future term, the total-variation bound gives

`|B_L x(s)| <= M sup_(sigma<=u<=s) |x(u)|`.

This is a causal Volterra bound. Iterating its time integral gives the usual factorial estimates, hence existence and uniqueness for arbitrary initial state over any finite interval, even with an atom at zero. The solution is continuous and absolutely continuous with derivative in `L^2`: the initial forcing is `L^2` and the future term is bounded on a finite interval. The displayed Gronwall estimate follows directly. The terminal history consists of a translated portion of the original `L^2` history plus a bounded future segment; these estimates make `U_L(t,sigma)` a bounded linear map on `E`.

#### Rejoining and right continuity

The evolution law needs special attention because the joined state has independent current value and history. At a rejoining time the concatenated paths can differ at a single point, but for fixed `theta` the set of times sampling that point has Lebesgue measure zero. The same common-envelope Fubini argument makes its contribution vanish almost everywhere in the integrated equation. Uniqueness then gives the claimed composition law. This would be suspect for an unrestricted time-dependent moving point mass; variation-norm `C^1` regularity and the envelope are what make it valid here.

Strong right continuity at the initial time also holds. The current value tends to its prescribed initial value. Translations of the old history converge in `L^2`, and the newly filled segment has vanishing length and bounded values. Norm continuity in the time variables is neither claimed nor used. Evolution can be continued on successive compact intervals, and uniqueness makes these local definitions consistent for all real initial times and every finite later time.

### 3. Operator-norm continuity in the coefficient

For nearby coefficient families and the same initial state, the forcing difference has `L^2` norm at most `nu_Delta mass * ||phi||_2`. The future difference decomposes exactly into `B_L(x-x_tilde)` plus `(B_L-B_Ltilde)x_tilde`. The latter is at most `nu_Delta mass * sup|x_tilde|`. The solution estimate supplies a uniform bound for `x_tilde` on a compact `C^1` neighborhood. Gronwall then gives

`sup|x-x_tilde| <= C * nu_Delta mass * (|a|+||phi||_2)`.

In the terminal histories the old initial-history portions agree exactly, and the difference of future portions is bounded by `sqrt(r) sup|x-x_tilde|` in `L^2`. Taking the supremum over the initial unit ball proves operator-norm continuity of `L -> U_L(t,sigma)` for every fixed pair. Thus the preimages used later are genuinely open in the original Frechet topology.

### 4. Gap-family injectivity on the enlarged space

For `L(t)f=A(t)f(-r)+integral_[-r+rho,0] d eta_t f`, with `0<rho<r` and `A(t)` invertible almost everywhere, terminal zero means that the concatenated trajectory is zero almost everywhere on `[t-r,t]`, with zero current value. Forward uniqueness extends it by zero afterward.

Suppose a zero region starts at `b >= sigma-r`. For almost every

`s >= max(sigma,b+r-rho)`,

the future derivative is zero, and all arguments in the residual delay integral are at least `b`. Its contribution vanishes for almost every such `s` by the common-envelope Fubini argument. Therefore `A(s)x(s-r)=0`, and almost-everywhere invertibility gives a zero region starting at

`max(sigma-r,b-rho)`.

The derivative-zero assertion is legitimate: `r-rho>0` makes these future times lie inside the already vanishing region, and the future path is continuous and absolutely continuous. Each iteration moves the lower endpoint backward by `rho`, until it reaches `sigma-r`. At most `ceil((t-sigma)/rho)` iterations suffice. The initial history is then zero in `L^2`, and continuity from the future at `sigma` forces the independent current value to be zero as well.

Crucially, this argument uses no bounded inverse estimate for `A(s)` and does not demand it be invertible at every time. Its almost-everywhere version is sufficient. It proves injectivity for every state in `E`, not just continuous compatible histories.

### 5. Density in compact `C^1` topology

Evaluation of a finite measure on the singleton `{-r}` is a bounded linear map on the variation-norm measure space, so `A(t)=mu_t({-r})` is globally `C^1`. Removing the measure in `(-r,-r+rho)` is a bounded linear restriction operation. Those restriction operators tend strongly to zero as `rho` decreases to zero: the intervals decrease to the empty set, and every finite variation measure is continuous from above. Their norms are uniformly at most one, so convergence is uniform on each norm-compact set. Apply this separately to the compact images of `mu_t` and `mu'_t` on the time interval being approximated. The same fixed restriction commutes with differentiation, so this proves approximation in `C^1`, not just in `C^0`.

To perturb the atom, for fixed `t` the function `S -> det(A(t)+S)` is a nonzero polynomial in the finitely many real matrix entries. It is not identically zero, since some translate is invertible. Its zero set has Lebesgue measure zero. The set of bad pairs `(t,S)` is measurable. Fubini on each `[-m,m]` times a small matrix ball, followed by a countable intersection over `m`, gives arbitrarily small constant matrices `S` for which `A(t)+S` is invertible for almost every real `t`. This changes no time derivative. Gap truncation remains a globally `C^1` family, while closeness is required only on the compact time set defining a neighborhood. The claimed dense family therefore exists in exactly the stated full coefficient space.

### 6. The `G_delta`, Baire and all-real-time steps

For bounded operators on the separable real Hilbert space `E`, `ker T=0` is equivalent to density of `Ran T*`. The proposed countable open tests approximate every orthonormal basis vector by `T*v` for `v` in a fixed countable dense set. Their intersection is precisely the set of injective operators: approximability of the basis gives density of the linear range; conversely density of the range and density of the chosen test vectors supply every approximation. Norm continuity of the adjoint makes each test open.

For every rational `sigma<t` take these tests' coefficient preimages. Every open preimage contains the single dense gap family, since that family is injective at all times; hence each is dense. There are countably many tests and rational pairs. `C^1(R;B_r)` is a complete metrizable locally convex space because `B_r` is Banach. It is Baire even though the coefficient Banach space need not be separable. The intersection `R` is therefore a dense `G_delta`.

The passage to all real pairs is valid and does not require injectivity to be closed under time limits. If `U(t,sigma)v=0`, choose rational `p>t` and any rational `q` strictly between `sigma` and `t`. Composition gives

`U(p,q) U(q,sigma)v = U(p,t) U(t,sigma)v = 0`.

Rational-pair injectivity forces `U(q,sigma)v=0`. Rational `q` can decrease to the original real `sigma`; strong right continuity then gives `v=0`. This covers every real initial and terminal time, including arbitrarily short intervals, with no uncountable Baire intersection.

Finally `J phi=(phi(0),phi)` is a bounded injection from the original continuous-history space into `E`. It need not have closed range or a bounded inverse on its image; neither is used. The classical continuous-history trajectory satisfies the integrated equation, so uniqueness gives the stated intertwining identity. Thus every `L` in `R` has injective classical solution maps for every real pair, proving that `G_(r,n)` contains a countable intersection of open dense sets, exactly the problem's definition of residuality.

### Required changes and remaining scope

No mathematical correction is required for the current canonical target. For exposition, the single-point joining argument and the almost-everywhere zero-region induction are worth retaining explicitly; both are essential. The result makes no assertion of surjectivity, a bounded inverse, residuality in a weaker `C^0` topology, or operator-norm continuity of `U` at the initial time.

A bounded fresh search by Hale--Oliva title, residuality, backward uniqueness, retarded equations and Hilbert phase spaces did not identify an independent full resolution. This is not an exhaustive current-literature or novelty determination. The validity assessment follows from checking the manuscript's new argument, rather than treating the old density theorem as a substitute for it.
