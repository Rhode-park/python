place = input()

x = ord(place[0]) - ord('a') + 1
y = int(place[1])

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx>=1 and nx<=8 and ny>=1 and ny<=8:
        count += 1

print(count)