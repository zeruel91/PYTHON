class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self,num):
        self.result -= num
        return self.result
    

cal1 = Calculator() #cal1이 어떤 클라스로 연산할지를 지시.
cal2 = Calculator()
# (연산이름 클래스 같은 사전정의 필요.).(클래스 내에서의 연산)((대상숫자))
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))



class Four:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self, first, second):
        result = self.first + self.second
        return result
    
    def sub(self,first,second):
        result = self.first - self.second
        return result
    
    def mul(self, first, second):
        result = self.first * self.second
        return result
    
    def dev(self, first, second):
        result = self.first / self.second
        return result
a = Four()
a.setdata(4,2)
a.sub(4,2)
b = Four()
b.setdata(3,5)
b.mul(3,5)
