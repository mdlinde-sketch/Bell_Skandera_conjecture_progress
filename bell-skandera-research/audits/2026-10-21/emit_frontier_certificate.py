"""Emit untrusted gzip interval-cover witness for d17.
Records [k,a,b,kind]: 0 impossible, 1 Smyth trace, 2 explicit singleton.
Independent checker must validate all mathematics; this is not a verifier.
"""
import gzip,json
from math import comb
from independent_python_frontier_degree17 import kk_next,max_n,max_coeff,cutoff

def emit(d=17,path='frontier_cover_d17.jsonl.gz'):
    counts=[0,0,0]
    with gzip.open(path,'wt',compresslevel=9) as out:
        for k in range(1,d):
            stack=[(comb(d,k),comb(cutoff(d,k),k)-1)]
            while stack:
                a,b=stack.pop()
                lo=kk_next(k,a)+1;hi=max_n(d,k,b)
                if lo>hi:kind=0
                elif 10000*max_coeff(d,k,b,lo,1)<=17719*d:kind=1
                elif a==b:kind=2
                else:
                    mid=(a+b)//2
                    stack.extend([(mid+1,b),(a,mid)])
                    continue
                counts[kind]+=1
                out.write(json.dumps([k,a,b,kind],separators=(',',':'))+'\n')
    print('Emitted',counts,'total leaves',sum(counts),path,flush=True)

if __name__=='__main__':emit()
