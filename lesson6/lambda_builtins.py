import math
import random
from functools import reduce


def func_name():
    pass


double = lambda x: x*2
print(double(5))
print(double(3))
print(double(9))


def func_double(x):
    return x*2

def to_cube(x):
    return x * x * x

lambda_to_cube = lambda x: x * x * x
print(to_cube(3))
print(lambda_to_cube(3))

lambda_multiple_3 = lambda a,b,c: a * b * c
print(lambda_multiple_3(1000,21,16))


sqrt_x = lambda x: math.sqrt(x)
print(sqrt_x(4))


lambda_list =[
    lambda x:x*2,
    lambda x:x*3,
    lambda x:x*4
]

for el in lambda_list:
    print(el(1000))

lambda_tuple = (
    lambda x: x * 2,
    lambda x: x * 3,
    lambda x: x * 4
)

for el in lambda_tuple:
    print(el(15000))


areas_dict = {
    'circle': lambda r:math.pi * r * r,
    'rectangle': lambda a, b: a * b,
    'square': lambda a: a*a
}

print(areas_dict['circle'](30))
print(areas_dict['rectangle'](10,20))
print(areas_dict['square'](300))


list_a = [1,2,3,4,5,6,7,8,9,10]

#filter(func,list)
filtered_list = list(filter(lambda x: x%2==0, list_a))
print(filtered_list)

filtered_list = list(filter(lambda x: x%2!=0, list_a))
print(filtered_list)

#map(func, list)
double_list = list(map(lambda x: x*2, list_a))
print(double_list)

#reduce(func, list)
sum_example = reduce(lambda x,y: x + y, list_a)
print(sum_example)

list_b = [90, 50, 120, 20, 69]

min_el = reduce(lambda x, y : x if (x>y) else y, list_b)
print(min_el)













