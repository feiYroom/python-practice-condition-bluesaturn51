from exercises.absolute_value import absolute_value

def test_basic():
    assert absolute_value(5) == 5
    assert absolute_value(-5) == 5
    assert absolute_value(0) == 0
