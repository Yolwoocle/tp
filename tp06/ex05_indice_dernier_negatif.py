#!/usr/bin/python3

import random

def est_croissant(tab):
  assert True, "Pré-condition"
  for i in range(len(tab)-1):
    if tab[i] > tab[i+1]:
      return False
  return True

def test_est_croissant():
  print('Test de la fonction est_croissant')
  assert est_croissant([])==True
  assert est_croissant([3])==True
  assert est_croissant([3,3])==True
  assert est_croissant([3,5])==True
  assert est_croissant([5,3])==False
  assert est_croissant([-5,-3,-3,0,1,2,2,4])==True
  assert est_croissant([-5,-3,-3,0,1,2,2,1])==False
  assert est_croissant([-2,-3,-3,0,1,2,2,4])==False
  assert est_croissant([-5,-3,-3,0,-1,2,2,4])==False
  print('  OK')

def indice_dernier_negatif_1(tab):
  n = len(tab)
  i = 0
  # assert tab[0] <= 0 and tab[n-1] > 0, "Pré-condition"
  assert 0<=i<n-1 and tab[i]<=0, "Invariant"
  while tab[i+1] <= 0:
    i += 1
    assert 0<=i<n-1 and tab[i]<=0, "Invariant"
  assert 0<=i<n-1 and tab[i]<=0<tab[i+1], 'Post-condition'
  return i
  

def indice_dernier_negatif_2(tab):
  n = len(tab)
  i = 0
  j = n-1
  # assert 0<=i<j<n and tab[i]<=0<tab[j], "Invariant (initialistion)"
  while i < j-1:
    m = (i + j) // 2
    if tab[m] <= 0:
      i = m
    else:
      j = m
    assert 0<=i<j<n and tab[i]<=0<tab[j], "Invariant (boucle)"
  assert 0<=i<n-1 
  assert tab[i]<=0<tab[i+1], 'Post-condition'
  return i

def test_indice_dernier_negatif(version):
  print('Test de la fonction indice_dernier_negatif (version {})'.format(version))
  indice_dernier_negatif = {
    1: indice_dernier_negatif_1,
    2: indice_dernier_negatif_2
  }[version]
  assert indice_dernier_negatif([-1,1])==0
  assert indice_dernier_negatif([0,1])==0
  assert indice_dernier_negatif([0,0,1])==1
  assert indice_dernier_negatif([-4,0,1])==1
  assert indice_dernier_negatif([-4,-3,-2,0,1,1,1])==3
  assert indice_dernier_negatif([-4,-3,-2,-2,-2,1,1,1])==4
  assert indice_dernier_negatif([-4,-3,-2,-1,-1,-1,1])==5
  print('  OK')

li = [-7,-5,-2,4,-1,7,6,-2,9,15]
for i in range(10000):
  # li = [random.randint(-100, 0)] + [random.randint(-100, 100) for _ in range(random.randint(0, 10))] + [random.randint(0, 10)]
  li = [-10, 0]
  print(li)
  print(indice_dernier_negatif_2(li))

# 4.a) Chacune des deux fonctions renvoie-t-elle un indice qui satisfait la
# post-condition? Si oui, sont-ils les mêmes? Expliquer.
# 
# non, elles renvoient 2 et 4
# pour la 1 c'est parce qu'on a ...-2 (i=2), 4 (i=3), -1,... et avec une recherche linéaire ça tombe 
# en premier sur ça
# 
# pour la 2 c'est parce qu'on a :
# i=0, j=9, m=4 -> ...-1, 7... 
# Donc on a 4
# 
# 4.b) 
# Pour la 1, non, car vu que tab[0] < tab[n-1] on aura forcément un i tel que 
# tab[i] <= 0 < tab[i]
# Pour la 2, oui [-10, 0]

# test_est_croissant()
# test_indice_dernier_negatif(1)
# test_indice_dernier_negatif(2)

