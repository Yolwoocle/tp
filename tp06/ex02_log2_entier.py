#!/usr/bin/python3

def log2_entier(n):
  assert n>0, 'Pre-condition'
  k = 0
  assert k>=0 and 2**k<=n, 'Invariant (initialisation)'
  while n >= 2**(k+1):
    k += 1
    assert k>=0 and 2**k<=n, 'Invariant (itération)'
  assert k>=0 and 2**k<=n<2**(k+1), 'Post-condition'
  return k


def test_log2_entier():
  print('Test de la fonction log2_entier')
  for n in range(1,1000):
    k = log2_entier(n)
  print('  OK')

test_log2_entier()

