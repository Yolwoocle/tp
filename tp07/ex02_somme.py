import random

def somme(tab):
  s,i = 0,0
  while i<len(tab):
    v_debut = len(tab) - i
    assert v_debut>=0, 'Variant (positif)'
    s += tab[i]
    i += 1
    v_fin = len(tab) - i
    assert v_fin<v_debut, 'Variant (décroissant)'
  return s

def test_somme():
  print('Test de la fonction somme')
  assert somme([])==0
  assert somme([8])==8
  assert somme([9,7])==16
  assert somme([3,5,2,10,19,17,2,11,3,14,3,14,20,5,17,20,2,8,4,20])==199
  for _ in range(1000):
    n = random.randint(1,100)
    tab = [random.randint(-1000,1000) for _ in range(n)]
    assert somme(tab) == sum(tab)
  print('  OK')

test_somme()
