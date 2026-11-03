# 906. Does every reflexive-space $`AC(\sigma)`$ operator admit a $`BV(\sigma)`$ functional calculus?

**Area:** Operator theory and Banach algebras
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\sigma\subset\mathbb C`$ be a nonempty compact set. Use the Ashton–Doust algebras $`BV(\sigma)`$ and $`AC(\sigma)`$: $`BV(\sigma)`$ consists of complex functions of finite planar variation, with the variation defined using finite ordered point lists and their maximum line-crossing count; $`AC(\sigma)`$ is the closure of restrictions of complex-coefficient polynomials in the two real coordinates in the $`BV(\sigma)`$ norm [1, §2].

Let $`X`$ be a reflexive complex Banach space, $`T\in B(X)`$, and $`\lambda(z)=z`$ on $`\sigma`$. By definition, $`T`$ is an $`AC(\sigma)`$ operator if there exists a bounded unital Banach-algebra homomorphism

```math
\Psi:AC(\sigma)\longrightarrow B(X),\qquad \Psi(\lambda)=T.
```


**Must $`T`$ also admit a $`BV(\sigma)`$ functional calculus?** Equivalently, must there exist a bounded unital homomorphism $`\Theta:BV(\sigma)\to B(X)`$ with $`\Theta(\lambda)=T`$? This is the question on [1, printed p. 1591], with the definition of an $`AC(\sigma)`$ operator pinned in [2, Definition 4.1]. It asks for a calculus for $`T`$; it does not assert that every initially selected $`\Psi`$ must extend, or require $`\sigma`$ to equal the spectrum of $`T`$.

## Application

A $`BV(\sigma)`$ calculus would assign bounded operators to a larger, idempotent-rich class of functions of $`T`$. In the known real-interval and unit-circle settings, such extensions support spectral representations and functional calculations beyond absolutely continuous functions [1, §5; 2, §1]. The question asks whether this feature persists for arbitrary compact planar $`\sigma`$ on reflexive spaces.

## Known results and scope

For real spectra on reflexive spaces, Doust and Terauds [3] prove the classical $`AC`$-to-$`BV`$ extension. The source paper's Theorem 5.1 proves the planar assertion when $`\sigma`$ belongs to the class of polygonally inscribed curves and is homeomorphic to the unit circle [1, pp. 1591–1592]. Neither result treats every compact planar $`\sigma`$.

Doust and Stoneham [4] later obtain an $`AC(\sigma(T))`$ calculus under restrictions on the spectrum of $`T`$; their paper explicitly leaves removal of those geometric restrictions as a challenge. This concerns changing the *domain* of the absolutely-continuous calculus and is distinct from obtaining a $`BV(\sigma)`$ calculus for arbitrary $`\sigma`$. No general result settling the present question was found in the bounded current search.

## References

1. S. Al-shakarchi and I. Doust, [*Isomorphisms of $`BV(\sigma)`$ Spaces*](https://files.ele-math.com/articles/oam-15-101.pdf), *Operators and Matrices* **15** (2021), no. 4, 1581–1596, §2, §5 and Theorem 5.1. [DOI](https://doi.org/10.7153/oam-2021-15-101).
2. B. Ashton and I. Doust, [*$`AC(\sigma)`$ Operators*](https://www.theta.ro/jot/archive/2011-065-002/2011-065-002-003.pdf), *Journal of Operator Theory* **65** (2011), no. 2, 255–279, Definition 4.1.
3. I. Doust and V. Terauds, [*Extensions of an $`AC(\sigma)`$ functional calculus*](https://arxiv.org/pdf/0803.2131v1), *Journal of Mathematical Analysis and Applications* **362** (2010), no. 1, 100–106. [DOI](https://doi.org/10.1016/j.jmaa.2009.10.001).
4. I. Doust and A. Stoneham, [*Tietze type extensions for absolutely continuous functions in the plane*](https://arxiv.org/pdf/2308.04628v1), *Studia Mathematica* **285** (2025), 203–234, §11. [DOI](https://doi.org/10.4064/sm230808-29-10).

## Status review


**Known cases:** The real-spectrum extension and polygonally inscribed Jordan-curve theorem impose spectral geometry. Later Tietze-type results change the domain of an AC calculus; they do not supply some BV calculus for every planar compact sigma on every reflexive space.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The real-spectrum extension and polygonally inscribed Jordan-curve theorem impose spectral geometry. Later Tietze-type results change the domain of an AC calculus; they do not supply some BV calculus for every planar compact sigma on every reflexive space.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [independent bounded source audit](../FURTHER_problems/_tracking/journal0881-j063-ac-bv-and-doubling-fock-status-audit-2026-10-23.json) and [coordinator review](../FURTHER_problems/_tracking/j063-ac-bv-calculus-coordinator-audit-2026-10-23.json) record the original question and definitions, the later restricted results, bounded proof and announcement searches, and the AIM/FURTHER duplicate check. The cited 2023 thesis was not fully inspected, so the status statement is appropriately bounded. The original review is a selected body passage, not complete article or journal coverage.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6488fd98883e30b1**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
