# 920. Invariant subspaces under complexification of real operators

**Area:** Operator theory and real Banach spaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be an infinite-dimensional separable real Banach space, and let $`T:X\to X`$ be a bounded real-linear operator. Assume that the only norm-closed real-linear subspaces $`M\subseteq X`$ satisfying $`T(M)\subseteq M`$ are $`\{0\}`$ and $`X`$.

Equip the algebraic complexification
```math
X_{\mathbb C}=X+iX
```

with the usual complex scalar multiplication
```math
(a+ib)(x+iy)=(ax-by)+i(bx+ay)
```

and the Taylor norm
```math
\|x+iy\|_{\mathbb C}
=\sup_{\theta\in[0,2\pi]}\|x\cos\theta-y\sin\theta\|_X.
```

Define its bounded complex-linear extension by
```math
T_{\mathbb C}(x+iy)=Tx+iTy.
```


Must every norm-closed complex-linear subspace $`N\subseteq X_{\mathbb C}`$ satisfying $`T_{\mathbb C}(N)\subseteq N`$ be either $`\{0\}`$ or $`X_{\mathbb C}`$?

This is Conjecture 3 of Abramovich, Aliprantis, Sirotkin and Troitsky [2], restated in Section 4.9 of [1]. It concerns ordinary invariant subspaces. Invariance under every operator commuting with $`T`$, called hyperinvariance, is a different condition.

One direction is elementary: a nonzero proper closed real invariant subspace $`M`$ produces the nonzero proper closed complex invariant subspace $`M+iM`$. The question asks for the converse implication between existence of invariant subspaces. No positivity, lattice, basis, reflexivity or Hilbert-space assumption is imposed on $`X`$ or $`T`$. Equivalent reasonable complexification norms give the same closed subspaces, so the specified norm fixes conventions.

## Application

The question asks whether complexification preserves the absence of decompositions for a real linear evolution. It would clarify when complex operator methods can detect invariant components of an operator originally defined over the real field.

## Known cases and scope

Proposition 4.1 of [3] proves the equivalence of real and complexified invariant-subspace existence when $`X`$ is a real Banach lattice whose order is induced by an unconditional basis. That additional structure is absent from the general question above.

Infinite dimension is part of the question: a rotation through a right angle on $`\mathbb R^2`$ has no nontrivial real invariant line, whereas its complexification has eigenlines.

## References

1. M. S. Moslehian, G. A. Muñoz-Fernández, A. M. Peralta and J. B. Seoane-Sepúlveda, [*Similarities and differences between real and complex Banach spaces: an overview and recent developments*, arXiv:2107.03740v1 (8 July 2021)](https://arxiv.org/abs/2107.03740v1), Section 4.9. [Version 3 (24 February 2022)](https://arxiv.org/html/2107.03740v3) retains the question and supplies complexification definitions in Sections 2.2 and 4.2. Published in *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* **116** (2022), article 88; [DOI 10.1007/s13398-022-01222-8](https://doi.org/10.1007/s13398-022-01222-8).
2. Y. A. Abramovich, C. D. Aliprantis, G. Sirotkin and V. G. Troitsky, *Some open problems and conjectures associated with the invariant subspace problem*, *Positivity* **9** (2005), no. 3, 273–286, Conjecture 3; [DOI 10.1007/s11117-004-3786-9](https://doi.org/10.1007/s11117-004-3786-9). The original attribution and wording were cross-checked against the survey and indexed author-manuscript text; direct access to the author PDF returned HTTP 403.
3. E. A. Gallardo-Gutiérrez and F. J. González-Doña, *Band-diagonal operators on Banach lattices: Matrix dynamics and invariant subspaces*, *Linear Algebra and its Applications* **674** (2023), 155–191, Proposition 4.1, printed p. 184; [DOI 10.1016/j.laa.2023.05.017](https://doi.org/10.1016/j.laa.2023.05.017), [institutional full text](https://e-archivo.uc3m.es/rest/api/core/bitstreams/fb6949dd-5e47-4200-ae9e-51c65160aadd/content).

4. OpenAI, [*Invariant-projection counterexamples for every irrational rotation*](https://github.com/openai/math/blob/main/preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/paper.pdf), preprint (27 September 2026), Theorem 1.1 and Corollary 1.4; [*Backward intertwiners and a transitive commutant*](https://github.com/openai/math/blob/main/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/paper.pdf), Theorem 1.1, Corollary 1.2 and §6.1. Announced hyperinvariant-subspace results; no assertion here of independent verification of their full proofs.

## Status review


**Known cases:** The primary complexification conjecture remains the ordinary invariant-subspace question. The recent factor hyperinvariant example and Banach-lattice special cases do not settle ordinary invariant subspaces for all complexifications.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The primary complexification conjecture remains the ordinary invariant-subspace question. The recent factor hyperinvariant example and Banach-lattice special cases do not settle ordinary invariant subspaces for all complexifications.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The revised and published survey preserves the precise complexification question. The 2023 result above covers the stated Banach-lattice case. Bounded searches checked the original authors and title, the conjecture number, complexification, later solutions and counterexamples, and indexed Prove2Me results. No matching complete resolution was located; these checks do not certify exhaustive absence of a solution.

The current OpenAI Math family 293 [4] concerns hyperinvariant subspaces and invariant projections inside a specified factor. Its two linked native manuscripts were checked at their main statements. The direct construction explicitly retains nontrivial ordinary invariant tail subspaces, including in Section 6.1. It therefore does not assert the complexification implication asked here.

All-status AIM and FURTHER comparisons included Banach-space geometry, information complexity, cyclicity of the Dirichlet shift, and common invariant subspaces of an invertible operator and its inverse on reflexive spaces. Their mathematical targets differ from this conditional real-to-complex question. The independent review and current finding-delta check found no equivalent target; these are bounded comparisons.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a462ecdd7f3722ea**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
