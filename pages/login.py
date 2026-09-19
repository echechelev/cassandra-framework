import allure
from selene import be, browser, have
from selene.core.entity import Element
from selenium.common.exceptions import TimeoutException

from pages.gateway import GatewayPage
from tests import data


class LoginPage(GatewayPage):

    # URL
    PATH = data.LOGIN_URL

    # Поля ввода
    callsign_input = browser.element('[data-wm-id="login-callsign-input"]')
    access_code_input = browser.element('[data-wm-id="login-access-code-input"]')

    # Кнопки
    establish_connect_btn = browser.element('[data-wm-id="establish-connect-btn"]')
    toggle_password_btn = browser.element('[data-wm-id="toggle-password-btn"]')

    # Тексты и ссылки
    page_subtitle = browser.element('[data-wm-id="login-page-subtitle"]')
    auth_error_message = browser.element('[data-wm-id="auth-error-message"]')

    # Свойства, которые переопределяют абстрактные поля из GatewayPage,
    @property
    def toggle_password(self)-> Element:
        return self.toggle_password_btn

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
    # region 2️⃣ 🖱️ ДЕЙСТВИЯ С КНОПКАМИ
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

    # endregion

    # ========================================================================
    # region 3️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================

    @allure.step("Проверка типа поля Access Code")
    def verify_access_code_type(self, expected_type: str):
        """Проверяет атрибут type поля ввода.

        Args:
            expected_type: 'password' (скрыт) или 'text' (виден)
        """
        try:
            self.access_code_input.should(have.attribute("type", expected_type))
        except TimeoutException:
            raise AssertionError(
                f"❌ Access code type mismatch!\n"
                f"   Expected: {expected_type}\n"
                f"   Actual: поле не имеет ожидаемого типа"
            ) from None
        except Exception as e:
            raise AssertionError(
                f"❌ Unexpected error while checking access code type!\n"
                f"   Expected: {expected_type}\n"
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

    # endregion
    # ========================================================================
