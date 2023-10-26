#!/usr/bin/python3

import random

def generer_collier_aleatoire(m0,m1):
  collier = [0]*(2*m0)+[1]*(2*m1)
  random.shuffle(collier)
  return collier

def somme(collier,g,d):
  s = 0
  for i in range(g,d):
    s += collier[i]
  return s

def est_collier_valide(collier):
  n0 = 0
  n1 = 0
  for perle in collier:
    if perle == 0:
      n0 += 1
    elif perle == 1:
      n1 += 1
    else: 
      return False
  return n0%2 == 0 and n1%2 == 0

def test_est_collier_valide():
  print('Test de la fonction est_collier_valide')
  assert est_collier_valide([])==True
  assert est_collier_valide([0,0])==True
  assert est_collier_valide([1,1])==True
  assert est_collier_valide([0,1])==False
  assert est_collier_valide([2,0])==False
  assert est_collier_valide([1,1,0])==False
  assert est_collier_valide([1,0,0,1])==True
  assert est_collier_valide([2,0,0,2])==False
  assert est_collier_valide([0,0,0,2])==False
  assert est_collier_valide([0,1,1,0,0])==False
  assert est_collier_valide([1,0,0,1,0,0])==True
  assert est_collier_valide([1,0,0,1,1,0,1,0])==True
  assert est_collier_valide([0,0,0,0,1,1,1,1])==True
  assert est_collier_valide([0,1,1,0,1,1,1,1])==True
  assert est_collier_valide([0,0,0,0,0,0,0,0])==True
  assert est_collier_valide([1,0,0,1,0,0,1,0])==False
  assert est_collier_valide([1,1,0,1,1,1,1,1])==False
  print('  OK')

def partager_collier(collier):
  n = len(collier)
  s1 = somme(collier,0,n)
  assert est_collier_valide(collier), 'Pre-condition'
  
  n1 = sum(collier)
  n0 = n - n1
  i = 0
  while i <= n//2 and somme(collier, i, i+n//2) != n1//2:
    i += 1
    
  assert 0<=i<=n//2 and somme(collier,i,i+n//2)==s1//2, 'Post-condition'
  return i

def test_partager_collier():
  print('Test de la fonction partager_collier')
  assert partager_collier([])==0
  assert partager_collier([1,1]) in [0,1]
  assert partager_collier([1,0,1,0]) in [0,1]
  assert partager_collier([1,1,0,0])==1
  for _ in range(100):
    m0 = random.randint(0,100)
    m1 = random.randint(0,100)
    collier = generer_collier_aleatoire(m0,m1)
    partager_collier(collier)
  print('  OK')
  
test_est_collier_valide()
test_partager_collier()