# AIM 523: target comparison

Target revision: `c4036871b0bf15cbc83e79c780b7191bcbb2cfed`. See [statement.md](statement.md).

The target is the real inclusion ell1 into ell-infinity on the open unit ball, with adaptive continuous linear queries, finite query count, a uniform expected budget, joint output/count measurability, and worst-input RMS error.

The proof gives the exact value 1/2 for every positive finite budget in this model. Its lower bound allows arbitrary history-to-query rules and seed spaces. Truncation after k queries incurs a squared-error penalty at most n/k. The one-query upper bound returns a constant sequence whose value is half the sum of the coordinates. No restriction to c0 or extra decision-rule measurability is imposed. This resolves the full target affirmatively.
