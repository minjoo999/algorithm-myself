# 오답 코드 : visited[x]의 수를 세는 식으로는 안됨
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

visited = [0 for _ in range(n+1)]


def dfs(x):
    print("현재 좌표: ", x)
    # visited[x] += 1
    if len(graph[x]) > 0:
        for g in graph[x]:
            if visited[g] == 0:
                print("다음 좌표: ", g)
                visited[g] = visited[x] + 1
                print("지금까지 횟수: ", visited[g])
                dfs(g)
            else:
                continue

    # visited[x] += 1

    # return g


visited[1] = 1
# d = dfs(1)
dfs(1)

print(visited)
# print(d)

# print(max(visited))
