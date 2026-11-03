# 709. Moderate measures and Hölder continuous Monge–Ampère potentials

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(X,\omega)`$ be a compact Kähler manifold of complex dimension $`n\ge2`$, normalized by $`\int_X\omega^n=1`$. Write $`dd^c=i\partial\bar\partial`$. A function $`\psi`$ is $`\omega`$-plurisubharmonic if $`\omega+dd^c\psi\ge0`$ as a current.

Let $`\mu`$ be a positive Borel probability measure on $`X`$. Suppose that $`\mu`$ is **moderate**: there exist $`a,C>0`$ such that
```math
\int_X e^{-a\psi}\,d\mu\le C
\quad\text{for every }\psi\in\mathrm{PSH}(X,\omega),\quad\sup_X\psi=0.
```

The constants are uniform over this normalized family.

Must there exist some $`\alpha\in(0,1]`$ and a Hölder continuous $`\omega`$-plurisubharmonic function $`\varphi\in C^{0,\alpha}(X)`$ such that
```math
(\omega+dd^c\varphi)^n=\mu?
```

The equation uses the Bedford–Taylor operator. No Hölder continuity of the super-potential of $`\mu`$ is assumed.

## Application

Moderateness controls concentration near plurisubharmonic singularities and appears naturally for invariant measures in complex dynamics. The question asks whether this exponential integrability forces Hölder regularity of the corresponding nonlinear elliptic potential.

## References

1. S. Dinew, V. Guedj and A. Zeriahi, *Open problems in pluripotential theory*, Complex Variables and Elliptic Equations 61(7) (2016), 902–930, Question 16, preprint p. 10. [Primary preprint](https://arxiv.org/pdf/1511.00705v1).
2. T.-C. Dinh and V.-A. Nguyên, *Characterization of Monge–Ampère measures with Hölder continuous potentials*, Journal of Functional Analysis 266(1) (2014), 67–84. Problem 1.3 and moderate definition in preprint pp. 3–4; published numbering differs. [Primary preprint](https://arxiv.org/pdf/1204.4883v1), [DOI](https://doi.org/10.1016/j.jfa.2013.08.026).
3. E. Di Nezza and C. Favre, *Regularity of push-forward of Monge–Ampère measures*, Annales de l'Institut Fourier 68(7) (2018), 2965–2979, p. 2972. [Publisher PDF](https://aif.centre-mersenne.org/item/10.5802/aif.3233.pdf).
4. S. Kołodziej and N.C. Nguyen, *Continuous solutions to Monge–Ampère equations on Hermitian manifolds for measures dominated by capacity*, Calculus of Variations and Partial Differential Equations 60 (2021), article 93, p. 2. [Published article](https://doi.org/10.1007/s00526-021-01944-4).

## Status review


**Known cases:** A moderate measure is weaker than having a Holder super-potential. The available Hermitian continuous-solution theorem and sufficient Holder characterizations do not establish Holder potentials for every moderate measure.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

A moderate measure is weaker than having a Holder super-potential. The available Hermitian continuous-solution theorem and sufficient Holder characterizations do not establish Holder potentials for every moderate measure.

Additional comparison sources: [comparison source 1](https://arxiv.org/pdf/1511.00705v1); [comparison source 2](https://arxiv.org/pdf/1204.4883v1); [comparison source 3](https://doi.org/10.1016/j.jfa.2013.08.026); [comparison source 4](https://aif.centre-mersenne.org/item/10.5802/aif.3233.pdf); [comparison source 5](https://doi.org/10.1007/s00526-021-01944-4). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 16 October 2026. The reverse implication is known: a Hölder continuous potential gives a moderate measure. The displayed implication holds in dimension one and in the toric setting. Hölder continuous super-potentials give a stronger, sufficient characterization. Known examples for weaker capacity conditions do not answer the moderate-measure question. No matching complete proof, counterexample or full-solution announcement was located in the dated searches. This is a literature check, not a guarantee that no proof exists. The exact statement was compared against all statuses of AIM, the OpenAI announcement index, the current FURTHER list and the Prove2Me catalogue. The [review packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/moderate-measure-review.json) records the comparisons and version-access limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-994dad94582f2891**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
