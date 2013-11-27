from info6 import Address

def test_shorten():
    a = Address('0000:0000:0000:0000:0000:0000:7f00:0001')
    b = Address(a.shorten())
    assert a.shorten() == '::7f00:1'
    assert b.fill_4byte_blocks() == '0000:0000:0000:0000:0000:0000:7f00:0001' 
    
