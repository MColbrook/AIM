# A uniform time lattice discretizes the infinite observation window

**Target:** Problem 457 at `aa776a01d7d48a79f93251af11fde9454b0aea95`; [unchanged statement](statement.md).

**Status:** Solution claimed — complete proof, awaiting independent review.

**Prepared:** 2026-10-02 by OpenAI Codex. Construction, source comparison and self-review were performed by the same AI agent. No independent or human audit is claimed.

## Result

Under all the hypotheses of problem 457, every sufficiently fine uniform lattice $`T_h=\{0,h,2h,\ldots\}`$ gives the required unweighted frame. The proof derives a spectral lower bound from the stated Bessel assumption, then uses a time-Sobolev estimate on the observation operator. Exponential stability is not assumed.

We use inner products linear in the first argument. Define the bounded analysis operator

```math
C:\mathcal H\longrightarrow\ell^2(J),\qquad
Cf=(\langle f,g_j\rangle)_{j\in J},\qquad \|C\|^2\le B_0.
```

The zero Hilbert space is immediate, so suppose $`\mathcal H\ne\{0\}`$. The lower frame bound then implies $`B_0>0`$.

## 1. The assumptions force a bounded logarithm of the evolution

Let $`E`$ be the spectral measure of the bounded normal operator $`A`$, and set

```math
r=\exp(-B_0/m)\in(0,1).
```

If $`f`$ belongs to $`E(\{|z|\le r\})\mathcal H`$, then for every $`t>0`$ the exact spectral-calculus convention of the problem gives

```math
\|(A^t)^*f\|\le r^t\|f\|.
```

Here the possible spectral value zero contributes zero for positive times. The Bessel estimate and the assumed continuous lower frame bound imply

```math
m\|f\|^2
\le\int_0^\infty\|C(A^t)^*f\|_{\ell^2}^2\,dt
\le B_0\int_0^\infty r^{2t}\,dt\,\|f\|^2
=\frac m2\|f\|^2.
```

Thus this spectral subspace is zero. In particular the spectral measure is supported away from zero, and $`A`$ is boundedly invertible. Define the bounded Borel-calculus logarithm

```math
L=\int\bigl(\log|z|+i\arg z\bigr)\,dE(z),\qquad \arg z\in(-\pi,\pi].
```

The modulus of the integrand is bounded because $`r\le|z|\le\|A\|`$ almost everywhere for the spectral measure and $`|\arg z|\le\pi`$. No continuous branch on a neighborhood of the spectrum is required. The definition in the problem is exactly

```math
A^t=e^{tL}\qquad(t\ge0).
```

## 2. The observations have a uniform square-integrable derivative

For $`f\in\mathcal H`$ put

```math
Y_f(t)=Ce^{tL^*}f\in\ell^2(J).
```

The continuous frame assumption reads

```math
\sqrt m\,\|f\|\le\|Y_f\|_{L^2(0,\infty;\ell^2)}\le\sqrt M\,\|f\|.
```

Since $`L`$ is bounded, $`Y_f`$ is continuously differentiable, and

```math
Y_f'(t)=Ce^{tL^*}L^*f=Y_{L^*f}(t).
```

Applying the same continuous upper frame bound to $`L^*f`$ gives

```math
\|Y_f'\|_{L^2(0,\infty;\ell^2)}
\le\sqrt M\,\|L^*f\|\le\sqrt M\,\|L\|\,\|f\|.                \tag{1}
```

This estimate is over the whole infinite interval; it does not introduce a constant growing with the observation horizon.

## 3. Uniform sampling preserves both frame bounds

Let $`Y_{f,h}(t)=Y_f(kh)`$ for $`kh\le t<(k+1)h`$. For any continuously differentiable Hilbert-valued function $`Y`$ and $`a=kh`$, Cauchy–Schwarz gives

```math
\|Y(t)-Y(a)\|^2
\le(t-a)\int_a^t\|Y'(s)\|^2\,ds.
```

Integrating over the cell, bounding $`t-a\le h`$, and summing the cells yields

```math
\|Y_f-Y_{f,h}\|_{L^2(0,\infty;\ell^2)}
\le h\|Y_f'\|_{L^2(0,\infty;\ell^2)}
\le h\sqrt M\,\|L\|\,\|f\|.                                \tag{2}
```

One may first sum over finitely many cells and then use monotone convergence. In particular the step function is in $`L^2`$, so its squared norm is the convergent sum

```math
\|Y_{f,h}\|_{L^2}^2
=h\sum_{k=0}^\infty\sum_{j\in J}|\langle f,A^{kh}g_j\rangle|^2.
```

By the triangle inequality and (2),

```math
\bigl(\sqrt m-h\sqrt M\,\|L\|\bigr)\|f\|
\le\|Y_{f,h}\|_{L^2}
\le\sqrt M(1+h\|L\|)\|f\|.
```

Choose any $`h>0`$ with $`h\sqrt M\|L\|<\sqrt m`$ (if $`L=0`$, this condition imposes no restriction). The unweighted discrete frame bounds are therefore

```math
m_{T_h}=\frac{(\sqrt m-h\sqrt M\|L\|)^2}{h}>0,
\qquad M_{T_h}=\frac{M(1+h\|L\|)^2}{h}<\infty.
```

Finally $`T_h`$ is locally finite and $`\#(T_h\cap[a,a+R])\le R/h+1`$ for every $`a,R\ge0`$. Hence $`D^+(T_h)=1/h<\infty`$. The factor $`h`$ in the intermediate integral identity has been absorbed into the two frame constants; every term of the requested discrete sum has weight one.

## Target comparison and audit

The proof covers arbitrary countable Bessel sensor families, arbitrary separable complex Hilbert spaces, and the specified argument convention for a bounded normal $`A`$. It derives invertibility instead of adding it as an assumption. It uses neither self-adjointness nor exponential stability nor a finite observation horizon. The boundedness of the initial analysis operator is essential to Step 1 and is explicitly present in the target; the proof does not claim a theorem for arbitrary non-Bessel sensors.

The source context is Aldroubi, Cabrelli, Krishtal and Molter, [Dynamical Sampling: A Survey](https://link.springer.com/article/10.1007/s44007-026-00215-y), Theorem 2.12, Open Problem 1 and §5.2(B). The earlier finite-window result is Aldroubi, Huang and Petrosyan, [Frames induced by the action of continuous powers of an operator](https://arxiv.org/html/1801.10103), Theorem 5.4. The argument above directly proves the pinned infinite-window target and does not infer it by passing to a limit of unspecified finite-window constants. It needs only the spectral theorem, elementary Hilbert-space calculus and the stated frame hypotheses. Independent mathematical review remains outstanding.
