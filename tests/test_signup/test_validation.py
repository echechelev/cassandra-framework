import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("📏 Позывной короче минимальной длины")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_callsign_shorter_than_min_length(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 3 символа в поле 'Full Name'.
    3. Выбрать 'ENGINEER' в поле 'Role'.
    4. Проверить: кнопка 'PROCEED' неактивна (disabled).
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.CALLSIGN_TOO_SHORT_3_CHARS)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.proceed_btn,
        is_disabled=True,
    )


@allure.id("CAS-02")
@allure.title("📏 Код доступа короче минимальной длины")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_access_code_shorter_than_min_length(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Заполнить Шаг 1 валидными данными и перейти на Шаг 2.
    3. Ввести 3 символа в 'Access Code'.
    4. Ввести валидные данные в 'Confirm Access Code'.
    5. Ввести валидные данные в 'Recovery Cipher'.
    6. Проверить: кнопка 'COMPLETE REGISTRATION' неактивна (disabled).
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(code=data.ACCESS_CODE_TOO_SHORT_3_CHARS)
    signup_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_NOVA)
    signup_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_NOVA)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.complete_btn,
        is_disabled=True,
    )


@allure.id("CAS-03")
@allure.title("📏 Подтверждение кода доступа короче минимальной длины")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_confirm_code_shorter_than_min_length(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Заполнить Шаг 1 валидными данными и перейти на Шаг 2.
    3. Ввести валидные данные в 'Access Code'.
    4. Ввести 3 символа в 'Confirm Access Code'.
    5. Ввести Ввести валидные в 'Recovery Cipher'.
    6. Проверить: кнопка 'COMPLETE REGISTRATION' неактивна (disabled).
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(code=data.ACCESS_CODE_NOVA)
    signup_page.enter_confirm_access_code(
        confirm_code=data.ACCESS_CODE_TOO_SHORT_3_CHARS
    )
    signup_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_NOVA)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.complete_btn,
        is_disabled=True,
    )


@allure.id("CAS-04")
@allure.title("📏 Шифр доступа короче минимальной длины")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_recovery_cipher_shorter_than_min_length(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Заполнить Шаг 1 валидными данными и перейти на Шаг 2.
    3. Ввести валидные данные в 'Access Code'.
    4. Ввести валидные данные в 'Confirm Access Code'.
    5. Ввести 3 символа в 'Recovery Cipher'.
    6. Проверить: кнопка 'COMPLETE REGISTRATION' неактивна (disabled).
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(code=data.ACCESS_CODE_NOVA)
    signup_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_NOVA)
    signup_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_TOO_SHORT_3_CHARS)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.complete_btn,
        is_disabled=True,
    )


@allure.id("CAS-05")
@allure.title("🌌 Пустой позывной при выбранной роли")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_empty_callsign_with_role_selected(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Оставить поле 'Full Name' пустым.
    3. Выбрать 'ENGINEER' в поле 'Role'.
    4. Проверить: кнопка 'PROCEED' неактивна (disabled).
    """

    # 🎬 ARRANGE
    signup_page.select_role(role_value=data.ROLE_ENGINEER)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.complete_btn,
        is_disabled=True,
    )


@allure.id("CAS-06")
@allure.title("🌌 Пустая роль при заполненном позывном")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_empty_role_with_callsign_filled(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name'.
    3. Оставить поле 'Role' пустым (не выбирать значение).
    4. Проверить: кнопка 'PROCEED' неактивна (disabled).
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(data.NAME_NOVA)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.complete_btn,
        is_disabled=True,
    )


@allure.id("CAS-07")
@allure.title("🗝️ Пустой код доступа при заполненных остальных полях")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_empty_access_code_with_other_fields_filled(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Заполнить Шаг 1 валидными данными и перейти на Шаг 2.
    3. Оставить поле 'Access Code' пустым.
    4. Ввести валидные данные в поле 'Confirm Access Code'.
    5. Ввести валидные данные в в поле 'Recovery Cipher'.
    6. Проверить: кнопка 'COMPLETE REGISTRATION' неактивна (disabled).
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_NOVA)
    signup_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_NOVA)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.complete_btn,
        is_disabled=True,
    )


@allure.id("CAS-08")
@allure.title("🗝️ Пустое подтверждение кода при заполненных остальных полях")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_empty_confirm_code_with_other_fields_filled(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Заполнить Шаг 1 валидными данными и перейти на Шаг 2.
    3. Ввести валлидные данные в поле 'Access Code'.
    4. Оставить поле 'Confirm Access Code' пустым.
    5. Ввести валидные данные в поле 'Recovery Cipher'.
    6. Проверить: кнопка 'COMPLETE REGISTRATION' неактивна (disabled).
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(code=data.ACCESS_CODE_NOVA)
    signup_page.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_NOVA)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.complete_btn,
        is_disabled=True,
    )


@allure.id("CAS-09")
@allure.title("🗝️ Пустой шифр при заполненных остальных полях")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_empty_recovery_cipher_with_other_fields_filled(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Заполнить Шаг 1 валидными данными и перейти на Шаг 2.
    3. Ввести валидные данные в поле 'Access Code'.
    4. Ввести валидные данные в поле 'Confirm Access Code'.
    5. Оставить поле 'Recovery Cipher' пустым.
    6. Проверить: кнопка 'COMPLETE REGISTRATION' неактивна (disabled).
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(code=data.ACCESS_CODE_NOVA)
    signup_page.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_NOVA)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.complete_btn,
        is_disabled=True,
    )


@allure.id("CAS-10")
@allure.title("📏 Проверка максимальной длины поля 'Full Name'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_full_name_max_length_boundary(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Попытаться ввести в поле 'Full Name' более 100 символов.
    3. Проверить: в поле 'Full Name' остаётся не более 100 символов.
    """

    # ✅ ASSERT
    signup_page.verify_max_length(element=signup_page.full_name_input, max_length=100)


@allure.id("CAS-11")
@allure.title("📏 Проверка максимальной длины поля 'Access Code'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_access_code_max_length(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Попытаться ввести в поле 'Access Code' более 30 символов.
    4. Проверить: в поле 'Access Code' остаётся не более 30 символов.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_max_length(element=signup_page.access_code_input, max_length=30)


@allure.id("CAS-12")
@allure.title("📏 Проверка максимальной длины поля 'Confirm Access Code'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_confirm_code_max_length(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Попытаться ввести в поле 'Confirm Access Code' более 30 символов.
    4. Проверить: в поле 'Confirm Access Code' остаётся не более 30 символов.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_max_length(
        element=signup_page.confirm_access_code_input, max_length=30
    )


@allure.id("CAS-13")
@allure.title("📏 Проверка максимальной длины поля 'Recovery Cipher'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_recovery_cipher_max_length(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести 'Nova' в поле 'Full Name', выбрать 'ENGINEER' в поле 'Role', нажать 'PROCEED'.
    3. Попытаться ввести в поле 'Recovery Cipher' более 30 символов.
    4. Проверить: в поле 'Recovery Cipher' остаётся не более 30 символов.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_max_length(
        element=signup_page.recovery_cipher_input, max_length=30
    )


@allure.id("CAS-14")
@allure.title("🛡️ Санитизация ввода — попытка ввести спецсимволы в поле Recovery Cipher")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_input_sanitization_recovery_cipher(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Заполнить Шаг 1 валидными данными и перейти на Шаг 2.
    3. Ввести строку с спецсимволами "' OR '1'='1'" в поле 'Recovery Cipher'.
    4. Ввести валидные данные в 'Access Code' и 'Confirm Access Code'.
    6. Проверить: фронтенд автоматически отсекает спецсимволы и цифры — в поле остаётся только 'OR' (2 символа).
    7. Проверить: кнопка 'COMPLETE REGISTRATION' остаётся неактивной 'disabled'  < 4 символов.
    9. Проверить: данные не сохраняются в 'localStorage'.
    8. Проверить: отправка формы не происходит.
    9. Проверить: данные не сохраняются в 'localStorage'.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)
    signup_page.click_proceed()

    # ⚡ ACT
    signup_page.enter_access_code(data.ACCESS_CODE_NOVA)
    signup_page.enter_confirm_access_code(data.ACCESS_CODE_NOVA)
    signup_page.enter_recovery_cipher(data.SQL_INJECTION_PAYLOAD)

    # ✅ ASSERT
    signup_page.verify_button_state(signup_page.complete_btn, is_disabled=True)
    signup_page.verify_field_value(
        element=signup_page.recovery_cipher_input, expected_value="OR"
    )
    signup_page.verify_user_saved_in_storage(is_saved=False, check_local=True)


@allure.id("CAS-15")
@allure.title("🤖 Автогенерация 'Callsign' из 'Full Name'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_callsign_auto_generation(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Ввести имя 'Nova' в поле 'Full Name'.
    3. Проверить: поле 'Callsign' автоматически заполняется значением 'NOVA'.
    """

    # ⚡ ACT
    signup_page.enter_full_name(name=data.NAME_NOVA)

    # ✅ ASSERT
    signup_page.verify_input_value(
        element=signup_page.callsign_input,
        expected_value=data.CALLSIGN_NOVA,
    )


@allure.id("CAS-16")
@allure.title("🤖 Автозаполнение 'Function' при выборе 'Role'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.validation
def test_function_auto_fill_on_role_select(signup_page):
    """
    Сценарий:
    1. Перейти на страницу 'Signup page'.
    2. Выбрать 'ENGINEER' в выпадающем списке поля 'Role'.
    3. Проверить: поле 'Function' автоматически заполняется значением 'Systems Engineering'.
    """

    # ⚡ ACT
    signup_page.select_role(role_value=data.ROLE_ENGINEER)

    # ✅ ASSERT
    signup_page.verify_input_value(
        element=signup_page.function_input,
        expected_value=data.FUNCTION_ENGINEER,
    )
