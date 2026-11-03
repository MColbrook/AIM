# 1039. A coupling bound independent of spin multiplicity for relativistic matter

**Area:** Many-body physics, quantum information and wave analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For integers $`q,N,M\ge1`$, distinct fixed nuclei $`R_1,\ldots,R_M\in\mathbb R^3`$, and real charges $`Z_1,\ldots,Z_M>0`$, set
```math
V_C(X,R)=\sum_{i<j}\frac1{|x_i-x_j|}
 -\sum_{i=1}^N\sum_{a=1}^M\frac{Z_a}{|x_i-R_a|}
 +\sum_{a<b}\frac{Z_aZ_b}{|R_a-R_b|}.
```

For a real vector potential $`A\in L^2_{\mathrm{loc}}(\mathbb R^3;\mathbb R^3)`$, let
```math
H_{N,M}(\alpha,A)=\sum_{i=1}^N\sqrt{(-i\nabla_{x_i}+A(x_i))^2}+\alpha V_C
```

be the massless, spin-independent magnetic kinetic-energy form on $`\bigwedge^N L^2(\mathbb R^3;\mathbb C^q)`$. The square root is defined from the nonnegative magnetic Laplacian. The charge factor in the magnetic potential is absorbed into $`A`$.

Do there exist universal constants $`c_0,c_1>0`$ such that
```math
0<\alpha<c_0,\qquad \alpha Z_a\le\frac2\pi,\qquad
 q\alpha\left(\frac\pi2\alpha Z_a\right)^2<c_1
 \quad (a=1,\ldots,M)
```

imply $`H_{N,M}(\alpha,A)\ge0`$ for every choice of $`q,N,M,Z_a,R_a,A`$ above?

This is the conjecture of Lieb and Seiringer [1, p. 160]: remove the factor $`q^{-1/3}`$ from the additional smallness condition on $`\alpha`$, while retaining the nuclear-charge and mixed charge-spin conditions on p. 159. Allowing arbitrarily small positive real nuclear charges is essential to this uniform question.

## Application

The criterion would determine whether the separate weak-coupling restriction can be chosen independently of the number of internal fermion states when the nuclear charges become small. It concerns the balance between relativistic kinetic energy, Coulomb attraction and Pauli exclusion.

## References

1. E. H. Lieb and R. Seiringer, [The Stability of Matter in Quantum Mechanics, Chapter 8](https://doi.org/10.1017/CBO9780511819681.009), Cambridge University Press (2009; online 2010), equation (8.7.1), pp. 157 and 159-160. The precise conjecture follows Theorem 8.2.
2. R. L. Frank, E. H. Lieb and R. Seiringer, [Stability of Relativistic Matter with Magnetic Fields for Nuclear Charges up to the Critical Value](https://arxiv.org/abs/math-ph/0610062), Communications in Mathematical Physics 275 (2007), 479-489, equations (2.1)-(2.2) and Theorem 2.1.
3. R. Reuvers, J. P. Solovej and D. Stuart, [Stability of Matter Interacting with Classical Non-Abelian Gauge Fields](https://arxiv.org/abs/2610.08313), preprint (2026), sections 1.2 and 3.2, Remark 13 and section 3.6: a current comparison with related stability thresholds.

## Status review


**Known cases:** The coupling threshold must be independent of arbitrarily large spin multiplicity, allowing small real charges. Existing q-alpha smallness theorems and non-Abelian comparisons do not give this uniform threshold.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The coupling threshold must be independent of arbitrarily large spin multiplicity, allowing small real charges. Existing q-alpha smallness theorems and non-Abelian comparisons do not give this uniform threshold.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked **30 October 2026**.

The book proves sufficient conditions with the extra restriction $`\alpha<C'q^{-1/3}`$ and explicitly conjectures the displayed improvement. Reference [2] permits arbitrary magnetic fields and critical nuclear charge under the different sufficient condition $`q\alpha\le1/66.5`$; that does not give a uniform positive threshold as $`q\to\infty`$ and the nuclear charges tend to zero. The general exchange-energy inequality with a $`q^{-1/3}`$ improvement is false, as [1] itself explains; the question here is the direct many-body stability statement.

Bounded primary-source and announcement searches on 30 October 2026 found no matching proof or counterexample. The non-abelian model in [3] has different charges and kinetic operators, and its small-coupling results do not establish this abelian conjecture. The 2025 inverse-nearest-neighbor Lieb-Thirring inequalities of Duong and Nam also concern a different displayed operator inequality. Current all-status AIM, FURTHER and OpenAI statement comparisons found no equivalent listed target. These are source- and statement-level checks, not a proof that no unindexed solution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-778cd0242ad3adee**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
