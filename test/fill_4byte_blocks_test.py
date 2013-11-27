from info6 import Address

def test_fill_4byte_blocks():
    a = Address('::1')
    assert a.fill_4byte_blocks() == '0000:0000:0000:0000:0000:0000:0000:0001'
