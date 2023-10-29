import random
from math import gcd as bltin_gcd
def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

def nod(a, b):
    if b > a:
        a, b = b, a
    U = [a, 1, 0]
    V = [b, 0, 1]
    while V[0] != 0:
        q = U[0] // V[0]
        T = [U[0] % V[0], U[1] - q * V[1], U[2] - q * V[2]]
        U = V
        V = T
    return U[0]


def coprime2(a, b):
    return bltin_gcd(a, b) == 1
def RSA():
    p = int(random.randint(1, 1000000000))
    while not is_prime(p):
        p = int(random.randint(0, 1000000000))
    q = int(random.randint(1, 1000000000))
    while not is_prime(q):
        q = int(random.randint(0, 1000000000))
    N = p * q
    f = (p - 1) * (q - 1)
    d = int(random.randint(1, 1000000000))
    while not coprime2(d, f):
        d = int(random.randint(1, 1000000000))
    c = pow(d, -1, f)
    return c, d, N
