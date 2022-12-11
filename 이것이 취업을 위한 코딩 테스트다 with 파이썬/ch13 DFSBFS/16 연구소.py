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
#
#

# 택도 없는 풀이라서 정답 봄

# n, m = map(int, input().split())
# data = []
# temp = [[0] * m for _ in range(n)]
#
# for _ in range(n):
#     data.append(list(map(int, input().split())))
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# result = 0
#
# def virus(x,y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx>=0 and nx<n and ny>=0 and ny<m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx,ny)
#
# def getScore():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score
#
# def dfs(count):
#     global result
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = data[i][j]
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i,j)
#         result = max(result, getScore())
#         return
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 data[i][j] = 0
#                 count -= 1
#
# dfs(0)
# print(result)