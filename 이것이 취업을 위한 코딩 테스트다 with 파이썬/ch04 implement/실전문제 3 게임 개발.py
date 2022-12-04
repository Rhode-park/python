n, m = map(int, input().split())
x, y, direction = map(int, input().split())

mapData = []
for i in range(n):
    mapData.append(list(map(int, input().split())))

def turnLeft():

    d