# 7.8.1. Дано натуральное число n (n ≤ 9). Напишите программу, которая печатает таблицу размером n × 3 состоящую из данного числа (числа отделены одним пробелом).
n = int(input())
for i in range(n):
    print(n, n, n)


# 7.8.1. Дано натуральное число (n≤ 9). Напишите программу, которая печатает таблицу размером n × 5, где в i-ой строке указано число i (числа отделены одним пробелом).
n = int(input())
for i in range(1, n+1):
    print(i, i, i, i, i)


# 7.8.1. Дано натуральное число n (n ≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n.
n = int(input())
for i in range(1, n + 1):
    for  j in range(1, 10):
        print(i,'+', j, '=', i + j)
    print() 


# 7.8.1. Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n.
n = int(input())
for i in range(1, n + 1):
    print('*' * min(i, n - i + 1))

# or
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        if i + j <= n:
            print('*', end='')
    print()


# 7.8.1. Дано натуральное число n. Напишите программу, которая печатает численный треугольник.
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end='')
    print()