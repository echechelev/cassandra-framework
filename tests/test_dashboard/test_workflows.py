import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🚀 Полная последовательность активации 'Uplink'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.workflows
def test_full_uplink_activation_sequence(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    4. Проверить: кнопка 'Uplink Button' становится неактивной, серой, теряет пульсацию.
    5. Проверить: кнопка 'Logout' и 5 центральных кнопок приобретают класс 'panel-online', кликабельные,
    яркие с неоновым свечением.
    6. Проверить: 'Role Panel' и 'User Panel' переключаются в 'panel-online'.
    7. Проверить: текст 'Telemetry' становится зеленым и содержит фразу 'SYSTEM READY FOR WORK'.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ⚡ ACT
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ✅ ASSERT
    dashboard_page_aurora.verify_uplink_button_disabled()
    dashboard_page_aurora.verify_uplink_buttons_activated()
    dashboard_page_aurora.verify_telemetry_color_with_cassandra(green=True)
    dashboard_page_aurora.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_SYSTEM_READY_AURORA
    )


@allure.id("CAS-02")
@allure.title("🌑 Успешный выход из системы для 'AURORA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.workflows
def test_logout_aurora_success(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    4. Нажать на кнопку 'Logout Button'.
    5. Проверить: ключ currentUser из 'sessionStorage' удален.
    6. Проверить: открывается страница 'login.html'.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ⚡ ACT
    dashboard_page_aurora.click_logout()

    # ✅ ASSERT
    dashboard_page_aurora.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_AURORA, check_session=True, should_exist=False
    )
    dashboard_page_aurora.wait_for_url(expected_url_part=data.LOGIN_URL)


@allure.id("CAS-03")
@allure.title("🌑 Успешный выход из системы для 'ORION'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.workflows
def test_logout_orion_success(dashboard_page_orion):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'ORION''.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    4. Нажать на кнопку 'Logout Button'.
    5. Проверить: ключ currentUser из 'sessionStorage' удален.
    6. Проверить: открывается страница 'login.html'.
    """

    # 🎬 ARRANGE
    dashboard_page_orion.click_uplink()
    dashboard_page_orion.wait_for_uplink_complete(callsign=data.CALLSIGN_ORION)

    # ⚡ ACT
    dashboard_page_orion.click_logout()

    # ✅ ASSERT
    dashboard_page_orion.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_ORION, check_session=True, should_exist=False
    )
    dashboard_page_orion.wait_for_url(expected_url_part=data.LOGIN_URL)


@allure.id("CAS-04")
@allure.title("🌑 Успешный выход из системы для 'NOVA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.workflows
def test_logout_nova_success(dashboard_page_nova):
    """
    Сценарий:
    1. Перейти на страницу 'Signup Page' и создать пользователя 'NOVA'.
    2. Выполнить авторизацию под пользователем 'NOVA'.
    3. Перейти на страницу 'Dashboard Page'.
    4. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    5. Нажать на кнопку 'Logout Button'.
    6. Проверить: ключ currentUser из 'sessionStorage удален'.
    7. Проверить: ключ 'registeredUsers' из 'localStorage' остался.
    8. Проверить: открывается страница 'login.html'.
    """

    # 🎬 ARRANGE
    dashboard_page_nova.click_uplink()
    dashboard_page_nova.wait_for_uplink_complete(callsign=data.CALLSIGN_NOVA)

    # ⚡ ACT
    dashboard_page_nova.click_logout()

    # ✅ ASSERT
    dashboard_page_nova.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_NOVA, check_session=True, should_exist=False
    )
    dashboard_page_nova.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_NOVA, check_local=True, should_exist=True
    )
    dashboard_page_nova.wait_for_url(expected_url_part=data.LOGIN_URL)


@allure.id("CAS-05")
@allure.title("🌑 Успешный выход из системы для 'KNOPA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.workflows
def test_logout_knopa_success(dashboard_page_knopa):
    """
    Сценарий:
    1. Перейти на страницу 'Restore page' и восстановить доступ пользователю 'KNOPA'.
    2. Выполнить авторизацию под пользователем 'KNOPA''
    3. Перейти на страницу 'Dashboard Page'.
    4. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    5. Нажать на кнопку 'Logout Button'.
    6. Проверить: ключ currentUser из 'sessionStorage удален'.
    7. Проверить: ключ restoredUsers из 'localstorage' остался.
    8. Проверить: открывается страница 'login.html'.
    """

    # 🎬 ARRANGE
    dashboard_page_knopa.click_uplink()
    dashboard_page_knopa.wait_for_uplink_complete(callsign=data.CALLSIGN_KNOPA)

    # ⚡ ACT
    dashboard_page_knopa.click_logout()

    # ✅ ASSERT
    dashboard_page_knopa.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_KNOPA, check_session=True, should_exist=False
    )
    dashboard_page_knopa.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_KNOPA, check_local=True, should_exist=True
    )
    dashboard_page_knopa.wait_for_url(expected_url_part=data.LOGIN_URL)


@allure.id("CAS-06")
@allure.title("🔄  Корректная переинициализация дашборда при восстановлении из bfcache")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.workflows
def test_bfcache_restore_reinitialization(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink' и дождаться полной инициализации (100%).
    4. Нажать на кнопку 'Galaxy Map'.
    5. Нажать кнопку 'Назад' в браузере.
    6. Проверить: в 'sessionStorage' присутствует ключ 'currentUser'.
    7. Проверить: кнопки 'Planet Bar' активны (имеют класс 'panel-online').
    8. Проверить: текст телеметрии содержит 'SYSTEM READY FOR WORK'.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ⚡ ACT
    dashboard_page_aurora.click_galaxy_map()
    dashboard_page_aurora.click_browser_back()

    # ✅ ASSERT
    dashboard_page_aurora.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_AURORA, check_session=True, should_exist=True
    )
    dashboard_page_aurora.verify_uplink_buttons_activated()
    dashboard_page_aurora.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_SYSTEM_READY_AURORA
    )
