# https://www.acmicpc.net/problem/16234

# 정답풀이

from collections import deque

n, l, r = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x,y,index):
    united = []
    united.append((x,y))
    queue = deque()
    queue.append((x,y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    queue.append((nx,ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))
    for i, j in united:
        graph[i][j] = summary//count
    return count

totalCount = 0

while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j,index)
                index += 1
    if index == n*n:
        break
    totalCount += 1

print(totalCount)