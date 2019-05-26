# bureaucracy_system_design
Core modules:

    bureaucrat.py:
        class Bureaucrat:
            attributes:
                name
                grade
            methods:
                __init__
                sign_form(Form)
                execute_form(Form)
                __str__

    exception.py:
        class GradeTooHighException(Exception)
        class GradeTooLowException(Exception)
        
    form.py:
        class Form:
            attributes:
                name
                is_signed
                grade_sign
                grade_exec
            methods:
                __init__
                be_signed(Bureaucrat)
                execute(Bureaucrat)
                __str__
     
     concrete_forms.py:
            multiple classes inheriting from Form with an additional method
            
     intern.py:
            class Intern: (Creates form if entries are valid)
                @classmethod
                make_form( form : str, form_attributes : str)
                            
Testing Modules:

    step1.py
    step2.py
    step3.py
    step4.py
    run_test.py
    
