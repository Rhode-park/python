# https://www.acmicpc.net/problem/1012

T = int(input())
M, N, K = map(int, input().split())

graph = [[0]*M for i in range(N)]
cabbages = []
for i in range(K):
    (cabbageX, cabbageY) = map(int, input().split())
    graph[cabbageX][cabbageY] = 1
    cabbages.append([cabbageX, cabbageY])

print(cabbages)
print(graph)