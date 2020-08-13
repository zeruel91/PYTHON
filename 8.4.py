#algorithm HW

def Mabu(n):
    i = n
    bulb = 'no'
    c = 0
    while i != 0:
        if n % i == 0:
            c += 1
        if c % 2 == 0:
            bulb = 'no'
        else:
            bulb = 'yes'
        print('{}th time of lunacy'.format(n-i+1),end=':')
        print(bulb)
        i -= 1
        
    print('"mabu" gets a sanity now')


Mabu(12)

#another way 
def factorization(a):
    b = range(1,a-1)
    factor = []
    for i in b:
        if a % i == 0:
            factor.append(i)
    factor.append(a)
    return factor #7/15일에 한factorization함수를 불러온다.

def Mabu_2(n):
    if len(factorization(n)) % 2 == 0:
        print('no')
    else:
        print('yes')

Mabu_2(12)#<-- 테스트케이스마다 한줄씩 출력되진 않고, 결과값만을 출력


a = [1,2,3,4,5,6,7,8,9]
for idx , val in enumerate(a):
    print(idx,val)

import numpy as np

a = np.random.randint(1,45,size = 6)
while list(set(a)) != list(a):
    a = np.random.randint(1,45,size = 6)
print(a)

###########
#소수점 몇자리에서 반올림하겠느냐는 연산 round
round(float(Fraction(2,7)),6)

round(103,1)

#np.zeroes((2,5)) Matrix