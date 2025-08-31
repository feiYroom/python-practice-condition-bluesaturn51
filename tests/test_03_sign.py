from exercises.sign import sign

def test_basic():
    assert sign(3) == 'positive'
    assert sign(-1) == 'negative'
    assert sign(0) == 'zero'
