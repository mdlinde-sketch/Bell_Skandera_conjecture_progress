"""Constructive independent f-complex witnesses for Smyth exceptions, 2026-10-22."""
from itertools import combinations
from collections import Counter
import json

SMYTH={
    'x-1':[1,1],
    'x2-3x+1':[1,3,1],
    'x3-5x2+6x-1':[1,5,6,1],
    'x4-7x3+13x2-7x+1':[1,7,13,7,1],
    'x4-7x3+14x2-8x+1':[1,7,14,8,1],
}

def colex(face):return tuple(reversed(face))

def build_complex(f):
    nv=f[1];faces={()}
    for size in range(1,len(f)):
        all_faces=sorted(combinations(range(1,nv+1),size),key=colex)
        assert len(all_faces)>=f[size]
        faces.update(all_faces[:f[size]])
    for s in faces:
        for i in range(len(s)):
            assert s[:i]+s[i+1:] in faces
    counts=Counter(map(len,faces))
    assert [counts[i] for i in range(len(f))]==f
    facets=[s for s in faces if not any(len(t)>len(s) and set(s).issubset(t) for t in faces)]
    recovered={()}
    for facet in facets:
        for j in range(len(facet)+1):recovered.update(combinations(facet,j))
    assert recovered==faces
    return facets

def join_facets(fa,fb):
    off=max((max(s) for s in fa if s),default=0)
    return [tuple(sorted(a+tuple(x+off for x in b))) for a in fa for b in fb]

def coeff_from_facets(facets):
    faces={()}
    for s in facets:
        for j in range(len(s)+1):faces.update(combinations(s,j))
    count=Counter(map(len,faces))
    return [count[i] for i in range(max(count)+1)]

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def audit():
    records=[]
    for name,orig in SMYTH.items():
        for rev,vector in [(False,orig),(True,orig[::-1])]:
            facets=build_complex(vector)
            records.append({'factor':name,'reciprocal':rev,'f_vector':vector,
                            'facets':[list(f) for f in facets]})
    for A in records:
        for B in records:
            joined=join_facets([tuple(x) for x in A['facets']],
                               [tuple(x) for x in B['facets']])
            assert coeff_from_facets(joined)==mul(A['f_vector'],B['f_vector'])
    print('PASS: 10 exception/reverse f-vectors, 100 explicit joins')
    with open('exception_join_witnesses_20261022.json','w') as out:
        json.dump(records,out,indent=2)
    for r in records:
        print(r['factor'],'reciprocal='+str(r['reciprocal']),r['f_vector'],'facets',len(r['facets']))

if __name__=='__main__':audit()
