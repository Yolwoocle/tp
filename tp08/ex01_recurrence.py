def factorielle(n):
  if n == 0:
    return 1
  return n * factorielle(n-1)

def test_factorielle():
  print('Test de la fonction factorielle')
  assert factorielle(0)==1
  assert factorielle(1)==1
  assert factorielle(2)==2
  assert factorielle(3)==6
  assert factorielle(4)==24
  assert factorielle(5)==120
  assert factorielle(10)==3628800
  assert factorielle(15)==1307674368000
  print('  OK')

def suite_geometrique(u0,r,n):
  if n == 0:
    return u0
  return r * suite_geometrique(u0, r, n-1)

def test_suite_geometrique():
  print('Test de la fonction suite_geometrique')
  assert suite_geometrique(6,10,0)==6
  assert suite_geometrique(0,1,10)==0
  assert suite_geometrique(5,0,10)==0
  assert suite_geometrique(5,1,10)==5
  assert suite_geometrique(6,3,15)==6*(3**15)
  assert suite_geometrique(8,2,16)==8*(2**16)
  print('  OK')

test_factorielle()
test_suite_geometrique()
