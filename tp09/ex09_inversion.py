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
def inverser_rec(liste,liste_inverse):
  ...

def test_inverser_rec():
  print('Test de la fonction inverser_rec')
  assert inverser_rec(None,None)==None
  assert inverser_rec(None,(6,None))==(6,None)
  assert inverser_rec((6,None),None)==(6,None)
  assert inverser_rec(None,(5,(4,(3,None))))==(5,(4,(3,None)))
  assert inverser_rec((5,None),(4,(3,None)))==(5,(4,(3,None)))
  assert inverser_rec((4,(5,None)),(3,None))==(5,(4,(3,None)))
  assert inverser_rec((3,(4,(5,None))),None)==(5,(4,(3,None)))
  print('  OK')

def inverser(liste):
  ...

def test_inverser():
  print('Test de la fonction inverser')
  assert inverser(None)==None
  assert inverser((6,None))==(6,None)
  assert inverser((3,(4,(5,None))))==(5,(4,(3,None)))
  print('  OK')

test_inverser_rec()
test_inverser()
