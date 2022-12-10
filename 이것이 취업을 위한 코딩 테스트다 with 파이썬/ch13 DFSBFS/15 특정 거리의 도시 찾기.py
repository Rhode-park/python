# https://www.acmicpc.net/problem/18352

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 단방향도로이므로 graph[b].append(a)는 해주지 않음

distance = [-1] * (n+1)
distance[x] = 0

queue = deque()
queue.append(x)
while queue:
    now = queue.popleft()
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

count = 0

for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        count += 1

if count == 0:
    print(-1)

# 시간 초과 뜸.. 왜지..?
