import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("📡 Состояние страницы при загрузке")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("component", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.ui_navigation
def test_initial_page_state(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Оценить начальное состояние страницы 'Login Page' при загрузке.
    3. Проверить: наличие подзаголовка 'Access to Colonization Assessment System'.
    4. Проверить: поле 'Callsign' пустое и редактируемое.
    5. Проверить: поле 'Access Code' пустое и редактируемое.
    6. Проверить: кнопка 'Establish Connection' неактивна (disabled).
    7. Проверить: текст '> SYSTEM READY. AWAITING CONNECTION', синего цвета.
    """

    # ✅ ASSERT
    login_page.verify_text(
        element=login_page.page_subtitle,
        expected_text=data.COLONIZATION_ACCESS,
    )
    login_page.verify_empty_field_state(
        element=login_page.callsign_input, is_readonly=False
    )
    login_page.verify_empty_field_state(
        element=login_page.access_code_input, is_readonly=False
    )
    login_page.verify_button_state(
        element=login_page.establish_connect_btn, is_disabled=True
    )
    login_page.verify_telemetry_text(
        expected_text=data.BLUE_TELEMETRY_AWAITING_CONNECTION
    )
    login_page.verify_telemetry_color_not_cassandra(blue=True)


@allure.id("CAS-02")
@allure.title("⚡ Реактивное состояние кнопки 'Establish Connection'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.ui_navigation
def test_reactive_button_state(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести <4 символов в поле 'Callsign'.
    3. Ввести <4 символов в поле 'Access Code'.
    4. Проверить: кнопка 'Establish Connection' остаётся неактивной `disabled`.
    5. Очистить все поля.
    6. Ввести 4 символа в поле 'Callsign'.
    7. Ввести 4 символа в поле 'Access Code'.
    8. Проверить: кнопка 'Establish Connection' активна.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_TOO_SHORT_3_CHARS)
    login_page.enter_access_code(access_code=data.ACCESS_CODE_TOO_SHORT_3_CHARS)

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=False)

    # ⚡ ACT
    login_page.enter_callsign(
        callsign=data.CALLSIGN_MIN_VALID_4_CHARS, clear_first=True
    )
    login_page.enter_access_code(
        access_code=data.ACCESS_CODE_MIN_VALID_4_CHARS, clear_first=True
    )

    # ✅ ASSERT
    login_page.should_be_establish_connect_btn(is_enabled=True)


@allure.id("CAS-03")
@allure.title("👁️ Переключение видимости ключа доступа")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.ui_navigation
def test_toggle_access_code_visibility(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Ввести валидный ключ доступа 'COMET_42' в поле 'Access Code'.
    3. Нажать на кнопку 'Toggle Password' (иконка глаза).
    4. Проверить: при первом клике символы в поле становятся видимыми, иконка глаза меняется.
    5. Нажать на кнопку 'Toggle Password' (иконка глаза).
    6. Проверить: при повторном клике символы скрываются звездочками, иконка глаза возвращается к исходному состоянию.
    """

    # 🎬 ARRANGE
    login_page.enter_callsign(callsign=data.CALLSIGN_AURORA)

    # ⚡ ACT
    login_page.click_toggle_password()

    # ✅ ASSERT
    login_page.verify_access_code_type(expected_type="text")

    # ⚡ ACT
    login_page.click_toggle_password()

    # ✅ ASSERT
    login_page.verify_access_code_type(expected_type="password")


@allure.id("CAS-04")
@allure.title("📡 Успешная навигация на страницу `Sign Up`")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.ui_navigation
def test_successful_navigation_to_signup(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Нажать на угловую кнопку 'Sign Up'.
    3. Проверить: происходит навигация, 'URL' страницы становится 'signup.html'.
    """

    # ⚡ ACT
    login_page.click_sign_up()

    # ✅ ASSERT
    login_page.wait_for_url(expected_url_part=data.SIGNUP_URL)


@allure.id("CAS-05")
@allure.title("🔑 Успешная навигация на страницу `Access Restoration`")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "login")
@pytest.mark.regress
@pytest.mark.login
@pytest.mark.ui_navigation
def test_successful_navigation_to_the_access_restoration(login_page):
    """
    Сценарий:
    1. Перейти на страницу 'Login Page'.
    2. Нажать на угловую кнопку 'Restore'.
    3. Проверить: происходит навигация, 'URL' страницы становится 'access-restoration.html'.
    """

    # ⚡ ACT
    login_page.click_restore()

    # ✅ ASSERT
    login_page.wait_for_url(expected_url_part=data.ACCESS_RESTORATION_URL)
