import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🚀 Успешная инициализация и зависимые селекты в секции отправление")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.interactions
def test_successful_initialization_and_dependent_dropdowns_in_departure(
    flight_calc_page,
):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Проверить: в инпуте поля 'Dep Planet', видна планета 'Earth'
    4. Проверить: в инпуте поля 'Dep Planet', не видна планета 'Proxima b'
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)

    # ✅ ASSERT
    flight_calc_page.verify_dep_planets_populated(
        system_id=data.SOL_CALC_ID_SYSTEM,
        expected_planet_id=data.EARTH_CALC_SELECT,
        unexpected_planet_id=data.PROXIMA_B_CALC_SELECT,
    )


@allure.id("CAS-02")
@allure.title("🛬 Успешная инициализация и зависимые селекты в секции прибытия")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.interactions
def test_successful_initialization_and_dependent_dropdowns_in_arrival(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "TRAPPIST-1" в поле Arr System.
    3. Проверить: в инпуте поля 'Arr Planet', видна планета 'TRAPPIST-1H'
    4. Проверить: в инпуте поля 'Arr Planet', не видна планета 'TAU CETI F'
    """

    # ⚡ ACT
    flight_calc_page.select_arr_system(data.TRAPPIST_1_CALC_ID_SYSTEM)

    # ✅ ASSERT
    flight_calc_page.verify_arr_planets_populated(
        system_id=data.TRAPPIST_1_CALC_ID_SYSTEM,
        expected_planet_id=data.TRAPPIST_1H_CALC_SELECT,
        unexpected_planet_id=data.TAU_CETI_F_CALC_SELECT,
    )


@allure.id("CAS-03")
@allure.title("🧹 Успешный сброс формы (Clear)")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.interactions
def test_verify_successful_form_clear(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать планету 'Mars' в поле 'Dep Planet'.
    4. Выбрать систему "Tay Ceti" в поле Arr System.
    5. Выбрать планету 'Tay Ceti F' в поле 'Arr Planet'.
    6. ВЫбрать корабль "Voyager".
    7. Нажать на кнопку "Clear"
    8. Проверить: все селекты полей сброшены на "— Select.
    9. Проверить: радио-кнопка снята.
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.MARS_CALC_SELECT)
    flight_calc_page.select_arr_system(data.TAU_CETI_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.TAU_CETI_F_CALC_SELECT)
    flight_calc_page.select_ship(voyager=True)
    flight_calc_page.click_clear()

    # ✅ ASSERT
    flight_calc_page.verify_form_cleared()
    flight_calc_page.verify_ship_selection_cleared()


@allure.id("CAS-04")
@allure.title("ℹ️ Открытие модального окна Info")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.interactions
def test_opening_info_modal(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Кликнуть на кнопку 'Info'.
    3. Проверить: открывается модальное окно, виден заголовок "Flight Calculation Methodology".
    """

    # ⚡ ACT
    flight_calc_page.click_info()

    # ✅ ASSERT
    flight_calc_page.verify_text(
        flight_calc_page.info_modal, expected_text=data.CALC_MODAL_INFO
    )
