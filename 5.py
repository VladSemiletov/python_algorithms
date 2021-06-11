class StackClass:
    def __init__(self):
        self.max_size = 6
        self.min_size = 0
        self.current_stack = 0
        self.elems = [[]]

    def is_empty(self):
        return self.elems[0] == []

    def push_in(self, el):
        if len(self.elems[self.current_stack]) == self.max_size:
            self.elems.append([])
            self.current_stack += 1
        self.elems[self.current_stack].append(el)

    def pop_out(self):
        if len(self.elems[self.current_stack]) == self.min_size:
            self.elems.pop(self.current_stack)
            self.current_stack -= 1
        return self.elems[self.current_stack].pop()

    def get_val(self):
        return self.elems[self.current_stack][len(self.elems[self.current_stack]) - 1]

    def stack_size(self):
        return len(self.elems[self.current_stack]) + self.current_stack * 6


if __name__ == '__main__':
    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(4.2)
    SC_OBJ.push_in(4.2)
    SC_OBJ.push_in(4.2)

    # получаем значение первого элемента из вершины стека, но не удаляем сам элемент
    # из стека
    print(SC_OBJ.get_val())  # 5.5

    # узнать размер стека
    print(SC_OBJ.stack_size())  # 4

    # проверка пустой ли стек
    print(SC_OBJ.is_empty())  # стек не пустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # убираем элемент с вершины и возвращаем его значение
    print(SC_OBJ.pop_out())  # 4.4

    # снова убираем элемент с вершины и возвращаем его значение
    print(SC_OBJ.pop_out())  # 5.5
    print(SC_OBJ.pop_out())  # 5.5
    print(SC_OBJ.pop_out())  # 5.5
    print(SC_OBJ.pop_out())  # 5.5

    # узнать размер стека теперь
    print(SC_OBJ.stack_size())