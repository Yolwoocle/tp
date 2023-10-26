#!/usr/bin/python3

import random
import time

def tableau_aleatoire(n):
  tab = [0]*n
  for i in range(n):
    tab[i] = random.randint(-n//2,n//2)
  return tab

def meilleure_plus_value_A(tab):
  n = len(tab)
  assert n>0, 'Pré-condition'
  difference_max = 0
  for i in range(n):
    for j in range(n):
      if (tab[j]-tab[i])>difference_max and i<=j:
        difference_max = tab[j]-tab[i]
  return difference_max

def meilleure_plus_value_B(tab):
  n = len(tab)
  assert n>0, 'Pré-condition'
  difference_max = 0
  for i in range(n):
    for j in range(i+1,n):
      if (tab[j]-tab[i])>difference_max:
        difference_max = tab[j]-tab[i]
  return difference_max


for i in range(1, 11):
  tic = time.time()
  
  meilleure_plus_value_A(tableau_aleatoire(10**i))
  tac = time.time()
  print(f"n = 10^{i} : {tac-tic}")