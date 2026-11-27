# AIM 453 — theorem-to-target comparison

Kaiwen Jin's [manuscript](paper.pdf) addresses the [AIM problem at revision b2ec0fac559f532fc0ed04fce81deea0ce07c68b](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/453-bourgain-spencer-nonperturbative-homogenization.md).

| Original requirement | Where it is proved |
| --- | --- |
| In every integer dimension $d\ge2$, the coefficient is $a=a_0(C_0*\xi)$ with vector spatial Gaussian white noise, a smooth compactly supported matrix kernel, and a $C_b^1$ symmetric matrix map satisfying $\lambda I\le a_0\le I$ for fixed $\lambda>0$. | Theorem 1 states this model. Sections 2.1 and 2.3 show how compact noise neighborhoods give the independence and stationarity needed after rescaling. Section 4 uses $d\ge2$ to make its masking event smaller than any fixed inverse power of the separation. |
| There is one collection of $2d$ constant tensors depending only on the law, with $A^1$ positive definite, for use with every deterministic compactly supported smooth vector forcing and every $0<\eta<1$. | Sections 5.1–5.2 expand the reciprocal of the physical averaged scalar response. For the original coefficient law its homogeneous polynomial terms are unique, so they agree for all choices of $\eta$ and auxiliary cell size. Section 5.2.1 constructs the tensors from those terms, with $A^1$ determined by the positive quadratic part. |
| The deterministic proxy uses the displayed recursion and $U_\varepsilon=\sum_{n=1}^{2d}\varepsilon^{n-1}v_n$. | Theorem 1 gives the same equations. Section 5.2.1 derives the signed Fourier recursion directly and shows that its finite inverse series is the specified proxy. |
| The error is measured in the whole-space $L^2$ norm of the mean gradient, bounded by $C_{f,\eta}\varepsilon^{2d-\eta}$ for every $0<\varepsilon\le1$. Constants may depend on the law and ellipticity. | Section 5.1 reconstructs the continuously stationary response, including the random lift at both endpoints. Section 5.2.1 bounds the multiplier remainder near zero by the Taylor expansion and away from zero by ellipticity and polynomial growth. Plancherel gives the global $L^2(\mathbb R^d)$ estimate. |
| Arbitrary fixed ellipticity contrast is allowed. | Sections 2.2–2.4 derive a uniformly coercive coarse operator on all edge fields and concentration of its local coefficients. Sections 3–4 control its centered inverse using sparsity and locality. The small parameter there is a chosen density of retained exceptional sites, while the starting ellipticity constant can be any $\lambda>0$ supported by the coefficient law. |

## Relation to prior results

Section 2.3 applies Propositions 1.7 and 1.10 of Armstrong, Kuusi and Mourrat to the rescaled field $b(y)=\lambda^{-1}a(Ry)$. The finite noise range gives their unit-range independence at $R$ sufficiently large. The paper uses the affine test and energy estimates to obtain forced weak-flux convergence and the constrained-energy limit. [Armstrong–Kuusi–Mourrat, author's book](https://perso.ens-lyon.fr/jean-christophe.mourrat/AKMbook.pdf).

Duerinckx's Theorem 2 gives a $d-\eta$ mixed-norm error for Gaussian-generated fields. Duerinckx, Lemm and Pagano's Corollary 3.6(i) gives the $2d-\eta$ error for sufficiently small contrast with $\eta$ above a contrast-dependent threshold. Their chain estimates inform Section 3.2. Sections 3–4 give the block estimates for the coercive inverse after short-scale propagation is summed. Conlon and Dabkowski's Theorem 1.1 concerns second differences of the averaged Green function for a lattice equation. [Duerinckx](https://arxiv.org/abs/2102.06319) · [Duerinckx–Lemm–Pagano](https://arxiv.org/abs/2406.09909) · [Conlon–Dabkowski](https://arxiv.org/html/2610.01656v1).

## Review scope

The manuscript discloses OpenAI Codex assistance in developing and checking the argument and preparing the paper. A Codex agent examined the complete mathematical argument and the applicable source results. Separate Codex contexts then read a frozen full draft as a target reader and as a mathematical referee, with earlier proof and review material withheld. The referee checked all sections, the original problem and the cited source passages. The referee identified local citation and exposition issues and requested minor revisions. The preparation agent reconciled the reports, revised the text once and checked the final version. The agents used the same provider and shared a local filesystem. The proposed resolution awaits independent mathematical review.

## Files

The [manuscript PDF](paper.pdf) and [LaTeX source](main.tex) contain the complete analytic argument. The LaTeX source builds on a standard TeX Live installation with the command `latexmk -pdf main.tex`. The [SHA-256 manifest](SHA256SUMS) identifies the exact supplied files.
