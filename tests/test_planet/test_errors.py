import allure
import pytest

from pages.planet import PlanetPage
from tests import data


@allure.id("CAS-01")
@allure.title("🚫 Редирект при отсутствии данных в sessionStorage")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.errors_ui
def test_access_denied_redirect_on_empty_storage():
    """
    Сценарий:
    1. Перейти на страницу planet.html?star=sun&planet=earth.
    2. Проверить: текст телеметрии становится красным и содержит '> ACCESS DENIED. REDIRECTING...'
    3. Проверить: через 1.5 сек происходит автоматический редирект на 'login.html'.
    """
    
    # ⚡ ACT
    planet = PlanetPage()
    planet.open_unauthenticated(data.PLANET_URL_SUN['earth'])
    
    # ✅ ASSERT
    planet.verify_telemetry_text(data.RED_TELEMETRY_ACCESS_DENIED)
    planet.verify_telemetry_color_with_cassandra(red=True)
    planet.wait_for_url(data.LOGIN_URL)


@allure.id("CAS-01")
@allure.title("🚫 Редирект при отсутствии данных в sessionStorage")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.errors_ui
def test_redirect_on_missing_planet_parameter(planet_page):
    """
    Сценарий:
    1. Перейти на страницу planet.html?star=sun (без &planet=).
    2. Проверить: URL после загрузки страницы.
    3. Проверить: через 1.5 сек происходит автоматический редирект на 'galaxy-map.html'.
    """
    # ⚡ ACT
    planet: PlanetPage = planet_page(data.PLANET_URL_SUN['no-planet'], expect_redirect=True)

    # ✅ ASSERT
    planet.wait_for_url(data.GALAXY_MAP_URL)