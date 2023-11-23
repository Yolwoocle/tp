def nombre_miroir_rec(n,m):
  if n == 0:
    return m
  return nombre_miroir_rec(n//10, m*10 + n%10)

def test_nombre_miroir_rec():
  print('Test de la fonction nombre_miroir_rec')
  assert nombre_miroir_rec(0,0)==0
  assert nombre_miroir_rec(0,237)==237
  assert nombre_miroir_rec(6,3278)==32786
  assert nombre_miroir_rec(3527,21)==217253
  assert nombre_miroir_rec(67287615,0)==51678276
  print('  OK')

def nombre_miroir(n):
  return nombre_miroir_rec(n, 0)


def test_nombre_miroir():
  print('Test de la fonction nombre_miroir')
  assert nombre_miroir(0)==0
  assert nombre_miroir(5)==5
  assert nombre_miroir(76)==67
  assert nombre_miroir(82938)==83928
  assert nombre_miroir(235672187265)==562781276532
  print('  OK')

test_nombre_miroir_rec()
test_nombre_miroir()
