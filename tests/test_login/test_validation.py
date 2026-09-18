import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("📏 Позывной короче минимальной длины")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_callsign_less_than_min_length(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести 3 символа в поле 'Callsign'.
    3. Ввести валидный ключ доступа 'COMET_42' в поле 'Access Code'.
    4. Проверить: кнопка `Establish Connection` остаётся неактивной `disabled`.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_TOO_SHORT_3_CHARS)
    login_page.enter_access_code(access_code=data.ACCESS_CODE_AURORA)

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=False)


@allure.id("CAS-02")
@allure.title("🔑 Ключ доступа короче минимальной длины")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_access_code_less_than_min_length(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести валидный позывной 'AURORA' в поле 'Callsign'.
    3. Ввести 3 символа в поле 'Access Code'.
    4. Проверить: кнопка `Establish Connection` остаётся неактивной `disabled`.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_AURORA)
    login_page.enter_access_code(access_code=data.ACCESS_CODE_TOO_SHORT_3_CHARS)

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=False)


@allure.id("CAS-03")
@allure.title("🌌 Пустой позывной при заполненном ключе")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_empty_callsign_with_valid_code(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Оставить поле 'Callsign' пустым.
    3. Ввести валидный ключ доступа 'COMET_42' в поле 'Access Code'.
    4. Проверить: кнопка `Establish Connection` остаётся неактивной `disabled`.
    """

    # 🎬 ARRANGE
    login_page.enter_access_code(access_code=data.ACCESS_CODE_AURORA)

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=False)


@allure.id("CAS-04")
@allure.title("🗝️ Пустой ключ доступа при заполненном позывном")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_empty_access_code_with_valid_callsign(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести валидный позывной 'AURORA' в поле 'Callsign'.
    3. Оставить поле 'Access Code' пустым.
    4. Проверить: кнопка `Establish Connection` остаётся неактивной `disabled`.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_AURORA)

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=False)


@allure.id("CAS-05")
@allure.title("🚫 Превышение максимальной длины Callsign >100")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_callsign_exceeds_max_length(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Попытаться ввести >100 в поле 'Callsign'.
    3. Проверить: в поле 'Callsign' остается не более 100 символов.
    """

    # ✅ ASSERT
    login_page.verify_max_length(element=login_page.callsign_input, max_length=100)


@allure.id("CAS-06")
@allure.title("🚫 Превышение максимальной длины Access Code >30")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_access_code_exceeds_max_length(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Попытаться ввести >30 в поле 'Access Code'.
    3. Проверить: в поле 'Access Code', остается не более 30 символов.
    """

    # ✅ ASSERT
    login_page.verify_max_length(element=login_page.access_code_input, max_length=30)


@allure.id("CAS-07")
@allure.title("🛡️ Санитизация ввода — попытка ввести спецсимволы в поле Callsign")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_input_sanitization_callsign(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести строку с спецсимволами "' OR '1'='1'" в поле 'Callsign'.
    3. Ввести валидный ключ доступа 'COMET_42' в поле 'Access Code'.
    4. Нажать на кнопку 'Establish Connection'.
    5. Проверить: фронтенд автоматически отсекает спецсимволы — в поле остаётся 'OR11'.
    6. Проверить: блок ошибки с текстом '⚠️ Invalid callsign or access code'.
    7. Проверить: текст 'Telemetry' меняется на красный: '> SYSTEM FAILURE. INVALID CREDENTIALS'.
    8. Проверить: данные не сохраняются в 'sessionStorage'.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.SQL_INJECTION_PAYLOAD)
    login_page.enter_access_code(access_code=data.ACCESS_CODE_AURORA)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_field_value(
        element=login_page.callsign_input, expected_value="OR11"
    )
    login_page.verify_telemetry_color_not_cassandra(red=True)
    login_page.should_show_error_container(
        element=login_page.auth_error_message, expected_text=data.RED_ERROR_AUTH_INVALID
    )
    login_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_SYSTEM_FAILURE)

    login_page.verify_user_saved_in_storage(is_saved=False, check_session=True)
