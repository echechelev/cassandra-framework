import time

import allure
from selene import be, browser, have
from selenium.common.exceptions import (
    TimeoutException,
)
from selenium.webdriver.common.by import By

from pages.core import CorePage
from tests import data


class CisIndexTablePage(CorePage):

    # URL
    PATH = data.CIS_INDEX_TABLE_URL

    # Основные кнопки
    add_planet_btn = browser.element('[data-wm-id="btn-add"]')
    analyze_cis_btn = browser.element('[data-wm-id="btn-scan"]')
    clear_all_btn = browser.element('[data-wm-id="btn-clear"]')
    index_info_btn = browser.element('[data-wm-id="btn-scan-info"]')

    # Тексты ошибок и модалок
    toast_message = browser.element('[data-wm-id="toast-message"]')

    # Общий локатор для лейбла планеты
    planet_labels = browser.all(".planet-name-label")

    # Локатор окна результатов с текстом CIS
    cis_result = browser.element('[data-wm-id="cis-result"]')
    cis_score = browser.element('[data-wm-id="cis-score"]')
    cis_status = browser.element('[data-wm-id="cis-status-badge"]')

    # Общий локатор для выдачи в архиве
    archive_planet_names = browser.all(".archive-list .planet-name")
    archive_list = browser.element('[data-wm-id="archive-list"]')


    # Модалка выбора планет при добавлении
    planet_selector_modal = browser.element('[data-wm-id="planet-selector-modal"]')
    add_modal_close_btn = browser.element('[data-wm-id="btn-close-modal"]')
    add_modal_cancel_btn = browser.element('[data-wm-id="btn-cancel"]')

    # Модалка подтверждения удаления
    confirm_delete_modal = browser.element('[data-wm-id="confirm-delete-title"]')

    # Контейнеры таблиц
    scanner_empty = browser.element('[data-wm-id="scanner-empty"]')
    scanner_active = browser.element('[data-wm-id="scanner-active"]')

    # Название планеты в активной сканере
    scan_planet_name = browser.element('[data-wm-id="scan-planet-name"]')

    # Модалка окна скан инфо
    scan_info_modal = browser.element('[data-wm-id="scan-info-modal"]')
    scan_modal_close_btn = browser.element('[data-wm-id="btn-close-scan-info"]')
    scan_modal_cancel_btn = browser.element('[data-wm-id="btn-cancel-info"]')

    # Модалка детали
    details_modal = browser.element('[data-wm-id="details-modal"]')
    details_modal_close_btn = browser.element('[data-wm-id="btn-close-details"]')
    details_modal_cancel_btn = browser.element('[data-wm-id="btn-cancel-details"]')
    details_planet_name = browser.element('[data-wm-id="details-planet-name"]')
    details_description = browser.element('[data-wm-id="details-description"]')
    details_warning = browser.element('[data-wm-id="details-warning"]')

    # Модалки подтверждения удаления
    delete_confirm_clear_all_modal = browser.element(
        '[data-wm-id="confirm-delete-modal"]'
    )
    delete_confirm_delete_modal = browser.element(
        '[data-wm-id="confirm-delete-overlay"]'
    )
    delete_all_modal_close_btn = browser.element(
        '[data-wm-id="btn-close-confirm-delete"]'
    )
    delete_all_modal_cancel_btn = browser.element('[data-wm-id="btn-cancel-delete"]')
    delete_all_modal_confirm_delete_btn = browser.element(
        '[data-wm-id="btn-confirm-delete"]'
    )

    # ========================================================================
    # region 1️⃣ 🌐 НАВИГАЦИЯ
    # ========================================================================

    @allure.step("🌐 Открытие страницы расчета индекса CIS")
    def open(self):
        """Открывает страницу расссчета индексса и проверяет её загрузку.

        Returns:
            self: Экземпляр Cis Index Table page для chaining-а методов.

        Raises:
            AssertionError: Если страница не загрузилась в течение таймаута.
        """
        with allure.step(f"Открываем страницу: {self.PATH}"):
            browser.open(self.PATH)

        with allure.step("Проверяем URL и отрисовку элементов"):
            try:
                self.wait_for_url(expected_url_part=data.CIS_INDEX_TABLE_URL)

                self.add_planet_btn.should(be.visible)

            except TimeoutException:
                raise AssertionError(
                    "❌ CIS page did not load!\n"
                    f"   Expected URL: {self.PATH}\n"
                    f"   Actual URL: {browser.driver.current_url}\n"
                    "   Timeout: add_planet_btn did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while opening cis index table page!\n"
                    f"   Path: {self.PATH}\n"
                    f"   Error: {e}"
                ) from e
        return self

    @allure.step("Нажатие кнопки Add planet")
    def click_add_planet(self, expected_error_message: str | None = None):
        """
        Нажимает кнопку добавить планету.
        Если передан expected_error_message, проверяет появление ошибки (Toast).
        Иначе ожидает появления модального окна выбора планеты.

        Args:
            expected_error_message: Ожидаемый текст ошибки (если ожидается ошибка, например, дубликата).
        """
        with allure.step("Кликаем по кнопке Add planet"):
            try:
                self.add_planet_btn.should(be.visible).should(be.enabled)
                self.add_planet_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Add planet button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Add planet!\n" f"   Error: {e}"
                ) from e

        if expected_error_message:
            with allure.step(f"Проверяем появление ошибки: '{expected_error_message}'"):
                self.toast_message.should(have.text(expected_error_message))
        else:
            with allure.step(
                "Ожидаем появление модального окна выбора планеты (planet_selector_modal)"
            ):
                self.planet_selector_modal.should(be.visible)

        return self

    @allure.step("Выбор планеты")
    def select_planet(self, planet_name: str, wait_for_close: bool = True):
        """
        Выбирает планету в модальном окне по тексту лейбла.

        Args:
            planet_name: Название планеты из констант (например, 'MARS', 'EARTH').
            wait_for_close: Если True (по умолчанию) — ждёт закрытия модалки.
                            Если False — не ждёт (для негативных сценариев, например, дубликата).
        """
        # Находим конкретный лейбл в коллекции по точному тексту
        target_label = self.planet_labels.element_by(have.text(planet_name))

        with allure.step(f"Ищем карточку планеты с лейблом '{planet_name}'"):
            target_label.should(be.visible)

        with allure.step(f"Кликаем по карточке планеты '{planet_name}'"):
            try:
                # Поднимаемся к родителю .planet-card через '..'
                target_label.element("..").click()
            except Exception as e:
                raise AssertionError(
                    f"❌ Failed to click planet card '{planet_name}'!\n"
                    f"   Error: {e}"
                ) from e

        if wait_for_close:
            with allure.step("Ожидаем закрытие модального окна выбора планеты"):
                self.planet_selector_modal.should(be.hidden)

        return self

    @allure.step("Нажатие кнопки Analyze CIS")
    def click_analyze_cis(self, wait_for_completion: bool = True):
        """
        Проверяет, что кнопка Analyze CIS активна, кликает по ней.
        Если wait_for_completion=True, ожидает завершения расчета (появление блока CIS Result)
        и делает паузу для сохранения записи в архив.

        Args:
            wait_for_completion: Ожидать ли появления блока CIS Result после клика.
        """
        with allure.step("Проверяем, что кнопка Analyze CIS активна"):
            self.analyze_cis_btn.should(be.visible).should(be.enabled)

        with allure.step("Кликаем по кнопке Analyze CIS"):
            try:
                self.analyze_cis_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Analyze CIS button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Analyze CIS!\n"
                    f"   Error: {e}"
                ) from e

        if wait_for_completion:
            with allure.step("Ожидаем завершения расчета (появление CIS Result)"):
                try:
                    # Ждем до 10 секунд, пока блок не станет видимым и не будет содержать нужный текст
                    self.cis_result.with_(timeout=10).should(be.visible).should(
                        have.text(data.CASSANDRA_INDEX_TEXT)
                    )
                except TimeoutException:
                    raise AssertionError(
                        "❌ CIS Result not appeared or text mismatch!\n"
                        "   Timeout: calculation took more than 10 seconds or text is incorrect"
                    )
                except Exception as e:
                    raise AssertionError(
                        f"❌ Unexpected error while waiting for CIS Result!\n"
                        f"   Error: {e}"
                    ) from e

            with allure.step("Ожидание 3 сек. для сохранения записи в архив"):
                self.pause(3)

        return self

    @allure.step("Проверка наличия или отсутствия планеты в архиве")
    def verify_planet_in_archive(self, planet_name: str, should_exist: bool = True):
        """
        Проверяет, что планета с заданным именем есть (или нет) в архиве.
        
        Args:
            planet_name: Имя планеты для поиска.
            should_exist: Если True - проверяет наличие (по умолчанию). 
                          Если False - проверяет отсутствие.
        """
        state_word = "наличия" if should_exist else "отсутствия"
        
        with allure.step(f"Проверяем {state_word} планеты '{planet_name}' в архиве"):
            # Ищем конкретный элемент в коллекции по точному тексту
            target_planet = self.archive_planet_names.element_by(have.text(planet_name))

            try:
                if should_exist:
                    target_planet.should(be.visible)
                else:
                    # Магия Selene: ждем, пока элемент исчезнет из DOM или станет скрытым
                    target_planet.should(be.hidden) 
                    
            except TimeoutException:
                if should_exist:
                    raise AssertionError(
                        f"❌ Planet '{planet_name}' not found in archive!\n"
                        f"   Timeout: planet did not appear in archive list"
                    )
                else:
                    raise AssertionError(
                        f"❌ Planet '{planet_name}' is still present in archive!\n"
                        f"   Expected: planet should be absent"
                    )
            except Exception as e:
                raise AssertionError(
                    f"❌ Failed to verify planet '{planet_name}' in archive!\n"
                    f"   Error: {e}"
                ) from e

        return self

    def verify_planet_visible_in_modal(self, planet_name: str):
        """
        Проверяет, что конкретная планета (по её имени из констант)
        отображается в модальном окне выбора.
        """

        target_label = self.planet_labels.element_by(have.text(planet_name))

        with allure.step(
            f"Проверяем, что лейбл планеты '{planet_name}' виден в модалке"
        ):
            target_label.should(be.visible)

        return self

    @allure.step("Проверка состояния окна")
    def verify_window_state(self, window_element, is_visible: bool = True):
        """
        Проверяет состояние окна (видно/скрыто).

        Args:
            window_element: Локатор элемента окна.
            is_visible: True (по умолчанию) — окно должно быть видно.
                        False — окно должно быть скрыто.
        """
        # Получаем читаемое описание элемента для логов и ошибок
        element_desc = str(window_element)

        if is_visible:
            with allure.step(f"Убеждаемся, что окно {element_desc} видимо"):
                try:
                    window_element.should(be.visible)
                except Exception as e:
                    raise AssertionError(
                        f"❌ Window {element_desc} is NOT visible, but it should be!\n"
                        f"   Expected: window to be visible on the screen.\n"
                        f"   Actual: window is hidden or missing."
                    ) from e
        else:
            with allure.step(f"Убеждаемся, что окно {element_desc} скрыто"):
                try:
                    window_element.should(be.hidden)
                except Exception as e:
                    raise AssertionError(
                        f"❌ Window {element_desc} is VISIBLE, but it should be hidden!\n"
                        f"   Expected: window to be closed/hidden.\n"
                        f"   Actual: window is still open on the screen."
                    ) from e

        return self

    @allure.step("Нажатие кнопки Index info и ожидание модалки")
    def click_index_info(self):
        """
        Нажимает кнопку открытия модального окна информации
        и ожидает появления модалки Scan Info.
        """
        with allure.step("Кликаем по кнопке Index info"):
            try:
                self.index_info_btn.should(be.visible).should(be.enabled)
                self.index_info_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Index info button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Index info!\n" f"   Error: {e}"
                ) from e

        with allure.step("Ожидаем появление модального окна Scan Info"):
            self.scan_info_modal.should(be.visible)

        return self

    @allure.step("Закрытие модалки добавления планеты")
    def close_add_planet_modal(
        self,
        click_cross: bool = False,
        click_cancel: bool = False,
    ):
        """
        Закрывает модалку выбора планеты одним из доступных способов.

        Args:
            click_cross: Клик по крестику (modal_close_btn).
            click_cancel: Клик по кнопке отмены (modal_cancel_btn).
        """
        # Проверяем, что выбран ровно один способ закрытия
        if sum([click_cross, click_cancel]) != 1:
            raise ValueError(
                "❌ Must specify exactly one close method (cross, cancel, or body)."
            )

        # 1. Клик по крестику
        if click_cross:
            with allure.step("Закрываем модалку кликом по крестику"):
                try:
                    self.add_modal_close_btn.click()
                except Exception as e:
                    raise AssertionError(
                        f"❌ Failed to click cross button (modal_close_btn)!\n"
                        f"   Error: {e}"
                    ) from e

        # 2. Клик по кнопке Cancel
        elif click_cancel:
            with allure.step("Закрываем модалку кликом по кнопке Cancel"):
                try:
                    self.add_modal_cancel_btn.click()
                except Exception as e:
                    raise AssertionError(
                        f"❌ Failed to click Cancel button (modal_cancel_btn)!\n"
                        f"   Error: {e}"
                    ) from e

        return self

    @allure.step("Закрытие модалки скан инфо")
    def close_index_info_modal(
        self,
        click_cross: bool = False,
        click_cancel: bool = False,
    ):
        """
        Закрывает модалку информации парамтеров одним из доступных способов.

        Args:
            click_cross: Клик по крестику (modal_close_btn).
            click_cancel: Клик по кнопке отмены (modal_cancel_btn).
        """
        # Проверяем, что выбран ровно один способ закрытия
        if sum([click_cross, click_cancel]) != 1:
            raise ValueError(
                "❌ Must specify exactly one close method (cross, cancel, or body)."
            )

        # 1. Клик по крестику
        if click_cross:
            with allure.step("Закрываем модалку кликом по крестику"):
                try:
                    self.scan_modal_close_btn.click()
                except Exception as e:
                    raise AssertionError(
                        f"❌ Failed to click cross button (modal_close_btn)!\n"
                        f"   Error: {e}"
                    ) from e

        # 2. Клик по кнопке Cancel
        elif click_cancel:
            with allure.step("Закрываем модалку кликом по кнопке Cancel"):
                try:
                    self.scan_modal_cancel_btn.click()
                except Exception as e:
                    raise AssertionError(
                        f"❌ Failed to click Cancel button (modal_cancel_btn)!\n"
                        f"   Error: {e}"
                    ) from e

        return self

    @allure.step("Закрытие модалки подтверждения удаления")
    def close_delete_confirmation_modal(
        self, click_cross: bool = False, click_cancel: bool = False
    ):
        """
        Универсальное закрытие модалок подтверждения удаления
        (например, 'Удалить все' или 'Удалить запись из архива').
        Локаторы кнопок идентичны, поэтому используем один метод.

        Args:
            click_cross: Клик по крестику.
            click_cancel: Клик по кнопке отмены.
        """
        # Проверяем, что выбран ровно один способ закрытия
        if sum([click_cross, click_cancel]) != 1:
            raise ValueError(
                "❌ Must specify exactly one close method (cross or cancel)."
            )

        # 1. Клик по крестику
        if click_cross:
            with allure.step("Закрываем модалку удаления кликом по крестику"):
                try:
                    self.delete_all_modal_close_btn.click()
                except Exception as e:
                    raise AssertionError(
                        f"❌ Failed to click cross button!\n" f"   Error: {e}"
                    ) from e

        # 2. Клик по кнопке Cancel
        elif click_cancel:
            with allure.step("Закрываем модалку удаления кликом по кнопке Cancel"):
                try:
                    self.delete_all_modal_cancel_btn.click()
                except Exception as e:
                    raise AssertionError(
                        f"❌ Failed to click Cancel button!\n" f"   Error: {e}"
                    ) from e

        return self

    @allure.step("Нажатие кнопки Clear all и ожидание модалки")
    def click_clear_all(self):
        """
        Нажимает кнопку 'Clear all'
        и ожидает появления модалки подтверждения удаления.
        """
        with allure.step("Кликаем по кнопке Clear all"):
            try:
                self.clear_all_btn.should(be.visible).should(be.enabled)
                self.clear_all_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Clear all button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking Clear all!\n" f"   Error: {e}"
                ) from e

        with allure.step("Ожидаем появление модального окна Delete clear all"):
            self.delete_confirm_clear_all_modal.should(be.visible)

        return self

    @allure.step("Закрытие модалки 'Детали'")
    def close_details_modal(
        self, click_cross: bool = False, click_cancel: bool = False
    ):
        """
        Закрытие модалки 'Детали' (Details) одним из доступных способов.

        Args:
            click_cross: Клик по крестику.
            click_cancel: Клик по кнопке отмены.
        """
        # Проверяем, что выбран ровно один способ закрытия
        if sum([click_cross, click_cancel]) != 1:
            raise ValueError(
                "❌ Must specify exactly one close method (cross or cancel)."
            )

        # 1. Клик по крестику
        if click_cross:
            with allure.step("Закрываем модалку 'Детали' кликом по крестику"):
                try:
                    self.details_modal_close_btn.click()
                except Exception as e:
                    raise AssertionError(
                        f"❌ Failed to click cross button!\n" f"   Error: {e}"
                    ) from e

        # 2. Клик по кнопке Cancel
        elif click_cancel:
            with allure.step("Закрываем модалку 'Детали' кликом по кнопке Cancel"):
                try:
                    self.details_modal_cancel_btn.click()
                except Exception as e:
                    raise AssertionError(
                        f"❌ Failed to click Cancel button!\n" f"   Error: {e}"
                    ) from e

        return self

    @allure.step("Нажатие кнопки DETAILS и ожидание модалки")
    def click_details_for_planet(self, planet_name: str):
        """
        Кликает по кнопке Details для конкретной планеты в архиве
        и ожидает появление модалки. Ищет кнопку по атрибуту data-planet.

        """

        with allure.step(f"Кликаем по кнопке DETAILS для планеты '{planet_name}'"):
            details_btn = browser.element(f'.action-btn[data-planet="{planet_name}"]')

            try:
                details_btn.should(be.visible).should(be.enabled)
                details_btn.click()
            except TimeoutException:
                raise AssertionError(
                    f"❌ DETAILS button for planet '{planet_name}' not found!\n"
                    f" Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Failed to click DETAILS button for planet '{planet_name}'!\n"
                    f" Error: {e}"
                ) from e

        with allure.step("Ожидаем появление модалки DETAILS"):
            self.details_modal.should(be.visible)

        return self

    @allure.step("Нажатие кнопки DELETE и ожидание модалки подтверждения удаления")
    def click_delete_for_planet(self, planet_name: str):
        """
        Кликает по кнопке DELETE для конкретной планеты в архиве
        и ожидает появление модалки удаления.
        Ищет кнопку по атрибуту data-planet.

        """

        with allure.step(f"Кликаем по кнопке DELETE для планеты '{planet_name}'"):
            delete_btn = browser.element(f'.delete-btn[data-planet="{planet_name}"]')

            try:
                delete_btn.should(be.visible).should(be.enabled)
                delete_btn.click()
            except TimeoutException:
                raise AssertionError(
                    f"❌ DELETE button for planet '{planet_name}' not found!\n"
                    f" Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Failed to click DELETE button for planet '{planet_name}'!\n"
                    f" Error: {e}"
                ) from e

        with allure.step("Ожидаем появление модалки подтверждения удаления"):
            self.delete_confirm_delete_modal.should(be.visible)

        return self

    @allure.step("Подтверждение удаления и ожидание закрытия модалки")
    def click_confirm_delete(
        self, delete_modal: bool = False, clear_all_modal: bool = False
    ):
        """
        Кликает по кнопке подтверждения удаления (DELETE/CLEAR ALL)
        и ожидает закрытия соотвествующей модалки.

        Args:
            delete_modal: Ожидать закрытие модалки удаления одной записи (delete_confirm_delete_modal).
            clear_all_modal: Ожидать закрытие модалки очистки всего архива (delete_confirm_clear_all_modal)
        """

        if sum([delete_modal, clear_all_modal]) != 1:
            raise ValueError(
                "❌ Must specify exactly one modal type (delete_modal or clear_modal)."
            )

        with allure.step("Кликаем по кнопке подтверждения удаления"):
            try:
                self.delete_all_modal_confirm_delete_btn.should(be.visible).should(
                    be.enabled
                )
                self.delete_all_modal_confirm_delete_btn.click()
            except TimeoutException:
                raise AssertionError(
                    "❌ Confirm delete button not found or not clickable!\n"
                    "   Timeout: button did not appear in time"
                )
            except Exception as e:
                raise AssertionError(
                    f"❌ Unexpected error while clicking confir, delete button!\n"
                    f"   Error: {e}"
                ) from e

        if delete_modal:
            with allure.step("Ожидаем закрытие модалки подтверждения удаления записи"):
                self.delete_confirm_delete_modal.should(be.hidden)

        elif clear_all_modal:
            with allure.step("Ожидаем закрытие модалки подтверждения удаления записи"):
                self.delete_confirm_clear_all_modal.should(be.hidden)

        return self

    # Хелпер для метода def validate_complete_cis_calculation
    def get_scan_parameter_element(self, param_name: str):
        """
        Возвращает локатор элемента значения параметра.
        Использует надежный атрибут data-param-key и contains() для классов.
        """
        # 1. Превращаем "HABITABLE ZONE" в "habitable_zone"
        param_key = param_name.lower().replace(" ", "_").strip()
        
        # 2. Используем contains(@class, 'param-row'), чтобы ловить и 'pending', и 'filled'
        xpath = (
            f"//div[contains(@class, 'param-row') and @data-param-key='{param_key}']"
            f"//div[contains(@class, 'param-value')]"
        )
        
        return browser.element((By.XPATH, xpath))

    @allure.step("Полная валидация результатов расчета CIS")
    def validate_complete_cis_calculation(
        self, 
        expected_score: str, 
        expected_status: str | None = None,  # ✅ Современный и чистый синтаксис
        expected_params: dict | None = None  # ✅ Тоже самое для словаря
    ):
        """
        Комплексная проверка результатов сканирования.
        Итоговый процент обязателен. Статус и параметры - опциональны.
        """
        # 1. Проверка итогового CIS Score (Всегда выполняется)
        with allure.step(f"Проверяем итоговый CIS Score: {expected_score}"):
            self.verify_text(self.cis_score, expected_score)

        # 2. Проверка статуса сканирования (Только если он передан)
        if expected_status is not None:
            with allure.step(f"Проверяем статус сканирования: {expected_status}"):
                self.verify_text(self.cis_status, expected_status)

        # 3. Проверка всех параметров в цикле (Только если словарь передан)
        if expected_params is not None:
            for param_name, expected_value in expected_params.items():
                with allure.step(f"Проверяем параметр '{param_name}': {expected_value}%"):
                    param_element = self.get_scan_parameter_element(param_name)
                    self.verify_text(param_element, expected_value)

        return self

    @allure.step("Проверка цвета полосы параметра (solid color)")
    def verify_param_bar_color(self, param_name: str, expected_rgb: str):
        """
        Проверяет цвет полосы .param-bar через JS.
        Учитывает, что цвет может быть задан через background-image (градиент), 
        box-shadow или background-color.
        """
        param_key = param_name.lower().replace(" ", "_")
        
        script = f"""
            const el = document.querySelector("div[data-param-key='{param_key}'] .param-bar");
            if (!el) return 'ELEMENT_NOT_FOUND';

            // 1. Проверяем background-image (так как часто используется linear-gradient)
            let bgImage = window.getComputedStyle(el).getPropertyValue('background-image');
            if (bgImage && bgImage !== 'none' && bgImage.includes('{expected_rgb}')) {{
                return bgImage;
            }}

            // 2. Проверяем box-shadow (иногда цвет задан там для свечения)
            let boxShadow = window.getComputedStyle(el).getPropertyValue('box-shadow');
            if (boxShadow && boxShadow !== 'none' && boxShadow.includes('{expected_rgb}')) {{
                return boxShadow;
            }}

            // 3. Проверяем background-color (на случай сплошного цвета)
            let bgColor = window.getComputedStyle(el).getPropertyValue('background-color');
            if (bgColor && bgColor !== 'rgba(0, 0, 0, 0)' && bgColor !== 'transparent') {{
                return bgColor;
            }}

            return 'NO_COLOR_FOUND';
        """
        
        actual_color = browser.driver.execute_script(script)
        
        assert expected_rgb in actual_color, (
            f"❌ Parameter bar color for '{param_name}' does not match!\n"
            f"   Expected to contain: {expected_rgb}\n"
            f"   Actual:   {actual_color}"
        )
        return self

    @allure.step("Проверка полосатого градиента (Star Radiation)")
    def verify_param_bar_is_striped(self, param_name: str, stripe_rgb: str):
        """
        Проверяет background-image (градиент) у .param-bar через JS.
        """
        param_key = param_name.lower().replace(" ", "_")
        
        script = (
            f"return window.getComputedStyle("
            f"document.querySelector(\"div[data-param-key='{param_key}'] .param-bar\")"
            f").getPropertyValue('background-image')"
        )
        
        actual_bg_image = browser.driver.execute_script(script)
        
        assert stripe_rgb in actual_bg_image, (
            f"❌ Striped gradient for '{param_name}' does not contain the expected color!\n"
            f"   Expected to contain: {stripe_rgb}\n"
            f"   Actual: {actual_bg_image}"
        )

    @allure.step("Проверка сортировки архива по убыванию CIS Score")
    def verify_archive_sorted_by_score_descending(self):
        """
        Проверяет, что записи в архиве отсортированы по убыванию CIS Score.
        Первая запись должна иметь наивысший процент.
        """
        # Берем элементы напрямую через Selenium драйвер (работает в любой версии Selene)
        web_elements = browser.driver.find_elements(By.CSS_SELECTOR, '.archive-row .cis-value')
        
        # У нативных Selenium WebElement свойство .text работает всегда
        scores = [
            float(el.text.replace('%', '').strip()) 
            for el in web_elements
        ]
        
        # Страховка: архив не должен быть пустым
        assert len(scores) > 0, (
            "❌ Archive is empty! Cannot verify sorting."
        )
        
        # Проверяем, что список равен самому себе, отсортированному по убыванию
        assert scores == sorted(scores, reverse=True), (
            f"❌ Archive is not sorted by CIS Score in descending order!\n"
            f"   Expected: {sorted(scores, reverse=True)}\n"
            f"   Actual:   {scores}"
        )
        return self

    @allure.step("Ожидание {seconds} сек.")
    def pause(self, seconds: float):
        """
        Универсальная пауза. 
        Элегантно ждет указанное количество секунд.
        """
        time.sleep(seconds)
        return self


    # endregion
