"""Reconstruct the finite degree-12 frontier without rerunning completed degrees.
AI-generated research tooling, not an independently certified proof.
"""
from math import comb
from itertools import count
from pathlib import Path
import json
from explore import kk, rootfloor

def frontier(n):
    C=[comb(n,j) for j in range(n+1)]
    result={'degree':n,'indices':{}}
    for k in range(1,n):
        r=next(r for r in count(n) if comb(r,k+1)**k*C[k]**(k+1)>C[k+1]**k*comb(r+1,k)**(k+1))
        pairs=[];exceptions=[]
        for m in range(C[k],comb(r,k)):
            lower=kk(m,k)+1
            upper=rootfloor(C[k+1]**k*m**(k+1)//C[k]**(k+1),k)
            if lower<=upper:
                exceptions.append(m)
                pairs.extend((m,v) for v in range(lower,upper+1))
        bounds=[]
        if exceptions:
            for j in range(1,n+1):
                p,q=(n-j,n-k) if j<k else (j,k)
                bounds.append(rootfloor(C[j]**q*max(exceptions)**p//C[k]**p,q))
        result['indices'][k]={'cutoff':r,'exception_count':len(exceptions),'pair_count':len(pairs),'coefficient_caps':bounds,'pairs':pairs}
        print(n,k,r,len(exceptions),len(pairs),flush=True)
    result['pair_total']=sum(row['pair_count'] for row in result['indices'].values())
    (Path(__file__).parent/f'degree{n}_frontier.json').write_text(json.dumps(result,indent=2))
    print('TOTAL',n,result['pair_total'],flush=True)
    return result

if __name__=='__main__':
    assert frontier(11)['pair_total']==34948
    frontier(12)
