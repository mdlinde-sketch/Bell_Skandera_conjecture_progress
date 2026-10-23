"""Independent exhaustive 3x3 Hankel norm-two audit, degrees 14-17.
Tests every admissible integer (q3,q4); no monotonic pruning shortcut.
"""
import json,sys
from math import comb

def ceil_root_quotient(num,den,exp):
    lo,hi=0,1
    while den*hi**exp<num:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if den*mid**exp>=num:hi=mid
        else:lo=mid
    return hi

def chord(d,j,previous):
    exp=d-j+1
    return ceil_root_quotient(previous**(exp-1)*comb(d,j)**exp,
                              comb(d,j-1)**(exp-1),exp)

def local(d,j,a,b):
    return comb(d,j)*comb(d,j-2)*a*a//(comb(d,j-1)**2*b)

def det3(d,e1,e2,e3,e4):
    p0=d;p1=e1;p2=e1*p1-2*e2
    p3=e1*p2-e2*p1+3*e3
    p4=e1*p3-e2*p2+e3*p1-4*e4
    return p0*(p2*p4-p3*p3)-p1*(p1*p4-p2*p3)+p2*(p1*p3-p2*p2)

def audit(path):
    obj=json.load(open(path));d=obj['degree']
    cases=obj['suspect']
    tested=0;worst=None;per=[]
    for k,m,n,ud,um in cases:
        assert k==d-2 and ud>=2
        lo3=chord(d,3,m);hi3=local(d,3,m,n)
        t4=comb(d,4)*m**3*d**2//(comb(d,2)**3*n**2)
        count=0;local_max=None
        for a3 in range(lo3,hi3+1):
            lo4=chord(d,4,a3)
            hi4=min(local(d,4,a3,m),t4)
            for a4 in range(lo4,hi4+1):
                H=det3(d,n,2*m,4*a3,8*a4)
                if H>=0:raise AssertionError((d,k,m,n,a3,a4,H))
                count+=1
                local_max=H if local_max is None else max(local_max,H)
        assert count>0
        tested+=count
        worst=local_max if worst is None else max(worst,local_max)
        per.append([k,m,n,count,local_max])
    print('PASS',d,'special cases',len(cases),
          'explicit (q3,q4) checks',tested,'largest H3',worst,flush=True)
    return {'degree':d,'cases':len(cases),'pairs_checked':tested,
            'max_H3':worst,'per_case':per}

if __name__=='__main__':
    for path in sys.argv[1:]:
        result=audit(path)
        with open('norm2_full_grid_degree%d_20261020.json'%result['degree'],'w') as f:
            json.dump(result,f,indent=2)
