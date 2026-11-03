# 850. Must every analytic compactification of complex affine space be Moishezon?

**Area:** Complex geometry and meromorphic functions
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every integer $`n\ge1`$, let $`X`$ be a connected compact complex manifold of complex dimension $`n`$. Suppose a proper closed complex-analytic subset $`A\subset X`$ satisfies
```math
X\setminus A\simeq\mathbb C^n
```

biholomorphically. Must
```math
\mathrm{trdeg}_{\mathbb C}\mathcal M(X)=n,
```

where $`\mathcal M(X)`$ is the field of global meromorphic functions on $`X`$? Equivalently, must there be $`n`$ algebraically independent such functions? This is the Moishezon conclusion in [1, printed p.245].

The ambient space is smooth, while $`A`$ may be singular or reducible. “Analytic Zariski-open” means precisely the complement of a closed analytic subset, not an arbitrary open embedding. There is no Kähler, equivariance, smooth-boundary or second-Betti-number assumption. The conclusion does not assert that $`X`$ itself is projective.

## Application

The question asks whether attaching an analytic compact boundary to complex affine space always preserves maximal meromorphic function dimension. Local affine coordinates need not automatically extend meromorphically through the boundary, so this tests a global algebraicity property of the compactification.

## References

1. Jun-Muk Hwang and Dror Varolin, [*A compactification of $`(\mathbb C^*)^4`$ with no non-constant meromorphic functions*](https://www.numdam.org/item/10.5802/aif.1884.pdf), *Annales de l'Institut Fourier* **52** (2002), 245–253, conjecture and distinctions on printed pp.245–246. [DOI](https://doi.org/10.5802/aif.1884).
2. Chi Li and Zhengyi Zhou, [*Kähler compactification of $`\mathbb C^n`$ and Reeb dynamics*, published author-hosted text](https://sites.math.rutgers.edu/~cl1412/papers/Reeb.pdf), Introduction and Theorem1.1. [Published article](https://doi.org/10.1007/s00222-025-01377-2).

## Status review


**Known cases:** Smooth Kahler-boundary compactification and equivariant cases are restricted. Non-Moishezon compactifications of (C-star)^4 have a different open part, while nonprojective Moishezon compactifications still satisfy the requested conclusion. No full affine-space result was located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Smooth Kahler-boundary compactification and equivariant cases are restricted. Non-Moishezon compactifications of (C-star)^4 have a different open part, while nonprojective Moishezon compactifications still satisfy the requested conclusion. No full affine-space result was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Source [1] reports the dimension-two and equivariant cases as known; the cited proofs of those cases were not reread here. The directly inspected Theorem1.1 of [2] proves that a compactification with a smooth Kähler boundary is the standard pair $`(\mathbb P^n,\mathbb P^{n-1})`$. It does not settle the question for an arbitrary analytic boundary.

The non-Moishezon examples in [1] compactify $`(\mathbb C^*)^4`$, whose open part differs from $`\mathbb C^4`$. The paper also refutes a different statement about faithful additive-group orbits. Neither is a counterexample to the displayed conjecture. A nonprojective Moishezon example would also not refute it.

Bounded current and announcement searches found no unrestricted complete proof or counterexample. Full nearest-statement comparisons found no equivalent AIM, OpenAI-announcement or existing FURTHER entry. Results assuming projectivity, Kähler geometry, nef adjoints or a split tangent bundle were not promoted to the unrestricted compactification statement. These checks do not certify absence of every possible resolution.

The [owner review](../FURTHER_problems/_tracking/AIF107/PRECISE-PROPOSAL.json), [independent model review](../FURTHER_problems/_tracking/AIF107/C-INDEPENDENT-CONNECTED-SMOOTH-AMBIENT-ANALYTIC-BOUNDARY-AND-MOISHEZON-CONCLUSION-MODEL-PEER-PASS.json) and [coordinator review](../FURTHER_problems/_tracking/ROOT-FINAL-AIF107-affine-compactification-Moishezon-admission-review-20261030.json) record the evidence and inspected extents.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d960713f1bd0a7d6**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
