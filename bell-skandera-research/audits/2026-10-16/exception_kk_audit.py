"""Independent exact KK checks of all five Smyth exceptions and reciprocals."""
from math import comb

def kk(k, n):
    t=n; cap=n+k+2; ans=0
    for i in range(k,0,-1):
        a=i-1
        while a+1<cap and comb(a+1,i)<=t:
            a+=1
        if a>=i:
            ans+=comb(a,i+1)
            t-=comb(a,i)
        cap=a
    assert t==0
    return ans

S=[(1,1),(1,3,1),(1,5,6,1),(1,7,13,7,1),(1,7,14,8,1)]
for a in S:
    for b in (a,a[::-1]):
        assert b[0]==1 and b[-1]==1
        assert all(b[i+1]<=kk(i,b[i]) for i in range(1,len(b)-1)),b
        print(b,'KK-valid')
