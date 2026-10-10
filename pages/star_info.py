import allure
from selene import be, browser, have
from selenium.common.exceptions import (
    TimeoutException,
)

from pages.core import CorePage


class StarInfoPage(CorePage):

    # Левая панель (Технические данные / Tech Panel)
    tech_panel_type = browser.element('[data-wm-id="tech-panel-type"]')
    tech_panel_name = browser.element('[data-wm-id="tech-panel-name"]')
    tech_classification = browser.element('[data-wm-id="tech-classification"]')

    # Правая панель (Журнал наблюдений / Info Panel)
    info_description = browser.element('[data-wm-id="info-description"]')
   

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌟 Открытие страницы Star Info")
    def open(self, url_path: str, expect_redirect: bool = False) -> "StarInfoPage":
        """
        Открывает страницу Star Info через переданный URL.
        
        Args:
            url_path: Путь к странице (например, из data.STAR_INFO_URL).
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
                        f"❌ Star Info Page did not load!\n"
                        f"   Expected URL part: {url_path}\n"
                        f"   Actual URL: {browser.driver.current_url}\n"
                        "   Timeout: tech-panel did not appear in time"
                    )
                except Exception as e:
                    raise AssertionError(
                        f"❌ Unexpected error while opening star-info!\n"
                        f"   Path: {url_path}\n"
                        f"   Error: {e}"
                    ) from e
                
        return self

    #endregion

    # ========================================================================
    # region 2️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================

    def verify_visual_class(self, expected_class: str) -> "StarInfoPage":
        """
        Проверяет отрисовку визуала объекта (звезды или черной дыры).
        """
        with allure.step(f"Проверка отрисовки визуала: {expected_class}"):

            selector = '.black-hole' if expected_class == 'black-hole' else f'.star-sphere.{expected_class}'
            element = browser.element(selector)

            try:
                
                element.should(be.visible)
            except TimeoutException:
               
                raise AssertionError(
                    f"❌ Visual element with selector '{selector}' is not visible or not found on the page."
                )

        return self

    def verify_tech_classification(self, expected_text: str) -> "StarInfoPage":
        """
        Проверяет текст классификации в левой технической панели.
        """
        with allure.step(f"Проверка классификации (левая панель): '{expected_text}'"):
            try:
                self.tech_classification.should(have.text(expected_text))
            except TimeoutException:
                raise AssertionError(
                    f"❌ Tech classification text mismatch. Expected to contain: '{expected_text}'."
                )
                
        return self

    def verify_info_description(self, expected_text: str) -> "StarInfoPage":
        """
        Проверяет начало описания в правой информационной панели.
        """
        with allure.step(f"Проверка описания (правая панель): '{expected_text}'"):
            try:
                self.info_description.should(have.text(expected_text))
            except TimeoutException:
                raise AssertionError(
                    f"❌ Info description text mismatch. Expected to contain: '{expected_text}'."
                )
                
        return self
    
    #endregion
    

