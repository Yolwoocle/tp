"""
On considère un nombre entier strictement positif :
  • s'il est pair, on le divise par 2.
  • s'il est impair, on le multiplie par 3 et on ajoute 1.
  En répétant l'opération, on obtient une suite d'entiers positifs dont chacun ne
  dépend que de son prédécesseur.
"""
def syracuse(n):
  if n == 1:
    return [n]
  
  if n % 2 == 0:
    return [n] + syracuse(n//2)
  return [n] + syracuse(3*n + 1)

def test_syracuse():
  print('Test de la fonction syracuse')
  assert syracuse(1)==[1]
  assert syracuse(2)==[2, 1]
  assert syracuse(3)==[3, 10, 5, 16, 8, 4, 2, 1]
  assert syracuse(14)==[14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
  print('  OK')

test_syracuse()
