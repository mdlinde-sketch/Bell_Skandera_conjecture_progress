"""Independent Python vs C++ interval-frontier classification audit d2..17."""
import json,hashlib
for d in range(2,18):
    p=json.load(open(f'python_independent_frontier_degree{d}.json'))
    c=json.load(open(f'cpp_interval_frontier_degree{d}_20261018.json'))
    for key in ('residual','suspect'):
        assert sorted(p[key])==sorted(c[key]),(d,key)
    assert p['counts']['blocks']==c['counts']['blocks'],d
    assert p['counts'].get('n_explicit',0)==c['counts']['n_explicit'],d
    print('MATCH',d,len(p['residual']),len(p['suspect']),c['counts']['blocks'],c['counts']['n_explicit'])
print('PASS all degree-2-through-17 candidate lists and partition counts')
