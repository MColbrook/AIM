# 730. The sharp generic bound on iterated Fuller singularities

**Area:** Geometric optimal control / continuous optimization
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a positive integer $`n`$, let $`M`$ be a smooth connected $`n`$-manifold and consider
```math
\dot q=f_0(q)+u f_1(q),\qquad u\in[-1,1],\qquad f_0,f_1\in\mathrm{Vec}(M).
```

An extremal triple $`(q,u,\lambda)`$ satisfies the Pontryagin maximum principle: $`\lambda`$ is an absolutely continuous, everywhere nonzero covector lift of $`q`$, and, almost everywhere,
```math
H(\lambda,u)=\max_{v\in[-1,1]}H(\lambda,v),\qquad
\dot\lambda=\vec H(\lambda,u),\qquad
H(\lambda,v)=\langle\lambda,f_0(q)+vf_1(q)\rangle.
```


For $`q:[0,T]\to M`$, $`T>0`$, let $`O_q\subset[0,T]`$ be the largest relatively open set on which there exists some control associated with $`q`$ that is smooth, and put $`\Sigma=[0,T]\setminus O_q`$. Set
```math
\Sigma_0=\mathrm{Iso}(\Sigma),\qquad
\Sigma_k=\mathrm{Iso}\!\left(\Sigma\setminus\bigcup_{j<k}\Sigma_j\right)
\quad(k\ge1),
```

where $`\mathrm{Iso}`$ denotes isolated points.

**Determine the least dimension-only integer $`K(n)\ge0`$ such that, for every $`M`$, an open dense subset of $`\mathrm{Vec}(M)^2`$, in the Whitney $`C^\infty`$ topology, satisfies**
```math
\Sigma=\bigcup_{k=0}^{K(n)}\Sigma_k
```

**for every extremal triple.**

Boarotto–Sigalotti prove $`K(n)\le(n-1)^2`$ and explicitly ask for the sharp bound. Their three-dimensional order-two improvement concerns time-minimizing trajectories; the question here retains all PMP extremals.

## Application

The bound measures how deeply accumulations of control switchings can repeat. A sharp value would clarify the generic complexity of extremals used in time-optimal control synthesis.

## References

1. F. Boarotto and M. Sigalotti, *Time-optimal trajectories of generic control-affine systems have at worst iterated Fuller singularities*, **Annales de l'Institut Henri Poincaré C** 36 (2019), 327–346, [DOI:10.1016/j.anihpc.2018.05.005](https://doi.org/10.1016/j.anihpc.2018.05.005). See Section 1.2, Definitions 1–2, Theorem 3 and the question following Remark 4 (p. 329); Section 2.1 specifies PMP extremals. [Latest arXiv version, v3, 22 May 2018](https://arxiv.org/abs/1705.10055v3).
2. F. Boarotto, Y. Chitour and M. Sigalotti, *Fuller singularities for generic control-affine systems with an even number of controls*, **SIAM Journal on Control and Optimization** 58 (2020), 1207–1228, [DOI:10.1137/19M1285305](https://doi.org/10.1137/19M1285305), Theorem 6. This proves a finite dimension-dependent bound for even-dimensional ball-valued controls under frame hypotheses; it does not determine the sharp single-input bound above.

## Status review


**Known cases:** The target is the least dimension-only Cantor-Bendixson order for every PMP extremal in an open dense set of vector-field pairs. The known squared-dimension bound and the sharper order for three-dimensional time minimizers do not identify this all-extremal optimum.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is the least dimension-only Cantor-Bendixson order for every PMP extremal in an open dense set of vector-field pairs. The known squared-dimension bound and the sharper order for three-dimensional time minimizers do not identify this all-extremal optimum.

Additional comparison sources: [comparison source 1](https://doi.org/10.1016/j.anihpc.2018.05.005); [comparison source 2](https://arxiv.org/abs/1705.10055v3); [comparison source 3](https://doi.org/10.1137/19M1285305). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

No matching complete or announced resolution was located in the dated review. This is a bounded literature check, rather than a claim that all later control literature has been searched.

The [source and current review](../FURTHER_problems/_tracking/focused-Fuller-sharp-generic-order-C161-A-20261028/FULLER-PRIMARY-LATEST-EXACT-QUESTION-CURRENT-ANNOUNCEMENT-PEER-PASS-NO-ADMISSION.json), [independent review](../FURTHER_problems/_tracking/focused-Fuller-sharp-generic-order-C161-A-20261028/ROOT-EXACT-ALL-PMP-TOPOLOGY-CONTROL-CHOICE-CURRENT-DUPLICATE-REVIEW-PASS.json) and [all-status comparison](../FURTHER_problems/_tracking/focused-Fuller-sharp-generic-order-C161-A-20261028/FULLER-ALL980-MODELS-613P-1704ROWS-DUPLICATE-ROUTES-SEMANTIC-FRESH-HEADS-PEER-PASS.json) record the exact scope. These are bounded AI checks, not human peer review or a proof certificate.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6c7ca27e24a96240**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
