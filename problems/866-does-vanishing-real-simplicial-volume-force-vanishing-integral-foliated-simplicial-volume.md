# 866. Does vanishing real simplicial volume force vanishing integral foliated simplicial volume?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be an oriented closed connected aspherical $`n`$-manifold: its universal cover $`\widetilde M`$ is contractible. Its real simplicial volume is
```math
\|M\|=\inf\left\{\sum_j|a_j|:\ 
  \sum_j a_j\sigma_j\text{ is a finite real singular cycle representing }[M]_{\mathbb R}\right\}.
```


Set $`\Gamma=\pi_1(M)`$. A standard $`\Gamma`$-space $`\alpha:\Gamma\curvearrowright(X,\mu)`$ is a probability-measure-preserving action on a standard Borel probability space. Give $`L^\infty(X,\mathbb Z)`$ the right action $`(f\cdot\gamma)(x)=f(\gamma x)`$, and use the deck action on singular chains of $`\widetilde M`$. In the balanced chain complex
```math
C_*^\alpha(M)=L^\infty(X,\mathbb Z)\otimes_{\mathbb Z\Gamma}
 C_*(\widetilde M;\mathbb Z),
```

the integer fundamental class maps to a class $`[M]^\alpha`$ by the inclusion of constant functions.

For a finite reduced chain $`c=\sum_j f_j\otimes\sigma_j`$, with the $`\sigma_j`$ in distinct deck-transformation orbits, set
```math
|c|_1=\sum_j\int_X |f_j(x)|\,d\mu(x),\qquad
|M|^\alpha=\inf\{|c|_1:\ \partial c=0,\ [c]=[M]^\alpha\}.
```

The **integral foliated simplicial volume** is
```math
|M|=\inf_\alpha |M|^\alpha,
```

where the infimum runs over all standard $`\Gamma`$-spaces.

Must
```math
\|M\|=0\quad\Longrightarrow\quad |M|=0
```

hold for every such $`M`$?

The target is the infimum over actions. It does not assert that every parametrized norm vanishes. No residual-finiteness assumption on $`\Gamma`$ is imposed.

## Application

Integral foliated simplicial volume controls measured topological invariants, including $`L^2`$-Betti numbers. A positive answer would turn real-volume vanishing into stronger measured vanishing and, in particular, imply the corresponding zero-Euler-characteristic conclusion.

## Known progress

Löh, Moraschini and Sauer prove vanishing for smooth aspherical manifolds with an open amenable cover of multiplicity at most the dimension. Their Theorem 1.2 proves the stronger parametrized conclusion for every essentially free action in this restricted class. It does not settle Question 1.1 for arbitrary aspherical manifolds.

Bargagnati, Casali, Milizia and Moraschini's 2026 Corollary 1.5 gives vanishing for mapping tori over oriented closed connected aspherical prime three-manifolds, and for mapping tori over closed connected oriented hyperbolic manifolds of dimension at least three. These are additional restricted families.

The stable integral simplicial volume defined using finite covers is a different invariant. The source's separate Question 2.4 about that invariant includes residual finiteness; those conditions are not substituted into this problem.

## Status review


**Known cases:** Amenable-cover and mapping-torus results give restricted vanishing families. Scalar-curvature criteria in the OpenAI collection impose additional geometry and do not infer integral foliated vanishing solely from zero real simplicial volume. Stable integral volume over finite covers is a different invariant.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Amenable-cover and mapping-torus results give restricted vanishing families. Scalar-curvature criteria in the OpenAI collection impose additional geometry and do not infer integral foliated vanishing solely from zero real simplicial volume. Stable integral volume over finite covers is a different invariant.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original Question 1.1, the source's real and twisted-chain definitions, the latest v2 question, the published question and Definition 2.6, and the actual 2026 mapping-torus corollary were read. Current primary-source searches for full proofs, counterexamples and announcements, with bounded Prove2Me searches, found no matching general resolution on 24 October 2026.

All-status AIM/OpenAI and FURTHER checks distinguish the target from positive-volume motion-planning complexity, affine-manifold real-volume vanishing, amenable-normal-subgroup real-volume vanishing, and scalar-curvature inequalities. The existing [zero-real-volume Euler-characteristic question](537-does-zero-simplicial-volume-force-zero-euler-characteristic.md) is a related weaker conclusion; it does not state integral foliated volume vanishing. This review compares statements and scope, without certifying every cited proof.

## References

1. C. Löh, M. Moraschini and R. Sauer, [Amenable covers and integral foliated simplicial volume](https://arxiv.org/abs/2112.12223), eligible v1 and latest v2, Question 1.1, Theorem 1.2 and Definitions 2.1, 2.5–2.6. [Published article](https://nyjm.albany.edu/j/2022/28-47p.pdf), *New York Journal of Mathematics* **28** (2022), 1112–1136.
2. G. Bargagnati, A. Casali, F. Milizia and M. Moraschini, [Minimal volume entropy of mapping tori over 3-manifolds](https://doi.org/10.1007/s00208-026-03590-7), *Mathematische Annalen* **396**, article 59 (13 October 2026), introduction and Corollary 1.5.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f83d255cb4607980**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
