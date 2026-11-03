# AIM 1019: final review and scope

**Author and submitter:** Matthew J. Colbrook.

**Disposition:** Partially resolved — checked partial progress.

**Reviewed:** 3 November 2026, by Codex (AI). An independent reviewer read the complete argument; the coordinator checked the target mapping, applied the editorial corrections, verified the final manuscripts and repository consistency, and independently audited the torus and Heun arguments. This does not assert human peer review or Lean verification.

**Proof:** [Standalone manuscript](../../solutions/1019-flat-torus-log-sobolev/aim1019.pdf), [TeX](../../solutions/1019-flat-torus-log-sobolev/aim1019.tex), and [source receipt](../../solutions/1019-flat-torus-log-sobolev/SOURCE_RECEIPT.json).

**Target:** [Current AIM 1019](../../../problems/1019-the-sharp-logarithmic-sobolev-constant-of-a-flat-torus.md) at base `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Its Problem statement is preserved.

An explicit flat torus has spectral gap one and logarithmic Sobolev constant at most 1296/2669, strictly less than one half.

**Remaining target:** Determine the sharp logarithmic Sobolev constant for general lattices, including its exact value for the displayed triangular-dual torus. Disproving universal equality alone does not answer that part of the entry.

The editorial and citation refinements recommended below have been applied. They do not change the construction or the claimed theorem. This record distinguishes each proved theorem from the full catalogue question.

# AIM 1019: second independent mathematical audit

Date: 2026-11-03. Reviewer: Codex AI, lane C. This is an independent AI audit of the supplied argument, not human peer review or proof-assistant verification.

I read the complete `submission/sections/1019.tex` and the authoritative canonical page `problems/1019-the-sharp-logarithmic-sobolev-constant-of-a-flat-torus.md`. This supplementary check focuses on normalization, the entropy Taylor bound, and scope. The coordinating reviewer separately checked Chen--Liu--Saloff-Coste Theorem 1.1/Q1 and Saloff-Coste Problem 11 and reran the supplied certificate; I have not duplicated that script run or represented those primary-source checks as my own.

## Verdict

**PARTIAL, with no mathematical gap found in the stated counterexample.** The triangular torus has gap 1 and satisfies alpha(T)<=1296/2669<1/2. The same conclusion holds on the stated open metric interval and, by products, in each dimension d>=2. This disproves the universal-equality clause of the canonical problem. Its conditional request to determine the sharp alpha(T) in terms of an arbitrary lattice remains unresolved, even for the displayed triangular torus.

## Normalization and moments

The matrix displayed in the manuscript is the **inverse** metric. The coordinate metric is [[4/3,2/3],[2/3,4/3]], and normalized Riemannian volume is exactly dx dy/(2pi)^2 because its constant density cancels on normalization. The Fourier eigenvalue is therefore m^2-mn+n^2, without any omitted 2pi factor: x,y already have period 2pi. This quadratic form is a positive integer for every nonzero integral pair, with value 1 attained at the listed modes.

The displayed direct Euclidean lattice is consistent with the dual vectors: their pairings are 2pi times the identity. Thus the coordinate-metric and Euclidean-lattice descriptions define the same torus.

I independently checked the moments by expanding cosine products. For the fourth moment, the three individual fourth powers contribute 9/8 and the three squared-pair terms contribute 6*3/4=36/8; all other terms integrate to zero. This gives 45/8. The only cubic contribution is 6 integral cos(x)cos(y)cos(x+y)=6/4=3/2. The range argument yields g>=-3/2, hence f=1+g/6>=3/4. The Dirichlet energy is integral g(-Delta g)/36=(3/2)/36=1/24.

## Taylor certificate

For h(z)=(1+z)^2 log((1+z)^2), direct differentiation gives the stated cubic polynomial and h''''(z)=-4/(1+z)^2. On the interval between zero and any z=g/6, one has 1+z>=3/4. The Lagrange fourth remainder is therefore at least

-(4/[24*(3/4)^2]) z^4 = -(8/27)z^4.

This bound is valid for negative as well as positive z because the remainder contains z^4. There is no alternating-series assumption or sign reversal at negative g.

For s=(3/2)/36=1/24, the mass correction satisfies (1+s)log(1+s)<=s+s^2/2. Subtracting this upper bound from the lower bound on integral h gives

Ent(f^2) >= 3 eps^2+eps^3-[(5/3)+(9/8)]eps^4
         = 1/12+1/216-67/31104
         = 2669/31104.

The subtraction direction, the factor 2 convention in the entropy expansion, and all coefficients check. Consequently the quotient is at most 1296/2669. Its strict comparison with gap/2 is the exact integer comparison 2592<2669; no numerical logarithm evaluation is required.

## Open metric family and higher dimensions

For G_c=[[1,-c],[-c,1]], 0<=c<1, normalized volume remains uniform. Fourier orthogonality gives E_c(g,g)=2-c. The shortest-frequency argument is correct: after taking absolute values and ordering the coordinates, write m=n+r; then q=2(1-c)n(n+r)+r^2. This yields gap min(1,2(1-c)), with both candidate values attained.

For c<=1/2, comparing 864(2-c)/2669 with 1/2 is equivalent to c>787/1728. For c>=1/2, comparison with 1-c is equivalent to c<941/1805. Their union across c=1/2 is exactly the stated open interval, which lies in the positive-definite metric range and contains 1/2. The original g need not remain a first eigenfunction for c!=1/2; its energy was computed directly, so this creates no gap.

The extension to changes in all metric coefficients is also justified. In a neighborhood of a fixed positive-definite metric, uniform coercivity bounds all frequency vectors that can minimize the gap to a finite set. The gap is thus a locally finite minimum of continuous quadratic forms and is continuous. The fixed witness has a strict margin, so an open neighborhood preserves the failure of equality even when the shortest dual vector is unique up to sign. If editing the last sentence of Section 4, say "extra triangular-lattice multiplicity" rather than suggesting that a flat torus could have a simple first positive Laplace eigenvalue: the sine/cosine pair always gives multiplicity at least two. This is a wording clarification, not a gap in the continuity argument.

Finally, the product with standard circumference-2pi circles has gap min(1,1,...)=1. A witness independent of the extra coordinates has identical energy and entropy under normalized product volume. No assertion about exact product log-Sobolev constants is needed for this counterexample.

## Catalogue recommendation

Keep `Partially resolved`. Known cases should record the explicit failure of alpha=lambda/2 for the triangular torus, an open neighborhood of metrics, and examples in every dimension d>=2. The remaining target should ask for the exact sharp alpha of general flat tori, including the displayed example. No normalization, Taylor-bound, endpoint, or product-scope repair is needed.


## Coordinating check

The coordinator also read the complete argument and checked the metric and dual lattice, Fourier moments through order four, the sign and constant in the fourth-order entropy remainder, the normalized mass term, the rational comparison, the open metric interval, and the product extension. The ratio bound is an upper certificate rather than a sharp-constant formula.

The primary Chen–Liu–Saloff-Coste paper was checked at Theorem 1.1 and Question Q1, printed page 242; Saloff-Coste Section 3.4, Problem 11, asks a different comparison question. Their titles, authors, journal details and source URLs in the manuscript agree with those texts.
