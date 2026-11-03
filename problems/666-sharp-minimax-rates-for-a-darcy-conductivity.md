# 666. Sharp minimax rates for a Darcy conductivity

**Area:** Bayesian inverse problems and uncertainty quantification
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`D=\{x\in\mathbb R^d:|x|<1\}`$, where $`d\ge2`$, and fix an integer $`\alpha>\max\{d/2+2,2d-1\}`$. Fix $`0<r<1`$ and $`R>\|1\|_{H^\alpha(D)}`$. Define

```math
\mathcal F_{\alpha,r}(R)=\left\{f\in H^\alpha(D):\inf_D f>r,\ \|f\|_{H^\alpha}\le R,\ f|_{\partial D}=1,\ \partial_n^j f|_{\partial D}=0\ (1\le j\le\alpha-1)\right\},
```

with boundary derivatives understood as Sobolev traces. For $`f`$ in this class, let $`u_f`$ solve

```math
\nabla\cdot(f\nabla u_f)=1\quad\text{in }D,\qquad u_f=0\quad\text{on }\partial D.
```

Observe the Gaussian white-noise experiment

```math
Y_\varepsilon(h)=\langle u_f,h\rangle_{L^2(D)}+\varepsilon W(h),\qquad h\in L^2(D),
```

where $`W`$ is isonormal Gaussian white noise and $`\varepsilon\downarrow0`$. Equivalently one observes all coordinates in a fixed orthonormal basis; $`W`$ is not an $`L^2`$-valued error vector.

Determine the sharp asymptotic order, including any logarithmic factors, of

```math
\mathcal R_\varepsilon=\inf_{\widehat f}\sup_{f\in\mathcal F_{\alpha,r}(R)}\mathbb E_f\|\widehat f(Y_\varepsilon)-f\|_{L^2(D)},
```

where the infimum ranges over measurable $`L^2(D)`$-valued estimators. Seek matching upper and lower bounds up to constants depending on the fixed class parameters.

No radial restriction or nonvanishing-gradient assumption is imposed. A known upper bound is $`\mathcal R_\varepsilon\lesssim\varepsilon^{2(\alpha-1)/(2\alpha+2+d)}`$; its optimality for conductivity loss is not established by the matching lower bound for estimating $`u_f`$ in $`H^2`$ prediction loss.

## Application

This asks for the statistical information limit in recovering a spatial conductivity or permeability from a single noisy interior diffusion field, independently of an estimator's computational cost or prior choice.

## References

1. R. Nickl, S. van de Geer and S. Wang, *Convergence Rates for Penalized Least Squares Estimators in PDE Constrained Regression Problems*, SIAM/ASA Journal on Uncertainty Quantification **8**(1) (2020), 374–413, [DOI](https://doi.org/10.1137/18M1236137); [latest preprint](https://arxiv.org/pdf/1809.08818v3), §3.1, Theorems 9–11 and the open-rate discussion on p.11. The parameter class and experiment are from this preprint; the unit ball and source one also occur in its Theorem 10.
2. M. Giordano and R. Nickl, *Consistency of Bayesian inference with Gaussian process priors in an elliptic inverse problem*, Inverse Problems **36** (2020), 085001, [DOI](https://doi.org/10.1088/1361-6420/ab7d2a); [preprint](https://arxiv.org/pdf/1910.07343v3), §2.3.2. This discusses the corresponding fixed-Sobolev rate question in random-design regression.

## Status review


**Known cases:** The First Proof batch-3 human theorem treats a sufficiently small Holder-Zygmund ball about the constant conductivity and identifies a rate only up to logarithmic factors. It does not treat this fixed general Sobolev ball with unrestricted allowed amplitude and sharp unsquared expected loss including logarithms. The source Theorem 13 still explicitly leaves the general Sobolev reconstruction rate open.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The First Proof batch-3 human theorem treats a sufficiently small Holder-Zygmund ball about the constant conductivity and identifies a rate only up to logarithmic factors. It does not treat this fixed general Sobolev ball with unrestricted allowed amplitude and sharp unsquared expected loss including logarithms. The source Theorem 13 still explicitly leaves the general Sobolev reconstruction rate open.

Additional comparison sources: [comparison source 1](https://github.com/1stproof/batch-3); [comparison source 2](https://hexagonmath.org/2610.00244v1); [comparison source 3](https://arxiv.org/html/2409.18415v3); [comparison source 4](https://doi.org/10.1137/18M1236137); [comparison source 5](https://arxiv.org/pdf/1809.08818v3); [comparison source 6](https://doi.org/10.1088/1361-6420/ab7d2a); [comparison source 7](https://arxiv.org/pdf/1910.07343v3); [comparison source 8](https://arxiv.org/html/2411.19797v1); [comparison source 9](https://iris.unibocconi.it/bitstream/11565/4080556/1/Inverse_main.pdf); [comparison source 10](https://raw.githubusercontent.com/1stproof/batch-3/main/batch-3-human-solution/problem-02/human-solution.tex). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Checked 17 October 2026.** Nickl's 2023 book and the latest version located of *Consistency of Variational Inference for Nonlinear Inverse Problems of Partial Differential Equations*, [2409.18415v3](https://arxiv.org/html/2409.18415v3), §4.1, retain the general-Sobolev Darcy reconstruction-rate question. The newer [linear-method approach](https://arxiv.org/html/2411.19797v1), Theorem 7.2, uses the smoothness of $`\Delta u_f`$ and provides contraction upper bounds; it does not supply matching minimax bounds for this conductivity class. The independently inspected [revised institutional manuscript](https://iris.unibocconi.it/bitstream/11565/4080556/1/Inverse_main.pdf), Theorem 7.2 and Remark 7.3, retains a Laplacian eigenscale parameterization and boundary conditions. Its minimax lower bound, Theorem 4.6, is for the potential equation with $`c(f,u)=2fu`$, which does not include Darcy conductivity. Its final 2026 paginated publication remains an access and parity gap; the institutional text is not labelled as that edition.

An independent selected-primary audit and the coordinator checked the exact class, expected unsquared loss and direction of the prediction/reconstruction implications. The current institutional revision and the June 2026 explicit open-rate discussion support retaining this precise question; the unavailable final body is recorded as a version limit, not silently assumed identical. No matching theorem or announcement for this exact class was located.

All-status AIM/OpenAI and FURTHER comparisons found no equivalent target. In particular, AIM 046–049 concern deterministic boundary-map identifiability, and the other admitted Darcy problem concerns forward electroconvection, rather than this statistical inverse experiment. The fresh 186-page catalogue scan returned no context for the six specified Darcy aliases. Listing comparisons do not certify mission proof bodies.

The [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/darcy-sobolev-minimax-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-darcy-sobolev-minimax-review.json), [catalogue receipt](../FURTHER_problems/_tracking/parallel/complex-bayesian/darcy-sobolev-prove2-0095-review.json) and [coordinator checks](../FURTHER_problems/_tracking/coordinator-selected-status-2026-10-17.json) preserve exact reading and search extents. The original author text was read in full; published-version parity and the separately recorded source-proof caveat remain explicit. No optimal exponent is proposed without evidence, and bounded negative searches do not prove openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-41e33c9bb7232ceb**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
