#Alg HW
a = input('str:')
b = []
'A'.islower()
'a'.upper()
a
for i in a:
    if i.islower == True:
        b.append(i.upper())
    else:
        b.append(i.lower())
print(b)
join()
a = 'ABCDefg'
b = []
for i in a:
    b.append(i)
print(b)
#########################################################
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10)

x = np.arange(-10,11)
y = 2.0**x
plt.plot(x,y)
plt.show()
plt.plot(x,int(2.0)**x,label = 'wow')


a = 2
float(a)
print(1*(0.15)*1110)

x = np.arange(0,11)
y = np.sqrt(x)
plt.plot(x,y)




def selectionSort(arr):
    newArr = arr[0]
    for i in range(len(arr)):
        if arr[i]>= newArr:
            newArr = arr[i]
    return newArr

selectionSort([5,3,6,2,10])


def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)


fib(3)

a = []
for i in range(25):
    a.append(fib(i))

print(a)


fib_list = [0,1]
def fib2(n):
    while len(fib_list) < n:
        fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list

fib2(250)

def fib3(n):
    if len(fib_list)>n+1:
        return fib_list[n]
    else:
        fib2(n)
        fib3(n)
import time
start = time.time()
fib2(2213)
end = time.time()
print(end - start)

from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma =Kkma()
pprint(kkma.nouns('u_명사만을 추출하여 워드클라우드를 그려봅니 다'))