class Person():
    def __init__(self, birth_year=1901):
        if 1900 < birth_year < 2019:
            self.birth_year = birth_year
        else:
            raise Exception('!!!year could not be less then 1901')

    def name_setvalidator(self):
        while True:
            full_name = input('Enter please full name according to format: Name(space)Surname: ')
            if ' ' in full_name:
                s_temp = full_name.replace(' ', '')
                if s_temp.isalpha():
                    self.full_name = full_name
                    break
            else:
                raise Exception('!!!full name need to be with space between name and surname!!!')

    def get_name(self):
        Name = self.full_name.split()[0]
        return Name

    def get_surname(self):
        Surname = self.full_name.split()[1]
        return Surname

    def age_in(self, year=2019):
        if year > 1902:
            return year - self.birth_year
        else:
            raise Exception('!!!zero age!!!')


class Employee(Person):
    def __init__(self, birth_year=1901, post='New Commer', exp=0, salary=400):
        super().__init__(birth_year)
        self.post = post
        if exp < 0 or salary < 0 or str(exp).isalpha() or str(salary).isalpha():
            raise Exception('!!!Experience and Salary could not be negative or string, enter positive numbers!!!')
        else:
            self.exp = exp
            self.salary = salary

    def get_status(self):
        if self.exp < 3:
            return 'Junior ' + str(self.post)
        elif self.exp >= 3 and self.exp <= 6:
            return 'Middle ' + str(self.post)
        else:
            return 'Senior ' + str(self.post)

    def sal_raise(self, amount):
        if str(amount).isdigit():
            self.salary += float(amount)
        else:
            print('sal_raise argument must be a digit')
            raise Exception


class ITEmployee(Employee):
    def __init__(self, birth_year=1901, post='New Commer', exp=0, salary=400, skills=[]):
        super().__init__(birth_year, post, exp, salary)
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)

    def add_skills(self, *args):
        self.skills.extend(args)


if __name__ == '__main__':
    emp2 = ITEmployee(1986, 'Tester', 1, 600, ['Perfect Tester'])
    emp2.sal_raise(100)
    emp2.add_skill('Sexy')
    emp2.name_setvalidator()
    print(emp2.full_name, emp2.get_name(), emp2.get_surname(), emp2.age_in(2020), emp2.get_status(), emp2.salary, emp2.skills, sep='\n')

