#####################################################################
def divider(a):
    result = []
    for i in range(1,a+1):
        if a % i == False:
            result.append(i)
    return result

prime = [] 
for x in range(10):
    if len(divider(x)) == 2:
        prime.append(x)
print(prime)   

####################################################################
divider(9973)

n = int(input("num : "))
a = 0 
b = 1
print('0', end='')
while b <= n:
    print(',%d'%b,end='')
    a,b = b,a+b


