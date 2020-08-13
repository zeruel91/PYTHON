#Alg HW Last time
#두 문자열의 공통분모의 길이를 반환하는 

s1 = 'THEISIS'
s2 = 'THESTRINGS'
s1[0:6]
'THE' in s2
c = [x for x in s1 if x in s2 and len(x) == 2]
c
s1 = list(s1)
s2 = list(s2)

#string 형태로 찾는게 더 유리하겠네

#주어진 string 에 대해 존재하면 True 를 출력하는

c = [x for x in a if x in b and len(x) == i]


def LongestCommonSubsequence(a,b):
    # a,b 문자열에 대해 b 가 더 긴 문자열이라고 가정
    
    #작은 리스트에 대해서 연속된 i 개의 문자에 대한 리스트와의 공통분모 탐색
     
    c = []
    
    for i in range(1,len(a)):
        for j in range(len(a)-i):
            if a[j:j+i] in b:
                c.append(a[j:j+i])
                print(c)
    result = max([len(x) for x in c])    
    return result
        
LongestCommonSubsequence(s1,s2)

            

#cmd -> pip install notebook -> jupyter notebook
import matplotlib.pyplot as plt
plt.plot([10, 20, 30, 40])
plt.show()


#Algithm HW

x =eval(input('write here: '))


try:
    x = eval(input('write here: '))
    if x - int(x) == 0:
        print('it is integer')
    else:
        print('it is not a integer')
except:
    print('math error')

#__________________________________________________________

plt.figure(figsize = (6,6))
plt.scatter(x,y, c= 'g' , s = 100, label = 'dot graph')
plt.plot(x,y,c='g',alpha = 0.5, label = 'line graph')
plt.grid
plt.xticks(fontsize = 14, color = 'b')

