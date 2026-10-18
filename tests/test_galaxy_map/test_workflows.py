import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🔄 Полный цикл исследования системы с возвратом")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "galaxy-map")
@pytest.mark.regress
@pytest.mark.galaxy_map
@pytest.mark.workflows
def test_full_system_exploration_cycle_with_return(galaxy_map_page):
    """
    Сценарий:
    1. Перейти на страницу 'Galaxy map Page'.
    2. Кликнуть на кнопку звезду "Sun".
    3. Проверить: URL сменился на 'star-system.html?star=sun'.
    4. Кликнуть на кнопку "Galaxy Map".
    5. Проверить: URL сменился на 'galaxy-map.html'.
    6. Проверить: тест заголовка не изменился.
    7. Проверить: текст телеметрии не изменился.
  
    """

    # ⚡ ACT
    galaxy_map_page.click_star(galaxy_map_page.sun_btn)

    # ✅ ASSERT
    galaxy_map_page.wait_for_url(data.STAR_SYSTEM_URL['sun'])

    # ⚡ ACT
    galaxy_map_page.click_galaxy_map()

    # ✅ ASSERT
    galaxy_map_page.wait_for_url(data.GALAXY_MAP_URL)
    galaxy_map_page.verify_text(
        element=galaxy_map_page.galaxy_title, expected_text=data.GALAXY_TITLE
    )
    galaxy_map_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_SELECT_STAR_SYSTEM_AURORA
    )