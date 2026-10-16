"""Positive-root moment controls of degree 14, deterministic seeds, exact integers."""
import random
R=random.Random(20261016)
def det3(a):
    return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def det4(a):
    A=[row[:] for row in a]; n=len(A); prev=1; sign=1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]),None)
            if j is None:return 0
            A[j],A[k]=A[k],A[j];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=A[i][j]*pivot-A[i][k]*A[k][j]
                assert val%prev==0
                A[i][j]=val//prev
        for i in range(k+1,n):A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]
for c in range(500):
    lambdas=[R.randrange(1,10) for _ in range(14)]
    q=[1]
    for x in lambdas:
        new=q+[0]
        for j in range(1,len(new)):
            new[j]=(q[j] if j<len(q) else 0)+x*q[j-1]
        q=new
    p=[len(lambdas)]+[sum(x**j for x in lambdas) for j in range(1,7)]
    for j in range(1,7):
        z=sum((-1)**(i-1)*q[i]*p[j-i] for i in range(1,j))
        z+=(-1)**(j-1)*j*q[j]
        assert z==p[j],(c,j,z,p[j])
    h3=det3([[p[i+j] for j in range(3)] for i in range(3)])
    h4=det4([[p[i+j] for j in range(4)] for i in range(4)])
    s3=det3([[p[i+j+1] for j in range(3)] for i in range(3)])
    assert h3>=0 and h4>=0 and s3>=0,(c,h3,h4,s3)
print("PASS: 500 seeded positive-rooted controls; exact Newton/PSD identities.")
