#!/usr/bin/python3
import math

def racine_entiere(n):
  assert n>=0, 'Pre-condition'
  
  a = 0
  while (n >= (a+1)**2):
    a += 1

  assert a>=0 and a**2<=n<(a+1)**2, f'Post-condition n={n} a={a} {a**2} {n} {(a+1)**2}'
  return a

def test_racine_entiere():
  print('Test de la fonction racine_entiere')
  for n in range(1000):
    a = racine_entiere(n)
    # print(a, math.sqrt(n))
  print('  OK')

def log2_entier(n):
  assert n>0, 'Pre-condition'
  k = 0
  while n >= 2**(k+1):
    k += 1
  assert k>=0 and 2**k<=n<2**(k+1), 'Post-condition'
  return k

def test_log2_entier():
  print('Test de la fonction log2_entier')
  for n in range(1,1000):
    k = log2_entier(n)
  print('  OK')

def logb_entier(n,b):
  assert n>0 and b>=2, 'Pre-condition'
  k = 0
  while n >= b**(k+1):
    k += 1
  assert k>=0 and b**k<=n<b**(k+1), 'Post-condition'
  return k

def test_logb_entier():
  print('Test de la fonction logb_entier')
  for n in range(1,100):
    for b in range(2,11):
      k = logb_entier(n,b)
  print('  OK')

test_racine_entiere()
test_log2_entier()
test_logb_entier()

