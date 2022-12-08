# https://www.acmicpc.net/problem/3190

from collections import deque

n = int(input())
k = int(input())

apples = []
for i in range(k):
    apples.append(list(map(int, input().split())))

l = int(input())

directions = []
for j in range(l):
    directions.append(list(input().split()))

time = 0

x, y, d = 1, 1, 0

dirX = [1, 0, -1, 0]
dirY = [0, 1, 0, -1]

snake = deque()

def turn():
    if direction == 'D':
        d += 1
        if d == 4:
            d = 0
    elif direction == 'L':
        d -= 1
        if d == -1:
            d = 3

snake.append((1, 1))

while snake:
    for k in range(len(directions)):
        if time == directions[k][0]:
            direction = directions[k][1]
            turn()
    dx = x + dirX[d]
    dy = y + dirY[d]
    if dx<1 or dx>n or dy<1 or dy>n:
        break
    if [dx, dy] in snake:
        break
    time += 1
    snake.append((dx, dy))
    print(snake)
    for l in range(len(apples)):
        if dx != apples[l][0] or dy != apples[l][1]:
            snake.pop(0)

print(time)


# 제혁님 풀이

# import sys
# from collections import deque
#
#
# def changeDir(cur, dir):  # 방향 전환
#     if dir == 'r':
#         if cur == 3:
#             return 1
#         elif cur == 2:
#             return 0
#         elif cur == 1:
#             return 2
#         else:
#             return 3
#     else:
#         if cur == 3:
#             return 0
#         elif cur == 2:
#             return 1
#         elif cur == 1:
#             return 3
#         else:
#             return 2
#
#
# N = int(sys.stdin.readline())  # 보드 크기
# K = int(sys.stdin.readline())  # 사과 개수
#
# map = [[0] * (N + 1) for _ in range(N + 1)]  # 맵
#
# for _ in range(K):
#     x, y = sys.stdin.readline().strip().split()
#     map[int(x)][int(y)] = 2  # 사과 위치 = 2
#
# L = int(sys.stdin.readline())  # 뱀의 방향 변환 횟수
#
# change_dir = []  # 뱀의 방향 변환 저장할 배열
#
# for _ in range(L):
#     x, c = sys.stdin.readline().strip().split()
#     change_dir.append((x, c))
#
# sec = 0  # 시간
#
# snake_info = deque([])
# snake_info.append((1, 1))
#
# x, y = 1, 1  # 머리 위치
# map[1][1] = 1  # 뱀 위치 = 1
#
# snake_dir = 3  # 뱀의 머리가 현재 바라보는 방향 # default 오른쪽
#
# dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
#
# while True:
#     sec += 1  # 1초 증가
#
#     # 머리 이동 전 체크
#     dx = x + dir[snake_dir][0]
#     dy = y + dir[snake_dir][1]
#
#     # 벽에 닿았거나 본인의 몸과 부딪히면 종료
#     if dx > N or dy > N or dx < 1 or dy < 1 or map[dx][dy] == 1:
#         break
#
#     # 꼬리 이동
#     # 머리가 사과를 안먹었을 경우
#     if map[dx][dy] != 2:
#         tail = snake_info.popleft()
#         t_x = tail[0]
#         t_y = tail[1]
#
#         map[t_x][t_y] = 0
#
#     # 머리 이동
#     map[dx][dy] = 1
#     x, y = dx, dy
#     # 뱀 위치 정보 갱신
#     snake_info.append((dx, dy))
#
#     # 뱀의 이동 경로가 바뀌었을 경우
#     if len(change_dir) > 0 and sec == int(change_dir[0][0]):
#         # 오른쪽으로 90도
#         if change_dir[0][1] == 'D':
#             snake_dir = changeDir(snake_dir, 'r')
#         else:  # 왼쪽으로 90도
#             snake_dir = changeDir(snake_dir, 'l')
#
#         change_dir.pop(0)
#
# print(sec)