from exercises.max_of_two import max_of_two

def test_basic():
    assert max_of_two(3, 5) == 5
    assert max_of_two(10, -10) == 10
    assert max_of_two(7, 7) == 7
