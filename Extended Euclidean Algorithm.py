def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y
def EE(a, m):
    gcd, x, _ = egcd(a, m)
    if gcd == 1:
        return x % m
    return None # modular inverse does not exist
# Find the inverse of 5 mod 72
b = EE(5, 72)
print(b)