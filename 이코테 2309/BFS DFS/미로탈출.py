from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

print(graph)

D = deque()

cnt = 0


def bfs(height, width, cnt):
    # cnt = 0

    if height <= -1 or height >= N or width <= -1 or width >= M:
        return False

    if graph[height][width] == 1:
        graph[height][width] = 0
        cnt += 1
        bfs(height+1, width, cnt)
        bfs(height-1, width, cnt)
        bfs(height, width+1, cnt)
        bfs(height, width-1, cnt)
        return True


for i in range(N):
    for j in range(M):
        b = bfs(i, j, cnt)
        # if b == True:
        #     cnt += 1

        # if graph[i][j] == 1:
        #     graph[i][j] = 0
        #     D.append(graph[])

print(cnt)
