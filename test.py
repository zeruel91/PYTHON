a = 'Python'

a * 100

b = 'is good'

a + b

print("="*50)

print("my progaram")

print("="*50)

len(a)

a = "Life is full of opportunity"

len(a)

a[3]

a = "20200630Rainy"

date = a[:8]

weather = a[8:]

date

weather

a[:10]

a[:8]

"I eat %10.9f apples" %1.123125

"they make me eat %s%% of apple" %3

"%s"%3.124123

"%10s" %'hi'

a = '20200630'

year = a[:4]

month = a[4:6]

day = a[6:8]

day

"%10.5f" % 3.4444

a[:4]+'07'+a[6:]

number = 10

day = "three"

"I ate {0} apples. so I was sick for {1} days.".format(number, day)

"I ate {number} apples. so I was sick for {day}days.".format(number=10,day=3)

"I ate {number} apples. so I was sick for {day}days.".format(day=3,number="20")

"{0:@^50}".format("hi")

y = 3.123125151231

"{0:=^20.12f}".format(y)

"{0:>10}".format("hi")

"%-10s"%"    hi"

"{{ and }}".format()

"I eat {0} apples and {2} pears".format(3,123,2)

name = 'king arthur'

age = 30

f'my name is {name}. and i am {age**3} years old'

d = {'name':'Voldemort','age':30}

f'my name is {d["name"]}. and i am {d["age"]*3+15} years old'

f'{"hi":>10}'
"{0:>10}".format("hi")
"%10s"%"hi"


y = 3.141592
y
f'{y:15.6f}' 
y.find(3)
x="avadacadabra"
x.count('a')
x.index('a')
x.find('t')

#join 
"  fucking idiots".join('4362752458')
",".join(['a','b','c','d'])

x.upper()
a = f'{0:>10}'.format("hi")
a
a= "           hi      "
a.lstrip()
b=a.strip()
b
b.upper()

#바꾸기
a = "Life is full of agony"
a.split()
x.split('a')

#list
a = list()
a = []
b = [1, 2, 3]
c = ['life', 'is', 'too', 'short']
d = [1,2, 'life', 'is']
e = [1, 2, ['life', 'is']]
b[1] + b[2]
e[-1][0][-1]
e[0:2]
str(b[2])+"hi"
e[0:]
a = [1, 2, 3]
a[2] = 4
del a[1]
a = a + [2]
a.sort()
len(a)
a.reverse()
a.sort()
a.append(5)
a.index(2)
a.append([1, 2, 3])
del a[4]
a =  ['a', 'b', 'c']
a.reverse()
a
a.sort()
a.insert(2,5)
a.remove('a')
a.remove(5)
a.extend([4,5])
a = a + [4,5]
a.count(5)
b = [0<int()]
a.pop()
a