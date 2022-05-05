# 1. Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит: 
# «Пароль принят», иначе: «Пароль не принят»
a, b = input(), input()
if a == b:
    print('Пароль принят')
else:
    print('Пароль не принят')

# 2. Напишите программу, которая определяет, является число четным или нечетным
a = int(input())
if a % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

# 3. Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: 
# сумма первой и последней цифр равна разности второй и третьей цифр
a = int(input())
if (a//1000) + (a%10) == ((a//100)%10) - ((a//10)%10):
    print('ДА')
else:
    print('НЕТ')

# 4. Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет
a = int(input())
if a >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

# 5. Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными 
# членами арифметической прогрессии
a, b, c = int(input()), int(input()), int(input())
if (b-a)+b == c:
    print('YES')
else:
    print('NO')

# 6. Напишите программу, которая определяет наименьшее из двух чисел
a, b = int(input()), int(input())
if a > b:
    print(b)
else:
    print(a)

# 7. Напишите программу, которая определяет наименьшее из четырёх чисел
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)

# 8. Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится: 
# до 13 включительно – детство; от 14 до 24 – молодость; от 25 до 59 – зрелость; от 60 – старость.
a = int(input())
if a <= 13:
    print('детство')
if 14 <= a <= 24:
    print('молодость')
if 25 <= a <= 59:
    print('зрелость')
if a >= 60:
    print('старость')

# 9. Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
a, b, c = int(input()), int(input()), int(input())
total = 0
if a > 0:
    total = total + a
if b > 0:
    total = total + b
if c > 0:
    total = total + c
print(total)