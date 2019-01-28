"""Программа получает на вход последовательность целых неотрицательных чисел,
каждое число записано в отдельной строке.
Последовательность завершается числом 0,
при считывании которого программа должна закончить свою работу
и вывести количество членов последовательности
(не считая завершающего числа 0).

Числа, следующие за числом 0, считывать не нужно.

Формат ввода

Вводится последовательность целых чисел, заканчивающаяся числом 0.

Формат вывода

Выведите ответ на задачу.

Примечание

По этой задаче возникает непонимание. Например, как ввести первый тест,
если после ввода нуля программа завершает работу
и не дает ввести оставшееся число 5?

Можно ввести несколько строчек за раз (в том числе и полный тест),
скопировав и вставив их."""

n = int(input())
i = 0
while n != 0:
    i += 1
    n = int(input())
print(i)
