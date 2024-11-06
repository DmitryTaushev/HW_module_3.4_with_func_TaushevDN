from utils import get_reg_data, reg_check,my_idea, check_unique_data
get_reg_data()
user_data = []
users_list = []
user_inform_check = []
count = 0
count_1 = 0
while count_1 != 3:
    user_data = []
    while len(user_data) != 4:
        user_information = input(f"{my_idea()[count]} ")
        if reg_check(user_information,get_reg_data()[count], users_list) is not True:
            print(f"Неверно: {my_idea()[count]}")
            continue
        elif check_unique_data(user_information,user_inform_check):
            print(f"Неуникальные данные:{my_idea()[count]}")
            continue
        else:
            user_data.append(user_information)
            if count == 2:
                user_inform_check.append(user_information)
            if count == 3:
                user_inform_check.append(user_information)
            count += 1
        if count == 4:
            count = 0
    users_list.append(user_data)
    count_1 += 1
print(users_list)