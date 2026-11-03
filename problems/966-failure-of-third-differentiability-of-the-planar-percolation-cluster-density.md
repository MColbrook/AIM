# 966. Failure of third differentiability of the planar percolation cluster density

**Area:** Probability, random media and phase transitions
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

On the nearest-neighbor square lattice $`\mathbb Z^2`$, independently declare each edge open with probability $`p\in[0,1]`$. Let $`C(0)`$ be the connected component of the origin using open edges, and let $`|C(0)|`$ count its vertices. Define
```math
\kappa(p)=\mathbb E_p\!\left[\frac1{|C(0)|}\right],
\qquad \frac1\infty:=0.
```

This is the mean number of open clusters per vertex in the infinite-volume limit [1, §4.1]. The critical probability is $`p_c=1/2`$.

**Prove or disprove that the ordinary third derivative $`\kappa'''(1/2)`$ does not exist as a finite real number.** Since $`\kappa`$ is twice continuously differentiable near $`1/2`$, the question is whether
```math
\lim_{h\to0}\frac{\kappa''(1/2+h)-\kappa''(1/2)}h
```

fails to exist finitely. No particular critical exponent or divergence amplitude is prescribed.

The conjecture is stated explicitly in [1, p. 325], with further discussion on p. 285. It concerns the next derivative at the critical point; failure of continuous third differentiability somewhere in every neighborhood would be a weaker conclusion.

## Application

The cluster density measures the average number of separate connected regions in a model of a porous or disordered medium. Its regularity describes a weak thermodynamic singularity at the connectivity transition.

## Status review


**Known cases:** The target is the ordinary third derivative at the square bond critical probability. Exact cluster values, numerical scaling, critical percolation existence and interface convergence do not by themselves establish failure of this derivative.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is the ordinary third derivative at the square bond critical probability. Exact cluster values, numerical scaling, critical percolation existence and interface convergence do not by themselves establish failure of this derivative.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The function $`\kappa`$ is analytic away from $`p_c`$ and is $`C^2`$ at $`p_c`$ [1]. The 2020 primary discussion [2, pp. 2–3 of the checked arXiv version] continues to distinguish this rigorous regularity from conjectured failure of the third derivative.

AIM 090 and the related OpenAI result family 223 concern critical crossing probabilities and interface scaling limits. The inspected October 2026 manuscript [3, Theorems 1.1–1.2] treats the critical edge parameter, with no uniformity in the cluster weight asserted. It gives no theorem about the displayed derivative of $`\kappa`$. Such critical convergence alone does not justify differentiating cluster-count limits as $`p`$ varies. The scaling relations involving the cluster-density exponent require separate care: [1, p. 252] explicitly excludes that exponent from its account of Kesten's proved scaling relations.

This review compared exact source definitions and selected current formal statements. It does not independently certify the complete proofs of the cited results.

## References

1. Geoffrey Grimmett, [*Percolation*, second edition](https://doi.org/10.1007/978-3-662-03981-6), Springer, 1999. Definition (4.1), p. 77; planar duality and the regularity discussion, p. 285; the explicit third-derivative conjecture after Theorem (11.93), p. 325; scaling notes, p. 252. The definition and conjecture pages were checked in the native publisher chapters, including their rendered formulas.
2. Dmitry Beliaev, Michael McAuley and Stephen Muirhead, [*Smoothness and monotonicity of the excursion set density of planar Gaussian fields*, arXiv:1905.09759v2](https://arxiv.org/pdf/1905.09759v2), 11 August 2020, introduction pp. 2–3. Published in **Electronic Journal of Probability 25** (2020), article 93, 1–37, [DOI 10.1214/20-EJP470](https://doi.org/10.1214/20-EJP470). The checked 39-page author version is described on arXiv as updated to match the published version; exact byte or pagination parity is not asserted.
3. OpenAI, [*Conformal Limits of Critical Square-Lattice Random-Cluster Interfaces*](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/paper.pdf), 5 October 2026, §§1.1–1.5 and Theorems 1.1–1.2, pp. 4–7. This is a related current claim, with the scope comparison described above.

The [coordinator review](../FURTHER_problems/_tracking/B081-cluster-density-entanglement-two-target-gates-C-20261028/ROOT-KAPPA-SOURCE-PIXELS-CURRENT-IMPLICATION-SCOPE-AND-SEMANTIC-PASS-20261028.json) records the current-result comparisons, source extents and all-status duplicate checks.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-009ea341fdfcfb25**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
