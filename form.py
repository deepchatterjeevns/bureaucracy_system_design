from exception import GradeTooHighException, GradeTooLowException
from bureaucrat import Bureaucrat

class Form:
    def __init__(self, name : str, grade_sign : int, grade_exec : int):
        self.name = name
        self.is_signed = False
        self.grade_sign = grade_sign
        self.grade_exec = grade_exec

    def be_signed( self, officer : Bureaucrat):
        if officer.grade > self.grade_sign:
            raise GradeTooLowException
        else:
            self.is_signed = True
        return

    def execute(self, bureaucrat):
        is_signed = self.is_signed
        if is_signed and bureaucrat.grade <= self.grade_exec:
            self.greet()
            return
        else:
            raise GradeTooLowException
        return

    def __str__(self):
        return '{} sign grade: {}, exec grade: {}, is signed: {}'.format(self.name, self.grade_sign, self.grade_exec, self.is_signed)