import random
from hypothesis import given, strategies as st
from mlkem.encoding import bits_to_bytes, bytes_to_bits, byte_encode, byte_decode, Q


def test_bits_to_bytes_example():
    bits = [0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0]
    assert bits_to_bytes(bits) == [128, 1]


def test_bits_to_bytes_single_byte():
    assert bits_to_bytes([1,0,1,1,0,0,0,0]) == [13]


def test_bytes_to_bits_example():
    assert bytes_to_bits([13]) == [1,0,1,1,0,0,0,0]


def test_bytes_to_bits_two_bytes():
    assert bytes_to_bits([128, 1]) == [0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0]


@given(st.lists(st.integers(0, 255)))
def test_roundtrip(B):
    assert bits_to_bytes(bytes_to_bits(B)) == B


def test_byte_encode_example():
    F = [5, 3] + [0] * 254
    B = byte_encode(F, 4)
    assert len(B) == 32 * 4
    assert B[0] == 53
    assert all(x == 0 for x in B[1:])


def test_byte_encode_sizes():
    for d in range(1, 13):
        assert len(byte_encode([0] * 256, d)) == 32 * d


def test_byte_decode_example():
    B = byte_encode([5, 3] + [0] * 254, 4)
    assert byte_decode(B, 4)[:2] == [5, 3]


def test_byte_roundtrip_all_d():
    for d in range(1, 12):
        F = [random.randrange(2 ** d) for _ in range(256)]
        assert byte_decode(byte_encode(F, d), d) == F
    F = [random.randrange(Q) for _ in range(256)]
    assert byte_decode(byte_encode(F, 12), 12) == F


def test_byte_decode_reduces_mod_q():
    B = bits_to_bytes([1] * (256 * 12))
    assert byte_decode(B, 12) == [4095 % Q] * 256
