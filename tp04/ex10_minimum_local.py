#!/usr/bin/python3

def minimum_local(matrice,i,j):
  w,h = len(matrice[0]), len(matrice)
  m = matrice[i][j]
  
  for ii in range(i-1, i+2):
    for jj in range(j-1, j+2):
      if (0 <= ii < h and 0 <= jj < w) and matrice[ii][jj] < m:
        m = matrice[ii][jj]
  
  return m
      

def test_minimum_local():
  print('Test de la fonction minimum_local')
  matrice = [
    [4, 5, 6, 3, 2],
    [3, 6, 4, 1, 2],
    [5, 4, 9, 6, 7],
    [0, 8, 7, 4, 3],
  ]
  assert minimum_local(matrice,2,1)==0
  assert minimum_local(matrice,2,2)==1
  assert minimum_local(matrice,1,3)==1
  assert minimum_local(matrice,1,0)==3
  assert minimum_local(matrice,2,4)==1
  assert minimum_local(matrice,0,1)==3
  assert minimum_local(matrice,3,3)==3
  #
  assert minimum_local([[8]],0,0)==8
  print('  OK')

test_minimum_local()
