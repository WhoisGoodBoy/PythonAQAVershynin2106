import math
import random

first_value = 2       # int
g_value = 9.8 #float
message = 'This is message' #string
result = True   # bool
empty_result = None #NoneType

'''
print(id(one))
one = g_value
print(id(one))
print(id(g_value))
print(one)

second_value = 4
third_value = first_value + second_value
print(third_value)
print(third_value - first_value)
print(first_value * second_value)
print(first_value / second_value)
print(6 // 2)
print(4 % 2)
print(3**2)
print(3**3)
print(2 + 3 * 4)
print((2+3) * 4)
small_number = 0.1 * 0.1
print(round(small_number, 2))

print(math.pi)
pi = math.pi
r = 2
print(pi * r**2)
print(math.cos(2))

random_number = random.randint(1,50)
pi = math.pi
print(random_number)
print(pi * random_number**2)
print(random.randrange(15))
print(random.choice(['god exists', 'you exists']))
'''

print(dir('aaaa'))
my_name = 'my name'
#print(my_name.title())
#print(my_name.upper())
#print(my_name.lower())
first_name = 'Batman'
second_name = 'Joker '
full_name = first_name + ' ' + second_name
print("hello, " + full_name)
print('\tpython')
print("hello, my neme is " + full_name + '\nand \ni`m \nhere \nto \nlearn \npython')

first_string = ' Python'
second_string = 'python '

print(second_string.rstrip())
print(first_string.lstrip())
print(full_name.strip())

company_info = 'amazon amazon is a very huge company, unfortunately'
#print(company_info.capitalize())
#print(company_info.replace('amazon', 'Apple', 2))

print('is' in company_info)
print(company_info.islower())
print(company_info.isupper())
print(first_name.isalpha())
print(' '.isspace())
print('4'.isdigit())
four_alpha = '4'
four_numeric = 4
print(company_info.count('a'))
print(company_info.index('a'))
print(company_info.find('m'))
print(len(company_info))
print(company_info.split('very'))
print('this is first line \nthis is second line'.splitlines())
print(company_info[21])
print(company_info[21:])
print(company_info[21:30])
print(company_info[:30])
print(company_info[21:30:2])
food = 'solyanka'
price = 90
print('Food is {} and price is {}'.format(food, price))
print(f'food is {food}, price is {price}')


