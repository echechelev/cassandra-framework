import allure
from selene import be, browser
from selenium.common.exceptions import (
    TimeoutException,
)

from pages.core import CorePage
from tests import data


class GalaxyMapPage(CorePage):

    # URL
    PATH = data.GALAXY_MAP_URL

    # Кнопки звезды
    black_hole_btn = browser.element('[data-wm-id="black-hole-btn"]')
    sun_btn = browser.element('[data-wm-id="star-sun-btn"]')
    alpha_centauri_btn = browser.element('[data-wm-id="star-alpha-centauri-btn"]')
    epsilon_eridani_btn = browser.element('[data-wm-id="star-epsilon-eridani-btn"]')
    tau_ceti_btn = browser.element('[data-wm-id="star-tau-ceti-btn"]')
    teegarden_btn = browser.element('[data-wm-id="star-teegarden-btn"]')
    trappist_1_btn = browser.element('[data-wm-id="star-trappist-1-btn"]')

    # Заголовки
    galaxy_title = browser.element('[data-wm-id="galaxy-title"]')

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌐 Открытие страницы дашборда")
    def open(self):
        """Открывает страницу карта глактик и проверяет её загрузку.

        Returns:
            self: Экземпляр Galaxy Map Page для chaining-а методов.

        Raises:
            AssertionError: Если страница не загрузилась в течение таймаута.
        """
        with allure.step(f"Открываем страницу: {self.PATH}"):
            browser.open(self.PATH)

        with allure.step("Проверяем URL и отрисовку элементов"):
            try:
                self.wait_for_url(expected_url_part=data.GALAXY_MAP_URL)

                self.dashboard_btn.should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Galaxy Map Page did not load!\n"
                    f"   Expected URL: {self.PATH}\n"
                    f"   Actual URL: {browser.driver.current_url}\n"
                    "   Timeout: start_diagnostics_btn did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening galaxy-map!\n"
                    f"   Path: {self.PATH}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("🌟 Клик по кнопке звезды: {star_key}")
    def click_star_button(self, star_key: str):
        browser.element(f"[data-wm-id='star-{star_key}-btn']").should(be.visible).click()
        
        self.wait_for_url(expected_url_part=f"star-system.html?star={star_key}")

    # endregion

    # ========================================================================
    # region 2️⃣ 🖱️ ДЕЙСТВИЯ С КНОПКАМИ
    # ========================================================================

    @allure.step("Нажатие на черную дыру")
    def click_black_hole(self):
        """Нажимает на черную дыру."""
        with allure.step("Кликаем по черной дыре"):
            try:
                self.black_hole_btn.should(be.visible).click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Black hole not found or not clickable!\n"
                    "   Timeout: element did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking black hole!\n" f"   Error: {e}"
                ) from e
        return self

    @allure.step("Клик по звёздной системе")
    def click_star(self, element):
        """Универсальный клик по любой звезде."""
        element.should(be.visible).click()
        return self

    # endregion
