#두 수가 주어져 처음을분자 두번째 수를 분모
# 로 할때 유한 소수인지 무한소수인지 판별하는 코딩함수를 만드세요.
def prime_factorization(a):
    primes = []
    for i in range(2,a):
        if a % i == 0:
            primes.append(i)
            a /= i
    if primes == False:
        primes.append(a)
    return primes

import numpy as np
from fractions import Fraction
Fraction(2,4)

def finite_OX(a,b):
    finite = True
    result = prime_factorization(b)
    for j in prime_factorization(a):
        if j in result:
            result.remove(j)
    for i in result:
        if i != 2 and i != 5:
            finite = False
    return finite

#지난시간 알고리즘 문제
finite_OX(3,15)

names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌".split(",")
a
a = [i[0] for i in names]
print("김씨 : %d\n이씨 : %d\n"%(a.count("김"),a.count("이")))#포맷여러개일떄 괄호로묶기
print(names.count("이재영"))


#Lambda

plus_5 = lambda x: x+5
plus_5(7)

plus_5(np.array([1,2,3,4,5]))

a = [1,2,3,4,5]
b = {1,2,3,4,5}

even = lambda x: x % 2 == 0
print(even(np.array([range(1,11)])))

np.array(a)+3

#BMI
BMI = lambda a,b: a/b**2
def obesity(a,b):
    if BMI(a,b)>35:
        return "고도 비만"
    elif BMI(a,b)>30:
        return "중등도 비만"
    elif BMI(a,b)>25:
        return "경도 비만"
    elif BMI(a,b)>23:
        return "과체중"
    elif BMI(a,b)>=18.5:
        return "정상"
    else:
        return "저체중"


obesity(85,1.88)

list(filter(even,range(1,11)))
list(filter(lambda x:x%2==0,[3,1,4,2,9]))#코딩의길이를 줄이는 효과



#7.21 Algorithm Problem //
result = 0
for i in range(24):
    for j in range(60):
        if '3' in str(i) or str(j):
            result += 60
print(result)
  


#head first python###########################


import numpy as np
import random
wait_time = random.randint(1,60)
wait_time

a = [1,2,3,4,5]
a.insert(3,4) #3위치에 4를 넣어라


import time
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
    time.sleep(1)
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

phrase[0::2]
book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
''.join(booklist[0:3])
''.join([phrase[1:3],' ',phrase[4],phrase[7],phrase[6]])