import allure
import pytest

from tests import data


@allure.id("CAS-18")
@allure.title("🎉 Успешная регистрация Nova")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_3
def test_successful_registration_nova(signup_page_step_2):
    """
    Сценарий:
    1. Ввести 'QUASAR_5' в поле 'Access Code'.
    2. Ввести 'QUASAR_5' в поле 'Confirm Access Code'.
    3. Ввести 'COMETA' в поле 'Recovery Cipher'.
    4. Нажать на кнопку 'COMPLETE REGISTRATION'.
    5. Проверяем: наличие подзаголовка 'Welcome aboard, new Operator.'.
    6. Проверяем: текст телеметрии.
    7. Проверяем: цвет текста телеметрии синий.
    8. Проверяем: все поля сводки создания на форме 3.

    """

    # 🎬 ARRANGE
    signup_page_step_2.enter_access_code(code=data.ACCESS_CODE_NOVA)
    signup_page_step_2.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_NOVA)
    signup_page_step_2.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_NOVA)

    # ⚡ ACT
    signup_page_step_2.click_complete_registration()

    # ✅ ASSERT
    signup_page_step_2.verify_text(
        element=signup_page_step_2.page_subtitle,
        expected_text=data.SUBTITLE_WELCOME_OPERATOR,
    )
    signup_page_step_2.verify_telemetry_text(
        expected_text=data.TELEMETRY_REGISTRATION_COMPLETE
    )
    signup_page_step_2.verify_telemetry_color_not_cassandra(green=True)
    signup_page_step_2.verify_step_3_summary(
        expected_callsign=data.CALLSIGN_NOVA,
        expected_full_name=data.NAME_NOVA,
        expected_role=data.ROLE_DISPLAY_ENGINEER,
        expected_function=data.FUNCTION_ENGINEER,
        expected_level=data.ACCESS_LEVEL_ENGINEER,
        expected_id=data.OPERATOR_ID_NOVA,
    )


@allure.id("CAS-19")
@allure.title("💾 Проверка данных в 'sessionStorage' после 'Launch'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_3
def test_verify_session_storage_after_launch(nova_created):
    """
    Сценарий:
    1. Нажимаем на кнопку 'INITIATE LAUNCH SEQUENCE 🚀'.
    2. Проверяем: url меняется на 'dashboard.html'
    3. Проверяем: сессия записывается в 'sessionStorage' - 'ключ currentUser'.
    4. Очищаем данные Новы из 'localStorage' - 'registeredUsers'.
    5. Проверяем: что 'localStorage' пустой.
    """

    # 🎬 ARRANGE
    nova_created.click_launch_dashboard()

    # ✅ ASSERT
    nova_created.verify_current_url(expected_url_part=data.DASHBOARD_URL)
    nova_created.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_NOVA, check_session=True
    )

    # 🧹 TEARDOWN
    nova_created.delete_operator_from_storage(callsign=data.CALLSIGN_NOVA)

    # ✅ ASSERT
    nova_created.clear_user_data(
        callsign=data.CALLSIGN_NOVA, clear_registered_user=True
    )


@allure.id("CAS-20")
@allure.title("🗄️ Проверка данных в 'localStorage' после 'Launch'")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_3
def test_verify_local_storage_after_launch(nova_created):
    """
    Сценарий:
    1. Нажимаем на кнопку 'INITIATE LAUNCH SEQUENCE 🚀'.
    2. Проверяем: url меняется на 'dashboard.html'
    3. Проверяем: данные оператора сохраняются в 'localStorage' - ключ 'registeredUsers'.
    4. Очищаем данные Новы из 'localStorage' - 'registeredUsers'.
    5. Проверяем: что 'localStorage' пустой.
    """

    # 🎬 ARRANGE
    nova_created.click_launch_dashboard()

    # ✅ ASSERT
    nova_created.verify_current_url(expected_url_part=data.DASHBOARD_URL)
    nova_created.verify_user_data_in_storage(
        expected_callsign=data.CALLSIGN_NOVA, check_local=True
    )

    # 🧹 TEARDOWN
    nova_created.delete_operator_from_storage(callsign=data.CALLSIGN_NOVA)

    # ✅ ASSERT
    nova_created.clear_user_data(
        callsign=data.CALLSIGN_NOVA, clear_registered_user=True
    )


@allure.id("CAS-21")
@allure.title("🔭 Успешная навигация на страницу `Log In`")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_3
def test_successful_navigatio_to_the_log_in(signup_page):
    """
    Сценарий:
    1. Нажимаем на кнопку 'Log in'.
    2. Проверяем: url страницы 'login.html'.
    """

    # ⚡ ACT
    signup_page.click_log_in()
   
    # ✅ ASSERT
    signup_page.verify_current_url(expected_url_part=data.LOGIN_URL)



@allure.id("CAS-22")
@allure.title("🔑 Успешная навигация на страницу `Access Restoration`.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_3
def test_successful_navigatio_to_the_access_restoration(signup_page):
    """
    Сценарий:
    1. Нажимаем на кнопку 'Access Restoration'.
    2. Проверяем: url страницы 'access-restoration.html'.
    """

    # ⚡ ACT
    signup_page.click_restore()
   
    # ✅ ASSERT
    signup_page.verify_current_url(expected_url_part=data.ACCESS_RESTORATION_URL)


@allure.id("CAS-23")
@allure.title("🔒 Блокировка угловой навигации на Шаге 3.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "signup")
@pytest.mark.regress
@pytest.mark.signup
@pytest.mark.step_3
def test_сorner_navigation_locked_on_step_3(signup_page_step_2):
    """
    Сценарий:
    1. Пройти путь регистрации до Шага 3.
    2. Проверяем CSS: у контейнера угловых кнопок присутствует класс locked.
    3. Проверяем: кнопки полупрозрачные (opacity: 0.3).
    4. Пооверяем: кнопки некликабельны (pointer-events: none), клик по ним не вызывает перехода.
    """

    # 🎬 ARRANGE
    signup_page_step_2.enter_access_code(code=data.ACCESS_CODE_NOVA)
    signup_page_step_2.enter_confirm_access_code(confirm_code=data.ACCESS_CODE_NOVA)
    signup_page_step_2.enter_recovery_cipher(cipher=data.RECOVERY_CIPHER_NOVA)
    signup_page_step_2.click_complete_registration()
  
    # ✅ ASSERT
    signup_page_step_2.check_corner_nav_locked()

    # ⚡ ACT
    signup_page_step_2.check_button_not_clickable('btn-login')

    # ✅ ASSERT
    signup_page_step_2.verify_current_url(expected_url_part=data.SIGNUP_URL)

    # ⚡ ACT
    signup_page_step_2.check_button_not_clickable('btn-restore')
    
    # ✅ ASSERT
    signup_page_step_2.verify_current_url(expected_url_part=data.SIGNUP_URL)








