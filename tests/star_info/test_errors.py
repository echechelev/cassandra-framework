import allure
import pytest

from pages.star_info import StarInfoPage
from tests import data


@allure.id("CAS-01")
@allure.title("🚫 Редирект при отсутствии данных в sessionStorage")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.errors_ui
def test_access_denied_redirect_on_empty_storage():
    """
    Сценарий:
    1. Перейти на страницу 'star-info.html?star=sun'.
    2. Проверить: текст телеметрии становится красным и содержит '> ACCESS DENIED. REDIRECTING...'
    3. Проверить: через 1.5 сек происходит автоматический редирект на 'login.html'.
    """

    # ⚡ ACT
    star_info = StarInfoPage()
    star_info.open_unauthenticated(data.STAR_INFO_URL['sun'])

  
    # ✅ ASSERT
    star_info.verify_telemetry_text(data.RED_TELEMETRY_ACCESS_DENIED)
    star_info.verify_telemetry_color_with_cassandra(red=True)
    star_info.wait_for_url(data.LOGIN_URL)


@allure.id("CAS-02")
@allure.title("🌌 Обработка отсутствующего параметра звезды")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "star-info")
@pytest.mark.regress
@pytest.mark.star_info
@pytest.mark.errors_ui
def test_redirect_on_missing_star_parameter(star_info_page):
    """
    Сценарий:
    1. Перейти на страницу star-info.html без параметра ?star=.
    2. Проверить: URL после загрузки страницы.
    3. Проверить: через 1.5 сек происходит автоматический редирект на 'galaxy-map.html'.
    """
    # ⚡ ACT
    star_info: StarInfoPage = star_info_page(data.STAR_INFO_URL['no-star'], expect_redirect=True)

    # ✅ ASSERT
    star_info.wait_for_url(data.GALAXY_MAP_URL)