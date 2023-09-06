from selenium.webdriver import Chrome
from lesson20.pages.dashboard_page import Dashboard
from lesson20.pages.category_page import CategoryPage
import pytest


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture
def dashboard(driver):
    driver.get('https://lordofboards.com.ua/')
    yield Dashboard(driver)

@pytest.fixture
def categories(driver):
    driver.get('https://lordofboards.com.ua/komiksy-i-knigi/')
    driver.add_cookie({'name':'flag', 'value':'red'})
    print(f'cookie:{driver.get_cookie("flag")}')
    driver.execute_script("window.localStorage['flag1'] = 'green'")
    print(driver.execute_script("return window.localStorage['userWay2'];"))
    yield CategoryPage(driver)