# 960. Does the rescaled vectorial doubly nonlinear flow have a full limit?

**Area:** Partial differential equations; nonlinear evolution and spectral asymptotics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^n`$ be a bounded domain with smooth boundary, $`m\geq2`$, and $`1<p<\infty`$. Given $`g\in W^{1,p}_0(\Omega;\mathbb R^m)`$, consider a weak solution $`v`$ of Hynd's vectorial Dirichlet flow

```math
|v_t|^{p-2}v_t=\mathrm{div}(|Dv|^{p-2}Dv),\qquad
v|_{\partial\Omega}=0,\qquad v(\cdot,0)=g.
```


Set

```math
\Lambda_p=\inf_{0\ne u\in W^{1,p}_0(\Omega;\mathbb R^m)}
\frac{\int_\Omega |Du|^p\,dx}{\int_\Omega|u|^p\,dx},
\qquad \Upsilon_p=\Lambda_p^{1/(p-1)}.
```


Suppose, as in Hynd's Theorem 1.3, that

```math
\liminf_{t\to\infty}e^{p\Upsilon_p t}\int_\Omega|Dv(x,t)|^p\,dx>0.
```


For $`p\ne2`$, must **the entire trajectory** $`e^{\Upsilon_p t}v(\cdot,t)`$ converge strongly in $`W^{1,p}_0(\Omega;\mathbb R^m)`$ as $`t\to\infty`$ to one vectorial $`p`$-ground state? Hynd proved that every time sequence has a further ground-state convergent subsequence. The question asks whether different subsequences can select different limits. The $`p=2`$ flow decouples into heat equations, so the unresolved focus is the nonlinear vectorial case.

## Application

The flow is a nonlinear method for approaching the sharp vectorial Poincaré quotient. Full convergence would justify using a long run to select one ground state; subsequential compactness alone leaves that selection unresolved.

## References

1. R. Hynd, [*Compactness methods for doubly nonlinear parabolic systems*](https://doi.org/10.1090/tran/6828), *Transactions of the American Mathematical Society* **369** (2017), 5031–5068. Model (1.8), Theorem 1.3 and the explicit conjecture following its proof in §5; [author PDF](https://bpb-us-w2.wpmucdn.com/web.sas.upenn.edu/dist/6/47/files/2017/10/TAMSCompactness-1g9c4rx.pdf).
2. R. Hynd and E. Lindgren, [*Large time behavior of solutions of Trudinger's equation*](https://arxiv.org/abs/1702.01630), *Journal of Differential Equations* **274** (2021), 188–230. Scalar full-limit result for a related equation, not a vectorial resolution.
3. R. Hynd, B. Kawohl and P. Lindqvist, [*On the uniqueness of eigenfunctions for the vectorial $`p`$-Laplacian*](https://doi.org/10.1007/s00013-023-01920-8), *Archiv der Mathematik* **121** (2023), 745–755. Classifies vectorial Rayleigh minimizers; does not establish temporal convergence of this flow.
4. L. Bungert and M. Burger, [*Asymptotic profiles of nonlinear homogeneous evolution equations of gradient flow type*](https://arxiv.org/abs/1906.09856), arXiv:1906.09856 (2019). Related abstract gradient-flow theory with different evolution hypotheses.

## Status review


**Known cases:** Subsequential ground-state convergence and classification of vectorial ground states do not establish convergence of the whole nonlinear trajectory. Scalar and standard gradient-flow theorems use different equations or simplicity assumptions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Subsequential ground-state convergence and classification of vectorial ground states do not establish convergence of the whole nonlinear trajectory. Scalar and standard gradient-flow theorems use different equations or simplicity assumptions.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The explicit conjecture appears after Hynd's subsequential theorem. Later vectorial eigenfunction classification describes possible ground states but supplies no assertion that a trajectory cannot drift among them. Scalar and Hilbertian-flow convergence results have different state spaces or dynamics. A bounded resolution and announcement search through 2026-10-22 found no proof for this exact vectorial full-limit question. See the [source-bound original passage](../FURTHER_problems/_tracking/parallel/rough-filtering/arxiv-body-secondpass-0189-remote-attested-review.json), [status audit](../FURTHER_problems/_tracking/hynd-vectorial-full-limit-status-2026-10-22.json), and [semantic duplicate audit](../FURTHER_problems/_tracking/hynd-vectorial-full-limit-duplicates-2026-10-22.json). These checks do not establish that every possible later result has been indexed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f3817289a92134ca**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
