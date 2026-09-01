import allure
import pytest


@allure.id("CAS-06")
@allure.title("🖱️ Валидация 'hover'-эффекта кнопки")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.visuals
def test_validate_button_hover_effect(index_page):
    """
    Сценарий:
    1. Навести курсор на кнопку 'Log in'.
    2. Проверяем: 'CSS-свойство 'transform' меняется на 'scale(1.15)'.
    3. Проверяем: свойство `border-color` становится ярче (rgba(77, 166, 255, 1)).
    """

    # ⚡ ACT
    index_page.hover_log_in()

    # ✅ ASSERT
    index_page.verify_log_in_hover_effects()


@allure.id("CAS-07")
@allure.title("💓 Проверка наличия и параметров анимации ЭКГ в DOM")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.visuals
def test_validate_ecg_animation_in_dom(index_page):
    """
    Сценарий:
    1. Навести курсор на кнопку 'Log in'.
    2. Проверяем: 'CSS-свойство 'transform' меняется на 'scale(1.15)'.
    3. Проверяем: свойство `border-color` становится ярче (rgba(77, 166, 255, 1)).
    """

    # ✅ ASSERT
    index_page.verify_ecg_animation_in_dom()
