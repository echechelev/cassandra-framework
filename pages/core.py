import json

import allure
from selene import be, browser, have, query
from selene.core.entity import Element
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣


class CorePage:
    """Общие методы и локаторы."""

    # Кнопки навигации
    log_in_btn = browser.element('[data-wm-id="nav-login-btn"]')
    sign_up_btn = browser.element('[data-wm-id="nav-signup-btn"]')
    restore_btn = browser.element('[data-wm-id="nav-restore-btn"]')
    dashboard_btn = browser.element('[data-wm-id="nav-dashboard-btn"]')
    cis_index_table_btn = browser.element('[data-wm-id="nav-cis-index-table-btn"]')
    galaxy_map_btn = browser.element('[data-wm-id="nav-galaxy-map-btn"]')

    # Служебные элементы 
    system_telemetry = browser.element('[data-wm-id="system-telemetry"]')

    # ========================================================================
    # region 1️⃣ 🧭 Навигация
    # ========================================================================

    @allure.step("Открытие страницы")
    def open_url(self, url: str):
        """Открывает переданный URL в браузере."""
        with allure.step(f"URL: {url}"):
            try:
                browser.open(url)
            except Exception as e:
                raise AssertionError(
                    f"❌ Не удалось открыть страницу!\n"
                    f"   Ожидаемый URL: {url}\n"
                    f"   Ошибка браузера: {e}"
                ) from e
        return self

    @allure.step("Ожидание перехода на URL")
    def wait_for_url(
        self, 
        expected_url_part: str, 
        element_to_wait: Element | None = None, 
        timeout: float = 10.0
    ):
        """
        Ждет появления элемента (если передан) и перехода на URL, содержащий ожидаемую часть.
        
        Args:
            expected_url_part: Ожидаемая часть URL.
            element_to_wait: Selene-элемент для ожидания появления (по умолчанию None).
            timeout: Таймаут ожидания в секундах (по умолчанию 10.0).
        """
        try:
            if element_to_wait is not None:
                with allure.step("Ожидаем появление элемента"):
                    element_to_wait.should(be.visible)

            with allure.step(f"Ожидаем URL, содержащий: '{expected_url_part}'"):
                WebDriverWait(browser.driver, timeout).until(EC.url_contains(expected_url_part))

        except TimeoutException:
            if element_to_wait is not None:
                raise AssertionError(
                    f"❌ Element did not appear within {timeout} seconds!\n"
                    f"   Expected URL part: {expected_url_part}\n"
                    f"   Condition: Element must be visible before URL check"
                )
            else:
                raise AssertionError(
                    f"❌ URL did not contain '{expected_url_part}' within {timeout} seconds!\n"
                    f"   Current URL: {browser.driver.current_url}\n"
                    f"   Expected part: {expected_url_part}\n"
                    f"   Condition: Browser URL must contain the expected part"
                )
   
        return self

    #endregion
    
    # ========================================================================
    # region 2️⃣ 🖱️ Методы для кнопок 
    # ========================================================================

    @allure.step("Нажатие кнопки Log In")
    def click_log_in(self):
        """Нажимает кнопку входа в систему."""
        with allure.step("Кликаем по кнопке Log In"):
            try:
                self.log_in_btn.should(be.visible).should(be.enabled)
                self.log_in_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Log In button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Log In!\n"
                    f"   Error: {e}"
                ) from e
        return self
    
    @allure.step("Нажатие кнопки Sign Up")
    def click_sign_up(self):
        """Нажимает кнопку регистрации нового пользователя."""
        with allure.step("Кликаем по кнопке Sign Up"):
            try:
                self.sign_up_btn.should(be.visible).should(be.enabled)
                self.sign_up_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Sign Up button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Sign Up!\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие кнопки Restore")
    def click_restore(self):
        """Нажимает кнопку восстановления доступа."""
        with allure.step("Кликаем по кнопке Restore"):
            try:
                self.restore_btn.should(be.visible).should(be.enabled)
                self.restore_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Restore button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Restore!\n"
                    f"   Error: {e}"
                ) from e
        return self


    @allure.step("Нажатие кнопки Dashboard")
    def click_dashboard(self):
        """Нажимает кнопку перехода на Dashboard."""
        with allure.step("Кликаем по кнопке Dashboard"):
            try:
                self.dashboard_btn.should(be.visible).should(be.enabled)
                self.dashboard_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Dashboard button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Dashboard!\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие кнопки CIS Index Table")
    def click_cis_index_table(self):
        """Нажимает кнопку перехода к CIS Index Table."""
        with allure.step("Кликаем по кнопке CIS Index Table"):
            try:
                self.cis_index_table_btn.should(be.visible).should(be.enabled)
                self.cis_index_table_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ CIS Index button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking CIS Index!\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие кнопки Galaxy Map")
    def click_galaxy_map(self):
        """Нажимает кнопку карта галактики."""
        with allure.step("Кликаем по кнопке Galaxy Map"):
            try:
                self.galaxy_map_btn.should(be.visible).should(be.enabled)
                self.galaxy_map_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Galaxy Map button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Restore!\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Обновляем страницу браузера")
    def click_refresh_page(self):
        """
        Обновляет текущую страницу (аналог F5 или Ctrl+R).
        """
        try:
            browser.driver.refresh()
        except Exception as e:
            raise AssertionError("❌ Failed to refresh page!\n" f"   Error: {e}") from e
        return self

    @allure.step("Нажатие кнопки 'Назад' в браузере")
    def click_browser_back(self):
        """Нажимает кнопку 'Назад' в браузере для возврата на предыдущую страницу."""
        try:
            browser.driver.back()
        except Exception as e:
            raise AssertionError(
                f"❌ Unexpected error while clicking browser Back button!\n"
                f"   Error: {e}"
            ) from e
        return self

    #endregion

    # ========================================================================
    # region 3️⃣ 💬 ТЕЛЕМЕТРИЯ И ТЕКСТЫ
    # ========================================================================
    @allure.step("Проверка текста телеметрии")
    def verify_telemetry_text(self, expected_text: str):
        """
        Проверяет точное совпадение текста системной телеметрии.
        """
        with allure.step(f"Ожидаемый текст телеметрии: '{expected_text}'"):
            try:
                self.system_telemetry.should(have.exact_text(expected_text))
            except TimeoutException:
                raise AssertionError(
                    f"❌ Telemetry text does not match or element not found!\n"
                    f"   Expected: '{expected_text}'\n"
                    f"   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Error while verifying telemetry!\n"
                    f"   Expected: '{expected_text}'\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Проверка текста элемента")
    def verify_text(self, element, expected_text: str):
        """
        Проверяет, что текст элемента содержит ожидаемую подстроку.
        (Используется для любых элементов на странице).
        """
        with allure.step(f"Проверяем текст элемента: '{expected_text}'"):
            try:
                element.should(have.text(expected_text.strip()))
            except TimeoutException:
                raise AssertionError(
                    f"❌ Element not found or text does not contain expected substring!\n"
                    f"   Expected: '{expected_text}'\n"
                    f"   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Error while verifying element text!\n"
                    f"   Expected: '{expected_text}'\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Проверка цвета телеметрии (NOT Cassandra)")
    def verify_telemetry_color_not_cassandra(
        self, green: bool = False, red: bool = False, blue: bool = False
    ):
        """
        Проверяет цвет всего блока телеметрии [data-wm-id="system-telemetry"].

        Используется на страницах, где НЕТ имени Кассандры:
        - Login Page
        - Registration Page
        - Password Recovery Page
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
                self.system_telemetry.should(be.visible)

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

    @allure.step("Проверка цвета телеметрии (WITH Cassandra, игнорируя её имя)")
    def verify_telemetry_color_with_cassandra(
        self, green: bool = False, red: bool = False, blue: bool = False
    ):
        """
        Проверяет цвет ТОЛЬКО текста сообщения [data-wm-id="telemetry-message"],
        игнорируя цвет имени Кассандры.

        Используется на Dashboard Page, где имя ИИ и сообщение — разные элементы.
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

        telemetry_selector = "[id='typing-target'], [data-wm-id='telemetry-message']"

        with allure.step(f"Ожидаемый цвет сообщения: {color_name}"):
            try:

                element = browser.element(telemetry_selector)
                element.should(be.visible)

                script = """ 
                    return window.getComputedStyle(arguments[0]).color
                    .replace('rgba(', 'rgb(')
                    .replace(', 1)', '');
                """

                actual_color = browser.driver.execute_script(script, element())

                if actual_color != expected_color:
                    raise AssertionError(
                        f"❌ Telemetry message color does not match!\n"
                        f"   Expected: {color_name} ({expected_color})\n"
                        f"   Actual: {actual_color}"
                    )

            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while verifying telemetry message color!\n"
                    f"   Expected: {color_name} ({expected_color})\n"
                    f"   Error: {e}"
                ) from e

        return self

    # endregion

    # ========================================================================
    # region 4️⃣ 💾 LOCALSTORAGE\SESSIONSTORAGE
    # ========================================================================
    @allure.step("Полная очистка хранилищ браузера")
    def clear_all_storages(self):
        """
        Полностью очищает localStorage и sessionStorage браузера.
        Используется для обеспечения стерильности тестового окружения.
        """
        with allure.step("Выполняем очистку localStorage и sessionStorage"):
            try:
                browser.driver.execute_script(
                    "localStorage.clear(); sessionStorage.clear();"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Failed to clear browser storages!\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Установка повреждённых данных в хранилище")
    def set_corrupted_user_data(
        self, check_local: bool = False, check_session: bool = False
    ):
        """
        Записывает невалидный JSON в localStorage и/или sessionStorage
        под ключом 'currentUser'.

        Используется для тестирования graceful degradation системы
        (например, проверка редиректа при повреждённых данных).
        """
        if not check_local and not check_session:
            check_local = True
            check_session = True

        storages_to_corrupt = []
        if check_local:
            storages_to_corrupt.append("localStorage")
        if check_session:
            storages_to_corrupt.append("sessionStorage")

        for storage_name in storages_to_corrupt:
            with allure.step(f"Записываем 'broken' в {storage_name}.currentUser"):
                try:
                    browser.driver.execute_script(
                        f"{storage_name}.setItem('currentUser', 'broken');"
                    )
                except Exception as e:
                    raise AssertionError(
                        f"❌ Failed to set corrupted user data in {storage_name}!\n"
                        f"   Error: {e}"
                    ) from e

        return self

    @allure.step("Проверка состояния данных пользователя в хранилище")
    def verify_user_data_in_storage(
        self,
        expected_callsign: str | None = None,
        check_local: bool = False,
        check_session: bool = False,
        should_exist: bool = True,
    ):
        """
        Проверяет наличие или отсутствие пользователя в хранилищах.

        Args:
            expected_callsign: Ожидаемый позывной (например, 'NOVA' или 'KNOPA').
                            Если None — проверяет, что хранилище вообще пустое/не пустое.
            check_local: Флаг проверки localStorage.
            check_session: Флаг проверки sessionStorage.
            should_exist: Если True — проверяем наличие, если False — отсутствие.
        """
        if not check_local and not check_session:
            check_local = True
            check_session = True

        if expected_callsign is None:
            state_word = "не пустое" if should_exist else "пустое"

            if check_local:
                with allure.step(f"Проверяем, что localStorage {state_word}"):
                    registered_users_str = browser.driver.execute_script(
                        "return localStorage.getItem('registeredUsers');"
                    )
                    restored_users_str = browser.driver.execute_script(
                        "return localStorage.getItem('restoredUsers');"
                    )

                    registered_users = json.loads(registered_users_str) if registered_users_str else {}
                    restored_users = json.loads(restored_users_str) if restored_users_str else {}

                    has_any_user = bool(registered_users) or bool(restored_users)

                    if should_exist:
                        assert has_any_user, (
                            "❌ localStorage is completely empty, although data was expected.\n"
                            f"registeredUsers: {list(registered_users.keys())}\n"
                            f"restoredUsers: {list(restored_users.keys())}"
                        )
                    else:
                        assert not has_any_user, (
                            "❌ localStorage is not empty, although full cleanup was expected.\n"
                            f"registeredUsers: {list(registered_users.keys())}\n"
                            f"restoredUsers: {list(restored_users.keys())}"
                        )

            if check_session:
                with allure.step(f"Проверяем, что sessionStorage {state_word}"):
                    current_user_str = browser.driver.execute_script(
                        "return sessionStorage.getItem('currentUser');"
                    )

                    if should_exist:
                        assert current_user_str is not None, (
                            "❌ sessionStorage is empty, although currentUser was expected"
                        )
                    else:
                        assert current_user_str is None, (
                            f"❌ sessionStorage is not empty: {current_user_str}"
                        )

            return self

        callsign_upper = expected_callsign.upper()
        state_word = "присутствует" if should_exist else "отсутствует"

        if check_local:
            with allure.step(f"Проверяем {state_word} '{callsign_upper}' в localStorage"):
                registered_users_str = browser.driver.execute_script(
                    "return localStorage.getItem('registeredUsers');"
                )
                registered_users = json.loads(registered_users_str) if registered_users_str else {}

                restored_users_str = browser.driver.execute_script(
                    "return localStorage.getItem('restoredUsers');"
                )
                restored_users = json.loads(restored_users_str) if restored_users_str else {}

                is_in_registered = callsign_upper in registered_users
                is_in_restored = callsign_upper in restored_users

                if should_exist:
                    assert is_in_registered or is_in_restored, (
                        f"❌ Callsign '{callsign_upper}' is missing in localStorage.\n"
                        f"registeredUsers: {list(registered_users.keys())}\n"
                        f"restoredUsers: {list(restored_users.keys())}"
                    )
                else:
                    assert not (is_in_registered or is_in_restored), (
                        f"❌ Callsign '{callsign_upper}' still found in localStorage after cleanup.\n"
                        f"registeredUsers: {list(registered_users.keys())}\n"
                        f"restoredUsers: {list(restored_users.keys())}"
                    )

        if check_session:
            with allure.step(f"Проверяем {state_word} '{callsign_upper}' в sessionStorage"):
                current_user_str = browser.driver.execute_script(
                    "return sessionStorage.getItem('currentUser');"
                )

                if should_exist:
                    assert current_user_str is not None, (
                        "❌ Key 'currentUser' is missing in sessionStorage"
                    )
                    try:
                        current_user = json.loads(current_user_str)
                    except json.JSONDecodeError:
                        raise AssertionError(
                            f"❌ Data in 'currentUser' is not valid JSON: {current_user_str}"
                        )

                    actual_callsign = current_user.get("callsign", "").upper()
                    assert actual_callsign == callsign_upper, (
                        f"❌ Expected callsign '{callsign_upper}', got '{actual_callsign}'"
                    )
                else:
                    if current_user_str is not None:
                        try:
                            current_user = json.loads(current_user_str)
                            actual_callsign = current_user.get("callsign", "").upper()
                            assert actual_callsign != callsign_upper, (
                                f"❌ User '{callsign_upper}' is still active in sessionStorage"
                            )
                        except json.JSONDecodeError:
                            pass

        return self

    # endregion

    # ========================================================================
    # region 5️⃣ 🛠️ СЛУЖЕБНЫЕ МЕТОДЫ
    # ========================================================================

    def fast_forward_uplink(self):
        """
        Мгновенно пропускает анимацию аплинка через sessionStorage.
        Идеально для вставки в фикстуру перед тестами других страниц.
        """
        browser.driver.execute_script("sessionStorage.setItem('uplinkCompleted', 'true');")
        
        return self


    # endregion

    # ========================================================================
    # region 6️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================
    @allure.step("Проверка содержимого кнопок навигации")
    def check_button_content(self, button_id: str, expected_text: str):
        """Проверяет наличие и текстовое содержимое кнопки навигации."""
        with allure.step(f"Проверяем кнопку {button_id}"):
            try:
                btn = browser.element(f'[data-wm-id="{button_id}"]')
                btn.should(be.visible).should(be.enabled)

                actual_text = btn.get(query.text)

                assert expected_text in actual_text, (
                    f"❌ Text of button {button_id} does not match!\n"
                    f"   Expected substring: '{expected_text}'\n"
                    f"   Actual text: '{actual_text}'"
                )
            except TimeoutError:
                raise AssertionError(
                    f"❌ Button {button_id} not found or not visible!\n"
                    f"   Expected text: {expected_text}\n"
                    f"   Timeout: element did not appear in time"
                )
            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking button {button_id}!\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Проверка атрибута href кнопки навигации")
    def check_button_href(self, button_id: str, expected_href: str):
        """Проверяет, что атрибут href кнопки заканчивается на ожидаемое значение."""
        with allure.step(f"Проверяем href кнопки {button_id}"):
            btn = browser.element(f'[data-wm-id="{button_id}"]')
            btn.should(be.visible)

            actual_href = btn.get(query.attribute('href'))

            assert actual_href.endswith(expected_href), (
                f"❌ Invalid href for button {button_id}!\n"
                f"   Expected to end with: {expected_href}\n"
                f"   Actual value: {actual_href}"
            )
        return self

    @allure.step("Проверяем значение поля")
    def verify_field_value(self, element, expected_value: str):
        """Проверяет, что поле ввода содержит ожидаемое значение."""
        try:
            element.should(have.value(expected_value))
        except TimeoutException:
            actual_value = element().get_attribute("value")
            raise AssertionError(
                f"❌ Field value mismatch!\n"
                f"   Expected: '{expected_value}'\n"
                f"   Actual: '{actual_value}'"
            )
        return self

    @allure.step("Проверка ограничения максимальной длины поля")
    def verify_max_length(self, element, max_length: int, char: str = "A"):
        """Универсальный метод проверки maxlength."""
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

    @allure.step("Проверяем состояние поля: пустое и (только для чтения / редактируемое)")
    def verify_empty_field_state(self, element, is_readonly: bool = True):
        """Проверяет, что поле ввода пустое и имеет (или не имеет) атрибут readonly."""
        try:
            element.should(have.value(""))
        except TimeoutException:
            actual_value = element().get_attribute("value")
            raise AssertionError(
                f"❌ Field is not empty!\n"
                f"   Expected value: ''\n"
                f"   Actual value: '{actual_value}'"
            )

        state_desc = "readonly" if is_readonly else "editable"

        try:
            if is_readonly:
                element.should(have.attribute("readonly"))
            else:
                element.should(have.no.attribute("readonly"))
        except TimeoutException:
            actual_readonly_val = element().get_attribute("readonly")
            raise AssertionError(
                f"❌ Field is not {state_desc}!\n"
                f"   Expected: attribute 'readonly' to be {'present' if is_readonly else 'absent'}\n"
                f"   Actual readonly attribute value: '{actual_readonly_val}'"
            )
        return self

    @allure.step("Проверка появления контейнера ошибки")
    def should_show_error_container(self, element: Element, expected_text: str):
        """Проверяет, что контейнер ошибки отображается и содержит верный текст."""
        with allure.step(f"Ожидаемый текст ошибки: '{expected_text}'"):
            try:
                element.should(be.visible).should(have.text(expected_text))
            except TimeoutException:
                raise AssertionError(
                    f"❌ Error container not visible or text mismatch!\n"
                    f"   Expected text: '{expected_text}'\n"
                    f"   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking error container!\n"
                    f"   Expected text: '{expected_text}'\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Проверяем состояние кнопки")
    def verify_button_state(self, element, is_enabled: bool = True):
        """Проверяет состояние кнопки (активна или неактивна)."""
        try:
            if is_enabled:
                element.should(be.enabled)
            else:
                element.should(be.disabled)
        except TimeoutException:
            expected_state = "ENABLED" if is_enabled else "DISABLED"
            is_actually_disabled = element.get_attribute("disabled")
            actual_state = "DISABLED" if is_actually_disabled else "ENABLED"
            
            raise AssertionError(
                f"❌ Button state mismatch!\n"
                f"   Expected state: {expected_state}\n"
                f"   Actual state: {actual_state}"
            )
        return self

    @allure.step("Проверка атрибута элемента")
    def verify_attribute(self, element, attr_name: str, expected_value: str):
        """
        Универсальная проверка любого атрибута элемента.
        """
        try:
            element.should(have.attribute(attr_name).value(expected_value))  # type: ignore
        except TimeoutException:
            raise AssertionError(
                f" Attribute verification failed!\n"
                f"   Expected attribute '{attr_name}' to be '{expected_value}'\n"
                f"   Element: {element}"
            )
        return self  