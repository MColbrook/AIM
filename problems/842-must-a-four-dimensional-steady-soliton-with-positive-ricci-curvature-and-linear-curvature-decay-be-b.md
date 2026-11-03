# 842. Must a four-dimensional steady soliton with positive Ricci curvature and linear curvature decay be Bryant?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M^4,g,f)`$ be a complete connected noncompact smooth gradient steady Ricci soliton, with the convention
```math
\mathrm{Ric}_g=\mathrm{Hess}_g f.
```

Assume $`\mathrm{Ric}_g>0`$ everywhere and that $`g`$ is $`\kappa`$-noncollapsed on all scales for some $`\kappa>0`$: a curvature-controlled ball with $`\sup_{B_g(x,r)}|\mathrm{Rm}_g|\le r^{-2}`$ has volume at least $`\kappa r^4`$.

Fix $`o\in M`$ and put $`\rho(x)=d_g(o,x)`$. Suppose there are constants $`C,r_0>0`$ such that
```math
|\mathrm{Rm}_g|(x)\le\frac{C}{\rho(x)}
\qquad\text{whenever }\rho(x)\ge r_0.
```


Must $`(M,g)`$ be isometric, up to positive constant rescaling, to the four-dimensional Bryant steady soliton?

The decay assumption concerns the **full curvature tensor**. No global nonnegative sectional-curvature or curvature-operator assumption is imposed, and the soliton is not assumed to arise as a singularity model.

## Application

Steady solitons model persistent geometric patterns in Ricci flow. The question asks whether noncollapse, positive Ricci curvature and this decay rate determine the entire metric, rather than just its geometry at infinity.

## References

1. Yuxing Deng and Xiaohua Zhu, *Classification of gradient steady Ricci solitons with linear curvature decay*, Science China Mathematics **63** (2020), 135–154. [DOI](https://doi.org/10.1007/s11425-019-1548-0); [primary preprint](https://arxiv.org/abs/1809.08502). Theorem 1.5 and the conjecture immediately following it state this target.
2. Michael B. Law, *On steady and expanding Ricci solitons with asymptotic symmetries*, [latest primary preprint, v3, 8 April 2026](https://arxiv.org/abs/2505.20576v3). Theorem 1.5, §1.2 and the version-correction note are essential to the current comparison.
3. Ziyi Zhao and Xiaohua Zhu, *Steady gradient Ricci solitons with nonnegative curvature away from a compact set*, Annales de la Faculté des sciences de Toulouse **35** (2026), 801–837. [Publisher](https://doi.org/10.5802/afst.1864). The stated Bryant rigidity conclusion retains a global nonnegative curvature-operator hypothesis.
4. Pak-Yeung Chan, Zilu Ma and Yongjia Zhang, *Hamilton-Ivey estimates for gradient Ricci solitons*. [Primary preprint](https://arxiv.org/abs/2112.11025); [published DOI](https://doi.org/10.1007/s00526-025-03167-3). Theorems 1.6–1.7 give curvature bounds and positivity outside a compact set under their stated hypotheses, without supplying the needed global sign condition.

## Status review


**Known cases:** Law v3 remains the latest revision and explicitly states that dropping its weighted Lichnerowicz-kernel dimension hypothesis is unknown. Positivity of sectional curvature only outside a compact set does not supply the global sign assumptions in other Bryant-rigidity results.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Law v3 remains the latest revision and explicitly states that dropping its weighted Lichnerowicz-kernel dimension hypothesis is unknown. Positivity of sectional curvature only outside a compact set does not supply the global sign assumptions in other Bryant-rigidity results.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 30 October 2026. Deng–Zhu already prove that these solitons are asymptotically cylindrical and have positive sectional curvature outside a compact set. The question asks for the further global Bryant conclusion.

Law's latest theorem proves this conclusion with an additional weighted Lichnerowicz-kernel dimension bound, at most one in dimension four. The same version explicitly says that removing that bound is unknown and replaces earlier arguments after an error in old Lemma 3.11. The earlier unconditional claim is therefore not treated as an active resolution. No implication from the assumptions above to the kernel bound was located.

Other rigidity results assume a global curvature sign or pinching condition. Positivity outside a compact set does not supply that premise. The known flying-wing counterexamples to a broader higher-dimensional conjecture are not identified as counterexamples satisfying the precise decay hypothesis here.

Bounded current searches and full nearest-statement comparisons against AIM, current saved OpenAI announcements and private findings found no equivalent target or matching active complete resolution. Exact preprint statements and the relevant version history were read; full published-body parity is not asserted. These checks are not a proof of openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ca7ac61e14ebae50**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
