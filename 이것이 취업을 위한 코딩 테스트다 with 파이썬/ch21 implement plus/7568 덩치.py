# https://www.acmicpc.net/problem/7568

n = int(input())

data = []

for i in range(n):
    data.append(list(map(int, input().split())))

scores = [0] * n

for j in range(n):
    for k in range(n):
        if data[j][0] > data[k][0]:
            if data[j][1] > data[k][1]:
                scores[j] += 1

rank = [n+1] * n

for l in range(n):
    for m in range(n):
        if scores[l] >= scores[m]:
            rank[l] -= 1


print(*rank, sep= ' ')

# 틀렸음, 게다가 for문을 너무 많이 쓴 것 같음
# 예시는 잘 돌아가는데.. 왜지...??

