#!/usr/bin/python3

def matrice_produit(colonne,ligne):
  l, c = len(ligne), len(colonne)
  
  mat = [None] * c
  for i in range(c):
    mat[i] = [0] * l
  
  for i in range(c):
    for j in range(l):
      mat[i][j] = colonne[i] * ligne[j]
  
  return mat

def test_matrice_produit():
  print('Test de la fonction matrice_produit')
  assert matrice_produit([2],[3])==[[6]]
  assert matrice_produit([1,2],[3,4])==[[3,4],[6,8]]
  assert matrice_produit([1,3,2],[4,6,5])==[[4,6,5],[12,18,15],[8,12,10]]
  assert matrice_produit([1,3],[4,6,5])==[[4,6,5],[12,18,15]]
  assert matrice_produit([7,8,-2,9],[1,-3,4,-5])==[
    [  7,-21, 28,-35],
    [  8,-24, 32,-40],
    [ -2,  6, -8, 10],
    [  9,-27, 36,-45]
  ]  
  assert matrice_produit([7,8,-2],[1,-3,4,-5])==[
    [  7,-21, 28,-35],
    [  8,-24, 32,-40],
    [ -2,  6, -8, 10]
  ]
  print('  OK')

test_matrice_produit()
