from info6 import Address

def test_has_correct_syntax():
    a_correct = Address('::1')
    a_incorrect = Address('::000j')
    assert a_correct.has_correct_syntax() == True
    assert a_incorrect.has_correct_syntax() == False
