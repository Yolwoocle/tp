#!/usr/bin/python3

def indice_stricte_croissance(liste):
  n = len(liste)
  assert n>=2 and liste[0]<liste[n-1], 'Pre-condition'
  i = 1
  while i < n and liste[i-1] >= liste[i]:
    i+=1 
  assert 1<=i<n and liste[i-1]<liste[i], 'Post-condition'
  return i

def test_indice_stricte_croissance():
  print('Test de la fonction indice_stricte_croissance')
  assert indice_stricte_croissance([8,10])==1
  assert indice_stricte_croissance([1,10,9,8,7,6,5,4,3,2])==1
  assert indice_stricte_croissance([9,8,7,6,5,4,3,2,1,10])==9
  assert indice_stricte_croissance([9,1,8,2,7,3,6,4,5,10])in [2,4,6,8,9]
  print('  OK')

def indice_minimum_local(liste):
  n = len(liste)
  assert n>=3 and liste[0]>=liste[1] and liste[n-2]<=liste[n-1], 'Pre-condition'
  i = 1
  while i < n-1 and (liste[i-1] < liste[i] or liste[i] > liste[i+1]):
    i += 1
  assert 1<=i<n-1 and liste[i-1]>=liste[i] and liste[i]<=liste[i+1], 'Post-condition'
  return i

def test_indice_minimum_local():
  print('Test de la fonction indice_minimum_local')
  assert indice_minimum_local([8,7,10])==1
  assert indice_minimum_local([10,1,2,3,4,5,6,7,8,9])==1
  assert indice_minimum_local([9,8,7,6,5,4,3,2,1,10])==8
  assert indice_minimum_local([9,1,8,2,7,3,6,4,5,10]) in [1,3,5,7]
  print('  OK')

test_indice_stricte_croissance()
test_indice_minimum_local()

