import concrete_forms

class Intern:
    @classmethod
    def make_form(cls, form_name: str, form_target: str):
        a_form = form_name.split(' ')
        req_form = ''
        for string in a_form:
            req_form += string.capitalize()
        req_form += 'Form'
        try:
            valid_class = getattr(concrete_forms, req_form)
            print('Intern creates {}'.format(form_name))
            return valid_class(form_target)
        except:
            return None
