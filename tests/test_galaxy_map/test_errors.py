import allure
import pytest

from pages.galaxy_map import GalaxyMapPage
from tests import data


@allure.id("CAS-01")
@allure.title("🚫 Редирект при отсутствии данных в sessionStorage")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "galaxy-map")
@pytest.mark.regress
@pytest.mark.galaxy_map
@pytest.mark.errors_ui
def test_access_denied_redirect_on_empty_storage():
    """
    Сценарий:
    1. Перейти на страницу 'Galaxy map Page'.
    2. Проверить: текст телеметрии становится красным и содержит '> ACCESS DENIED. REDIRECTING...'
    3. Проверить: через 1.5 сек происходит автоматический редирект на 'login.html'.
    """

    # ⚡ ACT
    galaxy_map_page = GalaxyMapPage()
    galaxy_map_page.open_unauthenticated(data.GALAXY_MAP_URL)

    # ✅ ASSERT
    galaxy_map_page.verify_telemetry_text(data.RED_TELEMETRY_ACCESS_DENIED)
    galaxy_map_page.verify_telemetry_color_with_cassandra(red=True)
    galaxy_map_page.wait_for_url(data.LOGIN_URL)