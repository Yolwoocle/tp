#!/usr/bin/python3

def est_matrice(matrice):
  if len(matrice) == 0:
    return True
  
  n = len(matrice[0])
  for i in range(1, len(matrice)):
    if len(matrice[i]) != n:
      return False
  return True

def test_est_matrice():
  print('Test de la fonction est_matrice')
  assert est_matrice([[1]])==True
  assert est_matrice([[4,7,3,-8,2]])==True
  assert est_matrice([[4],[7],[3],[-8],[2]])==True
  assert est_matrice([[1,2,3,4],[2,3,4,1]])==True
  assert est_matrice([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==True
  assert est_matrice([[8],[7,1],[3,4]])==False
  assert est_matrice([[9,7,8],[7,1,2],[6]])==False
  assert est_matrice([[1,2,3,4],[5,7,8],[9,10,11,12]])==False
  assert est_matrice([[1,4],[5,7,8],[9,10,12]])==False
  assert est_matrice([[1,4,1],[5,7,8],[9,12]])==False
  print('  OK')

test_est_matrice()
