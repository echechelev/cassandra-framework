import allure
import pytest

from . import data


@allure.id("CAS-04")
@allure.title("🧭 Успешная навигация на страницу 'Login'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.navigation
def test_successful_navigation_to_login_page(index_page):
    """
    Сценарий:
    1. Кликнуть на кнопку 'Log in'.
    2. Проверяем: открылась страница логина и проверить ее url.
    """

    # ⚡ ACT
    index_page.click_log_in()

    # ✅ ASSERT
    index_page.verify_current_url(expected_url_part=data.LOGIN)


@allure.id("CAS-05")
@allure.title("🧭 Успешная навигация на страницу 'Signup'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.navigation
def test_successful_navigation_to_signup_page(index_page):
    """
    Сценарий:
    1. Кликнуть на кнопку 'Sign up'.
    2. Проверяем: открылась страница регистрации и проверить ее url.
    """

    # ⚡ ACT
    index_page.click_sign_up()

    # ✅ ASSERT
    index_page.verify_current_url(expected_url_part=data.SIGNUP)