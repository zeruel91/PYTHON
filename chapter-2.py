a = [1, 2, 3]
a.append(4)
a
a.append([5,6])
a[4][1]
a[:3]
a.reverse()\
a.pop()
a = ['a', 'b', 'c']
a.sort()
a.reverse()
a.index(3)
len(a)
a.insert(1,3)
a.insert(2,[3,4])
str(a[0])+"hi"
a.remove(3)
a[1].remove(3)
a.pop()
t1 = ()
t2 = (1,)
t2.remove(1)
t2[0]
a = {1: 'a'}
a[2] = 'b'
a['do'] = 'something'
a['do']
del a['do']
a = {1:'a', 2:'b'}
for k in list(a.keys()):
    print(k)
a.keys()
a.values()
a.clear()
a = {'name':'pey', 'phone':'0194101125','birth':'1113'}
a.get('name')
a['name']
a.get('phone|')
a.get('stupid','idiot')
'name' in a
a['name2']
s1 = set([1,2,3,4,5,6,'hello'])
s1 = {1,2,3,4}
s1 = {"Hello"}
s1 = set("Hello")
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s1 & s2
s1.intersection(s2)
s2 - s1
s1.add(130294850)
s1.update([2,4,5,6,1,3,2,3,3,3,3])
s3 =  set([5,4,3,2,1])
s3.remove(3)
s3
s1
a = True
b = False
type(a)
type(b)
type(s1)
type(1>2)
"python"
a = {[1,2]:3} #error
a = {1:[1,2,3]}
a.get(1)
a = [1,2,3,4]
while a:
    print(a.pop())
'1' in a
type(a)
a = [1,2,3,4]

if a:
    print("참")
else:
    print("false")

while a:
    print(a.pop())
    
s1 = set([1,2,3])
l1 = list(s1)
s2 = set([1,2,3,4,5])
s1|s2
s2.difference(s1)
l2 = list(s2)
l2.index(3)
l2
while l2:
    print(l2.pop())
if l1:
    print("true")
else:
    print("false")

bool('python2')
bool(3)
a =  [1,2,3,4,5]
b = a
id(b)
id(a)
a is b
a[1] = 6
b[4] = 2
while a:
    print(a.pop())
from copy import copy
b = copy(a)
id(b)
c = a[:]
id(a)
a, b = ('pathetic', 'idiot')
a, b = b, a
a = a+"s"
a