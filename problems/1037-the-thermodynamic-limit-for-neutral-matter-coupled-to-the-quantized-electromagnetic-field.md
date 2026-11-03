# 1037. The thermodynamic limit for neutral matter coupled to the quantized electromagnetic field

**Area:** Many-body physics, quantum information and wave analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Consider the nonrelativistic Coulomb-gauge model of Lieb and Loss [1, §2], with a fixed ultraviolet cutoff. Electrons are spin-$`\tfrac12`$ fermions of charge $`-\sqrt{\alpha}`$, with $`g=2`$. There is one species of quantum nuclei of charge $`Z\sqrt{\alpha}`$ and mass $`M`$ in electron-mass units. Fix the nuclei to be either spinless bosons or spin-$`\tfrac12`$ fermions; their magnetic moments are omitted.

Fix an integer $`Z\ge1`$, $`\alpha,M,\beta,\Lambda,\rho>0`$, with
```math
\alpha<\frac1{98},\qquad Z\alpha^2<\frac{39}{40\cdot468}.
```

For each integer $`K\ge1`$, put $`N=ZK`$ and let $`\Omega_K`$ be the centered cube of volume $`K/\rho`$. Particles satisfy Dirichlet boundary conditions on $`\partial\Omega_K`$. The photon field occupies the larger periodic cube $`\mathcal U_L=(-L/2,L/2)^3`$, with $`L>|\Omega_K|^{1/3}`$, and is not confined to $`\Omega_K`$.

Use exactly the three-component photon convention in [1, (2.7)–(2.8)]. Thus $`k\in(2\pi/L)\mathbb Z^3\setminus\{0\}`$, $`\mathbf a(k)=(a_1(k),a_2(k),a_3(k))`$ obeys the canonical bosonic commutation relations, and
```math
H_{f,L}=\sum_{k\ne0}\sum_{j=1}^{3}|k|a_j^*(k)a_j(k).
```

Choose the sharp cutoff $`\chi_\Lambda(k)=\mathbf1_{\{|k|\le\Lambda\}}`$ and define
```math
C_{\Lambda,L}(x)=\frac1{2\pi}\left(\frac{2\pi}{L}\right)^{3/2}
 \sum_{k\ne0}\frac{\chi_\Lambda(k)}{|k|^{3/2}}
 \bigl[\mathbf a(k)e^{ik\cdot x}-\mathbf a^*(k)e^{-ik\cdot x}\bigr],
 \qquad A_{\Lambda,L}=i\,\mathrm{curl}C_{\Lambda,L}.
```

The cutoff acts on the matter–field coupling; the free field $`H_{f,L}`$ retains all nonzero modes. On the electron space, the chosen nuclear statistics space, and the photon Fock space, set
```math
\begin{split}
 H_{K,L}={}&\sum_{i=1}^{ZK}\bigl[\sigma_i\cdot(-i\nabla_{x_i}
             +\sqrt{\alpha}A_{\Lambda,L}(x_i))\bigr]^2\\
 &+\frac1M\sum_{j=1}^{K}
      \bigl(-i\nabla_{R_j}-Z\sqrt{\alpha}A_{\Lambda,L}(R_j)\bigr)^2
      +\alpha V_C+H_{f,L},\\
 V_C={}&\sum_{i<i'}|x_i-x_{i'}|^{-1}
       +Z^2\sum_{j<j'}|R_j-R_{j'}|^{-1}
       -Z\sum_{i,j}|x_i-R_j|^{-1}.
\end{split}
```

Let
```math
\mathcal Z_{K,L}=\mathrm{Tr}e^{-\beta H_{K,L}},
 \qquad \mathcal Z^0_L=\mathrm{Tr}_{\mathcal F_L}e^{-\beta H_{f,L}}.
```

Do the ordinary inner limits exist, and does the iterated, Planck-subtracted free-energy density
```math
-\frac1\beta\lim_{K\to\infty}\frac1{|\Omega_K|}
       \lim_{L\to\infty}
       \bigl(\log\mathcal Z_{K,L}-\log\mathcal Z^0_L\bigr)
```

exist as a finite real number for every fixed choice of the above parameters and nuclear statistics?

This is the standard neutral growing-cube specialization of [1, (2.3)]. The source leaves the matter-container shape unspecified for its lower-bound argument. The question here fixes that choice explicitly. It does not ask for the separate ultraviolet-renormalization limit $`\Lambda\to\infty`$, arbitrary-container shape independence, or nuclear hyperfine interactions.

## Application

A thermodynamic limit would justify an extensive equilibrium free energy for this continuum model of charged matter and quantized radiation.

## References

1. E. H. Lieb and M. Loss, [The thermodynamic limit for matter interacting with Coulomb forces and with the quantized electromagnetic field: I. The lower bound](https://arxiv.org/abs/math-ph/0408001), arXiv:math-ph/0408001v1 (2004), §1, (2.1)–(2.9), Theorem 3.1; published in Communications in Mathematical Physics 258 (2005), 675–695, [DOI](https://doi.org/10.1007/s00220-005-1365-y).
2. E. H. Lieb and R. Seiringer, [The Stability of Matter in Quantum Mechanics, Chapter 14](https://doi.org/10.1017/CBO9780511819681.015), Cambridge University Press (2009; online 2010), printed p. 248, referring to [1].
3. C. Hainzl, M. Lewin and J. P. Solovej, [The Thermodynamic Limit of Quantum Coulomb Systems. Part II. Applications](https://arxiv.org/abs/0806.1709), v2 (2008), §2.2 and Theorem 8: the magnetic field is an external classical periodic field; there is no quantized-radiation subsystem.

## Status review


**Known cases:** Finite-temperature neutral matter coupled to a quantized photon field and its iterated Planck-subtracted limits are required. Ordinary Coulomb thermodynamic Lean formalization has no photon subsystem; single-electron self-energy ultraviolet asymptotics do not cover the limit.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Finite-temperature neutral matter coupled to a quantized photon field and its iterated Planck-subtracted limits are required. Ordinary Coulomb thermodynamic Lean formalization has no photon subsystem; single-electron self-energy ultraviolet asymptotics do not cover the limit.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Lieb and Loss prove an extensive lower bound under the stated coupling restrictions, while explicitly retaining the ordinary limits as an additional task [1, §2 and Theorem 3.1]. The book [2, p. 248] identifies the corresponding QED thermodynamic-limit problem as open.

Bounded current searches on 26 October 2026 found no proof, counterexample or complete announcement matching this model and limit order. The current Armstrong–Loher thermodynamic-limit formalization concerns the nonmagnetic Coulomb ground-state energy; it does not cover this positive-temperature coupled-field question. This is a source- and statement-level status assessment, with no certification of entire proofs.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-62ab0eb0cc7dc6af**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
