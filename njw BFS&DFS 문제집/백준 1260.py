import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

print(graph)

dfs_visited = [0 for _ in range(N+1)]
dfs_result = []


def dfs(x):
    dfs_result.append(x)
    dfs_visited[x] = 1

    if len(graph[x]) > 0:
        for i in graph[x]:
            if dfs_visited[i] == 1:
                continue

            if dfs_visited[i] == 0:
                dfs(i)


bfs_visited = [0 for _ in range(N+1)]
bfs_result = []


def bfs(x):
    queue = deque()
    queue.append(x)
    bfs_visited[x] = 1
    bfs_result.append(x)

    while queue:
        q = queue.popleft()

        for g in graph[q]:
            if bfs_visited[g] == 0:
                queue.append(g)
                bfs_visited[g] = 1
                bfs_result.append(g)


dfs(V)
bfs(V)

print(*dfs_result)
print(*bfs_result)
