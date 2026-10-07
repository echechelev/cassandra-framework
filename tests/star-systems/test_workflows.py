import allure
import pytest

from pages.star_system import StarSystemPage
from tests import data


@allure.id("CAS-01")
@allure.title("↩️ Полный цикл исследования планеты с возвратом")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.workflows
def test_full_planet_exploration_cycle_with_return(star_system):
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html?star=sun'.
    2. Кликнуть на кнопку планеты "Earth".
    3. Проверить: URL браузера меняется на 'planet.html?star=sun&planet=earth'.
    4. Кликнуть на кнопку 'Назад' в браузере
    5. Проверить: URL браузера меняется на 'star-system.html?star=sun'.
    6. Проверить: текст заголовка отображается корректно.
    7. Проверить: текст телеметрии отображается корректно.
    8. Проверить: кнопки планеты отображаются корректно.
    """

    # ⚡ ACT
    star_page: StarSystemPage = star_system("sun")
    star_page.click_planet(star_page.earth_btn)

    # ✅ ASSERT
    star_page.wait_for_url_strict("planet.html?star=sun&planet=earth")

    # ⚡ ACT
    star_page.click_browser_back()

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-system.html?star=sun")
    star_page.verify_text(
        element=star_page.star_system_title,
        expected_text=data.STAR_SYSTEM_SUN,
    )
    star_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_SELECT_STAR_SYSTEM_SOL_AURORA
    )
    star_page.wait_for_url_strict("star-system.html?star=sun")
    star_page.check_button_content(
        button_id=data.MERCURY_ID, expected_text=data.MERCURY_NAME
    )
    star_page.check_button_content(
        button_id=data.VENUS_ID, expected_text=data.VENUS_NAME
    )
    star_page.check_button_content(
        button_id=data.EARTH_ID, expected_text=data.EARTH_NAME
    )
    star_page.check_button_content(button_id=data.MARS_ID, expected_text=data.MARS_NAME)
    star_page.check_button_content(
        button_id=data.URANUS_ID, expected_text=data.URANUS_NAME
    )
    star_page.check_button_content(
        button_id=data.NEPTUNE_ID, expected_text=data.NEPTUNE_NAME
    )
    
    
