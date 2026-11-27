#!/usr/bin/env python3
"""Replay the finite affine identities in the arch-joining proof.

Uses only the Python standard library. Each outer triangle and its three
corners are labelled. Each face map is extended to a permutation of the
four local positions by sending opposite corner to opposite corner.
"""

from itertools import combinations
import json

VERTICES = tuple(range(4))
EDGES = tuple(combinations(VERTICES, 2))
FACE_EDGES = tuple(tuple(e for e in EDGES if f not in e) for f in VERTICES)
SEPARATE = (
    (0, 2), (2, 0), (5, 0), (8, 0), (10, 0), (14, 0), (4, 0), (13, 2),
    (7, 0), (12, 3), (18, 2), (22, 2), (28, 0), (30, 1), (19, 3),
)
ZERO_BASE = ((0, 3), (3, 1), (5, 0), (7, 0))
ZERO_ARCH = ((0, 3), (1, 3))


def facet(word, f):
    return tuple(v for i, v in enumerate(word) if i != f)


def inverse(permutation):
    return tuple(permutation.index(i) for i in VERTICES)


def relative_map(a, f, b, g):
    assert set(facet(a, f)) == set(facet(b, g))
    return tuple(g if i == f else b.index(a[i]) for i in VERTICES)


class Chart:
    """Combinatorial face pairings and six labelled exterior triangles."""

    def __init__(self, cells):
        self.cells = set(cells)
        self.pairs = {}
        self.ports = {}

    def pair(self, a, f, b, p):
        left, right = (a, f), (b, p[f])
        assert left != right and left not in self.pairs and right not in self.pairs
        self.pairs[left] = (b, p)
        self.pairs[right] = (a, inverse(p))

    def check(self):
        slots = {(a, f) for a in self.cells for f in VERTICES}
        assert set(self.pairs).isdisjoint(self.ports)
        assert set(self.pairs) | set(self.ports) == slots
        assert len({port for port, _ in self.ports.values()}) == len(self.ports)

    def move(self, a, f):
        b, p = self.pairs[a, f]
        g = p[f]
        assert a != b
        common = facet(VERTICES, f)
        labels_a = tuple(3 if i == f else common.index(i) for i in VERTICES)
        labels_b = tuple(4 if i == g else labels_a[inverse(p)[i]] for i in VERTICES)
        alphabet = range(5)
        fan = {max(self.cells) + 1 + j: tuple(k for k in alphabet if k != j)
               for j in range(3)}
        outside = self.cells - {a, b}
        result = Chart(outside | fan.keys())

        candidates = {}
        for c, word in fan.items():
            for h in VERTICES:
                candidates.setdefault(frozenset(facet(word, h)), []).append((c, h))
        for matches in candidates.values():
            if len(matches) == 2:
                (c, h), (d, k) = matches
                result.pair(c, h, d, relative_map(fan[c], h, fan[d], k))

        transfer = {(c, h): (c, h, VERTICES) for c in outside for h in VERTICES}
        for original, opposite, labels in ((a, f, labels_a), (b, g, labels_b)):
            for h in facet(VERTICES, opposite):
                (c, k), = candidates[frozenset(facet(labels, h))]
                transfer[original, h] = (c, k, relative_map(labels, h, fan[c], k))
        for (c, h), (d, q) in self.pairs.items():
            old_left, old_right = (c, h), (d, q[h])
            if old_left > old_right or old_left not in transfer:
                continue
            new_c, new_h, left = transfer[old_left]
            new_d, new_k, right = transfer[old_right]
            new_pair = tuple(right[q[i]] for i in inverse(left))
            assert new_pair[new_h] == new_k
            result.pair(new_c, new_h, new_d, new_pair)
        for key, (name, colors) in self.ports.items():
            c, h, permutation = transfer[key]
            result.ports[c, h] = (name, tuple(colors[i] for i in inverse(permutation)))
        result.check()
        assert len(result.cells) == len(self.cells) + 1
        return result

    def replay(self, word):
        current = self
        for a, f in word:
            current = current.move(a, f)
        return current

    def marked_code(self):
        """Pairings in frames fixed by the first labelled port."""
        (a, f), (_, colors) = min(self.ports.items(), key=lambda item: item[1][0])
        initial = tuple(sorted(facet(VERTICES, f), key=colors.__getitem__)) + (f,)
        order = [a]
        index = {a: 0}
        frames = {a: initial}
        rows = []
        for a in order:
            row = []
            for f in frames[a]:
                if (a, f) in self.ports:
                    name, colors = self.ports[a, f]
                    row.append(("port", name, tuple(colors[i] for i in frames[a])))
                    continue
                b, p = self.pairs[a, f]
                images = tuple(p[i] for i in frames[a])
                if b not in index:
                    index[b] = len(order)
                    frames[b] = images
                    order.append(b)
                row.append(("pair", index[b], tuple(frames[b].index(i) for i in images)))
            rows.append(tuple(row))
        assert len(order) == len(self.cells)
        return tuple(rows)

    def boundary_edge_occurrences(self):
        classes = {(a, e): {(a, e)} for a in self.cells for e in EDGES}
        for (a, f), (b, p) in self.pairs.items():
            for e in FACE_EDGES[f]:
                left = classes[a, e]
                right = classes[b, tuple(sorted(p[v] for v in e))]
                if left is not right:
                    left.update(right)
                    for member in right:
                        classes[member] = left
        old_reps = {min(classes[a, e]) for a, f in self.ports for e in FACE_EDGES[f]}
        assert len(old_reps) == 9
        return {a: {e for e in EDGES if min(classes[a, e]) in old_reps} for a in self.cells}


def labelled_chart(words, paired, ports):
    """A pair lists its two cells and their respective opposite labels."""
    chart = Chart(range(len(words)))
    for a, mark_a, b, mark_b in paired:
        f, g = words[a].index(mark_a), words[b].index(mark_b)
        left, right = set(facet(words[a], f)), set(facet(words[b], g))
        paired_labels = {name: name for name in left & right}
        if left != right:
            old, = left - right
            new, = right - left
            paired_labels[old] = new
        p = tuple(g if i == f else words[b].index(paired_labels[v])
                  for i, v in enumerate(words[a]))
        chart.pair(a, f, b, p)
    for name, (cell, opposite, rename) in enumerate(ports):
        word = words[cell]
        f = word.index(opposite)
        chart.ports[cell, f] = (name, tuple("" if i == f else rename.get(v, v)
                                           for i, v in enumerate(word)))
    chart.check()
    return chart


def plain_ports(words, paired):
    paired_slots = {(a, f) for a, f, _, _ in paired} | {(b, g) for _, _, b, g in paired}
    return [(a, f, {}) for a, word in enumerate(words) for f in word
            if (a, f) not in paired_slots]


def check_separation():
    # Common facet 2 with matching frames.
    inp = ("abuc", "abvc")
    paired = [(0, "u", 1, "v")]
    out = labelled_chart(inp, paired, plain_ports(inp, paired)).replay(SEPARATE)
    old = out.boundary_edge_occurrences()
    port_cells = {a: f for a, f in out.ports}
    assert len(out.ports) == len(port_cells) == 6
    for a in out.cells:
        assert any(b != a and b not in port_cells
                   for (c, _), (b, _) in out.pairs.items() if a == c)
        if len(old[a]) > 1:
            assert a in port_cells and old[a] <= set(FACE_EDGES[port_cells[a]])
    for (a, f), (b, _) in out.pairs.items():
        assert not (a in port_cells and b in port_cells)
        assert len(old[a].intersection(FACE_EDGES[f])) <= 1
    return {
        "word": SEPARATE,
        "ports": sorted((name, a, f) for (a, f), (name, _) in out.ports.items()),
        "cells": [{"id": a, "neighbors": [out.pairs.get((a, f), (None, None))[0]
                                         for f in VERTICES],
                   "boundary_edge_occurrences": sorted(old[a])}
                  for a in sorted(out.cells)],
    }


def check_zero():
    natural = ("cuva", "cuvb")
    base_pairs = [(0, "a", 1, "b")]
    ports = plain_ports(natural, base_pairs)
    base = labelled_chart(natural, base_pairs, ports)
    arch = labelled_chart((*natural, "uvcd", "uvdc"), [
        (0, "a", 2, "d"),
        (1, "b", 2, "c"),
        (2, "u", 3, "u"),
        (2, "v", 3, "v"),
        (3, "c", 3, "d"),
    ], ports)
    return base.replay(ZERO_BASE).marked_code() == arch.replay(ZERO_ARCH).marked_code()


def check_lune():
    source = ("cxuv", "cxwv")
    seam = [(0, "u", 1, "w")]
    ports = plain_ports(source, seam)
    base = labelled_chart(source, seam, ports)
    target = labelled_chart((*source, "cxuw", "cxuw"), seam + [
        (0, "v", 2, "w"), (1, "v", 2, "u"), (2, "x", 3, "x"), (2, "c", 3, "c"),
    ], [(3, "w" if a == 0 else "u", r) if opp == "v" else (a, opp, r)
        for a, opp, r in ports])
    return base.replay(((0, 2), (2, 0))).marked_code() == target.marked_code()


def check_slide():
    inp = ("cuvd", "cquv")
    strand = [(0, "d", 1, "q")]
    ports = plain_ports(inp, strand)
    after = labelled_chart(("quvd", "cqud", "cqvd"), [
        (0, "v", 1, "c"), (0, "u", 2, "c"), (1, "u", 2, "v"),
    ], [(0, "q", {}), (2, "q", {}), (1, "q", {}),
        (0, "d", {}), (2, "d", {}), (1, "d", {})])
    return labelled_chart(inp, strand, ports).move(0, 3).marked_code() == after.marked_code()


def check_shortcut():
    inp = ("cpxu", "cpxw")
    membrane = [(0, "u", 1, "w")]
    ports = plain_ports(inp, membrane)
    after = labelled_chart(("cxuw", "pxuw", "cpuw"), [
        (0, "c", 1, "p"), (0, "x", 2, "p"), (1, "x", 2, "c"),
    ], [(1, "w", {}), (0, "w", {}), (2, "w", {}),
        (1, "u", {}), (0, "u", {}), (2, "u", {})])
    return labelled_chart(inp, membrane, ports).move(0, 3).marked_code() == after.marked_code()


def check_seed():
    inp = ("abxy", "abxz", "abyz")
    old_pairs = [(0, "y", 1, "z"), (0, "x", 2, "z"), (1, "x", 2, "y")]
    target = labelled_chart(("axyz", "bxyz", "ayzt", "byzt", "abzt"), [
        (0, "a", 1, "b"), (0, "x", 2, "t"), (1, "x", 3, "t"), (2, "a", 3, "b"),
        (2, "y", 4, "b"), (3, "y", 4, "a"), (4, "z", 4, "t"),
    ], [(1, "z", {}), (0, "z", {}), (1, "y", {}), (0, "y", {}),
        (3, "z", {"t": "z"}), (2, "z", {"t": "z"})])
    source = labelled_chart(inp, old_pairs, plain_ports(inp, old_pairs))
    return source.replay(((0, 3), (5, 3))).marked_code() == target.marked_code()


def main():
    result = {"separation": check_separation(),
              "zero_arch_join": check_zero(),
              "two_cell_lune": check_lune(),
              "buttress_slide": check_slide(),
              "ear_shortcut": check_shortcut(),
              "copying_seed": check_seed()}
    print(json.dumps(result, indent=2))
    checks = [value for key, value in result.items() if key != "separation"]
    if not all(checks):
        raise SystemExit("A boundary-relative equality failed")


if __name__ == "__main__":
    main()
