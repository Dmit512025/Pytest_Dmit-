from SFC.Calculator import add

def test_add_equal_numbers_different_signs():
    assert add(-5, 5) == 0
def test_add_positiv_numbers():
    assert add(5, 7) == 12
def test_negativ_numbers():
    assert add(-5, -7) == -12