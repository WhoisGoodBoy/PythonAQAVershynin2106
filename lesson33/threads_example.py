import time
import concurrent.futures


def function_example(name):
    print(f'we are in {name} function')
    time.sleep(2)
    print(f'we are exiting {name} function')


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(function_example, range(5))

