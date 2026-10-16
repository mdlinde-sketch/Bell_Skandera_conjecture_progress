"""Combine disjoint degree-16 C++ frontier outputs, validating full k coverage."""
import json
from collections import Counter
from pathlib import Path
d=16
paths=[f"independent_cpp_degree{d}_k1-5_20261016.json",
       f"independent_cpp_degree{d}_k6-8_20261016.json",
       f"independent_cpp_degree{d}_k9-10_20261016.json",
       f"independent_cpp_degree{d}_k11-11_20261016.json",
       f"independent_cpp_degree{d}_k12-15_20261016.json"]
out={"degree":d,"counts":Counter(),"by_k":{},"residual":[],"suspect":[]}
for path in paths:
    block=json.loads(Path(path).read_text())
    assert block["degree"]==d and not (set(block["by_k"])&set(out["by_k"]))
    out["by_k"].update(block["by_k"])
    out["counts"].update(block["counts"])
    for name in ("residual","suspect"):out[name].extend(block[name])
assert set(map(int,out["by_k"]))==set(range(1,d))
c=out["counts"]
assert c["raw"]==sum(c.get(k,0) for k in ("smyth_original","impossible_ud",
          "smyth_reverse_norm1","norm1_residual","ud_ge_3"))
assert c["norm1_residual"]==len(out["residual"])
assert c["ud_ge_3"]==len(out["suspect"])
out["counts"]=dict(c)
Path(f"independent_cpp_degree{d}_FULL_20261016.json").write_text(json.dumps(out,indent=2)+"\n")
print(out["counts"])
