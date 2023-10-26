#!/usr/bin/python3

def quatre_carres(n):
  assert n>=0, 'Pre-condition'
  
  def trouver_carre(n, somme):
    i = 0
    while i*i < n-somme:
      i += 1
    return i-1
  
  li = [0,0,0,0]
  somme = 0
  for i in range(4):
    x = trouver_carre(n, somme)
    print("x", x, "s", somme)
    somme += x*x
    li[i] = x
    
  a,b,c,d = li
  print(n, (a,b,c,d))
  assert a**2+b**2+c**2+d**2==n, f'Post-condition {a,b,c,d}'
  return a,b,c,d

def test_quatre_carres():
  print('Test de la fonction quatre_carres')
  for n in range(2,1000):
    a,b,c,d = quatre_carres(n)
    print(n,':',a,b,c,d)
  print('  OK')

test_quatre_carres()