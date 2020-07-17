a = 17
b = range(2,a)
print(b)
primes = []
for i in b:
    while a % i  == 0:
        primes.append(i)
        a = a/i
        continue

if primes == []:
    primes.append(a)

primes
        
def prime_factorization(a):
    b = range(2,a)
    primes = []
    for i in b:
        while a % i == 0:
            primes.append(i)
            a = a/i
    if primes == []:
        primes.append(a)
    return primes


prime_factorization(15)
prime_factorization(248)


a = 24
b = range(1,a-1)
factor = []
for i in b:
    if 24 % i == 0:
        factor.append(i)
factor.append(a)

print(factor)

def factorization(a):
    b = range(1,a-1)
    factor = []
    for i in b:
        if 24 % i == 0:
            factor.append(i)
    factor.append(a)
    return factor

factorization(24)

def intersection(a,b):
    result = []
    for i in a:
        if i in b:
            result.append(i)
    return result

a = [1,2,3,4,5]
b = [3,4,5,6,7]
intersection(a,b)

def GCD(a, b, show = False):
    c = factorization(a)
    d = factorization(b)
    if show == True:
        print(c)
        print(d)
        e = intersection(c,d)
    return max(e)


GCD(30,50, show = True) #default 값으로 트루

def LCM(a,b):
    c = prime_factorization(a)
    d = prime_factorization(b)
    e = c + d
    for i in c:
        if i in d:
            e.remove(i)
    f = 1
    for i in e:
        f = int(i)*f
    return f



LCM(35,42)

def degit_expand(a, n):
    digit_10 = []
    while a // n != 0:
        e = a % n
        digit_10.append(e)
        a //=n 

print (digit_expand(1732,7))

"""i = 0
i < 4
i = IndexMin
i+1 => k
array[k]<array[indexmin]이라면 (더 작은값이 나왔다면)
k = indexMin
k= k+1
"""
type('he')
x = input("아무거나입력하세요 : ")
if type(x) == str:
    print("x is string")
elif type(x)