import allure
import pytest
from selene import be

from pages.star_info import StarInfoPage
from tests import data


@allure.id("CAS-01")
@allure.title("↩️ Полный цикл исследования звезды с возвратом")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.workflows
def test_full_star_exploration_cycle_with_return(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=sun'.
    2. Кликнуть на кнопку планеты "Star System".
    3. Проверить: URL браузера меняется на 'star-system.html?star=sun'.
    4. Кликнуть на кнопку 'Назад' в браузере
    5. Проверить: URL браузера меняется на 'star-info.html?star=sun'.
    6. Проверить: текст заголовка левой панели отображается корректно.
    7. Проверить: текст заголовка правой панели отображается корректно.
    8. Проверить: текст телеметрии отображается корректно.
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["sun"])
    star_page.click_star_system()

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-system.html?star=sun")

    # ⚡ ACT
    star_page.click_browser_back()

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-info.html?star=sun")
    star_page.verify_text(star_page.tech_panel_type, expected_text=data.SUN_TYPE)
    star_page.verify_text(star_page.tech_panel_name, expected_text=data.SUN_NAME)
    star_page.verify_telemetry_text(expected_text=data.GREEN_TELEMETRY_STAR_INFO_SUN)
    star_page.star_system_btn.should(be.visible)

    
