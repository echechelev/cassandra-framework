import allure
import pytest

from pages.star_info import StarInfoPage
from tests import data


@allure.id("CAS-01")
@allure.title("🕳️ Валидация левой и правой панелей для Sagittarius A")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.states
def test_sagittarius_a_panels(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=sagittarius-a'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит Classification: 'Supermassive Black Hole (SMBH).
    4. Правая панель содержит Description: 'This supermassive object ...'
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["sagittarius-a"])

    # ✅ ASSERT
    star_page.verify_tech_classification(data.SAGITTARIUS_A_CLASSIFICATION)
    star_page.verify_info_description(data.SAGITTARIUS_A_DESCRIPTION)


@allure.id("CAS-02")
@allure.title("☀️ Валидация левой и правой панелей для Солнца")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.states
def test_sun_panels(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=sun'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит Classification: 'G-type Yellow Dwarf.
    4. Правая панель содержит Description: 'The central star of our planetary system...'
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["sun"])

    # ✅ ASSERT
    star_page.verify_tech_classification(data.SUN_CLASSIFICATION)
    star_page.verify_info_description(data.SUN_DESCRIPTION)


@allure.id("CAS-03")
@allure.title("⭐ Валидация левой и правой панелей для Альфы Центавра А")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.states
def test_alpha_centauri_a_panels(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=alpha-centauri'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит Classification: 'Triple Star System'.
    4. Правая панель содержит Description: 'The closest star system to our Solar System...'
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["alpha-centauri"])

    # ✅ ASSERT
    star_page.verify_tech_classification(data.ALPHA_CENTAURI_CLASSIFICATION)
    star_page.verify_info_description(data.ALPHA_CENTAURI_DESCRIPTION)


@allure.id("CAS-04")
@allure.title("🌟 Валидация левой и правой панелей для Эпсилон Эридана")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.states
def test_epsilon_eridani_panels(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=epsilon-eridani'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит Classification: 'K-type Orange Dwarf'.
    4. Правая панель содержит Description: 'A young orange dwarf star located ...'
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["epsilon-eridani"])

    # ✅ ASSERT
    star_page.verify_tech_classification(data.EPSILON_ERIDANI_CLASSIFICATION)
    star_page.verify_info_description(data.EPSILON_ERIDANI_DESCRIPTION)


@allure.id("CAS-05")
@allure.title("✨ Валидация левой и правой панелей для Тау Кита")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.states
def test_tau_ceti_panels(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=tau-ceti'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит Classification: 'G-type Yellow Dwarf'.
    4. Правая панель содержит Description: 'A stable, metal-poor yellow dwarf...'
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["tau-ceti"])

    # ✅ ASSERT
    star_page.verify_tech_classification(data.TAU_CETI_CLASSIFICATION)
    star_page.verify_info_description(data.TAU_CETI_DESCRIPTION)


@allure.id("CAS-06")
@allure.title("🌠 Валидация левой и правой панелей для Звезды Тигардена")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.states
def test_teegarden_panels(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=teegarden'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит Classification: 'M-type Ultra-Cool Dwarf'.
    4. Правая панель содержит Description: 'An extremely faint ultra-cool red dwarf, one of the ...'
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["teegarden"])

    # ✅ ASSERT
    star_page.verify_tech_classification(data.TEEGARDEN_CLASSIFICATION)
    star_page.verify_info_description(data.TEEGARDEN_DESCRIPTION)


@allure.id("CAS-07")
@allure.title("🪐 Валидация левой и правой панелей для TRAPPIST-1")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.states
def test_trappist_1_panels(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=trappist-1'.
    2. Проверить текстовое содержимое левой и правой панели.
    3. Левая панель содержит Classification: 'Ultra-Cool Planetary Dwarf'.
    4. Правая панель содержит Description: 'An extraordinary ultra-cool red dwarf...'
    """

    # ⚡ ACT
    star_page: StarInfoPage = star_info_page(data.STAR_INFO_URL["trappist-1"])

    # ✅ ASSERT
    star_page.verify_tech_classification(data.TRAPPIST_1_CLASSIFICATION)
    star_page.verify_info_description(data.TRAPPIST_1_DESCRIPTION)
