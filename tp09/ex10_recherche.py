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
def rechercher_premier_indice(liste,valeur):
  ...

def test_rechercher_premier_indice():
  print('Test de la fonction rechercher_premier_indice')
  assert rechercher_premier_indice(None,7)==-1
  assert rechercher_premier_indice((3,(5,(6,(6,(5,(4,(2,None))))))),7)==-1
  assert rechercher_premier_indice((3,(5,(6,(6,(5,(4,(2,None))))))),3)==0
  assert rechercher_premier_indice((3,(5,(6,(6,(5,(4,(2,None))))))),2)==6
  assert rechercher_premier_indice((3,(5,(6,(6,(5,(4,(2,None))))))),6)==2
  assert rechercher_premier_indice((3,(5,(6,(6,(5,(4,(2,None))))))),5)==1
  print('  OK')

def rechercher_indices_rec(liste,valeur,indice):
  ...

def test_rechercher_indices_rec():
  print('Test de la fonction rechercher_indices_rec')
  assert rechercher_indices_rec(None,5,4)==None
  assert rechercher_indices_rec((5,None),5,3)==(3,None)
  assert rechercher_indices_rec((6,(5,None)),5,2)==(3,None)
  assert rechercher_indices_rec((5,(6,(5,None))),5,1)==(1,(3,None))
  assert rechercher_indices_rec((3,(5,(6,(5,None)))),5,0)==(1,(3,None))
  print('  OK')

def rechercher_indices(liste,valeur):
  ...

def test_rechercher_indices():
  print('Test de la fonction rechercher_indices')
  assert rechercher_indices(None,7)==None
  assert rechercher_indices((3,(5,(6,(6,(5,(4,(2,None))))))),7)==None
  assert rechercher_indices((3,(5,(6,(6,(5,(4,(2,None))))))),3)==(0,None)
  assert rechercher_indices((3,(5,(6,(6,(5,(4,(2,None))))))),2)==(6,None)
  assert rechercher_indices((3,(5,(6,(6,(5,(4,(2,None))))))),6)==(2,(3,None))
  assert rechercher_indices((3,(5,(6,(6,(5,(4,(2,None))))))),5)==(1,(4,None))
  print('  OK')

test_rechercher_premier_indice()
test_rechercher_indices_rec()
test_rechercher_indices()
