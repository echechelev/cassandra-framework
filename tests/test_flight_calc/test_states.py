import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🚀 Расчет полета Земля - Марс на Voyager")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.states
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


@allure.id("CAS-02")
@allure.title("🚀 Расчет полета Земля - Proxima b на Parker Probe")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.states
def test_parker_probe_flight_earth_to_proxima_b(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать планету 'Earth' в поле Dep Planet.
    4. Выбрать систему "Alpha Centauri А" в поле Arr System.
    5. Выбрать планету 'Proxima b' в поле Arr Planet.
    6. Выбрать тип корабля 'Parker Probe (197 km/s)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется значение '7678 years 4 months and 0 days'.
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.EARTH_CALC_SELECT)
    flight_calc_page.select_arr_system(data.ALPHA_CENTAURI_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.PROXIMA_B_CALC_SELECT)
    flight_calc_page.select_ship(parker=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_flight_time(years=7678, months=4, days=0)


@allure.id("CAS-03")
@allure.title("🚀 Расчет полета Земля - Proxima b на Warp Drive")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.states
def ttest_warp_drive_flight_earth_to_proxima_b(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать планету 'Earth' в поле Dep Planet.
    4. Выбрать систему "Alpha Centauri А" в поле Arr System.
    5. Выбрать планету 'Proxima b' в поле Arr Planet.
    6. Выбрать тип корабля 'Warp Drive (0.5 c)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется значение '10 years 1 month and 2 days'.
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.EARTH_CALC_SELECT)
    flight_calc_page.select_arr_system(data.ALPHA_CENTAURI_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.PROXIMA_B_CALC_SELECT)
    flight_calc_page.select_ship(warp=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_flight_time(years=10, months=1, days=2)


@allure.id("CAS-04")
@allure.title("🚀 Расчет полета Земля - Tau Ceti e на Voyager")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.states
def test_voyager_flight_earth_to_tau_ceti_e(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать планету '' в поле Dep Planet.
    4. Выбрать систему "Tau Ceti" в поле Arr System.
    5. Выбрать планету 'Tau Ceti е' в поле Arr Planet.
    6. Выбрать тип корабля 'Voyager (16 km/s)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется значение '257445 years 10 months and 18 days'.
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.EARTH_CALC_SELECT)
    flight_calc_page.select_arr_system(data.TAU_CETI_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.TAU_CETI_E_CALC_SELECT)
    flight_calc_page.select_ship(voyager=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_flight_time(years=257445, months=10, days=18)


@allure.id("CAS-05")
@allure.title("🚀 Расчет полета Земля - Tau Ceti e на Light Drive")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.states
def test_light_drive_flight_earth_to_tau_ceti_e(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать планету 'Earth' в поле Dep Planet.
    4. Выбрать систему "Tau Ceti" в поле Arr System.
    5. Выбрать планету 'Tau Ceti е' в поле Arr Planet.
    6. Выбрать тип корабля 'Light Drive (0.1 c)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется значение '137 years 4 months and 23 days'.
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.EARTH_CALC_SELECT)
    flight_calc_page.select_arr_system(data.TAU_CETI_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.TAU_CETI_E_CALC_SELECT)
    flight_calc_page.select_ship(light=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_flight_time(years=137, months=4, days=23)


@allure.id("CAS-06")
@allure.title("🚀 Расчет полета Земля - TRAPPIST-1e на Warp Drive")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.states
def test_warp_drive_flight_earth_to_trappist_1e(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать планету 'Earth' в поле Dep Planet.
    4. Выбрать систему "TRAPPIST-1" в поле Arr System.
    5. Выбрать планету 'TRAPPIST-1е' в поле Arr Planet.
    6. Выбрать тип корабля 'Warp Drive (0.5 c)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется значение '91 years 9 months and 27 days'.
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.EARTH_CALC_SELECT)
    flight_calc_page.select_arr_system(data.TRAPPIST_1_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.TRAPPIST_1E_CALC_SELECT)
    flight_calc_page.select_ship(warp=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_flight_time(years=91, months=9, days=27)


@allure.id("CAS-07")
@allure.title("🚀 Расчет полета Землa - Солнцe на Voyager")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.states
def test_voyager_flight_earth_to_sun(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать планету 'Earth' в поле Dep Planet.
    4. Выбрать систему "Sol" в поле Arr System.
    5. Выбрать звезду 'Sun' в поле Arr Planet.
    6. Выбрать тип корабля 'Voyager (16 km/s)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется значение '0 years 9 months and 9 days'.
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.EARTH_CALC_SELECT)
    flight_calc_page.select_arr_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.SUN_CALC_SELECT)
    flight_calc_page.select_ship(voyager=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_flight_time(years=0, months=9, days=9)


@allure.id("CAS-08")
@allure.title("🚀 Расчет полета Солнце - Земля на Voyadger")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.states
def test_voyager_flight_sun_to_earth(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать звезду 'Sun' в поле Dep Planet.
    4. Выбрать систему "Sol" в поле Arr System.
    5. Выбрать планету 'Earth' в поле Arr Planet.
    6. Выбрать тип корабля 'Voyager (16 km/s)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется значение '0 years 9 month and 9 days'.
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.SUN_CALC_SELECT)
    flight_calc_page.select_arr_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.EARTH_CALC_SELECT)
    flight_calc_page.select_ship(voyager=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_flight_time(years=0, months=9, days=9)


@allure.id("CAS-09")
@allure.title("🚀 Расчет полета Солнце - Уран на Voyager")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.states
def test_voyager_flight_sun_to_uranus(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать звезду 'Sun' в поле Dep Planet.
    4. Выбрать систему "Sol" в поле Arr System.
    5. Выбрать планету 'Uranus' в поле Arr Planet.
    6. Выбрать тип корабля 'Voyager (16 km/s)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется значение '8 years 5 months and 6 days'.
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.SUN_CALC_SELECT)
    flight_calc_page.select_arr_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.URANUS_CALC_SELECT)
    flight_calc_page.select_ship(voyager=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_flight_time(years=8, months=5, days=6)


@allure.id("CAS-10")
@allure.title("🚀 Расчет полета Солнце - Теегарден на Light Drive")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "flight-calc")
@pytest.mark.regress
@pytest.mark.flight_calc
@pytest.mark.states
def test_voyager_flight_sun_to_teegarden(flight_calc_page):
    """
    Сценарий:
    1. Перейти на страницу 'Flight calc page'.
    2. Выбрать систему "Sol" в поле Dep System.
    3. Выбрать звезду 'Sun' в поле Dep Planet.
    4. Выбрать систему "Teegarden" в поле Arr System.
    5. Выбрать звезду 'Teegarden' в поле Arr Planet.
    6. Выбрать тип корабля 'Voyager (16 km/s)'.
    7. Нажать кнопку 'Start'.
    8. Проверить: в выдаче появляется значение '8 years 5 months and 6 days'.
    """

    # ⚡ ACT
    flight_calc_page.select_dep_system(data.SOL_CALC_ID_SYSTEM)
    flight_calc_page.select_dep_planet(data.SUN_CALC_SELECT)
    flight_calc_page.select_arr_system(data.TEEGARDEN_CALC_ID_SYSTEM)
    flight_calc_page.select_arr_planet(data.TEEGARDEN_CALC_SELECT)
    flight_calc_page.select_ship(light=True)
    flight_calc_page.click_start_calc()

    # ✅ ASSERT
    flight_calc_page.verify_flight_time(years=143, months=4, days=25)
