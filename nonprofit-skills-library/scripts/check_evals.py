#!/usr/bin/env python3
"""usage: python3 scripts/check_evals.py skills [category ...]  — validates evals/evals.json per skill."""
import json, sys, pathlib, re
root = pathlib.Path(sys.argv[1]); cats = sys.argv[2:]
names = {p.parent.name for p in root.glob("*/*/SKILL.md")}
errs = []; n = 0
for skill in sorted(root.glob("*/*/SKILL.md")):
    cat, name = skill.parent.parent.name, skill.parent.name
    if cats and cat not in cats: continue
    f = skill.parent / "evals" / "evals.json"
    if not f.exists(): errs.append(f"{name}: missing evals.json"); continue
    n += 1
    try: d = json.loads(f.read_text())
    except Exception as e: errs.append(f"{name}: bad JSON {e}"); continue
    if d.get("skill_name") != name: errs.append(f"{name}: skill_name mismatch")
    ev = d.get("evals", [])
    if len(ev) != 3: errs.append(f"{name}: needs 3 evals, has {len(ev)}")
    for i, e in enumerate(ev, 1):
        if e.get("id") != i: errs.append(f"{name}: eval ids must be 1..3")
        for k in ("prompt", "expected_output"):
            if not isinstance(e.get(k), str) or len(e[k]) < 40: errs.append(f"{name} #{i}: {k} missing/too short")
        a = e.get("assertions", [])
        if not (3 <= len(a) <= 6): errs.append(f"{name} #{i}: 3-6 assertions")
        if e.get("files"): errs.append(f"{name} #{i}: no input files in v1")
    if {e.get("type") for e in ev} != {"core", "varied", "edge"}: errs.append(f"{name}: types must be core, varied, edge")
    snt = d.get("should_not_trigger", [])
    if len(snt) != 2: errs.append(f"{name}: needs 2 should_not_trigger")
    for s in snt:
        if s.get("better_skill") not in names | {"none"}: errs.append(f"{name}: unknown better_skill {s.get('better_skill')}")
        if not s.get("query"): errs.append(f"{name}: empty should_not_trigger query")
    extra = [p.name for p in f.parent.iterdir() if p.name != "evals.json"]
    if extra: errs.append(f"{name}: unexpected files in evals/ {extra}")
print(f"{n} evals files checked"); [print("ERR", e) for e in errs]
sys.exit(1 if errs else 0)
