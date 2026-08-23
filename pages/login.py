import allure
from selene import be, browser, have
from selenium.common.exceptions import TimeoutException, WebDriverException


class LoginPage:
    """Страница авторизации (login.html)."""

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
    system_telemetry = browser.element('[data-wm-id="system-telemetry"]')

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌐 Открытие страницы авторизации")
    def open(self):
        """Открывает страницу авторизации."""
        browser.open(self.PATH)
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

    @allure.step("Проверка URL страницы авторизации")
    def should_be_on_login_page(self):
        """Проверяет, что браузер находится на странице Login Page."""
        with allure.step("Ожидаем, что URL содержит 'login.html'"):
            try:
                browser.should(have.url_containing("login.html"))
            except TimeoutException:
                raise AssertionError(
                    "❌ Not on Login Page!\n"
                    "   Timeout: URL did not contain 'login.html' in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking URL!\n" f"   Error: {e}"
                ) from e
        return self

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

    @allure.step("Проверка текста телеметрии")
    def verify_telemetry_text(self, expected_text: str):
        """Проверяет, что текст телеметрии точно совпадает с ожидаемым.

        Args:
            expected_type: точный текст для проверки
        """
        with allure.step(f"Ожидаемый текст: '{expected_text}'"):
            try:
                self.system_telemetry.should(have.exact_text(expected_text))
            except TimeoutException:
                raise AssertionError(
                    "❌ Telemetry text does not match!\n"
                    f"   Expected: {expected_text}\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while verifying telemetry text!\n"
                    f"   Expected: {expected_text}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Проверка цвета телеметрии")
    def verify_telemetry_color(
        self, green: bool = False, red: bool = False, blue: bool = False
    ):
        """Проверяет цвет телеметрии. Необходимо передать green=True, red=True или blue=True.

        Args:
            green: зеленый, если True передан, проверяет.
            red: красный, если True передан, проверяет.
            blue: синий, если True передан, проверяет.
        """

        if green:
            expected_color = "rgb(46, 204, 113)"
            color_name = "зелёный"
        elif red:
            expected_color = "rgb(231, 76, 60)"
            color_name = "красный"
        elif blue:
            expected_color = "rgb(77, 166, 255)"
            color_name = "синий"
        else:
            raise ValueError(
                "You must specify either green=True, red=True, or blue=True"
            )

        with allure.step(f"Ожидаемый цвет: {color_name}"):
            try:
                script = (
                    "return window.getComputedStyle("
                    "document.querySelector('[data-wm-id=\"system-telemetry\"]')"
                    ").color.replace('rgba(', 'rgb(').replace(', 1)', '');"
                )
                actual_color = browser.driver.execute_script(script)

                if actual_color != expected_color:
                    raise AssertionError(
                        f"❌ Telemetry color does not match!\n"
                        f"   Expected: {color_name} ({expected_color})\n"
                        f"   Actual: {actual_color}"
                    )

            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while verifying telemetry color!\n"
                    f"   Expected: {color_name} ({expected_color})\n"
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

    @allure.step("Проверка ограничения максимальной длины поля")
    def verify_max_length(self, element, max_length: int, char: str = "A"):
        """Универсальный метод проверки maxlength.

        Args:
            element: Selene-элемент (например, self.callsign_input)
            max_length: Максимально допустимая длина (например, 100)
            char: Символ для заполнения (по умолчанию 'A')
        """
        with allure.step(f"Проверка лимита: {max_length} символов"):
            try:
                element.clear()
                element.type(char * max_length)

                current_value = element().get_attribute("value") or ""

                if len(current_value) != max_length:
                    raise AssertionError(
                        f"❌ Length mismatch before extra char!\n"
                        f"   Expected: {max_length}\n"
                        f"   Actual: {len(current_value)}"
                    )

                try:
                    element.type(char)
                except WebDriverException:
                    pass

                final_value = element().get_attribute("value") or ""
                if len(final_value) != max_length:
                    raise AssertionError(
                        f"❌ Max length limit failed! Extra character was added.\n"
                        f"   Expected: {max_length}\n"
                        f"   Actual: {len(final_value)}"
                    )

            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while verifying max length!\n"
                    f"   Max length: {max_length}\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("Проверяем состояние пользователя в localStorage")
    def verify_user_saved_in_localstorage(
        self,
        expected_callsign: str | None = None,
        expected_role: str | None = None,
        expected_full_name: str | None = None,
        is_saved: bool = True,
    ):
        """Проверяет содержимое localStorage после авторизации (успешной или нет).

        Args:
            expected_callsign: ожидаемый позывной (если is_saved=True).
            expected_role: ожидаемая роль (если is_saved=True).
            expected_full_name: ожидаемое имя (если is_saved=True).
            is_saved: True - данные должны быть, False - хранилище должно быть пустым.
        """
        with allure.step("Получаем и парсим объект currentUser из localStorage"):
            try:
                user_data = browser.driver.execute_script(
                    "return JSON.parse(localStorage.getItem('currentUser'))"
                )

                if not is_saved:
                    assert user_data is None, (
                        f"❌ Expected LocalStorage to be empty (authentication failed), "
                        f"but found data: {user_data}"
                    )
                    return self

                assert user_data is not None, "❌ User data not found in localStorage!"

                if expected_callsign:
                    assert user_data["callsign"] == expected_callsign, (
                        f"❌ Callsign mismatch! Expected: {expected_callsign}, "
                        f"Got: {user_data.get('callsign')}"
                    )
                if expected_role:
                    assert user_data["role"] == expected_role, (
                        f"❌ Role mismatch! Expected: {expected_role}, "
                        f"Got: {user_data.get('role')}"
                    )
                if expected_full_name:
                    assert user_data["fullName"] == expected_full_name, (
                        f"❌ FullName mismatch! Expected: {expected_full_name}, "
                        f"Got: {user_data.get('fullName')}"
                    )

            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking localStorage!\n"
                    f"   Error: {e}"
                ) from e

        return self

    # endregion
    # ========================================================================
