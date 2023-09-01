import time

def test_go_to_books_and_comix(dashboard):
    dashboard.go_to_comix_and_books()
    time.sleep(5)

def test_search_for_pathfinder(dashboard):
    dashboard.search_for_game('pathfinder')
    time.sleep(10)