from info6 import address

def test_add_missing_blocks():
    a = address('::0001')
    assert a.add_missing_blocks() == '0000:0000:0000:0000:0000:0000:0000:0001'
