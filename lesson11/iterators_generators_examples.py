'''numbers = [1,2,3,4,5]
numbers_iterator = iter(numbers)
print(numbers_iterator)
for number in numbers_iterator:
    print(number)
print(next(numbers_iterator))
print(next(numbers_iterator))
'''

def my_gen():
    counter = 0
    while counter<10000:
        yield counter
        counter +=1


my_generator = my_gen()
for item in my_generator:
    print(item)

