import time

def test_go_to_books_and_comix(dashboard):
    dashboard.go_to_comix_and_books()
    time.sleep(5)

def test_search_for_pathfinder(dashboard):
    dashboard.search_for_game('pathfinder')
    dashboard.wait_until_element_appears(dashboard.locators.h1_header)
    h1 = dashboard.return_element(dashboard.locators.h1_header)
    assert h1.text == 'Результати пошуку «pathfinder»'


def test_login(dashboard):
    dashboard.login_user()
    time.sleep(10)

def test_logout(dashboard):
    dashboard.login_user()
    dashboard.logout_user()
    time.sleep(5)