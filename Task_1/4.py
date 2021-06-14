auth_dict = {
    'Dmitry': ['asdafefcx', True],
    'Pavel': ['sdsc98jwed', True],
    'Alex': ['akdjchlasic', False],
    'Danila': ['sdkcjrivbea', False]
}

# Сложность O(1) - константная
def try_to_auth_1(name):
    if auth_dict[name][1] == False:             # O(1) - константная
        return "Вы не активировали аккаунт"  # O(1) - константная
    else:                                       # O(1) - константная
        return 'Вы активировали аккаунт'              # O(1) - константная

# Сложность O(n) - линейная
def try_to_auth_2(name):
    for i in auth_dict.keys():                  # O(n) - линейная
        if i == name:                           # O(1) - константная
            if auth_dict[i][1] == False:        # O(1) - константная
                return "Вы не активировали аккаунт"  # O(1) - константная
            else:                               # O(1) - константная
                return 'Вы активировали аккаунт'      # O(1) - константная


inp_name_string = input('Введите ваш логин: ')
inp_pass_string = input('Введите ваш пароль: ')
if auth_dict[inp_name_string][0] == inp_pass_string:
    print(try_to_auth_1(inp_name_string))
    print(try_to_auth_2(inp_name_string))

# Решение под номером 1 более эффективное, так как является константным по сложности. А это значит, что оно занимает гораздо меньше времени на выполнение, чем решение под номером 2.