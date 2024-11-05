def my_idea():
    name = "Имя"
    surname = "Фамилия"
    phone = "Телефон"
    mail = "Почта"
    return name,surname,phone,mail

def get_reg_data():
    import re
    reg_name = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')

    reg_surname = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')

    my_reg_phone = re.compile(r'^\+(\d{1,3})\((\d{2})\)(\d{7})$')

    my_reg_mail = re.compile(r'[a-zA-z0-9]+@yandex\.ru$')

    return reg_name,reg_surname,my_reg_phone,my_reg_mail


def reg_check(user_data, reg_pattern, users_list, data_to_check = None):
    import re
    match_data = bool(re.match(reg_pattern, user_data))
    return match_data

def check_unique_data(user_data,data_to_check):
    if user_data in data_to_check:
        return True









