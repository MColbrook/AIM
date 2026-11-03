# 863. Stein fillability of all sufficiently large surgeries on a knot

**Area:** Contact and symplectic topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`K\subset S^3`$ be any smooth knot. For a rational slope $`r=p/q`$, in lowest terms with $`q>0`$, let $`S^3_r(K)`$ denote smooth Dehn surgery in the usual meridian–Seifert-longitude framing: the meridian of the attached solid torus is identified with $`p\mu+q\lambda`$.

Does there exist a finite real number $`R_K`$ such that **for every rational $`r\ge R_K`$**, the oriented three-manifold $`S^3_r(K)`$ admits a positive, cooriented Stein fillable contact structure?

Here Stein fillability means that the contact manifold is the oriented, strictly pseudoconvex boundary of a compact Stein domain of complex dimension two, with its complex-tangency contact planes. The contact structure and its Stein filling may depend on $`r`$. No Legendrian representative, contact-surgery construction, or topology of the filling is prescribed.

Equivalently, is the source's Stein fillable coefficient
```math
\mathrm{Sfc}(K)=\inf\{a\in\mathbb Q\cup\{\infty\}:a\ge\mathrm{TB}(K),
\ S^3_r(K)\text{ bounds a Stein domain for every rational }r\ge a\}
```

finite for every knot? Here $`\mathrm{TB}(K)`$ is the maximal Thurston–Bennequin invariant among Legendrian representatives in the standard contact three-sphere. The first formulation avoids any convention for the infimum when no finite threshold exists.

## Application

Dehn surgery constructs closed three-manifolds from knots. This question asks whether the large positive part of every knot's surgery family eventually bounds complex Stein surfaces. A positive answer would imply the high surgery conjecture about existence of tight contact structures; tightness alone does not imply Stein fillability.

## Known progress

The source proves the assertion for several knot families, including torus knots and their connected sums, certain closed three-braid L-space knots, specified two-bridge knots, and a family of pretzel knots (Theorems 1.13–1.16). Its accepted 2025 version retains Question 1.17 and the equivalent Question 4.5.

Mark and Tosun characterize when a **specified positive contact surgery** on a Legendrian representative yields a weakly fillable contact structure. Their obstructions restrict contact structures obtained by that operation. They do not exclude the existence of a different Stein fillable contact structure on the underlying smooth surgery manifold, as requested here.

## References

1. F. Ding, Y. Li and Z. Wu, *Nonexistence and existence of fillable contact structures on 3-manifolds*, [arXiv:2111.02151v1](https://arxiv.org/abs/2111.02151v1), Question 1.17, native p. 5; [accepted version v3](https://arxiv.org/abs/2111.02151v3), Questions 1.17 and 4.5 and Definition 1.19, native pp. 5–6 and 29. *Asian Journal of Mathematics* **28**(5) (2024), 617–652, [doi:10.4310/AJM.250225041731](https://doi.org/10.4310/AJM.250225041731).
2. T. E. Mark and B. Tosun, *Fillable contact structures from positive surgery*, [author-hosted PDF](https://bpb-us-e2.wpmucdn.com/sites.ua.edu/dist/8/406/files/2024/10/mark-tosun-fillable_contact_structures_from_positive_surgery.pdf), Theorem 1.1, the definition immediately following it, and Corollary 1.3, native pp. 1–2; [arXiv record](https://arxiv.org/abs/2301.10122).

## Status review


**Known cases:** Positive contact-surgery fillability criteria impose conditions on a Legendrian representative or a Lagrangian disk. They do not show that every sufficiently large rational surgery on every smooth knot admits some Stein-fillable structure. Known selected knot families leave the universal threshold question.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Positive contact-surgery fillability criteria impose conditions on a Legendrian representative or a Lagrangian disk. They do not show that every sufficiently large rational surgery on every smooth knot admits some Stein-fillable structure. Known selected knot families leave the universal threshold question.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 24 October 2026 against the eligible question, the latest accepted version, primary positive-contact-surgery comparison statements, and all-status AIM/FURTHER records, the OpenAI announcement catalogue, and bounded Prove2Me results. No matching proof, counterexample or announced resolution was located in the bounded current searches. Selected native windows and explicit scope comparisons are retained; no exhaustive literature or whole-paper proof audit is claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f3988dcb4c4033da**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
