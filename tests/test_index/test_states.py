import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🌌 Валидация логотипа и локатора")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.states
def test_validate_cassandra_logo(index_page):
    """
    Сценарий:
    1. Перейти на страницу 'Index page'.
    2. Проверить: наличие логотипа и текста 'CASSAN' по 'data-wm-id'.
    3. Проверить: наличие логотипа и текста 'DRA' по 'data-wm-id'.
    """

    # ✅ ASSERT
    index_page.verify_text(
        element=index_page.logo_cassan, expected_text=data.LOGO_CASSAN
    )
    index_page.verify_text(element=index_page.logo_dra, expected_text=data.LOGO_DRA)


@allure.id("CAS-02")
@allure.title("📝 Валидация заголовка, слогана и локаторов")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.states
def test_validate_title_and_slogan(index_page):
    """
    Сценарий:
    1. Перейти на страницу 'Index page'.
    2. Проверить: наличие заголовка и текста 'Planetary...' по 'data-wm-id'.
    3. Проверить: наличие слогана и текста 'We find....' по 'data-wm-id'.
    """

    # ✅ ASSERT
    index_page.verify_text(
        element=index_page.project_title, expected_text=data.PROJECT_TITLE
    )
    index_page.verify_text(
        element=index_page.project_slogan, expected_text=data.PROJECT_SLOGAN
    )


@allure.id("CAS-03")
@allure.title("©️ Валидация футера и локатора")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.states
def test_validate_footer_copyright(index_page):
    """
    Сценарий:
    1. Перейти на страницу 'Index page'.
    2. Проверить: наличие футера и текста по 'data-wm-id'.
    """
    # ✅ ASSERT
    index_page.verify_text(
        element=index_page.footer_copyright, expected_text=data.COPYRIGHT_TEXT
    )


@allure.id("CAS-04")
@allure.title("📋 Валидация содержимого кнопок навигации")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.states
def test_navigation_buttons_content(index_page):
    """
    Сценарий:
    1. Открыть страницу 'Index Page' (index.html).
    2. Проверить: кнопка 'Log In' содержит текст 'Log In'.
    3. Проверить: кнопка 'Sign Up' содержит текст 'Sign Up'.
    4. Проверить: кнопка 'Restore' содержит текст 'Restore'.
    """

    # ✅ ASSERT
    index_page.check_button_content(button_id="btn-login", expected_text="LOG IN")
    index_page.check_button_content(button_id="btn-signup", expected_text="SIGN UP")
    index_page.check_button_content(button_id="btn-restore", expected_text="RESTORE")


@allure.id("CAS-05")
@allure.title("🔗 Валидация href атрибутов кнопок навигации")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.states
def test_navigation_buttons_href_attributes(index_page):
    """
    Сценарий:
    1. Открыть страницу 'Index Page' (index.html).
    2. Проверить атрибут 'href' у кнопки 'Log In' по data-wm-id='btn-login'.
    3. Проверить атрибут 'href' у кнопки 'Sign Up' по data-wm-id='btn-signup'.
    4. Проверить атрибут 'href' у кнопки 'Restore' по data-wm-id='btn-restore'.
    """

    # ✅ ASSERT
    index_page.check_button_href(button_id="btn-login", expected_href=data.LOGIN_URL)
    index_page.check_button_href(button_id="btn-signup", expected_href=data.SIGNUP_URL)
    index_page.check_button_href(button_id="btn-restore", expected_href=data.ACCESS_RESTORATION_URL)
