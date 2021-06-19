from time import time

test_lst = []
test_dict = {}
n = 10000

def test_lst_append(n): #O(1), так как мы знаем, что n = 10000
    start = time()
    for i in range(n):
        test_lst.append(i)
    end = time()
    return f'Заполнение списка методом append выполнено за: {end - start} сек'

print(test_lst_append(n))

def test_lst_insert(n): #O(n), так как .insert является линейным
    start = time()
    for i in range(n):
        test_lst.insert(0, i)      
    end = time()
    return f'Заполнение списка методом insert выполнено за: {end - start} сек'

print(test_lst_insert(n))

def fill_dict(n): #O(1)
    start = time()
    for i in range(n):
        test_dict[i] = i
    end = time()
    return f'Заполнение словаря выполнено за: {end - start} сек'

print(fill_dict(n))

def remove_lst(lst): #O(n)
    start = time()
    for i in range(len(lst)):       
        lst.pop()                   
    end = time()
    return f'Удаление всех эл-ов (лин-ая сложн) из списка заняло: {end - start} сек'

def remove_lst_(lst): #O(1)
    l = len(lst)
    start = time()
    for i in range(l):       
        lst.pop(i)           
    end = time()
    return f'Удаление всех эл-ов (конст. сложность) из списка заняло: {end - start} сек'

print(remove_lst(test_lst))
print(remove_lst_(test_lst))

def remove_dict(dct): #O(n)
    start = time()
    for i in range(len(dct)):   
        dct.popitem()           
    end = time()
    return f'Удаление всех эл-ов из словаря (лин. сложн.)заняло: {end - start} сек'

def remove_dict_(dct): #O(1)
    n = len(dct)
    start = time()
    for i in range(n):          
        dct.popitem()           
    end = time()
    return f'Удаление всех эл-ов из словаря (конст. сложн.) заняло: {end - start} сек'

print(remove_dict(test_dict))
print(remove_dict_(test_dict))
#Вывод: для заполнения списка лучше использовать метод append, так как он занимает гораздо меньше времени
#В случаях удаления элементов из списка и словаря использовались линейные и константные сложности. Для n=10000 себя лучше показал константный метод.
