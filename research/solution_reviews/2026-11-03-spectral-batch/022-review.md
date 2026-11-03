# AIM 022: final review and scope

**Author and submitter:** Matthew J. Colbrook.

**Disposition:** Partially resolved — checked partial progress.

**Reviewed:** 3 November 2026, by Codex (AI). An independent reviewer read the complete argument; the coordinator checked the target mapping, applied the editorial corrections, verified the final manuscripts and repository consistency, and independently audited the torus and Heun arguments. This does not assert human peer review or Lean verification.

**Proof:** [Standalone manuscript](../../solutions/022-parallelogram-steklov/aim022.pdf), [TeX](../../solutions/022-parallelogram-steklov/aim022.tex), and [source receipt](../../solutions/022-parallelogram-steklov/SOURCE_RECEIPT.json).

**Target:** [Current AIM 022](../../../problems/022-steklov-polygon-optimizer.md) at base `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Its Problem statement is preserved.

The square uniquely maximizes the first positive Steklov eigenvalue among parallelograms of a fixed perimeter.

**Remaining target:** The regular-polygon comparison and its equality characterization remain open for arbitrary convex polygons with at most $`n`$ sides when $`n\ge4`$, including non-parallelogram quadrilaterals.

The editorial and citation refinements recommended below have been applied. They do not change the construction or the claimed theorem. This record distinguishes each proved theorem from the full catalogue question.

# AIM 022: independent mathematical audit

Date: 2026-11-03. Reviewer: Codex AI, geometric-constants review lane C. This is an independent AI audit, not human peer review or proof-assistant verification.

Canonical repository revision inspected: `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Authoritative target: `problems/022-steklov-polygon-optimizer.md` and row 022 of `data/spectral.json`. The complete supplied argument in `submission/sections/022.tex` was read, including its Robin appendix. Its SHA-256 is `9492d665990dc5de19b1e75d2cb408b62776fa29475b596fc58cc1e17ccf664c`.

## Verdict and exact scope

**PARTIAL: the stated parallelogram theorem is proved. No substantive mathematical gap found.** Among nondegenerate planar parallelograms of a prescribed perimeter, the square uniquely maximizes the first positive Steklov eigenvalue. The argument does not prove the canonical comparison for arbitrary convex quadrilaterals, nor the family for all n >= 4. The already recorded triangle case is a separate known case and should be retained.

Recommended catalogue scope:

- Known cases: the existing triangle theorem; additionally, the square is the unique maximizer among all parallelograms of the given perimeter.
- Remaining target: arbitrary convex polygons with at most n sides for n >= 4, including non-parallelogram quadrilaterals, with the prescribed regular-polygon equality characterization.
- Retain `Partially resolved`; neither `Solved` nor a full-entry `Solution claimed` follows from this manuscript.

## Proof checks

1. **Normalization and admissibility.** In the representation P = {xv+yw: |x|,|y|<1}, the actual edges have lengths 2a,2b, so perimeter 8 means a+b=2. The area is 4ab sin(theta). Relabeling/reversing v,w allows a=1+t, b=1-t, 0<=t<1 and 0<theta<=pi/2. All proposed trials are odd under central inversion and consequently have zero boundary mean. Affine pullbacks need not be harmonic: the Steklov variational principle admits all H1 trials with zero boundary mean.

2. **Boundary moments.** Direct integration over the four sides gives equation (1). For a unit vector along v it gives the manuscript's equation (2) after discarding sin(theta)<=1. Its right side decreases in t and equals 224/45 at t=1/8. For the angular bisector, the polynomial identity

   (a+3b)a^2+(3a+b)b^2=8

   gives equation (3), including the factor 6(1-t^2). Thus the two coarse reductions cover t>=1/8 and c>=1/2 with strict comparison to the square.

3. **Exact affine trial matrices.** With C=integral cos^2(kx), S=integral sin^2(kx), Ch=integral cosh^2(kx), Sh=integral sinh^2(kx), the identities tan(k)=1/h give

   E0=4kh/(1-h^4), B0=4/(1-h^4).

   These independently reproduce E0=s B0, the displayed delta and beta, and kappa=(1+h^4)/(2kh). The pulled-back Dirichlet form has diagonal terms (b A1/a+a A2/b)/z and the reversed counterpart; its mixed term is -c integral(f_x g_y+f_y g_x)/z. The boundary entries are a d_a+b d_b and b d_a+a d_b. These are exactly equation (5). The mixed boundary term and the two other mixed energy integrals vanish by parity. The remaining mixed integral is cosh(2k)-cos(2k).

4. **Small-parameter cases.** For c>=8t^2, f+g gives equation (6). The inequalities 1-z<= (2-sqrt(3))c and kappa>2/3 leave a margin greater than c/3, and 8/3>128/63. For c<8t^2, t>0 and the single f trial gives equation (7). The polynomial in equation (8) is correct, its stated lower bound is positive, and 64t^4<t for 0<t<=1/8. Therefore z>1-t and both cases are strictly below s except at t=c=0. This proves the full stated rigidity within parallelograms.

5. **First square eigenvalue.** The Robin proof is valid. For 0<s<1 the interval Robin operator with outward condition partial_nu u=s u has one negative even mode, no negative odd mode, and first positive odd mode k^2. The equations k tanh(k)=k cot(k)=s match. Tensor sums on the square give one negative eigenvalue and a two-dimensional zero eigenspace. A negative form value on a boundary-mean-zero function, together with the constant function, would give a two-dimensional negative subspace. This proves that s is the first positive Steklov eigenvalue, rather than merely some separated eigenvalue.

## Independent arithmetic

The supplied certificate was inspected before execution. It uses only `fractions` and `math`, performs no writes, and passed on a fresh run with Python `-B`:

```text
All exact rational inequalities for the parallelogram proof verified.
```

Certificate SHA-256: `6f076ae23589e8e4d44164f7d592a1766d7a4a9218f21a85502df2bde3d71193`.

I also wrote and executed a separate rational Taylor implementation: 20-term sine/cosine alternating bounds, a degree-50 exponential sum with geometric positive tail, and 70 exact bisections. This did not import the supplied certificate. Rounded numerical descriptions of the resulting rational enclosures are

```text
k in (0.9375520343559805832226499,
      0.9375520343559805832226585)
h in (0.7340955137589127558287808,
      0.7340955137589127558287848)
```

The coarse rational endpoint estimates independently give:

| Quantity | Value of rational bound, displayed approximately |
|---|---:|
| delta lower bound | 0.8183195113398504887866589994 |
| beta lower bound | 0.2289957446808510638297872340 |
| beta upper bound | 0.2627989247311827956989247311 |
| kappa lower bound | 0.9229315770557791834387579068 |
| 8kh lower bound | 5.4312 exactly |
| Case B polynomial margin | 0.0576822916666666666666666666 |

All comparisons were established with rational arithmetic; the displayed decimals are not the proof.

**Small completeness improvement:** the supplied program checks beta<1/3 but does not explicitly assert beta>0 despite saying it checks every comparison in (C). Add the elementary bound

beta >= 73/94-(74/100)^2 > 0,

or observe beta=h(1-kh)/k>0 because kh<1. The manuscript's conclusion and its estimates are unaffected; the direct rational check above supplies the missing advertised check.

## References and dated search

The primary source [Girouard, Lagace, Polterovich and Savo, arXiv:1711.03075v2](https://arxiv.org/html/1711.03075v2) was checked at its Robin-separation discussion and Theorem 1.6. The latter proves the cube comparison among cuboids, giving the known square-versus-rectangle result in dimension two. It does not claim the general parallelogram theorem. The arXiv record verifies *Mathematika* 65 (2019), 272-310 and [DOI 10.1112/S0025579318000414](https://doi.org/10.1112/S0025579318000414).

The current broader source [Cheng, Gui, Hu, Li and Yao, arXiv:2603.25116v1](https://arxiv.org/html/2603.25116v1) concerns monotonicity within the regular-polygon family. It does not by itself establish the arbitrary-polygon target. Searches on 2026-11-03 included `Steklov parallelograms square maximizes`, `Steklov parallelogram maximizes`, and `Steklov regular polygon conjecture proof 2026`. Results included cuboids, inverse spectral work on parallelograms, and the regular-polygon paper; I found no primary source invalidating the restricted scope above. This bounded search does not certify novelty or global continued openness.

## Integration recommendation

Accept the theorem as a checked partial advance. Preserve the explicit limitation to parallelograms in its title, abstract and catalogue notes. Add the beta-positivity sentence/check and cite the cuboid theorem precisely. No other mathematical repair is required.
