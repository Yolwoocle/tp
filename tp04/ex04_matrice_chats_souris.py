#!/usr/bin/python3

def chat_attrape_souris(carte, saut):
    pos_c = None
    pos_s = None
    for i in range(len(carte)):
        for j in range(len(carte[0])):
            if carte[i][j] == "C":
                pos_c = (i, j)
            elif carte[i][j] == "s":
                pos_s = (i, j)
    
    if pos_c == None or pos_s == None:
        return False
    
    dist = abs(pos_c[0] - pos_s[0]) + abs(pos_c[1] - pos_s[1])
    return dist <= saut

def test_chat_attrape_souris():
    print('Test de la fonction chat_attrape_souris')
    assert chat_attrape_souris(['..C...s..'], 5)==True
    assert chat_attrape_souris(['..s...C..'], 5)==True
    assert chat_attrape_souris(['..C...s..'], 2)==False
    assert chat_attrape_souris(['..s...C..'], 2)==False
    assert chat_attrape_souris(['..C......', '.........', '....s....'], 5)==True
    assert chat_attrape_souris(['..C......', '.........', '....s....'], 3)==False
    assert chat_attrape_souris(['.C.......', '.........', '......s..'], 5)==False
    assert chat_attrape_souris(['..C......', '.........', '.........'], 5)==False
    assert chat_attrape_souris(['..s......', '.........', '.........'], 5)==False
    print('  OK')

test_chat_attrape_souris()