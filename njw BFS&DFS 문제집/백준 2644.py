# 오답 코드 (10%대에서 오답)

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph_pc = [[] for _ in range(n+1)]
graph_cp = [0 for _ in range(n+1)]
for _ in range(m):
    parent, child = map(int, input().split())
    graph_pc[parent].append(child)
    graph_cp[child] = parent

print(graph_pc)
print(graph_cp)

visited = [0 for _ in range(n+1)]


def dfs(x):
    print("현재 좌표: ", x)

    if x == b:
        return True

    # 부모-자식 순으로 파고들기
    if len(graph_pc[x]) > 0:
        for g in graph_pc[x]:
            if visited[g] == 0:
                print("다음: ", g)
                visited[g] = visited[x] + 1
                dfs(g)

    else:
        gc = graph_cp[x]
        if gc == b:
            visited[gc] = visited[x] + 1
            return True
        if gc != 0 and visited[gc] == 0:
            visited[gc] = visited[x] + 1
            dfs(gc)

    return False


visited[a] = 1
dfs(a)

print(visited)

if visited[b] == 0:
    print(-1)
else:
    print(visited[b]-1)
