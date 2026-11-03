# 718. Continuous subsolutions for the complex Monge–Ampère Dirichlet problem

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb C^n`$, $`n\ge2`$, be a bounded hyperconvex domain: it admits a negative continuous plurisubharmonic exhaustion. Let $`\mu`$ be a positive Borel probability measure on $`\Omega`$. Suppose there is
```math
v\in\mathrm{PSH}(\Omega)\cap C(\overline\Omega),\qquad v|_{\partial\Omega}=0,\qquad \mu\le(dd^cv)^n.
```

Here $`dd^c=i\partial\bar\partial`$, and the measure inequality uses the Bedford–Taylor operator.

Must there be
```math
u\in\mathrm{PSH}(\Omega)\cap C(\overline\Omega),\qquad u|_{\partial\Omega}=0,\qquad (dd^cu)^n=\mu?
```

No Hölder or Dini condition is imposed on $`v`$.

## Application

A subsolution provides a barrier and bounds for a nonlinear elliptic boundary problem. This question asks whether continuity is preserved when the prescribed measure is dominated by the Monge–Ampère measure of a continuous potential.

## References

1. S. Dinew, V. Guedj and A. Zeriahi, *Open problems in pluripotential theory*, Complex Variables and Elliptic Equations 61(7) (2016), 902–930, Question 14, preprint p. 9. [Primary preprint](https://arxiv.org/pdf/1511.00705v1).
2. S. Kołodziej and N.C. Nguyen, *A remark on the continuous subsolution problem for the complex Monge–Ampère equation*, Acta Mathematica Vietnamica 45 (2020), 83–91, Theorem 1.1 and following paragraph. [Published article](https://doi.org/10.1007/s40306-019-00347-0).
3. N.C. Nguyen, *On the Hölder continuous subsolution problem for the complex Monge–Ampère equation, II*, Analysis & PDE 13(2) (2020), 435–453, p. 437. [Publisher PDF](https://msp.org/apde/2020/13-2/apde-v13-n2-p04-p.pdf).
4. M. Charabati and A. Zeriahi, *The continuous subsolution problem for complex Hessian equations*, Indiana University Mathematics Journal 73(5) (2024), 1639–1688. Latest preprint, Question (i), pp. 3–4, and Theorem 4, p. 6. [Preprint](https://arxiv.org/pdf/2007.10194v3), [DOI](https://doi.org/10.1512/iumj.2024.73.60071).

## Status review


**Known cases:** Available continuous-subsolution statements retain Dini or Holder modulus restrictions, smooth-domain conditions, or densities in a restricted class. No matching assertion with only continuous subsolution on every bounded hyperconvex domain was located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Available continuous-subsolution statements retain Dini or Holder modulus restrictions, smooth-domain conditions, or densities in a restricted class. No matching assertion with only continuous subsolution on every bounded hyperconvex domain was located.

Additional comparison sources: [comparison source 1](https://arxiv.org/pdf/1511.00705v1); [comparison source 2](https://doi.org/10.1007/s40306-019-00347-0); [comparison source 3](https://msp.org/apde/2020/13-2/apde-v13-n2-p04-p.pdf); [comparison source 4](https://arxiv.org/pdf/2007.10194v3); [comparison source 5](https://doi.org/10.1512/iumj.2024.73.60071). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 16 October 2026. The Hölder case and more general Dini conditions are known in smooth strictly pseudoconvex domains. These results do not impose merely continuity. The one-dimensional analogue is positive. The current published 2024 introduction and Theorem 4 were compared with the latest preprint; the Dini restriction remains. No complete announced solution of the displayed unrestricted problem was found. The complete announcement-catalogue alias scan found no matching target. Independent formulation and duplicate checks are recorded in the [review packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/continuous-subsolution-review.json), including the stronger assumptions in nearby 2026 results and the limits of publisher-version access. Current openness is a dated literature-search inference, not a guarantee that no proof exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c3f8f7c8332b9409**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
