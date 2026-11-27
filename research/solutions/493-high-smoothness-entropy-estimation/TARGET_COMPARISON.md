# AIM 493 target comparison

[Minimax entropy estimation beyond two derivatives](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/493-high-smoothness-entropy-estimation.md) asks for the minimax root-mean-square error for entropy over a compactly supported Lipschitz class. [The manuscript](paper/main.pdf) gives a proposed resolution for the full target.

| Requirement | Location and coverage |
| --- | --- |
| Probability densities on the unit cube, with the norm on the zero extension | Section 1 gives the exact density class and its whole-space difference modulus. Section 2 derives Fourier estimates from that norm. |
| All integer dimensions $`d\ge3`$, real $`s>2`$, finite $`2\le p<\infty`$, sufficiently large fixed $`L`$ | Theorem 1 specifies the parameter range and a radius threshold depending only on $`d,s,p`$. The order $`r=\lceil s\rceil`$ is used at integer and noninteger smoothness. |
| Densities may vanish | Section 3 uses signed local projections and controls the logarithm near zeros. Section 2 adds a floor to the internal likelihood candidates. |
| Uniform risk over the class for measurable estimators based on $`n`$ iid observations | Section 2 gives the likelihood-mixture bound for $`s\ge d`$, including $`s=d`$. Sections 3–6 give the nonparametric upper bound for $`2<s<d`$. Section 6.3 returns to a deterministic measurable estimator in the original fixed-sample experiment. |
| Two-sided order $`(n\log n)^{-s/(s+d)}+n^{-1/2}`$ in root-mean-square loss | Theorem 1 states both inequalities with constants and a sample-size cutoff depending only on $`d,s,p,L`$. Section 1 applies the lower-bound clause of Theorem 1 in [Han, Jiao, Weissman and Wu, version 4](https://arxiv.org/abs/1711.02141v4) after matching equations (1)–(5) and the radius window. |

The likelihood comparison in Section 2 credits [Yang and Barron](https://doi.org/10.1214/aos/1017939142). The matching upper bound for $`2<s<d`$ uses the amplitude-band count from Section 3 and the signed local estimator from Sections 4–6. The result is analytic and makes no computational-efficiency claim.

## Review scope

Codex assisted with proof development, natural-language checking and manuscript preparation. The argument underwent a full natural-language AI audit. Before the final author revision, a fresh AI reader and a fresh AI referee each examined the same frozen manuscript with scoped inputs and no access to the other's report. Both roles used the same provider and host. The referee reported no surviving substantive gap within that scope. The proposed resolution awaits independent mathematical review.

## Build

Run `latexmk -cd -pdf paper/main.tex` in this package, or compile [the editable source](paper/main.tex) with pdfLaTeX from the paper directory. The included SHA-256 manifest identifies the PDF, TeX sources and target comparison.
