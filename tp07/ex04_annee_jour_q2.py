def est_bissextile(annee):
  return annee%4==0 and annee%100!=0 or annee%400==0

def nb_jours_annee(annee):
  ...

def test_nb_jours_annee():
  print('Test de la fonction nb_jours_annee')
  assert nb_jours_annee(1981)==365
  assert nb_jours_annee(1980)==366
  assert nb_jours_annee(1900)==365
  assert nb_jours_annee(1600)==366
  print('  OK')

def calculer_annee_jour(jours):
  ...

def test_calculer_annee_jour():
  print('Test de la fonction calculer_annee_jour')
  assert calculer_annee_jour(1)==(1980,1)
  assert calculer_annee_jour(365)==(1980,365)
  assert calculer_annee_jour(367)==(1981,1)
  assert calculer_annee_jour(380)==(1981,14)
  assert calculer_annee_jour(732)==(1982,1)
  assert calculer_annee_jour(10592)==(2008,365)
  assert calculer_annee_jour(10594)==(2009,1)
  assert calculer_annee_jour(10593)==(2008,366)
  assert calculer_annee_jour(366)==(1980,366)
  print('  OK')

test_nb_jours_annee()
test_calculer_annee_jour()
