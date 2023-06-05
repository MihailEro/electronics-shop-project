"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

import pytest

@pytest.fixture
def test_item():
    return Item('phone', 100, 10)


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