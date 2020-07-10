#bool = 명제
a = 'apple'
b = ['tomato','orange', 'strawberry','apple']
a in b
type(a in b)

for a in range(1,6):
    if a > 3:
        print(a)



i = 1
while i < 10:
    print(i**2)
    i = i + 1

    
        
def odd_or_even(n):
    if not n % 2:
        print('{} is even number.'.format(n))
    elif n % 2:
        print('{} is odd number.'.format(n))
    else:
        return n


odd_or_even(1)

a = 4
type(4)


import numpy as np #<module error

print (np.sqrt(100))
round(a)#<반올림
int(a)#소수점 자르기 가우스 아님. 정수자리만 남김
float(a)#소수형으로 만들기
a = -100.1
np.squrt(100)
round(a)

for i in range(0,9,2):
    print(i)
#range(이상,미만,양수 공차)

a = 0
result = 0
for i in range(a,101):
    result += i
print('sum of {}to 100 : '.format(a),result)

a = 0
for i in range(100):
    if i % 2 == 1:
        a += i
        print(i ,end=' ')
print('the sum of odd number between 0 to 100 : {}'.format(a))

#Stack overflow 개발자들의 네이버 지식인
#pip install numpy # 파이썬이 아닌 cmd 에 직접 입력, 인터넷에서 찾아서 설치

import numpy as np
np.sqrt(100)

a = 123123
b = str(a)
b.count('3')

#연습문제

sum = 0
for a in range(10001):
    b = str(a)
    sum += b.count('8')
print(sum)

#피보나치 

n = int(input("num : "))
a = 0 
b = 1
print('0', end='')
while b <= n:
    print(',%d'%b,end='')
    a,b = b,a+b #동시 변경
[1,13,17,18,19,21,28]
head = 0 
tail = 6
center = ( head + tail ) / 2 
if a[center] = 17:
    print(a[center])
elif: 
 


#pseudocode (이진 탐색법 17 찾기)
#시작
#0 ->헤드 6 ->테일
#만약 헤드가 테일보다 작거나 같다면
    #(헤드+테일) /2 -> 센터
    #어레이 센터가 17인가?
        #아니다 ->작은가? -> 센터 + 1 을 새로운 헤드로 정함 -> 3번째줄로
            #작지않다 -> 센터 -1 -> 테일로
        #맞다
            #센터번쨰 요소가 일치라고 출력 => 종료
    #맞다
        #센터번쨰 요소가 일치라고 출력 => 종료
#아니면 끝


#인공지능 많이쓰는 라이브러리
#pip install keras /// pip install tensorflow << 연계형


#명령 프롬프트 cmd for DOS
#cd appdata (cd change directory)
#cd local
#(mkdir 파일명)파일 생성
#cd .. (하나 윗단계로 나가기)
#rmdir bigdata (rmdir <remove directory + 파일명)
#


#내장함수.

dir([1,2,3])
for i, name in enumerate([1,2,3]):
    print(i,name)

pow(2,100)

def twotimes(numberlist):
    result = []
    for number in numberlist:
        result.append(number*2)
    return result

result = twotimes([1,2,3,4])
print(result)

def twotimes(x):
    return x*2

list(map(twotimes,[1,2,3])) #map(함수,정의역)

round(56.123,2) 
# => 56.12

sorted([1,2,3,4]) #sort  와의 차이는 정렬후 돌려준다(list) 와 안돌려준다 차이,
                  # a.sort()는 정렬만 하고 안돌려줌
print(sorted([1,2,3,4]))
sum([1,2,3,4])

list(zip([1,2,3],[4,5,6],[7,8,9]))
#각 dimension 끼리 묶어 리스트로 결과 냄 !!!튜플로 묶임


#import sys
#os.environ['PATH'] <--패스값을 보여줘
#os.system("command")


#import shutil 복사 모듈

#time
    #import time
    #time.time() 초단위, 매우 쓸모없음.
    #time.localtime(time.time()) 조금 덜 쓸모없음
    #time.asctime(time.localtime(time.time())) 쓸모있음
    #time.ctime() 실용, <<< 타임.씨타임()
    #time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
                    %a ,%A

import time
for i in range(10):
    print(i)
    time.sleep(1) #<1초마다 찍음

import calendar
print(calendar.calendar(2020))
calendar.prmonth(2020,7) # 해당연도와 달.  
calendar.weekday(2015,12,31) #=> int <0이 월요일로 출력됨
calendar.monthrange(2020,7) #시작 요일, 끝 날짜

#random

import random
random.random()  
random.randint(1,1000)

import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)#random으로 숫자 지정, pop으로 해당숫자를 내보낸다.

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: #데이타가 남아있을때까지
        print(random_pop(data),end = '') #random으로 지정한숫자를 출력

i = 6
while i != 0:
    print(random.randint(1,45),end=',')
    i = i - 1 

#webbrowser

import webbrowser
webbrowser.open("http://google.com")


#연습문제 05장

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator): #inherit 상속 ()
    def minus(self, val):
        self.value -= val

#cal = UpgradeCalculator()
#cal.add(10)
#cal.minus(7)
#print(cal.value)

class MaxLimitCalculator(UpgradeCalculator): #override 기능 
    def add(self, val):
        self.value += val
        if self.value > 100:
            return 100
        

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

#
print(cal.value)

all([abs(-3)-3,1,2]) #abs < absolute value 
    #False
ord('a')
chr(ord('a'))  #chr < Uni ->charactor: Ord: Charactor -> Uni


#decimal
hex(234) #hexadecimal representation of an integer
int(0xea)

a = [ -8, 2, 7, 5, -3, 5, 0, 1]
print(min(a) + max(a))

round(17/3, 5) #반올림한다 소수점 다섯자리까지 표현.
int( 17/3) #뒤 날리기.


