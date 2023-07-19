#import lesson9.arithmetic as module
#from lesson9 import *
#from lesson9 import arithmetic
#from lesson9.folder1.folder2.folder3.arithmetic import sum as sum1
#from lesson9.folder1.folder2.folder3.arithmetic2 import sum as sum2


first_person_salary = 70
second_person_salary = 120
#print(module.sum(first_person_salary,second_person_salary))
#print(sum)
#print(arithmetic.sum(first_person_salary,second_person_salary))
from lesson9 import sum as sum1
from lesson9.folder1.folder2.folder3.arithmetic2 import sum as sum2
print(sum1(first_person_salary,second_person_salary))
print(sum2(first_person_salary,second_person_salary, 500))
import lesson9
print(lesson9.sum(1,2))
print(lesson9.difference(5000,2501))

from lesson9.new_directory.new_directory1.application1 import summ as new_exclellent_sum
print(new_exclellent_sum(15,20))

lesson9.multiple_parameters(1,2,3)