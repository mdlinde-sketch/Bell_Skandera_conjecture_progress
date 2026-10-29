"""Independent exact norm-one H4 monotone-corner certificate, 29 Oct 2026.

This program reads the untrusted, independently generated frontier case lists.
It checks the q1..q4 prefix constraints and the lower q5 chord, then uses
an explicit 3x3 adjugate to certify BOTH:
  H4(q5=L5,q6=L6(L5))<0, and
  (d/dq5)H4(q5=L5,q6 fixed)<0.
With H2>=0, H3>=0 and dH4/dq6=-6H3<=0, this implies H4<0
for ALL q5>=L5 and q6>=L6(q5), with NO q5 upper bound,
vertex maximization, or q5 interval enumeration.

The output remains a conditional, UNREVIEWED finite-degree certificate.
"""
import json, math, sys, time, random, hashlib
from itertools import permutations
from pathlib import Path

C=math.comb
TRACE_NUM=17719
# Fixed canonical SHA256s from independently verified 25-28 Oct frontier witnesses.
EXPECTED_CASE_HASHES={9: ('d2316b1b55bfadec5d36f0098a1ac2fb5e756ca92ee029eead1d8cc2a491b197', '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945'), 10: ('5aab7db10dd9c9d970d971be08f29aee9a6cb78ebf2d9bc8459cb2cd0cef7a6d', '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945'), 11: ('1ad88569245c65c432050c8d69c49735f23789ccbd2de4a502a4128347dc3bc1', '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945'), 12: ('0bf4531d01d6922241e072645505ecb73bc6a632e1465a144b1f109bcc70ed59', '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945'), 13: ('5002d73ee54489cf0fc59501cba640c8cff4302d04c26f862689e56a1ace5a80', '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945'), 14: ('6a0511e97d490d9728bce571c7ae489c3f7c293373cc2de71e1394860442a810', '85f4374cc8bbebb5b73b6691a77b0927dab91817ba098f22d7f27801f022f5eb'), 15: ('7a587278f61d3794eebb8795512a46d3af2e2d58b337fe83fd42e283aaacf1cd', '9aef47ba87c1c4e5ca5c736dba236869656abcd63e1849f78c28b4552f69b055'), 16: ('9f1f933341c75743d019542cf211fb298b2e7e36201f314ff42d5b491f3253f6', 'bcd58517824add03c7cf448b0c101066989227471f781b872c4bb444627628ab'), 17: ('f2763600f7244981a711a4d581b078afa3cc285b9d847300b112995eb7b121e0', '48f93be87cc5fc15fc6ba20d104630633a35466d114462459be6cee5754763b7')}


def root_floor(a,b,n):
    assert a>=0 and b>0 and n>=1
    l,h=0,1
    while b*h**n<=a:h*=2
    while l+1<h:
        mid=(l+h)//2
        if b*mid**n<=a:l=mid
        else:h=mid
    return l

def chord(d,j,previous):
    e=d-j+1
    a=previous**(e-1)*C(d,j)**e
    b=C(d,j-1)**(e-1)
    f=root_floor(a,b,e)
    return f if b*f**e==a else f+1

def local(d,j,prev,prevprev):
    return C(d,j)*C(d,j-2)*prev**2//(C(d,j-1)**2*prevprev)

def tangent(d,j,q1,q2):
    return C(d,j)*q2**(j-1)*d**(j-2)//(C(d,2)**(j-1)*q1**(j-2))

def moments(d,q1,q2,q3,q4,q5=0,q6=0,limit=6):
    q=[1,q1,q2,q3,q4,q5,q6]
    p=[d]
    for j in range(1,limit+1):
        p.append(sum((-1)**(i-1)*q[i]*p[j-i] for i in range(1,j)) +(-1)**(j-1)*j*q[j])
    return p

def cofactor_values(p):
    a,b,c,e,f=p[0],p[1],p[2],p[3],p[4]
    A00=c*f-e*e
    A01=c*e-b*f
    A02=b*e-c*c
    A11=a*f-c*c
    A12=b*c-a*e
    A22=a*c-b*b
    H3=a*A00+b*A01+c*A02
    return H3,(A00,A01,A02,A11,A12,A22)

def h4_corner_and_slope(p):
    H3,(A00,A01,A02,A11,A12,A22)=cofactor_values(p)
    v0,v1,v2=p[3],p[4],p[5]
    quadratic=A00*v0*v0+2*A01*v0*v1+2*A02*v0*v2+A11*v1*v1+2*A12*v1*v2+A22*v2*v2
    corner=p[6]*H3-quadratic
    slope=6*p[1]*H3-10*(A02*v0+A12*v1+A22*v2)
    return corner,slope,H3,A22

def leibniz(matrix):
    n=len(matrix); total=0
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        prod=1
        for i in range(n):prod*=matrix[i][perm[i]]
        total+=sign*prod
    return total

def independent_controls(n=1500):
    rng=random.Random(20261029)
    for _ in range(n):
        d=rng.randint(7,23)
        q1,q2,q3,q4,q5,q6=[rng.randint(1,50) for i in range(6)]
        p=moments(d,q1,q2,q3,q4,q5,q6)
        h4,slope,h3,h2=h4_corner_and_slope(p)
        assert h4==leibniz([[p[i+j] for j in range(4)] for i in range(4)])
        assert h3==leibniz([[p[i+j] for j in range(3)] for i in range(3)])
        assert h2==d*p[2]-p[1]**2
        pplus=moments(d,q1,q2,q3,q4,q5+1,q6)
        hp=h4_corner_and_slope(pplus)[0]
        assert hp-h4==slope-25*h2
        pplus2=moments(d,q1,q2,q3,q4,q5+2,q6)
        hp2=h4_corner_and_slope(pplus2)[0]
        assert hp2-2*hp+h4==-50*h2
        p6plus=moments(d,q1,q2,q3,q4,q5,q6+1)
        assert h4_corner_and_slope(p6plus)[0]-h4==-6*h3
    return n

def verify(path):
    data=json.loads(Path(path).read_text())
    d=data['degree']; assert 9<=d<=17
    assert tuple(hashlib.sha256(json.dumps(sorted(data[key]),separators=(',',':')).encode()).hexdigest() for key in ('residual','suspect'))==EXPECTED_CASE_HASHES[d],('case-list hash mismatch',d)
    cases=data['residual']+data['suspect']
    out=dict(degree=d,cases=len(cases),q4_checked=0,h3_negative=0,
             corners=0,
             min_slope=None,max_slope=None,max_corner=None)
    for k,m,n,ud,um in cases:
        assert k in (d-4,d-3,d-2)
        q1lo=n if k==d-2 else TRACE_NUM*d//10000+1
        q1hi=n if k==d-2 else um
        for q1 in range(q1lo,q1hi+1):
            if k==d-4:
                q2lo=chord(d,2,q1)
                upper=C(d,k+2)*n*n*C(d,k)//(C(d,k+1)**2*m)
                q2hi=min(local(d,2,q1,1),upper)
            else:
                q2lo=q2hi=(m if k==d-2 else n)
            for q2 in range(q2lo,q2hi+1):
                if not chord(d,2,q1)<=q2<=local(d,2,q1,1):continue
                H2=d*(q1*q1-2*q2)-q1*q1
                if H2<0:continue
                t3,t4=[tangent(d,j,q1,q2) for j in (3,4)]
                q3lo=chord(d,3,q2)
                q3hi=min(local(d,3,q2,q1),t3)
                if k in (d-4,d-3):
                    q3lo=q3hi=n if k==d-4 else m
                    if not chord(d,3,q2)<=q3lo<=min(local(d,3,q2,q1),t3):continue
                for q3 in range(q3lo,q3hi+1):
                    q4lo=chord(d,4,q3)
                    q4hi=min(local(d,4,q3,q2),t4)
                    if k==d-4:
                        q4lo=q4hi=m
                        if not chord(d,4,q3)<=m<=min(local(d,4,q3,q2),t4):continue
                    for q4 in range(q4lo,q4hi+1):
                        out['q4_checked']+=1
                        p=moments(d,q1,q2,q3,q4,limit=4)
                        H3,_=cofactor_values(p)
                        if H3<0:
                            out['h3_negative']+=1
                            continue
                        lo=chord(d,5,q4)
                        q6lo=chord(d,6,lo)
                        p=moments(d,q1,q2,q3,q4,lo,q6lo)
                        corner,slope,h3,h2=h4_corner_and_slope(p)
                        assert h3==H3 and h2==H2
                        if not (corner<0 and slope<0):
                            raise AssertionError(('MONOTONIC_CORNER_FAILED',d,k,m,n,q1,q2,q3,q4,lo,corner,slope,h2,h3))
                        out['corners']+=1
                        out['min_slope']=slope if out['min_slope'] is None else min(out['min_slope'],slope)
                        out['max_slope']=slope if out['max_slope'] is None else max(out['max_slope'],slope)
                        out['max_corner']=corner if out['max_corner'] is None else max(out['max_corner'],corner)
    print('PASS',json.dumps(out,sort_keys=True),flush=True)
    return out

if __name__=='__main__':
    assert independent_controls()==1500
    print('PASS 1500 direct Leibniz 4x4 + exact derivative controls',flush=True)
    for filename in sys.argv[1:]:verify(filename)
