from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as f_users:
    with open('hobby.csv', 'r', encoding='utf-8') as f_hobby:

        with open('user_hobby.json', 'w', encoding='utf-8') as f_u_h:
            my_list = zip_longest(f_users, f_hobby, fillvalue=None)
            my_dict = {str(i[0]).strip(): str(i[1]).strip() for i in my_list}
            dump(my_dict, f_u_h, ensure_ascii=False, indent=4)
            print(my_dict)
