#!/usr/bin/python3

def chat_attrape_souris_1(chaine):
    pos_c = -1
    pos_s = -1
    for i in range(len(chaine)):
        char = chaine[i]
        if char == "C":
            pos_c = i
        elif char == "s":
            pos_s = i
    return abs(pos_c - pos_s) <= 4
            

def test_chat_attrape_souris_1():
    print('Test de la fonction chat_attrape_souris_1')
    assert chat_attrape_souris_1('C....s')==False
    assert chat_attrape_souris_1('C..s')==True
    assert chat_attrape_souris_1('C.....s')==False
    assert chat_attrape_souris_1('C.s')==True
    assert chat_attrape_souris_1('s...C')==True 
    assert chat_attrape_souris_1('s..........C')==False
    assert chat_attrape_souris_1('........s..........C....')==False
    assert chat_attrape_souris_1('.......C.s............')==True
    print('  OK')


def chat_attrape_souris_2(chaine, saut):
    pos_c = -1
    pos_s = -1
    for i in range(len(chaine)):
        char = chaine[i]
        if char == "C":
            pos_c = i
        elif char == "s":
            pos_s = i
    if pos_c == -1 or pos_s == -1:
        return False
    return abs(pos_c - pos_s) <= saut

def test_chat_attrape_souris_2():
    print('Test de la fonction chat_attrape_souris_2')
    assert chat_attrape_souris_2('C....s',4)==False
    assert chat_attrape_souris_2('C....s',5)==True
    assert chat_attrape_souris_2('C....s',6)==True
    assert chat_attrape_souris_2('C..s',2)==False
    assert chat_attrape_souris_2('C..s',3)==True
    assert chat_attrape_souris_2('C..s',4)==True
    assert chat_attrape_souris_2('...C...s....',3)==False
    assert chat_attrape_souris_2('....C..s....',3)==True
    assert chat_attrape_souris_2('.....C.s....',3)==True
    assert chat_attrape_souris_2('...s...C....',3)==False
    assert chat_attrape_souris_2('...s..C.....',3)==True
    assert chat_attrape_souris_2('...s.C......',3)==True
    assert chat_attrape_souris_2('...................C....',1)==False
    assert chat_attrape_souris_2('...........s............',1)==False
    assert chat_attrape_souris_2('........................',1)==False
    print('  OK')

test_chat_attrape_souris_1()
test_chat_attrape_souris_2()