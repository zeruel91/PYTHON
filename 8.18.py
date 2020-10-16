def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)

fib(120)

x = 1
y = 2
import matplotlib.pyplot as plt

plt.scatter(x,y,s = 200)
plt.show()
x = range(10)
y = x
plt.plot(x,y,linewidth = 4, c = 'r',label = 'line graph' )
plt.legend()
plt.grid()
plt.xticks(fontsize = 14, c = 'b')


import numpy as np
x = np.arange(-10,10,1)
plt.figure(figsize = (5,7))
for i in [1/2, 0, -2, -8]:
    plt.plot(x, i*x,label = 'y ={}x'.format(i))
plt.grid()
plt.legend(fontsize = 14, loc = 4)
plt.show()

a = 1
x = np.arange(-10,-1,1/2)
plt.figure(figsize = (5, 8))
plt.scatter(x,1/x)
plt.axvline(x = 0, c = 'k')
plt.axhline(y = 0, c = 'k')
plt.grid()
plt.show()


a = 2
x = np.arange(-10,10,1)
t = np.arange(-5,6,2)
plt.figure(figsize = (5,5))
for i in t:
    plt.plot(x,a*(x-i), label = 'shift {}'.format(i))
plt.grid()
plt.legend()


from fractions import Fraction
x = np.arange(-10,11,1)
t = np.arange(0,100,1)
plt.figure(figsize = (10,10))
for i in t:
    plt.plot(x, abs(x))
plt.show()


#Alg homework
x = '10 9 8 7 6 5 4 3 2 1' 
c = x.split(' ')
b = []

for i in c:
    b.append(int(i))

import numpy as np
x = '10 9 8 7 6 5 4 3 2 1' 

def max2(a):
    x = a.split(' ')
    b = [int(i) for i in x]
    return np.max(b)

max2(x)
#모범답안
print(sorted(list(map(int, input().split())))[-1])


