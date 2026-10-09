
#bits to bytes
def bits_to_bytes(b):
    #check that it is a multiple of 8
    assert len(b) % 8 == 0
    #works out number of bits
    ell = len(b) // 8
    #creates a list of zeros of length ell
    B = [0] * ell
    #converts bits to bytes
    for i in range(8 * ell):
        B[i // 8] = B[i // 8] + b[i] * 2 ** (i % 8)
    return B

def bytes_to_bits(B):
    #number of bytes
    ell = len(B)
    #make a empty list for bits
    b = [0] * (8 * ell)
    #convert bytes to bits
    for i in range(8 * ell):
        b[i] = (B[i // 8] >> (i % 8)) & 1
    return b

#ML-KEM modulus
Q = 3329

def byte_encode(F, d):
    #checks its 256 numbers
    assert len(F) == 256
    #checks between 1-12
    assert 1 <= d <= 12
    #allowed range of numbers
    m = 2 ** d if d < 12 else Q
    assert all(0 <= a < m for a in F)
    #creates bits list 0's
    b = [0] * (256 * d)
    for i in range(256):
        for j in range(d):
            b[i * d + j] = (F[i] >> j) & 1
    return bits_to_bytes(b)

def byte_decode(B, d):
    assert 1 <= d <= 12
    assert len(B) == 32 * d
    m = 2 ** d if d < 12 else Q
    b = bytes_to_bits(B)
    F = [0] * 256
    for i in range(256):
        for j in range(d):
            F[i] = F[i] + b[i * d + j] * 2 ** j
        F[i] = F[i] % m
    return F
