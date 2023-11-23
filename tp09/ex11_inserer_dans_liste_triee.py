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
def inserer_dans_liste_triee(liste,valeur):
  ...

def test_inserer_dans_liste_triee():
  print('Test de la fonction inserer_dans_liste_triee')
  assert inserer_dans_liste_triee(None,6)==(6,None)
  assert inserer_dans_liste_triee((6,None),3)==(3,(6,None))
  assert inserer_dans_liste_triee((3,(6,None)),4)==(3,(4,(6,None)))
  assert inserer_dans_liste_triee((3,(4,(6,None))),7)==(3,(4,(6,(7,None))))
  assert inserer_dans_liste_triee((3,(4,(6,(7,None)))),1)==(1,(3,(4,(6,(7,None)))))
  print('  OK')

test_inserer_dans_liste_triee()
