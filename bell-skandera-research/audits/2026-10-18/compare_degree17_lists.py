"""Verify independent C++ k13-16 and Python all-k candidate lists match exactly."""
import json,hashlib
from pathlib import Path
A=json.loads(Path('python_independent_frontier_degree17.json').read_text())
B=json.loads(Path('independent_cpp_degree17_k13-16_20261016.json').read_text())
assert A['degree']==B['degree']==17
assert {x[0] for x in A['residual']+A['suspect']} <= {13,14,15,16}
for key in ('residual','suspect'):
    assert sorted(A[key])==sorted(B[key]),key
    sha=hashlib.sha256(json.dumps(sorted(A[key]),separators=(',',':')).encode()).hexdigest()
    print('MATCH',key,len(A[key]),sha)
print('PASS independent exact candidate list equality for d17 k13-16')
