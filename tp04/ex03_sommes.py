#!/usr/bin/python3

def sommes_lignes(matrice):
  vec = [0] * len(matrice)
  for i in range(len(matrice)):
    s = 0
    for j in range(len(matrice[0])):
      s += matrice[i][j]
    vec[i] = s
  return vec

def test_sommes_lignes():
  print('Test de la fonction sommes_lignes')
  assert sommes_lignes([[1]])==[1]
  assert sommes_lignes([[4,7,3,-8,2]])==[8]
  assert sommes_lignes([[4],[7],[3],[-8],[2]])==[4,7,3,-8,2] 
  assert sommes_lignes([[1,2,3,4],[2,3,4,5]])==[10,14]
  assert sommes_lignes([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==[10,26,42]
  print('  OK')

def sommes_colonnes(matrice):
  vec = [0] * len(matrice[0])
  for i in range(len(matrice[0])):
    s = 0
    for j in range(len(matrice)):
      s += matrice[j][i]
    vec[i] = s
  return vec

def test_sommes_colonnes():
  print('Test de la fonction sommes_colonnes')
  assert sommes_colonnes([[1]])==[1]
  assert sommes_colonnes([[4,7,3,-8,2]])==[4,7,3,-8,2]
  assert sommes_colonnes([[4],[7],[3],[-8],[2]])==[8] 
  assert sommes_colonnes([[1,2,3,4],[2,3,4,5]])==[3,5,7,9]
  assert sommes_colonnes([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==[15,18,21,24]
  print('  OK')

test_sommes_lignes()
test_sommes_colonnes()
