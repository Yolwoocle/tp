#!/usr/bin/python3

def est_croissant(tab):
  ...

def test_est_croissant():
  print('Test de la fonction est_croissant')
  assert est_croissant([])==True
  assert est_croissant([3])==True
  assert est_croissant([3,3])==True
  assert est_croissant([3,5])==True
  assert est_croissant([5,3])==False
  assert est_croissant([-5,-3,-3,0,1,2,2,4])==True
  assert est_croissant([-5,-3,-3,0,1,2,2,1])==False
  assert est_croissant([-2,-3,-3,0,1,2,2,4])==False
  assert est_croissant([-5,-3,-3,0,-1,2,2,4])==False
  print('  OK')

# Q1 : Méthodologie :
# Pre-condition : ...
# Post-condition : tab[i]<=valeur and (i+1==len(tab) or valeur<tab[i+1])
# Invariant : tab[i]<=valeur and (j==len(tab) or valeur<tab[j])
# Condition d'arrêt : ...
# Condition de boucle : ...

def recherche_par_dichotomie(tab,valeur):
  ...



def test_recherche_par_dichotomie():
  print('Test de la fonction recherche_par_dichotomie')
  assert recherche_par_dichotomie([5],5)==0
  assert recherche_par_dichotomie([5],6)==0
  assert recherche_par_dichotomie([1,2,2,4],2)==2
  assert recherche_par_dichotomie([6,7,7,8,9],10)==4
  assert recherche_par_dichotomie([7,8,9,10,11],10)==3
  assert recherche_par_dichotomie([0,1,2,4,4,6,6,6,7,8,8,8,9,9,10,13,14,15,16,18],9)==13
  assert recherche_par_dichotomie([0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7],1)==29
  print('  OK')

test_est_croissant()
test_recherche_par_dichotomie()
