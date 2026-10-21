# AIM 571 / PR 176: mathematical reduction and reproduction-supplement review

**PR:** [176](https://github.com/MColbrook/AIM/pull/176). **Reviewed head:** `3cc0f979cb475aeacc120e0523897a9786da1850`. **Review date:** 2026-10-21. **Finding:** No substantive geometric, encoding, fixed-class, exact-algebra or reproduction-driver gap was identified.

Independent OpenAI Codex AI review. This report covers the unchanged nine-page manuscript and mathematical sources, the additive reproduction supplement, stored-data checks, and a dated search for an earlier exact formula. Fresh Normaliz execution results are documented separately. No new Normaliz computation was performed for this report. This is an independent argument and software-interface audit, not human peer review or Lean verification.

## Target and preservation of the earlier audit

The target is the stated degree-seven count for every integer $`i\geq3`$, counting two-dimensional polygons with vertices in $`\tfrac12\mathbb Z^2`$, including integral polygons, modulo integer affine unimodular transformations. The equivalence uses integer translations of the original polygon. It does not count only denominator-exactly-two polygons or Ehrhart quasipolynomials.

All **17 original files**, including the manuscript TeX and PDF, generator, algebra code and compact series data, were independently compared byte for byte by SHA-256 with the existing repository package and the supplement's original-file manifest. Every comparison matched. The compact original input/output data retains SHA-256 `bd22e0775a0475fe485349483dec748c0045fa3b4e2b0f066a716a3b031bdc21`.

The [15 October audit of PR 122](https://github.com/MColbrook/AIM/blob/24edaadc6bb272737d8da0745c662c992db07b22/research/solution_reviews/2026-10-15-active-prs/571-review.md) therefore remains applicable to the unchanged proof, including its inspection of all nine PDF pages and its primary-source software-semantics checks. This review reread the complete TeX, generator and integer algebra and checked the new execution/receipt layer. The historical incomplete replay is not counted as complete evidence, and the supplement does not alter the mathematical claim.

## Boundary-chain reduction

Bohnert–Springer's strip proposition applies because $`i>2`$. After doubling and an integer translation, $`Q=2P`$ has exactly the interior even-lattice points $`(2j,0)`$, $`1\leq j\leq n-1`$, where $`n=i+1\geq4`$. Its extreme heights are $`-a,b`$ with $`a,b\in\{1,2\}`$. [Bohnert–Springer, Proposition 3.5](https://doi.org/10.1007/s00454-026-00822-0).

Writing the horizontal section as $`[f(y),2n-g(y)]`$, both boundary functions are convex and piecewise affine. Strict slope changes recover unique integer vertex-height sets. At successive heights $`u<v<w`$, strict convexity is exactly the integer condition

```math
(w-v)x_u-(w-u)x_v+(v-u)x_w\geq1.
```

For the edge $`u\leq0<v`$, the strict-interior row condition is exactly

```math
0\leq vx_u-ux_v\leq2(v-u)-1.
```

The upper endpoint is correct because the numerator is integral and the original section intercept must be strictly below two. Nonnegative endpoint widths imply nonnegative widths throughout by concavity. The width at zero is strictly greater than $`2n-4`$, so every nonextreme section has positive width. Point extreme faces and corners at zero are retained. The only other possible even rows are extreme boundary rows, so no extra interior lattice points are introduced.

The shear normalization $`0\leq f'_+(0)<1`$ has a unique representative in every integer-shear orbit, including a corner at zero. Its finite reference-pair loop is exhaustive: for each slope numerator the interval for the reference coordinate has length two and contains exactly two integers. The checked coordinate bounds give finite real and integer fibers at every $`n`$. This also makes the unbounded-degree generating series well defined.

## Residual equivalences and fixed classes

Preservation of the first and last interior lattice points forces the residual matrix to have diagonal signs and an integer upper-right shear. The required horizontal translation is either zero or $`n`$ in original coordinates. After quotienting the free shear action, the residual group has four elements, represented by horizontal reflection $`h`$, vertical reflection $`v`$, and their product.

The fixed-class equations were checked directly:

```math
h:\quad g(y)=f(y)+my,
```

```math
v:\quad f(-y)=f(y)+my,\qquad g(-y)=g(y)-my,
```

```math
hv:\quad g(-y)=f(y).
```

The first two retain the unique integer shear parameter $`m`$. For the product, commutation with shears and freeness force $`2m=0`$, hence $`m=0`$. Thus the generator counts fixed **shear classes**, including classes whose normalized polygon is not itself fixed by a reflection.

The generator's height-set restrictions, signs, strict inequalities, endpoint widths and retained degree coordinate match these conditions. The action counts are **420 identity, 72 horizontal, 84 vertical and 42 product cells**. Their **618** assignments reduce to **608** identical complete matrix-and-grading inputs, with all original multiplicities preserved. The stored-data verifier independently regenerated every assignment and input during this review.

## Entire rational functions and all parameters

The algebra retains the original exponent shift and denominator factors. For factors of degrees one and two, it forms a common denominator using $`1-z^2=(1-z)(1+z)`$ and performs integer polynomial addition and multiplication. It compares complete numerators after clearing denominators, so agreement is an identity of rational functions.

Burnside's sum yields

```math
\sum_{n\geq4}N(n-1)z^n
=\frac{F_e(z)+F_h(z)+F_v(z)+F_{hv}(z)}4
=\frac{z^4P_*(z)}{(1-z)^8}.
```

Writing $`c_k`$ for the degree-$`k`$ coefficient of the recorded degree-seven polynomial $`P_*`$ gives

```math
N(i)=\sum_{k=0}^7c_k\binom{i+4-k}{7},\qquad i\geq3.
```

The smallest upper binomial argument is $`i-3\geq0`$. When a shifted series coefficient should vanish, that upper argument lies between zero and six and its polynomial binomial expression vanishes too. Thus extraction includes the full lower endpoint $`i=3`$. The integer polynomial expansion gives exactly the target expression after division by $`7!=5040`$.

The standalone stored-data verifier passed in ordinary Python with bytecode generation disabled: **608 unique inputs, 618 cell memberships, zero full-rational differences and zero polynomial-coefficient difference**. These calculations check the complete exported algebra, rather than fitting an initial coefficient range.

## What the new worker actually computes

The supplement's `replay.py`, function `compute_one`, constructs a worker request containing only the exact input matrices/grading, options and timeout. Its `worker` function constructs the cone, requests `HilbertSeries`, checks that property was computed, and reads both the complete series and original grading. It does not load the expected per-system series. The controller subsequently compares the worker's result with that expected series as an entire rational function.

The default options remain `HilbertSeries`, `BigInt`, `NoGradingDenom`, with one Normaliz thread per worker. Inputs are not truncated, and no floating-point series substitute is accepted. The [PyNormaliz 2.24 primary documentation](https://github.com/Normaliz/PyNormaliz/tree/v2.24) confirms the numerator/denominator-exponents/shift format and the collective computation interface. The finite exact-series enumeration method is described by [Bruns–Ichim–Söger v4, Section 5.3](https://arxiv.org/pdf/1206.1916v4).

A successful result is saved only after comparison. Timeouts, worker errors and interrupted work remain outside completed coverage. Resumption revalidates existing records against the input, source, runner, environment and options context. The full checker distinguishes diagnostic subsets from all-input coverage. Bundling preserves individual result hashes and rechecks the resulting bundle.

## Receipts, acceptance gate and trust boundary

An independent read-only examination of the submitted recorded bundle checked all **608** result records and **618** cell memberships. The source, data, runner, context and per-record hash bindings matched; every stored series had exact integer data, the required grading and an entire rational-function match. The recorded run's option list was the original default list.

These checks establish internal consistency of the recorded outputs. Hashes, status labels and timing fields do not by themselves authenticate execution or derive Hilbert series. The receipt tests deliberately use synthetic fixtures and test accounting/error handling; they are not fresh mathematical computations. The independently observed replay record supplies the execution evidence separately.

The mathematical software gate is the calculation of each complete lattice-point series with its exact constraints, full ambient integer lattice, original grading and cell multiplicity, followed by the exact rational and polynomial identities. Normaliz remains the trusted enumeration implementation. `BigInt` does not remove bounded internal degree types or ordinary LLL arithmetic; the supplement discloses this and does not claim a second counting implementation or an independently checked simplicial-decomposition certificate. No additional blocker was found in the supplement under that disclosed exact-software trust model.

## Earlier-solution search

The published March 2026 paper states this exact formula as **Conjecture 3.7** and reports finite verification through $`i=20`$. The known integral-polygon formula is for a smaller family, and the separate Ehrhart-quasipolynomial conjecture counts different objects. [Bohnert–Springer, Classification 3.6 and Conjecture 3.7](https://doi.org/10.1007/s00454-026-00822-0).

Searches on 21 October 2026 combined the exact target, half-integral polygons, collinear interior lattice points, the conjecture number, author names, characteristic polynomial coefficients, and later 2026 proofs. No earlier matching all-parameter proof or counterexample was found. The author's [arXiv record](https://arxiv.org/abs/2410.17244) still lists only the original 2024 submission. The finite [classification dataset](https://zenodo.org/records/13928298) supplies comparison cases, rather than an all-parameter formula proof. This bounded search does not certify that every unindexed result has been excluded.
