import allure
from selene import be, browser
from selenium.common.exceptions import TimeoutException

from pages.core import CorePage
from tests import data


class IndexPage(CorePage):

    # URL
    PATH = data.INDEX_URL
    
    # Логотип и футер
    logo_cassan = browser.element('[data-wm-id="logo-cassan"]')
    logo_dra = browser.element('[data-wm-id="logo-dra"]')
    footer_copyright = browser.element('[data-wm-id="footer-copyright"]')

    # Заголовок и слоган
    project_title = browser.element('[data-wm-id="project-title"]')
    project_slogan = browser.element('[data-wm-id="project-slogan"]')

    
    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌐 Открытие страницы индекса")
    def open(self):
        """Открывает страницу индекса и проверяет её загрузку.

        Returns:
            self: Экземпляр IndexPage для chaining-а методов.

        Raises:
            AssertionError: Если страница не загрузилась в течение таймаута.
        """
        with allure.step(f"Открываем страницу: {self.PATH}"):
            browser.open(self.PATH)

        with allure.step("Проверяем URL и отрисовку элементов"):
            try:

                self.wait_for_url(expected_url_part=data.INDEX_URL)

                self.log_in_btn.should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Index page did not load!\n"
                    f"   Expected URL: {self.PATH}\n"
                    f"   Actual URL: {browser.driver.current_url}\n"
                    "   Timeout: log_in_btn did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening import page!\n"
                    f"   Path: {self.PATH}\n"
                    f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 2️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================
    
    @allure.step("💓 Проверка наличия и параметров анимации ЭКГ")
    def verify_ecg_animation_in_dom(self):
        """Проверяет наличие контейнеров ЭКГ и анимацию их внутренних путей.

        Ожидаемые параметры:
            - 2 контейнера: .heartbeat-blue и .heartbeat-white
            - animation-name: drawHeartbeat (на .heartbeat-path)
            - animation-duration: 15s (на .heartbeat-path)
        """
        with allure.step("Находим контейнеры .heartbeat-blue и .heartbeat-white"):
            try:
                heartbeat_blue = browser.element(".heartbeat-blue")
                heartbeat_white = browser.element(".heartbeat-white")

                with allure.step("Проверяем, что оба контейнера существуют"):
                    heartbeat_blue.should(be.visible)
                    heartbeat_white.should(be.visible)

                for name, container in [
                    ("blue", heartbeat_blue),
                    ("white", heartbeat_white),
                ]:
                    with allure.step(
                        f"Проверяем анимацию пути в контейнере .heartbeat-{name}"
                    ):
                
                        path = container.element(".heartbeat-path")

                        styles = browser.driver.execute_script(
                            """
                            const el = arguments[0];
                            const computed = window.getComputedStyle(el);
                            return {
                                animationName: computed.animationName,
                                animationDuration: computed.animationDuration
                            };
                            """,
                            path(),
                        )

                        animation_name = styles["animationName"]
                        animation_duration = styles["animationDuration"]

                        with allure.step(f"🔍 animation-name = {animation_name}"):
                            pass
                        with allure.step(
                            f"🔍 animation-duration = {animation_duration}"
                        ):
                            pass

                        assert "drawHeartbeat" in animation_name, (
                            f"❌ Ошибка animation-name!\n"
                            f"Ожидалось: drawHeartbeat\n"
                            f"Получено:  {animation_name}"
                        )

                        assert "15s" in animation_duration, (
                            f"❌ Ошибка animation-duration!\n"
                            f"Ожидалось: 15s\n"
                            f"Получено:  {animation_duration}"
                        )

            except TimeoutException:
                raise AssertionError(
                    "❌ Heartbeat containers not found!\n"
                    "   Timeout: elements did not appear in time"
                )
            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while checking ECG animation!\n"
                    f"   Error: {e}"
                ) from e
        return self
