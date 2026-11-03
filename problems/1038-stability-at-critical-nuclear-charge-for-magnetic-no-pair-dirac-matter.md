# 1038. Stability at critical nuclear charge for magnetic no-pair Dirac matter

**Area:** Many-body physics, quantum information and wave analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`\alpha_0=1/137`$ and write $`\gamma_B=2/(\pi/2+2/\pi)`$. Let $`\sigma_1,\sigma_2,\sigma_3`$ be the Pauli matrices, and put
```math
a_j=\begin{pmatrix}0&\sigma_j\\ \sigma_j&0\end{pmatrix},
 \qquad b=\begin{pmatrix}I_2&0\\0&-I_2\end{pmatrix}.
```

In units with electron mass, $`\hbar`$ and the speed of light equal to one, define
```math
D_A=\sum_{j=1}^3a_j(-i\partial_j+\sqrt{\alpha_0}A_j)+b,
 \qquad \mathcal H_A^+=\mathbf1_{(0,\infty)}(D_A)L^2(\mathbb R^3;\mathbb C^4).
```

Allow real vector potentials
```math
\mathcal A=\{A\in L^6(\mathbb R^3;\mathbb R^3):
 \mathrm{div}A=0,\ \mathrm{curl}A\in L^2(\mathbb R^3)\},
```

with derivatives interpreted distributionally. For distinct fixed nuclei $`R_1,\ldots,R_M`$ and charges $`Z_a>0`$ satisfying $`\alpha_0Z_a\le\gamma_B`$, set
```math
V_C=\sum_{i<j}|x_i-x_j|^{-1}
 -\sum_{i=1}^N\sum_{a=1}^M Z_a|x_i-R_a|^{-1}
 +\sum_{a<b}Z_aZ_b|R_a-R_b|^{-1}.
```

For normalized $`\Psi\in\bigwedge^N\mathcal H_A^+\cap H^{1/2}((\mathbb R^3)^N;\mathbb C^{4^N})`$, consider the quadratic-form energy
```math
\mathcal E_{A,R,Z}(\Psi)=
 \left\langle\Psi,\left(\sum_{i=1}^N D_{A,i}+\alpha_0V_C\right)\Psi\right\rangle
 +\frac1{8\pi}\int_{\mathbb R^3}|\mathrm{curl}A|^2.
```

Is there a finite constant $`C`$, independent of $`N,M,A,R,Z`$, such that
```math
\mathcal E_{A,R,Z}(\Psi)\ge-C(N+M)
```

for all these systems? The assertion is understood on the common finite-energy form domain and hence for its semibounded realization if the lower bound holds.

The electronic subspace depends on the magnetic field, and the nuclear Coulomb potential is not included in the operator defining that subspace. This is the modified Brown-Ravenhall model of [1, section 10.4]. The rational coupling $`1/137`$ specifies the benchmark used for the source's physical-coupling discussion; it is not an exact measured value. The required charge range reaches the Brown-Ravenhall value, approximately $`Z=124`$.

## Application

This asks whether self-generated classical magnetic fields preserve the expected relativistic stability range for heavy nuclei when both spin and relativistic Dirac dynamics are included.

## References

1. E. H. Lieb and R. Seiringer, [The Stability of Matter in Quantum Mechanics, Chapter 10](https://doi.org/10.1017/CBO9780511819681.011), Cambridge University Press (2009; online 2010), pp. 184-185 and 193-194, equations (10.4.1)-(10.4.4) and the open problem after Theorem 10.1.
2. E. H. Lieb, H. Siedentop and J. P. Solovej, [Stability and Instability of Relativistic Electrons in Classical Electromagnetic Fields](https://arxiv.org/abs/cond-mat/9610195v4), Journal of Statistical Physics 89 (1997), 37-59, section 2 and Theorem 1; [DOI](https://doi.org/10.1007/BF02770753).
3. M. Könenberg and O. Matte, [Ground states of semi-relativistic Pauli-Fierz and no-pair Hamiltonians in QED at critical Coulomb coupling](https://jot.theta.ro/jot/archive/2013-070-001/2013-070-001-011.pdf), Journal of Operator Theory 70 (2013), 211-237, introduction and sections 2-3: comparison with a one-electron model coupled to a quantized field with an ultraviolet cutoff.
4. R. Reuvers, J. P. Solovej and D. Stuart, [Stability of Matter Interacting with Classical Non-Abelian Gauge Fields](https://arxiv.org/abs/2610.08313), preprint (2026), section 1.2 and Theorem 7: a current related-model comparison.

5. O. Matte and E. Stockmeyer, [On the eigenfunctions of no-pair operators in classical magnetic fields](https://arxiv.org/html/0810.4897v1), **Integral Equations and Operator Theory** 65(2) (2009), 255–283, introduction and Theorem 2.1: a fixed-field one-electron comparison.

## Status review


**Known cases:** The many-electron field-dependent no-pair projection with classical magnetic energy must remain stable at critical nuclear charge. One-electron quantized-field binding and non-Abelian gauge analogues have different models.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The many-electron field-dependent no-pair projection with classical magnetic energy must remain stable at critical nuclear charge. One-electron quantized-field binding and non-Abelian gauge analogues have different models.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked **30 October 2026**.

The source [1] expressly leaves stability up to the expected critical nuclear charge open at physical coupling. Its Theorem 10.1 proves a sufficient regime reaching $`Z\le56`$ for the physical coupling and cites a stronger result reaching $`Z\le88`$. The original argument [2] also does not reach the displayed critical charge. The question asks for stability of the second kind; it does not require the stronger nonnegative bound in those sufficient theorems.

Reference [5] proves one-electron semiboundedness for a fixed external magnetic field, with additional regularity at critical coupling. It does not provide a lower bound uniform over fields and arbitrary particle and nuclear counts after adding one classical field-energy term.

The critical-coupling ground-state result [3] treats one electron coupled to a quantized photon field at fixed ultraviolet cutoff. It does not provide an arbitrary-particle lower bound uniform over the uncut classical magnetic fields in this question. The later non-abelian model [4] proves a small-coupling result for a different system. Results for an atomic Brown-Ravenhall operator without a magnetic field or for the Furry projection that already contains the attractive nuclear potential likewise have different hypotheses.

Bounded current searches on 30 October 2026 found no matching complete published or announced proof or counterexample, and all-status AIM, FURTHER and OpenAI statement comparisons found no equivalent existing target.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6e5bf5da93a1daa7**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
