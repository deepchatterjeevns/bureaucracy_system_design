from exception import GradeTooHighException, GradeTooLowException

class Bureaucrat:
    def __init__(self, name : str, grade : int):
        self.name = name
        if grade < 1:
            raise GradeTooHighException
        elif grade > 150:
            raise GradeTooLowException
        self.grade = grade

    def sign_form(self, form):
        if self.grade <= form.grade_sign:
            form.is_signed = True
            print('{} signs {}'.format(self.name, form.name))
        else:
            print('{} cannot sign {}'.format(self.name, form.name))
        return

    def execute_form(self, form):
        if self.grade > form.grade_exec:
            raise GradeTooLowException
        else:
            form.greet()
            print('{} executes {}'.format(self.name, form.name))
        return

    def __str__(self):
        return '{} grade: {}'.format(self.name, self.grade)

# bur1 = Bureaucrat('Bob', 15)
# bur2 = Bureaucrat('Tom', 75)

# print(bur1)
# print(bur2)
# print(bur1.grade)
# print(bur1.name)
# bur3 = Bureaucrat('Tom', 151)
# print(bur3)
