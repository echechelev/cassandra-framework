import allure
import pytest

from pages.planet import PlanetPage
from tests import data


@allure.id("CAS-01")
@allure.title("↩️ Полный цикл исследования планеты с возвратом")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.workflows
def test_full_planet_exploration_cycle_with_return(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=sun&planet=mercury'.
    2. Кликнуть на кнопку планеты "Star System".
    3. Проверить: URL браузера меняется на 'star-system.html?star=sun'.
    4. Кликнуть на кнопку 'Назад' в браузере
    5. Проверить: URL браузера меняется на 'planet.html?star=sun&planet=mercury'.
    6. Проверить: левая панель содержит PLANETARY METRICS - Mass: "0.055 M⊕".
    7. Проверить: левая панель содержит PLANETARY PROFILE - The smallest planet in the
    8. Проверить: правая панель содержит EXPLORATION STATUS - NO LANDINGS — Multiple flybys
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(data.PLANET_URL_SUN["mercury"], expect_redirect=True)
    planet.click_star_system()

    # ✅ ASSERT
    planet.wait_for_url_strict("star-system.html?star=sun")

    # ⚡ ACT
    planet.click_browser_back()

    # ✅ ASSERT
    planet.wait_for_url_strict("planet.html?star=sun&planet=mercury")
    planet.verify_tech_mass(data.MERCURY_MASS)
    planet.verify_info_description(data.MERCURY_PLANETARY_PROFILE)
    planet.verify_mission_status(data.MERCURY_EXPLORATION_STATUS)