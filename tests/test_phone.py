import pytest

from src.phone import Phone


@pytest.fixture()
def test_phone():
    return Phone("nokia", 23000, 1, 2)

def test_phone_init(test_phone):
    assert test_phone.name == "nokia"
    assert test_phone.price == 23000
    assert test_phone.quantity == 1
    assert test_phone.number_of_sim == 2

def test_phone_repr(test_phone):
    assert repr(test_phone) == "Phone('nokia', 23000, 1, 2)"

def test_phone_number_of_sim(test_phone):
    assert test_phone.number_of_sim == 2