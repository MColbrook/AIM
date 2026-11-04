# AIM 639: target comparison

Target revision: `c4036871b0bf15cbc83e79c780b7191bcbb2cfed`. See [statement.md](statement.md).

The target asks for a two-sided order uniform jointly in n and delta, for adaptive continuous bounded queries, adversarial errors and arbitrary history dependence.

Writing L=log2(1/delta), the manuscript proves the upper bound 256/[L log2(1+2^n/L)]. Query ranges, noise separation, fixed-history continuity, integer budgets and the ellipsoid tail are accounted for. Existing lower bounds match for L<=2^(n/2) and L>=2^n. Around L~2^n/n the remaining ratio can grow like n/log n. Thus the joint order remains unresolved in the transition; the entry is Partially resolved.
