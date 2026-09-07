import allure
import pytest
from selene import browser

from tests import data


@allure.id("CAS-12")
@allure.title("💡 Динамическая подстановка данных в тултипы для 'AURORA'.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.actions
def test_tooltips_display_dynamic_data_aurora(dashboard_page_aurora):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'. Дождидаемся завершения анимации (100%).
    2. Наводим курсор мыши 'ActionChains' на 'Role Panel' и 'User Panel'.
    4. Проверяем: Тултип `Role Panel` отображает текст `Access: Level 2`.
    5. Тултип `User Panel` отображает текст `ID: `884-2A`.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ⚡ ACT
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ✅ ASSERT
    dashboard_page_aurora.verify_tooltips_dynamic_data(data.USER_AURORA)


@allure.id("CAS-13")
@allure.title("💡 Динамическая подстановка данных в тултипы для 'ORION'.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.actions
def test_tooltips_display_dynamic_data_orion(dashboard_page_orion):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'. Дождидаемся завершения анимации (100%).
    2. Наводим курсор мыши 'ActionChains' на 'Role Panel' и 'User Panel'.
    4. Проверяем: Тултип `Role Panel` отображает текст `Access: Level 1`.
    5. Тултип `User Panel` отображает текст `ID: `001-1A`.
    """

    # 🎬 ARRANGE
    dashboard_page_orion.click_uplink()

    # ⚡ ACT
    dashboard_page_orion.wait_for_uplink_complete(callsign=data.CALLSIGN_ORION)

    # ✅ ASSERT
    dashboard_page_orion.verify_tooltips_dynamic_data(data.USER_ORION)


@allure.id("CAS-14")
@allure.title("🚀 Динамическая подстановка данных в тултипы для 'NOVA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.actions
def test_tooltips_display_dynamic_data_nova(nova_created, dashboard_page_selectors):
    """
    Сценарий:
    1. Создаем пользователя 'Nova' и заходим на дашборд.
    2. Нажимаем на кнопку на 'Uplink Button'. Дождидаемся завершения анимации (100%).
    3. Наводим курсор мыши 'ActionChains' на 'Role Panel' и 'User Panel'.
    4. Проверяем: Тултип `Role Panel` отображает текст `Access: Level 3`.
    5. Тултип `User Panel` отображает текст `ID: `512-3A`.
    6. Удаляем пользователя 'NOVA'.
    """

    # 🎬 ARRANGE
    nova_created.click_launch_dashboard()
    dashboard_page_selectors.click_uplink()

    # ⚡ ACT
    dashboard_page_selectors.wait_for_uplink_complete(callsign=data.CALLSIGN_NOVA)

    # ✅ ASSERT
    dashboard_page_selectors.verify_tooltips_dynamic_data(data.USER_NOVA)

    # 🧹 TEARDOWN
    nova_created.delete_operator_from_storage(callsign=data.CALLSIGN_NOVA)


@allure.id("CAS-15")
@allure.title("🖱️ Hover-эффект кнопки Logout в активном состоянии.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.actions
def test_logout_button_hover_effect(dashboard_page_aurora):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'. Дожидаемся завершения анимации (100%).
    2. Наводим курсор мыши на кнопку 'Logout Button'.
    3. Проверяем: rнопка увеличивается в размере `transform: scale 1.15`.
    4. Проверяем: рамка и свечение становятся ярче. Курсор меняется на 'pointer'.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ⚡ ACT
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ✅ ASSERT
    dashboard_page_aurora.verify_logout_button_hover_effect()


@allure.id("CAS-16")
@allure.title("🔌 Успешный выход из системы 'Happy Path Logout' 'AVRORA'.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.actions
def test_happy_path_logout_aurora(dashboard_page_aurora):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'. Дожидаемся завершения анимации (100%).
    2. Нажать на кнопку 'Logout Button'.
    3. Проверяем: ключь currentUser из 'sessionstorage' удален.
    4. Проверяем: открывается страница '/login.html'
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ⚡ ACT
    dashboard_page_aurora.click_logout()

    # ✅ ASSERT
    dashboard_page_aurora.verify_storage_cleared(
        expected_callsign=data.CALLSIGN_AURORA,
        check_session=True,
    )
    dashboard_page_aurora.verify_current_url(expected_url_part=data.LOGIN_URL)


@allure.id("CAS-17")
@allure.title("🔌 Успешный выход из системы 'Happy Path Logout' 'NOVA'.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.actions
def test_happy_path_logout_nova(nova_created, dashboard_page_selectors):
    """
    Сценарий:
    1. Создаем пользователя 'Nova' и заходим на дашборд.
    2. Нажимаем на кнопку на 'Uplink Button'. Дожидаемся завершения анимации (100%).
    3. Нажать на кнопку 'Logout Button'.
    4. Проверяем: ключь currentUser из 'sessionstorage удален'.
    5. Проверяем: ключь registeredUsers из 'loginstorage' остался.
    6. Проверяем: открывается страница '/login.html'
    7. Удаляем пользователя 'NOVA'.
    """

    # 🎬 ARRANGE
    nova_created.click_launch_dashboard()
    dashboard_page_selectors.click_uplink()
    dashboard_page_selectors.wait_for_uplink_complete(callsign=data.CALLSIGN_NOVA)

    # ⚡ ACT
    dashboard_page_selectors.click_logout()

    # ✅ ASSERT
    dashboard_page_selectors.verify_storage_cleared(
        expected_callsign=data.CALLSIGN_NOVA,
        check_session=True,
    )
    dashboard_page_selectors.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_NOVA,
        check_local=True,
    )
    dashboard_page_selectors.verify_current_url(expected_url_part=data.LOGIN_URL)


@allure.id("CAS-18")
@allure.title("🌌 Пост-активационная навигация 'Happy Path Navigation'.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.actions
def test_navigate_planet_bar_after_uplink(dashboard_page_aurora):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'. Дожидаемся завершения анимации (100%).
    2. Поочередно нажимаем на все кнопки 'Planet Bar', кроме 'Flight Calc Btn'.
    3. Проверяем: клик по каждой кнопке, кнопка активна после 100% загрузки 'прогресс-бара'
    4. Проверяем: соотвествия каждого 'url' открытой странице, своей кнопке 'Planet Bar'.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ⚡ ACT
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ✅ ASSERT
    dashboard_page_aurora.navigate_to_galaxy_map()
    dashboard_page_aurora.navigate_to_cis_table()
    dashboard_page_aurora.navigate_to_mission_control()
    dashboard_page_aurora.navigate_to_settings()


@allure.id("CAS-19")
@allure.title("↩️ Восстановление состояния дашборда после возврата с другой страницы.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.actions
def test_dashboard_state_restore_after_browser_back(dashboard_page_aurora):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'. Дожидаемся завершения анимации (100%).
    2. Кликнуть на 'Galaxy Map Btn', дождаться перехода на 'galaxy-map.html'.
    3. Нажать кнопку 'Дашборд', чтобы вернуться назад.
    4. Проверяем: все элементы, 2 верхние панели + 6 кнопок, в состоянии 'panel-online'.
    5. Проверяем: текст 'Telemetry' содержит зелёную фразу '> CASSANDRA: AURORA, SYSTEM READY...'.
    6. Проверяем: кнопка 'Uplink' остаётся неактивной, полупрозрачной, без пульсации.
    7. Проверяем: 'sessionStorage' содержит валидные данные пользователя.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ⚡ ACT
    dashboard_page_aurora.galaxy_map_btn.click()
    dashboard_page_aurora.verify_current_url(data.GALAXY_MAP_URL)
    browser.driver.back()
    dashboard_page_aurora.verify_current_url(data.DASHBOARD_URL)

    # ✅ ASSERT
    dashboard_page_aurora.verify_uplink_button_disabled()
    dashboard_page_aurora.verify_uplink_buttons_activated()
    dashboard_page_aurora.verify_telemetry_color_with_cassandra(green=True)
    dashboard_page_aurora.verify_telemetry_text(
        expected_text=data.TELEMETRY_SYSTEM_READY_AURORA
    )
    dashboard_page_aurora.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_AURORA,
        check_session=True,
    )


@allure.id("CAS-20")
@allure.title("🛡️ Защита от восстановления сессии через кнопку 'Назад' после 'Logout'.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.actions
def test_logout_protection_via_browser_back(dashboard_page_aurora):
    """
    Сценарий:
    1. Нажимаем на кнопку на 'Uplink Button'. Дожидаемся завершения анимации (100%).
    2. Кликаем на кнопку 'Logout Button' и дожидаемся редиректа на 'login.html' .
    3. Нажимаем на кнопку 'Назад', в браузере, чтобы вернуться назад.
    4. Проверяем: пользователь остаётся на 'login.html'.
    5. Проверяем: ключ `currentUser` в `sessionStorage`
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ⚡ ACT
    dashboard_page_aurora.logout_btn.click()
    dashboard_page_aurora.verify_current_url(data.LOGIN_URL)
    browser.driver.back()

    # ✅ ASSERT
    dashboard_page_aurora.wait_for_url(data.LOGIN_URL)
    dashboard_page_aurora.verify_storage_cleared(
        expected_callsign=data.CALLSIGN_AURORA, check_session=True
    )
