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

