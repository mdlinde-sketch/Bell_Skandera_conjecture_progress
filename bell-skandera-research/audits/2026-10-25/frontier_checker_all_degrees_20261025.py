"""Small independent exact certificate checker, degrees 2 through 17.
Input is an UNTRUSTED interval partition. Validates disjoint full m coverage,
KK shadow, Newton bounds, and every explicitly classified adjacent pair.
"""
import gzip,hashlib,json,sys
from math import comb

D=int(sys.argv[2])
TRACE=17719

def kk_shadow(k,m):
    cap=None;total=0
    for j in range(k,0,-1):
        low=j-1
        high=2*j+1 if cap is None else cap
        if cap is None:
            while comb(high,j)<=m:high*=2
        while low+1<high:
            mid=(low+high)//2
            if comb(mid,j)<=m:low=mid
            else:high=mid
        if low>=j:
            total+=comb(low,j+1)
            m-=comb(low,j)
        cap=low
    if m:raise AssertionError(('KK remainder',k,m))
    return total

def root_floor_ratio(num,den,degree):
    lo=0;hi=1
    while den*hi**degree<=num:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if den*mid**degree<=num:lo=mid
        else:hi=mid
    return lo

def upper_n(d,k,m):
    return root_floor_ratio(comb(d,k+1)**k*m**(k+1),comb(d,k)**(k+1),k)

def coeff_cap(d,k,m,n,j):
    if j==k:return m
    if j==k+1:return n
    if j<k:
        return (comb(d,j)*m**(k+1-j)*comb(d,k+1)**(k-j)//
                (comb(d,k)**(k+1-j)*n**(k-j)))
    return (comb(d,j)*n**(j-k)*comb(d,k)**(j-k-1)//
            (comb(d,k+1)**(j-k)*m**(j-k-1)))

def cutoff(d,k):
    r=d
    while comb(r,k+1)**k*comb(d,k)**(k+1)<=comb(d,k+1)**k*comb(r+1,k)**(k+1):r+=1
    return r

def check(path):
    buckets={k:[] for k in range(1,D)}
    with gzip.open(path,'rt') as inp:
        for line in inp:
            k,a,b,kind=json.loads(line)
            assert 1<=k<D and a<=b and kind in (0,1,2)
            buckets[k].append((a,b,kind))
    residual=[];special=[];blocks=[0,0,0];nchecks=0
    for k in range(1,D):
        expected=comb(D,k)
        stop=comb(cutoff(D,k),k)
        for a,b,kind in sorted(buckets[k]):
            assert a==expected,(k,'gap/overlap',a,expected)
            expected=b+1;blocks[kind]+=1
            low_n=kk_shadow(k,a)+1
            high_n=upper_n(D,k,b)
            if kind==0:
                assert low_n>high_n,(k,a,b,'bad no-pair')
            elif kind==1:
                assert low_n<=high_n
                assert TRACE*D>=10000*coeff_cap(D,k,b,low_n,1),(k,a,b,'bad trace')
            else:
                assert a==b and low_n<=high_n
                for n in range(low_n,high_n+1):
                    nchecks+=1
                    if 10000*coeff_cap(D,k,a,n,1)<=TRACE*D:continue
                    norm_cap=coeff_cap(D,k,a,n,D)
                    if norm_cap<1:continue
                    inv_cap=coeff_cap(D,k,a,n,D-1)
                    row=[k,a,n,norm_cap,inv_cap]
                    if norm_cap>=3:
                        special.append(row)
                    else:
                        if 10000*inv_cap>TRACE*D:residual.append(row)
                        if norm_cap>=2 and 10*inv_cap+30>=29*D:special.append(row)
        assert expected==stop,(k,'bad final cover',expected,stop)
    digests={}
    for name,rows in [('residual',residual),('suspect',special)]:
        canonical=json.dumps(sorted(rows),separators=(',',':')).encode()
        digests[name]=hashlib.sha256(canonical).hexdigest()
    assert 2<=D<=17
    expected_lists=json.load(open(f'regenerated_frontier_d{D}_20261025.json'))
    assert sorted(residual)==sorted(expected_lists['residual'])
    assert sorted(special)==sorted(expected_lists['suspect'])
    result=dict(degree=D,leaves=sum(blocks),no_pair=blocks[0],trace=blocks[1],
                singleton=blocks[2],explicit_n=nchecks,residual=len(residual),
                special=len(special),digests=digests)
    with open(f'frontier_checked_d{D}_20261025.json','w') as out:
        json.dump({'degree':D,'residual':residual,'suspect':special},out,separators=(',',':'))
    print('PASS',json.dumps(result,sort_keys=True),flush=True)
    return result

if __name__=='__main__':check(sys.argv[1])
