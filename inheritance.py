class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
    def work(self):
        print(f'{self.name} is working...')


class SoftwareEngineer(Employee):

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f'{self.name} is debugging...')

    def work(self):
        print(f'{self.name} is coding...')


class Designer(Employee):

    def draw(self):
        print(f'{self.name} is drawing...')

    def work(self):
        print(f'{self.name} is designing...')

se = SoftwareEngineer('Max', 25, 6000, 'Junior')

se.work()



d = Designer('Philip', 22, 5000)

d.work()
