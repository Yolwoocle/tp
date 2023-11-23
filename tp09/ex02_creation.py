#!/usr/bin/env python3

# FONCTIONS DE BASE
def creer_liste_vide():
  return None

def creer_liste(t,q):
  return t,q

def tete(liste):
  assert liste!=None, 'Pré-condition (tete)'
  return liste[0]

def queue(liste):
  assert liste!=None, 'Pré-condition (queue)'
  return liste[1]

def est_vide(liste):
  return liste==None

# EXERCICE
def entiers_decroissants(n):
  if n == 0:
    return creer_liste_vide()
  return creer_liste(n, entiers_decroissants(n-1))

def test_entiers_decroissants():
  print('Test de la fonction entiers_decroissants')
  assert entiers_decroissants(0)==None
  assert entiers_decroissants(1)==(1,None)
  assert entiers_decroissants(5)==(5,(4,(3,(2,(1,None)))))
  print('  OK')

test_entiers_decroissants()
