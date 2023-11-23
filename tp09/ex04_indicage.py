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
def lire_element(liste,i):
  assert i>=0 and not est_vide(liste), 'Pré-condition'
  if i == 0:
    return tete(liste)
  return lire_element(queue(liste), i-1)

def test_lire_element():
  print('Test de la fonction lire_element')
  liste = (4,(2,(8,(9,(10,None)))))
  assert lire_element(liste,0)==4
  assert lire_element(liste,1)==2
  assert lire_element(liste,2)==8
  assert lire_element(liste,3)==9
  assert lire_element(liste,4)==10
  print('  OK')

def ecrire_element(liste,i,valeur):
  assert i>=0 and not est_vide(liste), 'Pré-condition'
  if i == 0:
    return creer_liste(valeur, queue(liste))
  q = ecrire_element(queue(liste), i-1, valeur)
  return creer_liste(tete(liste), q)

def test_ecrire_element():
  print('Test de la fonction ecrire_element')
  assert ecrire_element((4,(2,(8,(9,(10,None))))),0,7)==(7,(2,(8,(9,(10,None)))))
  assert ecrire_element((7,(2,(8,(9,(10,None))))),2,3)==(7,(2,(3,(9,(10,None)))))
  assert ecrire_element((7,(2,(3,(9,(10,None))))),4,8)==(7,(2,(3,(9,(8,None)))))
  print('  OK')

test_lire_element()
test_ecrire_element()
