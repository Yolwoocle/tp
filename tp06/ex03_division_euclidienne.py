def division_euclidienne(a,b):
  assert a >= 0 and b > 0, "Pré-condition"
  q = 0
  r = a
  assert b*q + r == a, "Invariant (initialisation)"
  while r>=b:
    q += 1
    r -= b
    assert b*q + r == a, "Invariant (itération)"
  assert b*q + r == a and b > r, "Post-condition"
  return q,r

def test_division_euclidienne():
  print('Test de la fonction division_euclidienne')
  assert division_euclidienne(43,10)==(4,3)
  assert division_euclidienne(0,10)==(0,0)
  assert division_euclidienne(10,5)==(2,0)
  assert division_euclidienne(5,36)==(0,5)
  assert division_euclidienne(125,4)==(31,1)
  print('  OK')

test_division_euclidienne()
