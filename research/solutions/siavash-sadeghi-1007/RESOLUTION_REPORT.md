# Resolution report: AIM 1007

**Author and submitter:** Siavash Sadeghi.

**Target revision:** `ee5c5c52f527db2f310cb0734bbebc9f7b95aac8`.

**Target:** [Embedded eigenvalues in asymptotically flat twisted strips](https://github.com/MColbrook/AIM/blob/ee5c5c52f527db2f310cb0734bbebc9f7b95aac8/problems/1007-embedded-eigenvalues-in-asymptotically-flat-twisted-strips.md).

**Proposed outcome:** Negative; an embedded eigenvalue satisfies all the stated hypotheses.

**Evidence status:** Solution claimed, supported by a fresh AI mathematical audit and exact algebra checks. No human audit or formal verification is claimed.

## Claim

For unit half-width, let

```math
m=\frac13-\frac2{\pi^2},\qquad k=(2m)^{-1/2},\qquad
\lambda_* = \frac{\pi^4}{4(\pi^2-6)}.
```

For every sufficiently large scale $`S`$, the proof selects a phase $`\delta\in[0,2\pi]`$ for which

```math
q(s)^2=\frac{16k}{S+|s|}\left(1+\frac12\cos(2k|s|+\delta)\right)
```

produces a nonzero weighted-square-integrable eigenfunction at $`E_1<\lambda_*<E_2`$. This is an analytic existence result. The threshold scale and selected phase are not given numerically.

## Comparison with every target condition

| Repository requirement | Construction and justification |
| --- | --- |
| Ambient dimension $`n+1\ge3`$ | Choose the three-coordinate ribbon and append zero coordinates for any larger dimension. |
| Unit-speed $`C^{1,1}`$ reference curve | $`\Gamma(s)=(s,0,\ldots,0)`$ is smooth and unit speed. |
| Relatively parallel normal frame | Use the constant normal frame along the straight line. |
| Lipschitz unit twisting vector | $`\theta(s)=\int_0^s q(r)dr`$ and $`\Theta=(\cos\theta,\sin\theta,0,\ldots,0)`$ give $`|\Theta'|=q`$ a.e.; bounded $`q`$ gives global Lipschitz continuity. |
| Pure twisting $`k_{\rm curve}\cdot\Theta=0`$ | The reference curve has zero curvature. The scalar resonance parameter $`k`$ is distinct from this curvature. |
| Nontrivial twist | The displayed profile is positive everywhere. |
| Amplitude bound | $`q^2\le24k/(S+|s|)`$ gives $`\|q\|_\infty\le\sqrt2`$ for $`S\ge12k`$. |
| Decay at both ends | The same bound gives uniform decay of $`q`$ as $`|s|\to\infty`$. |
| All-Dirichlet strip operator | The metric is exactly $`\operatorname{diag}(1+t^2q^2,1)`$, with the same weighted Hilbert space and quadratic form as the source. The function has zero transverse traces. |
| Exact eigenfunction, not a scalar approximation | All closed transverse modes are eliminated by a convergent operator inverse. The remaining exact equation is solved by a second convergent inverse. |
| Full-line matching | Antiperiodicity in the phase supplies a zero of $`u_\delta'(0)`$. Closed-mode derivatives are already zero at the interface; even reflection gives an $`H^2\cap H_0^1`$ function and zero joining flux. |
| Eigenvalue strictly above threshold | $`\lambda_*-E_1=3\pi^2/[2(\pi^2-6)]>0`$, while $`E_2-\lambda_*=3\pi^2(\pi^2-8)/[4(\pi^2-6)]>0`$. |
| Every half-width $`a>0`$ | $`q_a(s)=a^{-1}q(s/a)`$ and the unitary dilation $`U_a\psi=a^{-1}\psi(s/a,t/a)`$ scale the eigenvalue to $`a^{-2}\lambda_*`$. |
| Embedded point spectrum | The source's Theorem 3.1 gives essential spectrum $`[E_1,\infty)`$; the weak eigenvalue identity places the constructed nonzero function in the operator domain. |

One admissible counterexample already refutes the universal absence assertion. The construction in fact scales to every half-width and embeds in every allowed ambient dimension. It does not address the source's separate resonance question, which the repository explicitly excludes. It does not contradict the known Hardy bound or claim an eigenvalue at or below threshold.

## Review and submission

The [proof](twisted-strip-counterexample.pdf) was reviewed afresh by Codex (AI) on 3 November 2026; see the step-by-step [audit](MATHEMATICAL_AUDIT.md). The original package's statements about previous agent reviews were treated as provenance claims, not verification evidence. No complete proof gap was identified in this audit. The repository page and metadata are proposed as **Solution claimed**, with proof and audit links, and generated indexes updated by the repository generator.
