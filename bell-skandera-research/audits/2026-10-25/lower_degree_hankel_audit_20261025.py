"""Generalized degree-9-through-17 Hankel audit using fraction-free Bareiss determinants.
No C++ Schur complement, no Leibniz expansion, no q4 monotonicity shortcut.
"""
from math import comb
import json,sys,time

def bareiss(matrix):
    a=[list(row) for row in matrix]
    n=len(a);sign=1;previous=1
    for k in range(n-1):
        if a[k][k]==0:
            r=next((r for r in range(k+1,n) if a[r][k]),None)
            if r is None:return 0
            a[k],a[r]=a[r],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=pivot*a[i][j]-a[i][k]*a[k][j]
                assert num%previous==0
                a[i][j]=num//previous
            a[i][k]=0
        previous=pivot
    return sign*a[n-1][n-1]

def floor_root_quotient(num,den,exp):
    lo=0;hi=1
    while den*hi**exp<=num:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if den*mid**exp<=num:lo=mid
        else:hi=mid
    return lo

def ceil_root_quotient(num,den,exp):
    lo=floor_root_quotient(num,den,exp)
    return lo if den*lo**exp==num else lo+1

def chord(d,j,previous):
    power=d-j+1
    return ceil_root_quotient(previous**(power-1)*comb(d,j)**power,
                              comb(d,j-1)**(power-1),power)

def local(d,j,prev,prev2):
    return comb(d,j)*comb(d,j-2)*prev*prev//(comb(d,j-1)**2*prev2)

def tangent(d,j,q1,q2):
    return comb(d,j)*q2**(j-1)*d**(j-2)//(comb(d,2)**(j-1)*q1**(j-2))

def moment_prefix(d,q1,q2,q3,q4):
    p0=d;p1=q1;p2=q1*p1-2*q2
    p3=q1*p2-q2*p1+3*q3
    p4=q1*p3-q2*p2+q3*p1-4*q4
    return p0,p1,p2,p3,p4

def h3(p):
    return bareiss([[p[i+j] for j in range(3)] for i in range(3)])

def h4(p,q1,q2,q3,q4,q5,q6):
    p5=q1*p[4]-q2*p[3]+q3*p[2]-q4*p[1]+5*q5
    p6=q1*p5-q2*p[4]+q3*p[3]-q4*p[2]+q5*p[1]-6*q6
    ps=list(p)+[p5,p6]
    return bareiss([[ps[i+j] for j in range(4)] for i in range(4)])

def quadratic_max(f0,f1,f2,width):
    diff=f2-2*f1+f0
    assert diff%2==0
    A=diff//2;B=f1-f0-A
    assert A<=0
    def val(t):return f0+B*t+A*t*t
    mx=max(val(0),val(width))
    if A<0 and B>0:
        t=min(width,B//(-2*A))
        mx=max(mx,val(t),val(min(width,t+1)))
    return mx,A

def check(path):
    obj=json.load(open(path));d=obj['degree'];assert 9<=d<=17
    cases=obj['residual']+obj['suspect']
    stats={'cases':0,'q12_prefixes':0,'q3_nodes':0,'q4_checks':0,
           'h3_negative':0,'intervals':0,'q5_integers':0,'worst_H4':None}
    start=time.monotonic()
    for k,m,n,ud,um in cases:
        stats['cases']+=1
        assert k in (d-4,d-3,d-2)
        q1lo=n if k==d-2 else (17719*d//10000+1)
        q1hi=n if k==d-2 else um
        for q1 in range(q1lo,q1hi+1):
            if k==d-4:
                q2lo=chord(d,2,q1)
                pairbound=comb(d,k+2)*n*n*comb(d,k)//(comb(d,k+1)**2*m)
                q2hi=min(local(d,2,q1,1),pairbound)
            else:q2lo=q2hi=(m if k==d-2 else n)
            for q2 in range(q2lo,q2hi+1):
                if q2<chord(d,2,q1) or q2>local(d,2,q1,1):continue
                p2=q1*q1-2*q2
                H2=d*p2-q1*q1
                if H2<0:continue
                stats['q12_prefixes']+=1
                t3,t4,t5=(tangent(d,j,q1,q2) for j in (3,4,5))
                q3lo=chord(d,3,q2)
                q3hi=min(local(d,3,q2,q1),t3)
                if k in (d-4,d-3):
                    q3lo=q3hi=(n if k==d-4 else m)
                    if not chord(d,3,q2)<=q3lo<=min(local(d,3,q2,q1),t3):continue
                for q3 in range(q3lo,q3hi+1):
                    stats['q3_nodes']+=1
                    q4lo=chord(d,4,q3)
                    q4hi=min(local(d,4,q3,q2),t4)
                    if k==d-4:
                        q4lo=q4hi=m
                        if not chord(d,4,q3)<=m<=min(local(d,4,q3,q2),t4):continue
                    for q4 in range(q4lo,q4hi+1):
                        stats['q4_checks']+=1
                        p=moment_prefix(d,q1,q2,q3,q4)
                        H3=h3(p)
                        if H3<0:
                            stats['h3_negative']+=1
                            continue
                        q5lo=chord(d,5,q4)
                        q5hi=min(local(d,5,q4,q3),t5)
                        if q5lo>q5hi:continue
                        q6lo=chord(d,6,q5lo)
                        f0=h4(p,q1,q2,q3,q4,q5lo,q6lo)
                        f1=h4(p,q1,q2,q3,q4,q5lo+1,q6lo)
                        f2=h4(p,q1,q2,q3,q4,q5lo+2,q6lo)
                        mx,A=quadratic_max(f0,f1,f2,q5hi-q5lo)
                        assert A==-25*H2,(A,H2)
                        if mx>=0:
                            raise AssertionError(('UNEXCLUDED',k,m,n,q1,q2,q3,q4,q5lo,q5hi,mx))
                        stats['intervals']+=1
                        stats['q5_integers']+=q5hi-q5lo+1
                        if stats['worst_H4'] is None or mx>stats['worst_H4']:
                            stats['worst_H4']=mx
        if stats['cases']%250==0:
            print('PROGRESS',stats['cases'],len(cases),
                  'seconds',round(time.monotonic()-start,1),flush=True)
    assert stats['cases']==len(cases)
    print('PASS',json.dumps(stats,sort_keys=True),
          'seconds',round(time.monotonic()-start,2),flush=True)
    return stats

if __name__=='__main__':check(sys.argv[1])
