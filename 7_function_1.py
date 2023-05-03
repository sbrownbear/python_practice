# 1. Напишите функцию, которая выводит звездный прямоугольник с размерами 10×14
def draw_triangle():
    print('*'*10)
    for i in range(14):
        print('*        *')
    print('*'*10)

draw_triangle()


# 2. Напишите функцию, которая выводит звездный прямоугольный треугольник с катетами, равными 10
def draw_triangle_2():
    for i in range(11):
        print('*' * i)

draw_triangle_2()


# 3. Напишите функцию draw_triangle(fill, base), которая принимает два параметра: символ 
# заполнитель; величина основания равнобедренного треугольника
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        print(fill * min(i, base - i + 1))

fill = input()
base = int(input())

draw_triangle(fill, base)


# 4. Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра: имя человека; 
# фамилия человека; отчество человека; а затем выводит на печать ФИО человека в верхнем регистре.
def print_fio(name, surname, patronymic):
    print((surname[0]+name[0]+patronymic[0]).upper())
    pass

name, surname, patronymic = input(), input(), input(),

print_fio(name, surname, patronymic)


# 5. Напишите функцию, которая принимает одно целое число num и выводит на печать сумму его цифр.
def print_digit_sum(n):
    c=0
    while n!=0:
        b=n%10
        c+=b
        n=n//10
    print(c)

n = int(input())

print_digit_sum(n)