# FONCTIONS AUXILIAIRES
from ex05_fonctions_auxiliaires import *
import random

# EXERCICE

def partitionner_pivot(tab):
  n = len(tab)
  assert n>0, 'Pre-condition'
  pivot = tab[0] # ne pas modifier
  i_pivot = 0
  j = len(tab) - 1
  assert (
    0<=i_pivot<=j<n and tab[i_pivot]==pivot
    and est_infegal(tab,0,i_pivot,pivot) and est_sup(tab,j+1,n,pivot)
  ), 'Invariant (initialisation)'
  while i_pivot < j:
    if tab[i_pivot + 1] <= pivot:
      permuter(tab, i_pivot, i_pivot+1)
      i_pivot += 1
    else:
      permuter(tab, i_pivot+1, j)
      j -= 1
    
    assert 0<=i_pivot<=j<n, "1" 
    assert tab[i_pivot]==pivot, "2"
    assert est_infegal(tab,0,i_pivot,pivot), "3"
    assert est_sup(tab,j+1,n,pivot), "4"
  assert (
    0<=i_pivot<n and tab[i_pivot]==pivot
    and est_infegal(tab,0,i_pivot,pivot) and est_sup(tab,i_pivot+1,n,pivot)
  ), 'Post-condition'
  return i_pivot

def tab_eq(t1, t2):
  if len(t1) != len(t2):
    return False
  for i in range(len(t1)):
    if t1[i] != t2[i]:
      return False
  return True

def test_eq():
  print("test eq")
  for _ in range(1000):
    n = random.randint(1,100)
    tab = [random.randint(-1000,1000) for _ in range(n)]
    assert tab_eq(tab, tab)
    
  for _ in range(1000):
    n = random.randint(40,100)
    t1 = [random.randint(-1000,1000) for _ in range(n)]
    t2 = [random.randint(-1000,1000) for _ in range(n)]
    assert not tab_eq(t1, t2)
  print("  OK")

def test_partitionner_pivot():
  print('Test de la fonction partitionner_pivot')
  tab = [8]
  assert partitionner_pivot(tab)==0 and tab==[8]
  tab = [8,7]
  assert partitionner_pivot(tab)==1 and tab==[7,8]
  tab = [1,2,3]
  assert partitionner_pivot(tab)==0 and tab==[1,3,2]
  tab = [5,4,3,2,1]
  assert partitionner_pivot(tab)==4 and tab==[4,3,2,1,5]
  tab = [4,4,5,1,7,2,6]
  assert partitionner_pivot(tab)==3 and tab==[4,2,1,4,7,6,5]
  tab = [8,7,6,5,4,4,4,1,2,3]
  assert partitionner_pivot(tab)==9 and tab==[7,6,5,4,4,4,1,2,3,8]
  tab = [9,4,6,13,4,2,9,8,11,10,5]
  assert partitionner_pivot(tab)==7 and tab==[4,6,5,4,2,9,8,9,10,11,13]
  tab = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
  assert partitionner_pivot(tab)==14 and tab==[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
  
  print('  OK')

test_eq()
test_partitionner_pivot()