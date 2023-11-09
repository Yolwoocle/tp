#!/usr/bin/python3

import random

def est_majorant(tab,m):
  for e in tab:
    if not e<=m:
      return False
  return True

def indice_maximum(tab):
  n = len(tab)
  assert n>0, 'Pre-condition'
  i,j = 0,n-1
  while i<j:
    v_debut = j - i
    assert v_debut >= 0, "Invariant (positif)"
    if tab[i]<=tab[j]:
      i += 1
    else:
      j -= 1
    v_fin = j - i
    assert v_fin < v_debut, "Invariant (décroissant)"
  assert 0<=i<n and est_majorant(tab,tab[i]), 'Post-condition'
  return i

def test_indice_maximum():
  print('Test de la fonction indice_maximum')
  assert indice_maximum([5])==0
  assert indice_maximum([5,2,7,3,1])==2
  assert indice_maximum([1,-2,-3])==0
  assert indice_maximum([6,7,8,0])==2
  assert indice_maximum([7,-8,9,-10,11])==4
  assert indice_maximum([3,5,2,10,19,17,2,11,3,14,3,14,20,5,17,20,2,8,4,19])==15
  for _ in range(1000):
    n = random.randint(1,100)
    tab = [random.randint(-1000,1000) for _ in range(n)]
    indice_maximum(tab)
  print('  OK')

test_indice_maximum()
