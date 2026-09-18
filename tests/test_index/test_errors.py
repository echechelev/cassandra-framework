import allure
import pytest

from tests import data


@allure.id("CAS-01")
@allure.title("🔄 Автоматический редирект на дашборд при наличии активной сессии")
@allure.label("owner", "Evgeniy Chechelev")
@allure.label("feature", "index")
@pytest.mark.regress
@pytest.mark.index
@pytest.mark.errors_ui
def test_redirect_to_dashboard_with_active_session(dashboard_page_aurora):
    """
    Сценарий:
    1. Выполнить авторизацию под пользователем 'AURORA'.
    2. Перейти на страницу 'Dashboard Page'.
    3. Принудительно перейти по URL главной страницы 'index.html'.
    4. Проверить: редирект сработал, URL содержит 'dashboard.html'.
    """

    # ⚡ ACT
    dashboard_page_aurora.open_url(path=data.INDEX_URL)

    # ✅ ASSERT
    dashboard_page_aurora.wait_for_url(data.DASHBOARD_URL)
