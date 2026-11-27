# Target comparison for AIM Problem 483

[Original statement at the pinned revision](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/483-nonlinear-diffusion-renormalization-mass-conservation.md)

The claim is a counterexample to the full conservation assertion. Theorem 1 of [the manuscript](paper.pdf) constructs a solution of the prescribed truncated identity with $q$-mass strictly larger than its prescribed initial value for every $0<t\le t_*$.

| Original requirement | Verification in the manuscript |
| --- | --- |
| Smooth bounded domain, at least two species, positive diffusivities, all exponents in $(0,2)$, and at least one nonlinear exponent | Section 2 chooses $\Omega=(0,1)$, five species, $d_i=1$, and exponents $(1/8,1,1,1,1)$. |
| Locally Lipschitz, quasi-positive reaction on the entire nonnegative cone | Section 4.1 defines a single autonomous $f$. The time-label cutoff makes the first three components locally zero at each finite state at the time threshold. Evenness of the prescribed profiles gives a Lipschitz composition with the extended spatial inverse. Each $f_i$ vanishes on its own zero-coordinate face. |
| Reaction entropy bound at every strictly positive state | Sections 3.3 and 4.1 establish the required bound along the profiles and on the full positive cone with $\mu_i=0$. The correction in the definition of $f_3$ preserves exact matching along the profiles. |
| Nonnegative finite-entropy data and the original mass and half-power energy spaces on every finite cylinder | Sections 3.1 and 3.4 verify the time-integrable energies, including at zero. Section 4.2 gives the assigned data. Section 4.3 provides the global extension from the positive, smooth terminal state of the explicit segment. |
| Every compact-gradient concentration test, every smooth closed-domain space-time test, almost every terminal time, and the original flux and mixed gradient terms | Section 4.2 proves the full identity by integration by parts on positive-time strips and bounded convergence in the initial term. Section 4.3 uses the continuation's prescribed initial term to concatenate the identities. |
| An admissible real invariant and a violation of the almost-everywhere conclusion | The invariant is $q=(1,1,0,0,0)$, with $q\cdot f=0$ on the entire cone. Section 4.3 computes the mass difference $M=\int_0^1\phi(y)\,dy>0$ on a positive-measure interval. |

The constructed first segment uses the original formulation without a solution entropy inequality or mass-conservation axiom. The sole imported PDE existence result supplies a continuation from smooth positive data at time $t_*$. [FFKT, Theorem 1.3 and Remark 1.4](https://doi.org/10.1007/s00332-023-09926-w)

## Review scope

An AI mathematical audit assessed the complete natural-language proof and the applicability of its existence source. A separate PDE reader and a separate AI referee examined the same frozen manuscript. The referee found no major objection and requested two local revisions. The final text addresses those requests and the reader's exposition findings. The reader and referee worked in separate AI contexts on a shared machine with limited prior task framing. They reported no exposure to the other report. The submission is a proposed solution.

Build the manuscript from [paper.tex](paper.tex) with `latexmk -pdf -halt-on-error -interaction=nonstopmode paper.tex`. The proof is analytic.
