# [1,2,3,4] 가 숫자1234 를 나타낸다고 합시다 이를 1234 로 바꿀수있는 코딩 함수

def list_to_number(a):
    b = len(a)
    result = ''
    for i in range(b):
        result += str(a[i])
    result = int(result)
    return result

b = [5,1,37,2346,438,5,1,]
list_to_number(b)

import numpy as np
i = 5
result = []
while i:
    result.append(np.random.randint(1,10))
    i -= 1

mul = 1
for i in range(len(result)):
    mul *= result[i]
print(result,mul)

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

prime_factorization(24)



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


a = np.random.randint(10,100)
b = np.random.randint(10,100)
LCM(a,b)

#
result = []
for i in range(100):
    if i % 6 == 3 and i % 8 == 5 and i % 9 == 6:
        result.append(i)
print(result)

#
result = []
for i in range(2,100):
    if i % 4 ==1 and i % 5 == 1 and i % 6 == 1:
        result.append(i)
print(min(result))

#
def list_to_number(a):
    number = ''
    for i in range(len(a)):
        number += str(a[i])
    number = int(number)
    return number

def digit_expand(a, n):
    digit_10 = []
    while a // n != 0:
    
        e = a % n
        a = a - e
        digit_10.append(e)
        a //= n
    digit_10.append(e)
    digit_10.reverse()
    
    return digit_10

print (digit_expand(1732,7))

def Number_system_change(number,n, m):
    num_str = str(number)     #325
    len_num = len(num_str)   #3
    number_10 = 0
    for i, num in enumerate(num_str):
        num_int = int(num)
        if num_int >= n:
            print ('{}is bigger or same as{}, so not {}n digit number'.format(num_int, n, n))

            break

        else:
            number_10 += num_int*n**(len_num-i-1)
        
        number_m = digit_expand(number_10,m)
        return number_m
a = Number_system_change(621,7,10)
b = Number_system_change(3213,4,10)
result = abs(list_to_number(a) - list_to_number(b)-1)
print(result)

#단순삽입법의 개념을 파악하자. 
a = [61,2,31,3,4,5]
a.insert(0,5)
a

def simple_insert(a):
  

simple_insert(a)


#응급 퀴즈
# 세 모서리 길이가 각각 48, 60, 70 cm 인 직육면체 모양의 나무 토막을 잘라서 
#될 수 있는 가장 큰 정육면체 모양의 나무토막으로 나누려한다.
# 이떄 정육면체 모양의 나무토막은 모두 몇개가 생기는지 구하세요
# 세 수의 최소공배수를 구하세요