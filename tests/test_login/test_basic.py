import allure
import pytest

from . import data


@allure.id("CAS-01")
@allure.title("🚀 Успешная авторизация пользователя 'AURORA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.basic
def test_successful_authorization_aurora(login_page, dashboard_page_selectors):
    """
    Сценарий:
    1. Вводим валидный позывной в поле 'Callsign'
    2. Вводим валидный ключ доступа в поле 'Access Code'.
    3. Нажимаем на кнопку 'Establish Connection'.
    4. Проверяем: в 'Telemetry', текст меняется на зелёный цвет.
    5. Проверяем: текст 'CONNECTION ESTABLISHED. WELCOME, SPECIALIST AURORA'
    6. Проверяем данных сохраняются в localStorage
    7. Проверяем: открылась страница '/dashboard'
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.AURORA_CALLSIGN)
    login_page.enter_access_code(access_code=data.AURORA_ACCESS_CODE)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(green=True)
    login_page.verify_telemetry_text(data.SUCCESS_TELEMETRY_TEXT_AURORA)
    login_page.verify_user_saved_in_localstorage(
        expected_callsign=data.AURORA_CALLSIGN,
        expected_role=data.ROLE_SPECIALIST,
        expected_full_name=data.NAME_AURORA,
    )
    login_page.verify_current_url(
        expected_url_part=data.DASHBOARD_URL,
        wait_for_element=dashboard_page_selectors.start_diagnostics_btn)


@allure.id("CAS-02")
@allure.title("🚀 Успешная авторизация пользователя 'ORION'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.basic
def test_successful_authorization_orion(login_page, dashboard_page_selectors):
    """
    Сценарий:
    1. Вводим валидный позывной в поле 'Callsign'
    2. Вводим валидный ключ доступа в поле 'Access Code'.
    3. Нажимаем на кнопку 'Establish Connection'.
    4. Проверяем: в 'Telemetry', текст меняется на зелёный цвет.
    5. Проверяем: текст 'CONNECTION ESTABLISHED. WELCOME, SPECIALIST AURORA'
    6. Проверяем данных сохраняются в localStorage
    7. Проверяем: открылась страница '/dashboard'
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.ORION_CALLSIGN)
    login_page.enter_access_code(access_code=data.ORION_ACCESS_CODE)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(green=True)
    login_page.verify_telemetry_text(data.SUCCESS_TELEMETRY_TEXT_ORION)
    login_page.verify_user_saved_in_localstorage(
        expected_callsign=data.ORION_CALLSIGN,
        expected_role=data.ROLE_COMMANDER,
        expected_full_name=data.NAME_ORION,
    )
    login_page.verify_current_url(
        expected_url_part=data.DASHBOARD_URL,
        wait_for_element=dashboard_page_selectors.start_diagnostics_btn)


@allure.id("CAS-03")
@allure.title("📡 Состояние страницы при загрузке")
@allure.label("owner", "Evgeniy Chechelev")

@allure.label("component", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.basic
def test_default_page_state_on_load(login_page):
    """
    Сценарий:
    1. Оцениваем состояние кнопки `Establish Connection`.
    2. Проверяем: кнопка `Establish Connection` неактивна (disabled)
    3. Оцениваем состояние элемента 'Telemetry'.
    4. Проверяем: текст '> SYSTEM READY. AWAITING CONNECTION', синего цвета.
    """

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=False)
    login_page.verify_telemetry_color_not_cassandra(blue=True)
    login_page.verify_telemetry_text(data.DEFAULT_TEXT_TELEMETRY_BLUE)


@allure.id("CAS-04")
@allure.title("📡 Реактивное состояние кнопки Establish Connection.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.basic
def test_reactive_button_state(login_page):
    """
    Сценарий:
    1. Вводим в поле 'Callsign' < 3 символов.
    2. Вводим в поле 'Access Code' < 4 символов.
    3. Проверяем: кнопка неактивна при невалидной длине полей.
    4. Вводим в поле 'Callsign' 3 символа.
    5. Вводим в поле 'Access Code' 4 символа.
    6. Проверяем: кнопка активна.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(data.CALLSIGN_TOO_SHORT_2_CHARS)
    login_page.enter_access_code(data.ACCESS_CODE_TOO_SHORT_3_CHARS)

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=False)

    # ⚡ ACT
    login_page.enter_callsign(
        callsign=data.CALLSIGN_MIN_VALID_3_CHARS, clear_first=True
    )
    login_page.enter_access_code(
        access_code=data.ACCESS_CODE_MIN_VALID_4_CHARS, clear_first=True
    )

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=True)
