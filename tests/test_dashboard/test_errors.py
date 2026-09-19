import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🚫 Редирект при отсутствии данных в sessionStorage")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.errors_ui
def test_access_denied_redirect_on_empty_storage(dashboard_page):
    """
    Сценарий:
    1. Перейти на страницу 'Dashboard Page'.
    2. Проверить: текст телеметрии становится красным и содержит '> ACCESS DENIED. REDIRECTING...'
    3. Проверить: через 1.5 сек происходит автоматический редирект на 'login.html'.
    """
    # ✅ ASSERT
    dashboard_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_ACCESS_DENIED)
    dashboard_page.verify_telemetry_color_with_cassandra(red=True)
    dashboard_page.wait_for_url(expected_url_part=data.LOGIN_URL)


@allure.id("CAS-02")
@allure.title("💥  Обработка поврежденных данных в 'sessionStorage'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.errors_ui
def test_redirect_corrupted_session(login_page, dashboard_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Установить в sessionStorage невалидный JSON под ключом 'currentUser'.
    3. Перейти на страницу 'Dashboard Page'.
    4. Проверить: телеметрия отображает красным цветом '> DATA CORRUPTED. REDIRECTING...'.
    5. Проверить: через 1.5 сек происходит редирект на login.html.
    6. Проверить: ключ 'currentUser' удалён из 'sessionStorage'.
    """

    # ⚡ ACT
    login_page.set_corrupted_user_data(check_session=True)

    # ✅ ASSERT
    dashboard_page.verify_telemetry_text(
        expected_text=data.RED_TELEMETRY_DATA_CORRUPTED
    )
    dashboard_page.verify_telemetry_color_with_cassandra(red=True)
    dashboard_page.wait_for_url(expected_url_part=data.LOGIN_URL)
    dashboard_page.verify_user_data_in_storage(check_session=True, should_exist=False)


@allure.id("CAS-03")
@allure.title("🔙 Защита от восстановления сессии через кнопку 'Назад' после 'Logout'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.errors_ui
def test_logout_protection_via_browser_back(dashboard_page_aurora):
    """
    Сценарий:
    1. Проверить: ключ 'currentUser' в 'sessionStorage' отсутствует (null).
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    4. Нажать на кнопку 'Logout Button' и дождаться редиректа на 'login.html' .
    5. Нажать кнопку 'Назад' в браузере.
    6. Проверить: пользователь остаётся на 'login.html'.
    7. Проверить: ключ 'currentUser' в 'sessionStorage' отсутствует.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ⚡ ACT
    dashboard_page_aurora.logout_btn.click()
    dashboard_page_aurora.wait_for_url(expected_url_part=data.LOGIN_URL)
    dashboard_page_aurora.click_browser_back()

    # ✅ ASSERT
    dashboard_page_aurora.wait_for_url(expected_url_part=data.LOGIN_URL)
    dashboard_page_aurora.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_AURORA, check_session=True, should_exist=False
    )


@allure.id("CAS-04")
@allure.title("🛡️ Защита от спама кликов по кнопке `Uplink`")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.errors_ui
def test_uplink_spam_click_protection(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Выполнить 3 последовательных клика по кнопке 'Uplink'.
    4. Проверить: проходит только 1 клик, кнопка становится неактивной.
    5. Проверить: контейнер прогресс-бара появился только один раз.
    """
    # ⚡ ACT
    dashboard_page_aurora.spam_click_diagnostics()

    # ✅ ASSERT
    dashboard_page_aurora.verify_progress_bar_appeared_once()
    dashboard_page_aurora.verify_uplink_button_disabled()
