import allure
from selene import be, browser, have
from selenium.common.exceptions import TimeoutException

from pages.hub import HubPage
from tests import data


class AccessRestorationPage(HubPage):

    # URL
    PATH = data.ACCESS_RESTORATION_URL

    # Поля ввода
    callsign_input = browser.element('[data-wm-id="restoration-callsign-input"]')
    recovery_cipher_input = browser.element(
        '[data-wm-id="restoration-recovery-cipher-input"]'
    )
    new_access_code_input = browser.element(
        '[data-wm-id="restoration-new-access-code-input"]'
    )
    confirm_access_code_input = browser.element(
        '[data-wm-id="restoration-confirm-access-code-input"]'
    )

    # Кнопки
    toggle_new_access_code_btn = browser.element(
        '[data-wm-id="restoration-toggle-new-access-code"]'
    )
    toggle_confirm_access_code_btn = browser.element(
        '[data-wm-id="restoration-toggle-confirm-access-code"]'
    )
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
    # region 2️⃣ ⌨️ ПОЛЯ ВВОДА
    # ========================================================================

    @allure.step("Ввод позывного на странице восстановления")
    def enter_callsign(self, callsign: str, clear_first: bool = False):
        """Вводит позывной в поле Callsign на странице восстановления.

        Args:
            callsign: Позывной (например, 'KNOPA').
            clear_first: Если True, сначала очищает поле.
        """
        with allure.step(f"Вводим позывной: '{callsign}' (очистка: {clear_first})"):
            try:
                self.callsign_input.should(be.visible)

                if clear_first:
                    self.callsign_input.clear()

                self.callsign_input.type(callsign)

            except TimeoutException:
                raise AssertionError(
                    "❌ Callsign field not found or not visible on Restoration page!\n"
                    f"   Callsign: {callsign}\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while entering callsign on Restoration page!\n"
                    f"   Callsign: {callsign}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Ввод шифра восстановления")
    def enter_recovery_cipher(self, cipher: str, clear_first: bool = False):
        """Вводит шифр восстановления в поле Recovery Cipher. Если clear_first=True, сначала очищает поле.

        Args:
            cipher: Шифр восстановления (например, 'AERO').
            clear_first: Если True, сначала очищает поле.
        """
        with allure.step(
            f"Вводим шифр восстановления: '{cipher}' (очистка: {clear_first})"
        ):
            try:
                self.recovery_cipher_input.should(be.visible)

                if clear_first:
                    self.recovery_cipher_input.clear()

                self.recovery_cipher_input.type(cipher)

            except TimeoutException:
                raise AssertionError(
                    "❌ Recovery Cipher field not found or not visible!\n"
                    f"   Cipher: {cipher}\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while entering recovery cipher!\n"
                    f"   Cipher: {cipher}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Ввод нового пароля доступа")
    def enter_new_access_code(self, access_code: str, clear_first: bool = False):
        """Вводит новый пароль в поле New Access Code. Если clear_first=True, сначала очищает поле.

        Args:
            access_code: Новый пароль доступа (например, 'AERO_99').
            clear_first: Если True, сначала очищает поле.
        """
        with allure.step(
            f"Вводим новый пароль доступа: '{access_code}' (очистка: {clear_first})"
        ):
            try:
                self.new_access_code_input.should(be.visible)

                if clear_first:
                    self.new_access_code_input.clear()

                self.new_access_code_input.type(access_code)

            except TimeoutException:
                raise AssertionError(
                    "❌ New Access Code field not found or not visible!\n"
                    f"   Access Code: {access_code}\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while entering new access code!\n"
                    f"   Access Code: {access_code}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Ввод подтверждения нового пароля")
    def enter_confirm_access_code(self, access_code: str, clear_first: bool = False):
        """Вводит подтверждение нового пароля в поле Confirm Access Code. Если clear_first=True, сначала очищает поле.

        Args:
            access_code: Подтверждение нового пароля доступа (например, 'AERO_99').
            clear_first: Если True, сначала очищает поле.
        """
        with allure.step(
            f"Вводим подтверждение нового пароля: '{access_code}' (очистка: {clear_first})"
        ):
            try:
                self.confirm_access_code_input.should(be.visible)

                if clear_first:
                    self.confirm_access_code_input.clear()

                self.confirm_access_code_input.type(access_code)

            except TimeoutException:
                raise AssertionError(
                    "❌ Confirm Access Code field not found or not visible!\n"
                    f"   Access Code: {access_code}\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while entering confirm access code!\n"
                    f"   Access Code: {access_code}\n"
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

    @allure.step("Клик по кнопке переключения видимости пароля (Глаз)")
    def click_toggle_password(self):
        """Нажимает на иконку глаза, чтобы показать/скрыть пароль."""
        try:
            self.toggle_new_access_code_btn.click()
        except Exception as e:
            raise AssertionError(
                f"❌ Failed to click toggle password button!\n" f"   Error: {e}"
            ) from e
        return self

    @allure.step("Клик по кнопке переключения видимости пароля (Глаз)")
    def click_toggle_confirm_password(self):
        """Нажимает на иконку глаза, чтобы показать/скрыть пароль."""
        try:
            self.toggle_confirm_access_code_btn.click()
        except Exception as e:
            raise AssertionError(
                f"❌ Failed to click toggle password button!\n" f"   Error: {e}"
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

    @allure.step("Проверка типа полей New Access Code и Confirm Access Code")
    def verify_restoration_access_code_types(self, expected_type: str):
        """Проверяет атрибут type полей ввода нового пароля и его подтверждения.

        Args:
            expected_type: 'password' (скрыт) или 'text' (виден)
        """
        try:
            new_code_type = self.new_access_code_input().get_attribute("type")
            confirm_code_type = self.confirm_access_code_input().get_attribute("type")

            if new_code_type != expected_type:
                raise AssertionError(
                    f" New Access Code type mismatch!\n"
                    f"   Expected: {expected_type}\n"
                    f"   Actual: {new_code_type}"
                )

            if confirm_code_type != expected_type:
                raise AssertionError(
                    f"❌ Confirm Access Code type mismatch!\n"
                    f"   Expected: {expected_type}\n"
                    f"   Actual: {confirm_code_type}"
                )
                
        except AssertionError:
            raise
        except Exception as e:
            raise AssertionError(
                f"❌ Unexpected error while checking access code types!\n"
                f"   Expected: {expected_type}\n"
                f"   Error: {e}"
            ) from e
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

    @allure.step("Переключаем видимость полей New Access Code и Confirm Access Code")
    def click_toggle_new_and_confirm_access_code(
        self,
        new_access_code: bool = False,
        confirm_access_code: bool = False,
    ):
        """
        Переключает видимость полей New Access Code и/или Confirm Access Code
        на странице Access Restoration.

        Args:
            new_access_code: Если True, кликает по кнопке переключения видимости New Access Code.
            confirm_access_code: Если True, кликает по кнопке переключения видимости Confirm Access Code.
        """
        try:
            if new_access_code:
                self.toggle_new_access_code_btn.click()
            if confirm_access_code:
                self.toggle_confirm_access_code_btn.click()
        except TimeoutException:
            raise AssertionError(
                "❌ Failed to toggle password visibility on Access Restoration page!\n"
                f"   New Access Code toggle: {new_access_code}\n"
                f"   Confirm Access Code toggle: {confirm_access_code}\n"
                "   Timeout: toggle button was not clickable or not visible"
            )
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
