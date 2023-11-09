def est_bissextile(annee):
  return annee%4==0 and annee%100!=0 or annee%400==0

def calculer_annee_jour(jours):
  annee = 1980
  while jours>365:
    if est_bissextile(annee):
      if jours > 366:
        jours -= 366
        annee += 1
    else:
      jours -= 365
      annee += 1
  return annee,jours

def test_calculer_annee_jour():
  print('Test de la fonction calculer_annee_jour')
  assert calculer_annee_jour(1)==(1980,1)
  assert calculer_annee_jour(365)==(1980,365)
  assert calculer_annee_jour(367)==(1981,1)
  assert calculer_annee_jour(380)==(1981,14)
  assert calculer_annee_jour(732)==(1982,1)
  assert calculer_annee_jour(10592)==(2008,365)
  assert calculer_annee_jour(10594)==(2009,1)
  print('  pas vraiment OK...')
  assert calculer_annee_jour(10593)==(2008,366)
  assert calculer_annee_jour(366)==(1980,366)
  print('  OK')

test_calculer_annee_jour()

