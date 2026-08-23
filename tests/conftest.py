import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login import LoginPage

# 🌍 КОНФИГУРАЦИЯ ОКРУЖЕНИЯ (Environment)
BASE_URL = os.getenv("CASSANDRA_URL", "file:///D:/Python/cassandra/app")
SHOW_BROWSER = os.getenv("SHOW_BROWSER", "true").lower() == "true"


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
    
    if report.when == "setup" and not os.path.exists("allure-results/environment.properties"):
        os.makedirs("allure-results", exist_ok=True)
        with open("allure-results/environment.properties", "w", encoding="utf-8") as f:
            f.write(f"Base URL={BASE_URL}\n")
            f.write(f"Headless Mode={not SHOW_BROWSER}\n")
            f.write("Browser=Google Chrome\n")
            f.write("Framework=Selene + Pytest\n")


@pytest.fixture
def login_page():
    """🔓 Открывает страницу логина и очищает LocalStorage после теста."""
    page = LoginPage()
    page.open()
    yield page
    
    browser.driver.execute_script("localStorage.clear()")


