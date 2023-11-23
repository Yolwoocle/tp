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
def sont_opposees(liste1,liste2):
  if est_vide(liste1) and est_vide(liste2):
    return True
  if est_vide(liste1) != est_vide(liste2):
    return False
  
  if tete(liste1) != -tete(liste2):
    return False
  return sont_opposees(queue(liste1), queue(liste2))

def test_sont_opposees():
  print('Test de la fonction sont_opposees')
  assert sont_opposees(None,None)==True
  assert sont_opposees(None,(6,None))==False
  assert sont_opposees((6,None),(-6,None))==True
  assert sont_opposees((6,None),(-8,None))==False
  assert sont_opposees((7,(-5,None)),(-7,None))==False
  assert sont_opposees((7,(-5,None)),(-7,(5,(-8,(6,(-1,(0,None)))))))==False
  assert sont_opposees((7,(-5,(8,(-6,(1,(0,None)))))),(-7,(5,(-8,(6,(-1,(0,None)))))))==True
  assert sont_opposees((7,(-5,(8,(-6,(1,(0,None)))))),(-7,(5,(-8,(2,(-1,(0,None)))))))==False
  print('  OK')

test_sont_opposees()
