import math

def factorielle(n):
  assert n>=0, 'Pré-condition'
  k = 0
  f = 1
  assert f==math.factorial(k), 'Invariant (initialisation)'
  while k<n:
    k += 1
    f *= k
    assert f==math.factorial(k), 'Invariant (itération)'
  assert f==math.factorial(n), 'Post-condition'
  return f


def test_factorielle():
  print('Test de la fonction factorielle')
  for n in range(100):
    assert factorielle(n)==math.factorial(n)
  print('  OK')

test_factorielle()