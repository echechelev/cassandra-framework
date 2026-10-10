import allure
import pytest

from pages.star_system import StarSystemPage
from tests import data


@allure.id("CAS-01")
@allure.title("🌌 Валидация заголовка звездной системы")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.states
def test_star_system_title_validation(star_system):
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html?star=trappist-1'.
    2. Проверить текст заголовка 'STAR SYSTEM TRAPPIST-1'.
    """
    
    # ⚡ ACT
    star_page: StarSystemPage = star_system("trappist-1")

    # ✅ ASSERT
    star_page.verify_text(
        element=star_page.star_system_title,
        expected_text=data.STAR_SYSTEM_TRAPPIST_TITLE,
    )


@allure.id("CAS-02")
@allure.title("🌌 Валидация строки телеметрии")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.states
def test_telemetry_string_validation(star_system):
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html?star=sun'.
    2. Проверить текст телеметрии "AURORA, SCANNING SOL (SUN) SYSTEM... 6 PLANETS DETECTED. AWAITING SELECTION.".
    """
    # ⚡ ACT
    star_page: StarSystemPage = star_system("sun")

    # ✅ ASSERT
    star_page.verify_telemetry_text(
        expected_text=data.GREEN_TELEMETRY_SELECT_STAR_SYSTEM_SOL_AURORA
    )
