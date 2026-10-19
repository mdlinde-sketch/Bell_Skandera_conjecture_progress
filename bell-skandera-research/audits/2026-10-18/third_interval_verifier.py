"""Independent all-prefix exact integer certificate audit, degrees 14-16.

This deliberately does not import the C++ implementation, its recurrence routines,
or any original proof scripts. It receives the finite residual adjacent-pair list
from an external frontier generator: it does NOT independently certify that list.
For every case in that list it checks all logically admissible q1..q4 prefixes,
and eliminates whole q5 intervals using the independently evaluated H4 quadratic.
"""
import json,sys
from math import comb

def det4(M):
    # Completely independent Leibniz determinant, avoiding Schur complement and C++ code
    import itertools
    s=0
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        s+=(-1 if inv%2 else 1)*M[0][p[0]]*M[1][p[1]]*M[2][p[2]]*M[3][p[3]]
    return s

def lower(d,j,prev):
    a=d-j+1
    num=pow(prev,a-1)*pow(comb(d,j),a)
    den=pow(comb(d,j-1),a-1)
    # ceil a-th integer root of num/den, exact
    x=1
    while den*pow(x,a)<num:
        x*=2
    low=x//2
    while low+1<x:
        mid=(low+x)//2
        if den*pow(mid,a)>=num:x=mid
        else:low=mid
    return x

def local(d,j,u1,u2):
    return comb(d,j)*comb(d,j-2)*u1*u1//(comb(d,j-1)**2*u2)

def tan(d,j,e1,e2):
    return comb(d,j)*e2**(j-1)*d**(j-2)//(comb(d,2)**(j-1)*e1**(j-2))

def moments(d,qs):
    p=[d]
    for r in range(1,7):
        term=sum((-1)**(i-1)*qs[i]*p[r-i] for i in range(1,r))
        term+=(-1)**(r-1)*r*qs[r]
        p.append(term)
    return p

def h4(d,a,b,c,e,f,g):
    p=moments(d,[1,a,b,c,e,f,g])
    return det4([[p[i+j] for j in range(4)] for i in range(4)])

def h3(d,a,b,c,e):
    p=moments(d,[1,a,b,c,e,0,0])
    x,y,z,w,v=p[:5]
    return x*(z*v-w*w)-y*(y*v-z*w)+z*(y*w-z*z)

def max_quadratic(f0,f1,f2,width):
    A=(f2-2*f1+f0)//2
    assert 2*A==f2-2*f1+f0
    B=f1-f0-A
    def v(t):return f0+B*t+A*t*t
    candidates=[0,width]
    if A<0 and B>0:
        t=min(width,B//(-2*A));candidates.extend([t,min(width,t+1)])
    # A>=0 is convex, so endpoints are sufficient
    return max(v(t) for t in candidates),A

def audit(path):
    data=json.load(open(path));d=data['degree']
    st=dict(cases=0,prefixes=0,depth3=0,depth4=0,positive_H3=0,intervals=0,q5_excluded=0,uncleared=0)
    rows=data['residual']+data['suspect']
    for k,m,n,ud,um in rows:
        st['cases']+=1
        assert k in (d-4,d-3,d-2),(d,k,m,n)
        q1range=[n] if k==d-2 else range(17719*d//10000+1,um+1)
        for q1 in q1range:
            bound2=comb(d,k+2)*n*n*comb(d,k)//(comb(d,k+1)**2*m) if k==d-4 else None
            q2range=range(lower(d,2,q1), min(local(d,2,q1,1),bound2)+1) if k==d-4 else [m if k==d-2 else n]
            for q2 in q2range:
                if (d-1)*q1*q1 < 2*d*q2:continue
                if not(lower(d,2,q1)<=q2<=local(d,2,q1,1)):continue
                st['prefixes']+=1
                tang=[None,None,None]+[tan(d,j,q1,q2) for j in range(3,7)]
                q3lo=lower(d,3,q2);q3hi=min(tang[3],local(d,3,q2,q1))
                if k in (d-3,d-4):
                    q3fixed=m if k==d-3 else n
                    q3lo=max(q3lo,q3fixed);q3hi=min(q3hi,q3fixed)
                for q3 in range(q3lo,q3hi+1):
                    st['depth3']+=1
                    q4lo=lower(d,4,q3);q4hi=min(tang[4],local(d,4,q3,q2))
                    if k==d-4:
                        q4lo=max(q4lo,m);q4hi=min(q4hi,m)
                    for q4 in range(q4lo,q4hi+1):
                        # Check exactly rather than exploiting H3's affine monotonicity.
                        H3=h3(d,q1,q2,q3,q4)
                        if H3<0:break
                        st['depth4']+=1
                        st['positive_H3']+=1
                        q5lo=lower(d,5,q4);q5hi=min(tang[5],local(d,5,q4,q3))
                        if q5lo>q5hi:continue
                        q6min=lower(d,6,q5lo)
                        f0=h4(d,q1,q2,q3,q4,q5lo,q6min)
                        f1=h4(d,q1,q2,q3,q4,q5lo+1,q6min)
                        f2=h4(d,q1,q2,q3,q4,q5lo+2,q6min)
                        maxH,A=max_quadratic(f0,f1,f2,q5hi-q5lo)
                        H2=d*(q1*q1-2*q2)-q1*q1
                        assert A==-25*H2
                        assert H2>=0
                        st['intervals']+=1
                        if maxH>=0:
                            st['uncleared']+=1
                            print('UNCLEARED',d,k,m,n,q1,q2,q3,q4, q5lo,q5hi,maxH)
                            raise AssertionError('interval might contain survivor: exact DFS required')
                        st['q5_excluded']+=q5hi-q5lo+1
        if st['cases']%100==0:print('progress',d,st['cases'],'/',len(rows),flush=True)
    print('PASS',d,st,flush=True)
    return st

if __name__=='__main__':
    for path in sys.argv[1:]:audit(path)
