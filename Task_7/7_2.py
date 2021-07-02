from timeit import timeit
import random


def merge_sort(x):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


orig_list10 = [random.uniform(0, 50) for _ in range(10)]
orig_list100 = [random.uniform(0, 50) for _ in range(100)]
orig_list1000 = [random.uniform(0, 50) for _ in range(1000)]
print('10', '\n', 'Исходный массив', orig_list10, '\n', 'Отсортированный массив', merge_sort(orig_list10[:]), '\n',
      timeit('merge_sort(orig_list10[:])', globals=globals(), number=1000))
print('100', '\n', 'Исходный массив', orig_list100, '\n', 'Отсортированный массив', merge_sort(orig_list100[:]), '\n',
      timeit('merge_sort(orig_list100[:])', globals=globals(), number=1000))
print('1000', '\n', 'Исходный массив', orig_list1000, '\n', 'Отсортированный массив',
      merge_sort(orig_list1000[:]), '\n', timeit('merge_sort(orig_list1000[:])', globals=globals(), number=1000))