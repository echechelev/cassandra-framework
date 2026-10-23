import re

import allure
from selene import be, browser, have
from selenium.common.exceptions import (
    TimeoutException,
)
from selenium.webdriver.common.by import By

from pages.core import CorePage
from tests import data


class FlightCalcPage(CorePage):

    # URL
    PATH = data.FLIGHT_CALC_URL

    # Поля
    dep_system_select = browser.element('[data-wm-id="dep-system-select"]')
    dep_planet_select = browser.element('[data-wm-id="dep-planet-select"]')
    arr_system_select = browser.element('[data-wm-id="arr-system-select"]')
    arr_planet_select = browser.element('[data-wm-id="arr-planet-select"]')

    # Кнопки выбора кораблей
    ship_voyager_btn = browser.element('[data-wm-id="ship-voyager-btn"]')
    ship_parker_btn = browser.element('[data-wm-id="ship-parker-btn"]')
    ship_light_btn = browser.element('[data-wm-id="ship-light-btn"]')
    ship_warp_btn = browser.element('[data-wm-id="ship-warp-btn"]')

    # Кнопки управления калькулятором
    start_btn = browser.element('[data-wm-id="start-btn"]')
    info_btn = browser.element('[data-wm-id="info-btn"]')
    clear_btn = browser.element('[data-wm-id="clear-btn"]')

    # Модальные окна
    alert_modal = browser.element('[data-wm-id="alert-modal"]')
    info_modal = browser.element('[data-wm-id="info-modal"]')
    warning_modal = browser.element('[data-wm-id="warning-modal"]')

    # Окно результата
    result_time = browser.element('[data-wm-id="result-time"]')

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌐 Открытие страницы калькулятора полетов")
    def open(self):
        """Открывает страницу калькулятора полетов и проверяет её загрузку.

        Returns:
            self: Экземпляр Flight calc page для chaining-а методов.

        Raises:
            AssertionError: Если страница не загрузилась в течение таймаута.
        """
        with allure.step(f"Открываем страницу: {self.PATH}"):
            browser.open(self.PATH)

        with allure.step("Проверяем URL и отрисовку элементов"):
            try:
                self.wait_for_url(expected_url_part=data.FLIGHT_CALC_URL)

                self.start_btn.should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Flight page did not load!\n"
                    f"   Expected URL: {self.PATH}\n"
                    f"   Actual URL: {browser.driver.current_url}\n"
                    "   Timeout: start_btn did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening flight calc!\n"
                    f"   Path: {self.PATH}\n"
                    f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 2️⃣ ⌨️ ЗАПОЛНЕНИЕ ПОЛЕЙ
    # ========================================================================

    @allure.step("🌌 Выбор системы отправления")
    def select_dep_system(self, system_name: str):
        """Выбирает звёздную систему отправления из выпадающего списка.

        Args:
            system_name: ID системы для выбора (например, 'sol', 'alpha-centauri-a').

        Returns:
            self: Экземпляр FlightCalculator page для chaining-а методов.

        Raises:
            AssertionError: Если поле не отрисовалось или опции не загрузились.
            AssertionError: Если переданная система не найдена в списке.
        """
        with allure.step("Кликаем по полю Dep System и ждём загрузки опций"):
            try:
                self.dep_system_select.should(be.visible)
                self.dep_system_select.click()

                self.dep_system_select.element('option[value="sol"]').should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Dep System select not loaded!\n"
                    "   Timeout: field or options did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening Dep System select!\n"
                    f"   Error: {e}"
                ) from e

        with allure.step(f"Выбираем систему: {system_name}"):
            try:
              
                option = self.dep_system_select.element(
                    f'option[value="{system_name}"]'
                )
                option.should(be.visible)
                option.click()

                browser.element("body").click()

                self.dep_system_select.should(have.value(system_name))

            except TimeoutException:
                raise AssertionError(
                    f"❌ System '{system_name}' not found in Dep System list!\n"
                    "   Timeout: option did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while selecting system '{system_name}'!\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("🪐 Выбор планеты отправления")
    def select_dep_planet(self, planet_name: str):
        """Выбирает планету отправления из выпадающего списка.

        Args:
            planet_name: ID планеты для выбора (например, 'earth', 'mars').

        Returns:
            self: Экземпляр FlightCalculator page для chaining-а методов.

        Raises:
            AssertionError: Если поле не отрисовалось или опции не загрузились.
            AssertionError: Если переданная планета не найдена в списке.
        """
        with allure.step("Кликаем по полю Dep Planet и ждём загрузки опций"):
            try:
                self.dep_planet_select.should(be.visible)
                self.dep_planet_select.click()

                self.dep_planet_select.element('option[value=""]').should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Dep Planet select not loaded!\n"
                    "   Timeout: field or options did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening Dep Planet select!\n"
                    f"   Error: {e}"
                ) from e

        with allure.step(f"Выбираем планету: {planet_name}"):
            try:
                option = self.dep_planet_select.element(
                    f'option[value="{planet_name}"]'
                )
                option.should(be.visible)
                option.click()

                browser.element("body").click()

                self.dep_planet_select.should(have.value(planet_name))

            except TimeoutException:
                raise AssertionError(
                    f"❌ Planet '{planet_name}' not found in Dep Planet list!\n"
                    "   Timeout: option did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while selecting planet '{planet_name}'!\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("🌌 Выбор системы прибытия")
    def select_arr_system(self, system_name: str):
        """Выбирает звёздную систему прибытия из выпадающего списка.

        Args:
            system_name: ID системы для выбора (например, 'sol', 'alpha-centauri-a').

        Returns:
            self: Экземпляр FlightCalculator page для chaining-а методов.

        Raises:
            AssertionError: Если поле не отрисовалось или опции не загрузились.
            AssertionError: Если переданная система не найдена в списке.
        """
        with allure.step("Кликаем по полю Arr System и ждём загрузки опций"):
            try:
                self.arr_system_select.should(be.visible)
                self.arr_system_select.click()

                self.arr_system_select.element('option[value="sol"]').should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Arr System select not loaded!\n"
                    "   Timeout: field or options did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening Arr System select!\n"
                    f"   Error: {e}"
                ) from e

        with allure.step(f"Выбираем систему: {system_name}"):
            try:
                option = self.arr_system_select.element(
                    f'option[value="{system_name}"]'
                )
                option.should(be.visible)
                option.click()

                browser.element("body").click()

                self.arr_system_select.should(have.value(system_name))

            except TimeoutException:
                raise AssertionError(
                    f"❌ System '{system_name}' not found in Arr System list!\n"
                    "   Timeout: option did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while selecting system '{system_name}'!\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("🪐 Выбор планеты прибытия")
    def select_arr_planet(self, planet_name: str):
        """Выбирает планету прибытия из выпадающего списка.

        Args:
            planet_name: ID планеты для выбора (например, 'proxima-b', 'tau-ceti-e').

        Returns:
            self: Экземпляр FlightCalculator page для chaining-а методов.

        Raises:
            AssertionError: Если поле не отрисовалось или опции не загрузились.
            AssertionError: Если переданная планета не найдена в списке.
        """
        with allure.step("Кликаем по полю Arr Planet и ждём загрузки опций"):
            try:
                self.arr_planet_select.should(be.visible)
                self.arr_planet_select.click()

                self.arr_planet_select.element('option[value=""]').should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ Arr Planet select not loaded!\n"
                    "   Timeout: field or options did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening Arr Planet select!\n"
                    f"   Error: {e}"
                ) from e

        with allure.step(f"Выбираем планету: {planet_name}"):
            try:
                option = self.arr_planet_select.element(
                    f'option[value="{planet_name}"]'
                )
                option.should(be.visible)
                option.click()

                browser.element("body").click()

                self.arr_planet_select.should(have.value(planet_name))

            except TimeoutException:
                raise AssertionError(
                    f"❌ Planet '{planet_name}' not found in Arr Planet list!\n"
                    "   Timeout: option did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while selecting planet '{planet_name}'!\n"
                    f"   Error: {e}"
                ) from e

        return self

    # endregion

    # ========================================================================
    # region 3️⃣ 🖱️ Методы для кнопок 
    # ========================================================================

    @allure.step("🚀 Выбор класса корабля")
    def select_ship(
        self,
        voyager: bool = False,
        parker: bool = False,
        light: bool = False,
        warp: bool = False,
    ):
        """Нажимает на одну из кнопок выбора класса корабля.

        Args:
            voyager: Нажать кнопку Voyager (16 km/s).
            parker: Нажать кнопку Parker Probe (197 km/s).
            light: Нажать кнопку Light Drive (0.1 c).
            warp: Нажать кнопку Warp Drive (0.5 c).

        Returns:
            self: Экземпляр FlightCalculator page для chaining-а методов.

        Raises:
            AssertionError: Если не передан ни один аргумент или передано больше одного True.
            AssertionError: Если кнопка не найдена или не кликабельна.
        """
        ship_buttons = {
            "Voyager": (self.ship_voyager_btn, voyager),
            "Parker Probe": (self.ship_parker_btn, parker),
            "Light Drive": (self.ship_light_btn, light),
            "Warp Drive": (self.ship_warp_btn, warp),
        }

        selected = [
            name for name, (_, is_selected) in ship_buttons.items() if is_selected
        ]

        with allure.step(
            f"Выбираем класс корабля: {selected if selected else 'НЕ УКАЗАН'}"
        ):
            if len(selected) == 0:
                raise AssertionError(
                    "❌ No vessel class selected!\n"
                    "   Please pass True to one of the arguments: voyager, parker, light, warp"
                )
            if len(selected) > 1:
                raise AssertionError(
                    f"❌ Multiple vessel classes selected: {selected}\n"
                    "   Only one argument can be set to True"
                )

            ship_name = selected[0]
            locator, _ = ship_buttons[ship_name]

            try:
                locator.click()

            except TimeoutException:
                raise AssertionError(
                    f"❌ '{ship_name}' button not found or not clickable!\n"
                    f"   Locator: {locator}\n"
                    "   Timeout: element did not appear in DOM within timeout"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking '{ship_name}' button!\n"
                    f"   Locator: {locator}\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("Нажатие кнопки Start")
    def click_start_calc(self):
        """Нажимает кнопку запуска расчёта времени полёта."""
        with allure.step("Кликаем по кнопке Start"):
            try:
                self.start_btn.should(be.visible).should(be.enabled)
                self.start_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Start button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Start!\n" f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие кнопки Info")
    def click_info(self):
        """Нажимает кнопку информационной модалки."""
        with allure.step("Кликаем по кнопке Info"):
            try:
                self.info_btn.should(be.visible).should(be.enabled)
                self.info_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Info button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Info!\n" f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие кнопки Clear")
    def click_clear(self):
        """Нажимает кнопку очистки полей."""
        with allure.step("Кликаем по кнопке Clear"):
            try:
                self.clear_btn.should(be.visible).should(be.enabled)
                self.clear_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Clear button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Clear!\n" f"   Error: {e}"
                ) from e
        return self

    # endregion

    # ========================================================================
    # region 4️⃣ ✅ ПРОВЕРКИ СОСТОЯНИЙ
    # ========================================================================
    
    @allure.step(" Проверка заполнения списка планет отправления")
    def verify_dep_planets_populated(
        self, 
        system_id: str, 
        expected_planet_id: str | None = None, 
        unexpected_planet_id: str | None = None
    ):
        """Проверяет наличие и/или отсутствие конкретных планет в селекте отправления.

        Args:
            system_id: ID системы (для логирования).
            expected_planet_id: ID планеты, которая ДОЛЖНА быть в списке (опционально).
            unexpected_planet_id: ID планеты, которой НЕ ДОЛЖНО быть в списке (опционально).

        Returns:
            self: Экземпляр FlightCalculator page для chaining-а методов.
        """
        with allure.step(f"Проверяем корректность списка планет для системы '{system_id}'"):
            try:
            
                if expected_planet_id:
                    with allure.step(f"✅ Ожидаем наличие планеты: {expected_planet_id}"):
                        self.dep_planet_select.element(
                            f'option[value="{expected_planet_id}"]'
                        ).should(be.present)

                if unexpected_planet_id:
                    with allure.step(f" Ожидаем отсутствие планеты: {unexpected_planet_id}"):
                        self.dep_planet_select.element(
                            f'option[value="{unexpected_planet_id}"]'
                        ).should(be.absent)

                if not expected_planet_id and not unexpected_planet_id:
                    allure.step("⚠️ Ни одна планета для проверки не передана.")

            except TimeoutException:
                raise AssertionError(
                    "❌ Dep Planet select not visible!\n"
                    "   Timeout: select did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while verifying Dep Planet list!\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("🔍 Проверка заполнения списка планет прибытия")
    def verify_arr_planets_populated(
        self, 
        system_id: str, 
        expected_planet_id: str | None = None, 
        unexpected_planet_id: str | None = None
    ):
        """Проверяет наличие и/или отсутствие конкретных планет в селекте прибытия.

        Args:
            system_id: ID системы (для логирования).
            expected_planet_id: ID планеты, которая ДОЛЖНА быть в списке (опционально).
            unexpected_planet_id: ID планеты, которой НЕ ДОЛЖНО быть в списке (опционально).

        Returns:
            self: Экземпляр FlightCalculator page для chaining-а методов.
        """
        with allure.step(f"Проверяем корректность списка планет для системы '{system_id}' в Arr Planet"):
            try:
            
                if expected_planet_id:
                    with allure.step(f"✅ Ожидаем наличие планеты: {expected_planet_id}"):
                        self.arr_planet_select.element(
                            f'option[value="{expected_planet_id}"]'
                        ).should(be.present)

                if unexpected_planet_id:
                    with allure.step(f"🚫 Ожидаем отсутствие планеты: {unexpected_planet_id}"):
                        self.arr_planet_select.element(
                            f'option[value="{unexpected_planet_id}"]'
                        ).should(be.absent)

                if not expected_planet_id and not unexpected_planet_id:
                    allure.step("⚠️ Ни одна планета для проверки не передана.")

            except TimeoutException:
                raise AssertionError(
                    "❌ Arr Planet select not visible!\n"
                    "   Timeout: select did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while verifying Arr Planet list!\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("🧹 Проверка успешного сброса формы")
    def verify_form_cleared(self):
        """Проверяет, что все поля формы вернулись к дефолтному состоянию после сброса.

        Returns:
            self: Экземпляр FlightCalculator page для chaining-а методов.

        Raises:
            AssertionError: Если хотя бы одно поле не содержит дефолтный текст.
        """
        with allure.step("Проверяем, что все селекты сброшены к дефолтным значениям"):
            try:
                default_system_text = "— Select System —"
                default_planet_text = "— Select Planet —"

                self.dep_system_select.element('option:checked').should(have.text(default_system_text))
                self.dep_planet_select.element('option:checked').should(have.text(default_planet_text))
                
                self.arr_system_select.element('option:checked').should(have.text(default_system_text))
                self.arr_planet_select.element('option:checked').should(have.text(default_planet_text))

            except TimeoutException:
                raise AssertionError(
                    "❌ Form not cleared!\n"
                    "   Timeout: fields did not reset to default values"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while verifying form reset!\n"
                    f"   Error: {e}"
                ) from e

        return self

    @allure.step("🧹 Проверка сброса выбора корабля")
    def verify_ship_selection_cleared(self):
        """Проверяет, что все кнопки выбора корабля отжаты после сброса формы."""
        from selene import browser
        
        with allure.step("Проверяем, что все кнопки кораблей отжаты"):
            try:
               
                active_count = browser.driver.execute_script(
                    "return document.querySelectorAll('.ship-option.active').length"
                )
                
                assert active_count == 0, f"Found {active_count} active ship buttons!"
                
            except Exception as e:
                raise AssertionError(f"❌ Error verifying ship reset: {e}") from e
        
        return self

    @allure.step("⏱️ Проверка времени полета")
    def verify_flight_time(self, years: int, months: int, days: int):
        """Проверяет время полета, извлекая только цифры и игнорируя склонения слов."""
        with allure.step(f"Ожидаем время: {years} лет, {months} мес, {days} дней"):
          
            self.result_time.should(be.visible)
            
            try:
                actual_text = self.result_time.get_actual_webelement().text  # type: ignore
            except AttributeError:
                
                actual_text = browser.driver.find_element(By.ID, "result-time").text
            
            numbers = re.findall(r'\d+', actual_text)
            
            assert len(numbers) == 3, f"❌ Expected 3 numbers in text, but found {len(numbers)} in: '{actual_text}'"

            assert int(numbers[0]) == years, f"❌ Years mismatch! Expected {years}, found {numbers[0]}"
            assert int(numbers[1]) == months, f"❌ Months mismatch! Expected {months}, found {numbers[1]}"
            assert int(numbers[2]) == days, f"❌ Days mismatch! Expected {days}, found {numbers[2]}"

        return self