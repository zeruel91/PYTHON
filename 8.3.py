#Algorithm HW

def multiple(x,n):
    result = []
    for i in range(1,x):
        if n*i == x:
            result.append(i)
    if result != []:
        return True
    else:
        return False

multiple(24,3)
multiple(15,2)

#Euclid Algorithm

def Euclid(a,b):
    Emin = min(a,b)
    Emax = max(a,b)
    if Emax % Emin == 0:
        return print(Emin)
    while Emin != Emax and Emin != 1:
        Emin,Emax = Emax%Emin,Emin
        continue
    return print(Emin)
##나무위키
def Euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    
    return a

def Euclidean(a, b):

  r = b % a

  if r == 0:
    return a

  else:
    return Euclidean(r, a)

    
Euclid(14,15)

#Fibonacci 

def Fib(n):
    result = [0,1]
    if n == 1 or n == 2:
        return result[n-1]
    else:
        for i in range(2,n):
            result.append(result[i-1]+result[i-2])
    return result[n-1]

Fib(1513)


#prime number 에 대한 재귀함수를 짜고싶다.
# 프라임을 설정, 이후나오면 프라임을재설정,
#프라임 리스트에서 원소로 안나눠지는 최초 정수를 프라임에 추가.


#prime 함수에서의 재귀호출은 의미가..

# a = [2,3,5,7]

# def next_prime(a):1240912rj02jt010uy920jktsmkgpok
    
#     start = max(a)+1
#     for i in range(start+1, start*2):
#         c = 0
#         for j in a:
#             if i % j == 0:
#                 c += 1
#             if c == 0:
#                 return i

# next_prime(a)
# next_prime([2])

# def next_prime2(b):
#     result = [2]
#     if b == 2:
#         return result
#     else:
#         while max(result) > b:
#             result += next_prime(result)
#         return result


# next_prime2(123)











#나무위키 에라토스테네스
def prime_list(n):
    sieve = [True]*n

    n = int(n**0.5)
    for i in range(2, m +1):
        if sieve[i] == True:
            for j in range(i+i,n,i):
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i] == True]


'''
리스트 주어졌을때, 어느 수가 이것으로 나누어지는지 여부 판별.
해당값을 n ~ 2n 까지 체크
결과값을 리스트에 추가.'''  

def relative_prime(a,b):
    c = 0
    for i in a:
        if b % i == 0:
            c += 1
    if c == 0:
        return True
    else:
        return False

def next_prime(a):
    i = max(a)+1
    while relative_prime(a,i) == False:
        i += 1
    a.append(i)
    return a

next_prime([2,3,5,7])


def repeat_til(a):
    result = [2]
    while max(next_prime(result)) < a:
        result = next_prime(result)
    return result[:-2]


repeat_til(124)
    