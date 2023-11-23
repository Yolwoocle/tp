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
def longueur(liste):
  if est_vide(liste):
    return 0
  return 1 + longueur(queue(liste))

def test_longueur():
  print('Test de la fonction longueur')
  assert longueur(None)==0
  assert longueur((5,None))==1
  assert longueur((5,(9,(10,(-1,None)))))==4
  print('  OK')

def somme(liste):
  if est_vide(liste):
    return 0
  return tete(liste) + somme(queue(liste))

def test_somme():
  print('Test de la fonction somme')
  assert somme(None)==0
  assert somme((6,None))==6
  assert somme((7,(4,(-2,(3,None)))))==12
  print('  OK')

def convertir_en_chaine(liste):
  if est_vide(liste):
    return ""
  return str(tete(liste)) + " " + convertir_en_chaine(queue(liste))

def test_convertir_en_chaine():
  print('Test de la fonction convertir_en_chaine')
  assert convertir_en_chaine(None)==''
  assert convertir_en_chaine((10,None))=='10 '
  assert convertir_en_chaine((1,(2,(4,(5,(7,(8,None)))))))=='1 2 4 5 7 8 '
  print('  OK')

test_longueur()
test_somme()
test_convertir_en_chaine()
