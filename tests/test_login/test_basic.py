import allure
import pytest

from tests import data


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
    5. Проверяем: текст 'CONNECTION ESTABLISHED. WELCOME, SPECIALIST AURORA'.
    6. Проверяем данных сохраняются в 'sessionStorage'.
    7. Проверяем: открылась страница '/dashboard'.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_AURORA)
    login_page.enter_access_code(access_code=data.ACCESS_CODE_AURORA)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(green=True)
    login_page.verify_telemetry_text(data.SUCCESS_TELEMETRY_TEXT_AURORA)
    login_page.verify_user_saved_in_storage(
        expected_callsign=data.CALLSIGN_AURORA,
        check_session=True,
    )
    login_page.verify_current_url(
        expected_url_part=data.DASHBOARD_URL,
        wait_for_element=dashboard_page_selectors.start_diagnostics_btn,
    )


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
    5. Проверяем: текст 'CONNECTION ESTABLISHED. WELCOME, SPECIALIST AURORA'.
    6. Проверяем данных сохраняются в 'sessionStorage'.
    7. Проверяем: открылась страница '/dashboard'.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_ORION)
    login_page.enter_access_code(access_code=data.ACCESS_CODE_ORION)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(green=True)
    login_page.verify_telemetry_text(data.SUCCESS_TELEMETRY_TEXT_ORION)
    login_page.verify_user_saved_in_storage(
        expected_callsign=data.CALLSIGN_ORION,
        check_session=True,
    )
    login_page.verify_current_url(
        expected_url_part=data.DASHBOARD_URL,
        wait_for_element=dashboard_page_selectors.start_diagnostics_btn,
    )


@allure.id("CAS-03")
@allure.title("🚀 Успешная авторизация пользователя 'Nova'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.basic
def test_successful_authorization_nova(
    nova_created, login_page_not_open, dashboard_page_selectors
):
    """
    Сценарий:
    1. Создаем пользователя 'Nova' и заходим на дашборд.
    2. Очищаемя 'sessionStorage' и нажимаем кнопку 'Обновить страницу'.
    3. Проверяем: открылась страница '/login'.
    4. Вводим валидный позывной в поле 'Callsign'
    5. Вводим валидный ключ доступа в поле 'Access Code'.
    6. Нажимаем на кнопку 'Establish Connection'.
    7. Проверяем: в 'Telemetry', текст меняется на зелёный цвет.
    8. Проверяем: текст 'CONNECTION ESTABLISHED. WELCOME, SPECIALIST NOVA'.
    9. Проверяем данных сохраняются в 'sessionStorage'.
    10. Проверяем: открылась страница '/dashboard'.
    11. Удаляем пользователя 'NOVA'
    """

    # 🎬 ARRANGE
    nova_created.click_launch_dashbord()
    nova_created.clear_user_data(callsign=data.CALLSIGN_NOVA, clear_current_user=True)
    nova_created.click_refresh_page()
    nova_created.wait_for_url(expected_url_part=data.LOGIN_URL)

    # ⚡ ACT
    login_page_not_open.enter_callsign(callsign=data.CALLSIGN_NOVA)
    login_page_not_open.enter_access_code(access_code=data.ACCESS_CODE_NOVA)
    login_page_not_open.click_establish_connect()

    # ✅ ASSERT
    login_page_not_open.verify_telemetry_color_not_cassandra(green=True)
    login_page_not_open.verify_telemetry_text(data.SUCCESS_TELEMETRY_TEXT_NOVA)
    login_page_not_open.verify_user_saved_in_storage(
        expected_callsign=data.CALLSIGN_NOVA,
        check_session=True,
    )
    login_page_not_open.verify_current_url(
        expected_url_part=data.DASHBOARD_URL,
        wait_for_element=dashboard_page_selectors.start_diagnostics_btn,
    )

    # 🧹 TEARDOWN
    nova_created.delete_operator_from_storage(callsign=data.CALLSIGN_NOVA)


@allure.id("CAS-04")
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
    login_page.verify_telemetry_text(data.DEFAULT_TEXT_TELEMETRY)


@allure.id("CAS-05")
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


@allure.id("CAS-06")
@allure.title("🔗 Переход на страницу восстановления доступа.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.basic
def test_navigation_to_access_restoration_page(login_page):
    """
    Сценарий:
    1. Нажимаем на кнопку 'Access Restoration'.
    6. Проверяем: url страницы 'access-restoration.html'.
    """

    # ⚡ ACT
    login_page.click_access_restoration_btn()

    # ✅ ASSERT
    login_page.verify_current_url(expected_url_part=data.ACCESS_RESTORATION_URL)
   
    

