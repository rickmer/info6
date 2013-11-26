from info6 import address

def test_shorten():
    a = address('0000:0000:0000:0000:0000:0000:7f00:0001')
    b = address(a.shorten())
    assert a.shorten() == '::7f00:1'
    assert b.fill_4byte_blocks() == '0000:0000:0000:0000:0000:0000:7f00:0001' 
    
