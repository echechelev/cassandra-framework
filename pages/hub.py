import json

import allure
from selene import be, browser, have, query
from selene.core.entity import Element
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HubPage:
    """Общие методы и локаторы."""

    # Кнопки Planet Bar
    galaxy_map_btn = browser.element('[data-wm-id="nav-galaxy-map"]')
    flight_calc_btn = browser.element('[data-wm-id="flight-calc-btn"]')
    cis_table_btn = browser.element('[data-wm-id="cis-table-btn"]')
    mission_control_btn = browser.element('[data-wm-id="mission-control-btn"]')
    nav_settings_btn = browser.element('[data-wm-id="nav-settings"]')

    # Кнопки "Log in", "Sign up" "Restore"
    log_in_btn = browser.element('[data-wm-id="btn-login"]')
    sign_up_btn = browser.element('[data-wm-id="btn-signup"]')
    restore_btn = browser.element('[data-wm-id="btn-restore"]')

    # Служебные элементы (для тестов анимации и состояний)
    system_telemetry = browser.element('[data-wm-id="system-telemetry"]')
    telemetry_message = browser.element(
        "[id='typing-target'], [data-wm-id='telemetry-message']"
    )
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

    @allure.step("Проверка текущего URL браузера")
    def verify_current_url(
        self,
        expected_url_part: str,
        wait_for_element: Element | None = None,
        timeout: int = 10,
    ):
        """
        Проверяет, что текущий URL браузера содержит переданную подстроку.
        Опционально ждет появления элемента перед проверкой URL (для синхронизации с анимациями).

        Args:
            expected_url_part: Обязательный аргумент. Часть URL, которая должна быть в адресной строке.
            wait_for_element: Необязательный аргумент. Элемент Selene, появления которого нужно дождаться.
            timeout: Таймаут ожидания элемента в секундах (по умолчанию 10).
        """
        if not expected_url_part or not isinstance(expected_url_part, str):
            raise ValueError(
                "❌ Аргумент 'expected_url_part' обязателен и должен быть непустой строкой!"
            )

        if wait_for_element is not None:
            with allure.step(
                f"Ожидаем появление элемента перед проверкой URL (timeout={timeout}s)"
            ):
                wait_for_element.with_(timeout=timeout).should(be.visible)

        with allure.step(f"Проверяем URL содержащий: '{expected_url_part}'"):
            current_url = browser.driver.current_url

            if expected_url_part not in current_url:
                raise AssertionError(
                    f"❌ URL не совпадает!\n"
                    f"   Ожидалось наличие: '{expected_url_part}'\n"
                    f"   Текущий URL:       {current_url}"
                )

        return self

    @allure.step("Ожидание перехода на URL: {expected_url_part}")
    def wait_for_url(self, expected_url_part: str, timeout: int = 5):
        """
        Ждет, пока URL браузера будет содержать ожидаемую часть.
        Используется для ожидания редиректов после действий пользователя.
        """

        WebDriverWait(browser.driver, timeout).until(EC.url_contains(expected_url_part))

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

    @allure.step("Переход в Galaxy Map")
    def navigate_to_galaxy_map(self):
        """
        Кликает по кнопке 'Galaxy Map', проверяет URL и возвращается на Dashboard.
        """
        self.galaxy_map_btn.should(be.clickable)
        self.galaxy_map_btn.click()
        self.verify_current_url("galaxy-map.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        self.back_btn.click()
        self.verify_current_url("dashboard.html")

        return self

    @allure.step("Переход в CIS Table")
    def navigate_to_cis_table(self):
        """
        Кликает по кнопке 'CIS Table', проверяет URL и возвращается на Dashboard.
        """
        self.cis_table_btn.should(be.clickable)
        self.cis_table_btn.click()
        self.verify_current_url("cis-table.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        self.back_btn.click()
        self.verify_current_url("dashboard.html")

        return self

    @allure.step("Переход в Mission Control")
    def navigate_to_mission_control(self):
        """
        Кликает по кнопке 'Mission Control', проверяет URL и возвращается на Dashboard.
        """
        self.mission_control_btn.should(be.clickable)
        self.mission_control_btn.click()
        self.verify_current_url("mission-control.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        self.back_btn.click()
        self.verify_current_url("dashboard.html")

        return self

    @allure.step("Переход в Settings")
    def navigate_to_settings(self):
        """
        Кликает по кнопке 'Settings', проверяет URL и возвращается на Dashboard.
        """
        self.nav_settings_btn.should(be.clickable)
        self.nav_settings_btn.click()
        self.verify_current_url("settings.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        self.back_btn.click()
        self.verify_current_url("dashboard.html")

        return self

    # endregion

    # ========================================================================
    # region 2️⃣ 🖱️ ДЕЙСТВИЯ С КНОПКАМИ
    # ========================================================================

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
        """Проверяет, что текст телеметрии точно совпадает с ожидаемым.

        Args:
            expected_text: точный текст для проверки
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

    def verify_text(self, element, expected_text: str) -> bool:
        """Проверяет текстовое содержимое элемента по локатору.

        Args:
            element: Selene Element для проверки.
            expected_text: Ожидаемый текст.

        Returns:
            bool: True, если текст совпадает.

        Raises:
            AssertionError: Если текст не совпадает (через Selene should).
        """
        with allure.step(f"✅ Проверяем текст: '{expected_text}'"):
            element.should(have.text(expected_text.strip()))

        return True

    # endregion

    # ========================================================================
    # region 4️⃣ 💾 LOCALSTORAGE\SESSIONSTORAGE
    # ========================================================================

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

    @allure.step("Очищаем данные пользователя из хранилищ")
    def clear_user_data(
        self,
        callsign: str | None = None,
        clear_registered_user: bool = False,
        clear_restored_user: bool = False,
        clear_current_user: bool = False,
    ):
        """
        Удаляет данные пользователя из localStorage и/или sessionStorage по флагам.
        Если все три флага False — очищает все хранилища (полная зачистка).

        Args:
            callsign: Позывной оператора для удаления (например, 'NOVA' или 'KNOPA').
                      Если None — полная очистка хранилища.
            clear_registered_user: Если True, удаляет оператора из localStorage['registeredUsers'].
            clear_restored_user: Если True, удаляет оператора из localStorage['restoredUsers'].
            clear_current_user: Если True, удаляет currentUser из sessionStorage.
        """
        # Если все флаги False — очищаем всё
        if not clear_registered_user and not clear_restored_user and not clear_current_user:
            clear_registered_user = True
            clear_restored_user = True
            clear_current_user = True

        try:
            if clear_registered_user:
                if callsign is None:
                    browser.driver.execute_script(
                        "localStorage.removeItem('registeredUsers');"
                    )
                else:
                    script = f"""
                        const users = JSON.parse(localStorage.getItem('registeredUsers') || '{{}}');
                        delete users['{callsign.upper()}'];
                        localStorage.setItem('registeredUsers', JSON.stringify(users));
                    """
                    browser.driver.execute_script(script)

            if clear_restored_user:
                if callsign is None:
                    browser.driver.execute_script(
                        "localStorage.removeItem('restoredUsers');"
                    )
                else:
                    script = f"""
                        const restored = JSON.parse(localStorage.getItem('restoredUsers') || '{{}}');
                        delete restored['{callsign.upper()}'];
                        localStorage.setItem('restoredUsers', JSON.stringify(restored));
                    """
                    browser.driver.execute_script(script)

            if clear_current_user:
                browser.driver.execute_script(
                    "sessionStorage.removeItem('currentUser');"
                )
        except Exception as e:
            raise AssertionError(
                "❌ Failed to clear user data!\n"
                f"   callsign: {callsign}\n"
                f"   clear_registered_user: {clear_registered_user}\n"
                f"   clear_restored_user: {clear_restored_user}\n"
                f"   clear_current_user: {clear_current_user}\n"
                f"   Error: {e}"
            ) from e
        return self

    @allure.step("Проверка наличия пользователя в хранилище по позывному")
    def verify_user_data_in_storage(
        self,
        expected_callsign: str,
        check_local: bool = False,
        check_session: bool = False,
    ):
        """
        Проверяет, что пользователь с указанным позывным сохранён в хранилищах.
        Позывные уникальны, поэтому проверки по callsign достаточно.

        Args:
            expected_callsign: Ожидаемый позывной (например, 'NOVA' или 'KNOPA').
            check_local: Флаг проверки localStorage (ищет в registeredUsers ИЛИ restoredUsers).
            check_session: Флаг проверки sessionStorage (currentUser).

        (Если оба флага False, метод проверит оба хранилища по умолчанию)
        """
        if not check_local and not check_session:
            check_local = True
            check_session = True

        callsign_upper = expected_callsign.upper()

        if check_local:
            with allure.step(f"Проверяем наличие '{callsign_upper}' в localStorage (registeredUsers или restoredUsers)"):
                
                registered_users_str = browser.driver.execute_script("return localStorage.getItem('registeredUsers');")
                registered_users = json.loads(registered_users_str) if registered_users_str else {}
             
                restored_users_str = browser.driver.execute_script("return localStorage.getItem('restoredUsers');")
                restored_users = json.loads(restored_users_str) if restored_users_str else {}

                is_in_registered = callsign_upper in registered_users
                is_in_restored = callsign_upper in restored_users

                assert is_in_registered or is_in_restored, (
                    f"❌ Позывной '{callsign_upper}' отсутствует как в 'registeredUsers', "
                    f"так и в 'restoredUsers'.\n"
                    f"Доступные ключи в registeredUsers: {list(registered_users.keys())}\n"
                    f"Доступные ключи в restoredUsers: {list(restored_users.keys())}"
                )
                
        if check_session:
            with allure.step(f"Проверяем currentUser в sessionStorage (callsign == '{callsign_upper}')"):
                current_user_str = browser.driver.execute_script("return sessionStorage.getItem('currentUser');")

                assert current_user_str is not None, "Ключ 'currentUser' отсутствует в sessionStorage"

                try:
                    current_user = json.loads(current_user_str)
                except json.JSONDecodeError:
                    raise AssertionError(f"Данные в 'currentUser' не являются валидным JSON: {current_user_str}")

                actual_callsign = current_user.get("callsign")
                assert actual_callsign.upper() == callsign_upper, (
                    f"❌ [sessionStorage] Ожидался callsign '{callsign_upper}', получено '{actual_callsign}'"
                )

        return self

    @allure.step("Проверка очистки данных пользователя из хранилища по позывному")
    def verify_storage_cleared(
        self,
        expected_callsign: str,
        check_local: bool = False,
        check_session: bool = False,
    ):
        """
        Проверяет, что данные конкретного пользователя удалены из хранилищ после logout.

        Args:
            expected_callsign: Позывной пользователя, который должен быть удалён (например, 'NOVA').
            check_local: Флаг проверки localStorage (registeredUsers).
            check_session: Флаг проверки sessionStorage (currentUser).

        (Если оба флага False, метод проверит оба хранилища по умолчанию)
        """
        if not check_local and not check_session:
            check_local = True
            check_session = True

        callsign_upper = expected_callsign.upper()

        # === Проверка localStorage: registeredUsers ===
        if check_local:
            with allure.step(
                f"Проверяем удаление '{callsign_upper}' из localStorage (registeredUsers)"
            ):
                registered_users_str = browser.driver.execute_script(
                    "return localStorage.getItem('registeredUsers');"
                )

                # Если ключа вообще нет (хранилище полностью очищено) — это успех
                if registered_users_str is not None:
                    try:
                        registered_users = json.loads(registered_users_str)
                        assert (
                            callsign_upper not in registered_users
                        ), f"Позывной '{callsign_upper}' всё ещё присутствует в registeredUsers после очистки"
                    except json.JSONDecodeError:
                        raise AssertionError(
                            f"Данные в 'registeredUsers' не являются валидным JSON: {registered_users_str}"
                        )

        # === Проверка sessionStorage: currentUser ===
        if check_session:
            with allure.step(
                f"Проверяем очистку currentUser в sessionStorage (пользователь '{callsign_upper}' не активен)"
            ):
                current_user_str = browser.driver.execute_script(
                    "return sessionStorage.getItem('currentUser');"
                )

                # Если ключа нет (сессия полностью убита) — это успех
                if current_user_str is not None:
                    try:
                        current_user = json.loads(current_user_str)
                        actual_callsign = current_user.get("callsign", "").upper()

                        assert (
                            actual_callsign != callsign_upper
                        ), f"[sessionStorage] Пользователь '{callsign_upper}' всё ещё числится в currentUser после logout"
                    except json.JSONDecodeError:
                        raise AssertionError(
                            f"Данные в 'currentUser' не являются валидным JSON: {current_user_str}"
                        )

        return self

    @allure.step("Полная очистка хранилищ браузера")
    def clear_all_storages(self):
        """
        Полностью очищает localStorage и sessionStorage браузера.
        Используется для обеспечения стерильности тестового окружения.
        """
        with allure.step("Выполняем очистку localStorage и sessionStorage"):
            try:
                browser.driver.execute_script("localStorage.clear(); sessionStorage.clear();")
                
            except Exception as e:
                raise AssertionError(
                    "❌ Failed to clear browser storages!\n"
                    f"   Error: {e}"
                ) from e
        return self

    
    # endregion

    # ========================================================================
    # region 5️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================

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

    @allure.step("Проверка очистки ключевых данных из sessionStorage после")
    def verify_session_storage_cleared(self):
        """
        Проверяет, что ключи currentUser отсутствуют в sessionStorage."""

        current_user = browser.driver.execute_script(
            "return localStorage.getItem('currentUser');"
        )

        assert current_user is None, (
            f"❌ Ключ 'currentUser' не очищен после logout!\n"
            f"   Ожидалось: None\n"
            f"   Получено: {current_user}"
        )

        return self

    @allure.step("Проверяем состояние кнопки")
    def verify_button_state(self, element, is_disabled: bool = True):
        """
        Проверяет состояние кнопки (активна или неактивна).

        Args:
            element: Элемент кнопки (button) для проверки.А
            is_disabled: Ожидаемое состояние. True - неактивна (disabled), False - активна (enabled).
        """
        try:
            if is_disabled:
                element.should(be.disabled)
            else:
                element.should(be.enabled)
        except TimeoutException:
            expected_state = "DISABLED" if is_disabled else "ENABLED"
            actual_state = (
                "DISABLED" if element.get_attribute("disabled") else "ENABLED"
            )

            raise AssertionError(
                f"❌ Button state mismatch!\n"
                f"   Expected state: {expected_state}\n"
                f"   Actual state: {actual_state}\n"
                f"   Element: {element}"
            )

        return self

    @allure.step("Очистка поля ввода по имени атрибута")
    def clear_field(self, field_attr_name: str):
        """
        Универсальный метод для очистки любого поля.
        """
        try:
            element = getattr(self, field_attr_name)
        except AttributeError:
            raise AssertionError(
                f"❌ Ошибка: у страницы {type(self).__name__} нет атрибута '{field_attr_name}'!\n"
                f"   Проверь, правильно ли указано имя локатора в Page Object."
            )

        element.clear()
        
        return self

    
    @allure.step("Проверяем состояние поля: пустое и (только для чтения / редактируемое)")
    def verify_empty_field_state(self, element, is_readonly: bool = True):
        """
        Проверяет, что поле ввода пустое и имеет (или не имеет) атрибут readonly.

        Args:
            element: Элемент поля ввода (input) для проверки.
            is_readonly: Если True — проверяет наличие атрибута readonly (заблокировано).
                         Если False — проверяет отсутствие атрибута readonly (доступно для ввода).
        """
        # 1. Проверка на пустоту
        try:
            element.should(have.value(""))
        except TimeoutException:
            raise AssertionError(
                "❌ Field is not empty!\n"
                f"   Expected value: ''\n"
                f"   Actual value: '{element.get_attribute('value')}'\n"
                "   Condition: Field must be empty"
            )

                # 2. Проверка на readonly
        state_desc = "readonly (заблокировано)" if is_readonly else "editable (доступно для ввода)"
        
        try:
            if is_readonly:
                element.should(have.attribute("readonly"))
            else:
                element.should(have.no.attribute("readonly"))  # ✅ Вот правильный синтаксис Selenide!
        except TimeoutException:
            actual_readonly_val = element.get_attribute("readonly")
            raise AssertionError(
                f"❌ Field is not {state_desc}!\n"
                f"   Expected: attribute 'readonly' to be {'present' if is_readonly else 'absent'}\n"
                f"   Actual readonly attribute value: '{actual_readonly_val}'\n"
                "   Condition: Field readonly state mismatch"
            )

    @allure.step("Проверяем значение поля ввода (input)")
    def verify_input_value(self, element, expected_value: str):
        """
        Проверяет, что поле ввода содержит ожидаемое значение.
        Использует have.value() для корректной проверки тегов <input>.

        Args:
            element: Элемент поля ввода (input) для проверки.
            expected_value: Ожидаемое значение поля.
        """
        try:
            element.should(have.value(expected_value))
        except TimeoutException:
            raise AssertionError(
                "❌ Input value mismatch!\n"
                f"   Expected value: '{expected_value}'\n"
                f"   Actual value: '{element.get_attribute('value')}'\n"
                "   Condition: Input field must contain the exact value"
            )
        return self

    @allure.step("Проверка содержимого кнопки навигации")
    def check_button_content(self, button_id: str, expected_text: str):
        """Проверяет наличие и текстовое содержимое кнопки навигации."""
        with allure.step(f"Проверяем кнопку {button_id}"):
            try:
                btn = browser.element(f'[data-wm-id="{button_id}"]')
                btn.should(be.visible).should(be.enabled)
            
                # Проверяем текст внутри кнопки
                btn.element('.btn-label').should(have.exact_text(expected_text))

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

    @allure.step("Проверяем значение поля")
    def verify_field_value(self, element, expected_value: str):
        """Проверяет, что в поле осталось только ожидаемое значение."""
        try:
            element.should(have.value(expected_value))
        except TimeoutException:
            actual_value = element.get_attribute("value")
            raise AssertionError(
                "❌ Значение поля не совпадает!\n"
                f"   Expected: '{expected_value}'\n"
                f"   Actual: '{actual_value}'"
            )
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

    @allure.step("Проверка появления контейнера ошибки")
    def should_show_error_container(self, element: Element, expected_text: str):
        """Проверяет, что контейнер ошибки отображается и содержит верный текст.

        Args:
            element: Selene-элемент (контейнер ошибки)
            expected_text: точный текст для проверки
        """
        with allure.step(f"Ожидаемый текст ошибки: '{expected_text}'"):
            try:
                element.should(be.visible).should(have.text(expected_text))
            except TimeoutException:
                raise AssertionError(
                    "❌ Контейнер ошибки не отображается или текст не совпадает!\n"
                    f"   Expected text: '{expected_text}'\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking error container!\n"
                    f"   Expected text: '{expected_text}'\n"
                    f"   Error: {e}"
                ) from e
        return self
    
    
    # endregion
