# 970. Uniform sine–Gordon Mayer bounds below the collapse threshold

**Area:** Probability, statistical mechanics and constructive field theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Put $`X=\mathbb R^2\times\{-1,1\}`$, with Lebesgue measure in position and counting measure in charge, and write $`\xi_i=(x_i,\sigma_i)`$. Fix $`\beta\in[6\pi,8\pi)`$. For $`m>0`$ set
```math
\dot c_s^{m^2}(x)=\frac{e^{-m^2s-|x|^2/(4s)}}{4\pi s},
\qquad
\dot u_s^{m^2}(\xi_i,\xi_j)
=\beta\sigma_i\sigma_j\dot c_s^{m^2}(x_i-x_j),
```

and
```math
w_t^{m^2}(\xi)-w_s^{m^2}(\xi)
=\frac12\sum_{i,j=1}^n\int_s^t\dot u_r^{m^2}(\xi_i,\xi_j)\,dr .
```

For $`\varepsilon>0`$ and $`t>\varepsilon^2`$, define the exact kernels
```math
\widetilde v_t^1(\xi\mid\varepsilon,m)
=\exp\!\left\{-\frac{\beta}{2}
\left(\int_{\varepsilon^2}^t\dot c_s^{m^2}(0)\,ds
+\frac{\log(\varepsilon^2)}{4\pi}\right)\right\}
```

and, for $`n\ge2`$,
```math
\begin{aligned}
\widetilde v_t^n(\xi_1,\ldots,\xi_n\mid\varepsilon,m)
={}&\frac12\int_{\varepsilon^2}^t
\sum_{\substack{I_1\dot\cup I_2=[n]\\I_1,I_2\ne\varnothing}}
\sum_{\substack{i\in I_1\\j\in I_2}}
\dot u_s^{m^2}(\xi_i,\xi_j)\,
\widetilde v_s^{|I_1|}(\xi_{I_1}\mid\varepsilon,m)
\widetilde v_s^{|I_2|}(\xi_{I_2}\mid\varepsilon,m)\\
&\hspace{15mm}\times
e^{-(w_t^{m^2}(\xi)-w_s^{m^2}(\xi))}\,ds .
\end{aligned}
```

The partition sum is over ordered pairs of nonempty complementary subsets; the factor $`1/2`$ is retained. Here $`[n]=\{1,\ldots,n\}`$ and $`\xi_I`$ is the tuple with indices in $`I`$. For $`n\ge2`$, use
```math
\|f\|_n=\sup_{\xi_1\in X}\int_{X^{n-1}}
|f(\xi_1,\ldots,\xi_n)|\,d\xi_2\cdots d\xi_n .
```


Let $`n_0`$ be the largest positive integer with
```math
2(n_0-1)-\frac{\beta n_0}{4\pi}\le0.
```

Does there exist a constant $`C_\beta`$, depending only on $`\beta`$, such that for every $`n>n_0`$ and $`t>0`$ there is a measurable majorant
$`h_t^n:X^n\to[0,\infty]`$, independent of $`\varepsilon,m`$, satisfying
```math
|\widetilde v_t^n(\xi\mid\varepsilon,m)|\le h_t^n(\xi)
\quad(0<\varepsilon^2<t<m^{-2}),
\qquad
\|h_t^n\|_n\le n^{n-2}t^{-1}
\left(C_\beta t^{1-\beta/(8\pi)}\right)^n?
```

The constant must be uniform in $`n,t,\varepsilon,m`$; the majorant may depend on $`\beta,n,t`$.

This is the explicit Proposition 4.1-form interpretation of the “similar estimates” conjectured in Remark 4.2. It concerns the exact kernels above, rather than kernels modified by additional subcluster subtractions. The source proves these bounds for $`\beta<6\pi`$ with $`n=2`$ excluded; the question here isolates the remaining range.

## Application

Such bounds would control the high-order tail of the renormalized sine–Gordon potential uniformly as the ultraviolet cutoff is removed. They ask for more than existence of the sine–Gordon measure.

## References

1. R. Bauerschmidt and C. Webb, [*The Coleman correspondence at the free fermion point*](https://ems.press/content/serial-article-files/48083), J. Eur. Math. Soc. **26** (2024), 3137–3241, §4, Equations (4.3), (4.7)–(4.13), Proposition 4.1 and Remark 4.2, pp.3177–3178. DOI: [10.4171/JEMS/1329](https://doi.org/10.4171/JEMS/1329). The [latest preprint, v3](https://arxiv.org/html/2010.07096v3), dated 20 August 2025, retains the conjecture.
2. G. Benfatto, [*An iterated Mayer expansion for the Yukawa gas*](https://doi.org/10.1007/BF01009027), J. Stat. Phys. **41** (1985), 671–684. Remark 4.2 of reference 1 attributes the conjecture to p.672; this attribution was checked in that remark.
3. W. Kroschinsky and D. H. U. Marchetti, [*On the Mayer series of two-dimensional Yukawa gas at inverse temperature in the interval of collapse*](https://arxiv.org/abs/1901.00819), J. Stat. Phys. **177** (2019), 324–364. DOI: [10.1007/s10955-019-02370-9](https://doi.org/10.1007/s10955-019-02370-9).
4. S.-J. Meyer, [*An FBSDE Construction of the Sine-Gordon EQFT for* $`\beta^2<(6/7)8\pi`$ *and Perturbative Renormalization in the Full Subcritical Regime*](https://arxiv.org/abs/2607.20632), 2026.
5. J. Pelaič, [*The subcritical finite-volume massive sine-Gordon model*](https://arxiv.org/abs/2508.13778), v2, 2025.

## Status review


**Known cases:** The exact unsubtracted Mayer kernels and uniform majorant for all n above the threshold are required. Full-subcritical finite-volume constructions and further subcluster renormalization do not give these estimates for the original kernels.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The exact unsubtracted Mayer kernels and uniform majorant for all n above the threshold are required. Full-subcritical finite-volume constructions and further subcluster renormalization do not give these estimates for the original kernels.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The latest Bauerschmidt–Webb version explicitly separates this expansion question from known measure constructions. Kroschinsky–Marchetti's extension above $`6\pi`$ has a neutral-subcluster cancellation assumption whose proof is left open. Meyer's 2026 results concern finite-order modified effective potentials and a measure-construction theorem below the full threshold. Pelaič constructs finite-volume massive measures by a different renormalization approach. These statements do not establish the exact all-order, cutoff-independent majorants requested here.

The [owner review](../FURTHER_problems/_tracking/journal1169-sine-Gordon-Mayer-owner-current-scope-audit-2026-10-23.json), [independent scope review](../FURTHER_problems/_tracking/sine-gordon-exact-mayer-independent-peer-2026-10-23.json), and [semantic duplicate review](../FURTHER_problems/_tracking/sine-gordon-exact-mayer-duplicate-review-2026-10-23.json) record the precise checks and their limits. No matching proof, counterexample or announced resolution was found in those bounded checks.

The [coordinator review](../FURTHER_problems/_tracking/sine-gordon-exact-mayer-coordinator-review-2026-10-23.json) also checked the final formulas and scope. The original 1985 body and first arXiv version were not available for a matching body check; the canonical question is the directly read JEMS/current v3 remark. Current Prove2Me access timed out. No exhaustive absence of a resolution or full proof certification is claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-268412ba065c3535**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
