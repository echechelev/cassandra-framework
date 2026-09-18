import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("❌ Неверный пароль для 'AURORA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.errors
def test_invalid_password_aurora(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести валидный позывной 'AURORA' в поле 'Callsign'.
    3. Ввести невалидный ключ доступа 'WRONG_PASS' в поле 'Access Code'.
    4. Нажать на кнопку 'Establish Connection'.
    5. Проверить: блок ошибки с текстом '⚠️ Invalid callsign or access code'.
    6. Проверить: текст 'Telemetry' меняется на красный: '> SYSTEM FAILURE. INVALID CREDENTIALS'.
    7. Проверить: пользователь остается на странице.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(data.CALLSIGN_AURORA)
    login_page.enter_access_code(data.ACCESS_CODE_WRONG)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(red=True)
    login_page.should_show_error_container(
        element=login_page.auth_error_message, expected_text=data.RED_ERROR_AUTH_INVALID
    )
    login_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_SYSTEM_FAILURE)

    login_page.wait_for_url(data.LOGIN_URL)


@allure.id("CAS-02")
@allure.title("🔀 Cross-user password substitution for 'ORION'")
@allure.label("ow Неверный пароль для 'AURORA'.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.errors
def test_cross_user_password_substitution_orion(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести валидный позывной 'ORION' в поле 'Callsign'.
    3. Ввести пароль от 'AURORA' - 'COMET_42' в поле 'Access Code'.
    4. Нажать на кнопку 'Establish Connection'.
    5. Проверить: блок ошибки с текстом '⚠️ Invalid callsign or access code'.
    6. Проверить: текст 'Telemetry' меняется на красный: '> SYSTEM FAILURE. INVALID CREDENTIALS'.
    7. Проверить: пользователь остается на странице.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(data.CALLSIGN_ORION)
    login_page.enter_access_code(data.ACCESS_CODE_AURORA)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(red=True)
    login_page.should_show_error_container(
        element=login_page.auth_error_message, expected_text=data.RED_ERROR_AUTH_INVALID
    )
    login_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_SYSTEM_FAILURE)
    login_page.wait_for_url(data.LOGIN_URL)


@allure.id("CAS-03")
@allure.title("❌ Неверный пароль для 'NOVA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.errors
def test_invalid_password_nova(nova_created, login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Создать пользователя 'NOVA'.
    3. Перейти на страницу 'Login page'.
    4. Ввести валидный позывной 'NOVA' в поле 'Callsign'.
    5. Ввести невалидный ключ доступа 'WRONG_CODE' в поле 'Access Code'.
    6. Нажать на кнопку 'Establish Connection'.
    7. Проверить: блок ошибки с текстом '⚠️ Invalid callsign or access code'.
    8. Проверить: текст 'Telemetry' меняется на красный: '> SYSTEM FAILURE. INVALID CREDENTIALS'.
    9. Проверить: пользователь остается на странице.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(data.CALLSIGN_AURORA)
    login_page.enter_access_code(data.ACCESS_CODE_WRONG)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(red=True)
    login_page.should_show_error_container(
        element=login_page.auth_error_message, expected_text=data.RED_ERROR_AUTH_INVALID
    )
    login_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_SYSTEM_FAILURE)
    login_page.wait_for_url(data.LOGIN_URL)


@allure.id("CAS-04")
@allure.title("🔒 Попытка входа за 'Knopa' до восстановления ключа доступа")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.errors
def test_login_knopa_before_restoration(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести валидный позывной 'KNOPA' в поле 'Callsign'.
    3. Ввести валидный ключ доступа 'AERO_99' в поле 'Access Code'.
    4. Нажать на кнопку 'Establish Connection'.
    5. Проверить: блок ошибки с текстом '⚠️ Invalid callsign or access code'.
    6. Проверить: текст 'Telemetry' меняется на красный: '> SYSTEM FAILURE. INVALID CREDENTIALS'.
    7. Проверить: пользователь остается на странице.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(data.CALLSIGN_KNOPA)
    login_page.enter_access_code(data.ACCESS_CODE_KNOPA)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(red=True)
    login_page.should_show_error_container(
        element=login_page.auth_error_message, expected_text=data.RED_ERROR_AUTH_INVALID
    )
    login_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_SYSTEM_FAILURE)
    login_page.wait_for_url(data.LOGIN_URL)


@allure.id("CAS-05")
@allure.title("🛸 Неверный позывной при валидном ключе")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.errors
def test_invalid_callsign_with_valid_code(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести невалидный позывной 'WRONG' в поле 'Callsign'.
    3. Ввести валидный ключ доступа 'COMET_42' в поле 'Access Code'.
    4. Нажать на кнопку 'Establish Connection'.
    5. Проверить: блок ошибки с текстом '⚠️ Invalid callsign or access code'.
    6. Проверить: текст 'Telemetry' меняется на красный: '> SYSTEM FAILURE. INVALID CREDENTIALS'.
    7. Проверить: пользователь остаётся на странице.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(data.CALLSIGN_WRONG)
    login_page.enter_access_code(data.ACCESS_CODE_AURORA)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(red=True)
    login_page.should_show_error_container(
        element=login_page.auth_error_message, expected_text=data.RED_ERROR_AUTH_INVALID
    )
    login_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_SYSTEM_FAILURE)
    login_page.wait_for_url(data.LOGIN_URL)


@allure.id("CAS-06")
@allure.title("💥 Оба поля неверны")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.errors
def test_both_fields_invalid(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести невалидный позывной 'WRONG' в поле 'Callsign'.
    3. Ввести невалидный ключ доступа 'WRONG_CODE' в поле 'Access Code'.
    4. Нажать на кнопку 'Establish Connection'".
    5. Проверить: блок ошибки с текстом '⚠️ Invalid callsign or access code'.
    6. Проверить: текст 'Telemetry' меняется на красный: '> SYSTEM FAILURE. INVALID CREDENTIALS'.
    7. Проверить: пользователь остается на странице.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(data.CALLSIGN_WRONG)
    login_page.enter_access_code(data.ACCESS_CODE_WRONG)

    # ⚡ ACT
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(red=True)
    login_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_SYSTEM_FAILURE)
    login_page.should_show_error_container(
        element=login_page.auth_error_message, expected_text=data.RED_ERROR_AUTH_INVALID
    )
    login_page.wait_for_url(data.LOGIN_URL)
