import allure
import pytest
from selene import be

from pages.planet import PlanetPage
from tests import data


@allure.id("CAS-01")
@allure.title("🪐 Успешная загрузка Меркурия")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.interactions
def test_mercury_page_loads_successfully(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=sun&planet=mercury'.
    2. Проверить: URL равен 'planet.html?star=sun&planet=mercury'
    3. Проверить: название планеты: MERCURY.
    4. Проверить: текст телеметрии '> CASSANDRA: AURORA, MERCURY. DOWNLOADING PLANETARY METRICS...'
    5. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(
        data.PLANET_URL_SUN["mercury"], expect_redirect=True
    )

    # ✅ ASSERT
    planet.wait_for_url_strict("planet.html?star=sun&planet=mercury")
    planet.check_planet_name(data.MERCURY_NAME)
    planet.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_PLANET_MERCURY_METRICS
    )
    planet.star_system_btn.should(be.visible)


@allure.id("CAS-02")
@allure.title("🪐 Успешная загрузка Проксима Б")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.interactions
def test_proxima_b_page_loads_successfully(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=alpha-centauri-a&planet=proxima-b'.
    2. Проверить: URL равен 'planet.html?star=alpha-centaur-ai&planet=proxima-b'
    3. Проверить: название планеты: PROXIMA B.
    4. Проверить: текст телеметрии '> CASSANDRA: AURORA, PROXIMA B. DOWNLOADING PLANETARY METRICS...'
    5. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(
        data.PLANET_URL_ALPHA_CENTAURI_A["proxima-b"], expect_redirect=True
    )

    # ✅ ASSERT
    planet.wait_for_url_strict("planet.html?star=alpha-centauri-a&planet=proxima-b")
    planet.check_planet_name(data.PROXIMA_B_NAME)
    planet.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_PLANET_PROXIMA_B_METRICS
    )
    planet.star_system_btn.should(be.visible)


@allure.id("CAS-03")
@allure.title("🪐 Успешная загрузка Тау Кита Е")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.interactions
def test_tau_ceti_e_page_loads_successfully(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=tau-ceti&planet=tau-ceti-e'.
    2. Проверить: URL равен 'planet.html?star=tau-ceti&planet=tau-ceti-e'
    3. Проверить: название планеты: TAU CETI E.
    4. Проверить: текст телеметрии '> CASSANDRA: AURORA, TAU CETI E. DOWNLOADING PLANETARY METRICS...'
    5. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(
        data.PLANET_URL_TAU_CETI["tau-ceti-e"], expect_redirect=True
    )

    # ✅ ASSERT
    planet.wait_for_url_strict("planet.html?star=tau-ceti&planet=tau-ceti-e")
    planet.check_planet_name(data.TAU_CETI_E_NAME)
    planet.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_PLANET_TAU_CETI_E_METRICS
    )
    planet.star_system_btn.should(be.visible)


@allure.id("CAS-04")
@allure.title("🪐 Успешная загрузка Тау Кита Е")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.interactions
def test_epsilon_eridani_c_page_loads_successfully(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=epsilon-eridani&planet=epsilon-eridani-c'.
    2. Проверить: URL равен 'planet.html?star=epsilon-eridani&planet=epsilon-eridani-c'
    3. Проверить: название планеты: EPSILON ERIDANI C.
    4. Проверить: текст телеметрии '> CASSANDRA: AURORA, EPSILON ERIDANI C. DOWNLOADING PLANETARY METRICS...'
    5. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(
        data.PLANET_URL_EPSILON_ERIDANI["epsilon-eridani-c"], expect_redirect=True
    )

    # ✅ ASSERT
    planet.wait_for_url_strict("planet.html?star=epsilon-eridani&planet=epsilon-eridani-c")
    planet.check_planet_name(data.EPSILON_ERIDANI_C_NAME)
    planet.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_PLANET_EPSILON_ERIDANI_C_METRICS
    )
    planet.star_system_btn.should(be.visible)


@allure.id("CAS-05")
@allure.title("🪐 Успешная загрузка Тегарден Б")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.interactions
def test_teegarden_b_page_loads_successfully(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=teegarden&planet=teegarden-b'.
    2. Проверить: URL равен 'planet.html?star=teegarden&planet=teegarden-b'
    3. Проверить: название планеты: TEEGARDEN B.
    4. Проверить: текст телеметрии '> CASSANDRA: AURORA, TEEGARDEN B. DOWNLOADING PLANETARY METRICS...'
    5. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(
        data.PLANET_URL_TEEGARDEN["teegarden-b"], expect_redirect=True
    )

    # ✅ ASSERT
    planet.wait_for_url_strict("planet.html?star=teegarden&planet=teegarden-b")
    planet.check_planet_name(data.TEEGARDEN_B_NAME)
    planet.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_PLANET_TEEGARDEN_B_METRICS
    )
    planet.star_system_btn.should(be.visible)


@allure.id("CAS-06")
@allure.title("🪐 Успешная загрузка Траппист 1Б")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.interactions
def test_trappist_1b_page_loads_successfully(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=trappist-1&planet=trappist-1b'.
    2. Проверить: URL равен 'planet.html?star=trappist-1&planet=trappist-1b'
    3. Проверить: название планеты: TRAPPIST-1B.
    4. Проверить: текст телеметрии '> CASSANDRA: AURORA, TRAPPIST-1B. DOWNLOADING PLANETARY METRICS...'
    5. Проверить: кнопка Star System видна.
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(
        data.PLANET_URL_TRAPPIST_1["trappist-1b"], expect_redirect=True
    )

    # ✅ ASSERT
    planet.wait_for_url_strict("planet.html?star=trappist-1&planet=trappist-1b")
    planet.check_planet_name(data.TRAPPIST_1B_NAME)
    planet.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_PLANET_TRAPPIST_1B_METRICS
    )
    planet.star_system_btn.should(be.visible)


@allure.id("CAS-07")
@allure.title("☀️ Навигация на Звездную Систему Солнце с Меркурия")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.interactions
def test_navigate_to_sun_system_from_mercury(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=sun&planet=mercury'.
    2. Кликнуть: на кнопку 'Star System'
    3. Проверить: URL сменился на 'star-system.html?star=sun'
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(
        data.PLANET_URL_SUN["mercury"], expect_redirect=True
    )
    planet.click_star_system()

    # ✅ ASSERT
    planet.wait_for_url_strict("star-system.html?star=sun")


@allure.id("CAS-08")
@allure.title("🌟 Навигация на Звездную Систему Альфа Центавра А с Проксимы Б")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "planet")
@pytest.mark.regress
@pytest.mark.planet
@pytest.mark.interactions
def test_navigate_to_alpha_centauri_a_from_proxima_b(planet_page):
    """
    Сценарий:
    1. Перейти на страницу 'planet.html?star=alpha-centauri-a&planet=proxima-b'.
    2. Кликнуть: на кнопку 'Star System'
    3. Проверить: URL сменился на 'star-system.html?star=alpha-centauri-a.'
    """

    # ⚡ ACT
    planet: PlanetPage = planet_page(
        data.PLANET_URL_ALPHA_CENTAURI_A["proxima-b"], expect_redirect=True
    )
    planet.click_star_system()

    # ✅ ASSERT
    planet.wait_for_url_strict("star-system.html?star=alpha-centauri-a")



   
   
