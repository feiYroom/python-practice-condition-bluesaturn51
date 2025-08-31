from exercises.min_of_three import min_of_three

def test_basic():
    assert min_of_three(3, 2, 1) == 1
    assert min_of_three(0, 0, 5) == 0
    assert min_of_three(-1, -2, -3) == -3
