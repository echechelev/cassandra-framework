import allure
import pytest

from . import data


@allure.id("CAS-01")
@allure.title("🚀 Успешная инициализация панели для пользователя 'AURORA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "system_initialization")
@allure.label("component", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.init
def test_successful_initialization_aurora(dashboard_page_aurora):
    """
    Сценарий:
    1. Наводим курсор на инфо панель 'Role Panel' до нажатия кнопки 'Uplink'.
    2. Проверяем: инфо панель содержит роль 'SPECIALIST'.
    3. Наводим курсор на инфо панель 'User Panel' до нажатия кнопки 'Uplink'
    4. Проверяем: инфо панель содержит имя 'AURORA'.
    5. Проверяем: элементы содержат класс 'panel-offline', не кликабельны, тултипы скрыты.
    """

    # ✅ ASSERT
    dashboard_page_aurora.verify_panels_data(
        expected_role=data.ROLE_SPECIALIST, expected_user=data.NAME_AURORA
    )
    dashboard_page_aurora.verify_panels_are_offline()


@allure.id("CAS-02")
@allure.title("🚀 Успешная инициализация панели для пользователя 'ORION'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "system_initialization")
@allure.label("component", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.init
def test_successful_initialization_orion(dashboard_page_orion):
    """
    Сценарий:
    1. Наводим курсор на инфо панель 'Role Panel' до нажатия кнопки 'Uplink'.
    2. Проверяем: инфо панель содержит роль 'COMMANDER'.
    3. Наводим курсор на инфо панель 'User Panel' до нажатия кнопки 'Uplink'
    4. Проверяем: инфо панель содержит имя 'ORION'.
    5. Проверяем: элементы содержат класс 'panel-offline', не кликабельны, тултипы скрыты.
    """

    # ✅ ASSERT
    dashboard_page_orion.verify_panels_data(
        expected_role=data.ROLE_COMMANDER, expected_user=data.NAME_ORION
    )
    dashboard_page_orion.verify_panels_are_offline()


@allure.id("CAS-03")
@allure.title("🚫 Редирект при отсутствии данных в localStorage")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "system_initialization")
@allure.label("component", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.init
def test_access_denied_redirect_on_empty_storage(dashboard_page_unauthorized):
    """
    Сценарий:
    1. Открываем Dashboard Page с пустым localStorage.
    2. Проверяем: телеметрия становится красной '> ACCESS DENIED. REDIRECTING...'.
    3. Через 1.5 сек происходит автоматический редирект на login.html.
    """
    # ✅ ASSERT
    dashboard_page_unauthorized.verify_telemetry_text(
        expected_text=data.TELEMETRY_ACCESS_DENIED_REDIRECT
    )
    dashboard_page_unauthorized.verify_telemetry_color_with_cassandra(red=True)
    dashboard_page_unauthorized.verify_redirect_to_login()
    dashboard_page_unauthorized.verify_currentuser_dashboard_keys_cleared()


@allure.id("CAS-04")
@allure.title("⚠️ Корректная обработка поврежденных данных в 'localStorage'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "system_initialization")
@allure.label("component", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.init
def test_redirect_on_corrupted_storage_data(dashboard_page_corrupted):
    """
    Сценарий:
    1. Устанавливаем в localStorage невалидный JSON под ключом 'currentUser'.
    2. Открываем Dashboard Page.
    3. Проверяем: телеметрия отображает красным цыетом '> DATA CORRUPTED. REDIRECTING...'.
    4. Проверяем: через 1.5 сек происходит редирект на login.html.
    5. Проверяем: ключ 'currentUser' удалён из localStorage.
    """

    # ✅ ASSERT
    dashboard_page_corrupted.verify_telemetry_text(
        expected_text=data.TELEMETRY_DATA_CORRUPTED_REDIRECT
    )
    dashboard_page_corrupted.verify_telemetry_color_with_cassandra(red=True)
    dashboard_page_corrupted.verify_redirect_to_login()
    dashboard_page_corrupted.verify_currentuser_dashboard_keys_cleared()
