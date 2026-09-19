import allure
import pytest
from selene import browser

from tests import data


@allure.id("CAS-01")
@allure.title("💡 Динамическая подстановка данных в тултипы для 'AURORA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.interactions
def test_tooltips_display_dynamic_data_aurora(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    4. Навести курсор мыши 'ActionChains' на 'Role Panel' и 'User Panel'.
    5. Проверить: тултип 'Role Panel' отображает текст 'Access: Level 2'.
    6. Проверить: тултип 'User Panel' отображает текст 'ID: '884-2A'.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ⚡ ACT
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ✅ ASSERT
    dashboard_page_aurora.verify_tooltips_dynamic_data(user_data=data.USER_AURORA)


@allure.id("CAS-02")
@allure.title("💡 Динамическая подстановка данных в тултипы для 'ORION'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.interactions
def test_tooltips_display_dynamic_data_orion(dashboard_page_orion):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'ORION'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    4. Навести курсор мыши 'ActionChains' на 'Role Panel' и 'User Panel'.
    5. Проверить: тултип 'Role Panel' отображает текст 'Access: Level 1'.
    6. Проверить: тултип 'User Panel' отображает текст 'ID: 001-1A'.
    """

    # 🎬 ARRANGE
    dashboard_page_orion.click_uplink()

    # ⚡ ACT
    dashboard_page_orion.wait_for_uplink_complete(callsign=data.CALLSIGN_ORION)

    # ✅ ASSERT
    dashboard_page_orion.verify_tooltips_dynamic_data(user_data=data.USER_ORION)


@allure.id("CAS-03")
@allure.title("🚀 Динамическая подстановка данных в тултипы для 'NOVA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.interactions
def test_tooltips_display_dynamic_data_nova(dashboard_page_nova):
    """
    Сценарий:
    1. Перейти на страницу 'Signup Page' и создать пользователя 'Nova'.
    2. Выполнить авторизацию под пользователем 'NOVA'.
    3. Перейти на страницу 'Dashboard Page'.
    4. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    5. Навести курсор мыши 'ActionChains' на 'Role Panel' и 'User Panel'.
    6. Проверить: тултип 'Role Panel' отображает текст 'Access: Level 3'.
    7. Проверить: тултип 'User Panel' отображает текст 'ID: 512-3A'.
    """

    # 🎬 ARRANGE
    dashboard_page_nova.click_uplink()

    # ⚡ ACT
    dashboard_page_nova.wait_for_uplink_complete(callsign=data.CALLSIGN_NOVA)

    # ✅ ASSERT
    dashboard_page_nova.verify_tooltips_dynamic_data(user_data=data.USER_NOVA)


@allure.id("CAS-04")
@allure.title("🚀 Динамическая подстановка данных в тултипы для 'KNOPA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.interactions
def test_tooltips_display_dynamic_data_knopa(dashboard_page_knopa):
    """
    Сценарий:
    1. Перейти на страницу 'Restore page' и восстановить доступ пользователю 'KNOPA'.
    2. Выполнить авторизацию под пользователем 'KNOPA'.
    3. Перейти на страницу 'Dashboard Page'.
    4. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    5. Навести курсор мыши 'ActionChains' на 'Role Panel' и 'User Panel'.
    6. Проверить: тултип 'Role Panel' отображает текст 'Access: Level 1'.
    7. ПРоверить: тултип 'User Panel' отображает текст 'ID: 769-1A'.
    """

    # 🎬 ARRANGE
    dashboard_page_knopa.click_uplink()

    # ⚡ ACT
    dashboard_page_knopa.wait_for_uplink_complete(callsign=data.CALLSIGN_KNOPA)

    # ✅ ASSERT
    dashboard_page_knopa.verify_tooltips_dynamic_data(user_data=data.USER_KNOPA)


@allure.id("CAS-05")
@allure.title("🖱️ Hover-эффект кнопки Logout в активном состоянии")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.interactions
def test_logout_button_hover_effect(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    4. Навести курсор мыши на кнопку 'Logout Button'.
    5. Проверить: кнопка увеличивается в размере 'transform: scale 1.15'.
    6. Проверить: рамка и свечение становятся ярче. Курсор меняется на 'pointer'.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ⚡ ACT
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ✅ ASSERT
    dashboard_page_aurora.verify_logout_button_hover_effect()


@allure.id("CAS-06")
@allure.title("🌌 Пост-активационная навигация по 'Planet Bar'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.interactions
def test_planet_bar_navigation(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    4. Поочередно нажать на все кнопки 'Planet Bar', кроме 'Flight Calc Btn'.
    5. Проверить: каждая кнопка становится кликабельной после 100% загрузки прогресс-бара.
    6. Проверить: каждая кнопка открывает соответствующую страницу (правильный URL).
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


@allure.id("CAS-07")
@allure.title("↩️ Восстановление состояния дашборда после возврата с другой страницы")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.interactions
def test_dashboard_state_restore_after_browser_back(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'. Дождаться завершения анимации (100%).
    4. Нажать на 'Galaxy Map Btn', дождаться перехода на 'galaxy-map.html'.
    5. Нажать на кнопку 'Дашборд', чтобы вернуться назад.
    6. Проверить: все элементы, 2 верхние панели + 6 кнопок, в состоянии 'panel-online'.
    7. Проверить: текст телеметрии содержит зелёную фразу '> CASSANDRA: AURORA, SYSTEM READY...'.
    8. Проверить: кнопка 'Uplink' остаётся неактивной, полупрозрачной, без пульсации.
    9. Проверить: 'sessionStorage' содержит валидные данные пользователя.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ⚡ ACT
    dashboard_page_aurora.galaxy_map_btn.click()
    dashboard_page_aurora.wait_for_url(expected_url_part=data.GALAXY_MAP_URL)
    dashboard_page_aurora.click_browser_back()
    dashboard_page_aurora.wait_for_url(expected_url_part=data.DASHBOARD_URL)

    # ✅ ASSERT
    dashboard_page_aurora.verify_uplink_button_disabled()
    dashboard_page_aurora.verify_uplink_buttons_activated()
    dashboard_page_aurora.verify_telemetry_color_with_cassandra(green=True)
    dashboard_page_aurora.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_SYSTEM_READY_AURORA
    )
    dashboard_page_aurora.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_AURORA,
        check_session=True,
    )
