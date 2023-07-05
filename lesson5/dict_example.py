field = 'field'
cat = {'name':'Tom', 'age': 5, 'goodboy': True, 'locations':['home', ['yard',field]]}
print(cat['name'])
print(cat)
print(len(cat))
del(cat['locations'])
print(cat)
print('name' not in cat)
cat2 = cat.copy()
print(id(cat2))
print(id(cat))
print(cat.get('age'))
print(cat.items())
print(cat.keys())
print(cat.values())
a = cat.pop('goodboy')
print(a)
print(cat)
print(cat.popitem())
print(cat)
cat.update({'tail':'black', 'eye_color':'geterochrome'})
print(cat)
cat['name'] = 'black'
print(cat)
cat.update(cat2)
print(cat)

'''
first_value = 5
second_value = first_value
print(id(first_value))
print(id(second_value))
second_value = 7
print(first_value)
print(second_value)
print(id(first_value))
print(id(second_value))
'''
first_list = [1,2,3]
second_list = first_list
print(id(first_list))
print(id(second_list))
second_list[0] = 12
print(first_list)
print(second_list)
print(id(first_list))
print(id(second_list))
print(first_list == second_list)
print(first_list is second_list)
#third_list = first_list.copy()
third_list = list(first_list)
print(id(third_list))
print(first_list == third_list)
print(first_list is third_list)
third_list.append(6)
print(first_list)
print(third_list)