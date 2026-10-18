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