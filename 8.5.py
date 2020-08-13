#앞자만따는 문제
def reduce(a):
    result = a.split(' ')
    i = 0
    while i != len(result):
        print(result[i][0])
        i += 1

reduce('복잡한 세상 편하게 살자')

#모범답안 1.
user_input = input().split(' ')
print(user_input)
result = ''

for s in user_input:
    result += s[0]

print(result)
#2.
user = input('English or Korean').split(' ')
for i in user:
    print(i[0],end = '')


a = [1,2,3,4]
b = [a, b, c, d]

result = []
for i in range(len(a)):
    if i % 2 == 0:
        result.append([a[i],b[i]])
    else:
        result.append([b[i],a[i]])


