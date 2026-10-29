#!/usr/bin/env python3
"""2026-10-29, independent small-excess (a1-degree<=6) arithmetic audit.
Standard-library only. Uses Smyth (1984), Newton/Maclaurin and Hankel PSD
as published mathematical inputs. NOT a proof of unrestricted Bell-Skandera.
"""
from math import comb
from functools import lru_cache

@lru_cache(None)
def kk(k,m):
    if not m: return 0
    r=k
    while comb(r+1,k)<=m:r+=1
    q=m-comb(r,k)
    return comb(r,k+1)+(kk(k-1,q) if q and k>1 else 0)

def mac(d,n,k):return comb(d,k)*n**k//d**k
def newton(d,k,prevprev,prev):
    return prev**2*comb(d,k-2)*comb(d,k)//(prevprev*comb(d,k-1)**2)

def dangerous(d,n,k):
    a,b=comb(d,k),comb(d,k+1)
    return [m for m in range(a,mac(d,n,k)+1)
            if b**k*m**(k+1)>=(kk(k,m)+1)**k*a**(k+1)]

def h3(d,n,b,c,e):
    p2=n*n-2*b
    p3=n*p2-b*n+3*c
    p4=n*p3-b*p2+c*n-4*e
    return d*p2*p4+2*n*p2*p3-d*p3*p3-p2**3-n*n*p4

def full(d,n):
    count=0
    def visit(a):
        nonlocal count
        k=len(a)
        if k==d+1:
            count+=1
            assert all(a[i+1]<=kk(i,a[i]) for i in range(1,d)),a
            return
        lim=min(mac(d,n,k),newton(d,k,a[k-2],a[k-1]))
        for v in range(comb(d,k),lim+1):visit(a+[v])
    visit([1,n])
    return count

def prefix(d,n):
    c=[comb(d,k) for k in range(d+1)]
    suspects=dangerous(d,n,5)
    assert not dangerous(d,n,d-1),("terminal-index gap",d,n)
    counts=[0,0,0,0,0]
    for b in range(c[2],mac(d,n,2)+1):
        counts[0]+=1
        for x in range(c[3],min(mac(d,n,3),newton(d,3,n,b))+1):
            counts[1]+=1
            for y in range(c[4],min(mac(d,n,4),newton(d,4,b,x))+1):
                counts[2]+=1
                if h3(d,n,b,x,y)<0:continue
                counts[3]+=1
                assert x<=kk(2,b) and y<=kk(3,x),(d,n,b,x,y)
                hi5=min(mac(d,n,5),newton(d,5,x,y))
                assert hi5<=kk(4,y),(d,n,b,x,y,hi5)
                for z in suspects:
                    if z>hi5:continue
                    counts[4]+=1
                    hi6=min(mac(d,n,6),newton(d,6,y,z))
                    assert hi6<=kk(5,z),(d,n,b,x,y,z,hi6)
    return counts

def main():
    exceptions=((1,1),(1,3,1),(1,5,6,1),
                (1,7,13,7,1),(1,7,14,8,1))
    for a in exceptions:
        assert all(a[i+1]<=kk(i,a[i]) for i in range(1,len(a)-1))
    # All nonexceptional irreducibles have [t]F > 17719*d/10000.
    # For excess s<=6 this implies d<=7. d<=3 has an analytic proof.
    for d in range(4,8):
        for n in range(17719*d//10000+1,d+7):
            if d<=5:
                print(f"d={d} n={n} full={full(d,n)} KK offenders=0")
            else:
                print(f"d={d} n={n} prefix={prefix(d,n)} KK offenders=0")
    print("PASS: arithmetic lemma for all excess s<=6 (external review pending)")
if __name__=="__main__":main()
