import allure
import pytest

from tests import data


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
    index_page.verify_current_url(expected_url_part=data.LOGIN_URL)


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
    index_page.verify_current_url(expected_url_part=data.SIGNUP_URL)


@allure.id("CAS-06")
@allure.title("🧭 Успешная навигация на страницу 'Access Restoration'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.navigation
def test_successful_navigation_to_access_restoration_page(index_page):
    """
    Сценарий:
    1. Кликнуть на кнопку 'Restore'.
    2. Проверяем: открылась страница востановления и проверить ее url.
    """

    # ⚡ ACT
    index_page.click_restore()

    # ✅ ASSERT
    index_page.verify_current_url(expected_url_part=data.ACCESS_RESTORATION_URL)


@allure.id("CAS-07")
@allure.title("🔄 Автоматический редирект на дашборд при наличии активной сессии")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.navigation
def test_redirect_to_dashboard_with_active_session(dashboard_page_aurora):
    """
    Сценарий:
    1. Принудительно перейти по URL главной страницы 'index.html'.
    2. Проверяем: редирект сработал, url содержит 'dashboard.html'.
    """

    # ⚡ ACT
    dashboard_page_aurora.open_url(path=data.INDEX_URL)

    # ✅ ASSERT
    dashboard_page_aurora.verify_current_url(expected_url_part=data.DASHBOARD_URL)