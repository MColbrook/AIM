# 780. The Montesinos–Morton conjecture for fibered links

**Area:** Geometric topology and open book decompositions
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

An oriented link $`L\subset S^3`$ is **fibered** if its complement fibers over the circle and the closure of each fiber is a Seifert surface whose boundary orientation agrees with that of $`L`$.

A **braid axis** for a link $`B\subset S^3`$ is an unknot disjoint from $`B`$ such that $`B`$ meets every disk page of the standard open book with that unknot as binding transversely and positively.

Is it true that for every oriented fibered link $`L\subset S^3`$, there exist a finite-degree **simple branched covering**
```math
\pi:S^3\longrightarrow S^3
```

with branch link $`B`$, and two braid axes $`\alpha,\beta`$ for this same $`B`$, such that
```math
\pi^{-1}(\alpha)=L,\qquad
\pi^{-1}(\beta)\text{ is an unknot}?
```

The first equality is understood up to oriented isotopy. A degree-$`n`$ cover is simple when each branch meridian has transposition monodromy: locally there is one two-sheeted branch and all other sheets are unbranched. The degree may depend on $`L`$.

The axes are not required to form a Hopf link. The question asks for both lifting properties in one covering. A covering realizing only the first lift is already known to exist.

## Application

Open books encode three-manifolds by surfaces and their monodromy. The conjecture asks whether every fibered link can be connected to the unknot by changing braid axes within one simple branched covering. This would give a constructive topological strengthening of the Hopf plumbing and deplumbing description of fibered links.

## Known progress

Ordinary Harer Hopf plumbing and deplumbing is a theorem. The present conjecture requires the additional symmetry induced by a fixed simple branched covering; Harer's theorem by itself does not supply it.

The corrected 2023 version retains Conjecture 2.14. Bode and Hsueh restate the exact target as Conjecture A in 2025. Their stronger Conjecture B asks whether every fibered link binds a braided open book, and their Conjecture C concerns mutual arc presentations. The proved implications are $`C\Rightarrow B\Rightarrow A`$.

Their Theorem 1.3 establishes the stronger Property C for canonically fibered links, whose fiber surfaces arise from Seifert's algorithm. They also obtain examples through connected sums and cabling. These partial results do not cover every fibered link.

## References

1. B. Bode, *Braided open book decompositions in $`S^3`$*, [arXiv:2111.05187v1](https://arxiv.org/abs/2111.05187v1), Conjecture 2.14, native p. 15; [corrected version v3](https://arxiv.org/abs/2111.05187v3), Definition 2.11 and Conjecture 2.14, native pp. 14–15. *Revista Matemática Iberoamericana* **39**(6) (2023), 2187–2232, [doi:10.4171/RMI/1429](https://doi.org/10.4171/RMI/1429).
2. B. Bode and C.-S. Hsueh, *Mutual arc presentations and braided open books*, [arXiv:2511.21837v1](https://arxiv.org/abs/2511.21837v1), Conjectures A–C, Proposition 1.2 and Theorem 1.3, native pp. 1–2.

## Status review


**Known cases:** The 2026 seminar and current braided-open-book paper cover canonically fibered links only. The withdrawn original theorem is not used. The required two lifting properties in a single simple branched covering are not implied by realizing one fibered-link lift.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2026 seminar and current braided-open-book paper cover canonically fibered links only. The withdrawn original theorem is not used. The required two lifting properties in a single simple branched covering are not implied by realizing one fibered-link lift.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2111.05187v1); [comparison source 2](https://arxiv.org/abs/2111.05187v3); [comparison source 3](https://doi.org/10.4171/RMI/1429); [comparison source 4](https://arxiv.org/abs/2511.21837v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 24 October 2026 against the original conjecture, its corrected version, current same-author primary statements, and all-status AIM/FURTHER records, the OpenAI announcement catalogue, and bounded Prove2Me results. No matching proof, counterexample or announced resolution was located in the bounded searches. The original v1 Theorem 1.5 was withdrawn and is not used as known progress here. Selected native windows, version identities and comparisons are retained; no exhaustive literature or whole-paper proof audit is claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-34fc2bfbd917be54**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
