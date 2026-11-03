# The polynomial computational gap in spiked-tensor detection

**Area:** High-dimensional statistical inference and average-case complexity

**Status:** Held; a potentially matching theorem scope requires clarification. Not an accepted catalogue entry.

**Last checked:** 2026-09-18

## Problem statement

Fix an integer $`k\geq3`$ and a constant $`\varepsilon>0`$. For each integer $`n\geq k`$, set

```math
m=n^k,\qquad \delta_n=n^{-k/4-\varepsilon}.
```

The algorithm receives $`n`$ and the observations $`D_n=((S_j,Y_j))_{j=1}^m`$. Independently sample each $`S_j`$ uniformly from the $`k`$-element subsets of $`[n]=\{1,\ldots,n\}`$. Sampling is **with replacement across observations**: a subset can occur several times. Consider two distributions:

- Under the **null law** $`Q_n`$, all $`Y_j`$ are independent uniform signs, independent of the subsets.
- Under the **planted law** $`P_n`$, first choose $`x`$ uniformly from $`\{-1,+1\}^n`$. Independently of $`x`$ and the subsets, choose independent signs $`W_j`$ with $`\Pr(W_j=1)=(1+\delta_n)/2`$, and set

```math
Y_j=W_j\prod_{i\in S_j}x_i.
```

Repeated observations of a subset receive independent noise. The hidden vector $`x`$ is not supplied to the algorithm. Encode the indices in binary and the labels as bits, giving an explicit input of length $`O(n^k k\log n)`$.

**Conjecture:** For every fixed $`k\geq3`$ and $`\varepsilon>0`$, no uniform randomized classical algorithm, running in time polynomial in this input length, strongly distinguishes $`P_n`$ from $`Q_n`$. In formulas, no such algorithm $`A`$, with output $`1`$ meaning planted, satisfies

```math
\Pr_{D_n\sim Q_n}\{A(D_n)=1\}
+\Pr_{D_n\sim P_n}\{A(D_n)=0\}
\longrightarrow0\qquad(n\to\infty).
```

Probabilities include the algorithm's internal randomness. Its finite description and polynomial running-time bound are fixed before $`n`$ tends to infinity; they may depend on the fixed parameters. It receives only the displayed data, with no additional sample oracle or advice depending on $`n`$.

This is the dense binary formulation of the tensor-detection hardness conjecture in [1, Believed Hardness 2.1–2.2], with $`\rho=1`$ and $`\eta=2\varepsilon`$. The interesting information–computation gap is $`0<\varepsilon<(k-2)/4`$: then

```math
n\ll m\delta_n^2=n^{k/2-2\varepsilon}\ll n^{k/2}.
```

Here $`a_n\ll b_n`$ means $`a_n/b_n\to0`$. The full assertion also includes smaller signals. The question concerns strong detection, not exact recovery or the stronger requirement that every success advantage vanish.

## Applied significance

Each observation measures a noisy interaction among $`k`$ binary variables. A hidden common assignment creates consistency across many interactions, although each label is almost a fair coin. Detecting that consistency is a basic test of whether higher-order observations contain structured information. In the associated Gaussian model, the mean of each distinct-index tensor entry has the form $`\kappa\prod_{i\in S}x_i`$, making the signal a rank-one tensor.

The problem asks whether the amount of information sufficient for unrestricted statistical inference can be used with polynomial computation. A resolution would clarify a widely used model of computational limits in inference from higher-order correlations. Its relevance is foundational: it does not assert that every empirical tensor has this noise law, and it is separate from numerical approximation of a deterministic tensor.

## References

1. Guy Bresler and Alina Harbuzova, *Average-Case Reductions for $`k`$-XOR and Tensor PCA*, [arXiv:2601.19016v2](https://arxiv.org/html/2601.19016v2), revised April 2, 2026, preprint. §1, equation (1); §2.1, Believed Hardness 2.1–2.2; §6.1; Appendix C.1–C.2.
2. Zhangsong Li, *A Smooth Computational Transition in Tensor PCA*, [arXiv:2509.09904v1](https://arxiv.org/html/2509.09904v1), submitted September 12, 2025, preprint. §1, Theorem 1.1 and Definition 1.2; §2.1, Theorems 2.6–2.7. The served manuscript carries an August 24, 2026 title-page date; the inspected submission history lists only v1.
3. Pravesh K. Kothari and Jeff Xu, *Smooth Trade-off for Tensor PCA via Sharp Bounds for Kikuchi Matrices*, SODA 2026, pp. 2617–2632, [published January 7, 2026](https://epubs.siam.org/doi/10.1137/1.9781611978971.95). The inspected [full preprint, arXiv:2510.03061v1](https://arxiv.org/pdf/2510.03061v1), contains Theorems 1.8–1.11 and §4.1, Claims 4.4–4.5.
4. Songtao Mao, *Near Optimal Algorithms for Noisy $`k`$-XOR under Low-Degree Heuristic*, [arXiv:2604.10457v1](https://arxiv.org/html/2604.10457v1), April 12, 2026, preprint. Question 1.2; §3.3; Theorems 5.8 and 6.3.
5. Songtao Mao, *The Polynomial-Time Low-Degree Conjecture is False*, [arXiv:2607.20318v1](https://arxiv.org/html/2607.20318v1), July 22, 2026, preprint. Theorem 1.2 and §§1.2–1.3.
6. Shashwat Agrawal, Amitabha Bagchi and Rajendra Kumar, *Spectral Method attacks Sparse LWE, Sparse LPN and Beyond*, [arXiv:2603.27190v2](https://arxiv.org/html/2603.27190v2), revised July 2, 2026; also [IACR ePrint 2026/614](https://eprint.iacr.org/2026/614), same revision date. §1, scope of contributions; §3.4, model definitions; equation (6), Theorems 5.9 and 5.15, Corollary 5.18, Theorem 5.21 and Theorem 6.2.

## Status review

**Admission held on 2026-09-18.** Reference [1] explicitly states the binary conjecture, and Li's independently authored discussion [2, §1] retains the computational gap for the spiked-tensor family. However, the separated A52 review found a potentially matching parameter substitution in [6, Corollary 5.18 and Theorem 5.21]. The introduction describes extensions to rings of size greater than two, while the formal statements appear broader. Their relation to the preceding proof bounds at a hierarchy level close to $`n`$ also needs clarification. The [scope audit](../spiked-tensor-scope-hold.md) records the exact substitution and the unresolved issue. This draft has no problem ID and contributes nothing to the accepted count.

The binary formulation fixes a finite input representation. Connections with Gaussian formulations in [1] concern polynomial scales and allow parameter losses; no equality of sharp constant thresholds is asserted.

The positive results in [2–3] are essential to the scope. For every fixed constant $`\lambda>0`$, [2] gives polynomial-time strong detection at Gaussian signal strength $`\kappa=\lambda n^{-k/4}`$. This resolves the former smooth-transition question. It does not allow replacing the fixed constant by $`\lambda_n=n^{-\varepsilon}`$ while retaining a fixed polynomial running-time exponent. Theorem 1.11 of [3] supplies a trade-off with running time $`n^{O(\ell)}`$ and signal requirement $`\kappa\geq C_k n^{-k/4}\ell^{-(k-2)/4}`$. Reaching a fixed power below $`n^{-k/4}`$ through that bound requires $`\ell`$ to grow as a power of $`n`$; the stated guarantee is then no longer polynomial time.

Reference [4] gives high-noise algorithms and lower bounds for restricted polynomial tests. Its §3.3 sampling comparison requires the number of constraints to be small relative to the square root of the number of available subsets. That comparison does not cover $`m=n^k`$, so its Bernoulli-model theorem is not asserted here as a lower bound for the exact displayed data law. More generally, bounds for low-degree tests do not establish hardness for every polynomial-time algorithm. The counterexample in [5] uses a specially constructed graph distribution derived from a code and a rank test, rather than the independent random subsets and parity signal above; its inspected theorem does not resolve this conjecture.

Searches covered tensor PCA, spiked tensors, dense high-noise parity detection, proofs, algorithms, disproofs, corrections and version histories, including 2025–2026 and unrestricted dates. The [evidence ledger](../candidates/spiked-tensor-detection-hardness.json) also compares recent gradient algorithms, quantum/classical speedups, coded constraint designs and planted-CSP algorithms. Full model and theorem statements were inspected where relevant; all supporting proofs were not independently certified. The SODA publication metadata and its full preprint were checked, without a line-by-line comparison of the published proceedings text.

[Planted clique](../../../problems/292-planted-clique.md) concerns a different random graph signal. [Learning parity with noise](../../../problems/306-learning-parity-noise.md) uses dense uniform coefficient vectors, fixed noise and an arbitrary polynomial sample budget for recovery; the present entry asks for a particular higher-order inference threshold. Related reductions do not make these full assertions identical. [Tensor-train approximation](../../../cut_problems/problems/045-tensor-train-approximation.md) is a deterministic numerical approximation problem. All fixed orders, and the binary and Gaussian descriptions of this tensor-inference family, are treated as one entry; no additional count is assigned to recovery or other sample densities.
