# https://www.acmicpc.net/problem/14502

# 정답 풀이 : 시간초과 뜸 - 이 방법은 지양해야 함 for문 중첩이 너무 심함, 제혁님 풀이가 더 적절함

# n, m = map(int, input().split())
# data = []
# temp = [[0] * m for _ in range(n)]  # 왜 temp를 굳이 따로 둬서 count가 3일 때 data를 받아주는거지?
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
#     for i in range(n):  # 근데 이렇게 하면 숫자가 작은? 배열에만 벽이 세워지는 것 아닌가?
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 data[i][j] = 0  # 이 두 줄 이해가 안 됨.. 왜 다시 벽을 치우는거지?
#                 count -= 1
#
# dfs(0)
# print(result)

# 제혁님 풀이

# import sys
# from collections import deque
# from copy import deepcopy
# from itertools import combinations
#
# N, M = map(int, sys.stdin.readline().strip().split())
#
# maps = []
# zeros = []
# viruses = []
#
# for i in range(N):
#     maps.append(list(map(int, sys.stdin.readline().strip().split())))
#
#     for j in range(M):
#         if maps[i][j] == 0:
#             zeros.append((i, j))
#         if maps[i][j] == 2:
#             viruses.append((i, j))
#
# zeros = list(combinations(zeros, 3))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]
#
#
# def bfs(tmp_map, x, y):
#     datas = [(x, y)]
#     queue = deque(datas)
#
#     while queue:
#         data = queue.popleft()
#
#         x = data[0]
#         y = data[1]
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or ny < 0 or nx >= N or ny >= M:
#                 continue
#
#             if tmp_map[nx][ny] == 0:
#                 queue.append((nx, ny))
#                 tmp_map[nx][ny] = 2
#
#     return tmp_map
#
#
# sizes = []
#
# for zero in zeros:
#     tmp_map = deepcopy(maps)
#
#     for data in zero:
#         tmp_map[data[0]][data[1]] = 1
#
#     for virus in viruses:
#         tmp_map = bfs(tmp_map, virus[0], virus[1])
#
#     size = 0
#
#     for i in range(N):
#         for j in range(M):
#             if tmp_map[i][j] == 0:
#                 size += 1
#
#     sizes.append(size)
#
# print(max(sizes))