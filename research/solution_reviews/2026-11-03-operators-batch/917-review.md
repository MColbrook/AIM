# AIM 917: mathematical review

**Final status:** Solved. **Reviewed:** 3 November 2026, by Codex (AI), separately from the author.

[Canonical problem](../../../problems/917-split-products-for-time-dependent-form-sum-schrodinger-evolution.md) · [PDF manuscript](../../solutions/917-nonautonomous-split-product-counterexamples/aim917.pdf) · [source and reproduction](../../solutions/917-nonautonomous-split-product-counterexamples/README.md).

The audit compares the complete supplied argument with the current target at revision 5d7e26e8444eb98de91988454564e45e011107c4. The original archive's earlier review assertions were not accepted as evidence.

## AIM 917: independent mathematical audit

Reviewer lane: c. Date: 2026-11-03. Repository base observed: `5d7e26e`.

**Verdict: accept the counterexamples as a complete negative resolution of both questions in the current canonical statement.** I found no fatal mathematical gap. The uniformly bounded strengthening also works for the exponential product. This report distinguishes failure to converge to the specified propagator from nonexistence of every possible weak limit.

### Material reviewed and target

Reviewed `submission/report/sections/917.tex` and `917_bounded.tex`, relative to `.cache/operators-batch/_sources/`, against `problems/917-split-products-for-time-dependent-form-sum-schrodinger-evolution.md` and the shared bibliography. The target assumes form relative bounds and strong differentiability only on the common form scale, not strong continuity of `V(t)` on the original Hilbert space or stability of the split factors on the dual form space. A single example on `[0,1]` refutes a universal assertion under these hypotheses.

SHA-256 of the reviewed main section: `328e87a4222b71a06a61420718fb69e90c8605ac303e03c8aa60cb443a6c5a31`.
SHA-256 of the bounded supplement: `1617a4801109988c17e1ee2c1b32a216ec68a8a48a3a98db753593f5abda2df7`.

### Source hypotheses and product conventions

Directly checked [Vuillermot--Wreszinski, publisher PDF](https://ems.press/content/serial-article-files/44680): positivity (7), printed p. 319; (V), (V'), equations (24), (29), p. 323; Remark (3), equations (32), (33), p. 324, continuing p. 325. These match the canonical data hypotheses and the stated left-endpoint product order. The proved full-Hamiltonian formulas (30), (31) are different. The discussion of split factors (69), (70), printed p. 336, identifies dual-form-space stability (18) as an additional obstruction; it is not a hypothesis on the data in the current canonical question. The construction does not contradict the paper's conditional approximation theorem.

### Main construction: checks

1. **The recursive mesh choice is valid.** At stage `n`, the sum of earlier bump functions is a fixed continuous nonnegative scalar function. Its integral is at most `sum 2 g_k w_k < 1/512 < delta`. Its left Riemann sums consequently satisfy the required bound for all sufficiently large mesh sizes. An arbitrarily large integer also meets `N_n >= 4 N_(n-1)`.

2. **The selected grid sees exactly the intended peak.** Each `w_n < h_n/10`. With `h_(n+1) <= h_n/4`, the intervals are disjoint and every later interval begins after `tau_n = 1-h_n`, the final left-endpoint sample on the `N_n` grid. No later group is sampled. The current interval contains just that last node because its width is smaller than the mesh spacing. Endpoint `1`, where `V(1)=0`, is absent from the product.

3. **Self-adjointness and form domains satisfy the question literally.** The diagonal `H_0` is self-adjoint on its usual weighted sequence domain and is at least `I`. Every individual `V(t)` is a bounded self-adjoint operator of rank at most two. Its form has domain the whole Hilbert space and is closed and semibounded at that individual time, including when its negative eigenvalue is large. Thus its form domain contains `Q`; no convention about a general indefinite unbounded form is needed. The sum is the ordinary bounded perturbation of `H_0` at each time, and also its form sum.

4. **The common form bounds are correct.** In the `Q` norm `||H_0^(1/2) u||`, conjugation by `H_0^(-1/2)` gives

   `B(t) = (g_n/sqrt(lambda_n)) beta((t-tau_n)/w_n) S_n = w_n^2 beta(...) S_n`.

   The two-coordinate inequality `2 |u_0 u_n| <= lambda_n^(-1/2)(|u_0|^2 + lambda_n |u_n|^2)` gives exactly the displayed form estimate. Differentiation gives `||B'(t)|| <= 2w_n`. These are bounds on the norm of the representing operators, hence also bounds on the diagonal forms. Both satisfy the same constants `a=1/4`, `b=0`. Positivity is stronger than needed: `q_t >= (3/4)q_0 >= (3/4)||u||^2`.

5. **Regularity at the accumulation endpoint is not being assumed without proof.** Bump values and first derivatives vanish at their endpoints. Near `1`, `||B(t)||/(1-t) <= 2w_n^2/h_n -> 0`, and the derivative norms tend to zero. Therefore the one-sided derivative at `1` is zero, and the derivative is norm continuous there. This proves norm `C^1([0,1]; L(Q,Q*))`, a stronger assertion than the source's strong differentiability. In contrast, this does not assert continuity of `V(t)e_0` in Hilbert norm.

### What the two product arguments prove

For the exponential product, telescoping unitary factors against the free product gives the prefix error at most `h_n sum_(j<N_n-1) ||V(jh_n)|| <= delta`. This is an operator norm estimate and does not involve an unjustified unbounded-generator estimate. At the final sample, `h_n g_n = pi/2`, so the perturbation step sends `e_0` exactly to `-i e_n`. The free last step only changes its phase. Thus

`P^E_(N_n)e_0 = c_n e_n + r_n`, with `|c_n|=1`, `||r_n|| <= delta`.

Orthogonality gives distance at least `sqrt(2)-2delta` between distinct terms of this subsequence. This proves **nonexistence of a strong limit**, not merely failure of the proposed limit.

For the resolvent product the same telescoping is legitimate because all factors are contractions and `||(I+ihV)^(-1)-I|| <= h||V||` for bounded self-adjoint `V`. The free prefix sends `e_0` to a multiple of modulus at most one. At the exceptional final perturbation step,

`||(I+i(pi/2)S_n)^(-1)e_0|| = 1/sqrt(1+pi^2/4)`.

The last free resolvent cannot increase norm. Therefore the selected product images have norm at most `1/sqrt(1+pi^2/4)+delta < 1`. Every image of `e_0` under the specified unitary propagator has norm one, producing the stated fixed strong-convergence gap. For contractions, weak convergence to a unitary implies strong convergence, by the displayed inner-product inequality. Consequently **the resolvent products do not converge weakly or strongly to `U(1,0)`**. This does not prove that the resolvent sequence has no weak limit whatsoever. The same contraction-to-unitary observation also excludes weak convergence of the exponential products to `U`, although the theorem only needs its stronger no-strong-limit statement.

### Propagator existence and its independent identification

The form hypotheses already supply the propagator assumed in the problem. Independently, `sum g_n w_n=1/1024` and `integral beta=16/15` give `integral ||V(t)||dt = 1/960`. The family is Bochner measurable in operator norm: it is a pointwise norm limit of finite sums of measurable finite-rank terms. In the interaction picture each term stays in the two-dimensional span of its matrix units and acquires continuous scalar phases. Its norm remains integrable. The usual Volterra/Dyson construction for an integrable bounded self-adjoint perturbation therefore applies and is unitary.

The short identification paragraph can be expanded without an extra hypothesis. For initial data in `Q`, use transported finite-support vectors as time-dependent test vectors in the form equation. Their derivatives are admissible, and cancellation of the free part gives the weak interaction-picture integral equation. Its integrand is bounded in norm by `||V(t)|| ||u||`; density of the test vectors turns this into the same Bochner integral equation. Its unique solution identifies the form evolution on `Q`, then density identifies it on the whole Hilbert space. This supports the additional norm bound `||U(1,0)-exp(-iH_0)|| <= 1/960`. This identification is ancillary: the nonconvergence proof needs only unitarity of the form propagator.

### Uniformly bounded extension

I also checked the supplement independently.

- The forbidden sets at every finite stage are closed and finite unions of intervals and points. Apart from `0` they have positive distance from `0`. The choice ensuring `1 in J_n` is therefore possible. The two counting estimates exclude at most a `delta/2` fraction of grid points. Finitely many chosen centers have positive distance from the forbidden set, so a common positive width satisfying all requirements exists.
- All groups' bump intervals are pairwise disjoint. Later groups avoid every earlier grid by the definition of `Z`. Thus the sum defining `V(t)` has at most one nonzero term and is a bounded finite-rank self-adjoint operator at every time, with global norm at most one and integral at most `epsilon_0`.
- The choice of resonant `lambda_n = 1+2pi k_n N_n` can simultaneously make `lambda_n^(-1/2)(1+2/w_n) <= 2^(-n)/16`. Uniform convergence of both form-operator series proves norm `C^1`, including all accumulation points, with the stated form and derivative bounds. This avoids a hidden differentiability gap in the infinite sum.
- Weak operator continuity follows first on `Q x Q` from form continuity and then on arbitrary Hilbert vectors from density and the uniform operator bound. Failure of strong continuity at zero follows from the exact values `V(1/N_n)e_0=e_n` and `V(0)e_0=0`.
- At mesh `N_n`, replacing earlier sampled perturbations by zero costs at most `delta/4` in operator norm. On `span(e_0,e_n)`, every free step is exactly `exp(-ih_n)I`; the resonant identity, rather than an approximate commutator argument, permits the product to be calculated. Its ideal image is `exp(-i)(cos(a_n)e_0-i sin(a_n)e_n)`, with `a_n=m_n/N_n in [1-delta,1]`. The claimed separation follows.

Hence the bounded supplement proves **no strong limit for the exponential products**, with norm `C^1` regularity on the form scale, weak operator continuity of `V`, and arbitrarily small time integral. It does not establish a bounded-family resolvent counterexample, and the text correctly restricts its strengthening to the exponential question.

### Required changes, surviving scope, and literature limits

No correction is required for the mathematical resolution of the current canonical question. Preserve the distinction between failure of weak convergence to `U` and nonexistence of a weak limit. Expanding the propagator-identification paragraph would improve exposition, but is not needed to repair the counterexample.

A bounded current search by source title/authors and split-product terminology did not locate a separate published counterexample or correction. This is not a priority determination and is not a claim that the full later splitting literature was exhaustively searched. The present validity verdict rests on the explicit construction and direct verification of the source hypotheses.
