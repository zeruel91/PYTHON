student = 1 
while student <= 5:
    print(student, "번 학생의 성적을 처리한다.")
    student += 1

n = 1

sum = 0

while n <=100:

    sum = sum + n

    n = n+1

    if n==101:

        print("sum=",sum)


treeHit = 0

while treeHit < 10:

    treeHit = treeHit + 1

    print("I %d slashed tree" %treeHit)

    if treeHit == 10:

        print("the tree is down")

money = 2000

card = True

if money>= 3000 or card:
    print("get a cab")
else:
    print("take a walk")

'a' in ('a', 'b', 'c')
'P'not in 'python'
a='python'
a.upper()

prompt = """
1.Add
2.del
3.list
4.quit

Enter number:"""

number = 4
while number !=4:
    print(prompt)
    number = int(input())
    break

coffee = 10

money = 300

while money:
    print("that cash gives you coffee")
    coffee = coffee - 1
    print("left over coffee is %d 개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("here's your coffee")
        coffee = coffee - 1
    elif money > 300:
        print("here's your coffee and change %d won" %(money-300))
        coffee = coffee - 1
    else:
        print("are you freakin kidding me?")
        print("the number of left over coffee is %d" % coffee)
    if coffee == 0:
        print("we are out of coffee today")
        
        break



a = 0
while a < 10:
    a = a + 1
    if (a % 2) == False: continue
    print(a,end='')


#infinite loop
while True:
    print("Ctrl+C only makes you escape from this loop")

