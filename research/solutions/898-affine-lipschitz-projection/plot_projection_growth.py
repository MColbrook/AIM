"""Illustrate the exact regression coefficient in the Problem 898 construction.

Requires NumPy, SciPy and Matplotlib. These calculations are illustrative;
the proof in aim898.tex uses exact moments and a proved Gaussian limit.
"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.special import betaln, betainc
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

def coefficient(n):
    """Use truncated beta moments of Z_n = sqrt(n) Y_1."""
    b = (n + 3) / 2
    def moments(k):
        a = (k + 1) / 2
        full = math.exp((k / 2) * math.log(n) + betaln(a, b) - betaln(.5, b))
        inside = full * betainc(a, b, 1 / n)
        return full, inside
    values = {k: moments(k) for k in (1, 2, 3, 4, 6)}
    outside = lambda k: values[k][0] - values[k][1]
    a = n / (n + 6)
    gamma_n = (values[6][1] / 9 - a * values[4][1] / 3
               + outside(4) / 3 - 2 * outside(3) / 9
               - a * outside(2) + 2 * a * outside(1) / 3)
    N = n + 4
    variance = 2 * n * (N - 1) / (3 * N * (N + 2)**2 * (N + 4))
    denominator = variance + 8 / (N * (N + 2))
    return gamma_n / (n**1.5 * denominator)

dimensions = np.unique(np.round(np.geomspace(1, 10**6, 90)).astype(int))
coefficients = np.array([coefficient(int(n)) for n in dimensions])
constant = (math.erf(1 / math.sqrt(2))
            - 2 * math.exp(-.5) / math.sqrt(2 * math.pi)) / 13
assert np.all(coefficients > 0)
assert abs(coefficients[-1] / math.sqrt(dimensions[-1]) - constant) < 2e-7

plt.rcParams.update({"font.family": "serif", "font.size": 10,
                     "mathtext.fontset": "cm", "axes.spines.top": False,
                     "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(6.35, 3.5), constrained_layout=True)
ax.loglog(dimensions + 1, coefficients, color="#174d73", linewidth=2,
          label=r"Exact-moment value of $a_n$")
ax.loglog(dimensions + 1, constant * np.sqrt(dimensions), color="#b86b26",
          linestyle="--", linewidth=1.5, label=r"$c_*\sqrt{n}$")
ax.axhline(1, color="#999999", linewidth=.8, linestyle=":")
ax.set_xlabel(r"Ambient dimension $n+1$")
ax.set_ylabel(r"Vertical coefficient $a_n$")
ax.grid(which="major", alpha=.15)
ax.legend(frameon=False, loc="upper left")
fig.savefig(OUT / "projection_growth.pdf")
fig.savefig(OUT / "projection_growth.png", dpi=180)
(OUT / "projection_growth_data.json").write_text(json.dumps({
    "description": "Vertical regression coefficient for the explicit Problem 898 example",
    "limit_a_n_over_sqrt_n": constant,
    "values": [{"n": int(n), "a_n": float(value)}
               for n, value in zip(dimensions, coefficients)]
}, indent=2))
print("Saved projection-growth figure and data; c_* =", constant)
