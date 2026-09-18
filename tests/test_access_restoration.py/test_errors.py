import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🔑 Неверный новый код доступа")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.errors
def test_invalid_new_access_code(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести 'KNOPA' в поле 'Callsign'.
    3. Ввести 'AERO' в поле 'Recovery Cipher'.
    4. Ввести неверное значение 'WRONG_CODE' в поле 'New Access Code'.
    5. Ввести такое же неверное значение 'WRONG_CODE' в поле 'Confirm Access Code'.
    6. Нажать кнопку 'RESTORE ACCESS' (wait_for_success=False).
    7. Проверить: текст ошибки в блоке `Restoration Error Block` — `⚠️ Security protocol failed. Invalid credentials provided.`
    8. Проверить: текст телеметрии — `> SECURITY PROTOCOL FAILED. RESTORATION ABORTED`.
    9. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.CALLSIGN_KNOPA)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_KNOPA)
    restore_page.enter_new_access_code(access_code=data.ACCESS_CODE_WRONG)
    restore_page.enter_confirm_access_code(access_code=data.ACCESS_CODE_WRONG)

    # ⚡ ACT
    restore_page.click_restore_access(wait_for_success=False)

    # ✅ ASSERT
    restore_page.verify_telemetry_color_not_cassandra(red=True)
    restore_page.should_show_error_container(
        restore_page.error_message, expected_text=data.RED_ERROR_SECURITY_FAILED
    )
    restore_page.verify_telemetry_text(
        expected_text=data.RED_TELEMETRY_RESTORATION_ABORTED
    )


@allure.id("CAS-02")
@allure.title("🔑 Несовпадение новых ключей доступа")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.errors
def test_access_codes_mismatch(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести 'KNOPA' в поле 'Callsign'.
    3. Ввести 'AERO' в поле 'Recovery Cipher'.
    4. Ввести 'AERO_99' в поле 'New Access Code'.
    5. Ввести неверное значение 'WRONG' в поле 'Confirm Access Code'.
    6. Нажать кнопку 'RESTORE ACCESS' (wait_for_success=False).
    7. Проверить: текст ошибки в блоке `Restoration Error Block` — `⚠️ Security protocol failed...
    8. Проверить: текст телеметрии — `> SECURITY PROTOCOL FAILED. RESTORATION ABORTED`.
    9. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.CALLSIGN_KNOPA)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_KNOPA)
    restore_page.enter_new_access_code(access_code=data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(access_code=data.ACCESS_CODE_WRONG)

    # ⚡ ACT
    restore_page.click_restore_access(wait_for_success=False)

    # ✅ ASSERT
    restore_page.verify_telemetry_color_not_cassandra(red=True)
    restore_page.should_show_error_container(
        restore_page.error_message, expected_text=data.RED_ERROR_SECURITY_FAILED
    )
    restore_page.verify_telemetry_text(
        expected_text=data.RED_TELEMETRY_RESTORATION_ABORTED
    )


@allure.id("CAS-03")
@allure.title("🔐 Неверный шифр восстановления")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.errors
def test_invalid_recovery_cipher(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести 'KNOPA' в поле 'Callsign'.
    3. Ввести неверное значение 'WRONG' в поле 'Recovery Cipher'.
    4. Ввести 'AERO_99' в поле 'New Access Code'.
    5. Ввести 'AERO_99' в поле 'Confirm Access Code'.
    6. Нажать кнопку 'RESTORE ACCESS' (wait_for_success=False).
    7. Проверить: текст ошибки в блоке `Restoration Error Block` — `⚠️ Security protocol failed..`
    8. Проверить: текст телеметрии — `> SECURITY PROTOCOL FAILED. RESTORATION ABORTED`.
    9. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.CALLSIGN_KNOPA)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_WRONG)
    restore_page.enter_new_access_code(access_code=data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(access_code=data.ACCESS_CODE_KNOPA)

    # ⚡ ACT
    restore_page.click_restore_access(wait_for_success=False)

    # ✅ ASSERT
    restore_page.verify_telemetry_color_not_cassandra(red=True)
    restore_page.should_show_error_container(
        restore_page.error_message, expected_text=data.RED_ERROR_SECURITY_FAILED
    )
    restore_page.verify_telemetry_text(
        expected_text=data.RED_TELEMETRY_RESTORATION_ABORTED
    )


@allure.id("CAS-04")
@allure.title("🔁 Попытка повторного восстановления доступа")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.errors
def test_user_already_restored(restore_page):
    """
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести 'KNOPA' в поле 'Callsign', 'AERO' в поле 'Recovery Cipher'.
    3. Ввести 'AERO_99' в поле 'New Access Code' и 'AERO_99' в поле 'Confirm Access Code'.
    4. Нажать кнопку 'RESTORE ACCESS' (wait_for_success=True).
    5. Проверить: в localStorage['restoredUsers'] появилась запись с ключом 'KNOPA'.
    6. Обновить страницу (F5).
    7. Ввести 'KNOPA' в поле 'Callsign', 'AERO' в поле 'Recovery Cipher'.
    8. Ввести 'AERO_99' в поле 'New Access Code' и 'AERO_99' в поле 'Confirm Access Code'.
    9. Нажать кнопку 'RESTORE ACCESS' (wait_for_success=False).
    10. Проверить: текст ошибки в блоке `Restoration Error Block` —
    `⚠️ Operator KNOPA has already been restored. Please use your new credentials to log in.`
    11. Проверить: текст телеметрии — `> SECURITY PROTOCOL FAILED. OPERATOR ALREADY RESTORED.`
    12. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.CALLSIGN_KNOPA)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_KNOPA)
    restore_page.enter_new_access_code(data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(data.ACCESS_CODE_KNOPA)

    # ⚡ ACT
    restore_page.click_restore_access()

    # ✅ ASSERT
    restore_page.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_KNOPA, check_local=True
    )

    # ⚡ ACT
    restore_page.click_refresh_page()
    restore_page.enter_callsign(callsign=data.CALLSIGN_KNOPA)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_KNOPA)
    restore_page.enter_new_access_code(data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(data.ACCESS_CODE_KNOPA)
    restore_page.click_restore_access(wait_for_success=False)

    # ✅ ASSERT
    restore_page.verify_telemetry_color_not_cassandra(red=True)
    restore_page.should_show_error_container(
        restore_page.error_message, expected_text=data.RED_ERROR_ALREADY_RESTORED
    )
    restore_page.verify_telemetry_text(
        expected_text=data.RED_TELEMETRY_OPERATOR_RESTORED
    )


@allure.id("CAS-05")
@allure.title("🚫 Попытка восстановления для неизвестного оператора")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.errors
def test_access_restoration_unknown_callsign(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести 'UNKNOWN' в поле 'Callsign'.
    3. Ввести 'AERO' в поле 'Recovery Cipher'.
    4. Ввести 'AERO_99' в поле 'New Access Code'.
    5. Ввести 'AERO_99' в поле 'Confirm Access Code'.
    6. Нажать кнопку 'RESTORE ACCESS'.
    7. Проверить: текст ошибки в блоке `Restoration Error Block` — `⚠️ Restoration unavailable...
    8. Проверить: текст телеметрии — `> SECURITY PROTOCOL FAILED. RESTORATION ABORTED`.
    9. Проверить: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.CALLSIGN_WRONG)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_KNOPA)
    restore_page.enter_new_access_code(access_code=data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(access_code=data.ACCESS_CODE_KNOPA)

    # ⚡ ACT
    restore_page.click_restore_access(wait_for_success=False)

    # ✅ ASSERT
    restore_page.verify_telemetry_color_not_cassandra(red=True)
    restore_page.should_show_error_container(
        restore_page.error_message, expected_text=data.RED_ERROR_ACCESS_RECOVERY
    )
    restore_page.verify_telemetry_text(
        expected_text=data.RED_TELEMETRY_RESTORATION_ABORTED
    )
