from collections import *
from timeit import timeit

my_deque = deque()
my_list = []
test_list = [i for i in range(25)]

def list_append(any_list):
    for i in any_list:
        my_list.append(i)

def deque_append(any_list):
    for i in any_list:
        my_deque.append(i)

def list_pop(any_list):
    for _ in any_list:
        my_list.pop()

def deque_pop(any_list):
    for _ in any_list:
        my_deque.pop()

def list_insert(any_num):
    for i in range(any_num):
        my_list.insert(0, i)

def deque_append_left(any_num):
    for i in range(any_num):
        my_deque.appendleft(i)

def pop_index_list(any_num):
    for _ in range(any_num):
        my_list.pop(0)

def pop_index_deque(any_num):
    for _ in range(any_num):
        my_deque.popleft()

def list_extend(any_list):
    my_list.extend(any_list)

print('list_append: ', timeit('list_append(test_list)', globals=globals()))
print('deq_append: ', timeit('deque_append(test_list)', globals=globals()))
print('list_pop: ', timeit('list_pop(test_list)', globals=globals()))
print('deq_pop: ', timeit('deque_pop(test_list)', globals=globals()))
print('list_insert: ', timeit('list_insert(25)', globals=globals(), number=10000))
print('deque_append_left: ', timeit('deque_append_left(25)', globals=globals(), number=10000))
print('pop_index_list: ', timeit('pop_index_list(10)', globals=globals(), number=1000))
print('pop_index_deque: ', timeit('pop_index_deque(10)', globals=globals(), number=1000))
'''list_append:  1.5236014269976295
deq_append:  1.4127621600018756
list_pop:  1.3404206019986304
deq_pop:  1.3183624929988582
list_insert:  19.342369926001993
deque_append_left:  0.01390088199696038
pop_index_list:  0.47824736699840287
pop_index_deque:  0.0007122220013116021'''