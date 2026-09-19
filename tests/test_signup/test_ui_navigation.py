import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🟢 Состояние страницы при загрузке")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.ui_navigation
def test_initial_page_state(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Оценить начальное состояние страницы при загрузке.
    3. Проверить: наличие подзаголовка 'Phase 1: Operator Identity'.
    4. Проверить: поле 'Callsign' пустое и 'readonly'.
    5. Проверить: поле 'Function' пустое и 'readonly'.
    6. Проверить: кнопка 'PROCEED' неактивна (disabled).
    7. Проверить: текст телеметрии '> SYSTEM READY. AWAITING OPERATOR REGISTRATION' синего цвета.
    """

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.page_subtitle, expected_text=data.PHASE_1_IDENTITY
    )
    signup_page.verify_empty_field_state(
        element=signup_page.callsign_input, is_readonly=True
    )
    signup_page.verify_empty_field_state(
        element=signup_page.function_input, is_readonly=True
    )
    signup_page.verify_button_state(element=signup_page.proceed_btn, is_disabled=True)
    signup_page.verify_telemetry_text(
        expected_text=data.BLUE_TELEMETRY_AWAITING_OPERATOR
    )
    signup_page.verify_telemetry_color_not_cassandra(blue=True)


@allure.id("CAS-02")
@allure.title("🟢 Состояние формы на Шаге 2")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.ui_navigation
def test_initial_step_2_state(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Проверить: поля 'Access Code', 'Confirm Access Code' и 'Recovery Cipher' пустые.
    4. Проверить: кнопка 'COMPLETE REGISTRATION' неактивна (disabled).
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_empty_field_state(
        element=signup_page.access_code_input, is_readonly=False
    )
    signup_page.verify_empty_field_state(
        element=signup_page.confirm_access_code_input, is_readonly=False
    )
    signup_page.verify_empty_field_state(
        element=signup_page.recovery_cipher_input, is_readonly=False
    )
    signup_page.verify_button_state(
        element=signup_page.proceed_btn,
        is_disabled=True,
    )


@allure.id("CAS-03")
@allure.title("⚡ Реактивное состояние кнопки 'PROCEED'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.ui_navigation
def test_reactive_button_state(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести <4 символов в поле 'Full Name'.
    3. Выбрать 'ENGINEER' в поле 'Role'.
    4. Проверить: кнопка 'PROCEED' неактивна.
    5. Очистить поле 'Full Name'.
    6. Ввести 4 символа в поле 'Full Name'.
    7. Проверить: кнопка 'PROCEED' становится активной.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.FULL_NAME_TOO_SHORT_3_CHARS)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.proceed_btn,
        is_disabled=True,
    )

    # ⚡ ACT
    signup_page.enter_full_name(
        name=data.FULL_BNAME_MIN_VALID_4_CHARS, clear_first=True
    )

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.proceed_btn,
        is_disabled=False,
    )


@allure.id("CAS-04")
@allure.title("⚡ Реактивное состояние кнопки 'COMPLETE REGISTRATION'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.ui_navigation
def test_reactive_complete_button_state(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Ввести < 4 символов в поля 'Access Code', 'Confirm Access Code' и 'Recovery Cipher'.
    4. Проверить: кнопка 'COMPLETE REGISTRATION' неактивна.
    5. Ввести 4 символа в поля 'Access Code', 'Confirm Access Code' и 'Recovery Cipher'.
    6. Проверить: кнопка 'COMPLETE REGISTRATION' становится активной.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(access_code=data.ACCESS_CODE_TOO_SHORT_3_CHARS)
    signup_page.enter_confirm_access_code(
        confirm_code=data.ACCESS_CODE_TOO_SHORT_3_CHARS
    )
    signup_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_TOO_SHORT_3_CHARS)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.complete_btn,
        is_disabled=True,
    )

    # ⚡ ACT
    signup_page.enter_access_code(access_code=data.ACCESS_CODE_MIN_VALID_4_CHARS)
    signup_page.enter_confirm_access_code(
        confirm_code=data.ACCESS_CODE_MIN_VALID_4_CHARS
    )
    signup_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_MIN_VALID_4_CHARS)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.complete_btn,
        is_disabled=False,
    )


@allure.id("CAS-05")
@allure.title("🔙 Кнопка BACK возвращает на Шаг 1")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.ui_navigation
def test_back_button_to_step_1(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Нажать на кнопку '← BACK TO OPERATOR DATA'.
    4. Проверить: Шаг 1 видим, Шаг 2 скрыт.
    5. Проверить: подзаголовок 'Phase 1: Operator Identity'.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.click_back()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.page_subtitle, expected_text=data.PHASE_1_IDENTITY
    )


@allure.id("CAS-06")
@allure.title("👁️ Переключение видимости полей пароля")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.ui_navigation
def test_toggle_password_visibility(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Ввести текст в поля 'Access Code' и 'Confirm Access Code'.
    4. Нажать кнопки 'Toggle Password' для обоих полей.
    5. Проверить: тип полей меняется с 'password' на 'text'.
    6. Нажать кнопки 'Toggle Password' для обоих полей еще раз.
    7. Проверить: тип полей меняется обратно с 'text' на 'password'.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(access_code=data.ACCESS_CODE_NOVA)
    signup_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_NOVA)
    signup_page.click_toggle_access_code()
    signup_page.click_toggle_confirm_code()

    # ✅ ASSERT
    signup_page.verify_field_type_after_toggle(access_code=True, expected_type="text")
    signup_page.verify_field_type_after_toggle(confirm_code=True, expected_type="text")

    # ⚡ ACT
    signup_page.click_toggle_access_code()
    signup_page.click_toggle_confirm_code()

    # ✅ ASSERT
    signup_page.verify_field_type_after_toggle(
        access_code=True, expected_type="password"
    )
    signup_page.verify_field_type_after_toggle(
        confirm_code=True, expected_type="password"
    )


@allure.id("CAS-07")
@allure.title("🔭 Успешная навигация на страницу `Log In`")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.ui_navigation
def test_successful_navigation_to_the_log_in(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Нажать на угловую кнопку 'Log In'.
    3. Проверить: URL страницы изменился на 'login.html'.
    """

    # ⚡ ACT
    signup_page.click_log_in()

    # ✅ ASSERT
    signup_page.wait_for_url(expected_url_part=data.LOGIN_URL)


@allure.id("CAS-08")
@allure.title("🔑 Успешная навигация на страницу `Access Restoration`.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.ui_navigation
def test_successful_navigation_to_the_access_restoration(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Нажать на угловую кнопку 'Restore'.
    3. Проверить: URL страницы изменился на 'access-restoration.html'.
    """

    # ⚡ ACT
    signup_page.click_restore()

    # ✅ ASSERT
    signup_page.wait_for_url(expected_url_part=data.ACCESS_RESTORATION_URL)
