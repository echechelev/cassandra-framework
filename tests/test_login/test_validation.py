import allure
import pytest

from . import data


@allure.id("CAS-05")
@allure.title("📏 Позывной короче минимальной длины.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_сallsign_less_than_min_length(login_page):
    """
    Сценарий:
    1. Вводим 1-2 символа в поле 'Callsign'.
    2. Вводим валидный ключ доступа в поле 'Access Code'.
    3. Проверяем: кнопка `Establish Connection` остаётся неактивной `disabled`.
    4. Проверяем: отправка формы не производится.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_TOO_SHORT_2_CHARS)
    login_page.enter_access_code(access_code=data.AURORA_ACCESS_CODE)

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=False)
    login_page.verify_current_url(expected_url_part=data.LOGIN)


@allure.id("CAS-06")
@allure.title("🔑 Ключ доступа короче минимальной длины.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_access_code_less_than_min_length(login_page):
    """
    Сценарий:
    1. Вводим валидный позывной в поле 'Callsign'.
    2. Вводим 2-3 символа в поле 'Access Code'.
    3. Проверяем: кнопка `Establish Connection` остаётся неактивной `disabled`.
    4. Проверяем: отправка формы не производится.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.AURORA_CALLSIGN)
    login_page.enter_access_code(access_code=data.ACCESS_CODE_TOO_SHORT_3_CHARS)

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=False)
    login_page.verify_current_url(expected_url_part=data.LOGIN)


@allure.id("CAS-07")
@allure.title("🌌 Пустой позывной при заполненном ключе.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_empty_callsign_with_valid_code(login_page):
    """
    Сценарий:
    1. Поле 'Callsign', оставляем пустым.
    2. В поле 'Access Code', вводим валидный ключ доступа.
    3. Проверяем: кнопка `Establish Connection` остаётся неактивной `disabled`.
    4. Проверяем: отправка формы не производится.
    """

    # 🎬 ARRANGE
    login_page.enter_access_code(access_code=data.AURORA_ACCESS_CODE)

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=False)
    login_page.verify_current_url(expected_url_part=data.LOGIN)


@allure.id("CAS-08")
@allure.title("🗝️ Пустой ключ доступа при заполненном позывном.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_empty_access_code_with_valid_callsign(login_page):
    """
    Сценарий:
    1. В поле 'Callsign', ввести валидный позывной.
    2. Поле 'Access Code', оставляем пустым.
    3. Проверяем: кнопка `Establish Connection` остаётся неактивной `disabled`.
    4. Проверяем: отправка формы не производится.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.AURORA_CALLSIGN)

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=False)
    login_page.verify_current_url(expected_url_part=data.LOGIN)


@allure.id("CAS-09")
@allure.title("🛸 Неверный позывной при валидном ключе.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_invalid_callsign_with_valid_code(login_page):
    """
    Сценарий:
    1. В поле 'Callsign', ввести неверный позывной.
    2. В Поле 'Access Code', ввести валидный ключ доступа.
    3. Нажать на кнопку 'Establish Connection'
    4. Проверяем: блок ошибки с текстом '⚠️ Invalid callsign or access code'.
    5. Проверяем: Текст 'Telemetry' меняется на красный: '> SYSTEM FAILURE. INVALID CREDENTIALS'.
    6. Проверяем: пользователь остаётся на странице.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(data.WRONG_CALLSIGN)
    login_page.enter_access_code(data.AURORA_ACCESS_CODE)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(red=True)
    login_page.verify_telemetry_text(expected_text=data.ERROR_TEXT_TELEMETRY_RED)
    login_page.should_show_auth_error(expected_text=data.AUTH_ERROR_BLOCK_TEXT)
    login_page.verify_current_url(expected_url_part=data.LOGIN)


@allure.id("CAS-10")
@allure.title("🔒 Валидный позывной при неверном ключе.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_valid_callsign_with_invalid_code(login_page):
    """
    Сценарий:
    1. В поле 'Callsign', ввести валидный позывной.
    2. В Поле 'Access Code', ввести невалидный ключ доступа.
    3. Нажать на кнопку 'Establish Connection'
    4. Проверяем: блок ошибки с текстом '⚠️ Invalid callsign or access code'.
    5. Проверяем: текст 'Telemetry' меняется на красный: '> SYSTEM FAILURE. INVALID CREDENTIALS'.
    6. Проверяем: пользователь остается на странице.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(data.AURORA_CALLSIGN)
    login_page.enter_access_code(data.WRONG_ACCESS_CODE)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(red=True)
    login_page.verify_telemetry_text(expected_text=data.ERROR_TEXT_TELEMETRY_RED)
    login_page.should_show_auth_error(expected_text=data.AUTH_ERROR_BLOCK_TEXT)
    login_page.verify_current_url(expected_url_part=data.LOGIN)


@allure.id("CAS-11")
@allure.title("💥 Оба поля неверны.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.validation
def test_both_fields_invalid(login_page):
    """
    Сценарий:
    1. В поле 'Callsign', ввести невалидный позывной.
    2. В Поле 'Access Code', ввести невалидный ключ доступа.
    3. Нажать на кнопку 'Establish Connection'
    4. Проверяем: блок ошибки с текстом '⚠️ Invalid callsign or access code'.
    5. Проверяем: Текст 'Telemetry' меняется на красный: '> SYSTEM FAILURE. INVALID CREDENTIALS'
    6. Проверяем: пользователь остается на странице.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(data.WRONG_CALLSIGN)
    login_page.enter_access_code(data.WRONG_ACCESS_CODE)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(red=True)
    login_page.verify_telemetry_text(expected_text=data.ERROR_TEXT_TELEMETRY_RED)
    login_page.should_show_auth_error(expected_text=data.AUTH_ERROR_BLOCK_TEXT)
    login_page.verify_current_url(expected_url_part=data.LOGIN)
