from form import Form

class ShrubberyCreationForm(Form):
    def __init__(self, target: str):
        self.name = 'ShrubberyCreationForm'
        self.grade_sign = 145
        self.grade_exec = 137
        self.target = target

    def greet(self):
        print('Shrubbery has been planted at {}'.format(self.target))

class RobotomyRequestForm(Form):
    def __init__(self, target: str):
        self.name = 'RobotomyRequestForm'
        self.grade_sign = 72
        self.grade_exec = 45
        self.target = target

    def greet(self):
        print('{} has been robotomied'.format(self.target))
