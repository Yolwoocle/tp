#!/usr/bin/python3

import random

def somme_distances(liste,v):
  s = 0
  for e in liste:
    s += abs(e-v)
  return s

def minimiser_somme_distance(liste):
  n = len(liste)
  assert n>0, 'Pre-condition'
  
  v = min(liste)
  while v <= max(liste) and (somme_distances(liste, v) > somme_distances(liste, v-1) or somme_distances(liste, v) > somme_distances(liste, v+1)):
    v += 1
  
  assert (
    somme_distances(liste,v)<=somme_distances(liste,v-1) 
    and somme_distances(liste,v)<=somme_distances(liste,v+1)
  ), 'Post-condition'
  return v

def test_minimiser_somme_distance():
  print('Test de la fonction minimiser_somme_distance')
  assert minimiser_somme_distance([8])==8
  assert minimiser_somme_distance([7,9]) in [7,8,9]
  for _ in range(100):
    liste = [random.randint(-100,100) for _ in range(random.randint(1,100))]
    v = minimiser_somme_distance(liste)
  print('  OK')

test_minimiser_somme_distance()

