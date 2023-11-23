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
def concatener_listes(liste1,liste2):
  if est_vide(liste1):
    return liste2
  
  li = concatener_listes(queue(liste1), liste2)
  return creer_liste(tete(liste1), li)
  
def test_concatener_listes():
  print('Test de la fonction concatener_listes')
  assert concatener_listes(None,None)==None
  assert concatener_listes(None,(6,(8,(3,(2,None)))))==(6,(8,(3,(2,None))))
  assert concatener_listes((4,(3,(1,(9,None)))),None)==(4,(3,(1,(9,None))))
  assert concatener_listes((8,(4,None)),(7,(1,None)))==(8,(4,(7,(1,None))))
  print('  OK')

test_concatener_listes()
