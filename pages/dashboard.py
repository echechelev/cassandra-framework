import re
import time

import allure
from selene import be, browser, have
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    JavascriptException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver import ActionChains

from pages.hub import HubPage


class DashboardPage(HubPage):

    # URL
    PATH = "/dashboard.html"

    # Информационные панели
    role_tooltip = browser.element('[data-wm-id="info-panel-role"] .info-tooltip')
    role_panel = browser.element('[data-wm-id="info-panel-role"]')
    role_icon = browser.element('[data-wm-id="role-icon"]')
    role_label = browser.element('[data-wm-id="role-label"]')
    user_tooltip = browser.element('[data-wm-id="info-panel-user"] .info-tooltip')
    user_panel = browser.element('[data-wm-id="info-panel-user"]')
    user_icon = browser.element('[data-wm-id="user-icon"]')
    user_label = browser.element('[data-wm-id="user-label"]')
    user_status = browser.element('[data-wm-id="status-dot"]')

    # Нижние кнопки
    start_diagnostics_btn = browser.element('[data-wm-id="start-diagnostics-btn"]')
    logout_btn = browser.element('[data-wm-id="logout-btn"]')

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌐 Открытие страницы Dashboard")
    def open(self):
        """Открывает страницу Dashboard и проверяет её загрузку."""
        with allure.step(f"Открываем страницу: {self.PATH}"):
            try:
                browser.open(self.PATH)
                self.start_diagnostics_btn.should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Dashboard page did not load!\n"
                    f"   Expected URL: {self.PATH}\n"
                    f"   Actual URL: {browser.driver.current_url}\n"
                    "   Timeout: start_diagnostics_btn did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening dashboard!\n"
                    f"   Path: {self.PATH}\n"
                    f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 2️⃣ 📡 UPLINK (Анимация загрузки)
    # ========================================================================

    def verify_progress_bar_appeared_once(self):
        """Проверяет, что прогресс-бар появился и он ровно один (нет дубликатов от спама)."""
        self.progress_container.should(be.visible)

        assert (
            len(self.progress_bars) == 1
        ), f"Ожидался 1 прогресс-бар, найдено: {len(self.progress_bars)}"

        return self

    @allure.step("Нажатие кнопки Uplink")
    def click_uplink(self):
        """Нажимает кнопку инициализации системы Uplink."""
        with allure.step("Кликаем по кнопке Uplink"):
            try:
                self.start_diagnostics_btn.should(be.visible).should(be.enabled)
                self.start_diagnostics_btn.click()

            except TimeoutException:
                raise AssertionError(
                    "❌ Uplink button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Uplink!\n" f"   Error: {e}"
                ) from e
        return self

    @allure.step("Ожидание полной активации Uplink")
    def wait_for_uplink_complete(self, callsign: str, timeout: int = 40):
        """
        Ждёт полной активации Uplink:
        1. Ожидает появления "SYSTEM READY" в телеметрии
        2. Проверяет полный текст телеметрии с позывным
        3. Ожидает активации Galaxy Map (маяк полной готовности)

        Args:
            callsign: Позывной пользователя (для проверки полного текста)
            timeout: Максимальное время ожидания в секундах (по умолчанию 40 сек)

        Returns:
            self: Экземпляр DashboardPage для chaining-а методов.
        """
        expected_full_text = (
            f"> CASSANDRA: {callsign}, SYSTEM READY FOR WORK. AWAITING COMMANDS."
        )

        with allure.step(f"Ожидаем 'SYSTEM READY' в телеметрии (timeout: {timeout}s)"):
            try:
                self.system_telemetry.with_(timeout=timeout).should(
                    have.text("SYSTEM READY")
                )
            except TimeoutException:
                raise AssertionError(
                    "❌ System did not load in time!\n"
                    f"   Timeout: {timeout}s\n"
                    "   Expected: telemetry contains 'SYSTEM READY'"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while waiting for system ready!\n"
                    f"   Error: {e}"
                ) from e

        with allure.step("Проверяем полный текст телеметрии"):
            self.verify_telemetry_text(expected_full_text)

        with allure.step("Ожидаем активации Galaxy Map (маяк полной готовности)"):
            try:
                self.galaxy_map_btn.with_(timeout=timeout).should(
                    have.css_class("panel-online")
                )
            except TimeoutException:
                raise AssertionError(
                    "❌ Uplink activation timeout!\n"
                    f"   Galaxy Map did not become 'panel-online' within {timeout}s\n"
                    "   Expected: class 'panel-online' on Galaxy Map button"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while waiting for Uplink completion!\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("Проверка, что кнопка Uplink стала неактивной")
    def verify_uplink_button_disabled(self):
        """
        Проверяет, что после завершения загрузки кнопка Uplink:
        1. Потеряла пульсацию (класс uplink-active удалён).
        2. Приобрела класс uplink-inactive.
        3. Стала некликабельной (pointer-events: none).
        4. Стала полупрозрачной (opacity: 0.5).
        """
        with allure.step("Проверяем состояние кнопки Uplink"):
            try:
                self.start_diagnostics_btn.should(have.no.css_class("uplink-active"))
                self.start_diagnostics_btn.should(have.css_class("uplink-inactive"))

                script = """
                    const btn = document.querySelector('[data-wm-id="start-diagnostics-btn"]');
                    const style = window.getComputedStyle(btn);
                    return {
                        pointerEvents: style.pointerEvents,
                        opacity: style.opacity
                    };
                """
                actual_state = browser.driver.execute_script(script)

                errors = []
                if actual_state["pointerEvents"] != "none":
                    errors.append(
                        f"   pointer-events: expected 'none', "
                        f"got '{actual_state['pointerEvents']}'"
                    )
                if actual_state["opacity"] != "0.5":
                    errors.append(
                        f"   opacity: expected '0.5', "
                        f"got '{actual_state['opacity']}'"
                    )

                if errors:
                    raise AssertionError(
                        "❌ Uplink button state does not match!\n" + "\n".join(errors)
                    )

            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking Uplink button state!\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("Проверка активации кнопок после Uplink")
    def verify_uplink_buttons_activated(self):
        """
        Проверяет, что после полной активации Uplink:
        - Role Panel и User Panel (верхние информационные панели)
        - Кнопка Disconnect
        - 5 центральных кнопок (планет)

        Приобрели состояние panel-online:
        - Класс 'panel-online' добавлен
        - Кликабельны (pointer-events: auto)
        - Имеют hover-эффект (cursor: pointer)
        """
        with allure.step(
            "Проверяем 8 элементов (2 панели + 6 кнопок) на состояние panel-online"
        ):
            try:
                buttons = [
                    ("Role Panel", self.role_panel),
                    ("User Panel", self.user_panel),
                    ("Disconnect", self.logout_btn),
                    ("Galaxy Map", self.galaxy_map_btn),
                    ("Flight Calc", self.flight_calc_btn),
                    ("CIS Table", self.cis_table_btn),
                    ("Mission Control", self.mission_control_btn),
                    ("Cassandra Settings", self.nav_settings_btn),
                ]

                errors = []

                for btn_name, btn_element in buttons:
                    # Проверяем наличие класса panel-online
                    try:
                        btn_element.should(have.css_class("panel-online"))
                    except TimeoutException:
                        errors.append(f"   {btn_name}: class 'panel-online' not found")
                        continue

                    # Проверяем pointer-events и cursor через JS
                    script = """
                        const btn = arguments[0];
                        const style = window.getComputedStyle(btn);
                        return {
                            pointerEvents: style.pointerEvents,
                            cursor: style.cursor
                        };
                    """
                    actual_state = browser.driver.execute_script(script, btn_element())

                    if actual_state["pointerEvents"] != "auto":
                        errors.append(
                            f"   {btn_name}: pointer-events expected 'auto', "
                            f"got '{actual_state['pointerEvents']}'"
                        )
                    if actual_state["cursor"] != "pointer":
                        errors.append(
                            f"   {btn_name}: cursor expected 'pointer', "
                            f"got '{actual_state['cursor']}'"
                        )

                if errors:
                    raise AssertionError(
                        "❌ Uplink buttons activation failed!\n" + "\n".join(errors)
                    )

            except AssertionError:
                raise
            except (WebDriverException, JavascriptException) as e:
                raise AssertionError(
                    f"❌ Browser error while checking Uplink buttons!\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("Проверка неактивности кнопок Planet Bar в состоянии panel-offline")
    def verify_planet_bar_buttons_inactive(
        self, expected_url: str = "/dashboard.html", timeout_per_button: int = 30
    ):
        """
        Проверяет, что все 5 кнопок Planet Bar неактивны до полной активации Uplink:
        1. Для каждой кнопки: ждём появления → кликаем → проверяем URL
        2. После всех кликов проверяем pointer-events: none для всех

        Args:
            expected_url: Ожидаемый URL (по умолчанию /dashboard.html)
            timeout_per_button: Максимальное время ожидания появления каждой кнопки
        """
        planet_bar_buttons = [
            ("Galaxy Map", self.galaxy_map_btn, "nav-galaxy-map"),
            ("Flight Calc", self.flight_calc_btn, "flight-calc-btn"),
            ("CIS Table", self.cis_table_btn, "cis-table-btn"),
            ("Mission Control", self.mission_control_btn, "mission-control-btn"),
            ("Nav Settings", self.nav_settings_btn, "nav-settings"),
        ]

        for btn_name, btn_element, btn_id in planet_bar_buttons:
            with allure.step(f"Проверяем кнопку {btn_name}"):
                btn_element.with_(timeout=timeout_per_button).should(be.visible)

                try:
                    native_btn = browser.driver.find_element(
                        "css selector", f'[data-wm-id="{btn_id}"]'
                    )
                    native_btn.click()
                except (
                    ElementClickInterceptedException,
                    ElementNotInteractableException,
                ):
                    pass

                current_url = browser.driver.current_url
                if expected_url not in current_url:
                    raise AssertionError(
                        f"❌ URL changed after clicking {btn_name}!\n"
                        f"   Expected URL containing: {expected_url}\n"
                        f"   Current: {current_url}\n"
                        f"   Button ID: {btn_id}"
                    )

        with allure.step("Проверяем pointer-events: none для всех кнопок Planet Bar"):
            script = """
                const selectors = [
                    '[data-wm-id="nav-galaxy-map"]',
                    '[data-wm-id="flight-calc-btn"]',
                    '[data-wm-id="cis-table-btn"]',
                    '[data-wm-id="mission-control-btn"]',
                    '[data-wm-id="nav-settings"]'
                ];
                return selectors.map(sel => {
                    const btn = document.querySelector(sel);
                    return {
                        id: btn.getAttribute('data-wm-id'),
                        pointerEvents: window.getComputedStyle(btn).pointerEvents
                    };
                });
            """
            button_states = browser.driver.execute_script(script)

            errors = []
            for state in button_states:
                if state["pointerEvents"] != "none":
                    errors.append(
                        f"   {state['id']}: expected 'none', got '{state['pointerEvents']}'"
                    )

            if errors:
                raise AssertionError(
                    "❌ Planet Bar buttons are not inactive!\n" + "\n".join(errors)
                )

        return self

    @allure.step("Валидация анимации и значений прогресс-бара")
    def verify_progress_bar_animation(self, timeout: int = 30):
        """
        Проверяет, что прогресс-бар заполняется монотонно:
        1. Собираем все значения ширины в цикле
        2. Проверяем синхронизацию ширины и текста
        3. Проверяем, что каждое следующее значение >= предыдущего
        4. Проверяем, что в конце контейнер прогресс-бара исчезает
        """
        progress_fill = self.progress_fill
        progress_text = self.progress_text

        width_values = []

        with allure.step("Собираем значения ширины прогресс-bar"):
            start_time = time.time()

            while time.time() - start_time < timeout:
                width_style = browser.driver.execute_script(
                    "return arguments[0].style.width;", progress_fill()
                )

                if width_style:
                    width_percent = int(width_style.replace("%", "").strip())
                    width_values.append(width_percent)

                    progress_text.should(be.visible)
                    text_content = progress_text().get_attribute("textContent")

                    if not text_content:
                        raise AssertionError(
                            "❌ Текст прогресс-бара пустой или не найден!"
                        )

                    match = re.search(r"\d+", text_content)
                    if not match:
                        raise AssertionError(
                            f"❌ Не удалось найти проценты в тексте: '{text_content}'"
                        )

                    text_percent = int(match.group())

                    if text_percent != width_percent:
                        raise AssertionError(
                            f"❌ Текст и ширина не синхронизированы!\n"
                            f"   Ширина: {width_percent}%, Текст: {text_percent}%"
                        )

                    if width_percent >= 100:
                        break

                time.sleep(0.5)

        with allure.step("Проверяем монотонное возрастание значений"):
            for i in range(1, len(width_values)):
                if width_values[i] < width_values[i - 1]:
                    raise AssertionError(
                        f"❌ Прогресс-бар не монотонен!\n"
                        f"   Значение {width_values[i-1]}% изменилось на {width_values[i]}%\n"
                        f"   Все значения: {width_values}"
                    )

        with allure.step("Проверяем исчезновение контейнера прогресс-бара после 100%"):

            self.progress_container.should(be.not_.visible)

        return self

    @allure.step("Выполняем 3 клика по кнопке 'Uplink'")
    def spam_click_diagnostics(self, times=3):
        """
        Выполняет серию быстрых нативных кликов по кнопке Start Diagnostics.

        Использует прямой доступ к Selenium WebDriver, чтобы избежать
        проблем с повторным поиском элемента в Selene 2.x.
        Ошибки клика по неактивному элементу игнорируются.

        Args:
            times (int): Количество попыток клика. По умолчанию 3.

        Returns:
            self: Экземпляр страницы для цепочки вызовов.
        """

        self.start_diagnostics_btn.should(be.visible)

        native_btn = browser.driver.find_element(
            "css selector", '[data-wm-id="start-diagnostics-btn"]'
        )

        for _ in range(times):
            try:
                native_btn.click()
            except (ElementClickInterceptedException, ElementNotInteractableException):
                pass

        return self

    @allure.step("Проверка неактивности кнопки Logout до полной активации")
    def verify_logout_button_inactive(
        self, expected_url: str = "/dashboard.html", timeout: int = 30
    ):
        """
        Проверяет, что кнопка Logout неактивна до полной активации Uplink:
        1. Ждём появления кнопки Logout
        2. Пытаемся кликнуть (нативный Selenium)
        3. Проверяем URL не изменился
        4. Проверяем pointer-events: none

        Args:
            expected_url: Ожидаемый URL (по умолчанию /dashboard.html)
            timeout: Максимальное время ожидания появления кнопки
        """
        with allure.step("Ждём появления кнопки Logout"):
            self.logout_btn.with_(timeout=timeout).should(be.visible)

        with allure.step("Пытаемся кликнуть на неактивную кнопку Logout"):
            try:
                native_btn = browser.driver.find_element(
                    "css selector", '[data-wm-id="logout-btn"]'
                )
                native_btn.click()
            except (ElementClickInterceptedException, ElementNotInteractableException):
                pass

        with allure.step("Проверяем, что URL не изменился"):
            current_url = browser.driver.current_url
            if expected_url not in current_url:
                raise AssertionError(
                    f"❌ URL changed after clicking Logout!\n"
                    f"   Expected URL containing: {expected_url}\n"
                    f"   Current: {current_url}"
                )

        with allure.step("Проверяем pointer-events: none для кнопки Logout"):
            script = """
                const btn = document.querySelector('[data-wm-id="logout-btn"]');
                return window.getComputedStyle(btn).pointerEvents;
            """
            pointer_events = browser.driver.execute_script(script)

            if pointer_events != "none":
                raise AssertionError(
                    f"❌ Logout button pointer-events is not 'none'!\n"
                    f"   Expected: none\n"
                    f"   Actual: {pointer_events}"
                )

        return self

    # endregion

    # ========================================================================
    # region 3️⃣ 👤 ИНФОРМАЦИОННЫЕ ПАНЕЛИ
    # ========================================================================

    @allure.step("Проверка данных в информационных панелях")
    def verify_panels_data(self, expected_role: str, expected_user: str):
        """
        Проверяет корректность данных в Role Panel и User Panel.

        Args:
            expected_role: Ожидаемая роль (например, "SPECIALIST")
            expected_user: Ожидаемый позывной (например, "AURORA")

        Returns:
            self: Экземпляр DashboardPage для chaining-а методов.

        Raises:
            AssertionError: Если текст в панелях не совпадает с ожидаемым.
        """
        with allure.step(
            f"Проверка данных панелей (Роль: {expected_role}, Юзер: {expected_user})"
        ):
            try:
                self.role_label.should(have.exact_text(expected_role))
                self.user_label.should(have.exact_text(expected_user))

            except TimeoutException:
                raise AssertionError(
                    "❌ Panel data verification failed!\n"
                    f"   Expected Role: {expected_role}\n"
                    f"   Expected User: {expected_user}\n"
                    "   Timeout: element text did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while verifying panels data!\n"
                    f"   Expected Role: {expected_role}\n"
                    f"   Expected User: {expected_user}\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step(
        "Проверка состояния панелей: panel-offline, некликабельны, тултипы скрыты"
    )
    def verify_panels_are_offline(self):
        """
        Комплексная проверка состояния панелей до нажатия Uplink:
        1. Присутствует класс 'panel-offline'
        2. Панели не кликабельны (pointer-events: none)
        3. Тултипы скрыты (display: none)
        """
        with allure.step("Проверка Role Panel (оффлайн, некликабельна, тултип скрыт)"):
            self.role_panel.should(have.css_class("panel-offline"))
            self.role_panel.should(have.css_property("pointer-events", "none"))
            self.role_tooltip.should(have.css_property("display", "none"))

        with allure.step("Проверка User Panel (оффлайн, некликабельна, тултип скрыт)"):
            self.user_panel.should(have.css_class("panel-offline"))
            self.user_panel.should(have.css_property("pointer-events", "none"))
            self.user_tooltip.should(have.css_property("display", "none"))

        return self

    @allure.step("Проверка динамических данных в тултипах (Level и ID)")
    def verify_tooltips_dynamic_data(self, user_data: dict):
        """
        Проверяет подстановку данных в тултипы:
        - Role Panel: 'Access: Level X'
        - User Panel: 'ID: Y'

        Args:
            user_data: Словарь с данными пользователя из data.py.
        """
        expected_level = user_data["access_level"]
        expected_id = user_data["id"]

        with allure.step(
            f"Проверяем тултип Role Panel (Access: Level {expected_level})"
        ):
            self.role_panel.hover()
            self.role_tooltip.should(be.visible)
            self.role_tooltip.should(have.text(f"Access: Level {expected_level}"))

        with allure.step(f"Проверяем тултип User Panel (ID: {expected_id})"):
            self.user_panel.hover()
            self.user_tooltip.should(be.visible)
            self.user_tooltip.should(have.text(f"ID: {expected_id}"))

        browser.element("body").click()

        return self

    # endregion

    # ========================================================================
    # region 4️⃣ БЕЗОПАСНОСТЬ И СЕССИЯ
    # ========================================================================

    @allure.step("Нажатие кнопки Logout")
    def click_logout(self):
        """Нажимает кнопку выхода из системы (Disconnect/Logout)."""
        with allure.step("Кликаем по кнопке Logout"):
            try:
                self.logout_btn.should(be.visible).should(be.enabled)
                self.logout_btn.click()

            except TimeoutException:
                raise AssertionError(
                    "❌ Logout button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Logout!\n" f"   Error: {e}"
                ) from e
        return self

    @allure.step("Проверка отказа доступа и редиректа")
    def verify_access_denied_and_redirect(
        self, expected_url_part: str = "login.html", timeout: float = 3.0
    ):
        """
        Проверяет сценарий отказа доступа:
        1. Телеметрия показывает '> ACCESS DENIED. REDIRECTING...'
        2. Через ~1.5 сек происходит редирект на страницу логина.

        Args:
            expected_url_part: Часть URL, которую ожидаем после редиректа.
            timeout: Максимальное время ожидания редиректа в секундах.
        """
        self.verify_telemetry_text("> ACCESS DENIED. REDIRECTING...")

        with allure.step(f"Ожидаем редирект на '{expected_url_part}'"):
            try:
                browser.should(have.url_containing(expected_url_part), timeout=timeout)  # type: ignore
            except TimeoutException:
                raise AssertionError(
                    f"❌ Redirect failed!\n"
                    f"   Expected URL containing: '{expected_url_part}'\n"
                    f"   Timeout: {timeout}s"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking redirect!\n" f"   Error: {e}"
                ) from e

        return self

    @allure.step("Проверка редиректа на страницу логина")
    def verify_redirect_to_login(self):
        """
        Проверяет, что произошел редирект на страницу логина.
        Использует глобальный таймаут Selene (по умолчанию 4 сек).
        """
        with allure.step("Ожидаем редирект на login.html"):
            try:
                browser.should(have.url_containing("login.html"))
            except TimeoutException:
                raise AssertionError(
                    "❌ Redirect to Login Page failed!\n"
                    "   Expected: URL containing 'login.html'"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking redirect!\n" f"   Error: {e}"
                ) from e

        return self

    @allure.step("Проверка hover-эффекта кнопки Logout")
    def verify_logout_button_hover_effect(self):
        """
        Проверяет, что при наведении курсора на активную кнопку Logout:
        1. Кнопка увеличивается.
        2. Курсор меняется на pointer.
        """
        with allure.step("Проверяем, что кнопка активна (panel-online)"):
            self.logout_btn.should(have.css_class("panel-online"))

        with allure.step("Наводим курсор и проверяем эффекты"):
            try:
                logout_element = self.logout_btn()

                actions = ActionChains(browser.driver)
                actions.move_to_element(logout_element).perform()
                time.sleep(0.5)

                script = """
                    const btn = document.querySelector('[data-wm-id="logout-btn"]');
                    const style = window.getComputedStyle(btn);
                    return {
                        transform: style.transform,
                        cursor: style.cursor
                    };
                """
                hover_state = browser.driver.execute_script(script)

                errors = []

                if not hover_state["transform"] or hover_state["transform"] == "none":
                    errors.append("   transform: button did not scale up")

                if hover_state["cursor"] != "pointer":
                    errors.append(
                        f"   cursor: expected 'pointer', got '{hover_state['cursor']}'"
                    )

                if errors:
                    raise AssertionError(
                        "❌ Logout button hover effect does not match!\n"
                        + "\n".join(errors)
                    )

            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking hover effect!\n   Error: {e}"
                ) from e

        return self
