# AIM 928: mathematical review

**Final status:** Solved. **Reviewed:** 3 November 2026, by Codex (AI), separately from the author.

[Canonical problem](../../../problems/928-does-the-closed-completely-positive-cone-generate-the-energy-constrained-completion.md) · [PDF manuscript](../../solutions/928-energy-constrained-positive-cone/aim928.pdf) · [source and reproduction](../../solutions/928-energy-constrained-positive-cone/README.md).

The audit compares the complete supplied argument with the current target at revision 5d7e26e8444eb98de91988454564e45e011107c4. The original archive's earlier review assertions were not accepted as evidence.

## AIM 928 independent proof review

**Verdict: PASS FULL TARGET, with a nonblocking citation improvement.** The supplied proof shows $`X_G=C_G-C_G`$ for exactly the closed cone and completion in the current canonical problem. The factor-two proof is complete on its own. The subsequent factor-one infimum refinement is also correct. Neither argument needs to identify the larger cone of maps with finite energy norm with the completed cone.

Review date: 3 November 2026 UTC. Input: the complete original `report/sections/928.tex`, the current canonical problem, and the relevant primary references. Exact file hashes are in `verdicts.json`. TeX line locators below refer to the original submitted file.

### Exact spaces and norm

Here $`Y`$ consists of Hermiticity-preserving complex-linear maps on trace class with finite ordinary diamond norm. The real completion is taken in a fixed energy-constrained norm $`q`$, with $`E>0`$, a separable infinite ancillary space, and $`G`$ having compact resolvent, minimum eigenvalue zero, and unbounded discrete spectrum. The proof constructs components as limits in that very norm of ordinary bounded CP maps. No trace-preserving or trace-nonincreasing constraint is added.

The fixed ancillary space is large enough for every construction: it contains finite purifying ancillary spaces and an isometric copy of itself plus finitely many orthogonal flags. A Hermiticity-preserving map's ordinary diamond norm can be computed on positive normalized inputs. One way to see the relevant reduction is to embed an arbitrary trace-class input $`Z`$ into the Hermitian block matrix $`\tfrac12\left(\begin{smallmatrix}0&Z\\Z^*&0\end{smallmatrix}\right)`$, then use its positive and negative parts. Enlarging the ancilla absorbs the block index. This justifies the ordinary diamond norm interpretation used in the weighting step, rather than silently assuming positivity of $`T`$.

### Subnormalized states and the dense subspace

At lines 32–45, padding a subnormalized state by a ground state in an orthogonal ancillary flag produces a normalized admissible state. The output is a direct sum and its trace norm is at least the trace norm of the original output, even if $`T`$ is neither positive nor trace preserving. The ground eigenvector exists under the exact hypotheses, and adding it costs zero input energy. Thus (928.1) is valid.

Compact resolvent provides nested finite-rank spectral projections $`P_n`$, containing the ground eigenspace, with omitted energies bounded below by $`g_n\to\infty`$. Since $`P_n`$ commutes with $`G`$, the omitted mass on every admissible input is at most $`E/g_n`$. The gentle projection bound, on the full input and ancilla, gives the trace norm error at most $`2\sqrt{E/g_n}`$. Multiplication by the finite ordinary diamond norm of the fixed $`T\in Y`$ proves (928.2). This does not assume an ordinary-diamond bound uniform over approximating $`T`$'s.

For fixed finite input dimension $`d`$, the Choi operator is trace class even when the output space is infinite dimensional: it is a finite sum of trace-class tensor products. Finite-rank output compressions converge to it in trace norm. The bound $`\|R\|_\diamond\le\|J_R\|_1`$ at lines 76–85 has the correct direction and normalization for the unnormalized Choi vector used in the submission. For a pure normalized input with arbitrary ancilla, write its vector as $`\sum_i e_i\otimes Ve_i`$ with $`\|V\|_2=1`$, hence $`\|V\|\le1`$. Its output is an ancillary congruence of $`J_R`$ and has trace norm at most $`\|J_R\|_1`$. Convexity or purification and partial trace covers mixed states. The Hermiticity-preserving norm reduction above then gives the ordinary diamond bound.

The compressed maps $`T_{n,m}`$ consequently approximate the fixed $`T`$ in $`q`$. Two finite supports fit in a common larger finite spectral input support and finite output support, so $`D`$ is a real linear space. It is dense in $`Y`$ and therefore in $`X_G`$. No finite-dimensional approximation of the entire ancillary state space in ordinary trace norm is needed.

### The uniform CP decomposition

For $`T\in D`$ supported on $`P=P_n`$, $`W=(I+G_P/E)^{-1/2}`$ is positive and invertible on the finite input subspace. For every ordinary normalized input and ancilla, $`W\omega W`$ is subnormalized and has energy at most $`E`$, because $`WG_PW=E(I-W^2)\le EI`$. Applying (928.1) proves $`\|S\|_\diamond\le q(T)`$ for $`S=T\circ\mathop{\mathrm{Ad}}_W`$, including entangled inputs.

The finite-dimensional decomposition (928.5) is valid for arbitrary Hermiticity-preserving maps, without a channel normalization. For Hermitian Choi matrix $`J`$, its ordinary diamond norm is the optimum of

```math
\min t\quad\text{subject to}\quad Z\ge J,\quad Z\ge-J,
\quad\mathop{\mathrm{Tr}}_B Z\le tI.
```

There is no extra requirement $`Z=|J|`$; such a requirement would in general be unjustified. The positive Choi matrices ( (Z+J)/2) and ( (Z-J)/2) define CP maps whose sum has diamond norm $`\|\mathop{\mathrm{Tr}}_B Z\|_\infty`$. Finite-dimensional SDP duality gives an attaining $`Z`$ and the asserted equality. A direct source for this Choi form, and the specialization from its displayed block dual, are supplied below.

The maps $`T_\pm=S_\pm\circ\mathop{\mathrm{Ad}}_{W^{-1}P}`$ are ordinary bounded CP maps with finite supports. Inverting $`W`$ only on that finite subspace avoids an unbounded inverse on the full Hilbert space. For an admissible full input, the transformed positive input $`\tau=W^{-1}P\rho PW^{-1}`$ has

```math
\mathop{\mathrm{Tr}}\tau
=\mathop{\mathrm{Tr}}(P\rho P)+E^{-1}\mathop{\mathrm{Tr}}(G_P P\rho P)
\le2.
```

Hence $`q(T_++T_-)\le2\|S_++S_-\|_\diamond\le2q(T)`$. The constant is independent of input and output dimensions, the support cutoff, and $`T`$. This uniformity is the needed ingredient for the completion argument.

For CP outputs, the trace of either positive component is at most the trace of their sum, so $`q(T_\pm)\le q(T_++T_-)`$. The argument does not assume the stronger, generally unavailable uniform bound on their ordinary diamond norms.

### Exact membership in the completed cone

Choose $`x_k\in D`$ with $`q(x-x_k)\le\epsilon2^{-k}`$ and $`d_1=x_1,d_k=x_k-x_{k-1}`$. The estimate

```math
\sum_k q(d_k)\le q(x)+2\sum_kq(x-x_k)\le q(x)+2\epsilon
```

is correct, including the initial term. Applying the uniform decomposition separately to the $`d_k`$'s gives absolutely convergent series $`a=\sum a_k,b=\sum b_k`$ in the complete normed space $`X_G`$. Every finite partial sum is an ordinary bounded CP map in $`Y`$. Thus the two limits lie in the specified $`C_G`$ by its definition, and $`a-b=x`$ exactly. The norm bound $`q(a+b)\le2q(x)+4\epsilon`$ follows by applying the triangle inequality to the sums of CP pairs. Choosing $`\epsilon<\eta/4`$ proves the main theorem as written.

This step does more than prove density of $`C_G-C_G`$. It supplies a single pair of limits in the closed cone for each $`x`$; summability is what ensures those limits exist. It also does more than decompose $`x`$ in the larger cone with finite energy norm.

### The factor one refinement

The finite-dimensional primal (928.8) is correct. Purification gives the maximum, over input marginals $`\rho`$ of energy at most $`E`$, of the trace norm of $`(I\otimes\sqrt{\rho})J(I\otimes\sqrt{\rho})`$. Trace norm duality converts this to the two inequalities $`-I\otimes\rho\le X\le I\otimes\rho`$. Singular $`\rho`$ cause no problem: these inequalities force the required support, and a contraction on that support realizes $`X`$. Choosing an eigenbasis of $`G_P`$ makes the input transpose preserve the energy constraint.

The finite-input norm equals the full-space (q(T)): compression of a full input gives a subnormalized state on $`P\mathcal H_A`$; padding within that same subspace with a ground vector and an ancillary flag can only increase the output trace norm. Conversely, states supported on $`P\mathcal H_A`$ are allowed full-space inputs.

For clarity, the primal Lagrangian with multipliers $`A,B\ge0,\lambda\ge0,\mu\in\mathbb R`$ has variable terms

```math
\mathop{\mathrm{Tr}}((J-A+B)X)
+\mathop{\mathrm{Tr}}((\mathop{\mathrm{Tr}}_B(A+B)-\lambda G_P-\mu I)\rho)
+\mu+\lambda E.
```

Taking the supremum over Hermitian $`X`$ and positive $`\rho`$ forces $`A-B=J`$ and the displayed partial trace inequality in (928.9). Conversely $`Z\ge\pm J`$ gives $`A=(Z+J)/2,B=(Z-J)/2\ge0`$, so the dual stated in the submission is exact. No sign error or omitted trace multiplier occurs.

There is a positive-definite density matrix with energy strictly below $`E>0`$, by assigning a sufficiently large weight to a ground vector and a small positive weight to the rest of the finite input basis. With $`X=0`$, all cone inequalities are strict. The dual is feasible, for example with a sufficiently large scalar $`Z`$ and $`\mu`$. Slater's theorem therefore gives strong duality and dual attainment as used at lines 212–215.

For an optimum $`Z,\mu,\lambda`$, the corresponding CP sum has energy norm at most $`\mu+\lambda E=q(T)`$. Positivity of its outputs gives the reverse inequality. Evaluation on a ground vector implies $`\mu\ge0`$, since $`Z\ge0`$; with $`\lambda\ge0`$, the bound on the partial trace extends by zero to the omitted spectral subspace. Thus the full-space norm comparison is valid as well.

Using these improved finite-support decompositions in the same summable series gives $`q(a+b)\le q(x)+\eta`$. For arbitrary $`a,b\in C_G`$, approximating them by ordinary CP maps and passing $`q(A-B)\le q(A+B)`$ to the limit proves the lower bound in the exact infimum formula. The proof correctly distinguishes an infimum from an attained minimizing pair in $`X_G`$.

### Primary references and citation correction

- [Shirokov, arXiv 1810.10922v2](https://arxiv.org/html/1810.10922v2), published in *Lobachevskii Journal of Mathematics* 40(10) (2019), 1549–1568: Theorem 1B and equation (31), printed p. 10 of the [versioned manuscript PDF](https://arxiv.org/pdf/1810.10922v2), identify the CP completion and its sublinear energy growth condition. Theorem 3B, p. 20, identifies the vector-space completion. The exact decomposition conjecture appears in §5, p. 23. These locators concern the closed cone $`\mathfrak F_G^0`$, as required.
- [Van Luijk, published article](https://link.springer.com/article/10.1007/s00220-025-05282-w), *Communications in Mathematical Physics* 406 (2025), article 120: Lemma 2.19 begins on article p. 19, its part (6) and the ensuing decomposition paragraph are on p. 20, and footnote 11 is on p. 20 of the [published PDF](https://link.springer.com/content/pdf/10.1007/s00220-025-05282-w.pdf). Its components have finite energy norm; that paragraph does not impose membership in the closure of ordinary bounded CP maps. The submitted proof correctly addresses this extra requirement independently.
- [Watrous, 2009](https://theoryofcomputing.org/articles/v005a011/), *Theory of Computing* 5 (2009), 217–238: §3 gives a general Stinespring-form SDP on pp. 226–231; §4, pp. 231–232, displays a Choi SDP specialized to differences of channels. The simple two-sided Hermitian Choi program used at submitted lines 121–127 is not literally the program displayed for arbitrary maps there. This is a citation precision issue, not a failure of (928.5).

The most direct additional entry is:

> J. Watrous, *Simpler semidefinite programs for completely bounded norms*, arXiv:1207.5726v2 (2 August 2012), [versioned record](https://arxiv.org/abs/1207.5726v2), [PDF](https://arxiv.org/pdf/1207.5726v2).

Its exact preprint locators are Theorem 6, printed p. 10, and §3.2, the unnumbered Choi-form primal/dual pair on p. 11, with strong duality and attainment on pp. 11–12. For Hermitian $`J`$, average any feasible displayed block dual with its block swap. This gives equal diagonal blocks $`Z=(Y_0+Y_1)/2`$, without increasing the objective. Hadamard conjugation of the resulting block matrix is equivalent to $`Z\ge\pm J`$, and its objective is $`\|\mathop{\mathrm{Tr}}_B Z\|_\infty`$. Introducing $`tI\ge\mathop{\mathrm{Tr}}_B Z`$ gives exactly (928.5)'s asserted dual.

Suggested citation placement is the sentence immediately after (928.5), original TeX lines 121–127: identify this as the Hermitian specialization of Watrous's Choi-form SDP and cite the versioned 2012 source alongside the general 2009 reference. The energy-constrained SDP later in the submission is derived there and need not be attributed to Watrous as a previously stated theorem.

For comparison, the [published author-hosted PDF](https://cs.uwaterloo.ca/~watrous/Papers/SimplerSDPforCBnorm.pdf), dated 11 July 2013 and headed *Chicago Journal of Theoretical Computer Science*, has different numbering: Theorem 3.1 and the §3.2 primal/dual pair on printed p. 12, strong duality on p. 13. Version and page numbers should not be mixed.

Bounded searches on 3 November 2026 under Shirokov's cone-completion conjecture and energy-constrained CP decomposition did not locate another primary theorem settling the closed-cone requirement. The 2025 paper is a partial result for the larger cone. This search does not establish novelty or priority.

### Required corrections and remaining target

Add or substitute the precise Watrous Choi-SDP citation as described above. No mathematical alteration is required for either the factor-two proof or its refinement. No residual part of the canonical exact-difference target remains outside the proof. The proof does not assert existence of a norm-minimizing decomposition for arbitrary $`x\in X_G`$.
