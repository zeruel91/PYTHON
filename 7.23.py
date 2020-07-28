def Card_Ord(a):
    a = str(a)
    if len(a)<= 2:
        if int(a) in [11,12,13]:
                return '{}th'.format(a)
        elif a[-1]=='1':
                return '{}st'.format(a)
        elif a[-1]=='2':
                return '{}nd'.format(a)
        elif a[-1]=='3':
                return '{}rd'.format(a)
    else:
        return '{}th'.format(a)


    
print(Card_Ord(123),Card_Ord(12),Card_Ord(1),Card_Ord(167),Card_Ord(32),Card_Ord(12),Card_Ord(2))






#수업내용

import numpy as np
a = np.zeros((5,5))
a
for idx1, val1 in enumerate(range(0,25,5)):
    for idx2, val2 in enumerate(range(1,10,2)):
        a[idx1,idx2] = val1+val2

a = np.zeros((6,4))
for idx1, val1 in enumerate(range(0,24,5)):
    for idx2, val2 in enumerate(range(1,10,2)):
b
a = np.array(range(1,25))
b = a.reshape(6,4)
for i in range(6):
    for j in range(4):
        b[i,j] = (b[i,j]*i) + j
print(b)

np.where(6 == c)[0]
b = [3,4,5,6,7]
b.index(6)
c = np.array(b)
c.index(6) #numpy has no option named 'index' 
#so,we should replace it as 'where'
np.where(6 == c)

c = np.array(range(1,26))
c.reshape(5,5)
cmax = np.max(c)
print( 'maximum is : {}'.format(cmax))
np.where(cmax == c)

def triangle_area(a,h):
    return 1/2*a*h
#                                         Matrix Caluculator
a = np.array(range(1,11))
b = np.array(range(1,11))
area = np.zeros((len(a),len(b)))
print(area.shape)
for i in range(len(a)):
    for j in range(len(b)):
        area[i,j] = triangle_area(a[i],b[j])

print(area)

Triangle_area = lambda a,b : 1/2*a*b 
Triangle_area(2,4)

answer = lambda x,y : x*y + y**2
answer(1,-2)

a = -5 
b = 3
3*a + b
-2*a + 5*b
(-a)**2+b




result=[]
cashbag = []
for a in range(5,31,5):
    for i in range(5,11):
        cash = (10000*((100-a)/100))*i
        cashbag.append(cash)
        result.append('cash discount{}%,{}books = {}'.format(a,i,cash))
print(result)
#1
#2
#3
c = max(cashbag)
c = int(c)
for i in range(len(result)):
    if str(c) in a[i]:
        print(a[i])

a = range(5,31,5)
b = range(5,11)
cost = np.zeros((len(a),len(b)))
for i in range(len(a)):
    for j in range(len(b)):
        cost[i,j] = (10000*((100-a[i])/100))*b[j]

print(cost)
np.max(cost)
np.where(np.max(cost)==cost)

a = range(1,21)
b = range(1,21)
result = np.zeros((len(a),len(b)))
for i in range(len(a)):
    for j in range(len(b)):
        result[i,j] = a[i]*b[j]
print(result)

x = range(-5,6)
y = range(-5,6)
A = lambda x,y:x**2 + 3*y
B = lambda x,y:-x-4*y**2

A_Plus_B = np.zeros((len(x),len(y)))
for i in range(len(x)):
    for j in range(len(y)):
        A_Plus_B[i,j] = A(x[i],y[j]) + B(x[i],y[j])
    



print(A(-3,-1/2)+B(-3,-1/2))
print('A+B의 크기는 {}'.format(A_Plus_B.shape))
print(A_Plus_B,'')

print(np.min(A_Plus_B))
print(np.max(A_Plus_B))
print(np.where((np.max(A_Plus_B)) == A_Plus_B))
print(np.where((np.min(A_Plus_B)) == A_Plus_B))


def quick_sort(arr):

    n = len(arr)

    if n <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater) #recursive call
        #함수 자체에 자신을 집어넣으면 반복시행. 언제까지?

arr = [7,3,1,6,5,2,4]
print(quick_sort(arr))

def Quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1]
    g_left = []
    g_right=[]
    for i in range(0,n-1):
        if a[i] <= pivot:
            g_left.append(a[i])
        else:
            g_right.append(a[i])
    return Quick_sort(g_left) + [pivot] + Quick_sort(g_right)

d = [8,12,1,9,102,25,32,98,31]
print(Quick_sort(d))

import random

result = []
for i in range(100000):
    result.append(random.randint(1,300000))



print(result)
import time
start = time.time()
time.clock(start)
Quick_sort(result)
print(time.time()-start)