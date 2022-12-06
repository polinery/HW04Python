''' 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо
запускать скрипт с параметрами.'''

from sys import argv

script_name, time, rate_time, bonus = argv
time = float(argv[1])
rate_time = float(argv[2])
bonus = float(argv[3])


def pay(time, rate_time, bonus):
    res = time * rate_time + bonus
    return res


print(pay(time, rate_time, bonus))
