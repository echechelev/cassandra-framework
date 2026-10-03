import allure
from selene import be, browser, have
from selenium.common.exceptions import TimeoutException

from pages.core import CorePage
from tests import data


class LoginPage(CorePage):

    # URL
    PATH = data.LOGIN_URL

    # Поля ввода
    callsign_input = browser.element('[data-wm-id="login-callsign-input"]')
    access_code_input = browser.element('[data-wm-id="login-access-code-input"]')

    # Кнопки
    establish_connect_btn = browser.element('[data-wm-id="establish-connect-btn"]')
    toggle_password_btn = browser.element('[data-wm-id="toggle-password-btn"]')

    # Информационные панели
    page_subtitle = browser.element('[data-wm-id="login-page-subtitle"]')
    auth_error_message = browser.element('[data-wm-id="auth-error-message"]')

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌐 Открытие страницы авторизации")
    def open(self):
        """Открывает страницу авторизации и проверяет её загрузку."""

        with allure.step(f"Открываем страницу: {self.PATH}"):
            browser.open(self.PATH)

        with allure.step("Проверяем URL и отрисовку элементов"):
            try:
                self.wait_for_url(expected_url_part=data.LOGIN_URL)

                self.callsign_input.should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Login page did not load!\n"
                    f"   Expected URL part: {data.LOGIN_URL}\n"
                    f"   Actual URL: {browser.driver.current_url}\n"
                    "   Timeout: page did not load or URL did not match"
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

    @allure.step("Ввод кода доступа")
    def enter_access_code(self, new_code: str, clear: bool = False):
        """Вводит код доступа. По умолчанию дописывает, если clear=True — очищает."""
        if clear:
            with allure.step(f"Очистка и ввод в поле 'Access code': '{new_code}'"):
                self.access_code_input.set_value(new_code)
        else:
            with allure.step(f"Дозапись в поле 'Access code': '{new_code}'"):
                self.access_code_input.type(new_code)
        return self

    # endregion

    # ========================================================================
    # region 3️⃣ 🖱️ Методы для кнопок 
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

    @allure.step("Нажатие на кнопку Toggle password")
    def click_toggle_password(self):
        """Переключает видимость пароля."""
        with allure.step("Кликаем по кнопке Toggle password"):
            try:
                self.toggle_password_btn.should(be.visible).should(be.enabled)
                self.toggle_password_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Toggle password button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Toggle password!\n"
                    f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 4️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================
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

    # endregion
    # ========================================================================