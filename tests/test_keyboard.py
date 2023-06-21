from src.keyboard import KeyBoard

import pytest

@pytest.fixture
def test_keyboard():
    return KeyBoard('ZetGaming', 5400, 3)

def test_init(test_keyboard):
    assert test_keyboard.name == 'ZetGaming'
    assert test_keyboard.price == 5400
    assert test_keyboard.quantity == 3
    assert test_keyboard.language == 'EN'

def test_change_lang(test_keyboard):
    assert test_keyboard.language == 'EN'
    test_keyboard.change_lang()
    assert test_keyboard.language == 'RU'
    test_keyboard.change_lang()
    assert test_keyboard.language == 'EN'