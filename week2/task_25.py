"""Определите сумму всех элементов последовательности,
 завершающейся числом 0.

Формат ввода

Вводится последовательность целых чисел, оканчивающаяся числом 0
(само число 0 в последовательность не входит,
а служит как признак ее окончания).

Формат вывода

Выведите ответ на задачу."""

n = int(input())
sum = 0
while n != 0:
    sum += n
    n = int(input())
print(str(sum))
