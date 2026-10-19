import allure
import pytest

from pages.planet import PlanetPage
from tests import data


@allure.id("CAS-01")
@allure.title("📡 Валидация метрик для Меркурия")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.states
def test_mercury_panels(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=sun&planet=mercury'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит PLANETARY METRICS - Mass: "0.055 M⊕".
    4. Правая панель содержит PLANETARY PROFILE - 'The smallest planet in the'
    5. Правая панель содержит EXPLORATION STATUS - 'NO LANDINGS — Multiple flybys'
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(data.PLANET_URL_SUN["mercury"], expect_redirect=True)

    # ✅ ASSERT
    planet.verify_tech_mass(data.MERCURY_MASS)
    planet.verify_info_description(data.MERCURY_PLANETARY_PROFILE)
    planet.verify_mission_status(data.MERCURY_EXPLORATION_STATUS)


@allure.id("CAS-02")
@allure.title("📡 Валидация метрик для Проксима Б")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.states
def test_proxima_b_panels(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=alpha-centauri-a&planet=proxima-b'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит PLANETARY METRICS - Mass: "~1.2 M⊕".
    4. Правая панель содержит PLANETARY PROFILE - 'The closest known exoplanet'
    5. Правая панель содержит EXPLORATION STATUS - 'BEYOND REACH — Physical landing currently'
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(data.PLANET_URL_ALPHA_CENTAURI_A["proxima-b"], expect_redirect=True)

    # ✅ ASSERT
    planet.verify_tech_mass(data.PROXIMA_B_MASS)
    planet.verify_info_description(data.PROXIMA_B_PLANETARY_PROFILE)
    planet.verify_mission_status(data.PLANET_EXPLORATION_STATUS)


@allure.id("CAS-03")
@allure.title("📡 Валидация метрик для Тау Кита Е")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.states
def test_tau_ceti_e_panels(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=tau-ceti&planet=tau-ceti-e'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит PLANETARY METRICS - Mass: "~4.29 M⊕".
    4. Правая панель содержит PLANETARY PROFILE - 'A super-Earth located in the habitable zone'
    5. Правая панель содержит EXPLORATION STATUS - 'BEYOND REACH — Physical landing currently'
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(data.PLANET_URL_TAU_CETI["tau-ceti-e"], expect_redirect=True)

    # ✅ ASSERT
    planet.verify_tech_mass(data.TAU_CETI_E_MASS)
    planet.verify_info_description(data.TAU_CETI_E_PLANETARY_PROFILE)
    planet.verify_mission_status(data.PLANET_EXPLORATION_STATUS)


@allure.id("CAS-04")
@allure.title("📡 Валидация метрик для Эпсилона Эридани Ц")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.states
def test_epsilon_eridani_c_panels(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=epsilon-eridani&planet=epsilon-eridani-c'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит PLANETARY METRICS - Mass: "~248 M⊕".
    4. Правая панель содержит PLANETARY PROFILE - 'A massive gas giant orbiting Epsilon Eridani'
    5. Правая панель содержит EXPLORATION STATUS - 'BEYOND REACH — Physical landing currently'
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(data.PLANET_URL_EPSILON_ERIDANI["epsilon-eridani-c"], expect_redirect=True)

    # ✅ ASSERT
    planet.verify_tech_mass(data.EPSILON_ERIDANI_C_MASS)
    planet.verify_info_description(data.EPSILON_ERIDANI_C_PLANETARY_PROFILE)
    planet.verify_mission_status(data.PLANET_EXPLORATION_STATUS)


@allure.id("CAS-05")
@allure.title("📡 Валидация метрик для Эпсилона Тегарден Б")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.states
def test_teegarden_b_panels(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=teegarden&planet=teegarden-b'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит PLANETARY METRICS - Mass: "~1.05 M⊕".
    4. Правая панель содержит PLANETARY PROFILE - 'One of the most Earth-like exoplanets'
    5. Правая панель содержит EXPLORATION STATUS - 'BEYOND REACH — Physical landing currently'
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(data.PLANET_URL_TEEGARDEN["teegarden-b"], expect_redirect=True)

    # ✅ ASSERT
    planet.verify_tech_mass(data.TEEGARDEN_B_MASS)
    planet.verify_info_description(data.TEEGARDEN_B_PLANETARY_PROFILE)
    planet.verify_mission_status(data.PLANET_EXPLORATION_STATUS)


@allure.id("CAS-06")
@allure.title("📡 Валидация метрик для Эпсилона Траппист-1Б")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.states
def test_trappist_1b_panels(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=trappist-1&planet=trappist-1b'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит PLANETARY METRICS - Mass: "~1.02 M⊕".
    4. Правая панель содержит PLANETARY PROFILE - 'The innermost known planet'
    5. Правая панель содержит EXPLORATION STATUS - 'BEYOND REACH — Physical landing currently'
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(data.PLANET_URL_TRAPPIST_1["trappist-1b"], expect_redirect=True)

    # ✅ ASSERT
    planet.verify_tech_mass(data.TRAPPIST_1B_MASS)
    planet.verify_info_description(data.TRAPPIST_1B_PLANETARY_PROFILE)
    planet.verify_mission_status(data.PLANET_EXPLORATION_STATUS)