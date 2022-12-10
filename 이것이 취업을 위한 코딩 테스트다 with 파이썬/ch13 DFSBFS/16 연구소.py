# https://www.acmicpc.net/problem/14502

# from collections import deque
#
# n, m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# queue = deque()
#
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 2:
#             queue.append((i,j))
#
# while queue:
#     virus = queue.popleft()
#     x, y = virus[0], virus[1]
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx<0 or nx>=n or ny<0 or ny>=m:
#             continue
#         if graph[nx][ny] == 1:
#             continue
#         if graph[nx][ny] == 0:
#             graph[nx][ny] = 2
#             queue.append((nx,ny))
#         if graph[nx][ny] == 2:
#             queue.append((nx,ny))
#
# count = 0
#
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             count += 1
#
# print(count)


