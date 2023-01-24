# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Enter n '))

my_list = list(map(lambda x: round((1+1/x)**x,2),range(1, n + 1)))
sum = 0
for i in range(len(my_list)):
    sum += my_list[i]
print(my_list)
print(sum)