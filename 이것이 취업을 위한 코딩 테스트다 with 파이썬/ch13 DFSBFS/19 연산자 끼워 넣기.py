# https://www.acmicpc.net/problem/14888

# 답 한 번 보고 풀음

n = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiple, devide = map(int, input().split())

maxValue = -1e9
minValue = 1e9

def dfs(i, now):
    global maxValue, minValue, plus, minus, multiple, devide
    if i == n:
        minValue = min(minValue, now)
        maxValue = max(maxValue, now)
    else:
        if plus>0:
            plus -= 1
            dfs(i+1, now+numbers[i])
            plus += 1  # 복구 해줘야 다음 if에서 동등한 조건으로 걸려 넘어가기 때문인가..?
        if minus>0:
            minus -= 1
            dfs(i+1, now-numbers[i])
            minus += 1
        if multiple>0:
            multiple -= 1
            dfs(i+1, now*numbers[i])
            multiple += 1
        if devide>0:
            devide -= 1
            dfs(i+1, int(now/numbers[i]))
            devide += 1

dfs(1, numbers[0])

print(maxValue)
print(minValue)