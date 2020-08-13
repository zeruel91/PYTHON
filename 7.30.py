#Algorithm Homework

s = 'aaaabbbcccbcbcaaaa'
result = s[0]
count = 0
for i in s:
    if i == result[-1]:
        count += 1
    else:
        if count == 1:
            result += i
        else:
            result += str(count)+i
            count = 1
result += str(count)
print(result)
#잘못했네

##_________________________________________________________________

#zip fuction
a = [1,2,3,4,5]
b = [6,5,4,3,2]
tuple(zip(a,b))
sum(a)
import numpy as np
def plus(*args):
    return np.sum(np.array(args)) #??? : 왜 엔피를 쓰는지 모르겠다.
c = [1,23,6,278,23,7,23476,25,12]
print(sum(c))
print(plus(c))

def plus_multiple(a,*b):
    return a*(plus(b))

plus_multiple(2,1,2,3)

dict(zip(a,b))  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def zip2(a,b):
    result = []
    if len(a) != len(b):
        return 'there is no 1-1 onto ft'
    else:
        for i in range(len(a)):
            result.append((a[i],b[i]))
    return result

zip2(a,b)

#웬만한 그래프는 pyplot으로 그릴 수 있다.
import matplotlib.pyplot as plt
plt.scatter(a,b)

import matplotlib.pyplot as plt
a = 1
b = 2
plt.scatter(a,b,s=15,c='g')
#s = size , c = color
plt.show()
#점과 점 선으로 잇기.
plt.plot(a,b)

#linewidth, alpha(transparency 0.5~)
plt.plot(a,b,linewidth = 5)
#둘다보고싶으면
plt.plot(a,b,linewidth = 5)
plt.scatter(a,b,s=15,c='g')
plt.show()
#격자
plt.grid()
# size for graph
plt.figure(figsize = (6,6))
plt.scatter(a,b,s=15,c='g')
plt.plot(a,b,linewidth = 5,alpha = 0.5,label = 'line graph')
plt.grid()
# closed x range
plt.xlim([0,6])
plt.scatter(a,b, c= 'g',s = 100,label = 'dot graph')
plt.legend() #plt.legend 를 안하면 라벨 주석 표시안됨
plt.legend(fontsize = 1, loc = 4)
plt.show()
#x축 표기값 변경
plt.xticks(fontsize = 14, color = 'b')

#Algorithm Homework
"""
1. 이름탐색
    O(n)
2. 전화번호 -> 이름
    O(n)
3. O(n)
4. n -> n/26
    O(n)




""" 