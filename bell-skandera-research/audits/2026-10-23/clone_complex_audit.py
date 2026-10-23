"""Exact constructive test of the vertex-cloning identity f_Delta(Nt).
Each original vertex is replaced by N distinct clones; each face may
contain at most one clone of any original vertex. No external packages.
"""
from itertools import combinations,product
from collections import Counter

EXCEPTIONS=[
    [1,1],[1,3,1],[1,5,6,1],[1,7,13,7,1],[1,7,14,8,1]
]

def colex(face):return tuple(reversed(face))

def original_facets(f):
    n=f[1];faces={()}
    for size in range(1,len(f)):
        ranked=sorted(combinations(range(1,n+1),size),key=colex)
        faces.update(ranked[:f[size]])
    for face in faces:
        for j in range(len(face)):
            assert face[:j]+face[j+1:] in faces
    counts=Counter(map(len,faces))
    assert [counts[j] for j in range(len(f))]==f
    return [face for face in faces if not any(
        len(g)>len(face) and set(face).issubset(g) for g in faces)]

def cloned_facets(facets,n):
    return [tuple((v-1)*n+c+1 for v,c in zip(face,clones))
            for face in facets for clones in product(range(n),repeat=len(face))]

def fvector(facets):
    faces={()}
    for face in facets:
        for j in range(1,len(face)+1):
            faces.update(combinations(face,j))
    counts=Counter(map(len,faces))
    return [counts[j] for j in range(max(counts)+1)]

def audit():
    tests=0
    for f in EXCEPTIONS:
        for vec in (f,f[::-1]):
            facets=original_facets(vec)
            for n in (1,2,3,4):
                actual=fvector(cloned_facets(facets,n))
                expected=[x*n**j for j,x in enumerate(vec)]
                assert actual==expected,(vec,n,actual,expected)
                tests+=1
    assert tests==40
    print("PASS",tests,"constructive exceptional/reverse vertex-cloning tests")

if __name__=="__main__":audit()
