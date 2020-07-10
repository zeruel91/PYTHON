for student in [1, 2, 3, 4, 5]:
    print(student, "번 학생의 성적을 비난한다")

for student in range (-3, 6):
    print(student, "번 학생의 성적을 처리한다")
# for 범위집합이름 ran(이상,미만,등차):
sum = 0
for num in range(2,101,2):#3번째 변수에 정수만 가능
    sum += num
    if num == 100:
        print("sum =",sum)

for x in range(1,51):
    if (x % 10 == 0):
        print("+", end='')#end=''줄바꿈을 없애는 것
    else:
        print("-", end='')

for x in range(1,51):
    if (x % 10):
        print("-",end='')
    else:
        print("+",end='')

x = 1
while x <=50:
    if (x % 10):
        print('-',end='')
    else:
        print('+',end='')
    x += 1 #while 구문에서 x 의 제한이 없으면 루프로 빠짐. 주의

x = 1
while x<=500:
    if (x % 5):
        print('-',end='')
    else:
        print('+',end='')
    x += 1
def Stack() :
    stack = []
    
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    print(stack)

    while stack :
        print("pop Value is",stack.pop())
Stack()