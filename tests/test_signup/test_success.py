import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("➡️ Успешный переход на Шаг 2")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.success
def test_successful_transition_to_step_2(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести имя 'Nova' в поле 'Full Name'.
    3. Выбрать 'ENGINEER' в поле 'Role'.
    4. Нажать на кнопку 'PROCEED'.
    5. Проверить: наличие подзаголовка 'Phase 2: Security Setup'.
    6. Проверить: текст телеметрии — `> SYSTEM READY. AWAITING SECURITY REGISTRATION`.
    7. Проверить: цвет текста телеметрии синий.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)

    # ⚡ ACT
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.page_subtitle, expected_text=data.PHASE_2_SECURITY
    )
    signup_page.verify_telemetry_text(
        expected_text=data.BLUE_TELEMETRY_AWAITING_SECURITY
    )
    signup_page.verify_telemetry_color_not_cassandra(blue=True)


@allure.id("CAS-02")
@allure.title("🎉 Успешная регистрация Nova")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.success
def test_successful_registration_nova(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Ввести 'QUASAR_5' в поле 'Access Code'.
    4. Ввести 'QUASAR_5' в поле 'Confirm Access Code'.
    5. Ввести 'COMETA' в поле 'Recovery Cipher'.
    6. Нажать кнопку 'COMPLETE REGISTRATION'.
    7. Проверить: Шаг 3 видим, подзаголовок 'Welcome aboard, new Operator.' (зеленый цвет).
    8. Проверить: текст телеметрии — `> REGISTRATION COMPLETE. OPERATOR ACCOUNT ACTIVATED.`
    9. Проверить: цвет текста телеметрии зеленый.
    10. Проверить: поля сводки — Callsign: NOVA, Full Name: Nova,
    Role: ⚙️ Engineer, Function: Systems Engineering, Access Level: 3, Operator ID: 512-3A.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(data.ACCESS_CODE_NOVA)
    signup_page.enter_confirm_access_code(data.ACCESS_CODE_NOVA)
    signup_page.enter_recovery_cipher(data.RECOVERY_CIPHER_NOVA)
    signup_page.click_complete_registration()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.page_subtitle,
        expected_text=data.WELCOME_OPERATOR,
    )
    signup_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_REGISTRATION_COMPLETE
    )
    signup_page.verify_telemetry_color_not_cassandra(green=True)
    signup_page.verify_step_3_summary(
        expected_callsign=data.CALLSIGN_NOVA,
        expected_full_name=data.NAME_NOVA,
        expected_role=data.ROLE_DISPLAY_ENGINEER,
        expected_function=data.FUNCTION_ENGINEER,
        expected_level=data.ACCESS_LEVEL_ENGINEER,
        expected_id=data.OPERATOR_ID_NOVA,
    )


@allure.id("CAS-03")
@allure.title("🗄️ Проверка данных в 'localStorage' после регистрации")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.success
def test_verify_local_storage_after_launch(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Ввести 'QUASAR_5' в поле 'Access Code', 'QUASAR_5' в поле 'Confirm Access Code',
    'COMETA' в поле 'Recovery Cipher'.
    4. Нажать кнопку 'COMPLETE REGISTRATION'.
    5. Проверить: в 'localStorage' по ключу 'registeredUsers' сохранен объект оператора 'NOVA'.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(data.ACCESS_CODE_NOVA)
    signup_page.enter_confirm_access_code(data.ACCESS_CODE_NOVA)
    signup_page.enter_recovery_cipher(data.RECOVERY_CIPHER_NOVA)
    signup_page.click_complete_registration()

    # ✅ ASSERT
    signup_page.verify_user_data_in_storage(
        expected_callsign=data.NAME_NOVA, check_local=True
    )
