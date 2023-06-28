'''a = input("plese write here integer")
integer_value_a = int(a)
print(a)



this_is_true = True
this_is_true_integer = int(this_is_true)
print(this_is_true_integer)
this_is_empty_string = ''
print(bool(this_is_empty_string))

# < less
# >more
# <= less or equal
# >= more or equal
# == equal
# != not equal
a = input("please insert a")
a_int = int(a)
if a_int > 5:
    print("COngratulations you are winner")
elif a_int < 3:
    print("try harder")
else:
    print("better luck next time")




first_value = 26
if type(first_value) == int or first_value < 25:
    print("it`s above 20")


second_value = 17
if second_value <= 16 and second_value > 10:
    print('it`s above 13')
elif second_value:
    print("second_value_exists")

print(bool(0))
print(bool(0.01))


third_value = 5
if third_value > 4 and not second_value > 20:
    print('a')


eyes = int(input("number of eyes"))
legs = int(input("number of legs"))
if eyes == 8:
    if legs == 8:
        print("this is spider")
    elif legs == 6:
        print("this is fly")
    else:
        print("creature is undefined")
elif eyes == 1:
    print("this is odin or cyclopus")
elif eyes > 1 and eyes < 8:
    print("meet the horror beyond your comprehesions")

'''
our_beautiful_list = [2,5,3,5,8,"jtjrsj", 9.0]
our_list1 = []
our_list_2 = list()
print(len(our_beautiful_list))
print(our_beautiful_list[-1])
print(our_beautiful_list.index(5))
our_beautiful_list.append(8)
print(our_beautiful_list)
our_beautiful_list.insert(3, 11)
print(our_beautiful_list)
our_beautiful_list[3:].remove(5)

print(our_beautiful_list)
'''
our_beautiful_list.pop()
print(our_beautiful_list)
our_beautiful_list.pop(0)
print(our_beautiful_list)
del our_beautiful_list[1]
print(our_beautiful_list)
our_beautiful_list.clear()
print(our_beautiful_list)

another_list = [9,3,6,2,6,9,5,1]
simple_list = [1,2,3]
another_list.sort(reverse = True)
print(another_list)
print(another_list[:5])
print(another_list[1:])
simple_list.extend(another_list)
another_list= simple_list
print(another_list)
'''
