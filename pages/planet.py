import allure
from selene import be, browser, have
from selenium.common.exceptions import (
    TimeoutException,
)

from pages.core import CorePage


class PlanetPage(CorePage):

    # Имя планеты
    planet_name_element = browser.element(".planet-name")

    # Левая панель (Технические данные)
    tech_panel = browser.element('[data-wm-id="tech-panel"]')
    mass_planet = browser.element('[data-wm-id="tech-mass"]')

    # Правая панель (Профиль планты/Статусс разведки)
    info_description = browser.element('[data-wm-id="info-description"]')
    mission_status = browser.element('[data-wm-id="mission-status-text"]')

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌟 Открытие страницы Star Info")
    def open(self, url_path: str, expect_redirect: bool = False) -> "PlanetPage":
        """
        Открывает страницу Planet через переданный URL.

        Args:
            url_path: Путь к странице (например, из data.PLANET_URL_SUN).
            expect_redirect: Если True, не ждет отрисовки tech-panel
                             (используется для тестов редиректа).
        """
        with allure.step(f"Переход по адресу: {url_path}"):
            browser.open(url_path)

        if not expect_redirect:
            with allure.step("Проверяем отрисовку элементов"):
                try:
                    browser.element('[data-wm-id="tech-panel"]').should(be.visible)
                except TimeoutException:
                    raise AssertionError(
                        f"❌ Planet Page did not load!\n"
                        f"   Expected URL part: {url_path}\n"
                        f"   Actual URL: {browser.driver.current_url}\n"
                        "   Timeout: tech-panel did not appear in time"
                    )
                except Exception as e:
                    raise AssertionError(
                        f"❌ Unexpected error while opening planet!\n"
                        f"   Path: {url_path}\n"
                        f"   Error: {e}"
                    ) from e

        return self

    # endregion

    # ========================================================================
    # region 2️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================

    @allure.step("🪐 Проверка имени планеты")
    def check_planet_name(self, expected_name: str) -> "PlanetPage":
        """
        Проверяет, что на странице отображается корректное имя планеты.

        Args:
            expected_name: Ожидаемое имя планеты (например, 'MERCURY').
        """
        with allure.step(f"Проверяем, что имя планеты равно '{expected_name}'"):
            try:
                browser.element(".planet-name").should(have.text(expected_name))
            except Exception as e:
                raise AssertionError(
                    f"❌ Planet name mismatch!\n"
                    f"   Expected: {expected_name}\n"
                    f"   Actual element: .planet-name\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("📡 Проверка массы планеты")
    def verify_tech_mass(self, expected_text: str) -> "PlanetPage":
        """
        Проверяет значение массы планеты в левой панели метрик.
        """
        with allure.step(f"Проверка массы (левая панель): '{expected_text}'"):
            try:
                self.mass_planet.should(have.text(expected_text))
            except TimeoutException:
                raise AssertionError(
                    f"❌ Planet mass text mismatch. Expected to contain: '{expected_text}'."
                )

        return self

    @allure.step(" Проверка описания планеты (правая панель)")
    def verify_info_description(self, expected_text: str) -> "PlanetPage":
        """
        Проверяет текст описания планеты в правой панели профиля.
        """
        with allure.step(f"Проверка описания (правая панель): '{expected_text}'"):
            try:
                self.info_description.should(have.text(expected_text))
            except TimeoutException:
                raise AssertionError(
                    f"❌ Planet description text mismatch. Expected to contain: '{expected_text}'."
                )

        return self

    @allure.step("🛰️ Проверка статуса миссии (правая панель)")
    def verify_mission_status(self, expected_text: str) -> "PlanetPage":
        """
        Проверяет текст статуса разведки в правой панели.
        """
        with allure.step(f"Проверка статуса миссии (правая панель): '{expected_text}'"):
            try:
                self.mission_status.should(have.text(expected_text))
            except TimeoutException:
                raise AssertionError(
                    f"❌ Mission status text mismatch. Expected to contain: '{expected_text}'."
                )

        return self

    # endregion
