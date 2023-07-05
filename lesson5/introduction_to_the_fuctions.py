def function_example(parameter1, parameter2='I`m default parameter'):
    print(f'hello {parameter1}')
    print(f'and meet the {parameter2}')

function_example('first' , parameter2='a')
function_example('second', 'b')
function_example('third')

def summ_of_two_numbers(first, second):
    result = first + second
    return result

a = summ_of_two_numbers(5,10)
b = summ_of_two_numbers(10,20)
c = summ_of_two_numbers(a,b)
print(c)


def summ_and_multiply(first, second):
    result_of_summ = summ_of_two_numbers(first,second)
    result_of_multiply = first * second
    return result_of_summ, result_of_multiply


first_result, second_result = summ_and_multiply(5,20)
print(first_result)
print(second_result)

def multiple_parameters(*paramters): # *args
    for element in paramters:
        print(element)


multiple_parameters('pepperoni')
multiple_parameters('pepperoni', 'carbanana', '4cheese')


def multiple_named_parameters(**user_info): # **kwargs
    for key, value in user_info.items():
        print(f'{key} : {value}')

multiple_named_parameters(firs_name = 'alejandro', second_name = 'formoza')
