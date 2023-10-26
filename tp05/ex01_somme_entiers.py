#!/usr/bin/python3

import time

def somme_entiers_1(n):
  somme = 0
  for i in range(1,n+1):
    somme += i
  return somme

def somme_entiers_2(n):
  somme = n*(n+1)//2
  return somme

for k in range(13):
  n = 10**k
  tic = time.time()
  somme_entiers_2(n)
  tac = time.time()
  print('n=10^',k,' : ',tac-tic,' sec',sep='')

