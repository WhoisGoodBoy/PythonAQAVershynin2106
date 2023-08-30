from selenium.webdriver import Chrome
from lesson20.pages.dashboard_page import Dashboard
import pytest


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.get('https://lordofboards.com.ua/')
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)