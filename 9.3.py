# 카운터에는 거스름돈으로 사용할 500원, 100원 50원,
# 10원짜리 동전이 무한히 존재한다고 가정한다. 손님에게
# 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의
# 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상

def change(n):
    n1 = n // 500
    n = n - 500*n1
    n2 = n // 100
    n = n - 100*n2
    n3 = n // 50 
    n = n - 50*n3
    n4 = n // 10
    return "{}개".format(n1+n2+n3+n4)


change(1320)

>>> change(1320)
'7개'

n = 1260
count = 0
# 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]
for coin in coin_types:
count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
n %= coin
print(count) #6

n = 1260
count = 0

coin_types = [500, 100, 50, 10]
coin_count = 0
for coin in coin_types:
    coin_count += n // coin
    n %= coin
print(coin_count)