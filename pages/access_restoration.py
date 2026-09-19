import allure
from selene import be, browser, have
from selenium.common.exceptions import TimeoutException

from pages.gateway import GatewayPage
from tests import data


class AccessRestorationPage(GatewayPage):

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
    nav_login_btn = browser.element('[data-wm-id="btn-login"]')
    nav_signup_btn = browser.element('[data-wm-id="btn-signup"]')

    # Текст, сообщения, блоки
    page_subtitle = browser.element('[data-wm-id="restoration-page-subtitle"]')
    error_message = browser.element('[data-wm-id="restoration-error-message"]')
    success_message = browser.element('[data-wm-id="restoration-success-message"]')
    success_logo = browser.element('[data-wm-id="restoration-success-logo"]')
    summary_block = browser.element('[data-wm-id="restoration-summary"]')
    sum_callsign = browser.element('[data-wm-id="sum-callsign"]')
    sum_role = browser.element('[data-wm-id="sum-role"]')
    sum_function = browser.element('[data-wm-id="sum-function"]')
    sum_id = browser.element('[data-wm-id="sum-id"]')
    sum_new_code = browser.element('[data-wm-id="sum-new-code"]')

    # Локальные методы страницы (специфика RestorePage)
    @allure.step("Переключаем видимость New Access Code")
    def click_toggle_new_access_code(self):
        self.toggle_new_access_code_btn.click()
        return self
    
    @allure.step("Переключаем видимость Confirm Code")
    def click_toggle_confirm_code(self):
        self.toggle_confirm_access_code_btn.click()
        return self

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

    @allure.step("Ввод нового пароля доступа")
    def enter_new_access_code(self, new_code: str, clear_first: bool = False):
        """Вводит новый пароль в поле New Access Code. Если clear_first=True, сначала очищает поле.

        Args:
            access_code: Новый пароль доступа (например, 'AERO_99').
            clear_first: Если True, сначала очищает поле.
        """
        with allure.step(
            f"Вводим новый пароль доступа: '{new_code}' (очистка: {clear_first})"
        ):
            try:
                self.new_access_code_input.should(be.visible)

                if clear_first:
                    self.new_access_code_input.clear()

                self.new_access_code_input.type(new_code)

            except TimeoutException:
                raise AssertionError(
                    "❌ New Access Code field not found or not visible!\n"
                    f"   Access Code: {new_code}\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while entering new access code!\n"
                    f"   Access Code: {new_code}\n"
                    f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 3️⃣ 🖱️ ДЕЙСТВИЯ С КНОПКАМИ
    # ========================================================================

    @allure.step("Нажатие на кнопку восстановления доступа")
    def click_restore_access(self, wait_for_success: bool = True):
        """
        1. Ждёт появления кнопки RESTORE ACCESS
        2. Кликает на неё
        3. Ждёт смены статуса телеметрии (уход из SYSTEM READY)
        4. (Опционально) Ждёт появления блока сводки (summary_block) на экране успеха
    
        Args:
            wait_for_success: Если True (по умолчанию), ждёт появления экрана успеха.
                            Если False, просто кликает и возвращает управление 
                            (идеально для негативных тестов, где ждём ошибку).
        """
        with allure.step("Ждём появления кнопки RESTORE ACCESS"):
            self.restore_access_btn.should(be.visible)
            self.restore_access_btn.should(be.enabled)

        with allure.step("Кликаем на кнопку RESTORE ACCESS"):
            self.restore_access_btn.click()

        with allure.step("Ожидание смены статуса телеметрии (уход из SYSTEM READY)"):
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

        Args:
            is_enabled: Если True — проверяет, что кнопка активна.
                    Если False (по умолчанию) — проверяет, что кнопка неактивна.
        """
        state = "enabled" if is_enabled else "disabled"
        with allure.step(f"Ожидаемое состояние кнопки: {state}"):
            try:
                if is_enabled:
                    self.restore_access_btn.should(be.enabled)
                else:
                    self.restore_access_btn.should(be.disabled)
            except TimeoutException:
                raise AssertionError(
                    f"❌ Restore Access button is not {state}!\n"
                    f"   Timeout: button did not become {state} in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking button state!\n"
                    f"   Expected state: {state}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Проверяем тип поля после переключения видимости на странице Access Restoration")
    def verify_field_type_after_toggle_restoration(
        self,
        new_access_code: bool = False,
        confirm_access_code: bool = False,
        expected_type: str = "text",
    ):
        """
        Проверяет атрибут type у полей New Access Code и/или Confirm Access Code
        после переключения видимости на странице Access Restoration.

        Args:
            new_access_code: Если True, проверяет тип поля New Access Code.
            confirm_access_code: Если True, проверяет тип поля Confirm Access Code.
            expected_type: Ожидаемый тип ('password' или 'text'). По умолчанию 'text'.
        """
        try:
            if new_access_code:
                self.new_access_code_input.should(have.attribute("type", expected_type))
            if confirm_access_code:
                self.confirm_access_code_input.should(have.attribute("type", expected_type))
        except TimeoutException:
            raise AssertionError(
                "❌ Field type verification failed on Access Restoration page!\n"
                f"   Expected type: '{expected_type}'\n"
                f"   New Access Code check: {new_access_code}\n"
                f"   Confirm Access Code check: {confirm_access_code}\n"
                "   Condition: Specified fields must have the expected type after toggle"
            )
        return self

    # endregion
    # ========================================================================
