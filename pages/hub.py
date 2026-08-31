import json

import allure
from selene import be, browser, have
from selene.core.entity import Element
from selenium.common.exceptions import TimeoutException
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

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

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

    @allure.step("Переход в Galaxy Map")
    def navigate_to_galaxy_map(self):
        """
        Кликает по кнопке 'Galaxy Map', проверяет URL и возвращается на Dashboard.
        """
        self.galaxy_map_btn.click()
        self.verify_current_url("galaxy-map.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        browser.element(".back-btn").click()
        self.verify_current_url("dashboard.html")

        return self

    @allure.step("Переход в CIS Table")
    def navigate_to_cis_table(self):
        """
        Кликает по кнопке 'CIS Table', проверяет URL и возвращается на Dashboard.
        """
        self.cis_table_btn.click()
        self.verify_current_url("cis-table.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        browser.element(".back-btn").click()
        self.verify_current_url("dashboard.html")

        return self

    @allure.step("Переход в Mission Control")
    def navigate_to_mission_control(self):
        """
        Кликает по кнопке 'Mission Control', проверяет URL и возвращается на Dashboard.
        """
        self.mission_control_btn.click()
        self.verify_current_url("mission-control.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        browser.element(".back-btn").click()
        self.verify_current_url("dashboard.html")

        return self

    @allure.step("Переход в Settings")
    def navigate_to_settings(self):
        """
        Кликает по кнопке 'Settings', проверяет URL и возвращается на Dashboard.
        """
        self.nav_settings_btn.click()
        self.verify_current_url("settings.html")

        # Временно: клик по заглушке "Back to Dashboard" для возврата
        browser.element(".back-btn").click()
        self.verify_current_url("dashboard.html")

        return self

    # endregion

    # ========================================================================
    # region 2️⃣ 💬 ТЕЛЕМЕТРИЯ
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

    # endregion

    # ========================================================================
    # region 3️⃣ 💾 LOCALSTORAGE
    # ========================================================================

    @allure.step("Установка повреждённых данных в localStorage")
    def set_corrupted_user_data(self):
        """
        Записывает невалидный JSON в localStorage под ключом 'currentUser'.

        Используется для тестирования graceful degradation системы
        (например, проверка редиректа при повреждённых данных).
        """
        with allure.step("Записываем 'broken' в localStorage.currentUser"):
            try:
                browser.driver.execute_script(
                    "localStorage.setItem('currentUser', 'broken');"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Failed to set corrupted user data!\n" f"   Error: {e}"
                ) from e

        return self

    @allure.step("Проверка очистки ключей currentUser и dashboardInitialized")
    def verify_currentuser_dashboard_keys_cleared(self):
        """
        Проверяет, что ключи 'currentUser' и 'dashboardInitialized'
        были удалены из localStorage.
        """
        with allure.step("Проверяем отсутствие ключей в localStorage"):
            try:
                actual_values = browser.driver.execute_script("""
                    return {
                        currentUser: localStorage.getItem('currentUser'),
                        dashboardInitialized: localStorage.getItem('dashboardInitialized')
                    };
                """)

                errors = []

                if actual_values.get("currentUser") is not None:
                    errors.append(
                        f"   currentUser: expected None, got '{actual_values['currentUser']}'"
                    )

                if actual_values.get("dashboardInitialized") is not None:
                    errors.append(
                        f"   dashboardInitialized: expected None, got '{actual_values['dashboardInitialized']}'"
                    )

                if errors:
                    raise AssertionError(
                        "❌ localStorage keys were NOT fully cleared!\n"
                        + "\n".join(errors)
                    )

            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking localStorage!\n   Error: {e}"
                ) from e

        return self

    @allure.step("Проверка корректности данных пользователя в localStorage")
    def verify_local_storage_user_data(
        self, expected_callsign: str, expected_role: str
    ):
        """
        Проверяет, что в localStorage сохранены корректные позывной (callsign)
        и роль (role) пользователя.
        """
        user_data_str = browser.driver.execute_script(
            "return localStorage.getItem('currentUser');"
        )

        assert (
            user_data_str is not None
        ), "Ключ 'currentUser' отсутствует в localStorage"

        try:
            user_data = json.loads(user_data_str)
        except json.JSONDecodeError:
            raise AssertionError(
                f"Данные в 'currentUser' не являются валидным JSON: {user_data_str}"
            )

        actual_callsign = user_data.get("callsign")
        actual_role = user_data.get("role")

        assert (
            actual_callsign.upper() == expected_callsign.upper()
        ), f"Ожидался callsign '{expected_callsign}', получено '{actual_callsign}'"
        assert (
            actual_role.lower() == expected_role.lower()
        ), f"Ожидалась роль '{expected_role}', получено '{actual_role}'"

        return self

    @allure.step("Проверка очистки ключевых данных из localStorage после logout")
    def verify_local_storage_cleared(self):
        """
        Проверяет, что ключи currentUser и dashboardInitialized
        отсутствуют в localStorage после выхода из системы.
        """
        current_user = browser.driver.execute_script(
            "return localStorage.getItem('currentUser');"
        )
        dashboard_init = browser.driver.execute_script(
            "return localStorage.getItem('dashboardInitialized');"
        )

        assert current_user is None, (
            f"❌ Ключ 'currentUser' не очищен после logout!\n"
            f"   Ожидалось: None\n"
            f"   Получено: {current_user}"
        )
        assert dashboard_init is None, (
            f"❌ Ключ 'dashboardInitialized' не очищен после logout!\n"
            f"   Ожидалось: None\n"
            f"   Получено: {dashboard_init}"
        )

        return self

    # endregion
