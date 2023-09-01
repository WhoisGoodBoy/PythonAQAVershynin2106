from lesson20.core.base_locators import BaseLocator


class CategoriesLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.checkbox_new = ('xpath', "//span[text()='Новинка']/../span[1]")
        self.results = ('xpath', '//a[@class="catalogCard-image "]')