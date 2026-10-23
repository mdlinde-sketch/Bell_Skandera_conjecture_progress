"""Exact rational Sturm positive-root counts for five Smyth exceptions."""
from fractions import Fraction as Q
from exception_join_certificate import SMYTH

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def derivative(p):return trim([i*p[i] for i in range(1,len(p))])

def neg_rem(p,q):
    a=list(p)
    while len(a)>=len(q) and a[-1]:
        c=a[-1]/q[-1];offset=len(a)-len(q)
        for j,x in enumerate(q):a[offset+j]-=c*x
        trim(a)
    return trim([-x for x in a])

def sturm(p):
    seq=[trim([Q(c) for c in p]),derivative(p)]
    while len(seq[-1])>1:
        nxt=neg_rem(seq[-2],seq[-1])
        assert any(nxt),'repeated root'
        seq.append(nxt)
    return seq

def variations(seq,at_infinity):
    vals=[p[-1] if at_infinity else p[0] for p in seq]
    signs=[1 if x>0 else -1 for x in vals if x]
    return sum(a!=b for a,b in zip(signs,signs[1:]))

def audit():
    for name,f in SMYTH.items():
        d=len(f)-1
        P=[(-1)**(d-i)*f[d-i] for i in range(d+1)]
        assert P[-1]==1 and P[0] in (-1,1)
        seq=sturm(P)
        npos=variations(seq,False)-variations(seq,True)
        assert npos==d,(name,npos,d)
        print('CERTIFIED',name,'degree',d,'positive roots',npos,'Sturm chain',len(seq))
    print('PASS 5 exact-rational Sturm root counts')

if __name__=='__main__':audit()
