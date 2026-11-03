# 975. Sharp disagreement probabilities for coherent forecasts with a fixed prior

**Area:** Probability inequalities and information aggregation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`p\in[0,1]`$ and $`0<\delta\le1/2`$. Let $`\mathcal C(p)`$ consist of all joint laws of

```math
X=\mathbb P(A\mid\mathcal G),\qquad
Y=\mathbb P(A\mid\mathcal H),\qquad \mathbb P(A)=p,
```

where the probability space, event $`A`$ and two sub-$`\sigma`$-fields are arbitrary. Such a pair is called coherent. In particular, $`X,Y\in[0,1]`$ and $`\mathbb EX=\mathbb EY=p`$, but equal means alone do not establish coherence.

Determine the exact function

```math
\varepsilon(\delta,p)
=\sup_{(X,Y)\in\mathcal C(p)}\mathbb P(|X-Y|\ge1-\delta).
```

Independence, finite support and exchangeability are not imposed. This asks for the full function, including cases already known; it does not assert that every parameter pair remains untreated or request a unique optimizer.

## Application

The quantity bounds how often two forecasts, formed from different information about one event with a specified prior probability, can disagree by a given amount. Fixing the prior retains information lost in a bound optimized over all event probabilities.

## References

1. K. Burdzy and J. Pitman, [Bounds on the probability of radically different opinions](https://doi.org/10.1214/20-ECP296), *Electronic Communications in Probability* **25** (2020), article 14, 1–12. The inspected [arXiv:1903.07773v1](https://arxiv.org/html/1903.07773v1) defines coherence in (1.1)–(1.2), the function in (5.3), and asks the remaining fixed-prior question in Problem 5.4. Published numbering: Problem 5.3.
2. S. Cichomski and F. Petrov, [A combinatorial proof of the Burdzy–Pitman conjecture](https://arxiv.org/html/2204.07219v1) (2022), Introduction and Section 3: the independent-pair problem.
3. [Coherent distributions: Hilbert space approach and duality](https://arxiv.org/html/2405.04375v1) (2024), Theorems 1.2–1.3: covariance and power-moment extrema.

## Status review


**Known cases:** The complete two-parameter fixed-prior function for arbitrary coherent pairs is needed. Independent-pair results and covariance/power-moment optimization change the feasible class or objective.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The complete two-parameter fixed-prior function for arbitrary coherent pairs is needed. Independent-pair results and covariance/power-moment optimization change the feasible class or objective.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Open in the cited source; no matching full resolution or announcement was located in checks through 29 October 2026. The independent-pair theorem changes the admissible class. Covariance and power-moment bounds change the objective and do not by themselves give the displayed function.

The original mixture examples supply some parameter cases. Their endpoint commentary is not used as a universal formula here: $`\varepsilon(\delta,0)=\varepsilon(\delta,1)=0`$, while $`\varepsilon(1/2,1/2)=1`$ follows by taking $`X=1/2`$ and $`Y=1_A`$ with $`\mathbb P(A)=1/2`$. The formulation follows the pinned preprint; indexed published passages corroborate the question, without a full published-body comparison.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-39be505120780b79**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
