import sys
print(f"sys.getrecursionlimit() == {sys.getrecursionlimit()}")

def puissance(a,n):
  if n == 0:
    return 1
  
  if n % 2 == 0:
    p = puissance(a, n//2)
    return p*p
  return a * puissance(a, n-1)


def test_puissance():
  print('Test de la fonction puissance')
  assert puissance(0,0)==1
  assert puissance(0,0)==1
  assert puissance(0,0)==1
  assert puissance(0,1)==0
  assert puissance(-3,1)==-3
  assert puissance(3,1)==3
  assert puissance(0,10)==0
  assert puissance(-4,7)==(-4)**7
  assert puissance(8,5)==8**5
  print('  OK (version non-optimisée)')
  for n in range(990,1010):
    assert puissance(11,n)==11**n
    print('  OK pour la valeur',n)
  assert puissance(11,1000000)==11**1000000
  # Le test suivant doit être traité par le cas général (pas de test ad hoc)
  # /!\ Attention aux doubles appels récursifs /!\
  assert puissance(1,100000000000000000000000000000000000000000)==1
  print('  OK (version optimisée)')

test_puissance()
