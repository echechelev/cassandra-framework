import allure
from selene import be, browser, have
from selenium.common.exceptions import (
    TimeoutException,
)

from pages.core import CorePage


class PlanetPage(CorePage):

    planet_name_element = browser.element('.planet-name')
    tech_panel = browser.element('[data-wm-id="tech-panel"]') 

  
    


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

    @allure.step("🪐 Проверка имени планеты")
    def check_planet_name(self, expected_name: str) -> "PlanetPage":
        """
        Проверяет, что на странице отображается корректное имя планеты.
        
        Args:
            expected_name: Ожидаемое имя планеты (например, 'MERCURY').
        """
        with allure.step(f"Проверяем, что имя планеты равно '{expected_name}'"):
            try:
                browser.element('.planet-name').should(have.text(expected_name))
            except Exception as e:
                raise AssertionError(
                    f"❌ Planet name mismatch!\n"
                    f"   Expected: {expected_name}\n"
                    f"   Actual element: .planet-name\n"
                    f"   Error: {e}"
                ) from e
                
        return self

    #endregion