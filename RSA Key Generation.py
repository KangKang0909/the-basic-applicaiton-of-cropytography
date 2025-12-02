import random
import math


def generate_rsa_keys(p, q):
    """
    Generates RSA public and private keys based on two prime numbers p and q.
    """
    # 1. Compute n (modulus)
    n = p * q

    # 2. Compute Euler's Totient function phi(n)
    phi = (p - 1) * (q - 1)

    # 3. Choose public exponent e
    # e must be coprime to phi and 1 < e < phi.
    # 65537 is the industry standard (efficient for encryption).
    e = 65537

    # Verify e is coprime to phi (gcd should be 1)
    if math.gcd(e, phi) != 1:
        raise ValueError("e and phi are not coprime. Choose different primes.")

    # 4. Compute private exponent d
    # d is the modular multiplicative inverse of e modulo phi
    # formula: d * e ≡ 1 (mod phi)
    # Python 3.8+ allows negative exponents in pow() for modular inverse
    d = pow(e, -1, phi)

    return (e, n), (d, n)


# --- Example Usage ---
# Note: In production, use large random primes (e.g., 2048-bit)
prime1 = 61
prime2 = 53

public_key, private_key = generate_rsa_keys(prime1, prime2)

print(f"Primes: p={prime1}, q={prime2}")
print(f"Public Key (e, n): {public_key}")
print(f"Private Key (d, n): {private_key}")