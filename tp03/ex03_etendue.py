#!/usr/bin/python3

def calculer_etendue(tableau):
    if len(tableau) == 0:
        return 0
    mi = tableau[0]
    ma = tableau[0]
    for i in range(1, len(tableau)):
        elt = tableau[i]
        if elt > ma:
            ma = elt
        if elt < mi:
            mi = elt
    return ma - mi

def test_calculer_etendue():
    print('Test de la fonction calculer_etendue')
    assert calculer_etendue([1]) == 0
    assert calculer_etendue([5,4,3,2,1]) == 4
    assert calculer_etendue([0,4,3,2,1]) == 4
    assert calculer_etendue([1,4,3,2,1]) == 3
    assert calculer_etendue([-5,-4,-3,-2,-4]) == 3

    assert calculer_etendue([]) == 0
    assert calculer_etendue([1,1,1,1,1,1,1]) == 0
    assert calculer_etendue([-1, -1, -1, -1]) == 0
    print('  OK')

test_calculer_etendue()