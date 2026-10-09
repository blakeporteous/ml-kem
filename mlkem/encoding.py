
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

