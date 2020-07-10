#근의공식
print("a*X^2 + b*X + c = 0")
while True:
    try:
        a = int(input("input integer for a from -10 to 10 : "))
        b = int(input("input integer for b from -10 to 10 : "))
        c = int(input("input integer for c from -10 to 10 : "))
        if a>=-10 and a<=10 and b>=-10 and b<=10 and c>=-10 and c<=10:
            break
    except ValueError:
        print("That was no valid number.  Try again...")

t = 1000000
x1 = t/100
x2 = t/100
flag = 0

for i in range((0-t), t):
    n = float(i / 1000)
    y_c1 = a * n**2 + b * n + c
    y_c2 = a * (n+0.001)**2 + b * (n+0.001) + c
    if y_c1 == 0:
        x1 = n
        break
    elif (y_c1 < 0 and y_c2 > 0) or (y_c1 > 0 and y_c2 < 0):
        x1 = n
        break
if x1 != t/100:
    for j in range(int((n+0.001)*1000), t):
        n = float(j / 1000)
        y_c1 = a * n**2 + b * n + c
        y_c2 = a * (n+0.001)**2 + b * (n+0.001) + c
        if y_c1 == 0:
            x2 = n
            break
        elif (y_c1 < 0 and y_c2 > 0) or (y_c1 > 0 and y_c2 < 0):
            x2 = n
            break
elif x1 == t/100:
    y = float(a * (t/100)**2 + b * t/100 + c)
    for i in range((0-t), t):
        n = float(i/1000)
        y_c1 = a * n**2 + b * n + c
        if abs(y_c1) < abs(y):
            x1 = n
            y = y_c1
            flag = 1
        else:
            x1 = x1
print()
if x2 == t/100 and flag != 1:
    print("x = {}".format(round(x1,2)))
    print()
    if a != 0:
        print("근의 공식값 : ",round(((0-b)-(((b**2)-4*a*c)**0.5))/(2*a),2)," ,  ", round((((0-b)+(((b**2)-4*a*c)**0.5))/(2*a)),2))
    print()
elif x2 == t/100 and flag == 1:
    print("0에 가장 가까운 값 x = {}".format(round(x1,2)))
    print("{}를 x에 입력해서 계산하면 나오는 값 : {}".format(round(x1,2),round((a*(x1**2) + b*x1 + c),2)))
else:
    print("x1 = {}, x2 = {}".format(round(x1,2), round(x2,2)))
    print()
    if a != 0:
        print("근의 공식값 : ",round(((0-b)-(((b**2)-4*a*c)**0.5))/(2*a),2)," ,  ", round((((0-b)+(((b**2)-4*a*c)**0.5))/(2*a)),2))
print()
