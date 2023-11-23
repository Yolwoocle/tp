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
def extraire_negatifs_positifs(liste):
  if est_vide(liste):
    return creer_liste_vide(), creer_liste_vide()
  n, p = extraire_negatifs_positifs(queue(liste))
  t = tete(liste)
  if t < 0:
    return creer_liste(t, n), p
  else:
    return n, creer_liste(t, p)
  
def test_extraire_negatifs_positifs():
  print('Test de la fonction extraire_negatifs_positifs')
  assert extraire_negatifs_positifs(None)==(None,None)
  assert extraire_negatifs_positifs((-7,None))==((-7,None),None)
  assert extraire_negatifs_positifs((0,None))==(None,(0,None))
  assert extraire_negatifs_positifs((6,None))==(None,(6,None))
  assert extraire_negatifs_positifs((-2,(11,(4,(3,(-6,None))))))==((-2,(-6,None)),(11,(4,(3,None))))
  assert extraire_negatifs_positifs((16,(-6,(2,(-7,(0,(9,None)))))))==((-6,(-7,None)),(16,(2,(0,(9,None)))))
  assert extraire_negatifs_positifs((-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,(-1,(1,None))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))) == (
    (-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,(-1,None)))))))))))))))))))))))))))))),
    (1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,(1,None))))))))))))))))))))))))))))))
  )
  print('  OK')

test_extraire_negatifs_positifs()
