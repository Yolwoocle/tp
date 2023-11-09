# FONCTIONS AUXILIAIRES

def est_infegal(tab,g,d,m):
  ...

def est_sup(tab,g,d,m):
  ...

def permuter(tab,i,j):
  ...

# EXERCICE

def partitionner_pivot(tab):
  n = len(tab)
  assert n>0, 'Pre-condition'
  pivot = tab[0] # ne pas modifier
  ...
  assert (
    0<=i_pivot<=j<n and tab[i_pivot]==pivot
    and est_infegal(tab,0,i_pivot,pivot) and est_sup(tab,j+1,n,pivot)
  ), 'Invariant (initialisation)'
  while ...:
    ...
    assert (
      0<=i_pivot<=j<n and tab[i_pivot]==pivot
      and est_infegal(tab,0,i_pivot,pivot) and est_sup(tab,j+1,n,pivot)
    ), 'Invariant (itération)'
  assert (
    0<=i_pivot<n and tab[i_pivot]==pivot
    and est_infegal(tab,0,i_pivot,pivot) and est_sup(tab,i_pivot+1,n,pivot)
  ), 'Post-condition'
  return i_pivot

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

test_partitionner_pivot()