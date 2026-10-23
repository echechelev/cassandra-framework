import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🔄 Полный цикл расчёта и возврата на страницу")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.workflows
def test_voyager_flight_earth_to_mars(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать планету 'Earth' в поле Dep Planet.
    4. Выбрать систему "Sol" в поле Arr System.
    5. Выбрать планету 'Mars' в поле Arr Planet.
    6. Выбрать тип корабля 'Voyager (16 km/s)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется значение '0 years 6 months and 26 days'.
    9. Нажать на кнопку 'Dashboard'.
    10. Проверить: URL меняется на 'dashboard.html'.
    11. Нажать на кнопку 'Flight Calc'.
    12. Проверить: URL меняется на 'flight-calc.html'.
    13. Проверить: все поля пустые.
    14. Проверить: кнопки кораблей не нажаты.
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.EARTH_CALC_SELECT)
    flight_calc_page.select_arr_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.MARS_CALC_SELECT)
    flight_calc_page.select_ship(voyager=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_flight_time(years=0, months=6, days=26)

    # ⚡ ACT
    flight_calc_page.click_dashboard()

    # ✅ ASSERT
    flight_calc_page.wait_for_url(data.DASHBOARD_URL)

    # ⚡ ACT
    flight_calc_page.click_browser_back()

    # ✅ ASSERT
    flight_calc_page.wait_for_url(data.FLIGHT_CALC_URL)
    flight_calc_page.verify_form_cleared()
    flight_calc_page.verify_ship_selection_cleared()
