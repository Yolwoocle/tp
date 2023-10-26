#!/usr/bin/python3

import random

def tableau_aleatoire(n):
  tab = [0]*n
  for i in range(n):
    tab[i] = random.randint(0,n)
  return tab

def maximum_et_bit_a_bit(tableau):
  n = len(tableau)
  assert n>=2, 'Pré-condition'
  m = 0
  for i in range(n):
    for j in range(i+1,n):
      b = tab[i] & tab[j]
      if b > m:
        m = b


def test_maximum_et_bit_a_bit():
  print('Test de la fonction maximum_et_bit_a_bit')
  assert maximum_et_bit_a_bit([26,22])==18
  assert maximum_et_bit_a_bit([240,15])==0
  assert maximum_et_bit_a_bit([240,15])==0
  # Puissances de 2 (1 seul bit à 1, jamais le même)
  assert maximum_et_bit_a_bit([256,16,1,8,64,0,1024,2,32,4,512])==0
  # Le maximum est atteint pour 170 & 38
  assert maximum_et_bit_a_bit([85,170,3,38,256])==34
  print('  OK')

test_maximum_et_bit_a_bit()

