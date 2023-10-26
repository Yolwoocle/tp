#!/usr/bin/python3
import random
import time

def tableau_aleatoire(n):
  tab = [0]*n
  for i in range(n):
    tab[i] = random.randint(0,n)
  return tab

def deux_maxima(tab):
  assert len(tab)>=2, 'Pré-condition'
  # m2 < m1
  m1 = tab[0]
  m2 = tab[1]
  if m1 < m2:
    m1, m2 = m2, m1
  for i in range(2, len(tab)):
    if tab[i] > m1:
      m2 = m1
      m1 = tab[i]
    elif tab[i] > m2:
      m2 = tab[i]
  return (m1, m2)

def test_deux_maxima():
  print('Test de la fonction deux_maxima')
  assert deux_maxima([3,7])==(7,3)
  assert deux_maxima([8,2,4])==(8,4)
  assert deux_maxima([8,13,2,13,7,1])==(13,13)
  assert deux_maxima([9,6,12,11,9,3,17,1,19,0])==(19,17)
  assert deux_maxima([-9,-9,14,-18,5,-8,-9,11,10,-3])==(14,11)
  print('  OK')

def somme_maximale(tab):
  assert len(tab)>=2, 'Pré-condition'
  m1, m2 = deux_maxima(tab)
  return m1 + m2

def test_somme_maximale():
  print('Test de la fonction somme_maximale')
  assert somme_maximale([3,7])==10
  assert somme_maximale([8,2,4])==12
  assert somme_maximale([8,13,2,13,7,1])==26
  assert somme_maximale([9,6,12,11,9,3,17,1,19,0])==36
  assert somme_maximale([-9,-9,14,-18,5,-8,-9,11,10,-3])==25
  print('  OK')

test_deux_maxima()
test_somme_maximale()

for i in range(1, 11):
  tic = time.time()
  
  somme_maximale(tableau_aleatoire(10**i))
  tac = time.time()
  print(f"n = 10^{i} : {tac-tic}")
