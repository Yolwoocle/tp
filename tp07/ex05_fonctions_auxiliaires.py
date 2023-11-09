# Q1

def permuter(tab,i,j):
  ...

def test_permuter():
  print('Test de la fonction permuter')
  tab = [0,1,2,3,4,5]
  assert permuter(tab,0,5)==None and tab==[5,1,2,3,4,0], 'Étape 1'
  assert permuter(tab,2,3)==None and tab==[5,1,3,2,4,0], 'Étape 2'
  assert permuter(tab,3,5)==None and tab==[5,1,3,0,4,2], 'Étape 3'
  assert permuter(tab,2,0)==None and tab==[3,1,5,0,4,2], 'Étape 4'
  assert permuter(tab,1,1)==None and tab==[3,1,5,0,4,2], 'Étape 5'
  print('  OK')

def est_infegal(tab,g,d,m):
  ...

def test_est_infegal():
  print('Test de la fonction est_infegal')
  assert est_infegal([4,2,5,1,3,0],0,6,5)==True
  assert est_infegal([4,2,5,1,3,0],2,6,3)==False
  assert est_infegal([4,2,5,1,3,0],3,6,3)==True
  assert est_infegal([4,2,5,1,3,0],3,6,1)==False
  assert est_infegal([4,2,5,1,3,0],3,4,1)==True
  assert est_infegal([4,2,5,1,3,0],3,4,0)==False
  assert est_infegal([4,2,5,1,3,0],3,3,0)==True
  print('  OK')

def est_inf(tab,g,d,m):
  ...

def test_est_inf():
  print('Test de la fonction est_inf')
  assert est_inf([4,2,5,1,3,0],0,6,6)==True
  assert est_inf([4,2,5,1,3,0],2,6,4)==False
  assert est_inf([4,2,5,1,3,0],3,6,4)==True
  assert est_inf([4,2,5,1,3,0],3,6,2)==False
  assert est_inf([4,2,5,1,3,0],3,4,2)==True
  assert est_inf([4,2,5,1,3,0],3,4,1)==False
  assert est_inf([4,2,5,1,3,0],3,3,1)==True
  print('  OK')

def est_supegal(tab,g,d,m):
  ...

def test_est_supegal():
  print('Test de la fonction est_supegal')
  assert est_supegal([4,2,5,1,3,0],0,6,0)==True
  assert est_supegal([4,2,5,1,3,0],0,6,1)==False
  assert est_supegal([4,2,5,1,3,0],0,5,1)==True
  assert est_supegal([4,2,5,1,3,0],0,4,2)==False
  assert est_supegal([4,2,5,1,3,0],0,3,2)==True
  assert est_supegal([4,2,5,1,3,0],2,3,6)==False
  assert est_supegal([4,2,5,1,3,0],3,3,6)==True
  print('  OK')

def est_sup(tab,g,d,m):
  ...

def test_est_sup():
  print('Test de la fonction est_sup')
  assert est_sup([4,2,5,1,3,0],0,6,-1)==True
  assert est_sup([4,2,5,1,3,0],0,6,0)==False
  assert est_sup([4,2,5,1,3,0],0,5,0)==True
  assert est_sup([4,2,5,1,3,0],0,4,1)==False
  assert est_sup([4,2,5,1,3,0],0,3,1)==True
  assert est_sup([4,2,5,1,3,0],2,3,5)==False
  assert est_sup([4,2,5,1,3,0],3,3,5)==True
  print('  OK')

def est_egal(tab,g,d,m):
  ...

def test_est_egal():
  print('Test de la fonction est_egal')
  assert est_egal([4,4,5,5,5,0],2,5,5)==True
  assert est_egal([4,4,5,5,5,0],1,5,5)==False
  assert est_egal([4,4,5,5,5,0],2,6,5)==False
  assert est_egal([4,4,5,5,5,0],0,2,4)==True
  assert est_egal([4,4,5,5,5,0],0,0,4)==True
  assert est_egal([4,4,5,5,5,0],0,3,4)==False
  assert est_egal([4,4,5,5,5,0],5,6,0)==True
  assert est_egal([4,4,5,5,5,0],6,6,0)==True
  assert est_egal([4,4,5,5,5,0],4,6,0)==False
  print('  OK')

test_permuter()
test_est_infegal()
test_est_inf()
test_est_supegal()
test_est_sup()
test_est_egal()
