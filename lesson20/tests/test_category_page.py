import time


def test_go_to_first_result(dashboard):
    category_page = dashboard.go_to_comix_and_books()
    product_page = category_page.go_to_first_result()
    time.sleep(5)

def test_filtered_new(dashboard):
    category_page = dashboard.go_to_comix_and_books()
    category_page.filter_new()
    prduct_page = category_page.go_to_first_result()
    time.sleep(5)


def test_filtered_new_start_from_categories(categories):
    categories.filter_new()
    product_page = categories.go_to_first_result()
    time.sleep(5)

def test_count_products_elements_on_page(categories):
    list_of_elements = categories.wait_until_list_of_elements_appears(categories.locators.results)
    assert len(list_of_elements) == 20
    time.sleep(5)

