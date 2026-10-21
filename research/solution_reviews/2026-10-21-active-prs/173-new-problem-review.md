# PR 173: admission review of canonical Stiefel injectivity radius

**PR:** [173](https://github.com/MColbrook/AIM/pull/173). **Reviewed head:** `dded7e8e8a65e059d8d1931c3eb2ca07536b8732`. **Review date:** 2026-10-21. **Decision:** Admit as **AIM 666, Open**, in **Imaging, control, geometry and dynamics** (`inverse2`).

Independent OpenAI Codex AI admission and literature-status review. The submitted statement, metric normalization, cited results, exceptional dimensions and current literature were checked. This report assesses whether the proposed target is a precise, relevant open problem; it does not certify the complete proofs of the imported published theorems.

## Target and placement

The question concerns the real Stiefel manifold of orthonormal frames, with the canonical metric

```math
g_U(\xi,\zeta)
=\mathop{\mathrm{tr}}\!\left(\xi^\top\left(I_n-\frac12 UU^\top\right)\zeta\right).
```

Its normalization is the parameter $`\beta=1/2`$ in the cited metric family. For a tangent vector $`\xi=UA+U_\perp B`$, its squared norm is $`\|A\|_{\mathrm F}^2/2+\|B\|_{\mathrm F}^2`$. The target is to determine the global injectivity radius for **every** integer pair $`2\leq p\leq n-2`$, including $`(n,p)=(4,2)`$. It does not require $`n\geq 2p`$.

The conjectured value is

```math
\mathop{\mathrm{inj}}(\mathrm{St}(n,p),g)=\sqrt2\,\tau,
\qquad \frac{\sin\tau}{\tau}+\cos\tau=0,
\qquad \tau\in(\pi/2,\pi).
```

There is no earlier positive root: both terms are nonnegative before $`\pi/2`$, with a positive sum. On $`(\pi/2,\pi)`$, the equivalent equation $`\tan t+t=0`$ has a unique root because its left side is strictly increasing from negative infinity to a positive value. Independent bisection gives $`\tau\approx2.028757838110434`$ and $`\sqrt2\tau/\pi\approx0.9132618915912204`$.

The new entry belongs beside the existing geometric length-minimizer problems in `inverse2`. Its applications concern canonical geodesic distances, manifold logarithms and geometric data processing. Matrix coordinates do not turn this geometric invariant question into a new numerical linear algebra problem. A catalogue search found no existing Stiefel injectivity-radius entry.

The submitted number 652 is already assigned to a retained catalogue identity. The issued collection ends at 665, so this admission receives 666. Existing identities and their records are preserved.

## Existing results and exact scope

The sharp sectional-curvature upper bound $`5/4`$ gives the lower radius bound, and the explicit conjugate points give the upper bound:

```math
\sqrt{\frac45}\,\pi
\leq\mathop{\mathrm{inj}}(\mathrm{St}(n,p),g)
\leq\sqrt2\,\tau<\pi.
```

The canonical shortest nontrivial geodesic loops have length $`2\pi`$. Klingenberg's formula therefore identifies the injectivity radius with the global conjugate radius in the target range, since the known conjugate upper bound is below $`\pi`$. The unresolved step is to exclude an earlier conjugate point in **every** initial direction. The bounds and their sources are recorded in [Absil–Mataigne, Sections 7.3–9](https://arxiv.org/html/2403.02079v3), [Zimmermann–Stoye, Theorem 8 and Section 3.4](https://arxiv.org/html/2403.01879v3), and the [2026 paper, Theorem 7.3](https://doi.org/10.1007/s10543-026-01141-9).

Appendix C of the 2026 paper determines a first conjugate point along one specified geodesic of $`\mathrm{St}(4,2)`$. That witness does not establish the minimum over all geodesics, even for that dimension pair. The same paper's Section 7.2 explicitly retains the canonical-metric radius as conjectural. Its exact results for other metric parameters do not include $`\beta=1/2`$ in the stated dimension range. [Stoye–Mataigne–Absil–Zimmermann, Section 7.2 and Appendix C](https://doi.org/10.1007/s10543-026-01141-9).

The excluded canonical cases $`p=1`$, $`p=n-1`$ and $`p=n`$ have radius $`\pi`$ in the relevant positive-dimensional cases, as detailed in [the same paper, Section 7.1](https://doi.org/10.1007/s10543-026-01141-9). The known Euclidean-metric radius $`\pi`$ concerns a different metric and does not resolve this target. [Zimmermann–Stoye, Theorem 9](https://arxiv.org/html/2405.02268v1).

## Literature status on 21 October 2026

The strongest recent direct status evidence is the published **22 June 2026** paper in *BIT Numerical Mathematics* 66, article 42: its Section 7.2 explicitly leaves this canonical case open. The corresponding [arXiv record](https://arxiv.org/abs/2511.01563) lists revision v2 dated 23 June 2026 and no later revision at review time.

Searches combined Stiefel injectivity radius, canonical metric, exact value, conjugate radius, proof, counterexample and 2026, including searches restricted to the period from 22 June through 21 October 2026 and September/October arXiv identifiers. No later matching proof or counterexample was found. This bounded search supports the recorded Open status without claiming that all unindexed work has been excluded.

The admitted page makes the universal conjecture explicit, defines the radius using open tangent balls to avoid implying uniqueness at their boundary, distinguishes the one-geodesic and Euclidean results, and supplies the dated source comparison. The existing bounds are context for the remaining exact-value target.
