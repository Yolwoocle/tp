def est_tranche_palindrome(tab,d,f):
  while d<f-1:
    if not tab[d] == tab[f-1]:
      return False
    d += 1
    f -= 1
  return True

# Q1 : Méthodologie
# Pré-condition : True
# Post-condition : d==0 or tab[d-1]!=tab[f]
# Invariant : 0<=d<=f<=n and d+f==n and est_tranche_palindrome(tab,d,f)
# Condition d'arrêt : ...
# Condition de boucle : ...

def plus_long_palindrome_centre(tab):
  n = len(tab)
  d = 0
  f = n-1
  invariant = lambda: 0<=d<=f<=n and d+f==n and est_tranche_palindrome(tab,d,f)
  assert invariant(), "Invariant (init)"
  assert invariant(), "Invariant (boucle)"
  assert (d==0 or tab[d-1]!=tab[f]), "Post-condition"


def test_plus_long_palindrome_centre():
  print('Test de la fonction plus_long_palindrome_centre')
  assert plus_long_palindrome_centre([])==(0,0)
  assert plus_long_palindrome_centre([1])==(0,1)
  assert plus_long_palindrome_centre([2,4])==(1,1)
  assert plus_long_palindrome_centre([3,5,4])==(1,2)
  assert plus_long_palindrome_centre([4,2,3,0])==(2,2)
  assert plus_long_palindrome_centre([2,3,3,1])==(1,3)
  assert plus_long_palindrome_centre([1,2,3,2,1,0])==(3,3)
  assert plus_long_palindrome_centre([4,4,3,2,4,4])==(3,3)
  assert plus_long_palindrome_centre([1,2,3,3,2,4])==(1,5)
  assert plus_long_palindrome_centre([4,2,2,5,2,2,1])==(1,6)
  assert plus_long_palindrome_centre([4,2,1,3,5,3,1,3,0])==(2,7)
  assert plus_long_palindrome_centre([4,2,6,6,2,4])==(0,6)
  print('  OK')

test_plus_long_palindrome_centre()
