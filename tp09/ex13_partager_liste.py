#!/usr/bin/env python3

# FONCTIONS DE BASE
def creer_liste_vide():
    return None

def creer_liste(t,q):
    return t,q

def tete(liste):
    assert liste!=None, 'Pré-condition (tete)'
    return liste[0]

def queue(liste):
    assert liste!=None, 'Pré-condition (queue)'
    return liste[1]

def est_vide(liste):
    return liste==None

# EXERCICE
def partager_liste(liste):
    def aux(liste, i):
        if est_vide(liste):
            return creer_liste_vide(), creer_liste_vide()
        a, b = aux(queue(liste), (i+1)%2)
        if i == 0:
            return creer_liste(tete(liste), a), b
        else: 
            return a, creer_liste(tete(liste), b)
    return aux(liste, 0)

def test_partager_liste():
    print('Test de la fonction partager_liste')
    assert partager_liste(None)==(None,None)
    assert partager_liste((4,None))==((4,None),None)
    assert partager_liste((5,(6,None)))==((5,None),(6,None))
    assert partager_liste((9,(8,(7,None))))==((9,(7,None)),(8,None))
    assert partager_liste((10,(2,(6,(4,(7,(3,(1,(5,None)))))))))==((10,(6,(7,(1,None)))),(2,(4,(3,(5,None)))))
    print('  OK')


test_partager_liste()
