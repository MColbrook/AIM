# 983. Coupled reflecting boundaries in the Case IID Brownian control problem

**Area:** Singular stochastic control and Brownian models of queueing networks
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix positive rates $`\lambda_1,\lambda_2,\mu_1,\mu_2,\mu_3`$ satisfying
```math
\frac{\lambda_1}{\mu_1}+\frac{\lambda_2}{\mu_2}=1,
\qquad \lambda_2=\mu_3.
```

Let $`\gamma>0`$, $`b_1,b_2,b_3\in\mathbb R`$, and $`c_1,c_2,c_3>0`$. The holding costs are in **Case IID**:
```math
c_2<c_3,\qquad c_2\mu_2<c_1\mu_1.
```

Take five independent, centred Brownian motions $`A_1,A_2,S_1,S_2,S_3`$, starting at zero, with respective variance rates
```math
\lambda_1\sigma_1^2,\quad \lambda_2\sigma_2^2,\quad
\lambda_1\zeta_1^2,\quad \lambda_2\zeta_2^2,\quad \mu_3\zeta_3^2,
```
where $`\sigma_i,\zeta_j\geq0`$ are finite. Define the workload Brownian motion by
```math
\begin{aligned}
B_1(t)&=(b_1+b_2)t+
\frac{A_1(t)-S_1(t)}{\mu_1}+
\frac{A_2(t)-S_2(t)}{\mu_2},\\
B_2(t)&=b_3t+\frac{A_2(t)-S_3(t)}{\mu_3}.
\end{aligned}
```

Assume its covariance matrix is positive definite. This is the nondegenerate workload part of the conjecture; the Brownian law is the one defined by these primitives.

For $`w\in\mathbb R_+^2`$, let
```math
h(w)=\min\left\{
\sum_{j=1}^3c_jq_j:
q_j\geq0,\quad
\frac{q_1}{\mu_1}+\frac{q_2}{\mu_2}=w_1,\quad
\frac{q_2+q_3}{\mu_3}=w_2
\right\}.
```

An admissible control $`I=(I_1,I_2)`$ is adapted, right-continuous with left limits, and componentwise nondecreasing, with $`I(0)=0`$, such that $`W=B+I`$ stays in $`\mathbb R_+^2`$ almost surely. The filtration makes the driving motions Brownian. The objective is to minimize
```math
J(I)=\mathbb E\int_0^\infty e^{-\gamma t}h(W(t))\,dt.
```

Do there always exist Lipschitz, strictly increasing functions $`\Psi_i:[0,\infty)\to[0,\infty)`$, with $`\Psi_i(z)\to\infty`$ as $`z\to\infty`$, such that
```math
\begin{aligned}
I_1^*(t)&=\sup_{0\leq s\leq t}
       [B_1(s)-\Psi_1(W_2^*(s))]^-,\\
I_2^*(t)&=\sup_{0\leq s\leq t}
       [B_2(s)-\Psi_2(W_1^*(s))]^-,\\
W^*&=B+I^*
\end{aligned}
```
has a unique adapted continuous nonnegative state solution and $`I^*`$ is admissible and optimal? Here $`u^-=\max\{-u,0\}`$.

The functions may depend on all the fixed model data. The initial workload is zero, and no initial control jump is allowed; in particular the asserted equations force $`\Psi_i(0)=0`$. The uniqueness assertion concerns the state solution for fixed boundary functions.

This is the nondegenerate, primitive-defined part of Conjecture 1.1 of [2], with the strict Case IID inequalities. Its use of the workload definition does not impose the paper's Case IIB main-theorem cost sign.

## Application

The two workload coordinates describe a crisscross service network in heavy traffic. A rigorous coupled-boundary description would identify how both workloads should be regulated when both reflecting boundaries must be determined.

## References

1. A. Budhiraja and K. Ross, *Optimal stopping and free boundary characterizations for some Brownian control problems*, Annals of Applied Probability 18(6) (2008), 2367-2391. [DOI](https://doi.org/10.1214/08-AAP525), [author version](https://arxiv.org/abs/0901.2474v1). The Case IID discussion is on pp. 4-5 of the author version; the one-boundary result treats Case IIB.
2. A. Budhiraja, X. Liu and S. Saha, *Construction of Asymptotically Optimal Control for Crisscross Network from a Free Boundary Problem*, Stochastic Systems 6(2), 459-518, published online 7 March 2017 (issue dated December 2016). [DOI](https://doi.org/10.1287/15-SSY211), [author version](https://arxiv.org/abs/1502.02320v1). See Conjecture 1.1, Definition 4.2, the cost LP, and the underlying arrival/service balance equations.
3. B. Ata, J. M. Harrison and N. Si, *Singular control of (reflected) Brownian motion: a computational method suitable for queueing applications*, Queueing Systems 108 (2024), 215-251. [DOI](https://doi.org/10.1007/s11134-024-09910-5). Section 6 gives numerical Case IID policies and distinguishes them from the earlier rigorous IIB/IIC results.

## Status review


**Known cases:** Strict Case IID needs two coupled increasing reflecting boundaries and uniqueness of the state solution. The rigorous Case IIB/IIC results and 2024 computed IID policies do not prove the conjecture.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Strict Case IID needs two coupled increasing reflecting boundaries and uniqueness of the state solution. The rigorous Case IIB/IIC results and 2024 computed IID policies do not prove the conjecture.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2017 published paper retains the Case IID conjecture. The 2024 numerical control policies and MDP comparisons do not establish the asserted continuous Brownian coupled-boundary theorem. Current and announced-resolution searches on 27 October 2026 located no matching complete solution, and comparison with the all-status AIM/OpenAI corpus and developing collection located no duplicate.

The workload above is explicitly constructed from the independent arrival/service Brownian primitives. The printed three-dimensional covariance display in [2] has a service-variance index discrepancy: it uses $`\zeta_1`$ in class-2 covariance entries while the class-2 balance equations use service process $`S_2`$. The stated primitive definition specifies the law directly; it does not silently reproduce that display or extend the conjecture to arbitrary workload covariances.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8b2a3f446fb7e944**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
