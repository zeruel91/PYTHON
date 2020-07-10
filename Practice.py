Q1

t = {'국어':80,'영어':75,'수학':55}

Everage=(t['국어']+t['영어']+t['수학'])/len(t)
Everage
Q2

x = 13
y=x%2
y
    if y:
        print('odd')
    else:
        print('even')
    
Q3
ID='881120-1068234'
print(ID[:6])
print(ID[7:])

Q4
pin = "881120-1068234"
pin[7]

Q5
a = "a:b:c:d"
a.replace(":","#")
a.replace(":","")

Q6
a = [1,3,5,4,2]
a.sort()
a.reverse()
a

Q7
a = ['life', 'is', 'too', 'short']
" ".join(a)

Q8
a = 1,2,3
type(a)
(a[0],a[1],a[2],4)

a = a +(4,)
print(a)

Q9
a = dict()
#3. key 위치엔 리스트가 올 수 없다.

Q10
a = {'A':90, 'B':80, 'C':70}
a.pop('B')
a

Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(a)
b

Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)

#b와a 의 id 위치가 같기 때문에 같이 변경된다.