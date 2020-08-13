#부등식
#Algorithm homework

def cnvt(s):
    l = list(s)
    for k in range(1,len(l),2):
        if l[k].isdigit():
            l[k] = '*'
    return ''.join(l)

print(cnvt("sd9f8d1423432ji25236366n12ijt79q7wt9w7q"))



result = []
for x in range(1,9):
    for y in range(1,9):
        if x + 2*y == 8:
            result.append([x,y])

print(result,'{}개'.format(len(result)))

for x in range(1,60):
    y = 60 - x
    if y + 12 == 2*(x + 12):
        print(x,y)

result = []
for x in [2,3,5,7]:
    if 3*x + 2 <= 11:
        result.append(True)
    else:
        result.append(False)
result
x = [2,3,5,7]


help(intersection)
# list 안에서의 for 문
a = [i for i in x if i*3 + 2 <= 11]
import numpy as np
x = np.arange(-10,10)
b = [bool(i + 5 >= 4) for i in x  ]
b

#edit plus < HTML 편집기
a = 0,0
a[1]=2






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
        self.coefficient = 0 , 0
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
        print('{}x + {} {} {} '.format(self.coefficient[0],self.constant[0],self.symbol[0],self.constant[1]))
        print('{}x + {} {} {} '.format(self.coefficient[1],self.constant[2],self.symbol[1],self.constant[3]))
    def answer(self):
        x = []
        for i, val in enumerate(self.a):
            if val % 4 == 0:
                x.append(list(filter(lambda a:self.coefficient[i]*a+
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

#Head First Python 


target = 'aaaaabbccca'

def str_multi(a):
    result = str()
    for i in range(len(a)):
        if a[i] == a[i+1]:
            
        # for j in range(1,len(a)-i):
        #     number_count = 1
        #     while a[i] == a[i + j]:
        #         number_count += 1
        #     result = result + a[i] + '{}'.format(number_count)
        #     else:
        #         result += a[i]

#Algorithm Homework

s = 'aaaabbbcccbcbcaaaa'
result = s[0]
count = 0
for i in s:
    if i == result[-1]:
        count += 1
    else:
        if count == 1:
            result += i
        else:
            result += str(count)+i
            count = 1
result += str(count)
print(result)
            


