from exercises.is_leap_year import is_leap_year

def test_cases():
    assert is_leap_year(2000) is True   # divisible by 400
    assert is_leap_year(1900) is False  # divisible by 100, not leap
    assert is_leap_year(2024) is True   # divisible by 4, not by 100
    assert is_leap_year(2023) is False
