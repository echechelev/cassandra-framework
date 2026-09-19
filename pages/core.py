import json

import allure
from selene import be, browser, have, query
from selene.core.entity import Element
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CorePage:
    """Общие методы и локаторы."""

    # Кнопки Planet Bar
    galaxy_map_btn = browser.element('[data-wm-id="nav-galaxy-map"]')
    flight_calc_btn = browser.element('[data-wm-id="flight-calc-btn"]')
    cis_table_btn = browser.element('[data-wm-id="cis-table-btn"]')
    mission_control_btn = browser.element('[data-wm-id="mission-control-btn"]')
    nav_settings_btn = browser.element('[data-wm-id="nav-settings"]')

    # Кнопки навигации и перехода
    log_in_btn = browser.element('[data-wm-id="btn-login"]')
    sign_up_btn = browser.element('[data-wm-id="btn-signup"]')
    restore_btn = browser.element('[data-wm-id="btn-restore"]')

    # Служебные элементы (для тестов анимации и состояний)
    system_telemetry = browser.element('[data-wm-id="system-telemetry"]')
    telemetry_message = browser.element("[id='typing-target'], [data-wm-id='telemetry-message']")
    progress_fill = browser.element("#progress-fill")
    progress_text = browser.element("#progress-text")
    progress_container = browser.element("#uplink-progress-container")

    # Добавляем коллекция для метода check_progress_bar_appeared_once
    progress_bars = browser.all("#progress-fill")

    # Временный локатор кнопка "Назад", на страницах заглушках для планет бара
    back_btn = browser.element(".back-btn")

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("Переходим по указанному URL")
    def open_url(self, path: str):
        """Открывает страницу по относительному или полному пути."""

        if path.startswith(("http", "file")):
            browser.driver.get(path)
        else:

            current_url = browser.driver.current_url
            base_url = current_url.rsplit("/", 1)[0]
            browser.driver.get(f"{base_url}/{path.lstrip('/')}")

        return self

    @allure.step("Переход в Galaxy Map")
    def navigate_to_galaxy_map(self):
        """
        Кликает по кнопке 'Galaxy Map', проверяет URL и возвращается на Dashboard.
        """
        self.galaxy_map_btn.should(be.clickable)
        self.galaxy_map_btn.click()
        self.wait_for_url("galaxy-map.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        self.back_btn.click()
        self.wait_for_url("dashboard.html")

        return self

    @allure.step("Переход в CIS Table")
    def navigate_to_cis_table(self):
        """
        Кликает по кнопке 'CIS Table', проверяет URL и возвращается на Dashboard.
        """
        self.cis_table_btn.should(be.clickable)
        self.cis_table_btn.click()
        self.wait_for_url("cis-table.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        self.back_btn.click()
        self.wait_for_url("dashboard.html")

        return self

    @allure.step("Переход в Mission Control")
    def navigate_to_mission_control(self):
        """
        Кликает по кнопке 'Mission Control', проверяет URL и возвращается на Dashboard.
        """
        self.mission_control_btn.should(be.clickable)
        self.mission_control_btn.click()
        self.wait_for_url("mission-control.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        self.back_btn.click()
        self.wait_for_url("dashboard.html")

        return self

    @allure.step("Переход в Settings")
    def navigate_to_settings(self):
        """
        Кликает по кнопке 'Settings', проверяет URL и возвращается на Dashboard.
        """
        self.nav_settings_btn.should(be.clickable)
        self.nav_settings_btn.click()
        self.wait_for_url("settings.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        self.back_btn.click()
        self.wait_for_url("dashboard.html")

        return self

    # endregion

    # ========================================================================
    # region 2️⃣ 🖱️ ДЕЙСТВИЯ С КНОПКАМИ
    # ========================================================================

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
        with allure.step("Кликаем по кнопке 'Назад' в браузере"):
            try:
                browser.driver.back()

            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking browser Back button!\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие кнопки Galaxy Map")
    def click_galaxy_map(self):
        """Нажимает кнопку перехода на страницу Galaxy Map."""
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
                    f" Unexpected error while clicking Galaxy Map!\n" f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие кнопки Log in")
    def click_log_in(self):
        """Нажимает кнопку инициализации системы Log in."""
        with allure.step("Кликаем по кнопке Log in"):
            try:
                self.log_in_btn.should(be.visible).should(be.enabled)
                self.log_in_btn.click()

            except TimeoutException:
                raise AssertionError(
                    "❌ Log in button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Log in!\n" f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие кнопки Sign up")
    def click_sign_up(self):
        """Нажимает кнопку инициализации системы Sign up."""
        with allure.step("Кликаем по кнопке Sign up"):
            try:
                self.sign_up_btn.should(be.visible).should(be.enabled)
                self.sign_up_btn.click()

            except TimeoutException:
                raise AssertionError(
                    "❌ Sign up button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Sign up!\n" f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие кнопки Rstore")
    def click_restore(self):
        """Нажимает кнопку инициализации системы Restore."""
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
                    f"❌ Unexpected error while clicking Restore!\n" f"   Error: {e}"
                ) from e
        return self

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
                    f"❌ Текст телеметрии не совпадает или элемент не найден!\n"
                    f"   Expected: '{expected_text}'\n"
                    f"   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Ошибка при проверке телеметрии!\n"
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
            element.should(have.text(expected_text.strip()))
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
                    "❌ Failed to clear browser storages!\n" f"   Error: {e}"
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
                            "❌ localStorage полностью пуст, хотя ожидалось наличие данных.\n"
                            f"registeredUsers: {list(registered_users.keys())}\n"
                            f"restoredUsers: {list(restored_users.keys())}"
                        )
                    else:
                        assert not has_any_user, (
                            "❌ localStorage не пуст, хотя ожидалась полная очистка.\n"
                            f"registeredUsers: {list(registered_users.keys())}\n"
                            f"restoredUsers: {list(restored_users.keys())}"
                        )

            if check_session:
                with allure.step(f"Проверяем, что sessionStorage {state_word}"):
                    current_user_str = browser.driver.execute_script(
                        "return sessionStorage.getItem('currentUser');"
                    )

                    if should_exist:
                        assert current_user_str is not None, "❌ sessionStorage пуст, хотя ожидался currentUser"
                    else:
                        assert current_user_str is None, (
                            f"❌ sessionStorage не пуст: {current_user_str}"
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
                        f"❌ Позывной '{callsign_upper}' отсутствует в localStorage.\n"
                        f"registeredUsers: {list(registered_users.keys())}\n"
                        f"restoredUsers: {list(restored_users.keys())}"
                    )
                else:
                    assert not (is_in_registered or is_in_restored), (
                        f" Позывной '{callsign_upper}' всё ещё найден в localStorage после очистки.\n"
                        f"registeredUsers: {list(registered_users.keys())}\n"
                        f"restoredUsers: {list(restored_users.keys())}"
                    )

        if check_session:
            with allure.step(f"Проверяем {state_word} '{callsign_upper}' в sessionStorage"):
                current_user_str = browser.driver.execute_script(
                    "return sessionStorage.getItem('currentUser');"
                )

                if should_exist:
                    assert current_user_str is not None, "❌ Ключ 'currentUser' отсутствует в sessionStorage"
                    try:
                        current_user = json.loads(current_user_str)
                    except json.JSONDecodeError:
                        raise AssertionError(
                            f" Данные в 'currentUser' не являются валидным JSON: {current_user_str}"
                        )

                    actual_callsign = current_user.get("callsign", "").upper()
                    assert actual_callsign == callsign_upper, (
                        f"❌ Ожидался callsign '{callsign_upper}', получено '{actual_callsign}'"
                    )
                else:
                    if current_user_str is not None:
                        try:
                            current_user = json.loads(current_user_str)
                            actual_callsign = current_user.get("callsign", "").upper()
                            assert actual_callsign != callsign_upper, (
                                f"❌ Пользователь '{callsign_upper}' всё ещё активен в sessionStorage"
                            )
                        except json.JSONDecodeError:
                            pass

        return self

    # endregion

    # ========================================================================
    # region 5️⃣ 🛠️ СЛУЖЕБНЫЕ МЕТОДЫ
    # ========================================================================

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
                    f" URL did not contain '{expected_url_part}' within {timeout} seconds!\n"
                    f"   Current URL: {browser.driver.current_url}\n"
                    f"   Expected part: {expected_url_part}\n"
                    f"   Condition: Browser URL must contain the expected part"
                )

        return self

    @allure.step("Проверка содержимого кнопок навигации")
    def check_button_content(self, button_id: str, expected_text: str):
        """Проверяет наличие и текстовое содержимое кнопки навигации."""
        with allure.step(f"Проверяем кнопку {button_id}"):
            try:
                btn = browser.element(f'[data-wm-id="{button_id}"]')
                btn.should(be.visible).should(be.enabled)

                btn.element(".btn-label").should(have.exact_text(expected_text))

            except TimeoutError:
                raise AssertionError(
                    f"❌ Button {button_id} not found or text mismatch!\n"
                    f"   Expected text: {expected_text}\n"
                    f"   Timeout: button did not appear in time"
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
        
            # В Selene 2.x используем query.attribute() для получения значения атрибута
            actual_href = btn.get(query.attribute('href'))
        
            assert actual_href.endswith(expected_href), (
                f"❌ Неправильный href у кнопки!\n"
                f"   Ожидалось, что заканчивается на: {expected_href}\n"
                f"   Фактическое значение: {actual_href}"
            )
        return self
    
    # endregion