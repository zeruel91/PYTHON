a = []
for i in [3,5,6,8,9]:
    if i % 2 == 0 :
        a.append(2*i)

print(a)

a = [2*x for x in [3,5,6,8,9]]
b = [x%7 for x in range(10,20)]
a = [2*x for x in [3,5,6,8,9] if x % 2 == 0]
def is_prime2(a):
    b = range(2,a)
    c = 0
    for i in b:
        if a % i == 0:
            c += 1
    if c > 0 :
        d = False
    else:
        d = True
    return d

d = [-x for x in range(2,101) if is_prime2(x)]
d


def prime_factorization(a):
    b = range(2,a)
    primes = []
    for i in b:
        while a % i == 0:
            primes.append(i)
            a /= i
    if primes == []:
        primes.append(a)
    return primes

from fractions import Fraction
Fraction(3,15).denominator


def finite_OX(a,b):
    finite = True
    result = prime_factorization(Fraction(a,b).denominator)
    for i in result:
        if i != 2 and i != 5:
            finite = False
    return finite

finite_OX(3,15)

e = [Fraction(1,x) for x in range(1,101) if finite_OX(1,x)]
e

for i in range(2,100):
    if i%4 == i%5== i%6 == 1:
        print(i)

########## sort of things about 'numpy' #############
import numpy as np
help(np.where)

a = [1,2,3,4,5]
b = np.array(a)
print(b)
type(b)
c = [1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]
d = np.array(c)
d[:,3]

a = [x for x in range(1,26)]
a = np.array(a)
a.reshape(5,5)

a = [3*x for x in range(1,41)]
a = np.array(a)
c = a.reshape(8,5)
print(c)
d = a.reshape(4,10)
print(d)
a.reshape(2,20)

print(np.zeros((5,5)))



#Algorithm for 7.22
a = '4727442525'
len(list(a))
set(a)
a = '1234567890'
len(set(a))
len(a)
{2,1} == {1,2}
set(range(0,10))
set(str(x) for x in range(0,10))


def once(a):
    if set(a) == set(str(x) for x in range(0,10)):
        if  len(a) == len(set(a)):
            return True
    else: 
        return False
once(input('input number array : '))

#Answer
a = input("put 0~9 number :")
print('true'if len(a) == len(set(a))==10 else 'false')



#QuickSort


def change(x , i, j):
    x[i], x[j] = x[j], x[i]

def Select(x, l, r):
    select_val = x[l]
    select_idx = l
    while l <= r:
        while l <= r and x[l] <= select_val:#괜찮을땐 패스
            l += 1
        while l <= r and x[r] >= select_val:#왼쪽부터 체크해서 
            r -= 1                          #걸리면 오른쪽에서 찾기
        if l <= r:#
            change(x, l, r)
            l += 1
            r -= 1
    change(x, select_idx, r)
    return r

def quickSort(x, pivotMethod = Select):
    def Qsort(x, first, last):
        if first<last:
            splitP = pivotMethod(x, first, last)
            Qsort(x, first, splitP - 1)
            Qsort(x, splitP + 1, last)
    Qsort(x, 0, len(x)-1)

x = [5,2,8,6,1,9,3,7]
quickSort(x)
print(x)
help(pivotMethod())
