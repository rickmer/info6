from info6 import address

def test_has_correct_syntax():
    a_correct = address('::1')
    a_incorrect = address('::000j')
    assert a_correct.has_correct_syntax() == True
    assert a_incorrect.has_correct_syntax() == False
