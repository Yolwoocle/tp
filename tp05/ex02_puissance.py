#!/usr/bin/python3

import time

def puissance_A(a,n):
  r = 1.0
  p = n
  while p>0:
    r = r*a
    p = p-1
  return r

def puissance_B(a,n):
  r = 1.0
  x = a
  p = n
  while p>0:
    if p%2==1:
      r = r*x
    p = p//2
    x = x*x
  return r

a = 3.141592

for i in range(13):
  n = 10**i
  tic = time.time()
  puissance_A(a, n)
  tac = time.time()
  print(f"n=10^{i} : {tac-tic} sec")

