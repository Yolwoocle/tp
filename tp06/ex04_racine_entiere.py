def racine_entiere(n):
  assert n>=0, 'Pre-condition'
  a,b = 0,n+1
  assert 0<=a<b and a**2<=n<b**2, 'Invariant (initialisation)'
  while a+1<b:
    m = (a+b)//2
    if m**2<=n:
      a = m
    else:
      b = m
    assert 0<=a<b and a**2<=n<b**2, 'Invariant (itération)'
  assert 0<=a, 'Post-condition (1)'
  assert a**2<=n<(a+1)**2, 'Post-condition (2)'
  return a


def test_racine_entiere():
  print('Test de la fonction racine_entiere')
  assert racine_entiere(0)==0
  assert racine_entiere(1)==1
  assert racine_entiere(2)==1
  assert racine_entiere(4)==2
  assert racine_entiere(15)==3
  assert racine_entiere(16)==4
  assert racine_entiere(25)==5
  assert racine_entiere(26)==5
  assert racine_entiere(395)==19
  assert racine_entiere(5469)==73
  assert racine_entiere(64474)==253
  assert racine_entiere(975602)==987
  print('  OK')

test_racine_entiere()
