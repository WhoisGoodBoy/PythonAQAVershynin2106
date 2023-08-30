from lesson20.pages.base_page import BasePage

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_comix_and_books(self):
        locator = ('xpath', '//div[@class="products-menu__title"]/a[@href="/komiksy-i-knigi/"]')
        element = self.wait_until_element_appears(locator)
        element.click()

    def go_to_login_form(self):
        locator = ('xpath', '//a[@title="Вхід"]')
        element = self.wait_until_element_appears(locator)
        element.click()
