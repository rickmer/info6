from info6 import Address

def test_add_missing_blocks():
    a = Address('::0001')
    assert a.add_missing_blocks() == '0000:0000:0000:0000:0000:0000:0000:0001'
