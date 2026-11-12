"""Krippendorff's alpha, Cohen's kappa, and bootstrap 95% intervals for Study Cycle 2.

Uses the exact Krippendorff's alpha formula (nominal and frequency-weighted ordinal) from v5/study/reliability.py,
extended to multi-rater units and 10,000-resample bootstrap 95% confidence intervals with fixed seed 20261111.
"""
import collections
import random

ORDER_V5 = ["contradicted", "undocumented", "claimed", "documented", "verified"]
BOOTSTRAP_SEED = 20261111
BOOTSTRAP_RESAMPLES = 10000


def part_a_category(value):
    """The Part A category without the free text in parentheses."""
    return value.split(" (")[0].strip()


def nominal_distance(a, b):
    return 0.0 if a == b else 1.0


def part_b_ordinal_distance(a, b):
    if a == b:
        return 0.0
    if a not in ORDER_V5 or b not in ORDER_V5:
        return 1.0
    return (( abs(ORDER_V5.index(a) - ORDER_V5.index(b)) ) / (len(ORDER_V5) - 1)) ** 2


def kalpha_units(units, order=None):
    """Krippendorff's alpha for units of >=2 ratings; nominal, or Krippendorff's frequency-weighted ordinal when order is given."""
    valid_units = [u for u in units if len(u) >= 2]
    if not valid_units:
        return None
    o = collections.Counter()
    n_c = collections.Counter()
    for u in valid_units:
        m = len(u)
        for v in u:
            n_c[v] += 1
        for i in range(m):
            for j in range(m):
                if i != j:
                    o[(u[i], u[j])] += 1.0 / (m - 1)
    n = sum(n_c.values())
    if n <= 1:
        return None
    values = sorted(n_c, key=order.index) if order else list(n_c)

    def delta(c, k):
        if c == k:
            return 0.0
        if order is None:
            return 1.0
        lo, hi = sorted((order.index(c), order.index(k)))
        between = sum(n_c[g] for g in values if lo <= order.index(g) <= hi)
        return (between - (n_c[c] + n_c[k]) / 2.0) ** 2

    d_o = sum(o[(c, k)] * delta(c, k) for c in values for k in values)
    d_e = sum(n_c[c] * n_c[k] * delta(c, k) for c in values for k in values) / (n - 1)
    return 1.0 if d_e == 0 else round(1.0 - d_o / d_e, 3)


def alpha(units, distance=None, order=None):
    if order is not None:
        return kalpha_units(units, order=order)
    if distance is part_b_ordinal_distance:
        return kalpha_units(units, order=ORDER_V5)
    return kalpha_units(units, order=None)


def alpha_with_ci(units, distance=None, seed=BOOTSTRAP_SEED, n_boot=BOOTSTRAP_RESAMPLES, order=None):
    """Return {'alpha': point, 'ci95': [low, high], 'n_units': len(valid_units)}."""
    valid_units = [u for u in units if len(u) >= 2]
    point = alpha(valid_units, distance=distance, order=order)
    if point is None or len(valid_units) < 2:
        return {"alpha": point, "ci95": [None, None], "n_units": len(valid_units)}
    rng = random.Random(seed)
    k = len(valid_units)
    samples = []
    for _ in range(n_boot):
        draw = [valid_units[rng.randrange(k)] for _ in range(k)]
        a = alpha(draw, distance=distance, order=order)
        if a is not None:
            samples.append(a)
    if not samples:
        return {"alpha": point, "ci95": [None, None], "n_units": k}
    samples.sort()
    lo = samples[int(0.025 * len(samples))]
    hi = samples[min(len(samples) - 1, int(0.975 * len(samples)))]
    return {"alpha": point, "ci95": [round(lo, 3), round(hi, 3)], "n_units": k}


def cohen_kappa(pairs):
    """Cohen's unweighted kappa for a list of (a, b) rating pairs."""
    if not pairs:
        return None
    n = len(pairs)
    po = sum(1 for a, b in pairs if a == b) / n
    cats = sorted({a for a, _ in pairs} | {b for _, b in pairs})
    pe = sum(
        (sum(1 for a, _ in pairs if a == c) / n) * (sum(1 for _, b in pairs if b == c) / n)
        for c in cats
    )
    if pe == 1.0:
        return 1.0
    return round((po - pe) / (1.0 - pe), 3)


def cohen_kappa_with_ci(pairs, seed=BOOTSTRAP_SEED, n_boot=BOOTSTRAP_RESAMPLES):
    """Return {'kappa': point, 'ci95': [low, high], 'raw_agreement': round(po, 3), 'n_pairs': len(pairs)}."""
    if not pairs:
        return {"kappa": None, "ci95": [None, None], "raw_agreement": None, "n_pairs": 0}
    point = cohen_kappa(pairs)
    po = round(sum(1 for a, b in pairs if a == b) / len(pairs), 3)
    if len(pairs) < 2:
        return {"kappa": point, "ci95": [None, None], "raw_agreement": po, "n_pairs": len(pairs)}
    rng = random.Random(seed)
    k = len(pairs)
    samples = []
    for _ in range(n_boot):
        draw = [pairs[rng.randrange(k)] for _ in range(k)]
        kap = cohen_kappa(draw)
        if kap is not None:
            samples.append(kap)
    samples.sort()
    lo = samples[int(0.025 * len(samples))]
    hi = samples[min(len(samples) - 1, int(0.975 * len(samples)))]
    return {"kappa": point, "ci95": [round(lo, 3), round(hi, 3)], "raw_agreement": po, "n_pairs": k}


def summarize_reliability(responses, benchmarks, seed=BOOTSTRAP_SEED, n_boot=BOOTSTRAP_RESAMPLES):
    """Compute full reliability statistics (including per-field Part A and bootstrap 95% CIs) for a dict of (benchmark, repeat) -> response."""
    part_a_pairs, part_a_same_cat, part_a_same_text = [], 0, 0
    part_a_per_facet = {}
    part_b_all, part_b_app = [], []
    na_both = na_one = 0

    for b in benchmarks:
        if (b, 1) not in responses or (b, 2) not in responses:
            continue
        r1, r2 = responses[(b, 1)], responses[(b, 2)]
        d1 = {d["facet"]: d["value"] for d in r1["description"]}
        d2 = {d["facet"]: d["value"] for d in r2["description"]}
        for f in d1:
            c1, c2 = f + ":" + part_a_category(d1[f]), f + ":" + part_a_category(d2[f])
            part_a_pairs.append([c1, c2])
            part_a_same_cat += c1 == c2
            part_a_same_text += d1[f] == d2[f]
            slot = part_a_per_facet.setdefault(f, {"pairs": 0, "same_category": 0, "same_text": 0})
            slot["pairs"] += 1
            slot["same_category"] += int(c1 == c2)
            slot["same_text"] += int(d1[f] == d2[f])
        j1 = {j["item_id"]: j["level"] for j in r1["judgments"]}
        j2 = {j["item_id"]: j["level"] for j in r2["judgments"]}
        for i in j1:
            pair = [j1[i], j2[i]]
            part_b_all.append(pair)
            if "not_applicable" in pair:
                if pair[0] == pair[1]:
                    na_both += 1
                else:
                    na_one += 1
            else:
                part_b_app.append(pair)

    pa_alpha = alpha_with_ci(part_a_pairs, nominal_distance, seed=seed, n_boot=n_boot)
    pb_ord = alpha_with_ci(part_b_app, part_b_ordinal_distance, seed=seed + 1, n_boot=n_boot, order=ORDER_V5)
    pb_nom = alpha_with_ci(part_b_all, nominal_distance, seed=seed + 2, n_boot=n_boot)
    na_pairs = [
        ("na" if p[0] == "not_applicable" else "app", "na" if p[1] == "not_applicable" else "app")
        for p in part_b_all
    ]
    na_kappa = cohen_kappa_with_ci(na_pairs, seed=seed + 3, n_boot=n_boot)

    return {
        "part_a_pairs": len(part_a_pairs),
        "part_a_same_category": part_a_same_cat,
        "part_a_same_text": part_a_same_text,
        "part_a_alpha_nominal": pa_alpha["alpha"],
        "part_a_alpha_nominal_ci95": pa_alpha["ci95"],
        "part_a_per_facet": part_a_per_facet,
        "part_b_pairs": len(part_b_all),
        "part_b_same_level": sum(a == b for a, b in part_b_all),
        "part_b_not_applicable_pairs": na_both + na_one,
        "part_b_not_applicable_concordant": na_both,
        "part_b_not_applicable_kappa": na_kappa["kappa"],
        "part_b_not_applicable_kappa_ci95": na_kappa["ci95"],
        "part_b_applicable_pairs": len(part_b_app),
        "part_b_alpha_ordinal": pb_ord["alpha"],
        "part_b_alpha_ordinal_ci95": pb_ord["ci95"],
        "part_b_alpha_nominal": pb_nom["alpha"],
        "part_b_alpha_nominal_ci95": pb_nom["ci95"],
    }
