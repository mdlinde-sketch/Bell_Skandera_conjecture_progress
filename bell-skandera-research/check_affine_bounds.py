"""Audit affine determinant pruning using separate rational elimination.
Tests arithmetic identities and known-positive-root controls, not exhaustiveness.
"""
from fractions import Fraction
from random import Random
from degree12_search import affine_bound,N
from explore import moments

def rational_det(A):
    A=[[Fraction(x) for x in row] for row in A];result=Fraction(1)
    for j in range(len(A)):
        pivot=next((i for i in range(j,len(A)) if A[i][j]),None)
        if pivot is None:return 0
        if pivot!=j:A[j],A[pivot]=A[pivot],A[j];result=-result
        x=A[j][j];result*=x
        for i in range(j+1,len(A)):
            factor=A[i][j]/x
            for k in range(j+1,len(A)):A[i][k]-=factor*A[j][k]
    return result

def main():
    rng=Random(12012);checks=0
    for _ in range(100):
        u=[1]+[rng.randrange(1,1000) for _ in range(N)]
        for j in range(1,N+1):
            b,a=affine_bound(u,j);shift=j%2;q=(j-shift)//2+1
            for value in (0,1,2,17,u[j]):
                v=u[:];v[j]=value;p=moments(v,j)
                d=rational_det([[p[x+y+shift] for y in range(q)] for x in range(q)])
                assert d==b+a*value
                if a>0:assert (d>=0)==(value>=-(b//a))
                elif a<0:assert (d>=0)==(value<=b//(-a))
                checks+=1
    for _ in range(100):
        roots=[rng.randrange(1,8) for _ in range(N)];u=[1]+[0]*N
        for root in roots:
            for j in range(N,0,-1):u[j]+=root*u[j-1]
        for j in range(1,N+1):
            b,a=affine_bound(u,j);shift=j%2;q=(j-shift)//2+1
            p=[sum(r**s for r in roots) for s in range(j+1)]
            d=rational_det([[p[x+y+shift] for y in range(q)] for x in range(q)])
            assert d==b+a*u[j]>=0
            checks+=1
    print('PASS:',checks,'exact affine/rounding/positive-root checks; not an exhaustive-search audit')

if __name__=='__main__':main()
