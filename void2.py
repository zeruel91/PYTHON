n = int(input("num? : "))
a = 0; b = 1
print('0',end='')
while b <= n:
    print(', %d'%b, end='')
    a,b = b,a+b


