# https://www.acmicpc.net/problem/18406

n = input()

total = 0
left = 0

for i in range(len(n)):
    total += int(n[i])

for j in range(len(n)//2):
    left += int(n[j])

right = total - left

if left == right:
    print('LUCKY')
else:
    print('READY')