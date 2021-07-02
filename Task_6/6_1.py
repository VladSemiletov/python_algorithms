from timeit import default_timer
from memory_profiler import memory_usage
import gc


def decor(func):
    def wrapper(*args):
        start = default_timer()
        before = memory_usage()
        res = func(*args)
        after = memory_usage()
        end = default_timer()
        print('---------------------------------------------')
        print(f'Функция {func.__name__}:')
        print(f'\tВремя выполнения - {end - start} c')
        print(f'\tИспользуемая память - {after[0] - before[0]} MiB')
        print('---------------------------------------------')
        return res
    return wrapper

########## 1 ##########

class CarBase:  # обычный класс Car
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return 'движется'


class CarOptimize:  # оптимизированный класс Car
    __slots__ = ['name', 'color', 'speed', 'is_police']     # применим слоты
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return 'движется'


@decor
def car_base():  # создаем машину из обычного класса
    car = CarBase('ВАЗ 2106', 'красный', 80, False)
    print(car.name, car.go())


@decor
def car_optimaze():  # создаем машину из оптимизированного класса
    car = CarOptimize('Лада Веста', 'белый', 120, False)
    print(car.name, car.go())


if __name__ == '__main__':
    car_base()
    car_optimaze()

''' ВАЗ 2106 движется
---------------------------------------------
Функция car_base:
        Время выполнения - 0.2012254960000064 c
        Используемая память - 0.0 MiB
---------------------------------------------
Лада Веста движется
---------------------------------------------
Функция car_optimaze:
        Время выполнения - 0.20106598300026235 c
        Используемая память - 0.0 MiB
--------------------------------------------- '''
#Время выполнения заметно уменьшено в случае оптимизации. Так же при более больших данных количество используемой памяти гораздо меньше в случае оптимизации за счет использования _slots_

########## 2 ##########

@decor
def revers_base(m):     # рекурсивный метод "переворота" числа
    def reverse(n):
        return f'{n%10}' if n < 10 else f'{n%10}' + reverse(n//10)
    return reverse(m)


@decor
def revers_optimaze(n):     # оптимизирванный метод "переворота" числа
    return ''.join([i for i in str(n)[::-1]])


if __name__ == '__main__':
    a = 123456789012345678901234567890123456789012345678901234567890
    print(revers_base(a))
    print(revers_optimaze(a))

'''Функция revers_base:
        Время выполнения - 0.20130993200018565 c
        Используемая память - 0.0 MiB
---------------------------------------------
098765432109876543210987654321098765432109876543210987654321
---------------------------------------------
Функция revers_optimaze:
        Время выполнения - 0.20129889500003628 c
        Используемая память - 0.0 MiB
---------------------------------------------
098765432109876543210987654321098765432109876543210987654321'''
#В случае оптимизации время выполнения немного быстрее в случае оптимизации. При более длинных числах количество используемой памяти во втором случае во много раз меньше. Это хорошо.

########## 3 ##########

lst_obj = [el for el in range(1000000)]
obj = tuple(el for el in range(1000000))

@decor
def get_sum_1(lst_obj_1):
    res_1 = 0
    for el in lst_obj_1:
        res_1 += el
    return res_1


print(get_sum_1(lst_obj))


@decor
def get_sum_2(lst_obj_2):
    lst_obj_2 = lst_obj_2
    res_1 = 0
    for el in lst_obj_2:
        res_1 += el
    gc.collect()
    return res_1


print(get_sum_2(lst_obj))

'''Функция get_sum_1:
        Время выполнения - 0.2592595039996013 c
        Используемая память - 0.0 MiB
---------------------------------------------
499999500000
---------------------------------------------
Функция get_sum_2:
        Время выполнения - 0.2901359150000644 c
        Используемая память - 0.0 MiB
---------------------------------------------
499999500000'''
#Попытка оптимизации привела к ухедшению результата по времени. По количеству используемой памяти разницы не обнаружил.
