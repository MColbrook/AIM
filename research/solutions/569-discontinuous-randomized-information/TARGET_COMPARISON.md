# AIM 569: target comparison

Target revision: `c4036871b0bf15cbc83e79c780b7191bcbb2cfed`. See [statement.md](statement.md).

The target permits incomplete normed input spaces and continuous nonlinear maps. It asks for equality of the optimal randomized errors for continuous and arbitrary algebraic linear information, with finite expected budgets and joint output/count measurability.

On ell1 with the inherited ell2 norm, S(x)=||x||_2^2 has continuous-information error exactly 1/2 at every finite budget. One fair-sign algebraic query gives RMS error at most sqrt(6)-2<1/2. The query sum and output are jointly Borel. The input is incomplete, so automatic continuity for a Banach domain does not apply. This counterexample resolves the universally quantified question negatively, without settling a Banach-only variant.
