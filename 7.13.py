a = 256
a_prime = True
for i in range(2,a):
    if a % i == False:
        a_prime = False
if a_prime == True:
    print('{} is prime number.'.format(a))
else:
    print('{} is not a prime number'.format(a))

#소수판독기
def prime(a):
    c = 0
    b = range(2, a)
    for i in b:
        if a % i == False:
            c += 1
            
    if c > 0:
        print('{} is not a prime'.format(a))
        d = False
    else:
        return True
        d = True


prime(17)
prime(17171771)
list1000 = list()
for a in range(1001):
    if prime(a)==True:
        list1000.append(a)
print(list1000)

a = range(2,1001)
diff= 0
prime_number=[1]
max_diff_primes=[]
c = len(list1000)
for i in c:
    c = prime(i)
    if c == True:
        prime_number.append(i)
        if prime_number[-1] - prime_number[-2] > diff:
            diff = prime_number[-1] - prime_number[-2]
            max_diff_primes = [prime_number[-2],prime_number[-1]]

print('max length btw prime numbers : {}'.format(diff))
print('{}'.format(max_diff_primes))

#소인수찾기
"""a = 24
factor = []
for i in range(2,a+1):

    if a % i == True:
       factor.append(i) 
       a = a // i
print (factor)"""
#정답.
a = 18
b = range(2,a)
primes = []
for i in b:
    while a % i == 0:
        primes.append(i)
        a /= i
        continue
if primes == []:
    primes.apppend(a)

primes

#알고리즘 숙제
def search(x,y,z):
    if x + y + z != 180:
        return 'it is not a triangle'
    else:
        if x  < 90 and y < 90 and z < 90:
            return 'it is acute angled triangle'
        elif 90 in [x, y, z]:
            return 'it is right angled triangle'
        elif x or y or z > 90:
            return 'it is abtuse angled triangle'
    return ''
x = int(input('제 1 각을 입력하세요'))
y = int(input('제 2 각을 입력하세요'))
z = int(input('제 3 각을 입력하세요'))

print(search(x,y,z))


#정렬 알고리즘 1

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for k in range(i+1,len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index]=temp
    return arr


test = [12, 13, 11, 14, 10]
selection_sort(test)
# #------------------------------------------------------------------
# """ a명령 프롬프트 명령어
# dir 디렉토리의 내용 확인
# mkdir make directory 만들떄
# rmdir remove directory 지울떄
# cd .. change directory .. <상위
# cd 디렉토리명 들어갈떄
# """
# print("Hello World")

# Ctrl + / :전부 주석처리 

age = 20
name = 'swaroop'

print ( ' {} was {} years old when he wrote this book'.format(name,age),end = '')
print ('why is {} playing with that python?'.format(name))

print ('{0:.3f}'.format(1.0/3))

print( 'hello ', end = '')

print(r'This is the first line\nThis is the second line') #Raw

i = 5
print(i)
i += 1
print(i)

s = '''This is a multi line string.
This is the second line.'''
print(s)

length = 5
breadth = 2
area = length * breadth
print('Area is',area)
print('Perimeter is',2*(length*breadth))

number = 23
guess = int(input('Enter an integer :'))

if guess == number:
    print ('Congratulations, you guessed it.')
    print ('(but you do not win any prizes!)')
elif guess < number:
    print ('No, it is a little higher than that')

else:
    print('No, it is a little lower than that')

print('Done')

for i in range(5):
    print (i)
else:
    print('The loop is over')




while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print ('Length of the string is',len(s))
print('Done')


while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s)<3:
        print('too small')
        continue
    print('input is of sufficient length')

def say_hello():
    print("Hello World")

say_hello()


def print_max(a, b):
    if a > b:
        print (a,'is maximum')
    elif a == b:
        print (a, 'is equal to',b)
    else:
        print(b, 'is maximum')




print_max(123,1254)


x = 50
def func(x):
    print('x is',x)
    x = 2
    print('Changed local x to',x)
func(x)

def f():
    global x

    print ('x is', x)
    x = 2
    print ("changed global x to", x)

f()
x

def say(message, times=1): #<-- default 값
    print (message*times)

say ('Hello',123)


def func(a, b=5, c=10):
    print ('a is', a, 'and b is',b, 'and c is',c)

func(3,7)
func(25,c=24)

def total(initial=5, *numbers, **keywords):# ** 딕셔너리,
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print (total(10,1,2,3, vegetables=50, fruits =100))


import sys

print('The command line qrguments are:')
for i in sys.argv:
    print (i)

print ('\n\nthe PYTHONPATH is',sys.path, '\n')

from math import sqrt
print("Square root of 16 is", sqrt(16))#math.sqrt 에서 메스 생략

if __name__ == '__main__': #직접실행되었다는 의미
    print('This program is being run by itself')
else:
    print ('I am being imported from another module')

import prime2

