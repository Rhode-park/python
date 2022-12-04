n = int(input())
plans = input().split()  #plans = list(map(str, input().split())) 이런 식으로 쓸 필요 없음

x, y = 1, 1

moveType = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(moveType)):
        if plan == moveType[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<1 or nx>5 or ny<1 or ny>5:
                continue
            x, y = nx, ny  #이 과정을 꼭 해줘야지 다음 for문에서 nx = x + dx[i]의 x에 반영이 됨

print(x, y)