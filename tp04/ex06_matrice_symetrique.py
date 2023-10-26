#!/usr/bin/python3

def est_carree(matrice):
  return len(matrice) == len(matrice[0])

def test_est_carree():
  print('Test de la fonction est_carree')
  assert est_carree([[8]])==True
  assert est_carree([[1,3],[2,1]])==True
  assert est_carree([[7,1,2],[1,7,2],[7,2,1]])==True
  assert est_carree([[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]])==True
  assert est_carree([[4,6,5],[12,18,15]])==False
  assert est_carree([[7,-21,28,-35],[8,-24,32,-40],[-2,6,-8,10]])==False
  print('  OK')

def est_symetrique(matrice):
  assert est_carree(matrice), 'Pre-condition'
  h, w = len(matrice), len(matrice[0])
  for i in range(h):
    for j in range(i+1):
      if matrice[i][j] != matrice[j][i]:
        return False
  return True
      

def test_est_symetrique():
  print('Test de la fonction est_symetrique')
  assert est_symetrique([[8]])==True
  assert est_symetrique([[1,3],[2,1]])==False
  assert est_symetrique([[1,3],[3,2]])==True
  assert est_symetrique([[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]])==True
  assert est_symetrique([[7,1,2],[1,7,2],[7,2,1]])==False
  print('  OK')

test_est_carree()
test_est_symetrique()
