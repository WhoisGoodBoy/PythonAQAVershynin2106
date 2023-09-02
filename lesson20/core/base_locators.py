

class BaseLocator:
    def __init__(self):
        self.login = ('xpath', '//a[@title="Вхід"]')
        self.catalog = ('xpath', "//a[text()='Каталог']")
        self.comix_and_books = ('xpath', '//div[@class="products-menu__title"]/a[@href="/komiksy-i-knigi/"]')
        self.search = ('xpath', '//input[@class="search__input"]')
        self.first_search_result = ('xpath', '//div[@class="search-results__title"]')
        self.login_email_field = ('xpath', '//div[@id="modal-overlay"]//input[@type="email"]')
        self.login_password_field = ('xpath', '//div[@id="modal-overlay"]//input[@type="password"]')
        self.login_submit_button = ('xpath', '//div[@id="modal-overlay"]//input[@type="submit"]')
        self.user_logged_in_button = ('xpath', '//a[@class="userbar__button"]')
        self.user_logout_button = ('xpath', '//a[@href="/security/logout/"]')
        self.h1_header = ('xpath', '//h1')