# 1. Напишите функцию, которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях

def convector(num):
    return num*0.6214

num = int(input())

convector(num)

# 2. Напишите функцию, которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце. Аргумент находится в диапазоне от 1 до 12. Год является невисокосным.

def get_days(num):
    if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
        return 31
    if num == 2:
        return 28
    else:
        return 30

num = int(input())

print(get_days(num))

# 3. Напишите функцию, принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.

def get_factors(num):
    c = []
    for i in range(1, n+1):
        if n%i == 0:
            c.append(i)
    return c

n = int(input())

print(get_factors(n))

# 4. Напишите функцию, принимающую в качестве аргумента число и возвращающую количество делителей данного числа.

def number_of_factors(num):
    c = 0
    for i in range(1, n+1):
        if n%i == 0:
            c += 1
    return c

n = int(input())

print(number_of_factors(n))