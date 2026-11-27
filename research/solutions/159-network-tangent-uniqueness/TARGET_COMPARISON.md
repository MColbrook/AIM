# AIM 159 statement comparison

[Fixed original statement](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/159-network-tangent-uniqueness.md) · [Manuscript](paper/article.pdf)

Theorem 1 gives the affirmative answer to the local weak arclength-varifold question in the original statement.

| Original requirement | Location and scope in the manuscript |
| --- | --- |
| Finite embedded planar network flow with only balanced $`120^\circ`$ triple junctions and fixed endpoints on the boundary of a smooth strictly convex domain | Theorem 1 and Section 1 use this class. Section 2.2 treats arbitrary finite embedded topology, including cycles, bridges, disconnected components and smooth loops. |
| Every interior finite-time singular point $`(x_0,T)`$ and the prescribed rescaling | Theorem 1 and (1.1) use $`(\Gamma(t)-x_0)/\sqrt{2(T-t)}`$ at the given point. The Gaussian boundary estimate in Section 2.1 keeps the fixed physical endpoints and uses their positive distance from $`x_0`$. |
| All local limits along arbitrary sequences $`t_i\uparrow T`$ | Section 4.3 gives convergence of spatial weights for all late times. Section 5.1 starts from an arbitrary convergent varifold subsequence. The short later comparison slices are auxiliary. Sections 5.3 and 5.4 bound the measure of projected coordinates where the starting slice fails to have the required count by the vanishing local curvature action, on each fixed regular patch. |
| Equality of the arclength varifolds, including all integer multiplicities | Section 2.3 obtains the integer arclength weight of a small-defect limit. Sections 5.4 and 5.5 retain the full intersection count at that multiplicity and identify every arbitrary-time angle measure with the single tangent line at the same weight. The final argument uses local weak precompactness. |
| Fixed ambient coordinates | Both the rescaling in (1.1) and the conclusions of Sections 4.3 and 5.5 use the original coordinate frame. |
| Full source class | The allowed networks include cycles and collapsing edges. Limits may be noncompact and have multiplicity greater than one. The argument allows arbitrary rates of curvature growth. Only simple material cycles are shown to have a positive rescaled length lower bound. The topology in the theorem is local weak convergence of varifolds. |

The closest cited uniqueness result is Pluda and Pozzetta's Theorem 1.1, for a nonempty compact nondegenerate limit on an endpoint-free graph. The manuscript supplies the exterior estimate, an energy that allows colliding vertices of its finite-dimensional representation, and the arbitrary-time tangent argument. Its other substantial external inputs are positive-time regularity, subanalytic gradient and selection results, and Angenent's scalar zero-number theorem. Their statements and uses are identified in Sections 1, 4 and 5.

The author-side review used an AI whole-proof check plus one AI reader and one AI referee on a frozen draft. These roles used separate evaluation assignments in a shared environment with some earlier task context. The author revised the manuscript once after those reports. This is a proposed solution.
