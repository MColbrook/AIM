# 897. Pedersen's sharp fractional-power commutator inequality

**Area:** Matrix analysis and operator theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a complex matrix $`Y`$, write
```math
\|Y\|_{\mathrm{op}}=\sup_{\|v\|_2=1}\|Yv\|_2.
```

A matrix $`A`$ is positive semidefinite if $`A=A^*`$ and all its eigenvalues are nonnegative. Its fractional power $`A^r`$ is defined by applying $`t\mapsto t^r`$ to its eigenvalues.

Is it true that, for every dimension $`n\geq1`$, every pair of positive semidefinite matrices $`A,B\in M_n(\mathbb C)`$, every matrix $`X\in M_n(\mathbb C)`$, and every $`0<r<1`$,
```math
\boxed{\;
 \|A^rX-XB^r\|_{\mathrm{op}}
 \leq
 \|X\|_{\mathrm{op}}^{\,1-r}
 \|AX-XB\|_{\mathrm{op}}^{\,r}\; ?}
```


The constant must be one, uniformly in the dimension and in the exponent. The case $`X=0`$ is interpreted directly; for $`X\ne0`$, the homogeneous formulation is equivalent to imposing $`\|X\|_{\mathrm{op}}=1`$. The scalar choice $`A=1`$, $`B=0`$, $`X=1`$ shows that the constant cannot be smaller than one.

Equivalently, one can take $`A=B`$ and ask about the commutator $`[A,X]=AX-XA`$, allowing the matrix dimension to vary. Indeed, apply the commutator formulation to the positive block matrix $`\mathrm{diag}(A,B)`$ and the matrix with off-diagonal blocks $`X,X^*`$; the relevant block commutator norms equal the two-matrix norms above.

## Application

The inequality would give the optimal control of fractional-power functional calculus by an original commutator. In particular, if a matrix approximately intertwines two positive matrices, it would quantify how accurately it intertwines their fractional powers. The square-root case also occurs in estimates for almost commuting operators.

## References

1. R. Bhatia, *Matrix Analysis*, Graduate Texts in Mathematics **169**, Springer, 1997, Problem X.5.3, printed p. 317, and the explicit conjecture in the Chapter X notes, printed p. 321. [Book](https://doi.org/10.1007/978-1-4612-0653-8).
2. T. A. Loring and F. Vides, *Estimating Norms of Commutators*, arXiv:1301.4252v3 (2013), Definition 1.4, Conjecture 1.6 and Lemma 1.7. Published in *Experimental Mathematics* **24** (2015), 106–122; the cited locators refer to the versioned preprint. [Preprint](https://arxiv.org/abs/1301.4252v3).
3. D. Herrera, *On the commutator modulus of continuity for operator monotone functions*, arXiv:2311.17448v1 (2023), equation (7), Conjectures 1.8–1.9 and Theorems 1.11–1.12. [Preprint](https://arxiv.org/abs/2311.17448v1).

## Status review


**Known cases:** The current primary Herrera record still gives factors below 1.01975, and below 1.00891 for square roots, while explicitly retaining the desired constant one. Hilbert-Schmidt constant-one inequalities and special commutator-size results do not settle the operator norm for all positive matrices and exponents.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The current primary Herrera record still gives factors below 1.01975, and below 1.00891 for square roots, while explicitly retaining the desired constant one. Hilbert-Schmidt constant-one inequalities and special commutator-size results do not settle the operator norm for all positive matrices and exponents.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Bhatia records the estimate with constant $`5/4`$ and explicitly conjectures that this factor can be replaced by one. The adjacent Hilbert–Schmidt-norm inequality already has constant one; the question here concerns the operator norm.

Loring and Vides state the square-root case as Conjecture 1.6. Their Lemma 1.7 proves it for a positive contraction $`H`$, a contraction $`X`$, and $`\|[H,X]\|_{\mathrm{op}}\geq1/4`$; it does not settle all commutator sizes.

Herrera's Theorem 1.11 gives a universal factor strictly below $`1.01975`$, which applies to all the powers in this question. Theorem 1.12 improves the square-root factor to strictly below $`1.00891`$. These are progress toward the required constant one. The stronger conjectures for general operator-monotone functions and for arbitrary unitarily invariant norms are not being added as separate problems here.

The checks on 24 October 2026 examined the original problem and conjecture, these later primary statements, current arXiv version metadata, and searches under Pedersen, square-root commutators, fractional-power quasicommutators, commutator moduli and the optimal constant. No matching full resolution or announcement was located. Prove2Me site searches found no matching entry; a direct live request timed out, so that site's current content was not exhaustively checked. This is a bounded literature check, not a certification that no unindexed result exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-23c8b6c115624c1d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
