"저번시간 Algorithm"

S = [1,3,4,8,13,17,20]

shortest = S[1]-S[0]
index = 0

for g in range(1,len(S)):
    if S[g]-S[g-1] < shortest:
        shortest = S[g]-s[g-1]
        index = g

print(S[index-1],S[index])

import numpy as np
from fractions import Fraction

A = np.array(S)
A*3


#연립 1차방정식 풀이 (식 두개)
def simultaneous_eq(a,b):
    a = np.array(a)
    b = np.array(b)
    c = b*Fraction(a[0],b[0])
    d = a - c
    y = Fraction(d[2],d[1])
    x = a[2]-a[1]*Fraction(y,a[0])
    return x,y

a = [2, 3, 4]
b = [3, -4, -4]
x, y = simultaneous_eq(a,b)
print(x,y)

def simultaneous_eq(a,b):
    if (a[0]/b[0]) == (a[1]/b[1]) != (a[2]/b[2]):
        print('impossible')
        return None, None
    elif (a[0]/b[0]) == (a[1]/b[1]) == (a[2]/b[2]):
        print('indefinite')
    else:
        if a[0] == 0:
            y = Fraction(a[2],a[1])
            x = Fraction(b[2] - b[1]*y, b[0])
        elif a[1] == 0:
            x = Fraction(a[2],a[0])
            y = Fraction(b[2]-b[0]*x,b[1])
        elif b[0] == 0:
            y = Fraction(b[2],b[1])
            x = Fraction(a[2]-a[1]*y,a[0])
        elif b[1] == 0:
            x = Fraction(b[2],b[0])
            y = Fraction(a[2] - a[0]*x,a[1])
        else:
            a = np.array(a)
            b = np.array(b)
            c = b*Fraction(a[0],b[0])
            d = a - c
            y = Fraction(d[2],d[1])
            x = Fraction(a[2]-a[1]*y,a[0])
        return x,y

a = Fraction(3,28)
a

import time
# start = time.time()
# a = list(range(2,100000))
# def prime(a):
#     result = a
#     for i in result:
#         b = []
#         for j in range(2,i+1):
#                 if i % j== 0:
#                     b.append(j)
#         if len(b) != 1:
#             for s in range(2,max(result)):
#                 if i*s in result:
#                     result.remove(i*s)
#     return result

# b = prime(a)
# end = time.time()
# print('time = {}'.format(end - start))

a = list(range(2,100000))
def prime(a):
    
todos = open('todos.txt','a') #open file with append-mode
print('Put out the trash.',file= todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.',file=todos)
todos.close() #ALWAYS close the file after the work is done

tasks = open('todos.txt')#아무 문자도 추가 안하면 디폴트로 reading
for chore in tasks:
    print(chore,end='')
tasks.close()

with open('todos.txt') as tasks: #with 을 쓰면알아서 닫는다.
    for chore in tasks:
        print(chore, end='')