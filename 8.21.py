#Alg HW
name = 'A D B C'.split(' ')
point = list(map(int,'70 10 55 40'.split(' ')))
data = dict(zip(name,point))
# data
# del data['A']
# max(data.values())
def make_it_dict_by_order(a,b):
    if len(a) != len(b):  #점수누락되면 에러출력
        return error
    result = dict(zip(a,b)) #딕셔너리로 묶기
    return result
def who_is_the_winner(a):
    result = dict() #빈 딕셔너리 생성
    i = 1           #반복문 초기설정
    while a:        #종료시점 설정
        max_point = max(a.values()) #앞서 받은 딕셔너리에서 벨류최대값 찾기
        b = [name for name, point in a.items() if point == max_point] 
        #item() 에서 끌어오지않으면 벨류 갯수 문제가 생김.
        del a[b[0]] #해당 최대 값에대한 키값을 b 로뽑고 제거
        result[b[0]] = i #하면서 순위 입력
        i += 1
    return result #출력

a = make_it_dict_by_order(name,point) #딕셔너리로 묶기
print(a)

# max_point = max(a.values())
# b = [name for name, point in a.items() if point == max_point]
# b
# result = dict()
# result
who_is_the_winner(a) #딕셔너리로 순위 출력 






weight = 22,24,26,30,32,40,35,45,20,29,34,36,36,38,39,48,43,37,33,31,29,39,26,29
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
bins = np.arange(20, 75, 5)
hist, bins = np.histogram(weight,bins) 
print(hist)# 히스토그램에서 bins 는 해당값이 들어가는 갯수를 체크해줌
print(bins)
total_number = len(weight)
hist_normal = np.asarray(hist)/total_number
print(hist_normal)
sum(hist_normal)
#accumulation 누적
accumul_weight = []
previous = 0
for i in hist:
    previous += i
    accumul_weight.append(previous)
print(accumul_weight)

plt.hist(weight, bins)
plt.xlabel('Weight (kg)', fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()
#줄간격 = rwidth , alpha = 투명도
plt.hist(weight, bins, rwidth = 0.8 )
plt.hist(weigt, bins, rwidth = 0.8, color = 'g', alpha = 0.5)
plt.xlabel('Weight (kg)', fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()

#DIY
height = [188,177,156,161,167,169,169,171,175,184,
180,177,175,174,172,173]#리스트든뭐든 나옴
bins = np.arange(150,190,5) #범주표시
hist, bins = np.histogram(height,bins)#히스토그램에 대한 수치적 결과값
#print(hist)
plt.hist(height,bins,rwidth = 0.4,color = 'r')
plt.xlabel('Height',fontsize = 13)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()
#-------------------
#DIY end
#-------------------

weight2 = 42,43,46,50,48,40,38,46,50,52,54,58,46,48,51,52,56,60,39,61,52,45,44,45
bins = np.arange(20,55,5)
bins2 = np.arange(20,65,5)
hist2, bin_edges = np.histogram(weight2,bins2)
print(hist2)
plt.hist(weight2,bins2,rwidth=0.8,color = 'red',alpha = 0.5)
plt.grid()
plt.xlabel('Weight (kg)',fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()

#-------------------
#-------------------

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
factorial(4)
#-------------------

def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
sum(4)
#-------------------

def power(x,n):
    if n == 0:
        return 1
    return x*power(x,n-1)
power(2,10)
#-------------------

def print_binary(n):
    if n < 2:
        return '{}'.format(n)
    return '{}'.format(n%2) + print_binary(n//2)
print_binary(15)

def print_binary(n):
    if n < 2:
        print(n, end ='')
    else:
        print_binary(n//2)
        print(n%2,end='')
print_binary(15)
#-------------------


def gcd(m, n):
    if m - n == 0:
        return m
    else:
        return gcd(abs(m-n),min(m,n))
gcd(48,60)
#-------------------

def gcd(m,n):
    if max(m,n)%min(m,n) == 0:
        return min(m,n)
    else:
        return gcd(max(m,n)%min(m,n),min(m,n))
gcd(48,60)
gcd(3,5)
#-------------------

li = [1,6,7,10,2,5,11]
li.index(6)
target = 10
search(li,0,5,10)
def search(li,begin,end,targetA):
    for i in range(begin,end+1):
        if li[i] == targetA:
            return i
    return 'None'
search(li,0,5,10)

def search(li,begin,end,targetA):

    if begin > end:
        return -1
    
    elif target == li[begin]:
        return begin
    else:
        return search(li,begin+1,end,targetA)
search(li,0,5,10)
#-------------------
def fibo(n):
    if n == 0 : return 1
    if n == 1 : return 1
    return fibo(n-2) + fibo(n-1)
fibo(7)


         


        