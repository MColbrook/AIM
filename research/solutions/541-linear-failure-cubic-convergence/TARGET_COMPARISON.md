# Target comparison: partial result for AIM 541

The target is [Problem 541, Low-degree convergence of relaxed
minimal-deformation surface elements](https://github.com/MColbrook/AIM/blob/24edaadc6bb272737d8da0745c662c992db07b22/problems/541-low-degree-relaxed-minimal-deformation.md),
checked at repository revision `24edaadc6bb272737d8da0745c662c992db07b22`.
Its statement is unchanged from the originally considered revision
`a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

**Scope: Partially solved (proposed). Known cases: degree 1 is negative in
general; degree 3 is positive under the original assumptions. Remaining
target: degree 2.**

| Original requirement | Manuscript result and location | Relation |
| --- | --- | --- |
| A smooth closed oriented initial surface and smooth ambient velocity; a smooth exact RMD flow and smooth inverse on a fixed interval | Equations (2.1), the torus and field in Section 2, and the general cubic hypotheses at the start of Section 6 | The linear example is one admissible instance; the cubic theorem covers the full original smooth data class. |
| Shape-regular quasi-uniform degree-k nodal curved meshes with the stated uniform parametrization and inverse bounds | Lemma 2.1 verifies the linear family; equation (6.1) states exactly the original cubic bounds, used in Section 6.1 | One admissible family for the counterexample; every original admissible family for the cubic theorem. |
| Exact fixed-reference mass and stiffness, with raw discontinuous geometric unit normals; no additional stabilization | Equations (2.2)–(2.4), restated as the unchanged system in Section 6 | Identical prescribed scheme for each result. |
| Initial numerical map is the identity | Equation (2.2); Section 6.5 uses equality of the exact and numerical nodal interpolants at time zero | Identical initial condition. |
| Unique discrete solution with nondegenerate evolving elements through the specified interval | Theorem 2.2 and Proposition 4.1 give a fixed positive interval for the linear example; Theorem 6.1 and Section 6.5 give the whole prescribed interval for cubic elements | The linear interval is fixed before mesh refinement; cubic full-time existence and nondegeneracy are proved. |
| Uniform-in-time L2 convergence of the original closest-point lifted map, or an admissible counterexample | Theorem 2.2 and Section 5.3 give a positive liminf of the lifted map-error supremum; Theorem 6.1 gives C_T h^3 sqrt(1+abs(log h)) for the same map error | Original permitted negative alternative at degree 1; quantitative convergence at degree 3. |
| Separate conclusions for degrees 1, 2, 3 | Introduction and Remark 6.2 state degree 2 remains unresolved | Partial coverage only. |

The cubic argument controls a signed-distance-weighted relative volume
and a weakly tangent map energy. Equations (6.22)–(6.24) keep the current
area ratio distinct from the fixed reference measure. Equations
(6.35)–(6.38) retain the fourth power of the weak normal error and close
the two estimates. Section 6.5 supplies the continuation and lift arguments.

The paper also proves a cubic signed-distance error of order h^3. That shape
estimate is distinguished from the map estimate requested by the problem.
No result for a modified normal or a different MDR scheme is substituted.
The previously known k>=4 theorem of Gao, Li and Tang is background rather
than a premise that already settles k=3.

The quadratic discussion identifies a limitation of the present estimates.
It is neither a quadratic counterexample nor a proof of quadratic convergence.
The package is submitted for mathematical review, not as evidence of prior
maintainer acceptance or formal verification.
