from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01():
    driver = Chrome()
    driver.get('https://google.com')
    search_field_locator = "//textarea[@type='search']"
    driver.implicitly_wait(10)
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('how to use webdriver')
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    action.key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()


def test_02():
    driver = Chrome()
    driver.get('https://lordofboards.com.ua/')
    web_driver_wait = WebDriverWait(driver, 3)
    search_input_locator = '//input[@placeholder="пошук товарів"]'
    search_input_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_input_locator,)))
    search_input_with_wait.send_keys('Полонянка')
    search_first_result_locator = '//div[@class="search-results__title"][1]'
    search_first_result_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_first_result_locator,)))
    assert search_first_result_with_wait.text == 'Комікс-квест: Полонянка'
    #search_input = driver.find_element(by='xpath', value=search_input_locator)
