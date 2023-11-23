# FONCTIONS AUXILIAIRES
from ex05_fonctions_auxiliaires import *

# Q1 : NÉGATIFS - POSITIFS

def negatifs_positifs(tab):
  n = len(tab)
  assert True, 'Pre-condition'
  i = 0
  j = len(tab)
  assert 0<=i<=j<=n and est_inf(tab,0,i,0) and est_supegal(tab,j,n,0), 'Invariant (initialisation)'
  while i < j:
    if tab[i] < 0:
      i += 1
    else: 
      permuter(tab, i, j-1)
      j -= 1
    assert 0<=i<=j<=n and est_inf(tab,0,i,0) and est_supegal(tab,j,n,0), 'Invariant (itération)'
  assert 0<=i<=n and est_inf(tab,0,i,0) and est_supegal(tab,i,n,0), 'Post-condition'
  return i

def test_negatifs_positifs():
  print('Test de la fonction negatifs_positifs')
  tab = []
  assert negatifs_positifs(tab)==0 and tab==[]
  tab = [0]
  assert negatifs_positifs(tab)==0 and tab==[0]
  tab = [1]
  assert negatifs_positifs(tab)==0 and tab==[1]
  tab = [-1]
  assert negatifs_positifs(tab)==1 and tab==[-1]
  tab = [2,-1,0]
  assert negatifs_positifs(tab)==1 and tab==[-1,0,2]
  tab = [2,2,-1,-1,2,2,-1,-1,2,-1,-1,2]
  assert negatifs_positifs(tab)==6 and tab==[-1,-1,-1,-1,-1,-1,2,2,2,2,2,2]
  tab = [9,-4,6,-13,4,-2,9,-8,11,0,-5]
  assert negatifs_positifs(tab)==5 and tab==[-5,-4,-8,-13,-2,9,4,11,0,6,9]
  print('  OK')

# Q2 : NÉGATIFS - NULS - POSITIFS

def negatifs_nuls_positifs(tab):
  n = len(tab)
  assert True, 'Pre-condition'
  i = 0
  j = 0
  k = len(tab)
  assert (
    0<=i<=j<=k<=n and est_inf(tab,0,i,0) 
    and est_egal(tab,i,j,0) and est_sup(tab,k,n,0)
  ), 'Invariant (initialisation)'
  while i < k and j < k:
    if tab[j] < 0:
      permuter(tab, i, j)
      i += 1
      j += 1
    elif tab[j] == 0:
      j += 1
    else:
      permuter(tab, j, k-1)
      k -= 1
    assert 0<=i<=j<=k<=n , 'Invariant (itération)1'
    assert est_inf(tab,0,i,0) , 'Invariant (itération)2'
    assert est_egal(tab,i,j,0) , 'Invariant (itération)3'
    assert est_sup(tab,k,n,0), 'Invariant (itération)4'
  assert (
    0<=i<=j<=n and est_inf(tab,0,i,0) 
    and est_egal(tab,i,j,0) and est_sup(tab,j,n,0)
  ), 'Post-condition'
  return i,j

def test_negatifs_nuls_positifs():
  print('Test de la fonction negatifs_nuls_positifs')
  tab = []
  assert negatifs_nuls_positifs(tab)==(0,0) and tab==[]
  tab = [0]
  assert negatifs_nuls_positifs(tab)==(0,1) and tab==[0]
  tab = [1]
  assert negatifs_nuls_positifs(tab)==(0,0) and tab==[1]
  tab = [-1]
  assert negatifs_nuls_positifs(tab)==(1,1) and tab==[-1]
  tab = [2,-1,0]
  assert negatifs_nuls_positifs(tab)==(1,2) and tab==[-1,0,2]
  tab = [2,0,2,-1,0,-1,0,2,2,-1,0,-1,2,-1,-1,0,2,0]
  assert negatifs_nuls_positifs(tab)==(6,12) and tab==[-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,2,2,2,2,2,2]
  tab = [9,-4,6,-13,4,-2,9,-8,11,0,-5]
  assert negatifs_nuls_positifs(tab)==(5,6) and tab==[-5,-4,-13,-8,-2,0,9,11,4,6,9]
  print('  OK')

test_negatifs_positifs()
test_negatifs_nuls_positifs()