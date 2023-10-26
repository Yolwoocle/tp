#!/usr/bin/python3

def appliquer_cycle(tableau,cycle):
  if (len(cycle) <= 1):
    return
  aux = tableau[cycle[-1]]
  for i in range(len(cycle)-1, 0, -1):
    tableau[cycle[i]] = tableau[cycle[i-1]]
  
  tableau[cycle[0]] = aux 

def test_appliquer_cycle():
  print('Test de la fonction appliquer_cycle')
  tableau = [11,12,13]
  assert appliquer_cycle(tableau,[])==None and tableau==[11,12,13]
  tableau = [11,12,13,14]
  assert appliquer_cycle(tableau,[2])==None and tableau==[11,12,13,14]
  tableau = [11,12,13,14,15,16]
  assert appliquer_cycle(tableau,[2,5,1])==None and tableau==[11,16,12,14,15,13]
  tableau = [11,12,13,14,15,16]
  assert appliquer_cycle(tableau,[4,3,1,2,0,5])==None and tableau==[13,14,12,15,16,11]
  print('  OK')

test_appliquer_cycle()
