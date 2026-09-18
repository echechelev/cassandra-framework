import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("📋 Состояние страницы при загрузке")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.ui_navigation
def test_initial_page_state(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Проверить: виден подзаголовок 'Access Restoration Protocol'.
    3. Проверить: поля 'Callsign', 'Recovery Cipher', 'New Access Code', 'Confirm Access Code' пустые.
    4. Проверить: кнопка 'RESTORE ACCESS' неактивна (disabled).
    5. Проверить: телеметрия синего цвета с текстом '> SYSTEM READY. AWAITING RESTORATION PROTOCOL'.
    """

    # ✅ ASSERT
    restore_page.verify_text(
        element=restore_page.page_subtitle,
        expected_text=data.RESTORATION_PROTOCOL,
    )
    restore_page.verify_empty_field_state(
        element=restore_page.callsign_input, is_readonly=False
    )
    restore_page.verify_empty_field_state(
        element=restore_page.recovery_cipher_input, is_readonly=False
    )
    restore_page.verify_empty_field_state(
        element=restore_page.new_access_code_input, is_readonly=False
    )
    restore_page.verify_empty_field_state(
        element=restore_page.confirm_access_code_input, is_readonly=False
    )
    restore_page.verify_button_state(
        element=restore_page.restore_access_btn, is_disabled=True
    )
    restore_page.verify_telemetry_text(
        expected_text=data.BLUE_TELEMETRY_AWAITING_RESTORATION
    )
    restore_page.verify_telemetry_color_not_cassandra(blue=True)


@allure.id("CAS-02")
@allure.title("⚡ Реактивное состояние кнопки 'RESTORE ACCESS'.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.ui_navigation
def test_reactive_button_state(restore_page):
    """
    Сценарий:
    1. Перейти на страницу `Access Restoration`.
    2. Ввести <4 символов в поле 'CALLSIGN'.
    3. Ввести <4 символов в поле 'RECOVERY CIPHER'.
    4. Ввести в поля 'New Access Code' и 'Confirm Access Code' <4 символов.
    5. Проверить: кнопка 'RESTORE ACCESS' остаётся неактивной `disabled`.
    6. Очистить все поля.
    7. Ввести 4 символа в поле 'CALLSIGN'.
    8. Ввести 4 символа в поле 'RECOVERY CIPHER'.
    9. Ввести в поля 'New Access Code' и 'Confirm Access Code' 4+ символов.
    10. Проверить: кнопка 'RESTORE ACCESS' активна `enabled`.
    """

    # 🎬 ARRANGE
    restore_page.enter_callsign(data.CALLSIGN_TOO_SHORT_3_CHARS)
    restore_page.enter_recovery_cipher(data.RECOVERY_CIPHER_TOO_SHORT_3_CHARS)
    restore_page.enter_new_access_code(data.ACCESS_CODE_TOO_SHORT_3_CHARS)
    restore_page.enter_confirm_access_code(data.ACCESS_CODE_TOO_SHORT_3_CHARS)

    # ✅ ASSERT
    restore_page.should_be_restore_access_btn(is_enabled=False)

    # ⚡ ACT
    restore_page.enter_callsign(data.CALLSIGN_MIN_VALID_4_CHARS, clear_first=True)
    restore_page.enter_recovery_cipher(
        data.RECOVERY_CIPHER_MIN_VALID_4_CHARS, clear_first=True
    )
    restore_page.enter_new_access_code(
        data.ACCESS_CODE_MIN_VALID_4_CHARS, clear_first=True
    )
    restore_page.enter_confirm_access_code(
        data.ACCESS_CODE_MIN_VALID_4_CHARS, clear_first=True
    )

    # ✅ ASSERT
    restore_page.should_be_restore_access_btn(is_enabled=True)


@allure.id("CAS-03")
@allure.title("👁️ Переключение видимости полей пароля")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.ui_navigation
def test_toggle_access_code_visibility(restore_page):
    """
    Сценарий:
    1. Перейти на страницу 'Access Restoration'.
    2. Ввести текст 'AERO_99' в поле 'New Access Code'.
    3. Ввести текст 'AERO_99' в поле 'Confirm Access Code'.
    4. Нажать на кнопки 'Toggle Password' (иконка глаза).
    5. Проверить: символы в полях, становятся видимыми (тип меняется на 'text').
    6. Нажать повторно на кнопки 'Toggle Password' (иконка глаза).
    7. Проверить: при повторном клике символы в полях скрываются (тип возвращается к 'password').
    """

    # 🎬 ARRANGE
    restore_page.enter_new_access_code(access_code=data.ACCESS_CODE_KNOPA)
    restore_page.enter_confirm_access_code(access_code=data.ACCESS_CODE_KNOPA)

    # ⚡ ACT
    restore_page.click_toggle_new_and_confirm_access_code(new_access_code=True)
    restore_page.click_toggle_new_and_confirm_access_code(confirm_access_code=True)

    # ✅ ASSERT
    restore_page.verify_field_type_after_toggle_restoration(
        new_access_code=True, expected_type="text"
    )
    restore_page.verify_field_type_after_toggle_restoration(
        confirm_access_code=True, expected_type="text"
    )

    # ⚡ ACT
    restore_page.click_toggle_new_and_confirm_access_code(new_access_code=True)
    restore_page.click_toggle_new_and_confirm_access_code(confirm_access_code=True)

    # ✅ ASSERT
    restore_page.verify_field_type_after_toggle_restoration(
        new_access_code=True, expected_type="password"
    )
    restore_page.verify_field_type_after_toggle_restoration(
        confirm_access_code=True, expected_type="password"
    )


@allure.id("CAS-04")
@allure.title("🔭 Успешная навигация на страницу Log In.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.ui_navigation
def test_navigation_to_login(restore_page):
    """
    Сценарий:
    1. Перейти на странцу 'Access Restoration'.
    2. Нажать на кнопку 'Log in'.
    3. Проверить: происходит навигация, url страницы становится 'login.html'.
    """

    # ⚡ ACT
    restore_page.click_log_in()

    # ✅ ASSERT
    restore_page.wait_for_url(data.LOGIN_URL)


@allure.id("CAS-05")
@allure.title("📡 Успешная навигация на страницу Sign Up.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "access_restoration")
@pytest.mark.regress
@pytest.mark.access_restoration
@pytest.mark.ui_navigation
def test_navigation_to_signup(restore_page):
    """
    Сценарий:
    1. Перейти на странцу 'Access Restoration'.
    2. Нажать на кнопку 'Sign up'.
    3. Проверить: происходит навигация, url страницы становится 'signup.html'.
    """

    # ⚡ ACT
    restore_page.click_sign_up()

    # ✅ ASSERT
    restore_page.wait_for_url(data.SIGNUP_URL)
