x = (5 + 3)/2
x
import numpy as np
from sympy import Symbol, solve
import sympy
def linear_eq(a,b,c):
    x = (c - b)/a
    return x


def linear_eq(a,b,c):
    x = (c - b)/a
    if x - int(x) == 0:
        return int(x)
    elif a == 0:
        return 'it is not possible'
    elif b == c:
        return 'regardless of x, the equation is true'
    else:
        return x

help(denominator)

from fractions import Fraction 

# 답안

def linear_eq(a,b,c):
    x = Fraction((c-b),a)
    if x.denominator == 1:#기약분수의 분모
        x = int(Fraction(x))
    return x

linear_eq(2,-3,5)

np.exp(1)

import random


class random_linear:
    def create_prob(self):
        self.coefficient = random.randint(0,100)
        self.constant1 = random.randint(0,100)
        self.constant2 = random.randint(0,100)
        return '{}x + {} = {}'.format(self.coefficient,self.constant1,self.constant2)
    def sol(self):
        if self.constant1 == self.constant2:
            return 'all the x is solution of the linear equation'
        elif self.coefficient == 0:
            return 'there is no solution for this equation'
        else:
            self.sol = (self.constant2 - self.constant1)/self.coefficient
            return 'the answer is {}'.format(self.sol)

for x in range(1,10000000):
    a = x + 100
    b = x
    if a//b == 10 and a%b == 1:
        print(x , 2*x+100)

for i in range(1,25):
    j = 50 - i
    if i // j != 2 and i % j == 3:
        print(i,j)

for i in range(1,100):
    if i % 2 == 1 and 3*i == 87:
        print(i + 2)


for i in range(0,30):
    if i % 2 == 0 and 3*i == 30:
        print(i - 2)


for i in range(10,100):
    if i%10 == 4:
        x = 4*10 + (i - 4)/10  #혹은 i//10 으로 해도 그만임.
        if x + 9 == i:
            print(i)



a = random_linear()
a.create_prob()
a.sol()

#7.27 Algorithm homework
s = [1,3,4,8,13,17,20]

def distance(a,b):
    result = abs(a-b)
    return result

distances = dict()
for i in s:
    for j in s:
        if i != j:
            distances[distance(i,j)]=(i,j)

a = min(distances.keys())
print('the minimum distance is {}'.format(a),'which is subtraction between{}'.format(distances[a]))



import time
start = time.time()
def divider(a):
    result = []
    for i in range(1,a+1):
        if a % i == False:
            result.append(i)
    return result

prime = [] 
for x in range(100000):
    if len(divider(x)) == 2:
        prime.append(x)
print(prime)        

end = time.time()
print('this code takes {}seconds'.format(end-start))


def is_prime(a):
    if a == 2:
        return True
    comp = []
    for i in range(2,a):
        if a % i == 0:
            comp.append(i)
    if bool(comp) == False:
        return True
    else:
        return False

is_prime(13)


################ 모든항목변경 단축키 = Ctrl + F2 ############
a = range(1,101)
prime_numbers = []
for i in a:
    c = is_prime(i)
    if c == True:
        prime_numbers.append(i)
print(prime_numbers)