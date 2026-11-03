# 725. Logarithmic comparison and strong Euler homogeneity of free divisors

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a complex analytic manifold of finite complex dimension $`n`$, and let $`D\subset X`$ be a reduced analytic hypersurface. Assume $`D`$ is a **free divisor**: the sheaf of logarithmic vector fields
```math
\mathrm{Der}_X(-\log D)
 =\{\delta:\delta(f)\in(f)\}
```

is locally free of rank $`n`$, where $`f`$ is a reduced local defining equation.

Write $`\Omega_X^\bullet(*D)`$ for meromorphic differential forms with poles along $`D`$, equipped with the exterior differential. Its logarithmic subcomplex consists locally of forms $`\eta`$ for which both $`f\eta`$ and $`f\,d\eta`$ are holomorphic. Suppose the inclusion
```math
\Omega_X^\bullet(\log D)\longrightarrow\Omega_X^\bullet(*D)
```

is a quasi-isomorphism of complexes of sheaves on $`X`$, namely the logarithmic comparison theorem (LCT).

Must $`D`$ be **strongly Euler-homogeneous**? Explicitly, for every $`p\in D`$, must there exist a holomorphic vector-field germ
```math
\delta\in\mathfrak m_{X,p}\mathrm{Der}_{X,p},
 \qquad \delta(f)=f?
```

Here $`\mathfrak m_{X,p}`$ is the maximal ideal of germs vanishing at $`p`$; thus the vector field must vanish at $`p`$. The property does not depend on the chosen reduced equation.

LCT is assumed on a neighbourhood, as a sheaf statement. A quasi-isomorphism at a single stalk is not substituted. There is no assumption of isolated singularities, linearity or Koszul freeness, and no converse is requested.

## Application

LCT allows logarithmic differential forms to replace meromorphic forms in studying the cohomology of a complex hypersurface complement. The question asks whether this comparison forces a local scaling symmetry of its defining equation, including at non-isolated singularities.

## References

- A. del Valle Rodríguez, *On strong Euler-homogeneity and Saito-holonomicity for complex hypersurfaces. Applications to a conjecture on free divisors*, **Journal of the London Mathematical Society** 113 (2026), e70451. [Published article](https://doi.org/10.1112/jlms.70451); [accepted-author version, arXiv:2504.21829v5](https://arxiv.org/html/2504.21829v5), Definitions 1.1 and 1.4, Conjecture 1.2, Section 6 and Corollary 7.3.

## Status review


**Known cases:** The inspected current v5 retains Conjecture 1.2 and proves dimensions up to four, weak Koszul freeness, punctured-neighborhood cases and dimension-five linear free divisors. Counterexamples to all linear divisors satisfying LCT do not refute the conditional implication.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The inspected current v5 retains Conjecture 1.2 and proves dimensions up to four, weak Koszul freeness, punctured-neighborhood cases and dimension-five linear free divisors. Counterexamples to all linear divisors satisfying LCT do not refute the conditional implication.

Additional comparison sources: [comparison source 1](https://doi.org/10.1112/jlms.70451); [comparison source 2](https://arxiv.org/html/2504.21829v5). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked **30 October 2026**. The accepted 2026 article explicitly retains the general conjecture. It covers ambient dimensions $`n\leq4`$, weakly Koszul-free divisors in arbitrary dimension, divisors already strongly Euler-homogeneous outside a discrete set, and linear free divisors in dimension five. The unrestricted case remains the target here.

The same article's counterexamples to the assertion that *all* linear free divisors satisfy LCT do not refute this conditional implication. No matching general resolution or complete announcement was located in the current searches. Semantic checks against the current AIM/OpenAI all-status corpus and the developing collection found no equivalent target. These are dated checks, not a guarantee against an undiscovered result.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e8b8511ca4f01ffc**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
