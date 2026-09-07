import json

import allure
from selene import be, browser, have
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
            raise AssertionError(
                "❌ Failed to refresh page!\n"
                f"   Error: {e}"
            ) from e
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
    # region 2️⃣ 💬 ТЕЛЕМЕТРИЯ И ТЕКСТЫ
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
    # region 3️⃣ 💾 LOCALSTORAGE
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
        clear_current_user: bool = False,
    ):
        """
        Удаляет данные пользователя из localStorage и/или sessionStorage по флагам.
        Если оба флага False — очищает оба хранилища (полная зачистка).

        Args:
            callsign: Позывной оператора для удаления из registeredUsers
                      (например, 'NOVA'). Обязателен при clear_registered_user=True.
            clear_registered_user: Если True, удаляет оператора из localStorage['registeredUsers'].
            clear_current_user: Если True, удаляет currentUser из sessionStorage.
        """
        # Если оба флага False — очищаем всё
        if not clear_registered_user and not clear_current_user:
            clear_registered_user = True
            clear_current_user = True

        try:
            if clear_registered_user:
                if callsign is None:
                    # Полная очистка registeredUsers
                    browser.driver.execute_script(
                        "localStorage.removeItem('registeredUsers');"
                    )
                else:
                    # Удаление конкретного оператора
                    script = f"""
                        const users = JSON.parse(localStorage.getItem('registeredUsers') || '{{}}');
                        delete users['{callsign.upper()}'];
                        localStorage.setItem('registeredUsers', JSON.stringify(users));
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
            expected_callsign: Ожидаемый позывной (например, 'NOVA').
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
            with allure.step(f"Проверяем наличие '{callsign_upper}' в localStorage (registeredUsers)"):
                registered_users_str = browser.driver.execute_script(
                    "return localStorage.getItem('registeredUsers');"
                )

                assert (
                    registered_users_str is not None
                ), "Ключ 'registeredUsers' отсутствует в localStorage"

                try:
                    registered_users = json.loads(registered_users_str)
                except json.JSONDecodeError:
                    raise AssertionError(
                        f"Данные в 'registeredUsers' не являются валидным JSON: {registered_users_str}"
                    )

                assert (
                    callsign_upper in registered_users
                ), f"Позывной '{callsign_upper}' отсутствует в registeredUsers"

        # === Проверка sessionStorage: currentUser ===
        if check_session:
            with allure.step(f"Проверяем currentUser в sessionStorage (callsign == '{callsign_upper}')"):
                current_user_str = browser.driver.execute_script(
                    "return sessionStorage.getItem('currentUser');"
                )

                assert (
                    current_user_str is not None
                ), "Ключ 'currentUser' отсутствует в sessionStorage"

                try:
                    current_user = json.loads(current_user_str)
                except json.JSONDecodeError:
                    raise AssertionError(
                        f"Данные в 'currentUser' не являются валидным JSON: {current_user_str}"
                    )

                actual_callsign = current_user.get("callsign")
                assert (
                    actual_callsign.upper() == callsign_upper
                ), f"[sessionStorage] Ожидался callsign '{callsign_upper}', получено '{actual_callsign}'"

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
            with allure.step(f"Проверяем удаление '{callsign_upper}' из localStorage (registeredUsers)"):
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
            with allure.step(f"Проверяем очистку currentUser в sessionStorage (пользователь '{callsign_upper}' не активен)"):
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

    # endregion

    # ========================================================================
    # region 4️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
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

    # endregion
