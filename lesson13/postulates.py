class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Employee(Human):
    def __init__(self, name, age, gender, salary, position):
        super().__init__(name, age, gender)
        self.salary = salary
        self.position = position

goose = Employee('Andy', 2, 'male', '2 glasses of wheat', 'good boy')
print()
