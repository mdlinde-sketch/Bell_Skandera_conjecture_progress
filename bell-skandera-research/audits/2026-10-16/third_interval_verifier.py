"""Independent exact interval certificate, degrees 14-16.

Reads a separately generated finite adjacent-pair list. Rebuilds every admissible
coefficient prefix using built-in Python integers. Evaluates the 4x4 Hankel
determinant by the Leibniz formula, independently of the C++ Schur formula.
Does not independently prove that the input residual list is complete.
"""
import itertools
import json
import sys
from math import comb

def determinant4(M):
    answer=0
    for order in itertools.permutations(range(4)):
        swaps=sum(order[i]>order[j] for i in range(4) for j in range(i+1,4))
        term=1
        for i in range(4):
            term*=M[i][order[i]]
        answer+=(-1 if swaps%2 else 1)*term
    return answer

def chord_lower(d,j,previous):
    a=d-j+1
    num=previous**(a-1)*comb(d,j)**a
    den=comb(d,j-1)**(a-1)
    hi=1
    while den*hi**a<num:hi*=2
    lo=hi//2
    while lo+1<hi:
        middle=(lo+hi)//2
        if den*middle**a>=num:hi=middle
        else:lo=middle
    return hi

def newton_upper(d,j,previous,previous2):
    return comb(d,j)*comb(d,j-2)*previous**2//(comb(d,j-1)**2*previous2)

def tangent_upper(d,j,q1,q2):
    return comb(d,j)*q2**(j-1)*d**(j-2)//(comb(d,2)**(j-1)*q1**(j-2))

def power_sums(d,coeffs):
    ps=[d]
    for j in range(1,7):
        ps.append(sum((-1)**(i-1)*coeffs[i]*ps[j-i] for i in range(1,j))
                  +(-1)**(j-1)*j*coeffs[j])
    return ps

def H3(d,a,b,c,e):
    p=power_sums(d,[1,a,b,c,e,0,0])
    A,B,C,D,E=p[:5]
    return A*(C*E-D*D)-B*(B*E-C*D)+C*(B*D-C*C)

def H4(d,a,b,c,e,f,g):
    p=power_sums(d,[1,a,b,c,e,f,g])
    return determinant4([[p[i+j] for j in range(4)] for i in range(4)])

def max_quadratic(f0,f1,f2,length):
    second=f2-2*f1+f0
    assert second%2==0
    A=second//2
    B=f1-f0-A
    def evaluate(t):return f0+B*t+A*t*t
    candidates=[0,length]
    if A<0 and B>0:
        vertex=min(length,B//(-2*A))
        candidates.extend((vertex,min(length,vertex+1)))
    return max(evaluate(t) for t in candidates),A

def audit(path):
    data=json.load(open(path));d=data["degree"]
    records=data["residual"]+data["suspect"]
    stats={"cases":0,"prefixes":0,"depth3":0,"valid_depth4":0,
           "intervals":0,"excluded_q5_values":0,"uncleared":0}
    for k,m,n,ud,um in records:
        stats["cases"]+=1
        assert k in (d-2,d-3,d-4)
        q1choices=[n] if k==d-2 else range(17719*d//10000+1,um+1)
        for q1 in q1choices:
            if k==d-4:
                u2_upper=(comb(d,k+2)*n*n*comb(d,k)
                          // (comb(d,k+1)**2*m))
                q2choices=range(chord_lower(d,2,q1),
                                min(newton_upper(d,2,q1,1),u2_upper)+1)
            else:q2choices=[m if k==d-2 else n]
            for q2 in q2choices:
                if (d-1)*q1*q1<2*d*q2:continue
                if not chord_lower(d,2,q1)<=q2<=newton_upper(d,2,q1,1):continue
                stats["prefixes"]+=1
                tangent={j:tangent_upper(d,j,q1,q2) for j in range(3,7)}
                lo3=chord_lower(d,3,q2)
                hi3=min(tangent[3],newton_upper(d,3,q2,q1))
                if k in (d-3,d-4):
                    required=m if k==d-3 else n
                    lo3=max(lo3,required);hi3=min(hi3,required)
                for q3 in range(lo3,hi3+1):
                    stats["depth3"]+=1
                    lo4=chord_lower(d,4,q3)
                    hi4=min(tangent[4],newton_upper(d,4,q3,q2))
                    if k==d-4:
                        lo4=max(lo4,m);hi4=min(hi4,m)
                    for q4 in range(lo4,hi4+1):
                        if H3(d,q1,q2,q3,q4)<0:break
                        stats["valid_depth4"]+=1
                        lo5=chord_lower(d,5,q4)
                        hi5=min(tangent[5],newton_upper(d,5,q4,q3))
                        if lo5>hi5:continue
                        low6=chord_lower(d,6,lo5)
                        vals=[H4(d,q1,q2,q3,q4,lo5+t,low6)
                              for t in (0,1,2)]
                        upper,A=max_quadratic(*vals,hi5-lo5)
                        H2=d*(q1*q1-2*q2)-q1*q1
                        assert H2>=0 and A==-25*H2
                        stats["intervals"]+=1
                        if upper>=0:
                            stats["uncleared"]+=1
                            raise AssertionError(
                                f"Uncleared interval: {d,k,m,n,q1,q2,q3,q4,lo5,hi5}")
                        stats["excluded_q5_values"]+=hi5-lo5+1
    print("PASS",d,stats,flush=True)
    return stats

if __name__=="__main__":
    for path in sys.argv[1:]:audit(path)
