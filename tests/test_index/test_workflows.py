import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🔄 Полный цикл навигации по всем точкам входа с возвратом на Index")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.workflows
def test_full_navigation_cycle_with_return_to_index(index_page):
    """
    Сценарий:
    1. Открыть страницу 'Index Page' (index.html).
    2. Кликнуть на кнопку 'Log In', дождаться перехода на 'login.html'.
    3. Нажать кнопку 'Назад' в браузере, вернуться на 'index.html'.
    4. Кликнуть на кнопку 'Sign Up', дождаться перехода на 'signup.html'.
    5. Нажать кнопку 'Назад' в браузере, вернуться на 'index.html'.
    6. Кликнуть на кнопку 'Restore', дождаться перехода на 'access-restoration.html'.
    7. Нажать кнопку 'Назад' в браузере, вернуться на 'index.html'.
    8. Проверить: все элементы Index (логотип, заголовок, слоган, кнопки, футер) присутствуют и корректно отображаются.
    """

    # ⚡ ACT
    index_page.click_log_in()
    index_page.wait_for_url(expected_url_part=data.LOGIN_URL)
    index_page.click_browser_back()
    index_page.wait_for_url(expected_url_part=data.INDEX_URL)

    index_page.click_sign_up()
    index_page.wait_for_url(expected_url_part=data.SIGNUP_URL)
    index_page.click_browser_back()
    index_page.wait_for_url(expected_url_part=data.INDEX_URL)

    index_page.click_restore()
    index_page.wait_for_url(expected_url_part=data.ACCESS_RESTORATION_URL)
    index_page.click_browser_back()
    index_page.wait_for_url(expected_url_part=data.INDEX_URL)

    # ✅ ASSERT
    index_page.verify_ecg_animation_in_dom()
    index_page.verify_text(
        element=index_page.logo_cassan, expected_text=data.LOGO_CASSAN
    )
    index_page.verify_text(element=index_page.logo_dra, expected_text=data.LOGO_DRA)
    index_page.verify_text(
        element=index_page.project_title, expected_text=data.PROJECT_TITLE
    )
    index_page.verify_text(
        element=index_page.project_slogan, expected_text=data.PROJECT_SLOGAN
    )
    index_page.verify_text(
        element=index_page.footer_copyright, expected_text=data.COPYRIGHT_TEXT
    )

    index_page.check_button_content(button_id="btn-login", expected_text="LOG IN")
    index_page.check_button_content(button_id="btn-signup", expected_text="SIGN UP")
    index_page.check_button_content(button_id="btn-restore", expected_text="RESTORE")
