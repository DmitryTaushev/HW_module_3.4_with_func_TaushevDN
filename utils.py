def get_reg_data():
    import re
    reg_name = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')

    reg_surname = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')

    my_reg_phone = re.compile(r'^\+(\d{1,3})\((\d{2})\)(\d{7})$')

    my_reg_mail = re.compile(r'[a-zA-z0-9]+@yandex\.ru$')

    return reg_name,reg_surname,my_reg_phone,my_reg_mail

