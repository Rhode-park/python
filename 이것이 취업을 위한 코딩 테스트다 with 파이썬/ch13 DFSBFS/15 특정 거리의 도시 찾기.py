# https://www.acmicpc.net/problem/18352

import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1 for i in range(n+1)]
distance[x] = 0  # 출발지점의 거리는 0으로 초기화 해주기!!

queue = deque()
queue.append(x)
while queue:
    now = queue.popleft()
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

count = 0

for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        count += 1
if count == 0:
    print("-1")


# 런타임 에러 떴음
# import sys
# input = sys.stdin.readline
# 이렇게 두 줄 추가했더니 해결 됨