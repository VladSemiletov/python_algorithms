from timeit import timeit
import random

def bubble_sort(lst_obj):
    n = len(lst_obj)
    for num in range(n):
        for i in range(len(lst_obj) - 1):
            if lst_obj[i + 1] < lst_obj[i]:
                lst_obj[i + 1], lst_obj[i] = lst_obj[i], lst_obj[i + 1]
    return lst_obj

def bubble_sort_lesson(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj

def optimized_bubble_sort(lst_obj):
    n = len(lst_obj)
    for j in range(n):
        for i in range(len(lst_obj[j:]) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
    return lst_obj

orig_list_10 = [random.randint(-100, 100) for num in range(10)]
orig_list_100 = [random.randint(-100, 100) for num1 in range(100)]
orig_list_1000 = [random.randint(-100, 100) for num2 in range(1000)]

print('bubble_sort 10', timeit('bubble_sort(orig_list_10[:])', globals=globals(), number=1000))
print('bubble_sort_lesson 10', timeit('bubble_sort_lesson(orig_list_10[:])', globals=globals(), number=1000))
print('optimized_bubble_sort 10', timeit('optimized_bubble_sort(orig_list_10[:])', globals=globals(), number=1000))
print('bubble_sort 100', timeit('bubble_sort(orig_list_100[:])', globals=globals(), number=1000))
print('bubble_sort_lesson 100', timeit('bubble_sort_lesson(orig_list_100[:])', globals=globals(), number=1000))
print('optimized_bubble_sort 100', timeit('optimized_bubble_sort(orig_list_100[:])', globals=globals(), number=1000))
print('bubble_sort 1000', timeit('bubble_sort(orig_list_1000[:])', globals=globals(), number=1000))
print('bubble_sort_lesson 1000', timeit('bubble_sort_lesson(orig_list_1000[:])', globals=globals(), number=1000))
print('optimized_bubble_sort 1000', timeit('optimized_bubble_sort(orig_list_1000[:])', globals=globals(), number=1000))

'''bubble_sort 10 0.014050212000256579
bubble_sort_lesson 10 0.011237542999879224
optimized_bubble_sort 10 0.012087029000213079
bubble_sort 100 1.039336822000223
bubble_sort_lesson 100 0.6444524220005405
optimized_bubble_sort 100 0.640804377000677
bubble_sort 1000 73.32511074600097
bubble_sort_lesson 1000 44.902309506000165
optimized_bubble_sort 1000 45.494137749999936'''

'''Вывод: Обычный пузырьковый метод показал себя хуже всего, особенно при возрастание длины массива. Метод рассмотренный 
на уроке дал такие же результаты как и метод со срезом и они оказались самыми лучшими, так как в обои случаях количество
итераций с каждым проходом уменьшается.'''