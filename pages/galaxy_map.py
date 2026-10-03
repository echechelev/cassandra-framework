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

    def open_unauthenticated(self):
        """
        Открывает страницу с очищенным sessionStorage (для негативных тестов).
        Симулирует переход на страницу без авторизации.
        """

        browser.open(data.GALAXY_MAP_URL)

        browser.driver.execute_script("sessionStorage.clear();")

        browser.driver.refresh()

        return self

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

    @allure.step("✨ Проверка CSS-эффектов при ховере на кнопку Sun")
    def verify_sun_btn_hover_effects(self):
        """Проверяет CSS-свойства кнопки после ховера.

        Ожидаемые эффекты:
            - transform: scale(1.15) [с допуском ±0.01]
            - border-color: rgba(77, 166, 255, 1)
        """
        with allure.step("Получаем computed CSS-свойства кнопки"):
            try:
                self.sun_btn.should(be.visible)

                styles = browser.driver.execute_script(
                    """
                    const el = arguments[0];
                    const computed = window.getComputedStyle(el);
                    return {
                        transform: computed.transform,
                        borderColor: computed.borderColor
                    };
                    """,
                    self.sun_btn(),
                )

                transform = styles["transform"]
                border_color = styles["borderColor"]

                with allure.step(f"🔍 transform = {transform}"):
                    pass
                with allure.step(f"🔍 border-color = {border_color}"):
                    pass

                import re

                matrix_match = re.search(r"matrix\(([\d.]+)", transform)
                assert (
                    matrix_match
                ), f"❌ Не удалось извлечь значение из transform: {transform}"

                scale_value = float(matrix_match.group(1))
                expected_scale = 1.15
                tolerance = 0.01  # Допуск 1%

                assert abs(scale_value - expected_scale) <= tolerance, (
                    f"❌ Ошибка transform!\n"
                    f"Ожидалось: scale({expected_scale}) ± {tolerance}\n"
                    f"Получено:  scale({scale_value})"
                )

                assert (
                    "77" in border_color
                    and "166" in border_color
                    and "255" in border_color
                ), (
                    f"❌ Ошибка border-color!\n"
                    f"Ожидалось: rgba(77, 166, 255, 1)\n"
                    f"Получено:  {border_color}"
                )

            except TimeoutException:
                raise AssertionError(
                    "❌ Sun button not found!\n"
                    "   Timeout: button did not appear in time"
                )
            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking hover effects!\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("🖱️ Наведение на кнопку звезду Sun")
    def hover_sun(self):
        """Наводит курсор на кнопку инициализации системы Sun."""
        with allure.step("Наводим курсор на кнопку Sun"):
            try:
                self.sun_btn.should(be.visible).should(be.enabled)
                self.sun_btn.hover()

            except TimeoutException:
                raise AssertionError(
                    "❌ Sun button not found or not hoverable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while hovering Sun!\n" f"   Error: {e}"
                ) from e
        return self

    # endregion
