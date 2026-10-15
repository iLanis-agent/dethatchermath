#!/usr/bin/env python3
# Dethatcher Math oracle - mirrors engine.js float-for-float.
import json, math
OVERLAP = 0.85
WALKFT = 132
FIRST = 0.7
SECOND = 0.9
BITEBAR = 0.3
THATCH = 0.005
PACKING = 0.8
def r1(x): return math.floor(x*10+0.5)/10
def f1(x): return "%.1f" % r1(x)
def jsnum(x):
    i = int(x)
    return i if x == i else x

def coverage_plan(claim, sqft):
    if not (claim > 0): return {"error": "the claimed inches must be above zero"}
    if not (sqft > 0): return {"error": "the square feet must be above zero"}
    honest_raw = claim * OVERLAP
    rate_raw = honest_raw / 12 * WALKFT
    min_raw = sqft / rate_raw
    verdict = "done before the grill heats" if min_raw <= 25 else ("a working morning" if min_raw <= 70 else "a second Saturday, honestly")
    return {"honestIn": jsnum(r1(honest_raw)), "minutes": jsnum(r1(min_raw)), "verdict": verdict}
def render_coverage(r, claim, sqft):
    min_word = "1 minute" if r["minutes"] == 1 else f1(r["minutes"]) + " minutes"
    return ("The %s-inch claim honestly sweeps %s inches after the 0.85 overlap norm; %s square feet at the 1.5-mile-an-hour walk norm takes %s - %s."
            % (claim, f1(r["honestIn"]), sqft, min_word, r["verdict"]))

def depth_plan(claim):
    if not (claim > 0): return {"error": "the claimed inches must be above zero"}
    first_raw = claim * FIRST
    second_raw = claim * SECOND
    verdict = "one pass through the thatch" if first_raw >= BITEBAR else ("two passes through the thatch" if second_raw >= BITEBAR else "a comb-over, honestly")
    return {"firstIn": jsnum(r1(first_raw)), "secondIn": jsnum(r1(second_raw)), "verdict": verdict}
def render_depth(r, claim):
    return ("The %s-inch claim honestly bites %s inches on the first pass and %s on the second (labeled norms); against the 0.3-inch bite bar, %s."
            % (claim, f1(r["firstIn"]), f1(r["secondIn"]), r["verdict"]))

def bag_plan(sqft, bag):
    if not (sqft > 0): return {"error": "the square feet must be above zero"}
    if not (bag > 0): return {"error": "the claimed bushels must be above zero"}
    thatch_raw = sqft * THATCH
    hold_raw = bag * PACKING
    fills = math.ceil(thatch_raw / hold_raw)
    verdict = "a few trips to the curb" if fills <= 4 else ("a working rhythm" if fills <= 10 else "a wheelbarrow of trips")
    return {"bushels": jsnum(r1(thatch_raw)), "holds": jsnum(r1(hold_raw)), "fills": fills, "verdict": verdict}
def render_bag(r, sqft, bag):
    fill_word = "1 fill" if r["fills"] == 1 else "%s fills" % r["fills"]
    return ("%s square feet at the 0.005-bushels-a-square-foot thatch norm is %s bushels; the claimed %s-bushel bag honestly holds %s after the 0.8 packing norm; %s - %s."
            % (sqft, f1(r["bushels"]), bag, f1(r["holds"]), fill_word, r["verdict"]))

CASES = [
    ("coverage", (15,5000)), ("coverage", (20,3000)), ("coverage", (13,9000)),
    ("coverage", (16,4000)), ("coverage", (22,2500)), ("coverage", (10,4000)),
    ("depth", (0.5,)), ("depth", (0.6,)), ("depth", (0.25,)),
    ("depth", (0.7,)), ("depth", (0.35,)), ("depth", (0.8,)),
    ("bag", (5000,2.5)), ("bag", (2000,3)), ("bag", (1500,4)),
    ("bag", (8000,2)), ("bag", (1000,5)), ("bag", (3000,2)),
    ("coverage", (0,5000)), ("coverage", (15,0)),
    ("depth", (0,)),
    ("bag", (0,2.5)), ("bag", (5000,0)),
]
PLANS = {"coverage": (coverage_plan, render_coverage), "depth": (depth_plan, render_depth), "bag": (bag_plan, render_bag)}
out = []
for tool, args in CASES:
    plan, render = PLANS[tool]
    r = plan(*args)
    case = {"tool": tool, "args": list(args), "result": r}
    if "error" not in r:
        case["render"] = render(r, *args)
    out.append(case)
print(json.dumps(out, separators=(",", ":")), end="")
