def somme_chiffres(n):
    assert n>=0, 'Pré-condition'
    resultat = 0
    while n > 0:
        v_debut = n
        assert n >= 0, 'Variant (positif)'
        resultat += n % 10
        n //= 10
        v_fin = n
        assert v_fin < v_debut, 'Variant (décroissant)'
    return resultat


def test_somme_chiffres():
    print('Test de la fonction somme_chiffres')
    assert somme_chiffres(1) == 1
    assert somme_chiffres(0) == 0
    assert somme_chiffres(123) == 6
    assert somme_chiffres(123456789) == 45
    print('  OK')


test_somme_chiffres()