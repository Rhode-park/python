n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:  # 종료조건1
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False  # 종료조건2 : 근데 왜 쓰는지 모르겠음.. graph[x][y] != 0일 경우에 False를 return한다는걸까..?

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)