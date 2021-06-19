from hashlib import sha256
from re import findall

table_url = {}


def hash_url(url):
    if findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]))+', url):
        salt = url.split('.')
        url_h = sha256(salt[-2].encode() + url.encode()).hexdigest()
        if not url_h in table_url.values():
            if len(table_url) == 0:
                table_url[1] = url_h
                return f'Хеш добавлен - {url_h}'
            else:
                key = max(table_url.keys()) + 1
                table_url[key] = url_h
                return f'Хеш добавлен - {url_h}'
        else:
            return f'{url} - url-адрес уже есть в хеш-таблице!'
    else:
        return f'{url} - неверный url адрес!'


print(hash_url('https://github.com/'))
print(hash_url('https://hd.kinopoisk.ru/'))
print(hash_url('https://www.reddit.com/'))
print(hash_url('https://github.com/'))
print(hash_url('https/github.com'))