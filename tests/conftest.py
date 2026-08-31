import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.dashboard import DashboardPage
from pages.login import LoginPage

# ========================================================================
# region 1️⃣ ⚙️ КОНФИГУРАЦИЯ И БРАУЗЕР
# ========================================================================
# 🌍 КОНФИГУРАЦИЯ ОКРУЖЕНИЯ (Environment)
BASE_URL = os.getenv("CASSANDRA_URL", "file:///D:/Python/cassandra/app")
SHOW_BROWSER = os.getenv("SHOW_BROWSER", "false").lower() == "true"

# 🌐 URL АДРЕСА (URL Addresses)
DASHBOARD_URL = "/dashboard.html"
LOGIN_URL = "/login.html"


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    """🚀 Запускает браузер перед тестом и закрывает после."""
    chrome_options = Options()

    if not SHOW_BROWSER:
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    browser.config.driver = webdriver.Chrome(options=chrome_options)
    browser.config.base_url = BASE_URL
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 6

    yield

    browser.quit()


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


# ========================================================================
# region 2️⃣ 🛠️ ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ========================================================================
def _do_login(callsign: str, access_code: str) -> DashboardPage:
    """Выполняет процедуру логина и возвращает объект DashboardPage."""
    login_page = LoginPage()
    login_page.open()
    login_page.enter_callsign(callsign)
    login_page.enter_access_code(access_code)
    login_page.click_establish_connect()
    return DashboardPage()


# ========================================================================
# region 3️⃣ 👤 АВТОРИЗАЦИЯ И ПОЛЬЗОВАТЕЛИ (Happy Path)
# ========================================================================
@pytest.fixture
def login_page():
    """🔓 Открывает страницу логина и очищает LocalStorage после теста."""
    page = LoginPage()
    page.open()
    yield page

    browser.driver.execute_script("localStorage.clear()")


@pytest.fixture(scope="function")
def dashboard_page_aurora():
    """Логин под AURORA → переход на Dashboard → очистка после теста."""
    page = _do_login("AURORA", "COMET_42")
    page.verify_current_url(expected_url_part=LOGIN_URL)

    yield page
    browser.driver.execute_script("localStorage.clear()")


@pytest.fixture(scope="function")
def dashboard_page_orion():
    """Логин под ORION → переход на Dashboard → очистка после теста."""
    page = _do_login("ORION", "NEBULA_7")
    page.verify_current_url(expected_url_part=LOGIN_URL)

    yield page
    browser.driver.execute_script("localStorage.clear()")


# ========================================================================
# region 4️⃣ 🧹 ОЧИСТКА И СПЕЦИАЛЬНЫЕ СОСТОЯНИЯ (Edge Cases)
# ========================================================================
@pytest.fixture(scope="function")
def ensure_empty_storage():
    """Гарантирует пустой localStorage (открывает login.html для активации домена)."""
    browser.open("/login.html")
    browser.driver.execute_script("localStorage.clear();")


@pytest.fixture(scope="function")
def dashboard_page_unauthorized(ensure_empty_storage):
    """Открывает Dashboard с пустым localStorage (без авторизации)."""
    page = DashboardPage()
    page.open()
    yield page


@pytest.fixture
def dashboard_page_corrupted(login_page):
    """
    Открывает Dashboard с повреждёнными данными в localStorage.

    Порядок:
    1. login_page активирует домен.
    2. Записываем битый JSON в currentUser.
    3. Открываем дашборд (JS попадёт в catch).
    """
    login_page.set_corrupted_user_data()

    page = DashboardPage()
    page.open()
    return page


@pytest.fixture
def dashboard_page_selectors():
    """Возвращает экземпляр DashboardPage без открытия страницы (только для доступа к селекторам)."""
    return DashboardPage()
