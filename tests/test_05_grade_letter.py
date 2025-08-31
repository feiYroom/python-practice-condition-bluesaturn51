from exercises.grade_letter import grade_letter

def test_boundaries():
    assert grade_letter(90) == 'A'
    assert grade_letter(89) == 'B'
    assert grade_letter(80) == 'B'
    assert grade_letter(79) == 'C'
    assert grade_letter(70) == 'C'
    assert grade_letter(69) == 'D'
    assert grade_letter(60) == 'D'
    assert grade_letter(59) == 'F'
