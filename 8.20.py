#Alg HW
print(result)
a = '101112131415'

a = input(':')
sum(list(map(int,list(a))))
#---------------------------------------------
import pandas as pd
import numpy as np
weight = 22,24,26,30,32,40,25,35,45,125,237,48,8,9,23,4,6,46,36,346,346,436,2,46,2,27

hist = np.zeros(6)

index = np.array([20,25,30,35,40,45])+2.5
b = pd.Series(hist,index = index) #pandas의 시리즈는
#pd.Series(data,index)
#데이터부터 왼쪽 세로로 나열
#column 2개 나옴

s = pd.Series(np.random.randn(5),index = ['a','b','c','d','e'])
s

a = {}
for i in range(5):
    a[i] = i**2
print(a)
pd.Series(a)
0 in a
16 in a #키 값만 찾음.np

s = ''
for i in range(101):
    s += str(i)
print(s)
result = 0
for i in s:
    result +=int(i)
print(result)