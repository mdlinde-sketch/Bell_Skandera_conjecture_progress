"""Exact norm-two exceptional case audit through degree 16.

Requires audit_norm2_degree14_20261016.py in same folder, and an independently
generated full residual/suspect JSON. Does NOT independently classify the cases.
"""
import json
import sys
from audit_norm2_degree14_20261016 import audit

def check(path):
    j=json.load(open(path))
    d=j["degree"]
    output=[]
    for k,m,n,ud,um in j["suspect"]:
        assert ud==3,(d,k,m,n,ud)
        v=audit(n,m,d=d)
        assert v["max_h3_at_lower"] is not None
        assert not v["nonnegative_h3_candidates"],(d,k,m,n,v)
        # For norm three, inverse-trace lemma forces (1+t);
        # ln 3 < 2 means this exact sufficient inequality has no logs.
        assert 20*um+180 < 87*d,(d,k,m,n,um)
        output.append({"k":k,"m":m,"n":n,
                       "q3_interval":v["q3_interval"],
                       "largest_H3":v["max_h3_at_lower"]})
    print("PASS",d,"special norm-two cases",len(output),
          "largest H3",max((v["largest_H3"] for v in output),default=None))
    return output

if __name__=="__main__":
    for p in sys.argv[1:]:check(p)
