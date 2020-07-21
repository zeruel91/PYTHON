a = input('type anything :') 

integer = ''
string = ''
for i in range(len(a)):
    try:
        if a[i] == str(int(a[i])):
            integer += a[i]
    except ValueError:
        string += a[i]
print('{}'.format(integer))
print('{}'.format(string))



a = 6
b = 2
print(a/b)


def prime(a):
    factor = []
    for i in range(2,a):
        if a % i == 0:
            factor.append(i)
    if factor == False:
        return True
    else:
        return False
    

prime(1221234125125)

def prime_factorization(a):
    primes = []
    for i in range(2,a):
        while a % i ==0:
            primes.append(i)
            a /= i
    if primes == False:
        primes.append(a)
    return primes

prime_factorization(123)

def digit_expand(a, n):
    digit_10 = []
    while a // n != 0:
        e = a % n
        digit_10.append(e)
        a //= n
    digit_10.append(a)
    digit_10.reverse()

    return digit_10

digit_expand(128,2)