import math

def sqrt_dichotomie_march_pas(n: int) -> int:
    a = 0
    b = n+1
    m = 0
    while a < b:
        m = (a + b) // 2
        if n < m*m:
            b = m 
        else:
            a = m
    return m

def sqrt(n: int) -> int:
    x = 0
    while x*x < n:
        x += 1
    return x

def test_sqrt():
    for i in range(200):
        print(sqrt(i), math.sqrt(i))