# https://www.acmicpc.net/problem/18405

# 답 한 번 보고 풀음

from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))  # 중간에 '0'은 흘러간 시간을 의미한다

targetS, targetX, targetY =  map(int, input().split())

data.sort()  # sort를 해줬기 때문에 1,2,3...의 순서로 바이러스가 번식한다 맞나?
queue = deque(data)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while queue:
    virus, s, x, y = queue.popleft()
    if s == targetS:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx and nx<n and 0<=ny and ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))

print(graph[targetX-1][targetY-1])

