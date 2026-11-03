# 767. A crystalline criterion for lifting algebraic cycles in higher codimension

**Area:** Algebraic geometry and arithmetic cohomology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`k`$ be a perfect field of characteristic $`p>0`$, let $`W(k)`$ be its ring of Witt vectors, and put $`K=\mathrm{Frac}W(k)`$. For a smooth $`k`$-variety $`V`$, write
```math
H^m_{\mathrm{crys}}(V)_K
=H^m_{\mathrm{crys}}(V/W(k))\otimes_{W(k)}K.
```

Write $`\mathrm{CH}^i(V)_{\mathbb Q}`$ for codimension-$`i`$ algebraic cycles modulo rational equivalence, with rational coefficients, and
```math
\mathrm{cl}_{\mathrm{crys}}:
\mathrm{CH}^i(V)_{\mathbb Q}\longrightarrow
H^{2i}_{\mathrm{crys}}(V)_K
```

for the crystalline cycle-class map.

Suppose that $`f:X\to S`$ is a smooth projective morphism of smooth $`k`$-varieties, $`s\in S`$ is a closed point, and $`i\ge2`$. Set $`X_s=f^{-1}(s)`$. Given $`z\in\mathrm{CH}^i(X_s)_{\mathbb Q}`$, put $`c=\mathrm{cl}_{\mathrm{crys}}(z)`$.

Assume that there is a class $`\widetilde c\in H^{2i}_{\mathrm{crys}}(X)_K`$ such that
```math
\widetilde c|_{X_s}=c,
\qquad
\varphi(\widetilde c)=p^i\widetilde c,
```

where $`\varphi`$ is the action of absolute Frobenius.

**Must there be $`\widetilde z\in\mathrm{CH}^i(X)_{\mathbb Q}`$ with**
```math
\mathrm{cl}_{\mathrm{crys}}(\widetilde z)|_{X_s}=c?
```


This asks for equality of cohomology classes on the fibre, not equality of cycles in its Chow group. The coefficients of the cycles are $`\mathbb Q`$. Frobenius can be semilinear over $`K`$; the displayed equation is the intended condition.

## Application

Cohomology gives a way to test whether an algebraic cycle on one fibre can extend through a family. This question asks whether the crystalline lifting condition detects a global algebraic cycle in higher codimension. It links deformation of cycles with arithmetic cohomology and the study of Tate-type algebraicity questions.

## Known results and scope

This is the projective higher-codimension part of Morrow's Conjecture 0.1. In this projective setting, his Theorem 2.1 shows that the Frobenius-compatible lift condition is equivalent to the corresponding lift in ordinary rational crystalline cohomology and to the flatness condition used in the conjecture.

For $`i=1`$, Morrow's Theorem 1.4 proves the assertion for divisors. His Theorem 0.6 gives an infinitesimal lifting result in all codimensions for classes in $`K_0`$, under its stated assumptions on the field and formal base. Lifting to every infinitesimal thickening does not supply the global rational cycle required here.

Lazda–Pál extend the divisor theory to semistable families. Their counterexample with $`\mathbb Q_p`$-coefficients also shows why the rational coefficients in this question must be retained.

The 2026 OpenAI announcements concerning CM abelian varieties, the Tate conjecture for abelian varieties over finite fields, and specialized Hodge classes after good reduction have narrower geometric hypotheses. Their selected statements do not assert the criterion above for arbitrary smooth projective families.

Fu–Huang–Li’s 2026 results treat excellent supersingular irreducible symplectic varieties of specified deformation types, with characteristic and Artin-invariant restrictions. Their cycle-class statements do not cover arbitrary smooth projective families.

## References

1. M. Morrow, *A Variational Tate Conjecture in crystalline cohomology*, J. Eur. Math. Soc. 21 (2019), 3467–3511, [DOI](https://doi.org/10.4171/JEMS/907). Eligible version: [arXiv:1408.6783v2](https://arxiv.org/pdf/1408.6783v2), Conjecture 0.1 pp. 2 and 5, Theorem 1.4 p. 7, Theorem 2.1 p. 9, and Theorem 0.6 pp. 3–4. The [separate author version](https://www.imo.universite-paris-saclay.fr/~matthew.morrow/Morrow%2C%20M.%2C%20Variational%20Tate.pdf) retains the conjecture.
2. C. Lazda and A. Pál, *Cycle classes in overconvergent rigid cohomology and a semistable Lefschetz (1,1) theorem*, Compositio Mathematica (2019), [DOI](https://doi.org/10.1112/S0010437X19007164). [arXiv:1701.05017v2](https://arxiv.org/pdf/1701.05017v2), Introduction pp. 1–2, summarizing the divisor results and the distinction between $`\mathbb Q`$ and $`\mathbb Q_p`$.
3. OpenAI, *Milne's rationality conjecture for abelian varieties* (2026), [preprint](https://github.com/openai/math/blob/main/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/paper.pdf), Theorem 1.1 and discussion pp. 1–2.
4. OpenAI, *The rational Hodge conjecture for CM abelian varieties* (2026), [preprint](https://github.com/openai/math/blob/main/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf), Theorem 1.1 p. 1 and Corollary 8.3 p. 49.

5. L. Fu, X. Huang and Z. Li, *Supersingular Tate conjecture for irreducible symplectic varieties of known types: I*, [arXiv:2609.38801v2](https://arxiv.org/html/2609.38801v2) (20 October 2026), Definition 1.6, Theorems 1.9–1.10 and Remark 1.13.

## Status review


**Known cases:** Global rational-cycle lifting in arbitrary higher codimension is required. Divisor lifting, infinitesimal lifting and the OpenAI abelian-variety algebraicity announcements do not give this for arbitrary smooth projective families.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Global rational-cycle lifting in arbitrary higher codimension is required. Divisor lifting, infinitesimal lifting and the OpenAI abelian-variety algebraicity announcements do not give this for arbitrary smooth projective families.

Additional comparison sources: [comparison source 1](https://doi.org/10.4171/JEMS/907); [comparison source 2](https://arxiv.org/pdf/1408.6783v2); [comparison source 3](https://www.imo.universite-paris-saclay.fr/~matthew.morrow/Morrow%2C%20M.%2C%20Variational%20Tate.pdf); [comparison source 4](https://doi.org/10.1112/S0010437X19007164); [comparison source 5](https://arxiv.org/pdf/1701.05017v2); [comparison source 6](https://github.com/openai/math/blob/main/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/paper.pdf); [comparison source 7](https://github.com/openai/math/blob/main/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf); [comparison source 8](https://arxiv.org/html/2609.38801v2). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 2026-10-24 against the eligible conjecture and selected supporting results, the later author version, official version histories, current primary statements and announcements, targeted Prove2Me searches, and all-status AIM/FURTHER comparisons. No matching resolution or announcement was located. The review distinguishes global rational-cycle lifting from divisor results, infinitesimal lifting, and abelian-variety algebraicity. It covers selected primary passages and does not certify every cited proof or exhaust the literature.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0e5030570b6434b6**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
