import allure
import pytest

from . import data


@allure.id("CAS-01")
@allure.title("🌌 Валидация логотипа и локатора.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.page
def test_validate_cassandra_logo(index_page):
    """
    Сценарий:
    1. Переходим на страницу 'index.html'.
    2. Проверяем: наличие логотипа и текста 'CASSAN' по 'data-wm-id'.
    3. Проверяем: наличие логотипа и текста 'DRA' по 'data-wm-id'.
    """

    # ✅ ASSERT
    index_page.verify_check_text(
        element=index_page.logo_cassan, expected_text=data.LOGO_CASSAN
    )
    index_page.verify_check_text(
        element=index_page.logo_dra, expected_text=data.LOGO_DRA
    )


@allure.id("CAS-02")
@allure.title("📝 Валидация заголовка, слогана и локаторов.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.page
def test_validate_title_and_slogan(index_page):
    """
    Сценарий:
    1. Переходим на страницу 'index.html'.
    2. Проверяем: наличие заголовка и текста 'Planetary...' по 'data-wm-id'.
    3. Проверяем: наличие слогана и текста 'We find....' по 'data-wm-id'.
    """

    # ✅ ASSERT
    index_page.verify_check_text(
        element=index_page.project_title, expected_text=data.PROJECT_TITLE
    )
    index_page.verify_check_text(
        element=index_page.project_slogan, expected_text=data.PROJECT_SLOGAN
    )


@allure.id("CAS-03")
@allure.title("©️ Валидация футера и локатора.")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.page
def test_validate_footer_copyright(index_page):
    """
    Сценарий:
    1. Переходим на страницу 'index.html'.
    2. Проверяем: наличие футера и текста по 'data-wm-id'.
    """
    # ✅ ASSERT
    index_page.verify_check_text(
        element=index_page.footer_copyright, expected_text=data.COPYRIGHT_TEXT
    )
   
