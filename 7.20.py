np.random.randint(-10,10,2)
np.random.randint(2,5)
import numpy as np
class integer:
    def question(self):
        self.constant = np.random.randint(-10,10,2)
        self.pm = np.random.randint(5)
        self.exponent = np.random.randint(2,5)
        if self.pm == 0:
            print('{} + {} ?'.format(self.constant[0],self.constant[1]))
            
        elif self.pm == 1:
            print('{} - {} ?'.format(self.constant[0],self.constant[1]))
            
        elif self.pm ==2:
            print('{}*{} ?'.format(self.constant[0],self.constant[1]))
            
        elif self.pm == 3:
            print('{}/{} ?'.format(self.constant[0],self.constant[1]))
            
        else:
            print('{}^{} = ?'.format(self.constant[0],self.exponent))
        

    def answer(self):
        if self.pm == 0:
            print(self.constant[0] + self.constant[1])
            
        elif self.pm == 1:
            print(elf.constant[0] - self.constant[1])
            
        elif self.pm == 2:
            print(self.constant[0] * self.constant[1])
          
        elif self.pm == 3:
            print(self.constant[0] / self.constant[1])
       
        else:
            print(self.constant[0] ** self.exponent)
        



a = integer()
a.question()
a.answer()

x = int(input('your answer? :'))
a = integer()
a.question()
while True:
    if x == a.answer():
        print('its correct')
        break
    else:
        print('incorrect. try again')




from fractions import Fraction
print(Fraction(2/4))

class Rational_number:
    def question(self):
        self.constant = np.random.randint(-10,11,4)

        self.pm = np.random.randint(4)
        if self.pm == 0:
            print('{} + {} ?'.format(
                Fraction(self.constant[0],self.constant[1]),
                Fraction(self.constant[2],self.constant[3])
            
        elif self.pm == 1:
            print('{} - {} ?'.format(
                Fraction(self.constant[0],self.constant[1]),
                Fraction(self.constant[2],self.constant[3]))
        elif self.pm ==2:
            print('{} * {} ?'.format(
                Fraction(self.constant[0],self.constant[1]),
                Fraction(self.constant[2],self.constant[3]))
            
        elif self.pm == 3:
            print('{} / {} ?'.format(
                Fraction(self.constant[0],self.constant[1]),
                Fraction(self.constant[2],self.constant[3]))
            
    
    def answer(self):
        if self.pm == 0:
            return self.constant[0]/self.constant[1] + self.constant[2]/self.constant[3]
            
        elif self.pm == 1:
            return self.constant[0]/self.constant[1] - self.constant[2]/self.constant[3]
            
        elif self.pm == 2:
            return self.constant[0]/self.constant[1] * self.constant[2]/self.constant[3]
          
        else :
            return (self.constant[0]/self.constant[1]) / (self.constant[2]/self.constant[3])
       


round(float(Fraction(7,10)))
def prime_factorization(a):
    b = range(2,a)
    primes = []
    for i in b:
        if a % i == 0 :
            primes.append(i)
            a /= i
    if primes == False:
        primes.append(a)
    primes.sort()
    return primes



def check_finite_fraction(a):
    result = []
    for i in prime_factorization(a):
        if i != 2 and i != 5:
            result.append(i)
    if result == False:
        return 'its finite fraction'
    else :
        return 'its not a finite fraction'

type(prime_factorization(10)[0])

check_finite_fraction(10)



#퀵정렬-----------------------------------------------------------------

# ? 대상의 크기가 1인가 -> 끗
#아니다 -> a[0]을픽스\
#for i in len(1,a)
#if a[i] < a[0] -> change( , )
#if a[i] > a[0]

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

##############Head First Python####################


import datetime
datetime.date.today()
        

odds = []
for i in range(1,60,2):
    odds.append(i)

odds

from datetime import datetime
right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute")

import random
dir(random)
random.shuffle(odds)
help(random.randint)
random.randint(3,5)

import time
for i in range(5):
    random.randint(1,60)
    time.sleep(5)


dir(time.start)


for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute")
    wait_time = random.randint(1,60)
    time.sleep(wait_time)

word = "bottles"
for beer_num in range(99,0,-1):
    print(beer_num,word,"of beer on the wall.")
    print(beer_num,word,"of beer")
    print("Take one down.")
    print("Pass it around")
    if beer_num == 1:
        print("No more bottles of beer on the wall")
    else:
        new_num = beer_num -1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
    print()


list(range(99,0))