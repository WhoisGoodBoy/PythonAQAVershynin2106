

class BaseLocator:
    def __init__(self):
        self.login = ('xpath', '//a[@title="Вхід"]')
        self.catalog = ('xpath', "//a[text()='Каталог']")
        self.comix_and_books = ('xpath', '//div[@class="products-menu__title"]/a[@href="/komiksy-i-knigi/"]')
        self.search = ('xpath', '//input[@class="search__input"]')
        self.first_search_result = ('xpath', '//div[@class="search-results__title"]')