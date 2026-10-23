import allure
import pytest

from pages.flight_calc import FlightCalcPage
from tests import data


@allure.id("CAS-01")
@allure.title("🚫 Редирект при отсутствии данных в sessionStorage")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.errors_ui
def test_access_denied_redirect_on_empty_storage():
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Проверить: текст телеметрии становится красным и содержит '> ACCESS DENIED. REDIRECTING...'
    3. Проверить: через 1.5 сек происходит автоматический редирект на 'login.html'.
    """

    # ⚡ ACT
    flight_calc_page = FlightCalcPage()
    flight_calc_page.open_unauthenticated(data.FLIGHT_CALC_URL)

    # ✅ ASSERT
    flight_calc_page.verify_telemetry_text(data.RED_TELEMETRY_ACCESS_DENIED)
    flight_calc_page.verify_telemetry_color_with_cassandra(red=True)
    flight_calc_page.wait_for_url(data.LOGIN_URL)


@allure.id("CAS-02")
@allure.title("🚫 Валидация отсутствия выбора системы")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.errors_ui
def test_validate_empty_system_selection(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Не выбирать системы, выбрать корабль Вояджер.
    3. Кликнуть на data-wm-id="start-btn".
    4. Проверить: открывается Alert Modal с текстом "Please select both Departure and Arrival systems first.".
    """

    # ⚡ ACT
    flight_calc_page.select_ship(voyager=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_text(
        flight_calc_page.alert_modal, data.CALC_MODAL_SELECT_SYSTEMS
    )


@allure.id("CAS-03")
@allure.title("🚫 Валидация отсутствия выбора планеты")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.errors_ui
def test_validate_empty_planet_selection(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать систему "Sol" в поле Arr System.
    4. Кликнуть на кнопку 'Start'
    5. Проверить: открывается Alert Modal с текстом "Please select both Departure and Arrival planets.".
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_text(
        flight_calc_page.alert_modal, data.CALC_MODAL_SELECT_PLANETS
    )


@allure.id("CAS-04")
@allure.title("🚫 Валидация отсутствия выбора корабля")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.errors_ui
def test_validation_of_missing_vessel_selection(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать маршрут Earth → Mars..
    3. Не выбирая корабль, кликнуть на data-wm-id="start-btn".
    4. Проверить: открывается Alert Modal с текстом "Please select a Vessel Class."
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.EARTH_CALC_SELECT)
    flight_calc_page.select_arr_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.MARS_CALC_SELECT)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_text(
        flight_calc_page.alert_modal, data.CALC_MODAL_SELECT_VESSEL
    )


@allure.id("CAS-05")
@allure.title("⚠️ Попытка полета внутри системы Sol на Light Drive")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.errors_ui
def test_intra_system_sol_light_drive_warning(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать планету 'Earth' в поле Dep Planet.
    4. Выбрать систему "Sol" в поле Arr System.
    5. Выбрать планету 'Mars' в поле Arr Planet.
    6. Выбрать тип корабля 'Light Drive (0.1 c)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется модальное окно "Distance: 0.000031 light-years (minimum required: 1.0 ly)".
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.EARTH_CALC_SELECT)
    flight_calc_page.select_arr_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.MARS_CALC_SELECT)
    flight_calc_page.select_ship(light=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_text(
        flight_calc_page.warning_modal, data.CALC_MODAL_WARNING_EARTH_MARS
    )


@allure.id("CAS-06")
@allure.title("⚠️ Попытка полета внутри системы Sol на Warp Drive")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.errors_ui
def test_intra_system_sol_warp_drive_warning(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать планету 'Earth' в поле Dep Planet.
    4. Выбрать систему "Sol" в поле Arr System.
    5. Выбрать планету 'Mars' в поле Arr Planet.
    6. ВВыбрать тип корабля 'Warp Drive (0.5 c)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется модальное окно "Distance: 0.000031 light-years (minimum required: 1.0 ly)".
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.EARTH_CALC_SELECT)
    flight_calc_page.select_arr_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.MARS_CALC_SELECT)
    flight_calc_page.select_ship(warp=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_text(
        flight_calc_page.warning_modal, data.CALC_MODAL_WARNING_EARTH_MARS
    )
