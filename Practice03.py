a = 1
sum = 0
while a<=1001:
    if (a%3==0):
        sum +=a
        
    elif a == 1000:
        print("sum = ",sum)

    a += 1
a = range(1001)

Q3
n = 0
while (n<=5):

    print("*"*n)

    n = n+1


A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
n=0
sum=0
while n<len(A):
    sum = sum + A[n]
    n = n+1
    
print(sum/len(A))

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)