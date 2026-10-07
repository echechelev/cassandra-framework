import allure
import pytest
from selene import browser

from tests import data

STAR_SYSTEM = [
    (
        "CAS-02",
        browser.element('[data-wm-id="star-sun-btn"]'),
        "star-system.html?star=sun",
        "Солнце",
    ),
    (
        "CAS-03",
        browser.element('[data-wm-id="star-alpha-centauri-btn"]'),
        "star-system.html?star=alpha-centauri",
        "Альфа Центавра",
    ),
    (
        "CAS-04",
        browser.element('[data-wm-id="star-epsilon-eridani-btn"]'),
        "star-system.html?star=epsilon",
        "Эпсилон",
    ),
    (
        "CAS-05",
        browser.element('[data-wm-id="star-tau-ceti-btn"]'),
        "star-system.html?star=tau-ceti",
        "Тау Кети",
    ),
    (
        "CAS-06",
        browser.element('[data-wm-id="star-teegarden-btn"]'),
        "star-system.html?star=teegarden",
        "Тригарден",
    ),
    (
        "CAS-07",
        browser.element('[data-wm-id="star-trappist-1-btn"]'),
        "star-system.html?star=trappist",
        "Триапсисит",
    ),
]


@allure.id("CAS-01")
@allure.title("🕳️ Успешная навигация к Чёрной дыре")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "galaxy-map")
@pytest.mark.regress
@pytest.mark.galaxy_map
@pytest.mark.interactions
def test_successful_navigation_to_black_hole(galaxy_map_page):
    """
    Сценарий:
    1. Перейти на страницу 'Galaxy map Page'.
    2. Кликнуть на 'Black_hole'.
    3. Проверить: URL браузера изменяется на black-hole.html.
    """

    # ⚡ ACT
    galaxy_map_page.click_black_hole()

    # ✅ ASSERT
    galaxy_map_page.wait_for_url_strict('star-info.html?star=black-hole')


@allure.id("CAS-01-CAS-07")
@allure.title("🌌 Успешная навигация к звёздной системе")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "galaxy-map")
@pytest.mark.regress
@pytest.mark.galaxy_map
@pytest.mark.interactions
@pytest.mark.parametrize("cas_id, btn, expected_url, star_name", STAR_SYSTEM)
def test_successful_navigation_to_a_star_system(
    cas_id, galaxy_map_page, btn, expected_url, star_name
):
    allure.dynamic.id(cas_id)
    allure.dynamic.title(f"🌌 Успешная навигация к звёздной системе: {star_name}")

    """
    Сценарий:
    1. Перейти на страницу 'Galaxy map Page'.
    2. Кликнуть на каждую кнопку "Star" 
    3. Проверить: URL браузера изменяется на выбранную звезду
    """

    # ⚡ ACT
    galaxy_map_page.click_star(btn)

    # ✅ ASSERT
    galaxy_map_page.wait_for_url(expected_url_part=expected_url)


@allure.id("CAS-08")
@allure.title("🕹️ Успешная навигация на Dashboard")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "galaxy-map")
@pytest.mark.regress
@pytest.mark.galaxy_map
@pytest.mark.interactions
def test_successful_navigation_to_dashboard(galaxy_map_page):
    """
    Сценарий:
    1. Перейти на страницу 'Galaxy map Page'.
    2. Кликнуть на кнопку "Dashboard".
    3. Проверить: URL браузера изменяется на dashboard.html.
    """

    # ⚡ ACT
    galaxy_map_page.click_dashboard()

    # ✅ ASSERT
    galaxy_map_page.wait_for_url(data.DASHBOARD_URL)


@allure.id("CAS-09")
@allure.title("🧬 Успешная навигация к CIS Index Table")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "galaxy-map")
@pytest.mark.regress
@pytest.mark.galaxy_map
@pytest.mark.interactions
def test_successful_navigation_to_cis_index_table(galaxy_map_page):
    """
    Сценарий:
    1. Перейти на страницу 'Galaxy map Page'.
    2. Кликнуть на кнопку "Cis index table".
    3. Проверить: URL браузера изменяется на cis-index-table.html.
    """

    # ⚡ ACT
    galaxy_map_page.click_cis_index_table()

    # ✅ ASSERT
    galaxy_map_page.wait_for_url(data.CIS_INDEX_TABLE_URL)


@allure.id("CAS-10")
@allure.title("✨ Валидация hover-эффекта кнопки звезды")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "galaxy-map")
@pytest.mark.regress
@pytest.mark.galaxy_map
@pytest.mark.interactions
def test_star_button_hover_effect_validation(galaxy_map_page):
    """
    Сценарий:
    1. Перейти на страницу 'Galaxy map Page'.
    2. С помощью ActionChains навести курсор на data-wm-id='star-sun-btn'.
    3. Проверить: CSS-свойство transform содержит scale(1.15).
    """

    # ✅ ASSERT
    galaxy_map_page.verify_hover_effects(
        galaxy_map_page.sun_btn, "sun", expected_scale=1.15
    )
