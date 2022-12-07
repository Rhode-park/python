n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x,y):
    if x<1 or x>n or y<1 or y>m:
        return False
    