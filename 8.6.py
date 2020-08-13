#0~1000
a = '11'
a.count('1')


#For 문
result = 0
for i in range(1001):
    
    result += str(i).count('1')
print(result)

#without For 문

result = 0 
i = 0
while i != 1001:
    result += str(i).count('1')
    i += 1
print(result)

#given  answer
def count(n):
    countN = str(list(range(n+1))).count('1')
    return countN


def count(n):
    s = str(list(range(n+1)))
    count = 0
    for i in s:
        if i == "1":
            count += 1
    return count

#Jupiter 에서의 시간 체크 %%time 
# %timeit < 천번 돌린 평균

import timeit
help(timeit)
timeit
#format function 
format(a)
help(format)

a = int(input('숫자를 입력해주세요')

print(format(123125,",")) #3digit , (default i assume)
print(format(1234,"E"))   #express by Exponention
print(format(123425,"X"))  
#위에서 마지막예는 _으로 빈공간을 채우고(첫글자는 채움글자), 오른
# 쪽에 숫자를 맞추며(>문자), 음수일때만 부호 표시하고(-문자),
#  항상 12자리 맞게 출력하고(012), 3자리마다 , 를 추가하고(,문자)
# , 소수점은 2자리까지인(.2문자) 소수(f문자)로 표현합니다.
print(format(1234, "_>-012,.2f")) 
#"채움문자"->_
# > 숫자를오른쪽에 맞춘다
# - 음수일때만 부호표시
#012 12자리로 출력
#, -> 3자리마다 ,
# .2f -> 소수점 두자리 표현
a = "hi"
print("{0:=^50}".format(a)+'=') # ^ 은 가운데에

'{0:<10}'.format('hi')
'{0:^10}'.format('hi')
'{0:>10}'.format('hi')


'{0:_^11}'.format('hello')

'what\'s your name?'

-1%3

a = 1124312512
a.join

#재귀함수.
def comf(n):
    if len(n) <= 3:
        return n
    else:
        return comf(n[:len(n)-3]) + ',' + n[len(n)-3:]

comf('113131313313')

x = 50

def func(x):
    print('x is',x)
    x = 2
    print('Changed local x to',x)
func(x)
print('x is still',x)

import this

len(a.pop())
str(len(a))
#--------------
#index 를쓰는게 더 편하다.
a = ['a','a','a','a','a','a','a','a','a']
nine = str(len(a))
a.remove('a')
eight = str(len(a))
a.remove('a')
seven = str(len(a))
a.remove('a')
six = str(len(a))
a.remove('a')
five = str(len(a))
a.remove('a')
four = str(len(a))
a.remove('a')
three = str(len(a))
a.remove('a')
two = str(len(a))
a.remove('a')
one = str(len(a))
a.remove('a')
zero = str(len(a))
print(two+zero+one+nine+zero+eight+zero+six)
#------------------------
bri = set(['brazil' 'russia', 'india'])
'india' in bri
bric = bri.copy()
bric.add('china')
bric.issuperset(bri)
bri & bric
#####find ft
a = 'there are two types of people in the world'
a.find('ar32') # <--- Return -1 on failure

#Quiz 6th time




student = ['강은지', '김유정', '박현서', '최성훈','홍유진', '박지호' ,'권윤일','김채리','한지호','김진이','김인호','강채연']

student.sort()

for i, j in enumerate(student):
    print('번호: {},'.format(i+1),'이름: {}'.format(j))
    print('번호: {}, 이름: {}'.format(i+1,j))

#Quiz 7th
a = int(input())
def min_labor(n):
    a = n // 7
    b = (n - a*7)//3
    if n != a*7 + b*3:
        return -1
    print('7kg: {}, 3kg: {}'.format(a,b))
min_labor(a)
min_labor(24)

#quiz 3,6,9


def threesixnine(n):
    a = {'3','6','9'}
    result = 0
    for i in range(1,int(n)+1):
        if a.issuperset(set(str(i))):
            result += 1
    return result

threesixnine(36)

#list 축약
a = [2*a for a in range(15) if a%2 == 0]
a

def sol(n):
    n = list(str(n))
    answer = 0
    count = 1
    d = {3:1,6:2,9:3}
    while n:
        answer += d[int(n.pop())]*count #리스트에서 뽑아낸것을 딕셔너리 키로 
        count*3
    return answer


#저번시간 알고리즘

a = ['a1','a2','a3','a4','an','b1','b2','bn']
b = []
c = []
for i in a :
    b.append(i[])

for i in range(len(a)):
    a.append(a[0]):
    a.pop(0)





Rule("ADBCEF","BCAD","ADEFBOQRX")


def even_odd(a):
    even = 0
    odd = 0
    for i in a:
        if i % 2 == 0 :
            even += 1
        else:
            odd += 1
    return 'odd: {}, even {}'.format(odd,even)

even_odd([1,2,3,4,5,6,7])




a = "AKDEM"
enumerate(a).find("A")
a.index("A")
list(a)
rule(a)



def Rule(*problem,rule = "ABD"):
    result = []
    for i in range(len(rule)-1):#규칙의 인덱스 i에 대해서
        if rule[i] in problem and rule[i+1] in problem:
            if problem.index(rule[i])>problem.index(rule[i+1]):
                result.append('impossible')
            else:
                pass
        if result == []:
            result.append('possible')        

    return result


def Hanoi(prob, rule = "ABD"):
    result = prob
    result2 = []
    for j in range(len(prob)):
        for i in prob:
            if i not in rule:
                result.remove(i)
                print(result)
        for j in range(len(result)-1):
            if rule.index(result[j])>rule.index(result[j+1]):
                result2.append('impossible')
            else:
                result2.append('possible')
    return result2



            





