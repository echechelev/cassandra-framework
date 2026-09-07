import json

import allure
from selene import be, browser, have
from selenium.common.exceptions import TimeoutException

from pages.hub import HubPage


class LoginPage(HubPage):

    # URL
    PATH = "/login.html"

    # Поля ввода
    callsign_input = browser.element('[data-wm-id="login-callsign-input"]')
    access_code_input = browser.element('[data-wm-id="login-access-code-input"]')

    # Кнопки
    establish_connect_btn = browser.element('[data-wm-id="establish-connect-btn"]')
    toggle_password_btn = browser.element('[data-wm-id="toggle-password-btn"]')

    # Тексты и ссылки
    restore_clearance_link = browser.element('[data-wm-id="restore-clearance-link"]')
    lost_access_text = browser.element('[data-wm-id="lost-access-text"]')
    auth_error_message = browser.element('[data-wm-id="auth-error-message"]')

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌐 Открытие страницы авторизации")
    def open(self):
        """Открывает страницу авторизации и проверяет её загрузку.

        Returns:
            self: Экземпляр LoginPage для chaining-а методов.

        Raises:
            AssertionError: Если страница не загрузилась в течение таймаута.
        """
        with allure.step(f"Открываем страницу: {self.PATH}"):
            try:
                browser.open(self.PATH)
                self.callsign_input.should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Login page did not load!\n"
                    f"   Expected URL: {self.PATH}\n"
                    f"   Actual URL: {browser.driver.current_url}\n"
                    "   Timeout: callsign_input did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening login page!\n"
                    f"   Path: {self.PATH}\n"
                    f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 2️⃣ ⌨️ ПОЛЯ ВВОДА
    # ========================================================================

    @allure.step("Ввод позывного")
    def enter_callsign(self, callsign: str, clear_first: bool = False):
        """Вводит позывной в поле Callsign. Если clear_first=True, сначала очищает поле.

        Args:
            callsign: Позывной.
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
                    "❌ Callsign field not found or not visible!\n"
                    f"   Callsign: {callsign}\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while entering callsign!\n"
                    f"   Callsign: {callsign}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Ввод ключа доступа")
    def enter_access_code(self, access_code: str, clear_first: bool = False):
        """Вводит ключ доступа в поле Access Code. Если clear_first=True, сначала очищает поле.

        Args:
            access_code: Ключ доступа.
            clear_first: Если True, сначала очищает поле.
        """
        with allure.step(
            f"Вводим ключ доступа: '{access_code}' (очистка: {clear_first})"
        ):
            try:
                self.access_code_input.should(be.visible)

                if clear_first:
                    self.access_code_input.clear()

                self.access_code_input.type(access_code)

            except TimeoutException:
                raise AssertionError(
                    "❌ Access Code field not found or not visible!\n"
                    f"   Access Code: {access_code}\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while entering access code!\n"
                    f"   Access Code: {access_code}\n"
                    f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 3️⃣ 🖱️ ДЕЙСТВИЯ С КНОПКАМИ
    # ========================================================================

    @allure.step("Нажатие на кнопку Establish Connect и ожидание ответа системы")
    def click_establish_connect(self):
        """Кликает по кнопке и ждет, пока JS обработает запрос (3 секунды)."""
        self.establish_connect_btn.click()

        with allure.step("Ожидание смены статуса телеметрии (уход из SYSTEM READY)"):
            try:
                self.system_telemetry.should(have.no.text("SYSTEM READY"))
            except Exception as e:
                raise AssertionError(
                    "❌ System did not respond after connection attempt!\n"
                    "   Telemetry is still showing 'SYSTEM READY'. "
                    "Check if JS timeout or button click failed."
                ) from e

        return self

    @allure.step("Клик по кнопке переключения видимости пароля (Глаз)")
    def click_toggle_password(self):
        """Нажимает на иконку глаза, чтобы показать/скрыть пароль."""
        try:
            self.toggle_password_btn.click()
        except Exception as e:
            raise AssertionError(
                f"❌ Failed to click toggle password button!\n" f"   Error: {e}"
            ) from e
        return self

    # endregion

    # ========================================================================
    # region 4️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================

    @allure.step("Проверка типа поля Access Code")
    def verify_access_code_type(self, expected_type: str):
        """Проверяет атрибут type поля ввода.

        Args:
            expected_type: 'password' (скрыт) или 'text' (виден)
        """
        try:
            actual_type = self.access_code_input().get_attribute("type")

            if actual_type != expected_type:
                raise AssertionError(
                    f" Access code type mismatch!\n"
                    f"   Expected: {expected_type}\n"
                    f"   Actual: {actual_type}"
                )
        except AssertionError:
            raise
        except Exception as e:
            raise AssertionError(
                f"❌ Unexpected error while checking access code type!\n"
                f"   Expected: {expected_type}\n"
                f"   Error: {e}"
            ) from e
        return self

    @allure.step("Проверка появления блока ошибки авторизации")
    def should_show_auth_error(self, expected_text: str):
        """Проверяет, что блок ошибки авторизации отображается и содержит верный текст.

        Args:
            expected_type: точный текст для проверки
        """
        with allure.step(f"Ожидаемый текст ошибки: '{expected_text}'"):
            try:
                self.auth_error_message.should(be.visible).should(
                    have.text(expected_text)
                )
            except TimeoutException:
                raise AssertionError(
                    "❌ Auth error message is not visible or text does not match!\n"
                    f"   Expected text: {expected_text}\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking auth error visibility!\n"
                    f"   Expected text: {expected_text}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Проверка состояния кнопки Establish Connect")
    def should_be_establish_connect_btn(self, is_enabled: bool = False):
        """
        Проверяет состояние кнопки Establish Connection.

        Args:
            is_enabled: Если True — проверяет, что кнопка активна.
                    Если False (по умолчанию) — проверяет, что кнопка неактивна.
        """
        state = "enabled" if is_enabled else "disabled"
        with allure.step(f"Ожидаемое состояние кнопки: {state}"):
            try:
                if is_enabled:
                    self.establish_connect_btn.should(be.enabled)
                else:
                    self.establish_connect_btn.should(be.disabled)
            except TimeoutException:
                raise AssertionError(
                    f"❌ Establish Connection button is not {state}!\n"
                    f"   Timeout: button did not become {state} in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking button state!\n"
                    f"   Expected state: {state}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Проверяем состояние пользователя в хранилище")
    def verify_user_saved_in_storage(
        self,
        expected_callsign: str | None = None,
        is_saved: bool = True,
        check_local: bool = False,
        check_session: bool = False,
    ):
        """Проверяет наличие и корректность позывного пользователя в хранилище.
        Если позывной сохранен корректно, считаем, что весь объект пользователя сохранен.

        Args:
            expected_callsign: Ожидаемый позывной.
            is_saved: Флаг наличия данных (True - данные есть, False - хранилище пустое).
            check_local: Проверять localStorage.
            check_session: Проверять sessionStorage.
        """

        if not check_local and not check_session:
            check_session = True

        storages_to_check = []
        if check_local:
            storages_to_check.append("localStorage")
        if check_session:
            storages_to_check.append("sessionStorage")

        for storage_name in storages_to_check:
            with allure.step(f"Получаем объект currentUser из {storage_name}"):

                raw_data = browser.driver.execute_script(
                    f"return {storage_name}.getItem('currentUser');"
                )

                if not is_saved:
                    assert (
                        raw_data is None
                    ), f"❌ Ожидали, что {storage_name} будет пустым, но нашли данные: {raw_data}"
                    continue

                assert (
                    raw_data is not None
                ), f"❌ Ожидали данные в {storage_name}, но ключ 'currentUser' отсутствует!"

                try:
                    user_data = json.loads(raw_data)
                except json.JSONDecodeError:
                    raise AssertionError(
                        f"❌ Данные в {storage_name} не являются валидным JSON: {raw_data}"
                    )

                if expected_callsign:
                    assert user_data.get("callsign") == expected_callsign, (
                        f"❌ [{storage_name}] Callsign mismatch! Expected: {expected_callsign}, "
                        f"Got: {user_data.get('callsign')}"
                    )

        return self

    @allure.step("Проверяем значение в поле Callsign")
    def verify_callsign_value(self, expected_value: str):
        """Проверяет, что в поле callsign осталось только ожидаемое значение."""
        try:
            self.callsign_input.should(have.value(expected_value))
        except TimeoutException:
            actual_value = self.callsign_input().get_attribute("value")
            raise AssertionError(
                "❌ Callsign value mismatch!\n"
                f"   Expected: '{expected_value}'\n"
                f"   Actual: '{actual_value}'"
            )
        return self
    
    # endregion
    # ========================================================================
