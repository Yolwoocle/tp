def somme_carres(n):
  if n == 0:
    return 0
  return n*n + somme_carres(n-1)

def test_somme_carres():
  print('Test de la fonction somme_carres')
  assert somme_carres(0)==0
  assert somme_carres(1)==1
  assert somme_carres(2)==5
  assert somme_carres(10)==385
  assert somme_carres(100)==338350
  print('  OK')

test_somme_carres()
