import numpy as np
a = [1, 2, 3, 4, 5]
b = np.array(a)
print(b)
print(b[0], b[-5]) #index is equall to list
print (b[::2]) # = 처음부터 두개단위로 출력

c = b + 5
print(b)
print(c) # 넘파이 어레이는 덧셈이 가능

np.sqrt(c) #루트
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.multiply(a, b)#각성분에 대한 곱 출력

np.max(a) # 명령 np.max or np min
np.argmax(a) # 맥시멈의 인덱스 출력
np.random.randint(45)

#로또 랜덤 추출기
np.random.randint(1,45,size = 6)

#clippy 깔면 도움주는 엿같은 캐릭 나옴
#simple dark mode 앱에서 깔면 어두워짐
#chrome.flags
def lotto():
    number = []
    while len(number) != 6:
        if np.random.randint(1,46) not in number:
            number.append(np.random.randint(1,45))
    return print(number)

print(lotto())

def til100():
    result = []
    while max.result<=95 or result==False:
        result.append(np.random.randint(1,100))
    return result

print(til100())
#오답
a = np.random.randint(1,30,size = 5) 
b = np.random.randint(1,30,size = 5) 
result = []
for i in a:    
    if i in b:
        result += i
    result.sort()
print(a,b)
print(result)
#랜덤한 집합 두개를 1~30까지에서 10개씩 뽑아서 교집합을 보는 계산
import numpy as np
def intersection(a,b):
    c = []
    for i in a:
        if i in b:
            c.append(i)
    c.sort()
    return c


def random_exclusive(low, high, how_many):
    number = []
    while how_many > 0:
        a = np.random.randint(low, high)
        if a not in number:
            number.append(a)
        how_many -= 1
    return number

print(random_exclusive(1,31,10))

def random_intersection(low, high, how_many):
    group_A = random_exclusive(low, high, how_many)
    group_B = random_exclusive(low, high, how_many)
    c = intersection(group_A, group_B)
    print ('그룹 A의 난수는 : {}'.format(group_A))
    print ('그룹 B의 난수는 : {}'.format(group_B))
    print ('그룹 A와 그룹 B의 교집합은 {}'.format(c))
    return c
print (random_intersection(1,31,10))



#Excel 1 -------------------------------------------------------------
"""Alt F11 //Alt Q

##Public Function FN추가할인(지역, 수용인원)

    If 지역 = "서울" Then
    
        FN추가할인 = 0
        
    ElseIf 수용인원 <= 2 Then
    
        FN추가할인 = 12000

    ElseIf 수용인원 <= 4 Then
    
        FN추가할인 = 34000
        
    Else
        
        FN추가할인 = 50000
        
    End If
    
End Function

끝나고는 f(x) 누르고 사용자정의해서 찾으면 됨"""

#--------------------------------------------------------------------


#정규 표현식은 파이썬이 아니라도 쓸 수 있다. 
#Regular Expressions -> re (import re),문자열 처리하는 모든곳

data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):#대상.isdigit() 안 비어있는 숫자가 맞니?
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

#____________________정규표현식 7_____________________________________
import re
data = """
par 800905-1049118
kim 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))

#정규식 검사
import re
p = re.compile('[a-z]+')

m = p.match("1python")

print(m)

p = re.compile(정규포현식)
m = p.match('strings goes here')
if m:
    print('Match found: ', m.group()) #대상.group() 파이썬에서 type 같음
else:
    print('No match')

m = p.search('python') #search 는 존재유무, match는 정확하게맞는지 체크
print(m)

result = p.findall("life is too short")#p 라는 형식에 맞는 해당문장 찾기
print(result)  #p = re.compile('[a-z]+') 떄문에 띄어쓰기는 삭제

result = p.finditer("life is too short")
print(result)
for r in result: print(r) #findall 과 같지만 결과가 iterable

m = p.match('python')
m.group() #매치된 문자열 돌려준다
m.start() #매치된 문자열의 시작위치
m.end() #현재 m 은 매치 함수로 잡아뒀음
m.span() #시작 끝을 튜플로 돌려줌

'''DOTALL(S) - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)
'''

import re
p = re.compile('a.b',re.DOTALL)
m = p.match('a\nb')
print(m)

p = re.compile('[a-z]+',re.I) #IGNORECASE 대소문자 구문X
p.match('python')
p.match('Python')
p.match('PYTHON')
#----Multiline 예시 M (각 줄에서 ^,$ 따위를 매번 적용)
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
#--- 각 줄에 처음으로
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three
"""

print(p.findall(data))
# ㄴ ['python one', 'python two', 'python three']


# re.VERBOSE 옵션을 사용하면 괄호 내에 사용된 줄바꿈
# , 빈칸을 무시할수 있어, 보기좋은 형태로 쓸 수 있다.

#\\section 이라 써야 \s 명령으로 인식하지않음
#허나 파이썬에서 리터럴 규칙 떄문에 \\->\로 인식
#따라서 \\쓰려면 \\\\ 써야함
#eg
p = re.compile('\\\\section')

# | <- vertical bar means 'or'
p = re.complile('Crow|Servo')
m = p.match('CrowHello')
print(m)

print(re.search('^Life', 'Life is too short'))
print(re.search('short$', 'Life is too short'))

# \b 단어 구분자. 띄어쓰기 찾기

p = re.compile(r'\bclass\b') #맨앞에 r 은 정규식문법임을 알려줌, 파이썬과 다름
print(p.search('no class at all'))

# \B 빈칸이 앞뒤에 없는 경우에만 결과나옴
p = re.compile(r'\Bclass\B')
print(p.search('no class at all')) #=none

#그루핑 문자열 ()
(ABC)+

p = re.compile('(ABC)+')
m = p.search('ABCABCABCABCAC OK?')
print(m)
print(m.group())

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)") #이름에 해당하는
# \w 부분이 (\w+)로 그룹화되었기에 가능함
m = p.search("park 010-1234-1234")
print(m.group(2)) #결과값에서 두번쨰 그룹, 숫자만 출력
#재참조 가능
"""
p = re.compile(r'(\b\w+)\s+\1')
p.search('Paris in the the spring').group()
->'the the'
정규식 (\b\w+)\s+\1은 (그룹) + " " + 그룹과 동일한 단어와 매치됨을 의미한다.
 이렇게 정규식을 만들게 되면 2개의 동일한 단어를 연속적으로 사용해야만 
 매치된다. 이것을 가능하게 해주는 것이 바로 재참조 메타 문자인 \1이다. 
 \1은 정규식의 그룹 중 첫 번째 그룹을 가리킨다.
"""
#그루핑된 문자열에 이름 붙이기

# (\w+) --> (?P<name>\w+) 이름이란 글자를 name 으로 이름짓기

p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))
#탐색 
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
#전방탐색
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group()) #(?=:)< :이 검색되지만 결과엔 포함 되지않는다.

#Substitution 바꾸기

p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')

p.sub('colour', 'blue socks and red shoes', count=1) #앞에거 한번만 바꾼다


#Greedy ______________________________________
#모든걸 다 찾는것 -> Greedy
#최소한의 반복을 수행 -> non-Greedy

s = '<html><head><title>Title</title>'
len(s)

print(re.match('<.*>', s).span())

print(re.match('<.*>', s).group())
print(re.match('<.*?>', s).group()) #한번만 나오게함
# * 가 있으면 전부다 
#*?, +?, ??,{m,n}처럼 제한을 줄 수 있음.

######################################################################




#종합문제

#1


a = "a:b:c:d"
b = a.split(":")
'#'.join(b)

#2
try:
a = {'A':90, 'B':80}
a.get('C',70) #뒤에 입력된 값이 디폴트.
a['C']

#더하기와 extend 는 데이터 저장되는 위치가 다르다

a = [1, 2, 3]
id(a)

a = a + [4,5]  #변경됨
a.extend([4,5])#같음

#4 
A = [20,55,67,82,45,33,90,87,100,25]
sum(A)
sum = 0
for i in range(len(A)-1):
    while A[i] >= 50:
        sum = sum + A[i]
        i += 1
print(sum)




#4-답---
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

result = 0
while A:                # A 리스트에 값이 있는 동안
    mark = A.pop()      # A리스트의 가장 마지막 항목을 하나씩 뽑아냄
    if mark >= 50:      # 50점 이상의 점수만 더함
        result += mark

print(result)           # 481 출력


#피보나치 ------------------n번쨰


def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)

for i in range(20):
    print(fib(i), end = ' ')


#-----------n 보다 작은 피보나치

def fib(n):
    a = 0
    b = 1
    while b<n:
        a , b = b , a + b
        print(b)

print(fib(123123123))
#-----------

n = int(input("num? : "))
a = 0; b = 1
print('0',end='')
while b <= n:
    print(', %d'%b, end='')
    a,b = b,a+b




    
