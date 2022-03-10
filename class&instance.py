# position, name, age, level, salary
se1 = ['Software engineer', 'Max', 20, 'Junior', 5000]
se1 = ['Software engineer', 'Max', 20, 'Junior', 5000]
d1 = ['Designer', 'Philipp']




class SoftwareEngineer:

    # class attribute
    alias = 'Keyboard Magician'

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self. level = level
        self.salary = salary

    def code(self):
        print(f'{self.name} is writing code...')

    def code_in_language(self, language):
        print(f'{self.name} is wirting code in {language}...')

    def __str__(self):
        information = f'name = {self.name}, age = {self.age}, level = {self.level}'
        return information
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000

se1 = SoftwareEngineer('Max', 20, 'Junior', 5000)
se2 = SoftwareEngineer('Lisa', 22, 'Senior', 5000)
se3 = SoftwareEngineer('Lisa', 22, 'Senior', 5000)

se1.code()
se2.code()
se1.code_in_language('Python')
print(se1)


print(se1.entry_salary(24))
print(SoftwareEngineer.entry_salary(27))
