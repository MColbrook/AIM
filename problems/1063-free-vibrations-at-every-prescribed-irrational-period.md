# 1063. Free vibrations at every prescribed irrational period

**Area:** Nonlinear wave equations and variational methods
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For $`p>2`$ and $`T>0`$, put $`Q_T=(0,T)\times(0,\pi)`$. Consider the real, unforced, defocusing wave equation
```math
u_{tt}-u_{xx}+|u|^{p-2}u=0,\qquad
 u(t,0)=u(t,\pi)=0,\qquad
 u(t+T,x)=u(t,x).
```


Here a weak solution means a real function $`u\in L^p(Q_T)`$, extended $`T`$-periodically in time, for which
```math
\int_0^T\!\!\int_0^\pi
 \left[u(\varphi_{tt}-\varphi_{xx})+
       |u|^{p-2}u\,\varphi\right]\,dx\,dt=0
```

for every smooth, $`T`$-periodic test function $`\varphi`$ on
$`\mathbb R\times[0,\pi]`$ with $`\varphi(t,0)=\varphi(t,\pi)=0`$.
No integrability of the derivatives of $`u`$ is assumed.

**For every $`p>2`$ and every prescribed $`T>0`$ with $`T/\pi\notin\mathbb Q`$, does there exist such a weak solution that is not identically zero?**

The period $`T`$ need not be the least positive period. There is no smallness condition, no external forcing, and no Diophantine restriction on the irrational number $`T/\pi`$. The cubic case is $`p=4`$.

## Application

This asks whether a nonlinear string with a defocusing restoring force admits a free oscillation at every prescribed repetition time. It would extend the existence theory from selected periods to all irrational ratios between the time period and the spatial length.

## References

1. M. Struwe, *Variational Methods: Applications to Nonlinear Partial Differential Equations and Hamiltonian Systems*, fourth edition, Springer, 2008, Chapter I, §6, equations (6.8)–(6.10), Theorem 6.6 and the following remark, printed p. 65. The remark's reference to Theorem 6.7 appears to be a numbering error; it follows the displayed periodic-wave Theorem 6.6. [Book](https://doi.org/10.1007/978-3-540-74013-1). [University course copy](https://www.ljll.fr/smets/ULM/Struwe.pdf).
2. E. Feireisl, *Wave equations, examples and qualitative properties*, institutional lecture notes, §6.1.1 and Definition 6.1, pp. 41–42, for the weak periodic Dirichlet formulation. The supplied notes are undated. [Notes](https://www.math.cas.cz/oldim/fichier/course/filepdf/course_pdf_20121128091130_33.pdf).
3. M. Berti and P. Bolle, *Cantor families of periodic solutions for wave equations via a variational principle*, Advances in Mathematics **217** (2008), 1671–1727. Theorem 1.1 in the cited 2006 preprint gives the frequency scope used below. [Article](https://doi.org/10.1016/j.aim.2007.11.004). [Versioned repository preprint](https://web.ma.utexas.edu/mp_arc/c/06/06-160.pdf).
4. A. Nowakowski and A. Rogowski, *Wave equation in higher dimensions—periodic solutions*, Electronic Journal of Qualitative Theory of Differential Equations **2018**, no. 103, 1–31, Introduction, p. 3. [Article](https://doi.org/10.14232/ejqtde.2018.1.103). [Official text](https://www.math.u-szeged.hu/ejqtde/p6921.pdf).
5. F. Ficek and M. Maliborski, *Periodic solutions for the 1D cubic wave equation with Dirichlet boundary conditions*, Nonlinearity **38** (2025), 065016, Introduction and Conclusions. [Article](https://doi.org/10.1088/1361-6544/add831). [Author-hosted published text](https://homepage.univie.ac.at/filip.ficek/papers/Ficek_2025_Nonlinearity.pdf).
6. F. Ficek and M. Maliborski, *New class of time-periodic solutions to the 1D cubic wave equation*, arXiv:2506.10839v1 (2025), Theorem 1. [Preprint](https://arxiv.org/abs/2506.10839v1).
7. F. Ficek, *Time-periodic solutions to the cubic wave equation: an elementary constructive approach*, arXiv:2510.20054v1 (2025), Theorem 1 and Remarks 1–2. [Preprint](https://arxiv.org/abs/2510.20054v1).
8. F. Ficek and M. Maliborski, *Nonlinear Oscillations of Strings and Beams*, Progress of Theoretical and Experimental Physics **2026**, 021A01, §2.1 and §3. [Article](https://doi.org/10.1093/ptep/ptag002). [Author-hosted published text](https://homepage.univie.ac.at/filip.ficek/papers/Ficek_2026_PTEP.pdf).

## Status review


**Known cases:** Every prescribed irrational period is included, without a Diophantine restriction or smallness. Rational-period existence, Cantor families and numerical continuation do not cover all irrational periods for this weak class.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Every prescribed irrational period is included, without a Diophantine restriction or smallness. Rational-period existence, Cantor families and numerical continuation do not cover all irrational periods for this weak class.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Struwe explicitly asks for the irrational-period extension of the rational-period weak-solution theorem. The $`L^p`$ condition here is imposed on one time period, rather than on the entire infinite time axis.

Cantor-family results establish existence for selected frequencies and hypotheses; their frequency quantifiers do not give every prescribed irrational period. The 2018 higher-dimensional paper explicitly warns that its theorems need not establish existence for a given fixed irrational frequency and nonlinearity.

The 2025 numerical study of the cubic problem suggests that large-amplitude solutions fill the frequency gaps. This is evidence for the conjecture, not a proof for every frequency. The June 2025 computer-assisted theorem proves three solutions at the rational frequency $`\Omega=69/40`$, where $`T=2\pi/\Omega`$. The October 2025 constructive theorem gives the rational frequencies $`\Omega=(2k+1)/(2k)`$ for integers $`k\ge79\,675`$, together with rational rescalings. These results do not cover the prescribed irrational ratios in this question. The 2026 strings-and-beams paper studies finite Galerkin systems and refers back to the computer-assisted examples; it does not state the all-prescribed-period theorem.

The review on 24 October 2026 checked the original statement, the weak-solution definition, these primary results and recent related work, and searches for proofs, counterexamples and announcements under prescribed irrational periods, free vibrations, pure-power wave equations and the relevant authors. No matching full resolution or announcement was located. This is a bounded literature check; it does not certify absence of unindexed work. Prove2Me site searches located no matching entry, while a direct live site request had timed out.

The linked one-page abstract for Filip Ficek’s [Equadiff 2026 talk](https://amca-admin.rachel.puxdesign.cz/Equadiff/media/amca/2026/abstracts/contributed-talks/ficek_abstract.pdf) was also checked. Its existence claim cites the June 2025 theorem above and does not announce an arbitrary-period result.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e4e231b718375b04**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
