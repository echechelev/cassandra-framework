import allure
from selene import be, browser, have
from selenium.common.exceptions import TimeoutException

from pages.core import CorePage
from tests import data


class AccessRestorationPage(CorePage):

    # URL
    PATH = data.ACCESS_RESTORATION_URL
    
    # Поля ввода
    callsign_input = browser.element('[data-wm-id="restoration-callsign-input"]')
    recovery_cipher_input = browser.element('[data-wm-id="restoration-recovery-cipher-input"]')
    new_access_code_input = browser.element('[data-wm-id="restoration-new-access-code-input"]')
    confirm_access_code_input = browser.element('[data-wm-id="restoration-confirm-access-code-input"]')

    # Кнопки
    toggle_new_access_code_btn = browser.element('[data-wm-id="restoration-toggle-new-access-code"]')
    toggle_confirm_access_code_btn = browser.element('[data-wm-id="restoration-toggle-confirm-access-code"]')
    restore_access_btn = browser.element('[data-wm-id="restoration-restore-btn"]')
    
    # Информационные панели
    page_subtitle = browser.element('[data-wm-id="restoration-page-subtitle"]')
    error_message = browser.element('[data-wm-id="restoration-error-message"]')
    success_message = browser.element('[data-wm-id="restoration-success-message"]')
    summary_block = browser.element('[data-wm-id="restoration-summary"]')
    sum_callsign = browser.element('[data-wm-id="sum-callsign"]')
    sum_role = browser.element('[data-wm-id="sum-role"]')
    sum_function = browser.element('[data-wm-id="sum-function"]')
    sum_id = browser.element('[data-wm-id="sum-id"]')
    sum_new_code = browser.element('[data-wm-id="sum-new-code"]')

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌐 Открытие страницы восстановления")
    def open(self):
        """Открывает страницу восстановления и проверяет её загрузку.

        Returns:
            self: Экземпляр AccessRestorationPage для chaining-а методов.

        Raises:
            AssertionError: Если страница не загрузилась в течение таймаута.
        """
        with allure.step(f"Открываем страницу: {self.PATH}"):
            browser.open(self.PATH)

        with allure.step("Проверяем URL и отрисовку элементов"):
            try:

                self.wait_for_url(expected_url_part=data.ACCESS_RESTORATION_URL)    

                self.callsign_input.should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Access-Restoration-Page did not load!\n"
                    f"   Expected URL: {self.PATH}\n"
                    f"   Actual URL: {browser.driver.current_url}\n"
                    "   Timeout: callsign_input did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening Access_Restoration Page!\n"
                    f"   Path: {self.PATH}\n"
                    f"   Error: {e}"
                ) from e
        return self

    # ========================================================================
    # region 2️⃣ ⌨️ ЗАПОЛНЕНИЕ ПОЛЕЙ
    # ========================================================================

    @allure.step("Ввод позывного")
    def enter_callsign(self, callsign: str, clear: bool = False):
        """Вводит позывной. По умолчанию просто дописывает, если clear=True — очищает поле."""
        if clear:
            with allure.step(f"Очистка и ввод в поле 'Callsign': '{callsign}'"):
                self.callsign_input.set_value(callsign)
        else:
            with allure.step(f"Дозапись в поле 'Callsign': '{callsign}'"):
                self.callsign_input.type(callsign)
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

    @allure.step("Ввод нового кода доступа")
    def enter_new_access_code(self, new_code: str, clear: bool = False):
        """Вводит новый код доступа. По умолчанию дописывает, если clear=True — очищает."""
        if clear:
            with allure.step(f"Очистка и ввод в поле 'New access code': '{new_code}'"):
                self.new_access_code_input.set_value(new_code)
        else:
            with allure.step(f"Дозапись в поле 'New access code': '{new_code}'"):
                self.new_access_code_input.type(new_code)
        return self

    @allure.step("Подтверждение нового кода доступа")
    def enter_confirm_access_code(self, code: str, clear: bool = False):
        """Подтверждает новый код доступа. По умолчанию дописывает, если clear=True — очищает."""
        if clear:
            with allure.step(f"Очистка и ввод в поле 'Confirm access code': '{code}'"):
                self.confirm_access_code_input.set_value(code)
        else:
            with allure.step(f"Дозапись в поле 'Confirm access code': '{code}'"):
                self.confirm_access_code_input.type(code)
        return self

    # endregion

    # ========================================================================
    # region 3️⃣ 🖱️ Методы для кнопок 
    # ========================================================================

    @allure.step("Нажатие на кнопку восстановления доступа")
    def click_restore_access(self, wait_for_success: bool = True):
        """
        1. Кликает на кнопку RESTORE ACCESS
        2. Ждёт смены статуса телеметрии (уход из SYSTEM READY)
        3. (Опционально) Ждёт появления блока сводки (summary_block) на экране успеха
        
        Args:
            wait_for_success: Если True (по умолчанию), ждёт появления экрана успеха.
                            Если False, просто кликает (для негативных тестов).
        """
        with allure.step("Кликаем по кнопке Restore Access"):
            try:
                self.restore_access_btn.should(be.visible).should(be.enabled)
                self.restore_access_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Restore Access button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Restore Access!\n"
                    f"   Error: {e}"
                ) from e

        with allure.step("Ожидание смены статуса телеметрии"):
            try:
                self.system_telemetry.should(have.no.text("SYSTEM READY"))
            except Exception as e:
                raise AssertionError(
                    "❌ System did not respond after restoration attempt!\n"
                    "   Telemetry is still showing 'SYSTEM READY'. "
                    "Check if JS timeout or button click failed."
                ) from e

        if wait_for_success:
            with allure.step("Ждём появления блока сводки (экран успеха)"):
                self.summary_block.should(be.visible)

        return self

    @allure.step("Нажатие на кнопку Toggle New Access Code")
    def click_toggle_new_access_code(self):
        """Переключает видимость поля нового кода доступа."""
        with allure.step("Кликаем по кнопке Toggle New Access Code"):
            try:
                self.toggle_new_access_code_btn.should(be.visible).should(be.enabled)
                self.toggle_new_access_code_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Toggle New Access Code button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f" Unexpected error while clicking Toggle New Access Code!\n"
                    f"   Error: {e}"
                ) from e
        return self
    
    @allure.step("Нажатие на кнопку Toggle Confirm Access Code")
    def click_toggle_confirm_access_code(self):
        """Переключает видимость поля подтверждения кода доступа."""
        with allure.step("Кликаем по кнопке Toggle Confirm Access Code"):
            try:
                self.toggle_confirm_access_code_btn.should(be.visible).should(be.enabled)
                self.toggle_confirm_access_code_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Toggle Confirm Access Code button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f" Unexpected error while clicking Toggle Confirm Access Code!\n"
                    f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 4️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================

    @allure.step("Проверяем поля сводки на экране успешного восстановления")
    def verify_restoration_summary(
        self,
        expected_callsign: str | None = None,
        expected_role: str | None = None,
        expected_function: str | None = None,
        expected_id: str | None = None,
        expected_new_code: str | None = None,
    ):
        """
        Проверяет указанные поля сводки на экране успешного восстановления.
        Все параметры опциональны — можно проверять точечно.

        Args:
            expected_callsign: Ожидаемый позывной (например, 'KNOPA').
            expected_role: Ожидаемая роль с иконкой (например, '✈️ Pilot').
            expected_function: Ожидаемая функция (например, 'Flight Operations').
            expected_id: Ожидаемый ID оператора (например, '769-1A').
            expected_new_code: Ожидаемый новый ключ доступа (например, 'AERO_99').
        """
        try:
            if expected_callsign is not None:
                self.sum_callsign.should(have.exact_text(expected_callsign))
            if expected_role is not None:
                self.sum_role.should(have.exact_text(expected_role))
            if expected_function is not None:
                self.sum_function.should(have.exact_text(expected_function))
            if expected_id is not None:
                self.sum_id.should(have.exact_text(expected_id))
            if expected_new_code is not None:
                self.sum_new_code.should(have.exact_text(expected_new_code))
                
        except TimeoutException:
            raise AssertionError(
                "❌ Restoration summary verification failed!\n"
                f"   Expected Callsign: '{expected_callsign}'\n"
                f"   Expected Role: '{expected_role}'\n"
                f"   Expected Function: '{expected_function}'\n"
                f"   Expected ID: '{expected_id}'\n"
                f"   Expected New Code: '{expected_new_code}'\n"
                "   Condition: Specified summary fields must match expected values"
            )
        return self

    @allure.step("Проверка состояния кнопки Restore Access")
    def should_be_restore_access_btn(self, is_enabled: bool = False):
        """
        Проверяет состояние кнопки Restore Access.
        """
        self.verify_button_state(self.restore_access_btn, is_enabled=is_enabled)
        return self

    # endregion
