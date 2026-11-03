# 791. Primitive inequalities for convex support functions on simplicial fans

**Area:** Convex and algebraic geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge1`$, let $`N\cong\mathbb Z^n`$, and set $`N_{\mathbb R}=N\otimes_{\mathbb Z}\mathbb R`$. Let $`\Sigma`$ be a finite rational simplicial fan in $`N_{\mathbb R}`$ with convex, full-dimensional support $`|\Sigma|`$. Here a fan is a collection of strongly convex rational polyhedral cones, closed under faces, such that the intersection of two cones is a face of each. Simplicial means that the generators of each cone are linearly independent.

Write $`\Sigma(1)`$ for its rays and $`v_\rho\in N`$ for the primitive generator of a ray $`\rho`$. A *primitive collection* is a subset $`P\subseteq\Sigma(1)`$ that is not contained in any cone of $`\Sigma`$, although every proper subset is contained in a cone.

Let $`\varphi:|\Sigma|\to\mathbb R`$ be continuous and linear on each cone. Suppose that every primitive collection satisfies
```math
\sum_{\rho\in P}\varphi(v_\rho)
\ \ge\ 
\varphi\!\left(\sum_{\rho\in P}v_\rho\right).
```

Convexity of the support makes the argument on the right well defined. Must
```math
\varphi(u)+\varphi(v)\ge\varphi(u+v)
\qquad\text{for all }u,v\in|\Sigma|?
```

The function is positively homogeneous, so this is the usual convexity condition on its support. The conjecture asks whether the finitely many primitive inequalities suffice. No completeness, smoothness or quasi-projectivity is assumed.

## Application

This would describe a cone of real convex piecewise-linear functions using explicit linear inequalities. In toric geometry, quotienting this cone by linear functions describes the nef cone. The unresolved extension concerns fans that need not admit a strictly convex support function.

## Known cases and scope

Cox and von Renesse prove the criterion under quasi-projectivity (Theorem 1.4); their published Conjecture 4.2 removes that hypothesis in the simplicial case. Their discussion also records a result of Casagrande for smooth complete fans admitting a toric blow-up to a projective variety. These are special cases of the question above.

The projective hypothesis in Cox–Little–Schenck, Theorem 6.4.9, and the standing restriction to normal fans in Ardila–Castillo–Eur–Postnikov do not establish the general assertion. Chang–Chen, Theorem 2.5, concerns strict inequalities and ampleness; it does not settle this weak inequality criterion without a quasi-projectivity assumption.

## References

- D. A. Cox and C. von Renesse, *Primitive Collections and Toric Varieties*, Tohoku Mathematical Journal **61** (2009), 309–332, especially Definitions 1.1 and 1.3, Theorem 1.4, and Conjecture 4.2 on p. 331. [Published paper](https://doi.org/10.2748/tmj/1255700197); [arXiv version history](https://arxiv.org/abs/0808.1836).
- C. Casagrande, *Contractible classes in toric varieties*, Mathematische Zeitschrift **243** (2003), 99–126, Theorem 5.6 (special case cited by Cox and von Renesse).
- D. A. Cox, J. B. Little and H. K. Schenck, *Toric Varieties*, Graduate Studies in Mathematics **124**, American Mathematical Society, 2011, Theorem 6.4.9.
- F. Ardila, F. Castillo, C. Eur and A. Postnikov, *Coxeter submodular functions and deformations of Coxeter permutahedra*, Advances in Mathematics **365** (2020), 107039, Section 2 and Lemma 2.14. [Paper](https://doi.org/10.1016/j.aim.2020.107039); [arXiv](https://arxiv.org/abs/1904.11029).
- C.-W. Chang and Y.-A. Chen, *Boundedness of toric foliations*, arXiv:2502.11080 (2025), Theorem 2.5. [Preprint](https://arxiv.org/abs/2502.11080).

## Status review


**Known cases:** The fan is simplicial with convex full-dimensional support but need not be complete or quasi-projective. The Cox-von Renesse quasi-projective theorem and unrelated non-simplicial or extremal-wall assertions do not settle its primitive-inequality conjecture.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The fan is simplicial with convex full-dimensional support but need not be complete or quasi-projective. The Cox-von Renesse quasi-projective theorem and unrelated non-simplicial or extremal-wall assertions do not settle its primitive-inequality conjecture.

Additional comparison sources: [comparison source 1](https://doi.org/10.2748/tmj/1255700197); [comparison source 2](https://arxiv.org/abs/0808.1836); [comparison source 3](https://doi.org/10.1016/j.aim.2020.107039); [comparison source 4](https://arxiv.org/abs/1904.11029); [comparison source 5](https://arxiv.org/abs/2502.11080). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 26 October 2026 against the original, latest arXiv and published formulations, later theorem hypotheses, public solution announcements, and the all-status AIM and FURTHER_problems lists. No equivalent entry or matching complete resolution was found in these bounded checks. This entry concerns the published simplicial Conjecture 4.2. The deleted extremal-wall conjecture from the first preprint and the separate non-simplicial Conjecture 4.3 are not included.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-5da6e3af38745f79**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
