from exercises.ticket_price import ticket_price

def test_ages():
    assert ticket_price(5) == 5
    assert ticket_price(12) == 5
    assert ticket_price(13) == 10
    assert ticket_price(30) == 10
    assert ticket_price(64) == 10
    assert ticket_price(65) == 7
    assert ticket_price(80) == 7
