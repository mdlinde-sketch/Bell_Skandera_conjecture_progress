"""Independent direct 3x3 moment determinant audit of u_d=2 special cases.
No C++ inputs: use the independently generated Python frontier case lists.
The possible u_d=3 branch is eliminated by certified_inverse_trace.py.
"""
from math import comb
from itertools import permutations
import json,sys


def integer_chord_min(d,j,previous):
    power=d-j+1
    numerator=previous**(power-1)*comb(d,j)**power
    denominator=comb(d,j-1)**(power-1)
    lo,hi=0,1
    while hi**power*denominator<numerator:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**power*denominator>=numerator:hi=mid
        else:lo=mid
    return hi


def local_max(d,j,previous,previous_previous):
    return comb(d,j)*comb(d,j-2)*previous**2//(comb(d,j-1)**2*previous_previous)


def det3(matrix):
    ans=0
    for perm in permutations(range(3)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        ans+=sign*matrix[0][perm[0]]*matrix[1][perm[1]]*matrix[2][perm[2]]
    return ans


def direct_H3(d,n,m,a3,a4):
    # u_d=2, roots of the reversed polynomial scaled by 2.
    # Their elementary symmetric functions are n,2m,4a3,8a4.
    e=[1,n,2*m,4*a3,8*a4]
    p=[d]
    for j in range(1,5):
        p.append(sum((-1)**(i-1)*e[i]*p[j-i] for i in range(1,j))
                 +(-1)**(j-1)*j*e[j])
    return det3([[p[i+j] for j in range(3)] for i in range(3)])


def audit_cases(path):
    data=json.load(open(path));d=data['degree']
    output=[]
    for k,m,n,ud,um in data['suspect']:
        assert k==d-2 and ud==3,(d,k,m,n,ud)
        # For u_d=3: u_(d-1)/3 + (3/2)log 3 < (29/20)d,
        # since log 3<2 and u_(d-1)<=um; this forces factor (1+t).
        assert 20*um+180<87*d,(d,k,m,n,um)
        q3min=integer_chord_min(d,3,m)
        q3max=local_max(d,3,m,n)
        tangent4=comb(d,4)*m**3*d**2//(comb(d,2)**3*n**2)
        max_det=None
        feasible=0
        for a3 in range(q3min,q3max+1):
            q4min=integer_chord_min(d,4,a3)
            q4max=min(local_max(d,4,a3,m),tangent4)
            if q4min>q4max:continue
            # H3 is decreasing in q4 because its slope is -32 H2,
            # and H2=d(n^2-4m)-n^2>0.
            assert d*(n*n-4*m)-n*n>0
            value=direct_H3(d,n,m,a3,q4min)
            assert value<0,(d,k,m,n,a3,q4min,value)
            max_det=value if max_det is None else max(max_det,value)
            feasible+=1
        assert feasible>0
        output.append((k,m,n,feasible,max_det))
    print('PASS degree',d,'special cases',len(output),'max H3',max((x[-1] for x in output),default=None))
    return output

if __name__=='__main__':
    for path in sys.argv[1:]:audit_cases(path)
