import pytest
import allure


@allure.step("Проверка длины строки")
def test_string_ln():
    test_string = "Если текст длиннее 15 символов"
    assert len(test_string) > 15, "Строка короче или равна 15 символов"