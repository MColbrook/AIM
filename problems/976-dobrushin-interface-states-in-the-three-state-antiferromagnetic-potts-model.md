# 976. Dobrushin interface states in the three-state antiferromagnetic Potts model

**Area:** Probability, statistical mechanics and phase transitions
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Give $`\mathbb Z^d`$ its nearest-neighbour graph and colour each vertex with a value in $`\{0,1,2\}`$. For a finite set $`\Lambda`$, boundary configuration $`\tau:\mathbb Z^d\to\{0,1,2\}`$, and finite inverse temperature $`\beta>0`$, let
```math
\mu^\tau_{\Lambda,\beta}(\sigma)
 =\frac{1}{Z^\tau_{\Lambda,\beta}}
   \exp\bigl(-\beta H_\Lambda(\sigma)\bigr),
\qquad
H_\Lambda(\sigma)=
 \sum_{\substack{\{x,y\}:|x-y|_1=1\\
                  \{x,y\}\cap\Lambda\ne\varnothing}}
       \mathbf1_{\{\sigma(x)=\sigma(y)\}},
```

on configurations agreeing with $`\tau`$ outside $`\Lambda`$. The positive energy penalty for equal neighbouring colours gives the antiferromagnetic convention.

A vertex is even or odd according to the parity of the sum of its coordinates. A domain is a finite, nonempty, connected set with connected complement; its external vertex boundary $`\partial^\circ\Lambda`$ consists of vertices outside it adjacent to it. Set
```math
\Pi=\{x:x_1\ge0\},
\qquad
\tau(x)=
\begin{cases}
0,&x\in\Pi,\\
1,&x\notin\Pi .
\end{cases}
```

Consider domains $`\Lambda_n\supseteq[-n,n]^d\cap\mathbb Z^d`$ satisfying
```math
\partial^\circ\Lambda_n\cap\Pi\subseteq\mathrm{Even},
\qquad
\partial^\circ\Lambda_n\setminus\Pi\subseteq\mathrm{Odd}.
```


**For sufficiently large $`d`$ and sufficiently large finite $`\beta`$, do these finite-volume measures converge weakly, along the full sequence, to an infinite-volume Gibbs measure which is not invariant under any parity-preserving translation moving $`\Pi`$?**

More explicitly, the temperature threshold may depend on $`d`$. For each admissible sequence, the proposed limit $`\mu`$ should satisfy the Dobrushin–Lanford–Ruelle specification determined by the finite-volume laws above, and
```math
\mu\circ T_z^{-1}\ne\mu
\quad\text{whenever}\quad
z\in\mathbb Z^d,\quad \sum_i z_i\in2\mathbb Z,\quad z_1\ne0,
\qquad (T_z\sigma)(x)=\sigma(x-z).
```

Weak convergence means convergence of every finite-coordinate marginal. The question asks for a full limit and this symmetry breaking, beyond the subsequential Gibbs limits supplied by compactness. No quantitative fluctuation bound is imposed here.

## Application

An affirmative answer would construct an equilibrium interface separating an even-zero phase from an odd-one phase in an antiferromagnetic material model. This tests how entropy-driven ordering can stabilize an interface when many different microscopic configurations have the same minimal energy.

## Known results and scope

Feldheim–Spinka construct six extremal bulk Gibbs phases at low temperature in high dimension. Their Theorem 1.3 proves full convergence for homogeneous even- or odd-colour boundary conditions. The mixed half-space boundary conditions above are their explicit remaining conjecture.

Peled–Spinka's later general results establish bulk ordering and classify periodic maximal-pressure Gibbs states, including the low-temperature antiferromagnetic Potts model. Their Theorem 1.3 assumes periodicity under a full-rank sublattice, and §10.3 explicitly includes that assumption in the definition of maximal pressure. The requested interface state would fail periodicity in the normal direction, so this classification does not answer the question.

The planar ferromagnetic Potts/random-cluster interface limits and tree reconstruction results concern different models, dimensions or limiting objects. They do not construct the high-dimensional antiferromagnetic interface above. The nearby old conjecture about bulk ordering with four or more colours has later positive results and is not the target of this entry.

## References

1. O. N. Feldheim and Y. Spinka, *Long-range order in the 3-state antiferromagnetic Potts model in high dimensions*, Journal of the European Mathematical Society **21** (2019), no. 5, 1509–1570, [DOI](https://doi.org/10.4171/JEMS/866). Primary question and definitions: [arXiv:1511.07877v3](https://arxiv.org/pdf/1511.07877v3), pp. 2–3 and 6; known homogeneous-boundary convergence: Theorem 1.3, p. 4.
2. R. Peled and Y. Spinka, *Long-range order in discrete spin systems*, [arXiv:2010.03177v3](https://arxiv.org/pdf/2010.03177v3) (2026), Theorems 1.1–1.3, pp. 2–3, antiferromagnetic Potts application pp. 4–5, and the periodicity convention p. 81.

## Status review


**Known cases:** Full-sequence interface limits for three-state high-dimensional antiferromagnetic Potts are required. Homogeneous periodic phases and planar ferromagnetic order-disorder interface results do not establish these mixed boundaries.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Full-sequence interface limits for three-state high-dimensional antiferromagnetic Potts are required. Homogeneous periodic phases and planar ferromagnetic order-disorder interface results do not establish these mixed boundaries.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The eligible original model and question, selected current main statements, official version histories, current public AIM/OpenAI metadata, and the closest all-status AIM/FURTHER targets were checked on 24 October 2026. The bounded current and announcement searches found no matching solution.

The author website could not be read directly because the connection closed; indexed primary publication descriptions were inspected separately. Prove2Me checking was limited to target navigation on its public homepage. No complete proof verification, publisher-native byte parity or whole-site completeness is claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-42a9e85470bde131**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
