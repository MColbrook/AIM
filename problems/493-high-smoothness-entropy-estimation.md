# 493. Minimax entropy estimation beyond two derivatives

**Area:** Nonparametric statistics and information estimation

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-11-27

## Problem statement

Fix $`d\ge3`$, $`s>2`$, $`2\le p<\infty`$ and a sufficiently large fixed radius $`L`$. Put $`r=\lceil s\rceil`$ and define

```math
\Delta_h^r f(x)=\sum_{j=0}^r(-1)^{r-j}\binom rj f\bigl(x+(j-r/2)h\bigr),\qquad
\omega_r(f,t)_p=\sup_{|h|\le t}\|\Delta_h^r f\|_{L^p(\mathbb R^d)}.
```

Let $`\mathcal F_{s,p,d}(L)`$ contain the probability densities supported on $`[0,1]^d`$ satisfying

```math
\|f\|_{L^p(\mathbb R^d)}+\sup_{t>0}t^{-s}\omega_r(f,t)_p\le L.
```

Here $`f`$ is extended by zero, so the norm also constrains its boundary behaviour. No positive lower bound on $`f`$ is imposed. Given $`n`$ independent observations with density $`f`$, estimate

```math
H(f)=-\int_{[0,1]^d}f(x)\log f(x)\,dx,\qquad 0\log0=0.
```

Determine, up to constants depending on $`s,p,d,L`$, the asymptotic order of

```math
R_n=\inf_{\widehat H}\sup_{f\in\mathcal F_{s,p,d}(L)}
\left(\mathbb E_f|\widehat H-H(f)|^2\right)^{1/2}.
```

The infimum is over measurable estimators based on the observations. In particular, is the known lower bound

```math
R_n\gtrsim(n\log n)^{-s/(s+d)}+n^{-1/2}
```

sharp throughout this high-smoothness regime? This is one rate-characterization problem, not separate entries for individual dimensions or exponents.

## Application

Differential-entropy estimation supports independence testing and independent component analysis. Sharp rates would quantify the sample cost of estimating this information measure for smooth densities that can approach zero; they would not by themselves establish optimal rates for every downstream test.

## References

1. Y. Han, J. Jiao, T. Weissman and Y. Wu, *Optimal rates of entropy estimation over Lipschitz balls*, Annals of Statistics **48** (2020), 3228–3250, [published article](https://doi.org/10.1214/19-AOS1927). The [author manuscript](https://arxiv.org/abs/1711.02141), version 4, defines the class in equations (1)–(4), gives the lower bound in Theorem 1 and discusses $`s>2`$ in §4.2, pp. 21–22.
2. T. B. Berrett, R. J. Samworth and M. Yuan, *Efficient multivariate entropy estimation via k-nearest neighbour distances*, Annals of Statistics **47** (2019), 288–318, [article](https://doi.org/10.1214/18-AOS1688); [manuscript](https://arxiv.org/abs/1606.00304), §2 and Theorem 1. Its relative smoothness conditions differ from the displayed class.
3. T. B. Berrett and R. J. Samworth, *Efficient functional estimation and the super-oracle phenomenon*, [author manuscript](https://arxiv.org/abs/1904.09347); [2023 accepted manuscript](https://api.repository.cam.ac.uk/server/api/core/bitstreams/22e87d27-4f33-4443-b3a6-68bea54919a9/content), §2, pp. 5–7. The efficiency theorem imposes additional integrability conditions involving local smoothness divided by the density.

## Status review

A proposed resolution establishes the two-sided minimax root-mean-square rate for the displayed class over the full parameter range. The analytic proof uses a likelihood mixture when $`s\ge d`$ and signed local polynomial estimation when $`2<s<d`$.

[Manuscript](../research/solutions/493-high-smoothness-entropy-estimation/paper/main.pdf) · [Target comparison and AI review scope](../research/solutions/493-high-smoothness-entropy-estimation/TARGET_COMPARISON.md). The submission awaits independent mathematical review.

The earlier literature review on 23 September 2026 identified the high-smoothness upper-bound question. The present status records the new proposed proof.
