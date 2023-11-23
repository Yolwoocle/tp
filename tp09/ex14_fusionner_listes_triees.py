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
def fusionner_listes_triees(liste1,liste2):
  ...

def test_fusionner_listes_triees():
  print('Test de la fonction fusionner_listes_triees')
  assert fusionner_listes_triees(None,(3,(5,(6,None))))==(3,(5,(6,None)))
  assert fusionner_listes_triees((7,(9,(10,None))),None)==(7,(9,(10,None)))
  assert fusionner_listes_triees((1,(6,None)),(3,(8,None)))==(1,(3,(6,(8,None))))
  assert fusionner_listes_triees((1,(2,(4,(5,(7,(8,None)))))),(2,(3,(5,(6,(6,(8,None)))))))==(1,(2,(2,(3,(4,(5,(5,(6,(6,(7,(8,(8,None))))))))))))
  print('  OK')

test_fusionner_listes_triees()
