from mimesis import Person, Business

PERSON = Person('ru')
COMPANY = Business('ru')
DOMAINS = ['google.com', 'yandex.ru', 'mail.ru']


def generate_sign_up_info():
    company_name = COMPANY.company()
    first_name = PERSON.first_name()
    last_name = PERSON.last_name()
    phone = PERSON.telephone(mask='##########')
    email = PERSON.email(domains=DOMAINS)
    password = "Qwerty123!"
    return company_name, first_name, last_name, phone, email, password
