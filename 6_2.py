from dataclasses import dataclass
from memory_profiler import profile

class ShopClass:
    def __init__(self, name=""):
        self.name = name
        self.listGoods = []

@dataclass
class DataGoods:
    name:str
    price:int
    unit:str


@profile
def my_func_1():

    shop = ShopClass("MyShop")
    for _ in range(20000):
        shop.listGoods.extend([
            DataGoods("телефон", 20000, "RUB"),
            DataGoods("телевизор", 45000, "RUB"),
            DataGoods("тостер", 2000, "RUB")
        ])

@profile
def my_func_2():
    
    shop = ShopClass("MyShop")
    getGoods = lambda index: {0: ("телефон", 20000, "RUB"),
                          1: ("телевизор", 45000, "RUB"),
                          2:("тостер", 2000, "RUB")}.get(index)
    shop.listGoods = [DataGoods(*getGoods(i%3)) for i in range(20000)]

if __name__ == '__main__':
    my_func_1()
    my_func_2()

'''Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    16     17.6 MiB     17.6 MiB           1   @profile
    17                                         def my_func_1():
    18                                         
    19     17.6 MiB      0.0 MiB           1       shop = ShopClass("MyShop")
    20     27.4 MiB      0.0 MiB       20001       for _ in range(20000):
    21     27.4 MiB      0.8 MiB       40000           shop.listGoods.extend([
    22     27.4 MiB      0.0 MiB       20000               DataGoods("телефон", 20000, "RUB"),
    23     27.4 MiB      7.0 MiB       20000               DataGoods("телевизор", 45000, "RUB"),
    24     27.4 MiB      1.9 MiB       20000               DataGoods("тостер", 2000, "RUB")
    25                                                 ])



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     18.8 MiB     18.8 MiB           1   @profile
    28                                         def my_func_2():
    29                                             
    30     18.8 MiB      0.0 MiB           1       shop = ShopClass("MyShop")
    31     20.8 MiB      0.8 MiB       80001       getGoods = lambda index: {0: ("телефон", 20000, "RUB"),
    32     20.8 MiB      0.0 MiB       20000                             1: ("телевизор", 45000, "RUB"),
    33     20.8 MiB      0.0 MiB       40000                             2:("тостер", 2000, "RUB")}.get(index)
    34     20.8 MiB      1.3 MiB       20003       shop.listGoods = [DataGoods(*getGoods(i%3)) for i in range(20000)]'''

"""
Конечно, использование сторонних надстроек или модулей для ускорения - это хорошо,
но также стоит оптимизировать свои алгоритмы.
Например, ускорим часть кода, где идет добавление новых товаров в список магазина.
Для этого напишем лямбда функцию, которая будет возвращать список параметров,
которые нужны для нового товара. Также будем пользоваться списковым включением.
Списковые включения в python - очень удобная вещь, они позволяют не только ускорить наш код,
но и оптимизировать его по используемой памяти.
"""