import time

import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🟢 Состояние страницы при загрузке")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_1
def test_initial_page_state(signup_page):
    """
    Сценарий:
    1. Оценить начальное состояние страницы 'signup' при загрузке.
    2. Проверяем: наличие подзаголовка 'Phase 1: Operator Identity'.
    3. Проверяем: поле 'Callsign' пустое и 'readonly'.
    4. Проверяем: поле 'Function' пустое и 'readonly'.
    5. Проверяем: кнопка неактивна PROCEED.
    6. Проверяем: текст телеметри.
    7. Проверяем: цвет текста телеметрии синий.
    """

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.page_subtitle, expected_text=data.SUBTITLE_PHASE_1
    )
    signup_page.verify_empty_readonly_field(element=signup_page.callsign_input)
    signup_page.verify_empty_readonly_field(element=signup_page.function_input)
    signup_page.verify_button_state(element=signup_page.proceed_btn, is_disabled=True)
    signup_page.verify_telemetry_text(expected_text=data.TELEMETRY_AWAITING_OPERATOR)
    signup_page.verify_telemetry_color_not_cassandra(blue=True)


@allure.id("CAS-02")
@allure.title("🤖 Автогенерация 'Callsign из 'Full Name'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_1
def test_callsign_auto_generation(signup_page):
    """
    Сценарий:
    1. Ввести имя 'Nova' в поле 'Full Name'.
    2. Проверяем: поле 'Callsign', автоматически заполняется значением 'NOVA'.
    """

    # ⚡ ACT
    signup_page.enter_full_name(name=data.NAME_NOVA)

    # ✅ ASSERT
    signup_page.verify_input_value(
        element=signup_page.callsign_input,
        expected_value=data.CALLSIGN_NOVA,
    )


@allure.id("CAS-03")
@allure.title("🤖 Автозаполнение 'Function' при выборе 'Role'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_1
def test_function_auto_fill_on_role_select(signup_page):
    """
    Сценарий:
    1. Выбрать 'ENGINEER' в выпадающем списке поля 'Role'.
    2. Проверяем: поле 'Function' автоматически заполняется значением 'Systems Engineering'.
    """

    # ⚡ ACT
    signup_page.select_role(role_value=data.ROLE_ENGINEER)

    # ✅ ASSERT
    signup_page.verify_input_value(
        element=signup_page.function_input,
        expected_value=data.FUNCTION_ENGINEER,
    )


@allure.id("CAS-04")
@allure.title("⚡ Реактивное состояние кнопки 'PROCEED'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_1
def test_proceed_button_reactive_state(signup_page):
    """
    Сценарий:
    1. Ввести имя 'Nova' в поле 'Full Name'.
    2. Проверяем: кнопка 'PROCEED' неактивна.
    3. Выбрать 'ENGINEER' в поле 'Role'.
    4. Проверяем: кнопка 'PROCEED' становится активной.
    """

    # ⚡ ACT
    signup_page.enter_full_name(name=data.NAME_NOVA)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.proceed_btn,
        is_disabled=True,
    )

    # ⚡ ACT
    signup_page.select_role(role_value=data.ROLE_ENGINEER)

    # ✅ ASSERT
    signup_page.verify_button_state(
        element=signup_page.proceed_btn,
        is_disabled=False,
    )


@allure.id("CAS-05")
@allure.title("🔒 Блокировка зарезервированного позывного 'AURORA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_1
def test_reserved_callsign_aurora_blocked(signup_page):
    """
    Сценарий:
    1. Ввести имя 'Aurora' в поле 'Full Name'.
    2. Выбрать роль 'SPECIALIST' в поле 'ROLE'.
    3. Нажать на кнопку 'PROCEED'.
    4. Проверяем: текст ошибки в заголовке формы.
    5. Проверяем: текст телеметрии.
    6. Проверяем: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_AURORA)
    signup_page.select_role(role_value=data.ROLE_SPECIALIST)

    # ⚡ ACT
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_message,
        expected_text=data.ERROR_CALLSIGN_AURORA_RESERVED,
    )
    signup_page.verify_telemetry_text(expected_text=data.TELEMETRY_ERROR_AURORA)
    signup_page.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-06")
@allure.title("🔒 Блокировка зарезервированного позывного 'ORION'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_1
def test_reserved_callsign_orion_blocked(signup_page):
    """
    Сценарий:
    1. Ввести имя 'Orion' в поле 'Full Name'.
    2. Выбрать роль 'COMMANDER' в поле 'ROLE'.
    3. Нажать на кнопку 'PROCEED'.
    4. Проверяем: текст ошибки в заголовке формы.
    5. Проверяем: текст телеметрии.
    6. Проверяем: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_ORION)
    signup_page.select_role(role_value=data.ROLE_COMMANDER)

    # ⚡ ACT
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_message,
        expected_text=data.ERROR_CALLSIGN_ORION_RESERVED,
    )
    signup_page.verify_telemetry_text(expected_text=data.TELEMETRY_ERROR_ORION)
    signup_page.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-07")
@allure.title("🚫 Блокировка неверной роли для 'NOVA'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_1
def test_block_invalid_role_for_nova(signup_page):
    """
    Сценарий:
    1. Ввести имя 'Nova' в поле 'Full Name'.
    2. Выбрать роль 'COMMANDER' в поле 'ROLE'.
    3. Нажать на кнопку 'PROCEED'.
    4. Проверяем: текст ошибки в заголовке формы.
    5. Проверяем: текст телеметрии.
    6. Проверяем: цвет текста телеметрии красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_NOVA)
    signup_page.select_role(role_value=data.ROLE_COMMANDER)

    # ⚡ ACT
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_message,
        expected_text=data.ERROR_ROLE_MISMATCH,
    )
    signup_page.verify_telemetry_text(expected_text=data.TELEMETRY_ERROR_ROLE_MISMATCH)
    signup_page.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-08")
@allure.title("🚫 Блокировка неизвестного позывного")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_1
def test_block_unknown_callsign(signup_page):
    """
    Сценарий:
    1. Ввести имя 'Ivan' в поле 'Full Name'.
    2. Выбрать 'ENGINEER' в поле 'Role'.
    3. Нажать на кнопку 'PROCEED'.
    4. Проверяем: текст ошибки в заголовке формы.
    5. Проверяем: текст телеметрии.
    6. Проверяем: цвет текста красный.
    """

    # 🎬 ARRANGE
    signup_page.enter_full_name(name=data.NAME_IVAN)
    signup_page.select_role(role_value=data.ROLE_ENGINEER)

    # ⚡ ACT
    signup_page.click_proceed()

    # ✅ ASSERT
    signup_page.verify_text(
        element=signup_page.error_message,
        expected_text=data.ERROR_CAPACITY_REACHED,
    )
    signup_page.verify_telemetry_text(expected_text=data.TELEMETRY_ERROR_UNKNOWN_USER)
    signup_page.verify_telemetry_color_not_cassandra(red=True)


@allure.id("CAS-09")
@allure.title("📏 Проверка максимальной длины поля 'Full Name'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_1
def test_full_name_max_length_boundary(signup_page):
    """
    Сценарий:
    1. Попытаться ввести в поле 'Full Name' более 100 символов..
    2. Проверяем: в поле 'Full Name', остаеться не более 100 символов.
    """

    # ✅ ASSERT
    signup_page.verify_max_length(element=signup_page.full_name_input, max_length=100)
