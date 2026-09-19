import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🧭 Успешная навигация на страницу 'Login'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.interactions
def test_successful_navigation_to_login_page(index_page):
    """
    Сценарий:
    1. Перейти на страницу 'Index page'.
    2. Нажать на кнопку 'Log in'.
    3. Проверить: происходит навигация на страницу логина, url 'login.html'.
    """

    # ⚡ ACT
    index_page.click_log_in()

    # ✅ ASSERT
    index_page.wait_for_url(expected_url_part=data.LOGIN_URL)


@allure.id("CAS-02")
@allure.title("🧭 Успешная навигация на страницу 'Signup'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.interactions
def test_successful_navigation_to_signup_page(index_page):
    """
    Сценарий:
    1. Перейти на страницу 'Index page'.
    2. Нажать на кнопку 'Sign up'.
    3. Проверить: происходит навигация на страницу регистрации, url 'signup.html'.
    """

    # ⚡ ACT
    index_page.click_sign_up()

    # ✅ ASSERT
    index_page.wait_for_url(expected_url_part=data.SIGNUP_URL)


@allure.id("CAS-03")
@allure.title("🧭 Успешная навигация на страницу 'Access Restoration'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.interactions
def test_successful_navigation_to_access_restoration_page(index_page):
    """
    Сценарий:
    1. Перейти на страницу 'Index page'.
    2. Нажать на кнопку 'Restore'.
    3. Проверить: происходит навигация на страницу восстановления, url 'access-restoration.html'.
    """

    # ⚡ ACT
    index_page.click_restore()

    # ✅ ASSERT
    index_page.wait_for_url(expected_url_part=data.ACCESS_RESTORATION_URL)


@allure.id("CAS-04")
@allure.title("🖱️ Валидация 'hover'-эффекта кнопки")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.interactions
def test_validate_button_hover_effect(index_page):
    """
    Сценарий:
    1. Перейти на страницу 'Index page'.
    2. Навести курсор на кнопку 'Log in'.
    3. Проверить: CSS-свойство 'transform' меняется на 'scale(1.15)'.
    4. Проверить: свойство `border-color` становится ярче (rgba(77, 166, 255, 1)).
    """

    # ⚡ ACT
    index_page.hover_log_in()

    # ✅ ASSERT
    index_page.verify_log_in_hover_effects()


@allure.id("CAS-05")
@allure.title("💓 Проверка наличия и параметров анимации ЭКГ в DOM")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.interactions
def test_validate_ecg_animation_in_dom(index_page):
    """
    Сценарий:
    1. Перейти на страницу 'Index page'.
    2. Найти элементы с классом '.heartbeat-path'.
    3. Проверить: элементов 2 штуки (.heartbeat-blue и .heartbeat-white).
    4. Проверить: CSS-свойство 'animation-name' равно 'drawHeartbeat'.
    5. Проверить: CSS-свойство 'animation-duration' равно '15s'.
    """

    # ✅ ASSERT
    index_page.verify_ecg_animation_in_dom()
