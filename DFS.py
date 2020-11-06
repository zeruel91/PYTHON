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
