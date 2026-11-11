# Target comparison for AIM 465

Original target: [Optimal nonlocal obstacle regularity with a minimally smooth obstacle](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/465-nonlocal-obstacle-minimal-smoothness.md), at revision `b2ec0fac559f532fc0ed04fce81deea0ce07c68b`.

The manuscript *Optimal obstacle regularity for stable operators with minimally smooth obstacles* states a proposed full solution in Theorem 1.1. Its proof is analytic. No numerical or formal-proof certificate is claimed.

| Original requirement | Manuscript location | Scope |
| --- | --- | --- |
| Every n >= 2 and 0 < s < 1 | Theorem 1.1; equations (1.1) and (2.1) | Identical |
| Even angular density a in Lip(S^(n-1)), with positive bounds lambda and Lambda | Theorem 1.1; Section 2 | Identical; constants also depend on the angular Lipschitz norm |
| Positive PV operator with the stated homogeneous stable kernel | Equations (1.1) and (2.1); one-dimensional normalization (2.5) | Identical sign and normalization |
| Every noninteger beta > 1+s | Theorem 1.1; exponent choices (4.2) | All the stated range, including 1+s < beta <= 1+2s |
| phi in C^beta(B1); bounded continuous viscosity solution of min{Lu,u-phi}=0 | Theorem 1.1; localization (4.3)-(4.4) | Identical solution and obstacle classes |
| Arbitrary bounded exterior values, without contact/boundary separation | Theorem 1.1 and its following paragraph; Sections 4.1 and 4.4 | No exterior smoothness or separation premise |
| Full C^(1+s)(B1/2) norm bound | Estimate (1.2); Sections 4.3-4.4 | One-point gradient estimate (4.11) is lifted to the complete norm |
| Constant depends only on n,s,beta,lambda,Lambda and the angular Lipschitz norm | Theorem 1.1; fixed exponents (4.2), scales (4.8)-(4.10), and closing estimate | No solution-specific graph, exterior derivative or contact-distance constant |

The inherited compactness and classification are Ros-Oton--Torres-Latorre--Weidner, arXiv:2306.16751v2, Lemma 6.5 and Theorem 1.5. The manuscript uses only the subcritical part of their Corollary 1.3. The added argument is the flat quotient estimate in Section 2, followed by the actual-contact matching and value/tail improvement in Section 3. The one-dimensional higher Liouville input is Abatangelo--Ros-Oton, arXiv:1909.10339v2, Proposition 3.11 with k=1. The stronger curved-domain estimates from that paper are not used. The local boundary/interior estimates and weak Dirichlet results are cited with exact statement numbers from the specified Fernandez-Real--Ros-Oton author manuscript.

The claim is offered for independent mathematical review. Its submission or successful document build does not establish acceptance by the problem repository.
