from abc import ABC, abstractmethod
class Employee(ABC):
    a = 5
    def __init__(self,salary,position):
        self.salary = salary
        self.position=position

    @abstractmethod
    def do_work(self):
        pass

    def do_another_work(self):
        print(2+5)

class Engineer(Employee):
    def __init__(self,salary, position):
        super().__init__(salary,position)


    def do_work(self):
        print('i`m working')

    def _deploy_program(self):
        print('program is deploying rn')

    def __create_new_framework(self):
        print('framework is done')

    def __create_ifrastructure(self):
        print('ifrastructure is done')

    def deploy(self):
        self.__create_new_framework()
        self.__create_ifrastructure()

class Programmer(Engineer):
    def __init__(self,salary,position):
        super().__init__(salary, position)

    def do_work(self):
        print('i`m writing programms')






class Toyota_employee(Employee):
    def __init__(self,salary,position):
        super().__init__(salary,position)

    def do_work(self):
        print('I`m doing Toyota stuff')


class Renault_employee(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('I`m doing Renault stuff')

#employee = Employee('worker', 2000)

toyota_employee = Toyota_employee('worker',2100)

engi = Engineer(2,'1')
engi._deploy_program()
prog = Programmer(3,5)
prog._deploy_program()
engi.deploy()
prog.deploy()