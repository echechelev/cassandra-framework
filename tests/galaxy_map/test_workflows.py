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
def test_full_system_exploration_cycle_with_return(galaxe_map_page):
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
    galaxe_map_page.click_star(galaxe_map_page.sun_btn)

    # ✅ ASSERT
    galaxe_map_page.wait_for_url(data.STAR_SUN_URL)

    # ⚡ ACT
    galaxe_map_page.click_galaxy_map()

    # ✅ ASSERT
    galaxe_map_page.wait_for_url(data.GALAXY_MAP_URL)
    galaxe_map_page.verify_text(
        element=galaxe_map_page.galaxy_title, expected_text=data.GALAXY_TITLE
    )
    galaxe_map_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_SELECT_STAR_SYSTEM_AURORA
    )