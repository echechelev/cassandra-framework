import allure
import pytest

from pages.star_system import StarSystemPage
from tests import data


@allure.id("CAS-01")
@allure.title("🌟 Успешная навигация к Солнцу и планетам")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.interactions
def test_successful_navigation_to_the_sun_and_planets(star_system):
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html?star=sun'.
    2. Проверить: URL звездной системы и название всех кнопок планет.
    3. Кликнуть на планету Меркурий.
    4. Проверить: URL браузера изменяется на 'planet.html?star=sun&planet=mercury'.
    """

    # ⚡ ACT
    star_page: StarSystemPage = star_system("sun")

    # ✅ ASSERT
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

    # ⚡ ACT
    star_page.click_planet(star_page.mercury_btn)

    # ✅ ASSERT
    star_page.wait_for_url_strict("planet.html?star=sun&planet=mercury")


@allure.id("CAS-02")
@allure.title("🌟 Успешная навигация к Альфе Центавра и планетам")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.interactions
def test_successful_navigation_to_alpha_centauri_and_planets(star_system):
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html?star=alpha-centauri'.
    2. Проверить: URL звездной системы и название всех кнопок планет.
    3. Кликнуть на кнопку планеты Проксима B.
    4. Проверить: URL браузера изменяется на 'planet.html?star=alpha-centauri&planet=proxima-b'.
    """

    # ⚡ ACT
    star_page: StarSystemPage = star_system("alpha-centauri")

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-system.html?star=alpha-centauri")
    star_page.check_button_content(
        button_id=data.PROXIMA_B_ID, expected_text=data.PROXIMA_B_NAME
    )
    star_page.check_button_content(
        button_id=data.PROXIMA_C_ID, expected_text=data.PROXIMA_C_NAME
    )
    star_page.check_button_content(
        button_id=data.PROXIMA_D_ID, expected_text=data.PROXIMA_D_NAME
    )

    # ⚡ ACT
    star_page.click_planet(star_page.proxima_b_btn)

    # ✅ ASSERT
    star_page.wait_for_url_strict("planet.html?star=alpha-centauri&planet=proxima-b")


@allure.id("CAS-03")
@allure.title("🌟 Успешная навигация к Эпсилон Эридана и планетам")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.interactions
def test_successful_navigation_to_epsilon_eridani_and_planets(star_system):
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html?star=epsilon-eridani'.
    2. Проверить: URL звездной системы и название всех кнопок планет.
    3. Кликнуть на кнопку планеты Эпсилон Эридана C.
    4. Проверить: URL браузера изменяется на 'planet.html?star=epsilon-eridani&planet=epsilon-eridani-c'.
    """

    # ⚡ ACT
    star_page: StarSystemPage = star_system("epsilon-eridani")

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-system.html?star=epsilon-eridani")
    star_page.check_button_content(
        button_id=data.EPSILON_ERIDANI_C_ID, expected_text=data.EPSILON_ERIDANI_C_NAME
    )

    # ⚡ ACT
    star_page.click_planet(star_page.epsilon_eridani_c_btn)

    # ✅ ASSERT
    star_page.wait_for_url_strict(
        "planet.html?star=epsilon-eridani&planet=epsilon-eridani-c"
    )


@allure.id("CAS-04")
@allure.title("🌟 Успешная навигация к Тау Кита и планетам")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.interactions
def test_successful_navigation_to_tau_ceti_and_planets(star_system):
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html?star=tau-ceti'.
    2. Проверить: URL звездной системы и название всех кнопок планет.
    3. Кликнуть на кнопку планеты Тау Кита e.
    4. Проверить: URL браузера изменяется на 'planet.html?star=tau-ceti&planet=tau-ceti-e'.
    """

    # ⚡ ACT
    star_page: StarSystemPage = star_system("tau-ceti")

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-system.html?star=tau-ceti")
    star_page.check_button_content(
        button_id=data.TAU_CETI_E_ID, expected_text=data.TAU_CETI_E_NAME
    )
    star_page.check_button_content(
        button_id=data.TAU_CETI_F_ID, expected_text=data.TAU_CETI_F_NAME
    )
    star_page.check_button_content(
        button_id=data.TAU_CETI_G_ID, expected_text=data.TAU_CETI_G_NAME
    )
    star_page.check_button_content(
        button_id=data.TAU_CETI_H_ID, expected_text=data.TAU_CETI_H_NAME
    )

    # ⚡ ACT
    star_page.click_planet(star_page.tau_ceti_e_btn)

    # ✅ ASSERT
    star_page.wait_for_url_strict("planet.html?star=tau-ceti&planet=tau-ceti-e")


@allure.id("CAS-05")
@allure.title("🌟 Успешная навигация к Тигарден и планетам")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.interactions
def test_successful_navigation_to_teegarden_and_planets(star_system):
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html?star=teegarden'.
    2. Проверить: URL звездной системы и название всех кнопок планет.
    3. Кликнуть на кнопку планеты Тигарден b.
    4. Проверить: URL браузера изменяется на 'planet.html?star=teegarden&planet=teegarden-b'.
    """

    # ⚡ ACT
    star_page: StarSystemPage = star_system("teegarden")

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-system.html?star=teegarden")
    star_page.check_button_content(
        button_id=data.TEEGARDEN_B_ID, expected_text=data.TEEGARDEN_B_NAME
    )
    star_page.check_button_content(
        button_id=data.TEEGARDEN_C_ID, expected_text=data.TEEGARDEN_C_NAME
    )

    # ⚡ ACT
    star_page.click_planet(star_page.teegarden_b_btn)

    # ✅ ASSERT
    star_page.wait_for_url_strict("planet.html?star=teegarden&planet=teegarden-b")


@allure.id("CAS-06")
@allure.title("🌟 Успешная навигация к TRAPPIST-1 и планетам")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.interactions
def test_successful_navigation_to_trappist_1_and_planets(star_system):
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html?star=trappist-1'.
    2. Проверить: URL звездной системы и название всех кнопок планет.
    3. Кликнуть на кнопку планеты TRAPPIST-1b.
    4. Проверить: URL браузера изменяется на 'planet.html?star=trappist-1&planet=trappist-1b'.
    """

    # ⚡ ACT
    star_page: StarSystemPage = star_system("trappist-1")

    # ✅ ASSERT
    star_page.wait_for_url_strict("star-system.html?star=trappist-1")
    star_page.check_button_content(
        button_id=data.TRAPPIST_1B_ID, expected_text=data.TRAPPIST_1B_NAME
    )
    star_page.check_button_content(
        button_id=data.TRAPPIST_1C_ID, expected_text=data.TRAPPIST_1C_NAME
    )
    star_page.check_button_content(
        button_id=data.TRAPPIST_1D_ID, expected_text=data.TRAPPIST_1D_NAME
    )
    star_page.check_button_content(
        button_id=data.TRAPPIST_1E_ID, expected_text=data.TRAPPIST_1E_NAME
    )
    star_page.check_button_content(
        button_id=data.TRAPPIST_1F_ID, expected_text=data.TRAPPIST_1F_NAME
    )
    star_page.check_button_content(
        button_id=data.TRAPPIST_1G_ID, expected_text=data.TRAPPIST_1G_NAME
    )
    star_page.check_button_content(
        button_id=data.TRAPPIST_1H_ID, expected_text=data.TRAPPIST_1H_NAME
    )

    # ⚡ ACT
    star_page.click_planet(star_page.trappist_1b_btn)

    # ✅ ASSERT
    star_page.wait_for_url_strict("planet.html?star=trappist-1&planet=trappist-1b")


@allure.id("CAS-07")
@allure.title("🌌 Успешная навигация на Карту Галактики")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.interactions
def test_successful_navigation_to_galaxy_map(star_system):
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html?star=sun'.
    2. Кликнуть на кнопку 'Galaxy Map'.
    3. Проверить: URL браузера изменяется на 'galaxy-map.html'.
    """

    # ⚡ ACT
    star_page: StarSystemPage = star_system("sun")
    star_page.click_galaxy_map()

    # ✅ ASSERT
    star_page.wait_for_url(data.GALAXY_MAP_URL)


@allure.id("CAS-08")
@allure.title("🌌 Валидация hover-эффекта кнопки планеты")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.interactions
def test_planet_button_hover_effect_validation(star_system):
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html?star=sun'.
    2. Навести навести курсор на data-wm-id='planet-earth-btn'.
    3. Проверить: CSS-свойство transform содержит scale(1.15).
    """

    # ⚡ ACT
    star_page: StarSystemPage = star_system("sun")

    # ✅ ASSERT
    star_page.verify_hover_effects(star_page.earth_btn, 'earth', expected_scale=1.15)

   
