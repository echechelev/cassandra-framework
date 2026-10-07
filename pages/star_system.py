import allure
from selene import be, browser
from selenium.common.exceptions import (
    TimeoutException,
)

from pages.core import CorePage
from tests import data


class StarSystemPage(CorePage):

    # Кнопки планеты

    # Sol
    mercury_btn = browser.element('[data-wm-id="planet-mercury-btn"]')
    venus_btn = browser.element('[data-wm-id="planet-venus-btn"]')
    earth_btn = browser.element('[data-wm-id="planet-earth-btn"]')
    mars_btn = browser.element('[data-wm-id="planet-mars-btn"]')
    uranus_btn = browser.element('[data-wm-id="planet-uranus-btn"]')
    neptune_btn = browser.element('[data-wm-id="planet-neptune-btn"]')

    # Alpha Centauri
    proxima_b_btn = browser.element('[data-wm-id="planet-proxima-b-btn"]')
    proxima_c_btn = browser.element('[data-wm-id="planet-proxima-c-btn"]')
    proxima_d_btn = browser.element('[data-wm-id="planet-proxima-d-btn"]')

    # Epsilon Eridani
    epsilon_eridani_c_btn = browser.element('[data-wm-id="planet-epsilon-eridani-c-btn"]')

    # Tau Ceti
    tau_ceti_e_btn = browser.element('[data-wm-id="planet-tau-ceti-e-btn"]')
    tau_ceti_f_btn = browser.element('[data-wm-id="planet-tau-ceti-f-btn"]')
    tau_ceti_g_btn = browser.element('[data-wm-id="planet-tau-ceti-g-btn"]')
    tau_ceti_h_btn = browser.element('[data-wm-id="planet-tau-ceti-h-btn"]')

    # Teegarden's
    teegarden_b_btn = browser.element('[data-wm-id="planet-teegarden-b-btn"]')
    teegarden_c_btn= browser.element('[data-wm-id="planet-teegarden-c-btn"]')

    # TRAPPIST-1
    trappist_1b_btn = browser.element('[data-wm-id="planet-trappist-1b-btn"]')
    trappist_1c_btn = browser.element('[data-wm-id="planet-trappist-1c-btn"]')
    trappist_1d_btn = browser.element('[data-wm-id="planet-trappist-1d-btn"]')
    trappist_1e_btn = browser.element('[data-wm-id="planet-trappist-1e-btn"]')
    trappist_1f_btn = browser.element('[data-wm-id="planet-trappist-1f-btn"]')
    trappist_1g_btn = browser.element('[data-wm-id="planet-trappist-1g-btn"]')
    trappist_1h_btn = browser.element('[data-wm-id="planet-trappist-1h-btn"]')

    # Заголовки
    star_system_title = browser.element('[data-wm-id="star-system-title"]')

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌐 Открытие страницы звёздной системы")
    def open(self, star_key: str = "sun"):
        """Открывает страницу звёздной системы для переданной звезды.
        
        Args:
            star_key (str): Ключ звезды из data.STAR_SYSTEM_URL (по умолчанию 'sun').
        """
        path = data.STAR_SYSTEM_URL.get(star_key)
        if not path:
            raise ValueError(f"❌ Звезда '{star_key}' не найдена в data.STAR_SYSTEM_URL!")

        with allure.step(f"Открываем страницу: {path}"):
            browser.open(path)

        with allure.step("Проверяем URL и отрисовку элементов"):
            try:
                self.wait_for_url(expected_url_part=path)
                self.star_system_title.should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    f"❌ Star System Page ({star_key}) did not load!\n"
                    f"   Expected URL part: {path}\n"
                    f"   Actual URL: {browser.driver.current_url}\n"
                    "   Timeout: system_title did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening star system!\n"
                    f"   Star Key: {star_key}\n"
                    f"   Error: {e}"
                ) from e
                
        return self

    # ========================================================================
    # region 2️⃣ 🖱️ ДЕЙСТВИЯ С КНОПКАМИ
    # ========================================================================

    @allure.step("Клик по планете")
    def click_planet(self, element):
        """Универсальный клик по любой планете."""
        element.should(be.visible).click()
        return self

    #endregion
