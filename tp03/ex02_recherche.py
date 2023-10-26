#!/usr/bin/python3

def rechercher(valeur, tableau):
    for i in range(len(tableau)):
        if tableau[i] == valeur:
            return i
    return -1

# pour validation, ne pas modifier
def test_rechercher():
    print('Test de la fonction rechercher')
    assert rechercher(1, [1]) == 0
    assert rechercher(1, [5,4,3,2,1]) == 4
    assert rechercher(1, [0,4,3,2,1]) == 4
    assert rechercher(1, [1,4,3,2,1]) == 0
    assert rechercher(1, [5,4,3,2,4]) == -1

    assert rechercher('charizard', ['snorlax', 'charizard', 'mewtwo','bulbizare']) == 1
    assert rechercher('kirby', ['snorlax', 'charizard', 'mewtwo','bulbizare']) == -1 # kirby n'est PAS un pokemon...
    assert rechercher('c', ['snorlax', 'charizard', 'mewtwo','bulbizare']) == -1

    assert rechercher(1, []) == -1
    assert rechercher([1,2,3], [[1], [1,2] , [1,2,3], [1,2,3,4]]) == 2
    print('  OK')

test_rechercher()