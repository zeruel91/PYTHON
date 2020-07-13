n = int(input("num? : "))
a = 0; b = 1
print('0',end='')
while b <= n:
    print(', %d'%b, end='')
    a,b = b,a+b


#fib by n th
def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)

for i in range(20):
    print(fib(i), end = ' ')

print(fib(51)) #<-- 계산값이 너무커서 오류가남

import random
random.randint(0,46)