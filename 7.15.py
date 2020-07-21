#복습

def prime_factorization(a):
    b = range(2,a)
    primes = []
    for i in b:
        while a % i == 0:
            primes.append(i)
            a /= i
    if primes == []:
        primes.append(a)
    return primes


try:
    num = eval(input("type :")) #eval < 숫자전환 함수
    if num - int(num):
        print("fraction")
    else:
        print("integer")
except:
    print('math error')


    #ALGORITH
a = input('type anything :') 

integer = ''
string = ''
for i in range(len(a)):
    try:
        if a[i] == str(int(a[i])):
            integer += a[i]
    except ValueError:
        string += a[i]
print('{}'.format(integer))
print('{}'.format(string))





#--
def intersection(a,b):
    result = []
    for i in a:
        if i in b:
            result.append(i)
    return result

def factorization(a):
    b = range(1,a-1)
    factor = []
    for i in b:
        if 24 % i == 0:
            factor.append(i)
    factor.append(a)
    return factor
def GCD(a, b, show = False):
    c = factorization(a)
    d = factorization(b)
    if show == True:
        print(c)
        print(d)
        e = intersection(c,d)
    return max(e)
def LCM(a,b):
    c = prime_factorization(a)
    d = prime_factorization(b)
    e = c + d
    for i in c:
        if i in d:
            e.remove(i)
    f = 1
    for i in e:
        f = int(i)*f
    return f
def digit_expand(a, n):
    digit_10 = []
    while a // n != 0:
    
        e = a // n
        digit_10.append(e)
        a = a/n

print (digit_expand(1732,7))

def Number_system_change(number,n, m):
    #num : 변형하려는 숫자
    #n : 현재 진법
    #m : 결과 진법
    # number의 각 숫자가 n 보다 크거나 같으면 오류

    num_str = str(number)       #325
    len_number = len(num_str)   #3
    for i, num in enumerate(num_str):
        num_int = int(num)
        if num_int >= n:
            print ('{}is bigger or same as{}, so not {}n digit number'.format(num_int, n, n))

            break

        else:
            number_10 += num_int*n**(len_num-i-1)
        
        number_m = digit_expand(number_10,m)
        return number_m
#class 로만들기
import numpy as np
class Natural_number:
    def question(self):
        self.select = np.random.randint(5)#문제발생난수
        self.n1 = np.random.randint(100)#문제에쓸 난수들 
        self.n2 = np.random.randint(100)
        self.n3 = np.random.randint(low = 2, high = 10)
        self.n4 = np.random.randint(low = 2, high = 30)

        if self.select ==0:#문제에 대한 텍스트들
            print('determind if {} is prime, if not, find diverder'.format(self.n1))
        elif self.select == 1:
            print ('find GCD with {} and {}'.format(self.n1,self.n2))
        elif self.select == 2:
            print ('find LCM with {} and {}'.format(self.n3,self.n4))
        elif self.select == 3:
            print('{} by binary '.format(self.n1))
        elif self.select == 4:
            self.n4_2 = digit_expand(self.n4,2)
            print('binary [{}] to decimal'.format(', '.join(map(str,self.n4_2))))

        def answer(self):
            if self.select == 0:
                if is_prime2(self.n1):
                    print('{}is prime'.format(self.n1))
                else:
                    print( factorization(self.n1))
            elif self.select == 1:
                print (GCD(self.n1,self.n2, show = False))
            elif self.select == 2:
                print (LCM(self.n1, self.n2))
            elif self.select == 3:
                print (digit_expand(self.n1,2))
            elif self.select == 4:
                print (digit_expand(self.n4,10))

q1 = Natural_number()
q1.question()


#교환정렬법

def sort_change(a):
    b = len(a)
    for j in range(b):
        if j != b -1:
            for i in range(b-1-j):
                if a[b-1-i] < a[b-1-i-1]:
                    a[b-1-i],a[b-1-i-1] = a[b-1-i-1],a[b-1-i]
    return a


a = [6,5,41,2,3,6,4,1,2,3,4,5,6,7,2,7,8,8,10]
sort_change(a)

#숙제풀이

while True:
    user = input("input")
    string = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    str = ''
    int = ''
    for i in user:
        if i in string or i in string.upper():
            str += i
        if i in number:
            int += i
        print("str:{}\nint:{}\n".format(str,int))
#2
inp = input("input:\n")
str = ""
int = ""
for i in range(0,len(inp)):
    if ord(inp[i])>47 and ord(inp[i])<58: #유니코드번호로 구분
        int += inp[i]



ord('')