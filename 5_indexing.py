# 9.1.1
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])


# 9.1.2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-10])


# 9.1.3
s = input()
for c in range(0, len(s), 2):
    print(s[c])


# 9.1.4
s = input()
for c in range(1, len(s)+1):
    print(s[-c])


# 9.1.5
a, b, c = input(), input(), input()
print(b[0] + a[0] + c[0])


# 9.1.6
a = input()
s = 0
for i in a:
    s += int(i)
print(s)


# 9.1.7
flag = True
s = input()
for i in range(0, len(s)):
    if s[i] in '0123456789':
        flag = False
if flag == False:
    print('Цифра')
else:
    print('Цифр нет')


# 9.1.8
a = 0
b = 0
for i in input():
    if i in '*':
        a += 1
    if i in "+":
        b += 1
print('Символ + встречается', b, 'раз')
print('Символ * встречается', a, 'раз')


# 9.1.9
s = input()
a = 0
for c in range(0, len(s)-1):
    if s[c] == s[c+1]:
        a += 1
print(a)


# 9.1.10
s = input().lower()
a = 0
b = 0
for i in range(len(s)):
    if s[i] in 'бвгджзйклмнпрстфхцчшщ':
        a +=1
    if s[i] in 'ауоыиэяюёе':
        b +=1
print('Количество гласных букв равно', b)
print('Количество согласных букв равно', a)


# 9.1.11
n = int(input())
b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2

print(b)