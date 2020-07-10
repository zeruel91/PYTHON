
class Sets(): #집합을 집합으로 연산.
    def setdata(self,  first, second):
        self.first = set(first)
        self.second = set(second)
        result = set()
    def union(self, first, second):
        for a in self.first:
            if a not in self.second:
                result = self.second|{a}
        return result
    
    def intersection(self, first, second):
        for a in self.first:
            if a in self.second:
                result = result|{a}
        return result

    def complement(self, first, second):
        for a in self.first:
            if a in self.second:
                result = self.first - a
        return result
    


a = Sets()
a.setdata({4,5,6},{5,6,7})
a.union({4,5,6},{5,6,7})

{3,4}+{4,5}
#클래스
class Sets(): #여기서 객체는 집합이 아닌 리스트
    def setdata(self, a, b):
        self.a = a
        self.b = b
        result = []
    
    def union(self):
        result = self.b + [] #리스트를 집합처럼 연산하는 방법
        for i in self.a:
            if i not in self.b:
                result.append(i)
        result.sort()
        return result
    
    def intersection(self):
        result=[]
        for i in self.a:
            if i in self.b:
                result.append(i)
        result.sort()
        return result
    
    def complement(self):
        result = [] + self.a
        for i in self.a:
            if i in self.b:
                result.remove(i)
        result.sort()

        return result

a = Sets()
a.setdata([1,2,3],[2,3,4])
a.union()
a.complement()
a.intersection()

def digit(a):
    str_number = str(a)
    n = len(str_number)
    return n

print (digit(12314141241241413123123))


def intersection(a,b):
    c = []
    for i in len(str(a)):
        if str(a)[i] in str(b):
            c += str(a)[i]
    c.sort()
    return c

print(intersection(123,234))

def intersection(a,b):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    c.sort()
    return c

def mumber_intersection(a,b):
    str_a = str(a)
    str_b = str(b)
    c = []
    c = intersection(str_a, str_b)
    c.sort()
    return c


def asd(a,b):
    int_a = int(a)
    int_b = int(b)
    if (int_a + int_b) < 2:
        print(int_a+int_b)  #print 대신 return 사용하는게 짦음.
    else:
        print(1)

asd(1,1)


def qwe(list_a):
    t = list_a.pop()
    result = t.append(list_a.remove(t))
    return result


qwe([1,2,3,4])


def rotation(list_a):
    
    new_list = []
    new_list.append(list_a[-1])
    new_list = new_list + list_a[:-1]
        
    return new_list


def rotatinon_n(list_a,n):
    for i in range(n):
        list_a = rotation(list_a)
    return list_a

a = [1,2,3,4,5,1,12,3,4]

rotatinon_n(a,5)

array = '1231312312319231'

def max(array):
    max = array[0]
    for i in range(len(array)):
        if array[i] >= max:
            max = array[i]
    return max

max(array)

def find(a,b):
    str_a = str(a)
    str_b = str(b)
    if str_a in str_b:
        return "yes there is"

    else:
        return "there is no such thing"

find(3,123123123)


array = '42351'

for i in range(len(array)):
    if array[i] == '3':
        print('찾았습니다.')

    else:
        i += 1
        if i == len(array)-1:
            print ('did not found')


def pib(n):
    a1 = 0
    a2 = 1
    
def digit(a):
    result = len(str(a))
    print(result)

def pib(a):
    if
pib(3)