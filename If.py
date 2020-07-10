country = "Korea"


if country == "Korea":

    print("한국입니다.")

if country=="korea":

    print("대한민국입니다.")

a = 3

if 1 < a < 10:
    
    print("OOK")

else:
    print("too much")

age = 22

if age < 19:
    
    print("애들은 가라")


else:
    if age < 25:
        print("something")
    else:
        print("Hello")
    
money = 6500

if money >= 20000:
    print("탕수육 먹기")

else:
    if money >= 10000:
    
        print("쟁반 짜장을 먹는다")
    
    if money >=6000:
    
        print("짬뽕을 먹는다.")
    
    elif money >= 4000:
    
        print("짜장면을 먹는다.")
    
    else:
    
        print("단무지나 처먹어")

Man = True
age = 22
if Man and age >= 19:
    print("adult male")

if Man == True:
    if age >= 19:
        print("Adult male")
    else:
        print("A boy")


money = True

if money:

    print("get a taxi")

else:
    print("take a walk")

#---------------------------------------------

pocket = 'paper', 'cellphone', 'money'

if 'money' in pocket:
    
    print("get a cab")   #pass 명령을 시행하면 아무것도 하지않음.

else:

    print('take a walk')


type(pocket)

score = 70

if score >= 60:

    message = "triumph"

else:

    message = "defeated"
score = 70
message = 'victory' if score >=60 else "failure"
print(message)
