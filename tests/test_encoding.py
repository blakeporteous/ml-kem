from hypothesis import given, strategies as st
from mlkem.encoding import bits_to_bytes, bytes_to_bits


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
