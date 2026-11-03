# 910. Weak-star maximal left ideals of Hermitian group measure algebras

**Area:** Operator theory and abstract harmonic analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`G`$ be a locally compact group with fixed left Haar measure. Write $`L^1(G)`$ for its convolution Banach algebra, and $`M(G)=C_0(G)^*`$ for the convolution algebra of finite complex regular Borel measures, with total variation norm. Here $`C_0(G)`$ consists of continuous functions vanishing at infinity. Equip $`M(G)`$ with the weak-star topology $`\sigma(M(G),C_0(G))`$.

Assume $`G`$ is **Hermitian**: every self-adjoint element of $`L^1(G)`$ has real spectrum, using the unitization when necessary. The involution is
```math
f^*(t)=\Delta(t^{-1})\overline{f(t^{-1})},
```

where $`\Delta`$ is the modular function.

Let $`\pi:G\to\mathcal U(\mathcal H_\pi)`$ be a strongly continuous irreducible unitary representation. Say that $`\pi`$ **vanishes at infinity** if
```math
g\longmapsto\langle\pi(g)\xi,\eta\rangle\in C_0(G)
\quad\text{for every }\xi,\eta\in\mathcal H_\pi.
```

Define $`\pi(\mu)`$ by weak integration against $`\mu`$. For a unit vector $`\xi\in\mathcal H_\pi`$, set
```math
I_{\pi,\xi}=\{f\in L^1(G):\pi(f)\xi=0\},
\qquad
J_{\pi,\xi}=\{\mu\in M(G):\pi(\mu)\xi=0\}.
```

A proper left ideal $`I\subset L^1(G)`$ is modular if there is $`u\in L^1(G)`$ such that $`f-f*u\in I`$ for every $`f\in L^1(G)`$. A maximal modular left ideal is a maximal proper left ideal which is modular.

Are the weak-star closed maximal proper left ideals of $`M(G)`$ precisely the ideals $`J_{\pi,\xi}`$ for which $`\pi`$ vanishes at infinity and $`I_{\pi,\xi}`$ is maximal modular in $`L^1(G)`$? Maximality is among all proper left ideals, rather than only among weak-star closed ones. No uniqueness of the representing pair is asserted.

This is White's Conjecture 1.1. One implication is known: every pair satisfying these conditions gives a weak-star closed maximal left ideal. The unresolved general direction asks whether every weak-star closed maximal left ideal admits such a representation with all coefficients vanishing at infinity. The question does not assert existence of these ideals for every $`G`$.

## Application

The classification would relate the weak-star ideal structure of convolution measure algebras to decay of irreducible representation coefficients. It extends the compact-group description toward general Hermitian groups and connects operator-algebra ideal structure with asymptotic harmonic analysis.

## References

- [Jared T. White, *The ideal structure of measure algebras and asymptotic properties of group representations*, arXiv:2106.07526v1 (14 June 2021)](https://arxiv.org/abs/2106.07526v1), Conjecture 1.1: the eligible original statement.
- [Revised version v2 (5 October 2022)](https://arxiv.org/pdf/2106.07526v2), pp. 1, 3–5, 8–11 and 20: definitions, Corollaries 4.4 and 4.6, Theorem 4.11 and Section 8. Published in *Journal of Operator Theory* **91** (2024), no. 2, 373–398; [DOI 10.7900/jot.2022apr13.2389](https://doi.org/10.7900/jot.2022apr13.2389).

## Status review


**Known cases:** The current primary measure-algebra classification is for certain Hermitian groups, adding coefficient-vanishing modulo projective-kernel hypotheses. Two-sided-ideal, non-Wiener-group and weighted-bidual results do not provide the full weak-star maximal-left-ideal classification for every Hermitian locally compact group.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current primary measure-algebra classification is for certain Hermitian groups, adding coefficient-vanishing modulo projective-kernel hypotheses. Two-sided-ideal, non-Wiener-group and weighted-bidual results do not provide the full weak-star maximal-left-ideal classification for every Hermitian locally compact group.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The revised primary source retains the conjecture and explicitly asks in Section 8 whether it holds for every Hermitian locally compact group. Theorem 4.11 proves the classification under the additional assumption that every irreducible representation vanishes at infinity modulo its projective kernel. This covers several classes, including connected nilpotent Lie groups and Euclidean rigid motion groups. The weighted classification in Theorem 4.12 concerns a different algebra with further hypotheses.

The author's current publication list and selected statements in newer papers on weak-star simplicity (2024), non-Wiener groups (2026), and radicals of Beurling-algebra biduals (2026) were checked. Those statements concern two-sided ideals, nonamenable groups, or weighted bidual algebras; none states the general classification above. The publisher's metadata and DOI were verified. Its PDF returned HTTP 403; the revised arXiv PDF and native HTML were readable.

Dated searches covered the exact source title, conjecture number, author, weak-star maximal left ideals, Hermitian locally compact groups, later proofs and counterexamples, and indexed Prove2Me results. A fresh OpenAI Math overview inspection found no matching measure-algebra result. These bounded searches do not certify that no solution exists.

The all-status AIM and FURTHER comparison returned matrix inequalities, complex Hermitian geometry, inverse problems, fracture estimates and other targets involving different mathematical objects. No equivalent measure-algebra classification was located among the matched records. The independent review checked the original and revised source statements, the newer works with different ideal classes, all matched duplicate targets, and the final delta through all 738 existing findings.

Independent admission evidence: [source and scope](../FURTHER_problems/_tracking/white-measure-algebra-independent-peer-2026-10-23.json), [duplicates](../FURTHER_problems/_tracking/white-measure-algebra-coordinator-duplicate-review-2026-10-23.json), [current searches](../FURTHER_problems/_tracking/white-measure-algebra-current-resolution-search-2026-10-23.json), [announcements](../FURTHER_problems/_tracking/white-measure-algebra-announcements-and-catalogues-2026-10-23.json) and [source versions](../FURTHER_problems/_tracking/white-measure-algebra-eligibility-and-source-versions-2026-10-23.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-80416c50b77266e1**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
