import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🔒 Блокировка зарезервированного позывного 'AURORA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.errors
def test_reserved_callsign_aurora_blocked(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести имя 'Aurora' в поле 'Full Name'.
    3. Выбрать роль 'SPECIALIST' в поле 'Role'.
    4. Нажать на кнопку 'PROCEED'.
    5. Проверить: текст ошибки в блоке `Signup Error Block` — `⚠️ Callsign 'AURORA'...
    6. Проверить: текст телеметрии — `> SYSTEM LOCKED. CALLSIGN 'AURORA' ALREADY EXISTS`.
    7. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_AURORA)
    signup_page.select_role(role_value=data.ROLE_SPECIALIST)

    # ⚡ ACT
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_message,
        expected_text=data.RED_ERROR_CALLSIGN_AURORA_RESERVED,
    )
    signup_page.verify_telemetry_text(
        expected_text=data.RED_TELEMETRY_CALLSIGN_AURORA_EXISTS
    )
    signup_page.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-02")
@allure.title("🔒 Блокировка зарезервированного позывного 'ORION'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.errors
def test_reserved_callsign_orion_blocked(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести имя 'Orion' в поле 'Full Name'.
    3. Выбрать роль 'COMMANDER' в поле 'Role'.
    4. Нажать на кнопку 'PROCEED'.
    5. Проверить: текст ошибки в блоке `Signup Error Block` — `⚠️ Callsign 'ORION'..
    6. Проверить: текст телеметрии — `> SYSTEM LOCKED. CALLSIGN 'ORION' ALREADY EXISTS`.
    7. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_ORION)
    signup_page.select_role(role_value=data.ROLE_COMMANDER)

    # ⚡ ACT
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_message,
        expected_text=data.RED_ERROR_CALLSIGN_ORION_RESERVED,
    )
    signup_page.verify_telemetry_text(
        expected_text=data.RED_TELEMETRY_CALLSIGN_ORION_EXISTS
    )
    signup_page.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-03")
@allure.title("⚠️ Блокировка неверной роли для 'NOVA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.errors
def test_wrong_role_for_nova(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести имя 'Nova' в поле 'Full Name'.
    3. Выбрать роль 'COMMANDER' в поле 'Role'.
    4. Нажать на кнопку 'PROCEED'.
    5. Проверить: текст ошибки в блоке `Signup Error Block` — `⚠️ Registration suspended...`
    6. Проверить: текст телеметрии — `> SYSTEM LOCKED. ROLE MISMATCH...`
    7. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_COMMANDER)

    # ⚡ ACT
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_message,
        expected_text=data.RED_ERROR_ROLE_MISMATCH,
    )
    signup_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_ROLE_MISMATCH)
    signup_page.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-04")
@allure.title("⚠️ Блокировка зарезервированного позывного 'KNOPA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.errors
def test_reserved_callsign_knopa(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести имя 'Knopa' в поле 'Full Name'.
    3. Выбрать роль 'COMMANDER' в поле 'Role'.
    4. Нажать на кнопку 'PROCEED'.
    5. Проверить: текст ошибки в блоке `Signup Error Block` — `⚠️ Callsign 'KNOPA'...`
    6. Проверить: текст телеметрии — `> SYSTEM LOCKED. CALLSIGN 'KNOPA'...`
    7. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_KNOPA)
    signup_page.select_role(role_value=data.ROLE_COMMANDER)

    # ⚡ ACT
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_message,
        expected_text=data.RED_ERROR_CALLSIGN_KNOPA_RESERVED,
    )
    signup_page.verify_telemetry_text(
        expected_text=data.RED_TELEMETRY_CALLSIGN_KNOPA_EXISTS
    )
    signup_page.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-05")
@allure.title("🚫 Блокировка неизвестного позывного")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.errors
def test_unknown_callsign(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести имя 'Ivan' в поле 'Full Name'.
    3. Выбрать 'ENGINEER' в поле 'Role'.
    4. Нажать на кнопку 'PROCEED'.
    5. Проверить: текст ошибки в блоке `Signup Error Block` — `⚠️ Registration suspended...`
    6. Проверить: текст телеметрии — `> SYSTEM LOCKED. PLEASE ENTER CORRECT...`
    7. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_IVAN)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)

    # ⚡ ACT
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_message,
        expected_text=data.RED_ERROR_CAPACITY_REACHED,
    )
    signup_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_UNKNOWN_USER)
    signup_page.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-06")
@allure.title("🔑 Невалидный 'Access Code' (несовпадение)")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.errors
def test_access_codes_mismatch(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Ввести 'QUASAR_5' в поле 'Access Code'.
    4. Ввести 'WRONG_CODE' в поле 'Confirm Access Code'.
    5. Ввести 'COMETA' в поле 'Recovery Cipher'.
    6. Нажать кнопку 'COMPLETE REGISTRATION'.
    7. Проверить: текст ошибки в блоке `Security Error Block` — `⚠️ Security protocol failed...`
    8. Проверить: текст телеметрии — `> SYSTEM LOCKED. INVALID CREDENTIALS.`.
    9. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(access_code=data.ACCESS_CODE_NOVA)
    signup_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_WRONG)
    signup_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_NOVA)
    signup_page.click_complete_registration()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_security_message,
        expected_text=data.RED_ERROR_SECURITY_FAILED,
    )
    signup_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_SECURITY_INVALID)
    signup_page.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-07")
@allure.title("🔑 Невалидный 'Access Code' (неверное значение)")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.errors
def test_invalid_access_code_value(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Ввести 'WRONG_CODE' в поле 'Access Code'.
    4. Ввести 'WRONG_CODE' в поле 'Confirm Access Code'.
    5. Ввести 'COMETA' в поле 'Recovery Cipher'.
    6. Нажать кнопку 'COMPLETE REGISTRATION'.
    7. Проверить: текст ошибки в блоке `Security Error Block` — `️ ⚠️ Security protocol failed...`
    8. Проверить: текст телеметрии — `> SYSTEM LOCKED. INVALID CREDENTIALS`.
    9. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(access_code=data.ACCESS_CODE_WRONG)
    signup_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_WRONG)
    signup_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_NOVA)
    signup_page.click_complete_registration()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_security_message,
        expected_text=data.RED_ERROR_SECURITY_FAILED,
    )
    signup_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_SECURITY_INVALID)
    signup_page.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-08")
@allure.title("🔐 Невалидный 'Recovery Cipher'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.errors
def test_invalid_recovery_cipher(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Ввести 'QUASAR_5' в поле 'Access Code'.
    4. Ввести 'QUASAR_5' в поле 'Confirm Access Code'.
    5. Ввести 'WRONG' в поле 'Recovery Cipher'.
    6. Нажать кнопку 'COMPLETE REGISTRATION'.
    7. Проверить: текст ошибки в блоке `Security Error Block` — `⚠️ Security protocol failed...`
    8. Проверить: текст телеметрии — `> SYSTEM LOCKED. INVALID CREDENTIALS.`.
    9. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(access_code=data.ACCESS_CODE_NOVA)
    signup_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_NOVA)
    signup_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_WRONG)
    signup_page.click_complete_registration()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_security_message,
        expected_text=data.RED_ERROR_SECURITY_FAILED,
    )
    signup_page.verify_telemetry_text(expected_text=data.RED_TELEMETRY_SECURITY_INVALID)
    signup_page.verify_telemetry_color_not_cassandra(red=True)
