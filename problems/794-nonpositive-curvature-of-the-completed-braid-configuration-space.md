# 794. Nonpositive curvature of the completed braid configuration space

**Area:** Metric geometry and configuration spaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For an integer $`n\geq 4`$, let
```math
W_n=\{(z_1,\ldots,z_n)\in\mathbb C^n:z_i\ne z_j\text{ whenever }i\ne j\}.
```
Equip $`W_n`$ with the Riemannian metric induced by the standard Euclidean metric on $`\mathbb C^n`$. Give its universal cover $`\widetilde W_n`$ the lifted length metric: the length of a path is the Euclidean length of its projection to $`W_n`$, and distance is the infimum of lengths of connecting paths. Let
```math
\mathcal B_n=\overline{\widetilde W_n}
```
be the metric completion.

Is $`\mathcal B_n`$ a CAT(0) space for every $`n\geq4`$? Here CAT(0) means that the space is geodesic and that distances between points on the sides of any geodesic triangle are at most the corresponding distances in the Euclidean comparison triangle.

The prescribed lifted Euclidean length metric and its completion are part of the question. The configurations are ordered; there is no quotient by permutations in the definition of $`W_n`$.

## Application

This is a concrete question about nonpositive curvature in the geometry of configuration spaces. An affirmative answer would give geodesic convexity and unique geodesics in these particular completions. It is a special case of Allcock's conjecture for complexified finite Coxeter arrangements, obtained from the symmetric group acting by coordinate permutations. The surrounding work connects these curvature questions with topology of hyperplane complements and Artin groups. Those connections do not make the present metric assertion equivalent to asphericity of a classifying space or to existence of some CAT(0) group action.

## References

1. D. Allcock, *Completions, branched covers, Artin groups and singularity theory*, Duke Mathematical Journal **162** (2013), no. 14, 2645–2689. The statement checked here is Conjecture 1.4 on native pp. 3–4 of arXiv:1106.3459v1. [Eligible preprint, arXiv:1106.3459v1, 17 June 2011](https://arxiv.org/abs/1106.3459v1); [published DOI](https://doi.org/10.1215/00127094-2380977).
2. S. Alexander, V. Kapovitch and A. Petrunin, *Alexandrov geometry: foundations*, Question 12.17 in the [current author PDF](https://anton-petrunin.github.io/book/arXiv.pdf). This current book location is corroborating evidence; eligibility is established separately by reference 1.
3. D. Panov and A. Petrunin, *Ramification conjecture and Hirzebruch's property of line arrangements*, Compositio Mathematica **152** (2016), no. 12, 2443–2460, Conjecture 1.1 and Corollary 1.3 in the cited arXiv revision. [arXiv:1312.6856v5, 23 October 2016](https://arxiv.org/abs/1312.6856v5); [published DOI](https://doi.org/10.1112/S0010437X16007648).
4. D. Panov and A. Petrunin, *Braid spaces have no geodesic loops*, [arXiv:2610.27437v1, 20 October 2026](https://arxiv.org/abs/2610.27437v1), definition of the braid space, Conjecture 0.1, and Theorems 0.2–0.3.

5. C. Postel-Vinay, *The Geometric Combinatorics of k-Shuffle Braid Groups*, [arXiv:2610.28986v1, 20 October 2026](https://arxiv.org/abs/2610.28986v1), Sections 2.1–2.4 and Corollaries 4.34–4.35. This comparator concerns orthoscheme complexes and group actions.

## Status review


**Known cases:** The October Panov-Petrunin theorem proves no geodesic loops but explicitly retains the braid-space CAT(0) conjecture. Other braid-group CAT(0) actions, orthoscheme metrics and contractibility of Artin covers do not decide this lifted Euclidean metric completion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The October Panov-Petrunin theorem proves no geodesic loops but explicitly retains the braid-space CAT(0) conjecture. Other braid-group CAT(0) actions, orthoscheme metrics and contractibility of Artin covers do not decide this lifted Euclidean metric completion.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/1106.3459v1); [comparison source 2](https://doi.org/10.1215/00127094-2380977); [comparison source 3](https://anton-petrunin.github.io/book/arXiv.pdf); [comparison source 4](https://arxiv.org/abs/1312.6856v5); [comparison source 5](https://doi.org/10.1112/S0010437X16007648); [comparison source 6](https://arxiv.org/abs/2610.27437v1); [comparison source 7](https://arxiv.org/abs/2610.28986v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Review date: 23 October 2026. The primary statement, current status and closest possible duplicates have been checked independently.

The cases $`n\leq3`$ are known. The October 2026 paper still states the same CAT(0) assertion as Conjecture 0.1. Its no-geodesic-loops theorem is explicitly weaker than absence of geodesic digons and does not settle the CAT(0) question. The real four-string case attributed there to Charney concerns a particular subset, rather than all of the complex four-string braid space.

The bounded current search did not locate a proof, counterexample, or announced complete resolution of this prescribed-metric question. The closest OpenAI announcements concern contractibility of Artin Salvetti covers and a particular Artin group having no geometric CAT(0) action. Their native main statements were checked: neither asserts the required curvature conclusion or its negation for $`\mathcal B_n`$. The separate results on CAT(0) orthoscheme complexes for shuffle braid groups use another complex and metric; no identification with the present completion is supplied.

The review does not certify those announced proofs, every subsequent paper, or the whole Prove2Me catalogue. Exact source bytes, selected reading extents, duplicate comparisons and access limits belong in the accompanying owner and coordinator receipts. The 2019 first arXiv revision of the foundations book does not contain the literal braid-space target and is not used to establish its eligibility.

Review evidence: [independent primary review](../FURTHER_problems/_tracking/braid-space-independent-peer-2026-10-23.json), [all-status comparison](../FURTHER_problems/_tracking/braid-space-all-status-coordinator-review-2026-10-23.json), [current searches](../FURTHER_problems/_tracking/braid-space-current-resolution-search-2026-10-23.json), and [announcement/version checks](../FURTHER_problems/_tracking/braid-space-announcements-and-latest-versions-2026-10-23.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-66cfb0877ad9a674**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
