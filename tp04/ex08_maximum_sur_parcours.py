#!/usr/bin/python3


def deplacer(position,direction):
    assert direction in 'NSOE'
    vectors = {'N': (-1, 0), 'S': (1, 0), 'O': (0, -1), 'E': (0, 1)}
    di, dj = vectors[direction]
    return (position[0] + di, position[1] + dj)


def test_deplacer():
    print('Test de la fonction deplacer')
    assert deplacer((6,3),'N')==(5,3)
    assert deplacer((5,3),'O')==(5,2)
    assert deplacer((5,2),'S')==(6,2)
    assert deplacer((6,2),'E')==(6,3)
    print('  OK')

def est_parcours_valide(dimensions,depart,chemin):
    h, w = dimensions
    pos = (depart[0], depart[1])
    def pos_valide(pos):
        return (0 <= pos[0] < h and 0 <= pos[1] < w)
    
    if not pos_valide(pos):
        return False
    for dir in chemin:
        pos = deplacer(pos, dir)
        if not pos_valide(pos):
            return False
    return True

def test_est_parcours_valide():
    print('Test de la fonction est_parcours_valide')
    # parcours : (0,0)->(1,0)->(1,1)->(0,1)->(0,0)
    assert est_parcours_valide((2,2),(0,0),'SENO')==True
    # parcours : (1,1)->(0,1)->(0,0)->(1,0)->(1,1)
    assert est_parcours_valide((2,2),(1,1),'NOSE')==True
    # departs invalides
    assert est_parcours_valide((4,5),(-1,2),'S')==False
    assert est_parcours_valide((4,5),(4,2),'N')==False
    assert est_parcours_valide((4,5),(2,-1),'S')==False
    assert est_parcours_valide((4,5),(2,5),'N')==False
    # erreurs après départ
    assert est_parcours_valide((6,6),(0,0),'SNN')==False
    assert est_parcours_valide((6,6),(0,0),'EOO')==False
    assert est_parcours_valide((6,6),(5,5),'NSS')==False
    assert est_parcours_valide((6,6),(5,5),'OEE')==False
    print('  OK')

def maximum_sur_parcours(carte,depart,chemin):
    dimensions = len(carte),len(carte[0])
    assert est_parcours_valide(dimensions,depart,chemin), 'Pre-condition'    
    
    h, w = dimensions
    pos = (depart[0], depart[1])
    max_alt = carte[pos[0]][pos[1]]
    for dir in chemin:
        pos = deplacer(pos, dir)
        alt = carte[pos[0]][pos[1]]
        if alt > max_alt:
            max_alt = alt
    
    return max_alt

def test_maximum_sur_parcours():
    print('Test de la fonction maximum_sur_parcours')
    carte = [
        [1, 1, 1, 2, 2],
        [1, 1, 2, 2, 2],
        [0, 1, 2, 2, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    # parcours : (0,2)->(0,1)->(1,1)->(2,1)->(2,0)->(3,0)->(4,0)->(4,1)->(3,1)->(3,2)->(3,3)
    assert maximum_sur_parcours(carte,(0,2),'OSSOSSENEE')==1
    # parcours : (4,4)->(4,3)->(4,2)->(4,1)->(4,0)->(3,0)->(2,0)
    assert maximum_sur_parcours(carte,(4,4),'OOOONN')==0
    # parcours : (4,2)->(4,3)->(3,3)->(3,4)->(2,4)->(2,3)->(3,3)
    assert maximum_sur_parcours(carte,(4,2),'ENENOS')==2
    print('  OK')

test_deplacer()
test_est_parcours_valide()
test_maximum_sur_parcours()