import re

user_list = []
user_data_list = []
count = 0

while count != 3:
    user_data_list = []    
    reg_name = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')   
    name = input("Введите имя пользователя ")
    match_name = bool(re.match(reg_name , name))
    while match_name != True:
        print("Содержит неподходящие символы")
        name = input("Введите корректное имя пользователя ")
        reg_name = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
        match_name = bool(re.match(reg_name , name))  
    
    user_data_list.append(name)
    print("Имя принято")
    
    reg_surname = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
    surname = input("Введите фамилию пользователя ")
    match_surname = bool(re.match(reg_surname , surname))
    while match_surname != True:
        print("Содержит неподходящие символы")
        surname = input("Введите корректную фамилию пользователя ")
        reg_surname = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
        match_surname = bool(re.match(reg_surname , surname))  
    user_data_list.append(surname)
    print("Имя принято")
    
    my_phone = input("Введите номер телефона по примеру +***(**)******* ") 
    my_reg_phone = re.compile(r'^\+(\d{1,3})\((\d{2})\)(\d{7})$')
    match_phone = bool(re.match(my_reg_phone , my_phone))
    while match_phone != True:
        print('Не соответствует формату +***(**)*******')
        my_phone = input("Введите корректный номер телефона по примеру +***(**)******* ") 
        my_reg_phone = re.compile(r'^\+(\d{1,3})\((\d{2})\)(\d{7})$')
        match_phone = bool(re.match(my_reg_phone , my_phone))
    user_data_list.append(my_phone)
    print("Телефон принят")
    
    my_mail = input("Введите почту ") 
    my_reg_mail = re.compile(r'[a-zA-z0-9]+@yandex\.ru$')
    match_mail = bool(re.match(my_reg_mail , my_mail))
    while match_mail != True:
        print("Почта должна содержать @yandex.ru")
        my_mail = input("Введите корректную почту ") 
        my_reg_mail = re.compile(r'[a-zA-z0-9]+@yandex\.ru$')
        match_mail = bool(re.match(my_reg_mail , my_mail))
    user_data_list.append(my_mail)
    print("Почта принята")
    if user_data_list in user_list:
        print("\nТакой пользователь уже существует\nВведите нового пользователя")
        continue
    else:
        user_list.append(user_data_list)
    count += 1

for user in user_list:
    print(user)
