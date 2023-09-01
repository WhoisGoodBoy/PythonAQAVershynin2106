from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
def test_01():
    driver = Chrome()
    driver.get('https://google.com')
    search_field_locator = "//textarea[@type='search']"
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('how to use webdriver')
    element.send_keys(Keys.ENTER)
    time.sleep(5)
    #time.sleep(5)
    #python_search_result_locator = '//div[@aria-label="how to use webdriver manager in python"]'
    #python_search_element = driver.find_element(by='xpath', value=python_search_result_locator)
    #python_search_element.click()
    second_page = driver.find_element(by='xpath', value = search_field_locator)
    assert second_page.text == 'how to use webdriver'

def test_02():
    driver = Chrome()
    driver.get('https://google.com')
    search_field_locator = "//textarea[@type='search']"
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('how to use webdriver')
    element.send_keys(Keys.ENTER)
    time.sleep(5)
    first_link_locator = "//h3[text()='Selenium Webdriver Tutorial with Examples - BrowserStack']"
    first_link = driver.find_element(by='xpath', value=first_link_locator)
    first_link.click()

    time.sleep(5)
    desired_text_locator = '//p[@class="guide-banner-section__heading"]'
    desired_text = driver.find_element(by='xpath', value=desired_text_locator)
    assert desired_text.text == 'Run Selenium Tests on Cloud'

def test_03():
    driver = Chrome('./drivers/chromedriver.exe')
    driver.get('https://google.com')
    search_field_locator = "//textarea[@type='search']"
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('how to use webdriver')
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    time.sleep(3)
    action.key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()
    time.sleep(5)
