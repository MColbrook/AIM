# 846. Maximal extensions of fine moduli spaces of coherent sheaves

**Area:** Complex algebraic geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix a smooth irreducible projective complex variety $`X`$, a very ample line bundle on $`X`$, a rank $`r\ge0`$, and Chern classes. Consider nonempty classes $`\mathcal S`$ of isomorphism classes of coherent sheaves with these invariants. Call $`\mathcal S`$ **open** if, in every flat algebraic family with those invariants, the locus of fibers belonging to $`\mathcal S`$ is Zariski open.

A **global fine moduli variety** for $`\mathcal S`$ means an integral algebraic variety $`M`$ with a coherent sheaf $`\mathcal E`$ on $`M\times X`$, flat over $`M`$, such that:

1. Its fibers classify $`\mathcal S`$ bijectively on closed points.
2. Every flat family $`\mathcal F`$ of members of $`\mathcal S`$ over an algebraic variety $`T`$ induces a morphism $`f:T\to M`$. Around each point of $`T`$, the family $`\mathcal F`$ is isomorphic to the pullback $`(f\times\mathrm{id}_X)^*\mathcal E`$.

The family $`\mathcal E`$ exists globally on $`M\times X`$; the pullback identifications are only required Zariski-locally on $`T`$. Use the source's category of integral algebraic varieties, with the usual finite-type and separated conventions.

**Does every open class $`\mathcal S`$ admitting a global fine moduli variety lie in a maximal such open class $`\mathcal S_{\max}`$, with the same $`X`$, rank and Chern classes?** Here maximal means that no strictly larger open class admits a global fine moduli variety.

The parameter variety need not be proper or projective, and the sheaves need not be stable or simple. Maximality is inclusion of sheaf classes. The separately asked existence of an infinite strictly increasing chain is not asserted equivalent to this question. An increasing union need not itself have a finite-type fine moduli variety.

## Application

Fine moduli varieties organize algebraic families through a universal sheaf. The question asks whether every such family can be enlarged to a maximal parameter space, including families outside the usual stability constructions.

## References

1. J.-M. Drézet, *Variétés de modules alternatives*, Annales de l'Institut Fourier 49(1) (1999), 57–139, [DOI](https://doi.org/10.5802/aif.1669). The published introduction, Question 1, and Section 2.6 ask the problem. The [author revision](https://webusers.imj-prg.fr/~jean-marc.drezet/papers/altern.pdf), Question 1 on p. 4, Definitions 3 and 5 on p. 7, and Section 2.6 on p. 13, retains the exact model and question.
2. J.-M. Drézet, *Exotic fine moduli spaces of coherent sheaves*, [author note](https://www.impan.pl/~pragacz/download/drezet1.pdf), Sections 2.1 and 5.1. Its terminology distinguishes locally defined families from a global universal family; its maximal examples do not give the general extension theorem.

## Status review


**Known cases:** Special maximal fine-moduli constructions do not imply that every open fine-moduli class has a maximal extension. Taking an increasing union need not preserve finite type or a global universal sheaf. No matching general extension theorem or counterexample was located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Special maximal fine-moduli constructions do not imply that every open fine-moduli class has a maximal extension. Taking an increasing union need not preserve finite type or a global universal sheaf. No matching general extension theorem or counterexample was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original question and its definitions were read directly and received a separate model check. Current searches for maximal-extension theorems, counterexamples and announced solutions found no matching complete resolution as of the check date. Later constructions on particular varieties or nonreduced multiple schemes do not establish the stated general extension claim.

All-status AIM/OpenAI entries and the developing collection were compared semantically. Numerical Chern-character questions, stability-condition constructions and cohomology of Higgs moduli spaces ask different questions. The [coordinating review](../FURTHER_problems/_tracking/B-AIF1669-maximal-fine-moduli-source-current-gate-20261029/ROOT-FINAL-GLOBAL-FINE-MAXIMAL-EXTENSION-PRIMARY-CURRENT-SEMANTIC-REVIEW.json) records the comparisons and access limits. The author revision and published article have different lengths; byte or whole-body parity is not claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d00c0c7438adaa8f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
