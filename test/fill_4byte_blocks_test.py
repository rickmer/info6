from info6 import address

def test_fill_4byte_blocks():
    a = address('::1')
    assert a.fill_4byte_blocks() == '0000:0000:0000:0000:0000:0000:0000:0001'
