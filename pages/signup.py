import allure
from selene import be, browser, have
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.core import CorePage
from tests import data


class SignupPage(CorePage):

    # URL
    PATH = data.SIGNUP_URL

    # Поля ввода
    full_name_input = browser.element('[data-wm-id="signup-full-name-input"]')
    callsign_input = browser.element('[data-wm-id="signup-callsign-input"]')
    role_select = browser.element('[data-wm-id="signup-role-select"]')
    function_input = browser.element('[data-wm-id="signup-function-input"]')
    access_code_input = browser.element('[data-wm-id="signup-access-code-input"]')
    confirm_access_code_input = browser.element('[data-wm-id="signup-confirm-code-input"]')
    recovery_cipher_input = browser.element('[data-wm-id="signup-recovery-cipher-input"]')

    # Кнопки
    proceed_btn = browser.element('[data-wm-id="signup-proceed-btn"]')
    back_to_operator_data_btn = browser.element('[data-wm-id="signup-back-btn"]')
    complete_btn = browser.element('[data-wm-id="signup-complete-btn"]')
    toggle_access_code_btn = browser.element('[data-wm-id="signup-toggle-access-code"]')
    toggle_confirm_code_btn = browser.element('[data-wm-id="signup-toggle-confirm-code"]')

    # Информационные панели
    error_message = browser.element('[data-wm-id="signup-error-message"]')
    error_security_message = browser.element('[data-wm-id="signup-security-error"]')
    page_subtitle = browser.element('[data-wm-id="signup-page-subtitle"]')
    activation_logo = browser.element('[data-wm-id="signup-activation-logo"]')
    sum_callsign = browser.element('[data-wm-id="sum-callsign"]')
    sum_name = browser.element('[data-wm-id="sum-name"]')
    sum_role = browser.element('[data-wm-id="sum-role"]')
    sum_function = browser.element('[data-wm-id="sum-function"]')
    sum_level = browser.element('[data-wm-id="sum-level"]')
    sum_id = browser.element('[data-wm-id="sum-id"]')

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌐 Открытие страницы регистрации")
    def open(self):
        """Открывает страницу регистрации и проверяет её загрузку.

        Returns:
            self: Экземпляр SignupPage для chaining-а методов.

        Raises:
            AssertionError: Если страница не загрузилась в течение таймаута.
        """
        with allure.step(f"Открываем страницу: {self.PATH}"):
            browser.open(self.PATH)
            
        with allure.step("Проверяем URL и отрисовку элементов"):
            try:
                self.wait_for_url(expected_url_part=data.SIGNUP_URL)
                
                self.full_name_input.should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Signup page did not load!\n"
                    f"   Expected URL part: {data.SIGNUP_URL}\n"
                    f"   Actual URL: {browser.driver.current_url}\n"
                    "   Timeout: page did not load or URL did not match"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening Signup page!\n"
                    f"   Path: {self.PATH}\n"
                    f"   Error: {e}"
                ) from e
                
        return self

    # endregion

    # ========================================================================
    # region 2️⃣ ⌨️ ЗАПОЛНЕНИЕ ПОЛЕЙ
    # ========================================================================

    @allure.step("Ввод имени оператора")
    def enter_full_name(self, name: str, clear: bool = False):
        """Вводит имя оператора. По умолчанию дописывает, если clear=True — очищает."""
        if clear:
            with allure.step(f"Очистка и ввод в поле 'Full Name': '{name}'"):
                self.full_name_input.set_value(name)
        else:
            with allure.step(f"Дозапись в поле 'Full Name': '{name}'"):
                self.full_name_input.type(name)
        return self

    @allure.step("Ввод шифра восстановления")
    def enter_recovery_cipher(self, cipher: str, clear: bool = False):
        """Вводит шифр восстановления доступа. По умолчанию дописывает, если clear=True — очищает."""
        if clear:
            with allure.step(f"Очистка и ввод в поле 'Recovery Cipher': '{cipher}'"):
                self.recovery_cipher_input.set_value(cipher)
        else:
            with allure.step(f"Дозапись в поле 'Recovery Cipher': '{cipher}'"):
                self.recovery_cipher_input.type(cipher)
        return self

    @allure.step("Ввод кода доступа")
    def enter_access_code(self, code: str, clear: bool = False):
        """Вводит код доступа. По умолчанию дописывает, если clear=True — очищает."""
        if clear:
            with allure.step(f"Очистка и ввод в поле 'Access code': '{code}'"):
                self.access_code_input.set_value(code)
        else:
            with allure.step(f"Дозапись в поле 'Access code': '{code}'"):
                self.access_code_input.type(code)
        return self

    @allure.step("Подтверждение кода доступа")
    def enter_confirm_access_code(self, code: str, clear: bool = False):
        """Подтверждает код доступа. По умолчанию дописывает, если clear=True — очищает."""
        if clear:
            with allure.step(f"Очистка и ввод в поле 'Confirm access code': '{code}'"):
                self.confirm_access_code_input.set_value(code)
        else:
            with allure.step(f"Дозапись в поле 'Confirm access code': '{code}'"):
                self.confirm_access_code_input.type(code)
        return self

    @allure.step("Выбираем роль из выпадающего списка")
    def select_role(self, role_value: str):
        """
        Выбирает роль из выпадающего списка по атрибуту value.
        Использует нативный Selenium Select для обхода ограничений Selene.

        Args:
            role_value: Значение атрибута value (например, 'ENGINEER').
        """
        try:

            webelement = browser.driver.find_element(
                By.CSS_SELECTOR, '[data-wm-id="signup-role-select"]'
            )
            Select(webelement).select_by_value(role_value)
        except TimeoutException:
            raise AssertionError(
                "❌ Failed to select Role!\n"
                f"   Expected role value: '{role_value}'\n"
                "   Timeout: role_select dropdown did not appear"
            )
        except NoSuchElementException:
            raise AssertionError(
                f"❌ Role value '{role_value}' not found in the dropdown!\n"
                f"   Element: [data-wm-id='signup-role-select']"
            )
        return self

    # endregion

    # ========================================================================
    # region 3️⃣ 🖱️ Методы для кнопок 
    # ========================================================================

    @allure.step("Нажатие на кнопку Complete Registration и ожидание ответа системы")
    def click_complete_registration(self):
        """
        Кликает по кнопке COMPLETE REGISTRATION и ждет, пока JS обработает запрос (2 секунды).
        Ожидает смены статуса телеметрии (уход из состояния SYSTEM READY).
        """
        with allure.step("Кликаем на кнопку COMPLETE REGISTRATION"):
            self.complete_btn.click()

        with allure.step("Ожидание смены статуса телеметрии (уход из SYSTEM READY)"):
            try:
                self.system_telemetry.should(have.no.text("SYSTEM READY"))
            except Exception as e:
                raise AssertionError(
                    "❌ System did not respond after registration attempt!\n"
                    "   Telemetry is still showing 'SYSTEM READY'. "
                    "Check if JS timeout or button click failed."
                ) from e

        return self

    @allure.step("Нажатие на кнопку Proceed")
    def click_proceed(self):
        """Нажатие на кнопку Proceed для перехода к следующему шагу."""
        with allure.step("Кликаем по кнопке Proceed"):
            try:
                self.proceed_btn.should(be.visible).should(be.enabled)
                self.proceed_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Proceed button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f" Unexpected error while clicking Proceed!\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие на кнопку Back to operator data")
    def click_back_operator_data(self):
        """Нажатие на кнопку Back to operator data для возврата на Шаг 1."""
        with allure.step("Кликаем по кнопке Back to operator data"):
            try:
                self.back_to_operator_data_btn.should(be.visible).should(be.enabled)
                self.back_to_operator_data_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Back to operator data button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Back to operator data!\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Переключаем видимость Access Code")
    def click_toggle_access_code(self):
        """Переключает видимость поля кода доступа."""
        with allure.step("Кликаем по кнопке Toggle Access Code"):
            try:
                self.toggle_access_code_btn.should(be.visible).should(be.enabled)
                self.toggle_access_code_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Toggle Access Code button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Toggle Access Code!\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Переключаем видимость Confirm Code")
    def click_toggle_confirm_code(self):
        """Переключает видимость поля подтверждения кода."""
        with allure.step("Кликаем по кнопке Toggle Confirm Code"):
            try:
                self.toggle_confirm_code_btn.should(be.visible).should(be.enabled)
                self.toggle_confirm_code_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Toggle Confirm Code button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f" Unexpected error while clicking Toggle Confirm Code!\n"
                    f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 4️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================

    @allure.step("Проверяем поля формы Шага 1")
    def verify_step_1_fields(
        self,
        expected_full_name: str,
        expected_callsign: str | None = None,
        expected_role: str | None = None,
        expected_function: str | None = None,
    ):
        """
        Проверяет указанные поля Шага 1 на ожидаемые значения.
        Имя — обязательное, остальные поля — опциональные.

        Args:
            expected_full_name: Ожидаемое значение поля Full Name (обязательно).
            expected_callsign: Ожидаемое значение поля Callsign (опционально).
            expected_role: Ожидаемое значение атрибута value поля Role (опционально).
            expected_function: Ожидаемое значение поля Function (опционально).
        """
        try:
            self.full_name_input.should(have.value(expected_full_name))

            if expected_callsign is not None:
                self.callsign_input.should(have.value(expected_callsign))
            if expected_role is not None:
                self.role_select.should(have.value(expected_role))
            if expected_function is not None:
                self.function_input.should(have.value(expected_function))
        except TimeoutException:
            raise AssertionError(
                "❌ Step 1 fields verification failed!\n"
                f"   Expected Full Name: '{expected_full_name}'\n"
                f"   Expected Callsign: '{expected_callsign}'\n"
                f"   Expected Role: '{expected_role}'\n"
                f"   Expected Function: '{expected_function}'\n"
                "   Condition: Specified Step 1 fields must retain their values"
            )
        return self

    @allure.step("Проверяем, что форма Шага 2 пуста, а кнопка Complete заблокирована")
    def verify_step_2_empty_state(self):
        """
        Проверяет, что все поля Шага 2 пустые, а кнопка Complete Registration заблокирована.
        """
        try:
            self.access_code_input.should(have.value(""))
            self.confirm_access_code_input.should(have.value(""))
            self.recovery_cipher_input.should(have.value(""))
            self.complete_btn.should(be.disabled)
        except TimeoutException:
            raise AssertionError(
                "❌ Step 2 empty state verification failed!\n"
                "   Expected: Access Code = '', Confirm Code = '', Recovery Cipher = '', Complete Button = DISABLED\n"
                "   Condition: All Step 2 fields must be empty and Complete button must be disabled"
            )
        return self

    @allure.step("Проверяем поля сводки на Шаге 3")
    def verify_step_3_summary(
        self,
        expected_callsign: str | None = None,
        expected_full_name: str | None = None,
        expected_role: str | None = None,
        expected_function: str | None = None,
        expected_level: str | None = None,
        expected_id: str | None = None,
    ):
        """
        Проверяет указанные поля сводки Шага 3 на ожидаемые значения.
        Все параметры опциональны — можно проверять точечно.

        Args:
            expected_callsign: Ожидаемый позывной (например, 'NOVA').
            expected_full_name: Ожидаемое полное имя (например, 'Nova').
            expected_role: Ожидаемая роль с иконкой (например, '⚙️ Engineer').
            expected_function: Ожидаемая функция (например, 'Systems Engineering').
            expected_level: Ожидаемый уровень доступа (например, '3').
            expected_id: Ожидаемый ID оператора (например, '512-3A').
        """
        try:
            if expected_callsign is not None:
                self.sum_callsign.should(have.exact_text(expected_callsign))
            if expected_full_name is not None:
                self.sum_name.should(have.exact_text(expected_full_name))
            if expected_role is not None:
                self.sum_role.should(have.exact_text(expected_role))
            if expected_function is not None:
                self.sum_function.should(have.exact_text(expected_function))
            if expected_level is not None:
                self.sum_level.should(have.exact_text(expected_level))
            if expected_id is not None:
                self.sum_id.should(have.exact_text(expected_id))
        except TimeoutException:
            raise AssertionError(
                "❌ Step 3 summary verification failed!\n"
                f"   Expected Callsign: '{expected_callsign}'\n"
                f"   Expected Full Name: '{expected_full_name}'\n"
                f"   Expected Role: '{expected_role}'\n"
                f"   Expected Function: '{expected_function}'\n"
                f"   Expected Level: '{expected_level}'\n"
                f"   Expected ID: '{expected_id}'\n"
                "   Condition: Specified summary fields must match expected values"
            )
        return self

    @allure.step("Проверяем тип поля после переключения видимости")
    def verify_field_type_after_toggle(
        self,
        access_code: bool = False,
        confirm_code: bool = False,
        expected_type: str = "text",
    ):
        """
        Проверяет атрибут type у полей после переключения видимости.
        Убеждается, что точки исчезли и введенные символы видны.

        Args:
            access_code: Если True, проверяет тип поля Access Code.
            confirm_code: Если True, проверяет тип поля Confirm Access Code.
            expected_type: Ожидаемый тип ('password' или 'text'). По умолчанию 'text'.
        """
        try:
            if access_code:
                self.access_code_input.should(have.attribute("type", expected_type))
            if confirm_code:
                self.confirm_access_code_input.should(
                    have.attribute("type", expected_type)
                )
        except TimeoutException:
            raise AssertionError(
                "❌ Field type verification failed!\n"
                f"   Expected type: '{expected_type}'\n"
                f"   Access Code check: {access_code}\n"
                f"   Confirm Code check: {confirm_code}\n"
                "   Condition: Specified fields must have the expected type after toggle"
            )
        return self

    # endregion
    # ========================================================================
