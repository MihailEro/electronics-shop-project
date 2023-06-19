"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

import pytest

from src.phone import Phone
@pytest.fixture
def test_item():
    return Item('phone', 100, 10)

@pytest.fixture()
def test_phone():
    return Phone("nokia", 23000, 1, 2)


def test_item_init(test_item):
    assert test_item.name == 'phone'
    assert test_item.price == 100
    assert test_item.quantity == 10


def test_item_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 1000


def test_item_apply_discount(test_item):
    Item.pay_rate = 0.9
    test_item.apply_discount()
    assert test_item.price == 90


def test_item_property(test_item):
    test_item.name = 'phone'
    assert test_item.name == 'phone'


def test_item_istantiate_from_csv(test_item):
    test_item.instantiate_from_csv()
    assert test_item.all[0].name == "Смартфон"
    assert test_item.all[0].price == "100"
    assert test_item.all[0].quantity == "1"


def test_string_to_number(test_item):
    assert test_item.string_to_number('1357') == 1357
    assert test_item.string_to_number('12.75') == 12


def test_item_repr():
    my_item = Item('компьютер', 100000, 15)
    assert repr(my_item) == "Item('компьютер', 100000, 15)"
def test_item_str():
    my_item = Item('компьютер', 100000, 15)
    assert  str(my_item) == 'компьютер'


def test_item_add(test_item, test_phone):
    assert test_item + test_phone == 11