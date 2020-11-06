N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_, max_ = 1e9, -1e9

def dfs(i, res, add, sub, mul, div):
    global max_, min_#맥스값과 미니멈 값만 밖에서 받아온다.
    if i == N:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return

    else:
        if add:
            dfs(i+1, res+nums[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-nums[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)
            #if 문의 각 분화되는 과정은 순차적으로 모두 빠짐없이 일어난다.
            #글로벌로 연산자의 남은 횟수를 가져오지 않았기 때문에
            #각각의 다른 계산에 대해
            #복구해줄 필요가 없다.

dfs(1, nums[0], add, sub, mul, div)
#i 와 res 는 굳이 적힌대로 일 필요가 없지만
#빠짐없이 모든원소를 포함해서 계산해줘야하기때문에
#1과 0으로 잡는게 간편하다.
print(max_)
print(min_)
#해당 연산의 횟수는 연산자의 합인 N-1 에 대한 팩토리얼에, 분화된 값들의 각 팩토리얼의 나눗셈과 같다.
#가령 연산횟수 10에 3,2,2,2 의 배열이라면
#10!/3!2!2!2! 이란 소리.
-------------------------------------------------------
n = int(input())
# 연산을 수행하고자 하는 횟수
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())
# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1
            #해당 문제에서는 글로벌 값으로 처리했기때문에 다시 복구해줘야한다.
            #그렇지 않으면 아직 연산하지 않았는데, 연산횟수가
            #차감되어 있는 오류가 생긴다.
dfs(1,data[0])
print(min_value)
print(max_value)
