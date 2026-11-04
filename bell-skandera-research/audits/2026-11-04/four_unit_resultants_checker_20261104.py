#!/usr/bin/env python3
from math import comb
import json
def primes(n):
 s=bytearray(b'\x01')*n
 s[:2]=b'\x00\x00'
 for k in range(2,int(n**.5)+1):
  if s[k]: s[k*k:n:k]=b'\x00'*len(s[k*k:n:k])
 return [i for i in range(5,n) if s[i]]
def evalpoly(a,x):
 v=0
 for c in a:v=v*x+c
 return v
ps=primes(1000)
for p in ps:
 d=(p-1)//2
 a=[(-1)**j*comb(2*d-j,j) for j in range(d+1)]
 vals=[evalpoly(a,x) for x in range(5)]
 assert all(abs(v)==1 for v in vals[:4]),(p,vals)
 assert vals[4]==p,(p,vals)
print(json.dumps({'status':'PASS','prime_count':len(ps),'largest_prime':max(ps),'unit_points':[0,1,2,3],'P4':'p'}))
