from lesson20.pages.base_page import BasePage
from lesson20.pages.category_page import CategoryPage
from lesson20.core.dashboard_locators import DashboardLocators
from lesson20.core.credentials import login, password

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DashboardLocators()

    def go_to_comix_and_books(self):
        self.click_on_element(self.locators.comix_and_books)
        return CategoryPage(self._driver)

    def go_to_login_form(self):
        self.click_on_element(self.locators.login)

    def search_for_game(self, message):
        self.send_keys_into_field(self.locators.search, message)
        self.wait_until_element_appears(self.locators.first_search_result)
        self.press_enter(self.locators.search)

    def fill_login_form_and_enter(self):
        self.send_keys_into_field(self.locators.login_email_field, login)
        self.send_keys_into_field(self.locators.login_password_field, password)
        self.click_on_element(self.locators.login_submit_button)

    def login_user(self):
        self.go_to_login_form()
        self.fill_login_form_and_enter()

    def logout_user(self):
        self.click_on_element(self.locators.user_logged_in_button)
        self.click_on_element(self.locators.user_logout_button)


