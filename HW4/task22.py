# -*- coding: utf-8 -*-

"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке 
возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого 
множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены
только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте 
выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из 
управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед 
некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального 
числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном 
файле грядки.
"""

from collections import deque, Counter


def intersect(lst_a: list, lst_b:list) -> list:
    lst_c: list = []
    for item in lst_a:
        if item not in lst_c:
            min_count = min(lst_a.count(item), lst_b.count(item))
            lst_c += [item] * min_count
    return sorted(lst_c)
3

def intersectc(lst_a: list, lst_b:list) -> list:
    return sorted(list((Counter(lst_a) & Counter(lst_b)).elements()))

def blueberry(lst: list) -> int:
    lst_out: list = []
    for i in range(0, len(lst)):
        lst_out.append((lst[i - 2::1][0], lst[i - 1::1][0], lst[i::1][0]))
    return max(list(map(lambda x: sum(x), lst_out)))


def blueberryc(lst: list) -> int:
    res: int = 0
    deq = deque(lst)
    for _ in range(0, len(lst)):
        deq.rotate(-1)
        s: int = sum(list(deq)[:3:])
        if res < s:
            res = s
    return res


if __name__ == '__main__':
    in_lst = list(map(int, list(input('Введите список целых чисел через пробел: ').split(" "))))
    print(f'Максимальное числа ягод, которое система может собрать за один заход, находясь над некоторым кустом грядки: {blueberry(in_lst)}')
    print(f'Максимальное числа ягод, которое система может собрать за один заход, находясь над некоторым кустом грядки: {blueberryc(in_lst)}')

    in_lst_a = [5, 2, 4, 20, 4, 7, 1, 1, 4]
    in_lst_b = [4, 1, 24, 20, 8, 4, 1, 1, 4, 4, 4]
    print(intersect(in_lst_a, in_lst_b))
    print(intersectc(in_lst_a, in_lst_b))