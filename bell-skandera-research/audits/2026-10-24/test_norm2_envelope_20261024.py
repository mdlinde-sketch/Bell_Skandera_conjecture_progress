"""Independent adversarial controls for the 24 Oct norm-two H3 envelope."""
from random import Random
from math import comb
from norm2_quadratic_envelope_20261024 import (
    det3,lower_chord,local_upper,maximum_quadratic_integer
)
R=Random(20261024)
FACTORS=[[1,1],[1,3,1],[1,5,6,1],[1,7,13,7,1],[1,7,14,8,1]]
def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def h3_direct(d,n,m,a3,a4):
    from itertools import permutations
    e=[1,n,2*m,4*a3,8*a4]
    p=[d]
    for j in range(1,5):
        p.append(sum((-1)**(i-1)*e[i]*p[j-i] for i in range(1,j))
                 +(-1)**(j-1)*j*e[j])
    H=[[p[i+j] for j in range(3)] for i in range(3)]
    return sum((-1)**sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))
               *H[0][t[0]]*H[1][t[1]]*H[2][t[2]]
               for t in permutations(range(3)))

# Verify coefficient identities, slope and quadratic coefficient on randomized
# arbitrary integer coefficient choices (even those not positive-rooted).
for _ in range(3000):
    d=R.randint(5,30);n=R.randint(5,100);m=R.randint(1,400)
    a3=R.randint(1,1000);a4=R.randint(1,1500)
    f=det3(d,n,m,a3,a4)
    assert f==h3_direct(d,n,m,a3,a4)
    H2=d*(n*n-4*m)-n*n
    assert det3(d,n,m,a3,a4+1)-f==-32*H2
    assert (det3(d,n,m,a3+2,a4)-2*det3(d,n,m,a3+1,a4)+f)//2==-144*d

# For actual totally-positive norm-two polynomials, verify all coefficient
# inequalities and H3 >= 0; also verify the envelope really dominates H3.
for d in range(5,18):
    for trial in range(120):
        f=[1,2]
        while len(f)-1<d:
            options=[g for g in FACTORS if len(g)-1<=d-(len(f)-1)]
            f=multiply(f,R.choice(options))
        assert len(f)==d+1 and f[-1]==2
        n,m,a3,a4=f[-2],f[-3],f[-4],f[-5]
        lo=lower_chord(d,3,m);hi=local_upper(d,3,m,n)
        assert lo<=a3<=hi
        amin=lower_chord(d,4,lo)
        assert a4>=amin
        h2=d*(n*n-4*m)-n*n
        assert h2>=0
        f0=det3(d,n,m,lo,amin)
        f1=det3(d,n,m,lo+1,amin)
        f2=det3(d,n,m,lo+2,amin)
        upper,A=maximum_quadratic_integer(f0,f1,f2,hi-lo)
        actual=det3(d,n,m,a3,a4)
        assert A==-144*d and upper>=actual and actual>=0
print('PASS 3,000 direct-Leibniz/derivative controls; 1,560 genuine norm-two positive-root controls')
