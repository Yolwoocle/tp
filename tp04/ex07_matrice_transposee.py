#!/usr/bin/python3

def transposer(matrice):
  w, h = len(matrice[0]), len(matrice)
  out = [None] * w
  for i in range(w):
    out[i] = [0] * h
  
  for i in range(h):
    for j in range(w):
      out[j][i] = matrice[i][j]
    
  return out

  
def test_transposer():
  print('Test de la fonction transposer')
  assert transposer([[1]])==[[1]]
  assert transposer([[4,7,3,-8,2]])==[[4],[7],[3],[-8],[2]]
  assert transposer([[4],[7],[3],[-8],[2]])==[[4,7,3,-8,2]] 
  assert transposer([[1,2,3,4],[2,3,4,5]])==[[1,2],[2,3],[3,4],[4,5]]
  assert transposer([[1,2],[2,3],[3,4],[4,5]])==[[1,2,3,4],[2,3,4,5]]
  assert transposer([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==[[1,5,9],[2,6,10],[3,7,11],[4,8,12]]
  assert transposer([[1,5,9],[2,6,10],[3,7,11],[4,8,12]])==[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
  print('  OK')

test_transposer()
