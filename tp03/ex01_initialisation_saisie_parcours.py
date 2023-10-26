#!/usr/bin/python3

import sys,io

def initialiser_tableau(taille,valeur_defaut):
    return [valeur_defaut] * taille

def test_initialiser_tableau():
    print('Test de la fonction initialiser_tableau')
    assert initialiser_tableau(2,0)==[0,0]
    assert initialiser_tableau(5,0)==[0,0,0,0,0]
    assert initialiser_tableau(3,False)==[False,False,False]
    assert initialiser_tableau(4,1.0)==[1.0,1.0,1.0,1.0]
    assert initialiser_tableau(6,'a')==['a','a','a','a','a','a']
    print('  OK')

def saisir_valeurs(tableau):
    n = len(tableau)
    for i in range(n):
        tableau[i] = int(input("Votre valeur ?"))

def calculer_somme(tableau):
    s = 0
    for e in tableau:
        s += e
    return s

def test_calculer_somme():
    print('Test de la fonction calculer_somme')
    assert calculer_somme([0,0,0,0,0])==0
    assert calculer_somme([0,0,0,1,0])==1
    assert calculer_somme([0,0,0,1,0,1])==2
    assert calculer_somme([12,-10])==2
    print('  OK')

def calculer_moyenne(tableau):
    return calculer_somme(tableau) / len(tableau)

def test_calculer_moyenne():
    print('Test de la fonction calculer_moyenne')
    assert calculer_moyenne([0,0,0,0,0])==0
    assert calculer_moyenne([10,10,10,10,10])==10
    assert calculer_moyenne([0, 20, 10])==10
    print('  OK')

test_initialiser_tableau()
test_calculer_somme()
test_calculer_moyenne()