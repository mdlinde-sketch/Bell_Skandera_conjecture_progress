"""Independent exact H3 test of degree-14 norm-2 exceptional coefficient pairs.
Uses only Newton log-concavity, chord-to-top coefficient and moment PSD.
"""
from math import comb
import json

def lower_chord(d,j,qprev,qd=1):
    a=d-j+1
    lhs_factor=comb(d,j-1)**(a-1)
    rhs=qprev**(a-1)*qd*comb(d,j)**a
    lo=0;hi=1
    while hi**a*lhs_factor<rhs:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**a*lhs_factor>=rhs:hi=mid
        else:lo=mid
    return hi

def local_upper(d,j,qprev,qprevprev):
    return comb(d,j)*comb(d,j-2)*qprev*qprev//(comb(d,j-1)**2*qprevprev)

def h3(d,n,m,q3,q4):
    p1=n;p2=n*n-4*m
    p3=n**3-6*n*m+12*q3
    p4=n**4-8*n*n*m+8*m*m+16*n*q3-32*q4
    return d*(p2*p4-p3*p3)-p1*(p1*p4-p2*p3)+p2*(p1*p3-p2*p2)

def audit(n,m,d=14):
    q3min=lower_chord(d,3,m)
    q3max=local_upper(d,3,m,n)
    q4tan=comb(d,4)*m**3*d**2//(comb(d,2)**3*n**2)
    summary={'n':n,'m':m,'q3_interval':[q3min,q3max], 'q3_visited':0,'q3_feasible':0,'nonnegative_h3_candidates':[],'max_h3_at_lower':None}
    for q3 in range(q3min,q3max+1):
        summary['q3_visited']+=1
        q4min=lower_chord(d,4,q3)
        q4max=min(q4tan,local_upper(d,4,q3,m))
        if q4min>q4max:continue
        summary['q3_feasible']+=1
        assert d*(n*n-4*m)-n*n>0
        det=h3(d,n,m,q3,q4min)
        if summary['max_h3_at_lower'] is None or det>summary['max_h3_at_lower']:
            summary['max_h3_at_lower']=det
            summary['argmax']=[q3,q4min,q4max]
        if det>=0:summary['nonnegative_h3_candidates'].append([q3,q4min,q4max,det])
    return summary

if __name__=='__main__':
    cases=[(43,268),(44,273),(44,274),(45,279)]
    results=[audit(n,m) for n,m in cases]
    print(json.dumps(results,indent=2))
    with open('norm2_degree14_h3_20261016.json','w') as f:json.dump(results,f,indent=2)
    assert all(not x['nonnegative_h3_candidates'] for x in results)
