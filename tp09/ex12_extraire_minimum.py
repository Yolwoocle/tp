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

def est_singleton(liste):
  return est_vide(queue(liste))

# EXERCICE
def extraire_minimum(liste):
  def aux(liste, acc_min):
    if est_vide(liste):
      return acc_min, creer_liste_vide()
    
    x = tete(liste)
    mini, acc_li = aux(queue(liste), x if x < acc_min else acc_min)
    if x == mini:
      return mini, acc_li
    else:
      return mini, creer_liste(tete(liste), acc_li)
      
  mini, nli = aux(liste, tete(liste))
  return mini, nli

def test_extraire_minimum():
  print('Test de la fonction extraire_minimum')
  
  # print(extraire_minimum((7,None)), "\t", (7,None))
  # print(extraire_minimum((1,(3,None))), "\t", (1,(3,None)))
  # print(extraire_minimum((3,(1,None))), "\t", (1,(3,None)))
  # print(extraire_minimum((1,(7,(2,(6,(9,None)))))), "\t", (1,(7,(2,(6,(9,None))))))
  # print(extraire_minimum((7,(2,(6,(9,(1,None)))))), "\t", (1,(7,(2,(6,(9,None))))))
  # print(extraire_minimum((2,(7,(1,(6,(9,None)))))), "\t", (1,(2,(7,(6,(9,None))))))
  # print(extraire_minimum((2,(7,(1,(6,(9,None)))))), "\t", (1,(2,(7,(6,(9,None))))))
  
  assert extraire_minimum((7,None))==(7,None)
  assert extraire_minimum((1,(3,None)))==(1,(3,None))
  assert extraire_minimum((3,(1,None)))==(1,(3,None))
  assert extraire_minimum((1,(7,(2,(6,(9,None))))))==(1,(7,(2,(6,(9,None)))))
  assert extraire_minimum((7,(2,(6,(9,(1,None))))))==(1,(7,(2,(6,(9,None)))))
  assert extraire_minimum((2,(7,(1,(6,(9,None))))))==(1,(2,(7,(6,(9,None)))))
  assert extraire_minimum((2,(7,(1,(6,(9,None))))))==(1,(2,(7,(6,(9,None)))))
  print('  OK')

test_extraire_minimum()
