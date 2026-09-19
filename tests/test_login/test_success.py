import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🛰️ Успешная авторизация пользователя 'AURORA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.success
def test_successful_authorization_aurora(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести валидный позывной 'AURORA' в поле 'Callsign'.
    3. Ввести валидный ключ доступа 'COMET_42' в поле 'Access Code'.
    4. Нажать на кнопку 'Establish Connection'.
    5. Проверить: в 'Telemetry', текст меняется на зелёный цвет.
    6. Проверить: текст '> CONNECTION ESTABLISHED. WELCOME, SPECIALIST AURORA'.
    7. Проверить: данные сохраняются в 'sessionStorage'.
    8. Проверить: открылась страница 'dashboard.html'.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_AURORA)
    login_page.enter_access_code(access_code=data.ACCESS_CODE_AURORA)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(green=True)
    login_page.verify_telemetry_text(expected_text=data.GREEN_TELEMETRY_WELCOME_AURORA)
    login_page.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_AURORA, check_session=True, should_exist=True
    )
    login_page.wait_for_url(expected_url_part=data.DASHBOARD_URL)


@allure.id("CAS-02")
@allure.title("🏅 Успешная авторизация пользователя 'ORION'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.success
def test_successful_authorization_orion(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести валидный позывной 'ORION' в поле 'Callsign'.
    3. Ввести валидный ключ доступа 'NEBULA_7' в поле 'Access Code'.
    4. Нажать на кнопку 'Establish Connection'.
    5. Проверить: в 'Telemetry', текст меняется на зелёный цвет.
    6. Проверить: текст '> CONNECTION ESTABLISHED. WELCOME, COMMANDER ORION'.
    7. Проверить: данные сохраняются в 'sessionStorage'.
    8. Проверить: открылась страница 'dashboard.html'.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_ORION)
    login_page.enter_access_code(access_code=data.ACCESS_CODE_ORION)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(green=True)
    login_page.verify_telemetry_text(expected_text=data.GREEN_TELEMETRY_WELCOME_ORION)
    login_page.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_ORION, check_session=True, should_exist=True
    )
    login_page.wait_for_url(expected_url_part=data.DASHBOARD_URL)


@allure.id("CAS-03")
@allure.title("⚙️ Успешная авторизация пользователя 'Nova'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.success
def test_successful_authorization_nova(nova_created, login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Создать пользователя 'Nova'.
    3. Перейти на страницу 'Login Page'.
    4. Ввести валидный позывной 'NOVA' в поле 'Callsign'.
    5. Ввести валидный ключ доступа 'QUASAR_5' в поле 'Access Code'.
    6. Нажать на кнопку 'Establish Connection'.
    7. Проверить: в 'Telemetry', текст меняется на зелёный цвет.
    8. Проверить: текст '> CONNECTION ESTABLISHED. WELCOME, ENGINEER NOVA'.
    9. Проверить: данные сохраняются в 'sessionStorage'.
    10. Проверить: открылась страница 'dashboard.html'.
    """

    # 🎬 ARRANGE

    # ⚡ ACT
    login_page.enter_callsign(callsign=data.CALLSIGN_NOVA)
    login_page.enter_access_code(access_code=data.ACCESS_CODE_NOVA)
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(green=True)
    login_page.verify_telemetry_text(expected_text=data.GREEN_TELEMETRY_WELCOME_NOVA)
    login_page.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_NOVA, check_session=True, should_exist=True
    )
    login_page.wait_for_url(expected_url_part=data.DASHBOARD_URL)


@allure.id("CAS-04")
@allure.title("✈️ Успешная авторизация пользователя 'KNOPA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.success
def test_successful_authorization_knopa(knopa_restored, login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration page'.
    2. Восстановить ключ доступа пользователю 'KNOPA'.
    3. Перейти на страницу 'Login Page'.
    4. Ввести валидный позывной 'KNOPA' в поле 'Callsign'.
    5. Ввести валидный ключ доступа 'AERO_99' в поле 'Access Code'.
    6. Нажать на кнопку 'Establish Connection'.
    7. Проверить: в 'Telemetry', текст меняется на зелёный цвет.
    8. Проверить: текст '> CONNECTION ESTABLISHED. WELCOME, PILOT KNOPA'.
    9. Проверить: данные сохраняются в 'sessionStorage'.
    10. Проверить: открылась страница 'dashboard.html'.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_KNOPA)
    login_page.enter_access_code(access_code=data.ACCESS_CODE_KNOPA)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(green=True)
    login_page.verify_telemetry_text(expected_text=data.GREEN_TELEMETRY_WELCOME_KNOPA)
    login_page.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_KNOPA, check_session=True, should_exist=True
    )
    login_page.wait_for_url(expected_url_part=data.DASHBOARD_URL)
