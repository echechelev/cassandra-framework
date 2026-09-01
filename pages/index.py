import allure
from selene import be, browser
from selenium.common.exceptions import TimeoutException

from pages.hub import HubPage


class IndexPage(HubPage):

    # URL
    PATH = "/index.html"

    # Логотип
    logo_cassan = browser.element('[data-wm-id="logo-cassan"]')
    logo_dra = browser.element('[data-wm-id="logo-dra"]')

    # Заголовок и слоган
    project_title = browser.element('[data-wm-id="project-title"]')
    project_slogan = browser.element('[data-wm-id="project-slogan"]')

    # Кнопки
    log_in_btn = browser.element('[data-wm-id="btn-login"]')
    sign_up_btn = browser.element('[data-wm-id="btn-signup"]')

    # Футер
    footer_copyright = browser.element('[data-wm-id="footer-copyright"]')

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
            try:
                browser.open(self.PATH)
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
    # region 2️⃣ 🖱️ ДЕЙСТВИЯ С КНОПКАМИ
    # ========================================================================

    @allure.step("Нажатие кнопки Log in")
    def click_log_in(self):
        """Нажимает кнопку инициализации системы Log in."""
        with allure.step("Кликаем по кнопке Log in"):
            try:
                self.log_in_btn.should(be.visible).should(be.enabled)
                self.log_in_btn.click()

            except TimeoutException:
                raise AssertionError(
                    "❌ Log in button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Log in!\n" f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие кнопки Sign up")
    def click_sign_up(self):
        """Нажимает кнопку инициализации системы Sign up."""
        with allure.step("Кликаем по кнопке Sign up"):
            try:
                self.sign_up_btn.should(be.visible).should(be.enabled)
                self.sign_up_btn.click()

            except TimeoutException:
                raise AssertionError(
                    "❌ Sign up button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Sign up!\n" f"   Error: {e}"
                ) from e
        return self

    @allure.step("🖱️ Наведение на кнопку Log in")
    def hover_log_in(self):
        """Наводит курсор на кнопку инициализации системы Log in."""
        with allure.step("Наводим курсор на кнопку Log in"):
            try:
                self.log_in_btn.should(be.visible).should(be.enabled)
                self.log_in_btn.hover()

            except TimeoutException:
                raise AssertionError(
                    "❌ Log in button not found or not hoverable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while hovering Log in!\n" f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 3️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================

    @allure.step("✨ Проверка CSS-эффектов при ховере на кнопку Log in")
    def verify_log_in_hover_effects(self):
        """Проверяет CSS-свойства кнопки после ховера.

        Ожидаемые эффекты:
            - transform: scale(1.15) [с допуском ±0.01]
            - border-color: rgba(77, 166, 255, 1)
        """
        with allure.step("Получаем computed CSS-свойства кнопки"):
            try:
                self.log_in_btn.should(be.visible)

                styles = browser.driver.execute_script(
                    """
                    const el = arguments[0];
                    const computed = window.getComputedStyle(el);
                    return {
                        transform: computed.transform,
                        borderColor: computed.borderColor
                    };
                    """,
                    self.log_in_btn(),
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
                    "❌ Log in button not found!\n"
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
