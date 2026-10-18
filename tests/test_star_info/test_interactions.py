import allure
import pytest
from selene import be

from pages.star_info import StarInfoPage
from tests import data


@allure.id("CAS-01")
@allure.title("☀️ Успешная загрузка Sagittarius A")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.interactions
def test_successful_sagittarius_a_loading(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=sagittarius-a'.
    2. Проверить: URL равен 'star-info.html?star=sagittarius-a'
    3. Проверить: отображается желтая звезда (.star-sphere.black-hole).
    4. Проверить: заголовок панели: BLACK HOLE SAGITTARIUS A*.
    5. Проверить: текст телеметрии '> CASSANDRA: AURORA, ANALYZING SAGITTARIUS A* DATA...'
    6. Проверить: кнопка Galaxy Map видна.
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["sagittarius-a"])

    # ✅ ASSERT
    star_page.verify_visual_class(data.SAGITTARIUS_A_CLASS)
    star_page.verify_text(
        star_page.tech_panel_type, expected_text=data.SAGITTARIUS_A_TYPE
    )
    star_page.verify_text(
        star_page.tech_panel_name, expected_text=data.SAGITTARIUS_A_NAME
    )
    star_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_STAR_INFO_SAGITTARIUS_A
    )
    star_page.galaxy_map_btn.should(be.visible)


@allure.id("CAS-02")
@allure.title("☀️ Успешная загрузка Солнца")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.interactions
def test_successful_sun_loading(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=sun'.
    2. Проверить: URL равен 'star-info.html?star=sun'
    3. Проверить: отображается желтая звезда (.star-sphere.sun).
    4. Проверить: заголовок панели: STAR SOL (THE SUN).
    5. Проверить: текст телеметрии '> CASSANDRA: AURORA, ANALYZING SOL (THE SUN) DATA...'
    6. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["sun"])

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-info.html?star=sun")
    star_page.verify_visual_class(data.SUN_CLASS)
    star_page.verify_text(star_page.tech_panel_type, expected_text=data.SUN_TYPE)
    star_page.verify_text(star_page.tech_panel_name, expected_text=data.SUN_NAME)
    star_page.verify_telemetry_text(expected_text=data.GREEN_TELEMETRY_STAR_INFO_SUN)
    star_page.star_system_btn.should(be.visible)


@allure.id("CAS-03")
@allure.title("⭐ Успешная загрузка Альфы Центавра А")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.interactions
def test_successful_alpha_centauri_a_loading(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=alpha-centauri'.
    2. Проверить: URL равен 'star-info.html?star=alpha-centauri'
    3. Проверить: отображается желтая звезда (.star-sphere.alpha).
    4. Проверить: заголовок панели: STAR SYSTEM ALPHA CENTAURI А.
    5. Проверить: текст телеметрии '> CASSANDRA: AURORA, ANALYZING ALPHA CENTAURI А DATA...'
    6. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["alpha-centauri"])

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-info.html?star=alpha-centauri")
    star_page.verify_visual_class(data.ALPHA_CENTAURI_CLASS)
    star_page.verify_text(
        star_page.tech_panel_type, expected_text=data.ALPHA_CENTAURI_TYPE
    )
    star_page.verify_text(
        star_page.tech_panel_name, expected_text=data.ALPHA_CENTAURI_NAME
    )
    star_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_STAR_INFO_ALPHA_CENTAURI
    )
    star_page.star_system_btn.should(be.visible)


@allure.id("CAS-04")
@allure.title("🌟 Успешная загрузка Эпсилон Эридана")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.interactions
def test_successful_epsilon_eridani_loading(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=epsilon-eridani'.
    2. Проверить: URL равен 'star-info.html?star=epsilon-eridani'
    3. Проверить: отображается желтая звезда (.star-sphere.epsilon).
    4. Проверить: заголовок панели: STAR EPSILON ERIDANI.
    5. Проверить: текст телеметрии '> CASSANDRA: AURORA, ANALYZING EPSILON ERIDANI DATA...'
    6. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["epsilon-eridani"])

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-info.html?star=epsilon-eridani")
    star_page.verify_visual_class(data.EPSILON_ERIDANI_CLASS)
    star_page.verify_text(
        star_page.tech_panel_type, expected_text=data.EPSILON_ERIDANI_TYPE
    )
    star_page.verify_text(
        star_page.tech_panel_name, expected_text=data.EPSILON_ERIDANI_NAME
    )
    star_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_STAR_INFO_EPSILON_ERIDANI
    )
    star_page.star_system_btn.should(be.visible)


@allure.id("CAS-05")
@allure.title("✨ Успешная загрузка Тау Кита")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.interactions
def test_successful_tau_ceti_loading(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=tau-ceti'.
    2. Проверить: URL равен 'star-info.html?star=tau-ceti'
    3. Проверить: отображается желтая звезда (.star-sphere.tau).
    4. Проверить: заголовок панели: STAR TAU CETI.
    5. Проверить: текст телеметрии '> CASSANDRA: AURORA, ANALYZING TAU CETI DATA...'
    6. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["tau-ceti"])

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-info.html?star=tau-ceti")
    star_page.verify_visual_class(data.TAU_CETI_CLASS)
    star_page.verify_text(star_page.tech_panel_type, expected_text=data.TAU_CETI_TYPE)
    star_page.verify_text(star_page.tech_panel_name, expected_text=data.TAU_CETI_NAME)
    star_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_STAR_INFO_TAU_CETI
    )
    star_page.star_system_btn.should(be.visible)


@allure.id("CAS-06")
@allure.title("🌠 Успешная загрузка Тигардена")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.interactions
def test_successful_teegarden_loading(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=teegarden'.
    2. Проверить: URL равен 'star-info.html?star=teegarden'
    3. Проверить: отображается желтая звезда (.star-sphere.teegarden).
    4. Проверить: заголовок панели: STAR TEEGARDEN'S.
    5. Проверить: текст телеметрии '> CASSANDRA: AURORA, ANALYZING TEEGARDEN'S DATA...'
    6. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["teegarden"])

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-info.html?star=teegarden")
    star_page.verify_visual_class(data.TEEGARDEN_CLASS)
    star_page.verify_text(star_page.tech_panel_type, expected_text=data.TEEGARDEN_TYPE)
    star_page.verify_text(star_page.tech_panel_name, expected_text=data.TEEGARDEN_NAME)
    star_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_STAR_INFO_TEEGARDEN
    )
    star_page.star_system_btn.should(be.visible)


@allure.id("CAS-07")
@allure.title("🪐 Успешная загрузка TRAPPIST-1")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.interactions
def test_successful_trappist_1_loading(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=trappist-1'.
    2. Проверить: URL равен 'star-info.html?star=trappist-1'
    3. Проверить: отображается желтая звезда (.star-sphere.trappist).
    4. Проверить: заголовок панели: STAR SYSTEM TRAPPIST-1.
    5. Проверить: текст телеметрии '> CASSANDRA: AURORA, ANALYZING TRAPPIST-1 DATA...'
    6. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["trappist-1"])

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-info.html?star=trappist-1")
    star_page.verify_visual_class(data.TRAPPIST_1_CLASS)
    star_page.verify_text(star_page.tech_panel_type, expected_text=data.TRAPPIST_1_TYPE)
    star_page.verify_text(star_page.tech_panel_name, expected_text=data.TRAPPIST_1_NAME)
    star_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_STAR_INFO_TRAPPIST_1
    )
    star_page.star_system_btn.should(be.visible)
    

@allure.id("CAS-08")
@allure.title("🌌 Навигация на Карту Галактики (для черной дыры)")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.interactions
def test_successful_navigation_to_galaxy_map_from_sagittarius_a(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=sagittarius-a'.
    2. Кликнуть на кнопку 'Galaxy Map'.
    3. Проверить: URL браузера изменяется на 'galaxy-map.html'.
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["sagittarius-a"])
    star_page.click_galaxy_map()

    # ✅ ASSERT
    star_page.wait_for_url(data.GALAXY_MAP_URL)


@allure.id("CAS-09")
@allure.title("🌟 Навигация на Звездную Систему (для звезды)")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.interactions
def test_successful_navigation_to_star_system_from_sun(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=sun'.
    2. Кликнуть на кнопку 'Star System'.
    3. Проверить: URL браузера изменяется на 'star-system.html?star=sun'.
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["sun"])
    star_page.click_star_system()

    # ✅ ASSERT
    star_page.wait_for_url_strict('star-system.html?star=sun')


@allure.id("CAS-10")
@allure.title("☄️ Валидация hover-эффекта кнопки Star System")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.interactions
def test_star_system_button_hover_effect_validation(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=sun'.
    2. Навести навести курсор на кнопку 'Star System'.
    3. Проверить: CSS-свойство transform содержит scale(1.10).
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["sun"])

    # ✅ ASSERT
    star_page.verify_hover_effects(star_page.star_system_btn, 'Star System', expected_scale=1.10)
