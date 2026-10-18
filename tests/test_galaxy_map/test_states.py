import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🌌 Валидация заголовка галактики")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "galaxy-map")
@pytest.mark.regress
@pytest.mark.galaxy_map
@pytest.mark.states
def test_galaxy_title_validation(galaxy_map_page):
    """
    Сценарий:
    1. Перейти на страницу 'Galaxy map Page'.
    2. Проверить текст заголовка 'GALAXY MILKY WAY'.
    """

    # ✅ ASSERT
    galaxy_map_page.verify_text(
        element=galaxy_map_page.galaxy_title, expected_text=data.GALAXY_TITLE
    )


@allure.id("CAS-02")
@allure.title("🌌 Валидация строки телеметрии")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "galaxy-map")
@pytest.mark.regress
@pytest.mark.galaxy_map
@pytest.mark.states
def test_telemetry_string_validation(galaxy_map_page):
    """
    Сценарий:
    1. Перейти на страницу 'Galaxy map Page'.
    2. Проверить текст телеметрии "SELECT A STAR SYSTEM FOR INVESTIGATION".
    """

    # ✅ ASSERT
    galaxy_map_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_SELECT_STAR_SYSTEM_AURORA
    )

