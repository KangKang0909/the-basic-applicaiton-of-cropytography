from math import gcd
def find_coprimes(c):
    coprimes = []
    for x in range(c):
        if gcd(x, c) == 1:
            coprimes.append(x)
    return coprimes

print(find_coprimes(72))