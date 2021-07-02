from timeit import timeit
import random
from statistics import median


def gnome_sort(lst_obj):
    i = 1
    j = 2
    while i < len(lst_obj):
        if lst_obj[i - 1] <= lst_obj[i]:
            i = j
            j += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            i -= 1
            if i == 0:
                i = j
                j += 1
    return lst_obj


m = int(input('Введите натуральное число: '))
orig_list = [random.randint(0, 100) for _ in range(2 * m + 1)]

print(f'Медиана Гномьей сортировки: {gnome_sort(orig_list[:])[m]}')
print(f'Поиск с помощью Гномьей сортировки: '
      f'{timeit("gnome_sort(orig_list[:])[m]", globals=globals(), number=1000)}')
print(f'Медиана из библиотеки statistics: {median(orig_list)}')
print(f'Поиск функецией из библиотеки statistics: '
      f'{timeit("median(orig_list[:])", globals=globals(), number=1000)}')

'''Вывод: встроенная функция работает гораздо лучше любой сортировки, которая написана нами вручную.'''