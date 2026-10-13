"""Resumable degree-12 branch search with exact affine moment bounds.
Usage: python degree12_search.py INDEX SECONDS
Only fully exhausted pairs are checkpointed. Timed-out pairs are retried.
This is new AI-generated code, not the recovered degree-11 certificate.
"""
import json,sys,time
from pathlib import Path
from math import comb
from explore import moments,det

BASE=Path(__file__).parent;N=12;C=[comb(N,j) for j in range(N+1)]
def affine_bound(u,j):
    # Unshifted even moments; shifted odd moments (roots are positive).
    shift=j%2;q=(j-shift)//2+1
    vals=[]
    for x in (0,1):
        v=u[:j]+[x]+[0]*(N-j)
        p=moments(v,j)
        vals.append(det([[p[a+b+shift] for b in range(q)] for a in range(q)]))
    return vals[0],vals[1]-vals[0]

def main(k,seconds):
    info=json.loads((BASE/'degree12_frontier.json').read_text())['indices'][str(k)]
    pairs=info['pairs'];caps=[1]+info['coefficient_caps']
    path=BASE/f'degree12_k{k}_checkpoint.json'
    state=json.loads(path.read_text()) if path.exists() else {'degree':12,'index':k,'completed_pairs':0,'survivors':[],'nodes':0,'method':'Newton plus unshifted and shifted leading moment determinants; unreviewed'}
    start=time.monotonic();deadline=start+seconds;nodes=0
    order=list(range(k-1,0,-1))+list(range(k+2,N+1))
    def visit(u,pos):
        nonlocal nodes
        nodes+=1
        if nodes%1024==0 and time.monotonic()>deadline:raise TimeoutError
        if pos==len(order):
            state['survivors'].append(u[:]);return
        j=order[pos];lower=C[j];upper=caps[j]
        if j<k:upper=min(upper,C[j]*C[j+2]*u[j+1]**2//(C[j+1]**2*u[j+2]))
        else:upper=min(upper,C[j-2]*C[j]*u[j-1]**2//(C[j-1]**2*u[j-2]))
        if all(x is not None for x in u[:j]):
            b,a=affine_bound(u,j)
            if a>0:lower=max(lower,-(b//a))
            elif a<0:upper=min(upper,b//(-a))
            elif b<0:return
        for v in range(lower,upper+1):
            u[j]=v
            if any(u[t-1] is not None and u[t] is not None and u[t+1] is not None and C[t-1]*C[t+1]*u[t]**2<C[t]**2*u[t-1]*u[t+1] for t in range(1,N)):continue
            # When filling the left side makes the fixed pair part of a known
            # prefix, also check the determinants at those fixed coefficients.
            if j==1:
                bad=False
                for t in range(2,k+2):
                    b,a=affine_bound(u,t)
                    if b+a*u[t]<0:bad=True;break
                if bad:continue
            visit(u,pos+1)
        u[j]=None
    try:
        for index in range(state['completed_pairs'],len(pairs)):
            u=[None]*(N+1);u[0]=1;u[k],u[k+1]=pairs[index]
            visit(u,0)
            state['completed_pairs']=index+1
            state['nodes']+=nodes;nodes=0
            path.write_text(json.dumps(state,indent=2))
            if (index+1)%25==0:print('Completed',index+1,'of',len(pairs),'survivors',len(state['survivors']),flush=True)
            if time.monotonic()>deadline:break
    except TimeoutError:pass
    state['total_pairs']=len(pairs)
    state['complete']=state['completed_pairs']==len(pairs)
    path.write_text(json.dumps(state,indent=2))
    print('Checkpoint',state['completed_pairs'],'/',len(pairs),'survivors',len(state['survivors']),'complete',state['complete'],flush=True)

if __name__=='__main__':main(int(sys.argv[1]),float(sys.argv[2]))
