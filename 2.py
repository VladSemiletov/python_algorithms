from random import randint
# O(n**2)
def min_1_st(lst):
    for i in lst:
        min = True
        for j in lst:
            if i > j:
                min = False
        if min:
            return i
# O(n)
def min_second(lst):
    second_min = lst[0]
    for i in lst:
        if i < second_min:
            second_min = i
    return second_min

lst1 = [randint(0, 1000) for i in range(10)]
print(lst1)
print(min_1_st(lst1))
print(min_second(lst1))
