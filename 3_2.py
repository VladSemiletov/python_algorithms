from hashlib import pbkdf2_hmac
from binascii import hexlify
from json import dump, load


def hash_gen(passwd, nick):
    hash_user = pbkdf2_hmac(hash_name='sha256',
                            password=passwd.encode(),
                            salt=nick.encode(),
                            iterations=10000)
    return hash_user


def validation():
    user_login = input('Введите логин: ')
    user_passwd = input('Введите пароль: ')
    passwd_gen = hexlify(hash_gen(user_passwd, user_login))

    with open('hash.json', 'w') as file:
        passwd_gen = passwd_gen.decode('utf-8')  # превращаем байты в строку для json
        dump(passwd_gen, file)

    with open('hash.json', 'r') as file:
        passwd_gen = load(file)
        print(f'В файле хранится: {passwd_gen}')
        user_passwd = input('Введите пароль ещё раз: ')
        passwd_gen = bytes(passwd_gen, encoding='utf-8')
        user_passwd = hexlify(hash_gen(user_passwd, user_login))

        if user_passwd == passwd_gen:
            return 'Пароли совпадают.\nВалидация пройдена.'
        else:
            return 'Пароли не совпадают!\nПерепройдите валидацию!'


result = validation()
print(result)