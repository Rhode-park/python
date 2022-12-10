from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

x, y = 1, 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # graph[x][y]의 최단거리에다가 1을 더한게 graph[nx][ny]의 거리
                queue.append((nx, ny))
    return(graph[n-1][m-1])  # (n-1, m-1)의 좌표에 출구가 있으므로 출구에 해당하는 값을 return

print(bfs(0,0))