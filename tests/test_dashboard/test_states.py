import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🛰️ Успешная инициализация панели для 'AURORA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.states
def test_init_aurora(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Навести курсор на инфо панель 'Role Panel' до нажатия кнопки 'Uplink'.
    4. Проверить: инфо панель содержит роль 'SPECIALIST'.
    5. Навести курсор на инфо панель 'User Panel' до нажатия кнопки 'Uplink'.
    6. Проверить: инфо панель содержит имя 'AURORA'.
    7. Проверить: элементы содержат класс 'panel-offline', некликабельны, тултипы скрыты.
    """

    # ✅ ASSERT
    dashboard_page_aurora.verify_panels_data(
        expected_role=data.INFO_PANEL_ROLE_SPECIALIST,
        expected_user=data.TELEMETRY_NAME_AURORA,
    )
    dashboard_page_aurora.verify_panels_are_offline()


@allure.id("CAS-02")
@allure.title("🏅 Успешная инициализация панели для 'ORION'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.states
def test_init_orion(dashboard_page_orion):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'ORION'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Навести курсор на инфо панель 'Role Panel' до нажатия кнопки 'Uplink'.
    4. Проверить: инфо панель содержит роль 'COMMANDER'.
    5. Навести курсор на инфо панель 'User Panel' до нажатия кнопки 'Uplink'.
    6. Проверить: инфо панель содержит имя 'ORION'.
    7. Проверить: элементы содержат класс 'panel-offline', некликабельны, тултипы скрыты.
    """

    # ✅ ASSERT
    dashboard_page_orion.verify_panels_data(
        expected_role=data.INFO_PANEL_ROLE_COMMANDER,
        expected_user=data.TELEMETRY_NAME_ORION,
    )
    dashboard_page_orion.verify_panels_are_offline()


@allure.id("CAS-03")
@allure.title("⚙️ Успешная инициализация панели для 'NOVA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.states
def test_init_nova(dashboard_page_nova):
    """
    Сценарий:
    1. Перейти на страницу 'Signup Page' и создать пользователя 'Nova'.
    2. Выполнить авторизацию под пользователем 'NOVA'.
    3. Перейти на страницу 'Dashboard Page'.
    4. Навести курсор на инфо панель 'Role Panel' до нажатия кнопки 'Uplink'.
    5. Проверить: инфо панель содержит роль 'ENGINEER'.
    6. Навести курсор на инфо панель 'User Panel' до нажатия кнопки 'Uplink'.
    7. Проверить: инфо панель содержит имя 'NOVA'.
    8. Проверить: элементы содержат класс 'panel-offline', некликабельны, тултипы скрыты.
    """

    # ✅ ASSERT
    dashboard_page_nova.verify_panels_data(
        expected_role=data.INFO_PANEL_ROLE_ENGINEER,
        expected_user=data.TELEMETRY_NAME_NOVA,
    )
    dashboard_page_nova.verify_panels_are_offline()


@allure.id("CAS-04")
@allure.title("⚙️ Успешная инициализация панели для 'KNOPA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.states
def test_init_knopa(dashboard_page_knopa):
    """
    Сценарий:
    1. Перейти на страницу 'Restore page' и восстановить доступ пользователю 'KNOPA'.
    2. Выполнить авторизацию под пользователем 'KNOPA'.
    3. Перейти на страницу 'Dashboard Page'.
    4. Навести курсор на инфо панель 'Role Panel' до нажатия кнопки 'Uplink'.
    5. Проверить: инфо панель содержит роль 'PILOT'.
    6. Навести курсор на инфо панель 'User Panel' до нажатия кнопки 'Uplink'.
    7. Проверить: инфо панель содержит имя 'KNOPA'.
    8. Проверить: элементы содержат класс 'panel-offline', некликабельны, тултипы скрыты.
    """

    # ✅ ASSERT
    dashboard_page_knopa.verify_panels_data(
        expected_role=data.INFO_PANEL_ROLE_PILOT,
        expected_user=data.TELEMETRY_NAME_KNOPA,
    )
    dashboard_page_knopa.verify_panels_are_offline()


@allure.id("CAS-05")
@allure.title("🔒 Проверка неактивности кнопки 'Logout' до полной активации")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.states
def test_logout_button_inactive_before_activation(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'.
    4. Дождаться появления кнопки 'Logout'.
    5. Проверить: попытаться кликнуть на кнопку и проверить url.
    6. Проверить: кнопкf имеет 'CSS' свойство 'pointer-events'.

    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ✅ ASSERT
    dashboard_page_aurora.verify_logout_button_inactive()
    dashboard_page_aurora.wait_for_url(expected_url_part=data.DASHBOARD_URL)


@allure.id("CAS-06")
@allure.title("🔒 Проверка неактивности кнопок 'Planet Bar' до полной активации")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.states
def test_planet_bar_buttons_inactive_before_activation(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'.
    4. Дождаться поочередного появления кнопок 'Planet Bar'.
    5. Проверить: при клике на каждую кнопку URL не изменяется.
    6. Проверить: каждая кнопка имеет 'CSS'- свойство 'pointer-events'.
    7. Проверить: что после каждого клика url не изменился.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ✅ ASSERT
    dashboard_page_aurora.verify_planet_bar_buttons_inactive()
    dashboard_page_aurora.wait_for_url(expected_url_part=data.DASHBOARD_URL)


@allure.id("CAS-07")
@allure.title("📊 Валидация анимации и значений прогресс-бара")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.states
def test_progress_bar_animation_and_values(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'.
    4. Проверить: через явные ожидания значение атрибута 'style' у 'Progress Fill',
    значение ширины монотонно возрастает ('10%' -> '22%' -> ... -> '100%') .
    5. Проверить: через явные ожидания значение атрибута `style` у 'Progress Text',
    текстовое значение синхронизировано с шириной.
    6. Проверить: в конце контейнер прогресс-бара имеет 'display: none' или 'opacity: 0'.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ✅ ASSERT
    dashboard_page_aurora.verify_progress_bar_animation()


@allure.id("CAS-08")
@allure.title("💤 Визуальное угасание кнопки 'Uplink' после 100% загрузки")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "dashboard")
@pytest.mark.regress
@pytest.mark.dashboard
@pytest.mark.states
def test_uplink_button_visual_fade_out_after_100_load(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Нажать на кнопку 'Uplink Button'. Дожидаемся завершения анимации (100%).
    4. Проверить: у кнопки 'Uplink Button' отсутствует класс 'uplink-active'.
    5. Проверить: свойство 'opacity' равно 0.4.
    """

    # 🎬 ARRANGE
    dashboard_page_aurora.click_uplink()

    # ⚡ ACT
    dashboard_page_aurora.wait_for_uplink_complete(callsign=data.CALLSIGN_AURORA)

    # ✅ ASSERT
    dashboard_page_aurora.verify_uplink_button_disabled()
