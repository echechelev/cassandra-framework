import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("📏 Позывной короче минимальной длины")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.validation
def test_callsign_less_than_min_length(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Restore Page'.
    2. Ввести 3 символа в поле 'Callsign'.
    2. Ввести валидный позывной в поле 'Callsign'.
    3. Ввести валидное кодовое слово 'AERO' в поле 'Recovery Cipher'.
    3. Ввести валидный ключ доступа в поля 'New Access Code' и 'Confirm Access Code'.
    4. Проверить: кнопка `RESTORE ACCESS` остаётся неактивной `disabled`.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.CALLSIGN_TOO_SHORT_3_CHARS)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_KNOPA)
    restore_page.enter_new_access_code(new_code=data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_KNOPA)

    # ✅ ASSERT
    restore_page.should_be_restore_access_btn(is_enabled=False)


@allure.id("CAS-02")
@allure.title("📏 Шифр восстановления короче минимальной длины")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.validation
def test_recovery_cipher_less_than_min_length(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести валидный позывной 'KNOPA' в поле 'Callsign'.
    3. Ввести 3 символа в поле 'Recovery Cipher'.
    4. Ввести валидный ключ доступа 'AERO_99' в поле 'New Access Code'.
    5. Ввести валидный ключ доступа 'AERO_99' в поле 'Confirm Access Code'.
    6. Проверить: кнопка 'RESTORE ACCESS' остаётся неактивной 'disabled'.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.CALLSIGN_KNOPA)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_TOO_SHORT_3_CHARS)
    restore_page.enter_new_access_code(new_code=data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_KNOPA)

    # ✅ ASSERT
    restore_page.should_be_restore_access_btn(is_enabled=False)


@allure.id("CAS-03")
@allure.title("📏 Новый код доступа короче минимальной длины")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.validation
def test_new_access_code_less_than_min_length(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести валидный позывной 'KNOPA' в поле 'Callsign'.
    3. Ввести валидный шифр 'AERO' в поле 'Recovery Cipher'.
    4. Ввести 3 символа в поле 'New Access Code'.
    5. Ввести валидный код доступа 'AERO_99' в поле 'Confirm Access Code'.
    6. Проверить: кнопка 'RESTORE ACCESS' остаётся неактивной 'disabled'.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.CALLSIGN_KNOPA)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_KNOPA)
    restore_page.enter_new_access_code(new_code=data.ACCESS_CODE_TOO_SHORT_3_CHARS)
    restore_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_KNOPA)

    # ✅ ASSERT
    restore_page.should_be_restore_access_btn(is_enabled=False)


@allure.id("CAS-04")
@allure.title("📏 Код подтверждения короче минимальной длины")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.validation
def test_confirm_access_code_less_than_min_length(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести валидный позывной 'KNOPA' в поле 'Callsign'.
    3. Ввести валидный шифр 'AERO' в поле 'Recovery Cipher'.
    4. Ввести валидный код доступа 'AERO_99' в поле 'New Access Code'.
    5. Ввести 3 символа в поле 'Confirm Access Code'.
    6. Проверить: кнопка 'RESTORE ACCESS' остаётся неактивной 'disabled'.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.CALLSIGN_KNOPA)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_KNOPA)
    restore_page.enter_new_access_code(new_code=data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(
        confirm_code=data.ACCESS_CODE_TOO_SHORT_3_CHARS
    )

    # ✅ ASSERT
    restore_page.should_be_restore_access_btn(is_enabled=False)


@allure.id("CAS-05")
@allure.title("🚫 Превышение максимальной длины Callsign >100")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.validation
def test_callsign_exceeds_max_length(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Попытаться ввести >100 в поле 'Callsign'.
    3. Проверить: в поле 'Callsign' остается не более 100 символов.
    """

    # ✅ ASSERT
    restore_page.verify_max_length(element=restore_page.callsign_input, max_length=100)


@allure.id("CAS-06")
@allure.title("🚫 Превышение максимальной длины Recovery Cipher >100")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.validation
def test_recovery_cipher_exceeds_max_length(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Попытаться ввести >100 в поле 'Recovery Cipher'.
    3. Проверить: в поле 'Recovery Cipher' остается не более 100 символов.
    """

    # ✅ ASSERT
    restore_page.verify_max_length(
        element=restore_page.recovery_cipher_input, max_length=100
    )


@allure.id("CAS-07")
@allure.title("🚫 Превышение максимальной длины New Access Code >30")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.validation
def test_new_access_code_exceeds_max_length(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Попытаться ввести >30 в поле 'New Access Code'.
    3. Проверить: в поле 'New Access Code' остается не более 30 символов.
    """

    # ✅ ASSERT
    restore_page.verify_max_length(
        element=restore_page.new_access_code_input, max_length=30
    )


@allure.id("CAS-08")
@allure.title("🚫 Превышение максимальной длины Confirm Access Code >30")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.validation
def test_confirm_access_code_exceeds_max_length(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Попытаться ввести >30 в поле 'Confirm Access Code'.
    3. Проверить: в поле 'Confirm Access Code' остается не более 30 символов.
    """

    # ✅ ASSERT
    restore_page.verify_max_length(
        element=restore_page.confirm_access_code_input, max_length=30
    )


@allure.id("CAS-09")
@allure.title("🛡️ SQL-инъекция в поле Callsign")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.validation
def test_sql_injection_in_callsign(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести SQL-инъекцию "' OR '1'='1" в поле 'Callsign'.
    3. Проверить: фронтенд автоматически отсекает спецсимволы — в поле остаётся только 'OR11'.
    4. Ввести валидный шифр 'AERO' в поле 'Recovery Cipher'.
    5. Ввести валидный код доступа 'AERO_99' в поле 'New Access Code'.
    6. Ввести валидный код доступа 'AERO_99' в поле 'Confirm Access Code'.
    7. Нажать кнопку 'RESTORE ACCESS'.
    8. Проверить: через 2 секунды появляется ошибка '⚠️ Restoration unavailable. Only operator KNOPA is eligible for access recovery.'.
    9. Проверить: телеметрия красная: '> SECURITY PROTOCOL FAILED. RESTORATION ABORTED'.
    10. Проверить: данные не сохраняются в localStorage.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.SQL_INJECTION_PAYLOAD)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_KNOPA)
    restore_page.enter_new_access_code(new_code=data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_KNOPA)

    # ⚡ ACT
    restore_page.click_restore_access(wait_for_success=False)

    # ✅ ASSERT
    restore_page.verify_field_value(
        element=restore_page.callsign_input, expected_value="OR11"
    )
    restore_page.verify_telemetry_color_not_cassandra(red=True)
    restore_page.should_show_error_container(
        element=restore_page.error_message, expected_text=data.RED_ERROR_ACCESS_RECOVERY
    )
    restore_page.verify_telemetry_text(
        expected_text=data.RED_TELEMETRY_RESTORATION_ABORTED
    )
    restore_page.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_KNOPA, check_local=True, should_exist=False
    )


@allure.id("CAS-10")
@allure.title("🛡️ SQL-инъекция в поле Recovery Cipher")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.validation
def test_sql_injection_in_recovery_cipher(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести валидный позывной 'KNOPA' в поле 'Callsign'.
    3. Ввести SQL-инъекцию "' OR '1'='1" в поле 'Recovery Cipher'.
    4. Ввести валидный код доступа 'AERO_99' в поле 'New Access Code'.
    5. Ввести валидный код доступа 'AERO_99' в поле 'Confirm Access Code'.
    6. Проверить: фронтенд автоматически отсекает спецсимволы и цифры — в поле остаётся только 'OR' (2 символа).
    7. Проверить: кнопка 'RESTORE ACCESS' остаётся неактивной 'disabled' (длина Recovery Cipher < 4 символов).
    8. Проверить: отправка формы не происходит.
    9. Проверить: данные не сохраняются в localStorage.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.CALLSIGN_KNOPA)
    restore_page.enter_recovery_cipher(cipher=data.SQL_INJECTION_PAYLOAD)
    restore_page.enter_new_access_code(new_code=data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_KNOPA)

    # ✅ ASSERT
    restore_page.verify_field_value(
        element=restore_page.recovery_cipher_input, expected_value="OR"
    )

    restore_page.verify_button_state(
        element=restore_page.restore_access_btn, is_disabled=True
    )
    restore_page.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_KNOPA, check_local=True, should_exist=False
    )
