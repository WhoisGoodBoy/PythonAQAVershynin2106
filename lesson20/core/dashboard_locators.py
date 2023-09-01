from lesson20.core.base_locators import BaseLocator


class DashboardLocators(BaseLocator):
    def __init__(self):
        super().__init__()
        self.banner = ('xpath', '//div[@class="banner-image"]')
        self.popular_categories_comix = ('xpath', '//a[@class="frontCategories-a"][@href="/komiksy/"]')