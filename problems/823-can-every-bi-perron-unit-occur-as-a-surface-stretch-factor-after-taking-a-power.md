# 823. Can every bi-Perron unit occur as a surface stretch factor after taking a power?

**Area:** Surface dynamics and Teichmuller geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

A real algebraic unit $`\lambda>1`$ is **bi-Perron** if each of its other Galois conjugates $`\beta`$ satisfies
```math
\lambda^{-1}<|\beta|<\lambda,
```

except that at most one conjugate may equal $`\lambda^{-1}`$ or $`-\lambda^{-1}`$.

Does every such $`\lambda`$ admit a positive integer $`k`$ for which $`\lambda^k`$ is the stretch factor of a pseudo-Anosov homeomorphism of a compact connected surface [1, 2]?

Here the surface and its topology may depend on $`\lambda`$. A pseudo-Anosov homeomorphism preserves two transverse singular measured foliations, multiplying their transverse measures by reciprocal factors $`\lambda^k`$ and $`\lambda^{-k}`$. Boundary is allowed, following Fried's original definition. No fixed genus or additional orientability of the invariant foliations is imposed.

## Application

The logarithm of a stretch factor measures exponential dynamical complexity. The question asks whether a precise algebraic condition can characterize the possible rates of stretching on compact surfaces, allowing a positive power.

## References

1. D. Fried, [*Growth rate of surface homeomorphisms and flow equivalence*](https://doi.org/10.1017/S0143385700003151), Ergodic Theory and Dynamical Systems **5** (1985), 539–563, Problem 2, pp. 543–544.
2. L. Liechti and J. Pankau, [*The geometry of bi-Perron numbers with real or unimodular Galois conjugates*](https://arxiv.org/pdf/2009.03647v2), arXiv:2009.03647v2 (28 February 2023), Introduction, Theorem 1 and footnote 1.
3. L. Liechti, [*Geometry and Arithmetic of Pseudo-Anosov Stretch Factors*](https://homeweb.unifr.ch/liechtli/pub/habilitation_Liechti_final.pdf), habilitation thesis, Fribourg (2025), Section 1.2, pp. 9–11.
4. P. Hillen, M. Loving and C. Wu, [*Every Weak Perron Number is an End-Periodic Stretch Factor*](https://arxiv.org/pdf/2603.20491v1), arXiv:2603.20491v1 (2026), Introduction.

## Status review


**Known cases:** Current compact-surface results cover bi-Perron numbers with real or unimodular conjugates. The 2026 weak-Perron realization uses infinite-type end-periodic surfaces, outside this compact-surface target. The withdrawn degree-three claim is not an active resolution.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Current compact-surface results cover bi-Perron numbers with real or unimodular conjugates. The 2026 weak-Perron realization uses infinite-type end-periodic surfaces, outside this compact-surface target. The withdrawn degree-three claim is not an active resolution.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The power version is known when all conjugates are real or lie on the unit circle [2]. The general question remains listed as open in [3]. Results on fixed-genus scarcity do not settle a question in which the surface may vary.

The 2026 realization theorem in [4] concerns infinite-type surfaces and explicitly distinguishes the compact-surface question. Kenyon's [degree-three preprint](https://arxiv.org/abs/1912.09385) was withdrawn because of a proof mistake and is not treated as a resolution.

The stronger version asking for $`k=1`$ is a separate variant; the statement here follows Fried's original power question. The [independent source/status review](../FURTHER_problems/_tracking/C148-source672893-first75000-A30-20261027/focused-biPerron-and-weighted-projection/ROOT-PRECISE-PRIMARY-CURRENT-AND-DUPLICATE-GATES-PASS.json) records bounded checks of current and announced solutions and all-status AIM/OpenAI/FURTHER duplicates. These checks are not a certificate of openness or human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a411ed9ba646c1b4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
