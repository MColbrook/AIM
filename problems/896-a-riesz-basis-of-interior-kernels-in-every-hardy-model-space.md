# 896. A Riesz basis of interior kernels in every Hardy model space

**Area:** Operator theory and complex analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb D=\{z\in\mathbb C:|z|<1\}`$ and let $`H^2(\mathbb D)`$ be the Hardy Hilbert space, with
```math
\|f\|_{H^2}^2=\sup_{0<r<1}\frac1{2\pi}\int_0^{2\pi}|f(re^{it})|^2\,dt.
```

For a nonconstant inner function $`\theta`$ (a bounded analytic function whose boundary values have modulus one almost everywhere), put
```math
K_\theta=H^2(\mathbb D)\ominus\theta H^2(\mathbb D).
```

Its evaluation kernel at $`\lambda\in\mathbb D`$ is
```math
k_\lambda^\theta(z)=\frac{1-\overline{\theta(\lambda)}\theta(z)}{1-\overline\lambda z},
\qquad
\|k_\lambda^\theta\|_{H^2}^2=\frac{1-|\theta(\lambda)|^2}{1-|\lambda|^2}>0.
```


**Does every such $`K_\theta`$ admit a Riesz basis consisting of normalized kernels at points strictly inside $`\mathbb D`$?** Explicitly, are there distinct nodes $`(\lambda_j)`$ and constants $`0<A\le B<\infty`$ such that, with $`e_j=k_{\lambda_j}^\theta/\|k_{\lambda_j}^\theta\|`$,
```math
\overline{\mathrm{span}}\{e_j\}=K_\theta,
\qquad
A\sum_j|a_j|^2\le\left\|\sum_j a_j e_j\right\|_{H^2}^2
\le B\sum_j|a_j|^2
```

for every finitely supported complex coefficient sequence?

The index set may be finite when $`K_\theta`$ is finite dimensional. The nodes and bounds may depend on $`\theta`$. No restriction to zeros of $`\theta`$, meromorphic inner functions, connected level sets or boundary kernels is imposed. This is the existential unconditional-basis question in Fricain's Remark 2.2.12 [1]; normalization converts the Hilbert-space unconditional-basis formulation to the Riesz bounds above.

## Application

Such a basis gives stable coordinates and reconstruction from normalized point evaluations in a model space. These spaces represent compressed shifts and contraction operators; particular cases connect to nonharmonic Fourier expansions. The question asks for a suitable stable sampling system for each space, without prescribing an algorithm or bounds uniform over all inner functions.

## References

1. E. Fricain, *Complétude des noyaux reproduisants dans les espaces modèles*, Annales de l'Institut Fourier **52** (2002), 661–686, [DOI](https://doi.org/10.5802/aif.1897), [published PDF](https://www.numdam.org/item/10.5802/aif.1897.pdf), Corollary 2.2.11 and Remark 2.2.12, pp. 678–679.
2. A. Baranov and Yu. Belov, *Systems of reproducing kernels and their biorthogonal: completeness or incompleteness?*, [arXiv:1005.1197v2](https://arxiv.org/pdf/1005.1197v2) (2011), Section 1.5 and Theorem 4.1. This author version explicitly separates the basis-existence problem from a different biorthogonal-completeness question.
3. A. Baranov, *Stability of the bases and frames reproducing kernels in model spaces*, Annales de l'Institut Fourier **55** (2005), 2399–2422, [DOI](https://doi.org/10.5802/aif.2165), [published PDF](https://www.numdam.org/item/10.5802/aif.2165.pdf), introductory criteria and connected-level-set discussion, pp. 2401–2403.

## Status review


**Known cases:** Complete systems of interior kernels and criteria for specified sequences do not establish existence of a Riesz kernel basis in every model space. Biorthogonal-incompleteness counterexamples concern a chosen exact system, not all possible bases of that space. Meromorphic-inner and doubling-weight results impose additional restrictions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Complete systems of interior kernels and criteria for specified sequences do not establish existence of a Riesz kernel basis in every model space. Biorthogonal-incompleteness counterexamples concern a chosen exact system, not all possible bases of that space. Meromorphic-inner and doubling-weight results impose additional restrictions.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 30 October 2026. Source [1] proves existence of complete interior kernel sequences, which is weaker than the two-sided basis bounds. Source [2] explicitly retains the existential Riesz-basis question. Its counterexamples concern a chosen exact kernel system whose biorthogonal is incomplete; they do not rule out a different suitable basis for the same space. Criteria and stability results in [3] concern specified sequences or restricted inner classes and do not establish existence for every inner function.

Bounded current searches, including announced completions, found no matching full resolution. The May 2026 revision of [Bergman's inner-approximation paper](https://arxiv.org/abs/2509.21229v4) was checked at abstract/history level: its stated doubling-weight and meromorphic-inner applications do not assert this unrestricted basis theorem. No full-body review of that comparator is claimed. Boundary Clark kernels, finite partitions into Riesz basic sequences and counterexamples in other reproducing-kernel spaces do not by themselves answer the displayed question.

All-status AIM, announced-result and private-candidate records were compared. The existing question about uniform approximation of Blaschke products by interpolating products has a different phase-sensitive approximation target; no equivalence with this basis question was asserted in the checked sources. The [coordinating review](../FURTHER_problems/_tracking/ROOT-FINAL-Nikolski-interior-kernel-Riesz-basis-current-and-semantic-admission-20261030.json), [current-source check](../FURTHER_problems/_tracking/AIF109/RIESZ-CURRENT-GATE.json) and [independent model review](../FURTHER_problems/_tracking/AIF109/C-INDEPENDENT-EXISTENTIAL-INTERIOR-NORMALIZED-KERNEL-RIESZ-BOUNDS-MODEL-PEER-PASS.json) record the evidence and limits. These are bounded AI checks, not human peer review or a proof that no unindexed resolution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-21ea526e3bba56c9**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
