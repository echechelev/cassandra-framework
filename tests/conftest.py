import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.access_restoration import AccessRestorationPage
from pages.dashboard import DashboardPage
from pages.index import IndexPage
from pages.login import LoginPage
from pages.signup import SignupPage
from tests import data

# ========================================================================
# region 1️⃣ ⚙️ КОНФИГУРАЦИЯ И БРАУЗЕР
# ========================================================================
# 🌍 УНИВЕРСАЛЬНАЯ КОНФИГУРАЦИЯ ОКРУЖЕНИЯ
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "app"))
SAFE_DIR = APP_DIR.replace("\\", "/")
BASE_URL = os.getenv("CASSANDRA_URL", f"file:///{SAFE_DIR}/")
SHOW_BROWSER = os.getenv("SHOW_BROWSER", "false").lower() == "true"


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    """🚀 Запускает браузер перед тестом и закрывает после (полная изоляция)."""
    chrome_options = Options()

    if not SHOW_BROWSER:
        chrome_options.add_argument("--headless=new")

    # Стабильность в headless и CI
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Убираем лишние уведомления и автоматизацию
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Инициализация драйвера
    browser.config.driver = webdriver.Chrome(options=chrome_options)
    browser.config.base_url = BASE_URL
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    browser.config.timeout = 6

    yield

    browser.quit()


# ========================================================================
# region 2️⃣ 🌐 НАВИГАЦИЯ
# ========================================================================
@pytest.fixture
def login_page():
    """🔓 Открывает страницу логина и очищает Storage после теста."""
    page = LoginPage()
    page.open()

    yield page

    page.clear_all_storages()


@pytest.fixture
def signup_page():
    """🔓 Открывает страницу регистрации и очищает Storage после теста."""
    page = SignupPage()
    page.open()

    yield page

    page.clear_all_storages()


@pytest.fixture
def restore_page():
    """🔓 Открывает страницу восстановления и очищает Storage после теста."""
    page = AccessRestorationPage()
    page.open()

    yield page

    page.clear_all_storages()


@pytest.fixture(scope="function")
def index_page():
    """🔓 Открывает страницу индекса и очищает Storage после теста."""
    page = IndexPage()
    page.open()

    yield page

    page.clear_all_storages()


@pytest.fixture(scope="function")
def dashboard_page():
    """🔓 Открывает страницу дашборда и очищает Storage после теста."""
    page = DashboardPage()
    page.open()

    yield page

    page.clear_all_storages()


# ========================================================================
# region 3️⃣ 👤 АВТОРИЗАЦИЯ
# ========================================================================
@pytest.fixture(scope="function")
def dashboard_page_aurora():
    """Логин под AURORA → переход на Dashboard → очистка после теста."""

    page = _do_login(data.NAME_AURORA, data.ACCESS_CODE_AURORA)

    yield page

    page.clear_all_storages()


@pytest.fixture(scope="function")
def dashboard_page_orion():
    """Логин под ORION → переход на Dashboard → очистка после теста."""

    page = _do_login(data.NAME_ORION, data.ACCESS_CODE_ORION)

    yield page

    page.clear_all_storages()


@pytest.fixture(scope="function")
def dashboard_page_nova(nova_created):
    """Создание NOVA → логин переход → на Dashboard → очистка после теста."""

    page = _do_login(data.NAME_NOVA, data.ACCESS_CODE_NOVA)

    yield page

    page.clear_all_storages()


@pytest.fixture(scope="function")
def dashboard_page_knopa(knopa_restored):
    """Создание KNOPA → логин переход → на Dashboard → очистка после теста."""

    page = _do_login(data.NAME_KNOPA, data.ACCESS_CODE_KNOPA)

    yield page

    page.clear_all_storages()


# ========================================================================
# region 4️⃣ 🛠️ СОЗДАНИЕ/ВОССТАНОВЛЕНИЕ ПОЛЬЗОВАТЕЛЕЙ
# ========================================================================
@pytest.fixture(scope="function")
def nova_created():
    """Создает пользователя NOVA через UI регистрации."""
    page = SignupPage()
    page.open()

    page.enter_full_name(data.NAME_NOVA)
    page.select_role(data.ROLE_ENGINEER)
    page.click_proceed()

    page.enter_access_code(data.ACCESS_CODE_NOVA)
    page.enter_confirm_access_code(data.ACCESS_CODE_NOVA)
    page.enter_recovery_cipher(data.RECOVERY_CIPHER_NOVA)
    page.click_complete_registration()

    yield page


@pytest.fixture(scope="function")
def knopa_restored():
    """Восстанавливает доступ пользователю KNOPA через UI."""
    page = AccessRestorationPage()
    page.open()

    page.enter_callsign(data.NAME_KNOPA)
    page.enter_recovery_cipher(data.RECOVERY_CIPHER_KNOPA)
    page.enter_new_access_code(data.ACCESS_CODE_KNOPA)
    page.enter_confirm_access_code(data.ACCESS_CODE_KNOPA)
    page.click_restore_access()

    yield page


# ========================================================================
# region 5️⃣ ⚙️ Хелпер-функции
# ========================================================================
def _do_login(callsign: str, access_code: str) -> DashboardPage:
    """Выполняет процедуру логина и возвращает объект DashboardPage."""
    login_page = LoginPage()
    login_page.open()
    login_page.enter_callsign(callsign)
    login_page.enter_access_code(access_code)
    login_page.click_establish_connect()

    dashboard_page = DashboardPage()
    dashboard_page.wait_for_url(expected_url_part=data.DASHBOARD_URL)

    return dashboard_page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Создает файл environment.properties для красивого отображения в Allure Report."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "setup" and not os.path.exists(
        "allure-results/environment.properties"
    ):
        os.makedirs("allure-results", exist_ok=True)
        with open("allure-results/environment.properties", "w", encoding="utf-8") as f:
            f.write(f"Base URL={BASE_URL}\n")
            f.write(f"Headless Mode={not SHOW_BROWSER}\n")
            f.write("Browser=Google Chrome\n")
            f.write("Framework=Selene + Pytest\n")
