# Comparison with AIM problem 158

The [original problem](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/158-network-multiplicity-one.md) asks whether every self-similarly shrinking tangent at an interior point of the first finite singular time has embedded support and unit arclength multiplicity. [Theorem 1 and its proof](paper/article.pdf) give a negative answer by constructing one admissible flow with a weight-two tangent.

| Original requirement | Where the paper addresses it |
| --- | --- |
| Smooth embedded finite network in a bounded smooth strictly convex planar domain | Theorem 1 and §2.1 choose a single smooth compatible initial network in a disk. Figure 1 specifies its topology. |
| Interior triple junctions at 120 degrees, fixed boundary endpoints and curvature-driven normal velocity | Sections 2.1–2.2 construct six triple junctions and four fixed endpoints, apply regular network flow existence and preserve the graph geometry along that evolution. |
| First finite singular time at an interior point | The cell areas prescribe time 1/2. Sections 3–4 trap the actual evolving network and rule out earlier singularities, including simultaneous collapse of the connectors while the cells still have positive area. Section 5 locates the singularity at the origin. |
| Parabolic rescalings at negative times and a self-similarly shrinking limit | Theorem 1 and §5 identify the local varifold limit for every dilation sequence and each negative time in the question. The time dependence is exactly the shrinker dilation in Theorem 1. |
| Multiplicity retained by taking arclength-varifold limits | Section 5 obtains convergence of positions and slopes for each exterior branch. On each open exterior ray two original branches contribute one copy of arclength apiece. The two lens arcs and the diameter have weight one. This violates the unit-multiplicity clause. |

The proof uses the ordinary symmetric lens of Schnürer et al. to identify the bounded arcs in the limit. The classical lens flow has two junctions and one bounded cell. The construction here uses two cells and the first-singular-time proof in §§3–4. The compactness and small-density regularity used in §4.1 are Proposition 8.17 and Corollaries 9.5–9.6 of Mantegazza, Novaga, Pluda and Schulze, in the cited version. [Ordinary lens](https://arxiv.org/pdf/0711.1108v1) [Network flow monograph](https://arxiv.org/pdf/1611.08254v4)

## Review status

This is an analytic proof claim. AI tools assisted with developing, checking and writing the argument. One AI reader and one AI referee reviewed the same earlier draft in separate contexts with access to a shared workspace and briefings about the proof topics. The revision clarified the fixed-area second variation and the use of two good slices and uniform graphical intervals in the proof of the first singular time. Independent human review remains outstanding.
