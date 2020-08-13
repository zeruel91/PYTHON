import numpy as np
def intersection(a,b):
    c = []
    for i in a:
        if i in b:
            c.append(i)
    return c

class Simul_inequality:
    def __init__(self):
        print('let x be integer btw (-10,10). find the soultion for equations')
    def question(self):
        self.coefficient = 0, 0
        self.constant = np.random.randint(low = -10,high = 10, size = 4)
        while self.coefficient[0] == 0 or self.coefficient[1] == 0:
            self.coefficient = np.random.randint(low = -10, high = 10, size = 2)
        
        self.a = np.random.randint(4, size = 2)#부호결정 난수
        self.symbol = []
        for i in self.a:
            if i % 4 == 0: 
                self.symbol.append('>')
            elif i % 4 == 1: 
                self.symbol.append('>=')
            elif i % 4 == 2: 
                self.symbol.append('<=')
            elif i % 4 == 3: 
                self.symbol.append('<')
        print('{}x + {} {} {} '.format(self.coefficient[0],
        self.constant[0],self.symbol[0],self.constant[3]))
        print('{}x + {} {} {} '.format(self.coefficient[1],
        self.constant[2],self.symbol[1],self.constant[3]))
    def answer(self):
        x = []
        for i, val in enumerate(self.a):
            if val % 4 == 0:
                x.append(list(filter(lambda a : self.coefficient[i]*a+
                self.constant[2*i]> self.constant[2*i+1], np.arange(-10,11,1))))
            elif val % 4 == 1:
                x.append(list(filter(lambda a:self.coefficient[i]*a+
                self.constant[2*i]>=self.constant[2*i+1], np.arange(-10,11,1))))
            elif val % 4 == 2:
                x.append(list(filter(lambda a:self.coefficient[i]*a+
                self.constant[2*i]<=self.constant[2*i+1], np.arange(-10,11,1))))
            elif val % 4 == 3:
                x.append(list(filter(lambda a:self.coefficient[i]*a+
                self.constant[2*i]< self.constant[2*i+1], np.arange(-10,11,1))))
            
            x_common = intersection(x[0],x[1])
            print(x_common)
  

np.arange(-10,11,1)

a = Simul_inequality()
a.question()
a.answer()
a = np.random.randint(4, size = 2)
a[0]
while a[0]==0:
    a[0] = np.random.randint(3,size=2)
print(a)




print(enumerate(range(0,35,3)))
import numpy as np

array = np.array(range(1,25))
b = array.reshape((6,4)) #<-- (6,4) 로 걍 해도 됨

for i in range(6):
     for j in range(4):
         b[i,j] = i*j



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
        print('left = {}'.format(Quick_sort(g_left)),'pivot = {}'.format([pivot]),'right ={}'.format(Quick_sort(g_right)),'result = {}'.format(Quick_sort(g_left) + [pivot] + Quick_sort(g_right)))
    return Quick_sort(g_left) + [pivot] + Quick_sort(g_right)

d = [8,12,1,9,102,25,32,98,31]
print(Quick_sort(d))


import numpy as np

result = np.arange(2,10,1)
result[1]

#1. is it optimized form for Eratosthenes sieve?

def Eratosthenes_sieve(a):
    result = [i for i in a if i != 1]
    for i in result:
        for j in result:
            if j%i == 0 and j>i:
                result.remove(j)
    return result

#2. 스타트타임과 엔드 타임을 적고 뺄셈을하는게 번잡스럽습니다.
#   간단하게 코드실행 시간을 체크할수있는 다른방법이있을까요?
import time
start = time.time()
Eratosthenes_sieve(list(range(2,10000)))
end = time.time()
print(end-start)

#3. 아래 코드는 수업시간에 실행하지 않았지만 PPT에 있는것을 그대로 옮겨적은것입니다.
# 한시간넘게 살펴보았지만 어떻게 index error 가 생겼는지 확인하지 못했습니다.
#   오타도 없고 오류도 없는데 a.answer()만 안나오는 이유가 궁금합니다.
