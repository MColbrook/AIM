# AIM 408 target comparison

[Official problem statement](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/408-polynomial-anisotropic-minimal-graphs.md#problem-statement) · [Complete manuscript](paper.pdf) · [LaTeX source](paper.tex)

Theorem 1 of *Polynomial rigidity for anisotropic minimal graphs in dimensions four and five* gives a negative answer to AIM 408. For each of the two dimensions and for every integrand in the stated class, any entire polynomial solution is affine.

| Original requirement | Location and coverage in the manuscript |
| --- | --- |
| Base dimension four or five | Theorem 1 includes both dimensions. Section 4 rules out every non-affine solution in dimension four and reduces dimension five to an indefinite quadratic factor with a homogeneous cofactor. Sections 5–8 exhaust the two cofactor cases in dimension five. |
| A real polynomial on the whole base space | Theorem 1 assumes a real polynomial on the entire space. The proof considers every degree at least two. Sections 6 and 8 use the full polynomial, including all its lower homogeneous terms. |
| A positive even integrand on the sphere with locally Lipschitz second derivatives | Theorem 1 gives the class and its positively one-homogeneous extension. Sections 2 and 6 use the fixed integrand for oriented minimizing boundaries and translated graphs. Section 5 uses the Lipschitz bound for second derivatives at the singular point of an ordinary differential equation. |
| A uniform positive lower bound of the extended Hessian on tangential directions | Theorem 1 states the bound for all unit normals. Section 2 checks that restrictions to linear subspaces retain the bound and that the regularity theorem applies. Section 3 uses the same strict ellipticity in the Jacobi equation on a cone. |
| The prescribed graph equation throughout the base space | Theorem 1 uses the exact graph integrand, obtained by evaluating the homogeneous energy at the vector with horizontal component minus the slope and last component one. Section 2 uses the equation for the ambient calibration. Sections 6 and 7 use the Jacobi field of the actual rescaled graphs. |
| Existence of a non-affine polynomial under these requirements | The contradiction in Sections 4–8 excludes such a polynomial in either dimension. |

The external geometric inputs in Section 2 are the density, compactness and regularity results of Schoen and Simon in Part I of the cited Acta Mathematica article. The argument uses local regular convergence at interior regular points and dimension-two interior regularity for minimizing boundaries. The proof is analytic.

## Review scope

ChatGPT/Codex assisted with developing and checking the argument and preparing the paper. The argument received a full AI-assisted natural-language inference audit. An AI reader and an AI referee then reviewed a frozen earlier draft in separate fresh contexts using the draft and the public target. The referee could consult public primary sources. Their reports were withheld from each other. The review contexts shared a filesystem, and their physical isolation was unverified. The author revision and final build followed those reports. Independent mathematical review is requested.

## Reproduce the manuscript

From this directory, run `latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex` with a standard TeX Live installation. The submitted manuscript was built with TeX Live 2025. The submitted files and their SHA-256 digests are listed in [SHA256SUMS](SHA256SUMS).
