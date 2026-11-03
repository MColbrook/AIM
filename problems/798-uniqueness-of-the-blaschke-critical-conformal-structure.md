# 798. Uniqueness of the Blaschke critical conformal structure

**Area:** Projective differential geometry / geometric variational problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Sigma`$ be a connected closed oriented smooth surface with $`\chi(\Sigma)<0`$, and let $`\mathfrak p`$ be a properly convex projective structure. This means that $`\Sigma`$ is a quotient $`\Omega/\Gamma`$, where $`\Omega\subset\mathbb{RP}^2`$ is convex and bounded in an affine chart and $`\Gamma`$ acts freely and cocompactly by projective transformations. The projective structure specifies an equivalence class of torsion-free connections with the same unparametrized geodesics.

Here is an explicit definition of Mettler's conformally invariant functional. For a tensor $`T\in\Gamma(S^2T^*\Sigma\otimes T\Sigma)`$ put

```math
(T_0)^k{}_{ij}=T^k{}_{ij}-\frac13\left(\delta_i^kT^\ell{}_{j\ell}+\delta_j^kT^\ell{}_{i\ell}\right).
```

Choose any $`\nabla\in\mathfrak p`$ and any smooth Riemannian metric $`g`$. Write $`D^g`$ for its Levi-Civita connection and define

```math
B=(\nabla-D^g)_0,\qquad
X_g^k=\frac34 g^{ij}B^k{}_{ij},\qquad
A_{[g]}=(\nabla-D^g-g\otimes X_g)_0,
\qquad(g\otimes X_g)^k{}_{ij}=g_{ij}X_g^k.
```

The tensor $`A_{[g]}`$ is independent of the representative $`\nabla`$ and of replacing $`g`$ by $`e^{2f}g`$. The functional

```math
\mathcal E_{\mathfrak p}([g])
 =\int_\Sigma |A_{[g]}|_g^2\,d\mu_g
```

therefore depends only on the smooth conformal structure $`[g]`$. Call $`[g]`$ critical when

```math
\left.\frac d{dt}\right|_{t=0}\mathcal E_{\mathfrak p}([g_t])=0
```

for every smooth family of Riemannian metrics $`g_t`$ with $`g_0=g`$. These variations may change the conformal structure; the space is not quotiented by diffeomorphisms.

Let $`g_B`$ be the Blaschke metric of the properly convex projective surface. It is the metric induced by the canonical complete hyperbolic affine sphere asymptotic to the cone over $`\Omega`$, normalized to affine mean curvature $`-1`$; its induced metric descends to $`\Sigma`$. Its conformal class is known to be critical.

**Must every critical conformal structure satisfy $`[g]=[g_B]`$?**

This is Mettler's published Remark 5.5, without an added closedness assumption on the Weyl connection associated with the competing conformal structure.

## Application

The functional measures the discrepancy between prescribed unparametrized geodesics and conformal geometry. Uniqueness would characterize the canonical Blaschke conformal structure intrinsically by a variational equation for the fixed projective structure, and connect this projective-geometric construction with energy methods in higher Teichmüller theory.

## References

1. T. Mettler, *Extremal conformal structures on projective surfaces*, Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) **20** (2020), 1621–1663, [published paper](https://journals.sns.it/index.php/annaliscienze/article/download/721/708/951), especially §2.4, Theorem C and Remark 5.5 on p.1660; [arXiv:1510.01043v3](https://arxiv.org/abs/1510.01043v3), Remark 5.4 on p.39. The author's [current reformat](https://www.mettler.xyz/docs/articles/A18_print.pdf), created 26 May 2026, retains the question as Remark 5.5 on p.37.
2. T. Mettler and G. P. Paternain, *Convex projective surfaces with compatible Weyl connection are hyperbolic*, Analysis & PDE **13** (2020), 1073–1097, [doi:10.2140/apde.2020.13.1073](https://doi.org/10.2140/apde.2020.13.1073), [arXiv:1804.04616v3](https://arxiv.org/abs/1804.04616v3), Corollary 6.2. This treats zero defect, rather than all critical points.
3. T. Mettler, *Prescribing geodesics and a variational problem for Riemannian metrics* (2026), [arXiv:2605.10308v1](https://arxiv.org/abs/2605.10308v1), §§2.2–2.3 and 4. Its metric functional and conformal-variation theorem are distinct from the present target.

## Status review


**Known cases:** Mettler retains uniqueness for the Blaschke-critical conformal structure. The May 2026 prescribed-geodesics variational functional includes an additional term and its conformal criticality theorem is not uniqueness for the stated energy over all conformal structures. Minimal-Hitchin harmonic-map uniqueness concerns another variational problem.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Mettler retains uniqueness for the Blaschke-critical conformal structure. The May 2026 prescribed-geodesics variational functional includes an additional term and its conformal criticality theorem is not uniqueness for the stated energy over all conformal structures. Minimal-Hitchin harmonic-map uniqueness concerns another variational problem.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves uniqueness among critical conformal structures whose associated Weyl connection induces a flat connection on $`\Lambda^2T^*\Sigma`$. The question removes that restriction. The zero-defect rigidity theorem also does not classify critical points with positive defect.

The 2026 paper proves that each fixed conformal class contains a unique, up to homothety, conformally critical metric for a different functional. In dimension two that functional equals $`\mathcal E_{\mathfrak p}([g])+(4/3)\int_\Sigma|X_g|_g^2d\mu_g`$; conformal variations within one class do not establish the assertion here.

The separate uniqueness theorem for equivariant minimal maps into $`\mathrm{SL}(3,\mathbb R)/\mathrm{SO}(3)`$ concerns a different energy on Teichmüller space. Mettler explicitly leaves the relation to $`\mathcal E_{\mathfrak p}`$ unresolved. Searches through 17 October 2026 located no matching complete proof or counterexample. All-status AIM and OpenAI catalogue comparisons found only unrelated meanings of Blaschke; the complete 186-page cached Prove2Me listing comparison returned no matching description, and a separate selected-primary audit passed. These checks do not certify every mission proof or universal absence of a solution. See the [review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/blaschke-critical-review.json) for precise reading and search limits.

[Independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-blaschke-critical-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/blaschke-critical-duplicate-navigation.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/batch-0157-deployment-validation.json) and [coordinator review](../FURTHER_problems/_tracking/blaschke-critical-coordinator-review-2026-10-17.json) preserve the checked extents and remaining version gaps. This is a dated literature assessment, not a guarantee that no solution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-73e547ec77403dd4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
