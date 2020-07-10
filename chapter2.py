
# 02-1 숫자형

# 사칙연산
a = 3
b = 4

a + b

a * b

a / b


# 제곱

a = 3
b = 4
a ** b



# %연산자

7 % 3

3 % 7



# //연산자

7 / 4

7 // 4

###############################################################################
# 02-2 문자열 자료형
###############################################################################


# 문자열 자료형 만드는 4가지 방법
"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''


food = "Python's favorite food is perl"

food


#SyntaxError

food = 'Python's favorite food is perl'
food = "Python's favorite food is perl"
food

say = '"Python is very easy." he says.'
say


food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

food
say





# 여러줄로 이루어진 문자열

multiline = "Life is too short\nYou need python"
multiline
print(multiline)


multiline='''
    Life is too short
    You need python
    '''

print(multiline)



# 문자열 더해서 연결하기 (Concatenation)

head = "Python"
tail = " is fun!"
head + tail


# 문자열 곱하기

a = "python"
a * 2



# 문자열 곱하기 응용

print("=" * 50)
print("My Program")
print("=" * 50)


# 문자열 길이 구하기

a = "Life is too short"
len(a)



# 인덱싱(Indexing)

a = "Life is too short, You need Python"

a[3]

a[0]

a[12]

a[-1]

a[-0]

a[-2]

a[-5]



# 슬라이싱(Slicing)

a = "Life is too short, You need Python"

a[0:4]

a = "20010331Rainy"

date = a[:8]
weather = a[8:]

date

weather


# 문자열 슬라이싱


a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
b


a = "Life is too short, You need Python"

a[0:4]

a[0:3]

a[0:5]

a[0:2]

a[5:7]

a[12:17]

a[19:]

a[:17]

a[:]

a[19:-7]



# 슬라이싱으로 문자열 나누기

a = "20010331Rainy"

date = a[:8]
weather = a[8:]
date

weather


a = "20010331Rainy"

year = a[:4]
day = a[4:8]
weather = a[8:]

year

day

weather






# 문자열 포매팅

"I eat %d apples." % 3

"I eat %s apples." % "five"


number = 3
"I eat %d apples." % number



number = 10
day = "three"

"I ate %d apples. so I was sick for %s days." % (number, day)





# 정렬과 공백

"%10s" % "hi"

"%-10sjane." % 'hi'



# 소수점 표현

"%0.4f" % 3.42134234

"%10.4f" % 3.42134234


# format 함수를 사용한 포매팅

"I eat {0} apples".format(3)

"I eat {0} apples".format("five")

number = 3
"I eat {0} apples".format(number)

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)

"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)

"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)


"{0:<10}".format("hi")

"{0:>10}".format("hi")

"{0:^10}".format("hi")

"{0:=^10}".format("hi")

"{0:!<10}".format("hi")


y = 3.42134234
"{0:0.4f}".format(y)

"{0:10.4f}".format(y)


"{{ and }}".format()


name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'


age = 30
f'나는 내년이면 {age+1}살이 된다.'


d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'


f'{"hi":<10}'  # 왼쪽 정렬

f'{"hi":>10}'  # 오른쪽 정렬

f'{"hi":^10}'  # 가운데 정렬

f'{"hi":=^10}'  # 가운데 정렬하고 '=' 문자로 공백 채우기

f'{"hi":!<10}'  # 왼쪽 정렬하고 '!' 문자로 공백 채우기



y = 3.42134234
f'{y:0.4f}'  # 소수점 4자리까지만 표현

f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤


f'{{ and }}'




################ 문자열 관련 함수들 ###################

# 문자열 개수 세기(count)

a = "hobby"
a.count('b')


# 위치 알려주기1(find)

a = "Python is best choice"
a.find('b')

a.find('k')


# 위치 알려주기2(index)

a = "Life is too short"
a.index('t')

a.index('k')


# 문자열 삽입(join)

",".join('abcd')

",".join(['a', 'b', 'c', 'd'])


# 소문자를 대문자로 바꾸기(upper)

a = "hi"
a.upper()


# 대문자를 소문자로 바꾸기(lower)

a = "HI"
a.lower()



# 왼쪽 공백 지우기(lstrip)

a = " hi "
a.lstrip()


#오른쪽 공백 지우기(rstrip)

a= " hi "
a.rstrip()



# 양쪽 공백 지우기(strip)

a = " hi "
>>> a.strip()


#문자열 바꾸기(replace)

a = "Life is too short"
a.replace("Life", "Your leg")



# 문자열 나누기(split)

a = "Life is too short"
a.split()
b = "a:b:c:d"
b.split(':')



###############################################################################
# 02-3 리스트 자료형
###############################################################################

odd = [1,3,5,7,9]



a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 리스트의 인덱싱

a = [1, 2, 3]

a

a[0]

a[0]+a[2]

a[-1]


a = [1, 2, 3, ['a','b','c']]a

a[0]

a[-1]

a[-1][0]

a[-1][1]



# 리스트의 슬라이싱



a = [1, 2, 3, 4, 5]

a[0:2]


a = "12345"

a[0:2]


a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
b
c


# 리스트 연산하기

a = [1, 2, 3]
b = [4, 5, 6]
a+b


a = [1, 2, 3]
a*3



a = [1, 2, 3]
len(a)



# 리스트의 수정과 삭제

a = [1, 2, 3]
a[2] = 4
a


a = [1, 2, 3]
del a[1]
a

a = [1, 2, 3, 4, 5]
del a[2:]
a


# 리스트 관련 함수들

# 리스트에 요소 추가 (append)
a = [1, 2, 3]
a.append(4)
a

a.append([5, 6])
a


# 리스트 정렬(sort)

a = [1, 4, 3, 2]
a.sort()
a

a = ['a','c','b']
a.sort()
a


# 리스트 뒤집기(reverse)

a = ['a', 'c', 'b']
a.reverse()
a



# 위치 반환(index)

a = [1, 2, 3]
a.index(3)
a.index(1)
a.index(0)


# 리스트에 요소 삽입 (insert)

a = [1, 2, 3]
a.insert(0,4)
a


a.insert(3,5)
a


# 리스트 요소 제거 (remove)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a

a.remove(3)
a


# 리스트 요소 끄집어내기 (pop)

a = [1, 2, 3]
a.pop()
a


a = [1, 2, 3]
a.pop(1)
a



# 리스트에 포함된 요소 x의 개수 세기(count)

a = [1,2,3,1]
a.count(1)


# 리스트 확장(extend)

a = [1,2,3]
a.extend([4,5])
a


b = [6, 7]
a.extend(b)
a

###############################################################################
# 02-4 튜플 자료형
###############################################################################

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))



# 튜플 요솟값을 삭제하려 할 때

t1 = (1, 2, 'a', 'b')
del t1[0]

# 튜플 요솟값을 변경하려 할 때

t1 = (1, 2, 'a', 'b')
t1[0] = 'c


# 인덱싱하기

t1 = (1, 2, 'a', 'b')
t1[0]
t1[3]


# 슬라이싱하기

t1 = (1, 2, 'a', 'b')
t1[1:]

# 튜플 더하기

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t1 + t2


# 튜플 곱하기

t2 = (3, 4)
t2 * 3



# 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
len(t1)




###############################################################################
# 02-5 딕셔너리 자료형
###############################################################################

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
dic

a = {1: 'hi'}
a

a = { 'a': [1,2,3]}
a


# 딕셔너리 쌍 추가하기

a = {1: 'a'}
a
a[2] = 'b'
a


a['name'] = 'pey'
a

a[3] = [1,2,3]
a

# 딕셔너리 요소 삭제하기

del a[1]
a


# 딕셔너리에서 Key 사용해 Value 얻기

grade = {'pey': 10, 'julliet': 99}
grade['pey']



a = {1:'a', 2:'b'}
a[1]
a[2]



a = {'a':1, 'b':2}
a['a']
a['b']


dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
dic['name']
dic['phone']
dic['birth']



# 딕셔너리 만들 때 주의할 사항

a = {1:'a', 1:'b'}
a

a = {[1,2] : 'hi'} # 오류발생









# 딕셔너리 관련 함수들

# Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()
list(a.keys())

# Value 리스트 만들기(values)
a.values()

# Key, Value 쌍 얻기(items)
a.items()

# Key: Value 쌍 모두 지우기(clear)
a.clear()
a

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a.get('name')
a.get('phone')
print(a.get('nokey'))
print(a['nokey'])  # error
a.get('foo', 'bar')

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)

'name' in a
'email' in a



###############################################################################
# 02-6 집합 자료형
###############################################################################


s1 = set([1,2,3])
s1


s2 = set("Hello")
s2

s1 = set([1,2,3])
l1 = list(s1)
l1

l1[0]

t1 = tuple(s1)
t1

t1[0]

# 교집합, 합집합, 차집합 구하기

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s1 & s2   #교집합

s1.intersection(s2)

s1 | s2    #합집합

s1.union(s2)

s1 - s2    #차집합

s2 - s1

s1.difference(s2)

s2.difference(s1)



# 집합 자료형 관련 함수들

# 값 1개 추가하기(add)

s1 = set([1, 2, 3])
s1.add(4)
s1

# 값 여러 개 추가하기(update)

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1

# 특정 값 제거하기(remove)

s1 = set([1, 2, 3])
s1.remove(2)
s1





###############################################################################
# 02-7 불 자료형
###############################################################################

a = True
b = False

type(a)

type(b)

1 == 1

2 > 1

2 < 1


a = [1, 2, 3, 4]
while a:
    print(a.pop())


if []:
        print("참")
    else:
        print("거짓")



if [1, 2, 3]:
        print("참")
    else:
        print("거짓")

# 불 연산

bool('python')

bool('')

bool([1,2,3])

bool([])

bool(0)

bool(3)



###############################################################################
# 02-8 변수
###############################################################################

a = 1
b = "python"
c = [1,2,3]

a
b
c

a = [1, 2, 3]

type(a)

id(a)

b = a

id(b)

a is b

a[1] = 4

a

b


a = [1, 2, 3]

b = a[:]

a[1] = 4

a

b

from copy import copy

b = copy(a)

b
a

b is a

# 변수를 만드는 여러 가지 방법

a, b = ('python', 'life')

a
b

(a, b) = 'python', 'life'

a
b


[a,b] = ['python', 'life']

a
b

a = b = 'python'

a
b


a = 3
b = 5

a, b = b, a

a
b




###############################################################################
###############################################################################












Chapter2.py
Chapter2.py 표시 중입니다.