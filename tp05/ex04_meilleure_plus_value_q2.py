#!/usr/bin/python3

import random
import time

def tableau_aleatoire(n):
  tab = [0]*n
  for i in range(n):
    tab[i] = random.randint(-n//2,n//2)
  return tab

def meilleure_plus_value_C(tab):
  assert len(tab)>0, 'Pré-condition'
  m = tab[0]
  plusval = 0
  for i in range(1, len(tab)):
    if tab[i] < m:
      m = tab[i]
    elif tab[i] - m > plusval:
      plusval = tab[i] - m
  return plusval

def test_meilleure_plus_value():
  print('Test de la fonction meilleure_plus_value_C')
  assert meilleure_plus_value_C([1])==0
  assert meilleure_plus_value_C([5,2])==0
  assert meilleure_plus_value_C([2,5])==3
  assert meilleure_plus_value_C([5,4,1,-1,-2,-3])==0
  assert meilleure_plus_value_C([4,5,1,-1,-2,-3])==1
  assert meilleure_plus_value_C([1,5,-1,-3,-2,4])==7
  # test de complexité
  meilleure_plus_value_C(tableau_aleatoire(100000))
  print('  OK')

test_meilleure_plus_value()


for i in range(1, 11):
  tic = time.time()
  
  meilleure_plus_value_C(tableau_aleatoire(10**i))
  tac = time.time()
  print(f"n = 10^{i} : {tac-tic}")

