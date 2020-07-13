#함수에 대한 내용 -> def ~ return

a = []

for n in range(101):
    if n%2 == 1:
        a.append(n)
        n+=1
    else:
        n+=1
print(a)


from timeit import default_timer as timer
start = timer()
def prime_numbers(n):
    out = list()
    for x in range(1, n+1):
        if (x % i != 0 for i in range (2, int(x**.5)+1)):
            if all(x % t !=0 for t in x):
                out.append(x)
    return out
end = timer()
print (end -start)

from timeit import default_timer as timer
start = timer
a = [1,2,3,1]
new_a = []
for i in a:
    if i not in new_a:
        new_a.append(i)
print(new_a)



a = [ 1,2,3,]

b = [4, 5, 6]
c = a + b
print(c)


c = []
for s in a:
    if s not in b:
        c.append(s)
c = c + b
c.sort()
print(c)


a = [1, 2, 3]

b = [4, 5, 6]
c = list()
for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in c:
        c.append(i)
c.sort(c)
print(c)

a = ['apple', 'melon', 'orange']
b = ['chicken', 'pig', 'cow']
b[1]='melon'
print(b)

c= list()
for i in a or b:
    c.append(i)
print(c)


a = [1, 2, 3]

b = [3, 4, 5, 6]
c = list()
c = a.copy()
for i in b:
    if i in a:
        c.remove(i)
c.sort()
print(c)
print(a)

u = [0,1,2,3,4,5,6,7,8,9,0]
a = [1,3,4,5,7,9]
a_rest = u.copy()
for i in a:
    if i in a_rest:
        a_rest.remove(i)
print(a_rest)

def plus(a,b):
    c = a + b
    return c

plus(4,5)


a = [1,3,5,7,9]
b = [2,4,6,8,0,3]


def union(a,b):
    c = list()
    for i in a:
        if i not in b:
            c.append(i)
        c = c + b
    return c


def intersection(a,b):
    c = list()
    for i in a:
        if i in b:
            c.append(i)
    c.sort()
    return c


def complement(a,b):
    c = a.copy()
    for i in b:
        if i in a:
            c.remove(i)
    c.sort()
    return c

complement(a,b)

union(complement(a,b),complement(b,a))

def multi_input(*args): #여러개의 알규먼트를 넣을수 있다.
    print (args[0])
    print (args[1])
    print (args[2])
    print (args[3])
    print (args[4])
    print (args[-1])
multi_input(1,2,3,4,5)


def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

add_many(1,2,3,4,5,)

#base = something
# height = something
# 1/2*(base * height) = area
#print area

base = 5
height = 3
area = (1/2)*base*height
print(area)

a = int(input("a :"))
b = int(input("b :"))
while True:
    if a > b:
        print('a is bigger than b')
        break
    elif a < b:
        print('a is smaller than b')
        break
    else:
        print('a is equal to b')
        break

a = 11
b = 55
w = a
a = b
b = w
print("a = %d"%a,"b = %d"%b)

array ="123123123123"
array[3]

for n in range(0,10):
    array[n] = n

print(array)



sum = 0
for i in range(10):
    if i%3 == False:
        sum = sum + i
    elif i%5 == False and i%3==True:
        sum = sum + i
    
print(sum)
        
sum=0     
for i in range(16):
    if i%3 == False:
        sum = sum + i
    elif i%5 == False:
        sum = sum + i
print(sum)


from timeit import default_timer as timer
start = timer()
sum = list()
for i in range(1000):
    if i%3 == False:
        sum.append(i)
    elif i%5==False:
        if i%3==True:
            sum.append(i)
    else:
        pass
end = timer()
print(sum)
len(sum)
a = set(sum)
a
len(a)
print(end - start)

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3)
print(result)


def add_mul(choice,*args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result*i
    return result

result = add_mul('mul', 1,2,3,4,5)
print(result)

def nick(nick):
    if nick == 'fool':
        return                   #함수에선 끝내고싶을떄 return 쓴다.
    print("my nick name is %s"%nick)

nick('prince charming')

nick('fool')

def myself(name, old, man = True):
    print("my name is %s"%name)
    print("and %d years old"%old)
    if man:
        print('male')
    else:
        print('female')

myself('something',19,True)

#vartest.py
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)
def vartest(a):
    a = a + 1

vartest(3)
print(a)



a=1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)
    


a = 1 
def vartest():
    global a        #비추천 // 밖의 변수를 써서 오류발생이 쉬움.
    a = a + 1

vartest()
print(a)


#lambda 는 비추 (함수를 한줄로 만듬)

add = lambda a, b: a+b
result = add(3,4)
print(result)   #return 이 없어도 결과가 나온다.ArithmeticError


a = input()

number = input("숫자를 입력하세요: ")
print(number)

for i in range(10):
    print(i,end=' ')

#creating files


f = open("E:/creat_file/new file.txt", 'w')
f.close()

f = open("C:/doit/새파일.txt",'w')
f.close()
#r: read, w: write, a: add
f = open("E:/creat_file/new file.txt",'w')
for i in range(1,131):
    data = "%dth row. \n"%i
    f.write(data)
f.close

f.open("E:/creat_file/new file.txt",'r')
line = f.readline()
print(line)
f.close

f = open("E:/creat_file/new file.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close


f = open("foo.txt",'w')
f.write("life is too something")
f.close

with open("foo.txt","w") as f:
    f.write("life is too short, you need python") #with 문을쓰면 close 없어도됨





#연습문제

def evenodd(a):
    if a%2:
        print("odd")
    else:
        print("even")


evenodd(132)

#2
def average(*num):
    sum = 0
    for n in num:
        sum += n
    result = sum / len(num)
    return result

average(1,2,3,4)
a=(1,2,3,24)
len(a)

#3
input1 = input("put in first num: ")
input2 = input("put in second num: ")

total = int(input1) + int(input2)
print("the sum of two number is %s"%total)

#asdasdsa
#입력하는 프로그램 각기 ctrl+ F5 로 해야함
input1 = input("저장을 원하는 내용을 입력하세요: ")
f = open("test.txt",'a')
f.write(input1)
f.write("\n")
f.close             

f = open("test.txt",'r') #읽은다음
body = f.read()
f.close

body = body.replace('대상','수정')#찾아서 바꿔서

f=open('test.txt','w')#다시입력
f.write(body)#여기서
f.close