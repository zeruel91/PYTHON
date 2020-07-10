prime = [2]
n = 3
comp = []
for n in range(10):
    for a in range(2,n):
        if n%a == False:
            comp.append(a)
            
            if comp == False:
                prime.append(n)
        
                comp = []

print(prime)
    


b = []
for a in range(10):
    b = b + [a]
print(b)


#divider
def divider(a):
    result = []
    for i in range(1,a+1):
        if a % i == False:
            result.append(i)
    return result

prime = [] 
for x in range(1000):
    if len(divider(x)) == 2:
        prime.append(x)
print(prime)        



