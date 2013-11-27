from info6 import Address

def test_convert_decimal_notation():
    a = Address('0000:0000:0000:0000:0000:0000:127.0.0.1')
    assert a.convert_decimal_notation() == '0000:0000:0000:0000:0000:0000:7f00:0001' 
