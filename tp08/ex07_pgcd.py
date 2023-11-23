
def pgcd(a,b):
  """
  Le PGCD de a et 0 est a.
  • Si b est non nul, le PGCD de a et b est aussi le PGCD de b et a%b  
  """
  if b == 0:
    return a
  return pgcd(b, a%b)

def test_pgcd():
  print('Test de la fonction pgcd')
  assert pgcd(1,0)==1
  assert pgcd(167,0)==167
  assert pgcd(167,1)==1
  assert pgcd(81,3)==3
  assert pgcd(81285,23)==1
  assert pgcd(144,84)==12
  assert pgcd(51,9)==3
  assert pgcd(678,13)==1
  print('  OK')

test_pgcd()
