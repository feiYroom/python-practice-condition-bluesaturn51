from exercises.fizz_label import fizz_label

def test_vals():
    assert fizz_label(1) == '1'
    assert fizz_label(3) == 'Fizz'
    assert fizz_label(5) == 'Buzz'
    assert fizz_label(15) == 'FizzBuzz'
    assert fizz_label(16) == '16'
