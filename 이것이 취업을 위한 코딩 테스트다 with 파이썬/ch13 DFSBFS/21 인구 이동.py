# https://www.acmicpc.net/problem/16234

n, l, r = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

land = A

def dfs():
    if 