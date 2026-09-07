import allure
import pytest

from tests import data


@allure.id("CAS-14")
@allure.title("🚫 Превышение максимальной длины Callsign >100.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("component", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.edge_cases
def test_callsign_exceeds_max_length(login_page):
    """
    Сценарий:
    1. В поле 'Callsign', попытаться ввести больше 100 символов.
    2. Проверяем: в поле 'Callsign', остается не более 100 символов
    """

    # ✅ ASSERT
    login_page.verify_max_length(element=login_page.callsign_input, max_length=100)


@allure.id("CAS-15")
@allure.title("🚫 Превышение максимальной длины Access Code >30.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.edge_cases
def test_access_code_exceeds_max_length(login_page):
    """
    Сценарий:
    1. В поле 'Access Code', попытаться ввести больше 30 символов.
    2. Проверяем: в поле 'Access Code', остается не более 30 символов
    """

    # ✅ ASSERT
    login_page.verify_max_length(element=login_page.access_code_input, max_length=30)


@allure.id("CAS-16")
@allure.title("🛡️ Санитизация ввода — попытка ввести спецсимволы в поле Callsign.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.edge_cases
def test_input_sanitization_callsign(login_page):
    """
    Сценарий:
    1. В поле 'Callsign', ввести '' OR '1'='1'.
    2. Проверяем: фронтенд отсек спецсимволы — в поле осталось только 'OR11'.
    3. В поле 'Access Code', ввести валидный ключ доступа.
    4. Нажимаем на кнопку 'Establish Connection'.
    5. Проверяем: блок ошибки с текстом '⚠️ Invalid callsign or access code'.
    6. Проверяем: текст 'Telemetry' меняется на красный: '> SYSTEM FAILURE. INVALID CREDENTIALS'.
    7. Проверяем: данные не сохранились в 'sessionStorage'.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.SQL_INJECTION_PAYLOAD)

    # ✅ ASSERT
    login_page.verify_callsign_value(expected_value="OR11")

    # ⚡ ACT
    login_page.enter_access_code(access_code=data.ACCESS_CODE_AURORA)
    login_page.click_establish_connect()

    # ✅ ASSERT
    login_page.verify_telemetry_color_not_cassandra(red=True)
    login_page.verify_telemetry_text(expected_text=data.ERROR_TEXT_TELEMETRY_RED)
    login_page.should_show_auth_error(expected_text=data.AUTH_ERROR_BLOCK_TEXT)
    login_page.verify_user_saved_in_storage(is_saved=False, check_session=True)


@allure.id("CAS-17")
@allure.title("👁️ Переключение видимости ключа доступа")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.edge_cases
def test_toggle_access_code_visibility(login_page):
    """
    Сценарий:
    1. В поле 'Access Code', ввести любые данные, например валидный ключ доступа.
    2. Нажимаем на кнопку 'Toggle Password' (иконка глаза).
    3. Проверяем: при первом клике символы в поле становятся видимыми.
    4. Нажимаем на кнопку 'Toggle Password' (иконка глаза).
    5. Проверяем: при повторном клике, символы скрываются звездочками
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_AURORA)

    # ⚡ ACT
    login_page.click_toggle_password()

    # ✅ ASSERT
    login_page.verify_access_code_type(expected_type="text")

    # ⚡ ACT
    login_page.click_toggle_password()

    # ✅ ASSERT
    login_page.verify_access_code_type(expected_type="password")
