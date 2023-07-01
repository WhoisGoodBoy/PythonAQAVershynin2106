'''import random
list_of_numbers = [5,8,3,4,8,1,3,7,4,3]
list_of_numbers2 = []
for element in list_of_numbers:
    element = element + 5
    list_of_numbers2.append(element)
    #print(element)
#print(list_of_numbers2)
#new_list_of_numbers = list_of_numbers.copy()
new_list_of_numbers = list(list_of_numbers)
for i in range(len(new_list_of_numbers)):
    new_list_of_numbers[i] = new_list_of_numbers[i] + 5
print(list_of_numbers)
#[0,1,2,3,4,5,6,7,8,9]



new_list_of_numbers = list_of_numbers + new_list_of_numbers + new_list_of_numbers

print(new_list_of_numbers)
print(new_list_of_numbers.count(10))
new_list_of_numbers.reverse()
print(new_list_of_numbers)
new_tuple = (1,2,3)
for element in new_tuple:
    print(element)

while len(new_list_of_numbers) > 5:
    new_list_of_numbers.pop()
    print(new_list_of_numbers)

counter = 0
#while counter < 10:
#    new_list_of_numbers.append(1)
#    counter +=1
#print(new_list_of_numbers)
while counter < 10:
    a = random.randint(1,10)
    print('aaaaaaaaaaaaaaaa')
    print(a)
    if a == 10:
        continue
    counter +=2


for element in new_list_of_numbers:
    if element == 8:
        print('we`re in continue block')
        continue
    print(element)

for element in new_list_of_numbers:
    if element == 9:
        print('we`re in breaking')
        break
    print(element)

'''

unique_values = {'A', 2,3,4,'B'}
list_with_doubles = ['a','a',1,1,2,2,3,3,4]
new_set = set(list_with_doubles)
list_with_doubles = list(new_set)
print(list_with_doubles)
print(len(unique_values))
second_unique_values = {2,3,4}
print(16 not in unique_values)
print(unique_values.isdisjoint(second_unique_values))
print(second_unique_values.issubset(unique_values))
print(second_unique_values<unique_values)
print(unique_values.issuperset(second_unique_values))
third_unique_values = {4,5,6}
print(third_unique_values.union(second_unique_values))
print(third_unique_values.intersection(second_unique_values))
print(third_unique_values.difference(second_unique_values))
print(third_unique_values.symmetric_difference(second_unique_values))
#second_unique_values.update(third_unique_values)
#print(second_unique_values)
#second_unique_values.intersection_update(third_unique_values)
#print(second_unique_values)
#second_unique_values.difference_update(third_unique_values)
#print(second_unique_values)
second_unique_values.symmetric_difference_update(third_unique_values)
print(second_unique_values)
second_unique_values.add(4)
print(second_unique_values)
second_unique_values.remove(6)
print(second_unique_values)
second_unique_values.discard(5)
print(second_unique_values)
second_unique_values.pop()
print(second_unique_values)
second_unique_values.clear()
another_set = set()
print(another_set)
print(second_unique_values)