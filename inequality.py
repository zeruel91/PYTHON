import numpy as np

def intersection(a,b):
    c = []
    for i in a:
        if i  in b:
            c.append(i)
    return c


class Simul_Inequality:
    def __init__(self):
        print ('x는 -10부터 10까지의 정수이다. 다음 연립부등식을 만족하는 x를 구하시오.')
        
    def question(self):
        self.coefficient = 0 , 0
        self.constant = np.random.randint(low = -10, high = 10, size = 4)
        while self.coefficient[0] == 0 or self.coefficient[1] == 0:
            self.coefficient = np.random.randint(low = -10, high = 10, size = 2)
        
        self.a = np.random.randint(4, size = 2)
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
    
        print ('{}x + {} {} {} '.format(self.coefficient[0], self.constant[0], self.symbol[0], self.constant[1]))
        print ('{}x + {} {} {} '.format(self.coefficient[1], self.constant[2], self.symbol[1], self.constant[3]))
        
    def answer(self):
        x = []
        for i, val in enumerate(self.a):
            if val % 4 == 0:
                x.append(list(filter(lambda a: self.coefficient[i]*a + self.constant[2*i] > self.constant[2*i+1],  np.arange(-10,11,1))))
            elif val % 4 == 1:
                x.append(list(filter(lambda a: self.coefficient[i]*a + self.constant[2*i] >= self.constant[2*i+1],  np.arange(-10,11,1))))
            elif val % 4 == 2:
                x.append(list(filter(lambda a: self.coefficient[i]*a + self.constant[2*i] <= self.constant[2*i+1],  np.arange(-10,11,1))))
            elif val % 4 == 3:
                x.append(list(filter(lambda a: self.coefficient[i]*a + self.constant[2*i] < self.constant[2*i+1],  np.arange(-10,11,1))))
                
        x_common = intersection(x[0], x[1])
        print (x_common)
        
q1 = Simul_Inequality()
q1.question()
q1.answer()