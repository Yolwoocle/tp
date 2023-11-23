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
def multiplier(liste,facteur):
  if est_vide(liste):
    return creer_liste_vide()
  return creer_liste(tete(liste) * facteur, multiplier(queue(liste), facteur))

def test_multiplier():
  print('Test de la fonction multiplier')
  assert multiplier(None,7)==None
  assert multiplier((2,None),-4)==(-8,None)
  assert multiplier((2,(3,(4,(1,None)))),2)==(4,(6,(8,(2,None))))
  print('  OK')

test_multiplier()
