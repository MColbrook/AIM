# 721. Real C¹,¹ regularity of complex Hessian obstacle envelopes

**Area:** Complex analysis, potential theory and nonlinear obstacle problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\Subset\mathbb C^n`$ be a bounded smooth strongly $`m`$-pseudoconvex domain, where $`2\le m\le n`$. Thus $`\Omega`$ admits a smooth defining function $`\rho`$ that is strictly $`m`$-subharmonic near $`\overline\Omega`$ and satisfies $`|\nabla\rho|>0`$ on its boundary. For real $`h\in C^2(\overline\Omega)`$, define

```math
P_{m,\Omega}h=\left(\sup\{v\in\mathrm{SH}_m(\Omega):v\le h\text{ on }\Omega\}\right)^*.
```

Here the star denotes upper semicontinuous regularization, and $`\mathrm{SH}_m`$ is the standard class of $`m`$-subharmonic functions. For smooth functions, this means that the first $`m`$ elementary symmetric functions of the eigenvalues of the complex Hessian are nonnegative.

Must $`P_{m,\Omega}h`$ have locally Lipschitz first derivatives with respect to all real coordinates, that is,

```math
P_{m,\Omega}h\in C^{1,1}_{\mathrm{loc}}(\Omega)?
```

## Application

The envelope enforces a pointwise obstacle constraint on a nonlinear potential. The proposed regularity bounds its curvature and is closely related to identifying its Hessian measure on the contact set with the obstacle.

## References

1. A. Benali and A. Zeriahi, [The Hölder continuous subsolution theorem for complex Hessian equations](https://doi.org/10.5802/jep.133), *J. Éc. polytech. Math.* **7** (2020), 981–1007; explicit question on p. 998.
2. J. Chu and N. McCleerey, [Fully non-linear degenerate elliptic equations in complex geometry](https://doi.org/10.1016/j.jfa.2021.109176), *J. Funct. Anal.* **281** (2021), 109176. The compact Hermitian envelope theorem has a different domain setup.
3. A. Benali and A. Zeriahi, [Erratum](https://doi.org/10.5802/jep.157), *J. Éc. polytech. Math.* **8** (2021), 779–789.

## Status review


**Known cases:** The June complex Hessian flow paper, Lemma 8.1, supplies continuity of the obstacle envelope, not bounds on all real second derivatives. Compact-background complex Hessian estimates and the withdrawn 2017 envelope proof do not give this bounded-domain real C1,1 conclusion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The June complex Hessian flow paper, Lemma 8.1, supplies continuity of the obstacle envelope, not bounds on all real second derivatives. Compact-background complex Hessian estimates and the withdrawn 2017 envelope proof do not give this bounded-domain real C1,1 conclusion.

Additional comparison sources: [comparison source 1](https://doi.org/10.5802/jep.133); [comparison source 2](https://doi.org/10.1016/j.jfa.2021.109176); [comparison source 3](https://doi.org/10.5802/jep.157); [comparison source 4](https://arxiv.org/abs/2402.03098); [comparison source 5](https://arxiv.org/abs/1703.07727). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The bounded-domain question is distinct from the established compact Hermitian theorem, which assumes a strictly positive background and no boundary. The source and its precise obstacle hypotheses were checked independently. The 2026 compact results controlling the complex Hessian do not by themselves bound all real second derivatives. The related [complex Hessian eigenvalue paper](https://arxiv.org/abs/2402.03098) has different boundary, right-hand-side and barrier assumptions; its displayed estimates do not directly give estimates uniform in the obstacle-penalization parameter here.

An exact-looking [2017 plurisubharmonic-envelope paper](https://arxiv.org/abs/1703.07727) was withdrawn because of a mistake in its main proof. It is not a valid resolution. Current searches on 17 October 2026, all-status AIM/OpenAI comparisons and Prove2Me listing-description comparisons found no matching resolution or announcement. These bounded checks are not an exhaustive certification of the literature. The related contact-measure identity is not asserted to be equivalent to this regularity question.

See the [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/hessian-envelope-review.json) and [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-hessian-envelope-review.json) for the exact passages read, closest theorem comparisons, versions and access limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d367b11ee7252273**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
