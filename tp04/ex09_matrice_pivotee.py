#!/usr/bin/python3

def pivoter(matrice):
  w, h = len(matrice[0]), len(matrice)
  out = [None] * w
  for i in range(w):
    out[i] = [0] * h
    
  for i in range(h):
    for j in range(w):
      out[j][h - i - 1] = matrice[i][j]
      
  return out
      

def test_pivoter():
  print('Test de la fonction pivoter')
  assert pivoter([[1]])==[[1]]
  assert pivoter([[4,7,3,-8,2]])==[[4],[7],[3],[-8],[2]]
  assert pivoter([[4],[7],[3],[-8],[2]])==[[2,-8,3,7,4]] 
  assert pivoter([[1,2,3,4],[2,3,4,5]])==[[2,1],[3,2],[4,3],[5,4]]
  assert pivoter([[1,2],[2,3],[3,4],[4,5]])==[[4,3,2,1],[5,4,3,2]]
  assert pivoter([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==[[9,5,1],[10,6,2],[11,7,3],[12,8,4]]
  assert pivoter([[1,5,9],[2,6,10],[3,7,11],[4,8,12]])==[[4,3,2,1],[8,7,6,5],[12,11,10,9]]
  print('  OK')

test_pivoter()
