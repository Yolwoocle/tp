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
def ajouter_element_fin(liste,valeur):
  ...

def test_ajouter_element_fin():
  print('Test de la fonction ajouter_element_fin')
  assert ajouter_element_fin(None,-6)==(-6,None)
  assert ajouter_element_fin((-6,None),3)==(-6,(3,None))
  assert ajouter_element_fin((-6,(3,None)),7)==(-6,(3,(7,None)))
  print('  OK')

def inserer_element(liste,i,valeur):
  assert i==0 or (i>0 and not est_vide(liste)), 'Pré-condition'
  ...

def test_inserer_element():
  print('Test de la fonction inserer_element')
  assert inserer_element(None,0,-6)==(-6,None)
  assert inserer_element((-6,None),0,3)==(3,(-6,None))
  assert inserer_element((3,(-6,None)),1,7)==(3,(7,(-6,None)))
  assert inserer_element((3,(7,(-6,None))),3,9)==(3,(7,(-6,(9,None))))
  print('  OK')

def supprimer_element(liste,i):
  assert i>=0 and not est_vide(liste), 'Pré-condition'
  ...

def test_supprimer_element():
  print('Test de la fonction supprimer_element')
  assert supprimer_element((7,(4,(2,(3,None)))),2)==(7,(4,(3,None)))
  assert supprimer_element((7,(4,(3,None))),2)==(7,(4,None))
  assert supprimer_element((7,(4,None)),0)==(4,None)
  assert supprimer_element((4,None),0)==None
  print('  OK')

test_ajouter_element_fin()
test_inserer_element()
test_supprimer_element()
