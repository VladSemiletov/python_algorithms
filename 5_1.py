from collections import namedtuple
from collections import defaultdict

profit = namedtuple('profit', 'profit_1 profit_2 profit_3 profit_4 avr_pr')  # прибыль по кварталам, avr_pr - сред прибыль
company_name = defaultdict()  # для хранения названия компании и прибыли по кварталам (зна-ия - mnf, ключи - назв-я предпр)
sum_all = 0  # для расчета общей средней прибыли за год (по всем предприятиям)
n_low, n_high = "", ""  # для хранения названий предприятий с прибылью ниже и выше общего среднего значения

n = input('введите количество предприятий:')
for i in range(int(n)):
    nam = input(f'введите название предприятия {i+1}:')
    pr = input(f'введите прибыль за каждый квартал  предприятия {i+1}, через пробел:')
    sr = (int(pr.split()[0]) + int(pr.split()[1]) + int(pr.split()[2]) + int(pr.split()[3]))
    company_name[nam] = profit(int(pr.split()[0]),  int(pr.split()[1]), int(pr.split()[2]), int(pr.split()[3]), sr/4)   # исполь-
    # зуем  словарь

# расчет средней прибыли по всем предприятиям
for v in company_name.values():
    sum_all += v.avr_pr  # используем доступ по имени параметра avr_pr  именованного кортежа  mnf
print(f'Средняя прибыль по всем предприятиям: {sum_all / len(company_name)}')

# сортировка предприятий на предприятия со средней прибылью меньше и больше  общей средней
for r, v in company_name.items() :
    if v.avr_pr < sum_all/len(company_name):
        n_low += r + '  '
    else:
        n_high += r + '  '

print(f'Предприятия с прибылью меньше среднего значения: {n_low}')
print(f'Предприятия с прибылью больше среднего значения: {n_high}')