#!/usr/bin/python3

def somme_deux_a_deux(tableau):
  n = len(tableau)
  somme_tab = [0] * (n-1)
  for i in range(n-1):
    somme_tab[i] = tableau[i] + tableau[i+1]
  return somme_tab

def test_somme_deux_a_deux():
  print('Test de la fonction somme_deux_a_deux')
  tableau = [1,2,3,4]
  assert somme_deux_a_deux(tableau)==[3,5,7] and tableau==[1,2,3,4]
  tableau = [3,1]
  assert somme_deux_a_deux(tableau)==[4] and tableau==[3,1]
  tableau = [4,7,3,-8,2]
  assert somme_deux_a_deux(tableau)==[11,10,-5,-6] and tableau==[4,7,3,-8,2]
  tableau = [7,-3,2,9,11,-6]
  assert somme_deux_a_deux(tableau)==[4,-1,11,20,5] and tableau==[7,-3,2,9,11,-6]
  tableau = [-5,3,0,0,-1,5,-5,7]
  assert somme_deux_a_deux(tableau)==[-2,3,0,-1,4,0,2] and tableau==[-5,3,0,0,-1,5,-5,7]
  print('  OK')

def somme_glissante(tableau,n):
  somme_tab = [0] * (len(tableau) - n + 1)
  for j in range(n):
    somme_tab[0] += tableau[j]
  
  for i in range(1, len(tableau)-n+1):
    somme_tab[i] = somme_tab[i-1] - tableau[i-1] + tableau[i+n-1]
    
  return somme_tab


def test_somme_glissante():
  print('Test de la fonction somme_glissante Q2')
  tableau = [1,7,8,-2]
  # assert somme_glissante(tableau,1)==[1,7,8,-2] and tableau==[1,7,8,-2]
  assert somme_glissante(tableau,2)==[8,15,6] and tableau==[1,7,8,-2]
  assert somme_glissante(tableau,3)==[16,13] and tableau==[1,7,8,-2]
  assert somme_glissante(tableau,4)==[14] and tableau==[1,7,8,-2]
  print('  OK')
  print('Test de la fonction somme_glissante optimisée Q3')
  tableau = [1]*199999
  assert somme_glissante(tableau,100000)==[100000]*100000 and tableau==[1]*199999
  print('  OK')

test_somme_deux_a_deux()
test_somme_glissante()
