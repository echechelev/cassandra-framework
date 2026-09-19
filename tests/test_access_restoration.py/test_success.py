import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("✅ Успешное восстановление доступа для KNOPA")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.success
def test_restoration_happy_path(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести 'KNOPA' в поле 'Callsign'.
    3. Ввести 'AERO' в поле 'Recovery Cipher'.
    4. Ввести 'AERO_99' в поле 'New Access Code'.
    5. Ввести 'AERO_99' в поле 'Confirm Access Code'.
    6. Нажать кнопку 'RESTORE ACCESS' (ожидая успешного завершения).
    7. Проверить: наличие сообщения '✅ Access Protocol Verified'.
    8. Проверить: текст телеметрии изменился на '> RESTORATION COMPLETE...' и стал зелёным.
    9. Проверить: данные в блоке сводки (Summary Block) корректны.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.NAME_KNOPA)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_KNOPA)
    restore_page.enter_new_access_code(new_code=data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_KNOPA)

    # ⚡ ACT
    restore_page.click_restore_access()

    # ✅ ASSERT
    restore_page.verify_text(
        element=restore_page.success_message,
        expected_text=data.PROTOCOL_VERIFIED,
    )
    restore_page.verify_telemetry_color_not_cassandra(green=True)
    restore_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_RESTORATION_COMPLETE
    )
    restore_page.verify_restoration_summary(
        expected_callsign=data.CALLSIGN_KNOPA,
        expected_role=data.ROLE_DISPLAY_PILOT,
        expected_function=data.FUNCTION_PILOT,
        expected_id=data.OPERATOT_ID_KNOPA,
        expected_new_code=data.ACCESS_CODE_KNOPA,
    )


@allure.id("CAS-02")
@allure.title("💾 Проверка данных в localStorage после успеха")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.success
def test_data_saved_in_localstorage(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести 'KNOPA' в поле 'Callsign'.
    3. Ввести 'AERO' в поле 'Recovery Cipher'.
    4. Ввести 'AERO_99' в поле 'New Access Code'.
    5. Ввести 'AERO_99' в поле 'Confirm Access Code'.
    6. Нажать кнопку 'RESTORE ACCESS' (ожидая успешного завершения).
    7. Проверить: в localStorage существует ключ 'restoredUsers'.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(callsign=data.CALLSIGN_KNOPA)
    restore_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_KNOPA)
    restore_page.enter_new_access_code(new_code=data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_KNOPA)

    # ⚡ ACT
    restore_page.click_restore_access()

    # ✅ ASSERT
    restore_page.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_KNOPA, check_local=True
    )
