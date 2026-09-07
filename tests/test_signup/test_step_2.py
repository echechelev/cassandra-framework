import allure
import pytest

from tests import data


@allure.id("CAS-10")
@allure.title("➡️ Успешный переход на Шаг 2")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_2
def test_successful_transition_to_step_2(signup_page):
    """
    Сценарий:
    1. Ввести имя 'Nova' в поле 'Full name'.
    2. Выбрать 'ENGINEER' в поле 'Role'.
    3. Нажать на кнопку 'PROCEED'.
    4. Проверяем: наличие подзаголовка 'Phase 2: Security Setup'.
    5. Проверяем: текст телеметрии.
    6. Проверяем: цвет текста телеметрии синий.

    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)

    # ⚡ ACT
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.page_subtitle, expected_text=data.SUBTITLE_PHASE_2
    )
    signup_page.verify_telemetry_text(expected_text=data.TELEMETRY_AWAITING_SECURITY)
    signup_page.verify_telemetry_color_not_cassandra(blue=True)


@allure.id("CAS-11")
@allure.title("🔀 Невалидный 'Access Code' (несовпадение)")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_2
def test_access_codes_mismatch(signup_page_step_2):
    """
    Сценарий:
    1. Ввести 'QUASAR_5'в поле 'Access Code'.
    2. Ввести 'WRONG_CODE' в поле 'Confirm Access Code'.
    3. Ввести 'COMETA' в поле 'Recovery Cipher'.
    4. Нажать кнопку 'COMPLETE REGISTRATION'.
    5. Проверяем: текст ошибки в заголовке формы.
    6. Проверяем: текст телеметрии.
    7. Проверяем: цвет текста красный.
    """

    # 🎬 ARRANGE
    signup_page_step_2.enter_access_code(code=data.ACCESS_CODE_NOVA)
    signup_page_step_2.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_WRONG)
    signup_page_step_2.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_NOVA)

    # ⚡ ACT
    signup_page_step_2.click_complete_registration()

    # ✅ ASSERT
    signup_page_step_2.verify_text(
        element=signup_page_step_2.error_security_message,
        expected_text=data.ERROR_ACCESS_CODES_MISMATCH,
    )
    signup_page_step_2.verify_telemetry_text(
        expected_text=data.TELEMETRY_ERROR_CODES_MISMATCH
    )
    signup_page_step_2.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-12")
@allure.title("❌ Невалидный 'Access Code' (неверное значение)")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_2
def test_invalid_access_code_value(signup_page_step_2):
    """
    Сценарий:
    1. Ввести 'WRONG_CODE'в поле 'Access Code'.
    2. Ввести 'WRONG_CODE' в поле 'Confirm Access Code'.
    3. Ввести 'COMETA' в поле 'Recovery Cipher'.
    4. Нажать кнопку 'COMPLETE REGISTRATION'.
    5. Проверяем: текст ошибки в заголовке формы.
    6. Проверяем: текст телеметрии.
    7. Проверяем: цвет текста красный.
    """

    # 🎬 ARRANGE
    signup_page_step_2.enter_access_code(code=data.ACCESS_CODE_WRONG)
    signup_page_step_2.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_WRONG)
    signup_page_step_2.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_NOVA)

    # ⚡ ACT
    signup_page_step_2.click_complete_registration()

    # ✅ ASSERT
    signup_page_step_2.verify_text(
        element=signup_page_step_2.error_security_message,
        expected_text=data.ERROR_ACCESS_CODE_INVALID,
    )
    signup_page_step_2.verify_telemetry_text(
        expected_text=data.TELEMETRY_ERROR_INVALID_ACCESS_CODE
    )
    signup_page_step_2.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-13")
@allure.title("🔑 Невалидный 'Recovery Cipher'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_2
def test_invalid_recovery_cipher(signup_page_step_2):
    """
    Сценарий:
    1. Ввести 'QUASAR_5'в поле 'Access Code'.
    2. Ввести 'QUASAR_5' в поле 'Confirm Access Code'.
    3. Ввести 'WRONG_CODE' в поле 'Recovery Cipher'.
    4. Нажать кнопку 'COMPLETE REGISTRATION'.
    5. Проверяем: текст ошибки в заголовке формы.
    6. Проверяем: текст телеметрии.
    7. Проверяем: цвет текста красный.
    """

    # 🎬 ARRANGE
    signup_page_step_2.enter_access_code(code=data.ACCESS_CODE_NOVA)
    signup_page_step_2.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_NOVA)
    signup_page_step_2.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_WRONG)

    # ⚡ ACT
    signup_page_step_2.click_complete_registration()

    # ✅ ASSERT
    signup_page_step_2.verify_text(
        element=signup_page_step_2.error_security_message,
        expected_text=data.ERROR_RECOVERY_CIPHER_INVALID,
    )
    signup_page_step_2.verify_telemetry_text(
        expected_text=data.TELEMETRY_ERROR_INVALID_RECOVERY_CIPHER
    )
    signup_page_step_2.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-14")
@allure.title("🔙 Невалидный 'Recovery Cipher'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_2
def test_back_button_returns_to_step_1(signup_page_step_2):
    """
    Сценарий:
    1. Нажать кнопку '← BACK TO OPERATOR DATA'.
    2. Проверяем: наличие подзаголовка 'Phase 1: Operator Identity'.
    3. Проверяем: данные формы 1 сохранены.
    4. Жмем на кнопку 'PROCEED'.
    5 Проверяем: наличие подзаголовка 'Phase 2: Security Setup'.
    6. Проверяем: все поля формы 2 пустые.
    """

    # ⚡ ACT
    signup_page_step_2.click_back()

    # ✅ ASSERT
    signup_page_step_2.verify_text(
        element=signup_page_step_2.page_subtitle, expected_text=data.SUBTITLE_PHASE_1
    )
    signup_page_step_2.verify_step_1_fields(
        expected_full_name=data.NAME_NOVA,
        expected_callsign=data.CALLSIGN_NOVA,
        expected_role=data.ROLE_ENGINEER,
        expected_function=data.FUNCTION_ENGINEER,
    )

    # ⚡ ACT
    signup_page_step_2.click_proceed()

    # ✅ ASSERT
    signup_page_step_2.verify_text(
        element=signup_page_step_2.page_subtitle, expected_text=data.SUBTITLE_PHASE_2
    )
    signup_page_step_2.verify_step_2_empty_state()


@allure.id("CAS-15")
@allure.title("👁️ Переключение видимости 'Access Code'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_2
def test_toggle_access_code_visibility(signup_page_step_2):
    """
    Сценарий:
    1. Ввести текст в 'Access Code'.
    2. Нажать кнопку 'Toggle Password'.
    3. Проверяем: тип поля меняется с 'password' на 'text'
    """

    # 🎬 ARRANGE
    signup_page_step_2.enter_access_code(code=data.ACCESS_CODE_WRONG)

    # ⚡ ACT
    signup_page_step_2.click_toggle_password(access_code=True)

    # ✅ ASSERT
    signup_page_step_2.verify_field_type_after_toggle(access_code=True)


@allure.id("CAS-16")
@allure.title("📏 Проверка максимальной длины поля 'Access Code'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_2
def test_access_code_max_length(signup_page_step_2):
    """
    Сценарий:
    1. Попытаться ввести в поле 'Access Code' более 30 символов..
    6. Проверяем: в поле 'Access Code', остаеться не более 30 символов.
    """

    # ✅ ASSERT
    signup_page_step_2.verify_max_length(
        element=signup_page_step_2.access_code_input, max_length=30
    )


@allure.id("CAS-17")
@allure.title("📏 Проверка максимальной длины поля 'Recovery Cipher'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_2
def test_recovery_cipher_max_length(signup_page_step_2):
    """
    Сценарий:
    1. Попытаться ввести в поле 'Recovery Cipher' более 30 символов..
    6. Проверяем: в поле 'Recovery Cipher', остаеться не более 30 символов.
    """

    # ✅ ASSERT
    signup_page_step_2.verify_max_length(
        element=signup_page_step_2.recovery_cipher_input, max_length=30
    )
