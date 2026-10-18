import allure
import pytest

from pages.star_system import StarSystemPage
from tests import data


@allure.id("CAS-01")
@allure.title("🚫 Редирект при отсутствии данных в sessionStorage")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.errors_ui
def test_access_denied_redirect_on_empty_storage():
    """
    Сценарий:
    1. Перейти на страницу 'star-system.html'.
    2. Проверить: текст телеметрии становится красным и содержит '> ACCESS DENIED. REDIRECTING...'
    3. Проверить: через 1.5 сек происходит автоматический редирект на 'login.html'.
    """

    # ⚡ ACT
    star_page = StarSystemPage()
    star_page.open_unauthenticated(data.STAR_SYSTEM_URL['sun'])

    # ✅ ASSERT
    star_page.verify_telemetry_text(data.RED_TELEMETRY_ACCESS_DENIED)
    star_page.verify_telemetry_color_with_cassandra(red=True)
    star_page.wait_for_url(data.LOGIN_URL)


@allure.id("CAS-02")
@allure.title("🌌 Обработка отсутствующего параметра звезды")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-system")
@pytest.mark.regress
@pytest.mark.star_system
@pytest.mark.errors_ui
def test_redirect_on_missing_star_parameter(star_system):
    """
    Сценарий:
    1. Перейти на страницу star-system.html без параметра ?star=.
    2. Проверить: URL после загрузки страницы.
    3. Проверить: через 1.5 сек происходит автоматический редирект на 'galaxy-map.html'.
    """
    # ⚡ ACT
    star_page: StarSystemPage = star_system("sun")
    star_page.open_url(data.STAR_SYSTEM_URL['no-star'])

    # ✅ ASSERT
    star_page.wait_for_url(data.GALAXY_MAP_URL)

