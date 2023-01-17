# 1. 
t = 0
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        t += 1
        print(t, end=' ')
    print()


# 2
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 2 * i):
        print(min(j, 2 * i - j), end='')
    print()


# 3
a , b = int(input()), int(input())
total_max = 0
digit = 0

for i in range(a, b + 1):
    max = 0
    for j in range(1, i + 1):
        if i % j == 0:
            max += j
        if max >= total_max:
            total_max = max
            digit = j
print(digit, total_max)


# 4
n = int(input())
for i in range(1, n+1):
    print(i, end= '')
    for j in range(1, i+1):
        if i%j == 0:
            print('+', end= '')
    print()


# 5
n = int(input())
while n // 10 > 0:
    n = n // 10 + n % 10
print(n)


# 6
from math import factorial
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += factorial(i)
print(sum)


# 7
a, b, = int(input()), int(input())
for i in range(a, b + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)




