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
def est_singleton(liste):
  return est_vide(queue(liste))

def maximum(liste):
  assert not est_vide(liste), 'Pré-condition'
  if est_singleton(liste):
    return tete(liste)
  
  m = maximum(queue(liste))
  if m > tete(liste):
    return m
  else:
    return tete(liste)

def test_maximum():
  print('Test de la fonction maximum')
  assert maximum((6,None))==6
  assert maximum((7,(4,(-2,(3,None)))))==7
  assert maximum((7,(4,(-2,(8,(3,None))))))==8
  assert maximum((7,(4,(-2,(8,(3,(19,None)))))))==19
  assert maximum((-999999999999999999999999999999999999999999999999999999999999,None))==-999999999999999999999999999999999999999999999999999999999999
  assert maximum((63,(82,(84,(81,(71,(14,(52,(38,(5,(23,(38,(26,(66,(22,(10,(64,(48,(63,(57,(3,(23,(72,(45,(78,(99,(100,(90,(83,(47,(36,(37,(62,(8,(16,(89,(56,(48,(71,(83,(89,None)))))))))))))))))))))))))))))))))))))))))==100
  print('  OK')

test_maximum()
