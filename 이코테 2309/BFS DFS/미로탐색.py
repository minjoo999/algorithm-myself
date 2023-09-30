# 처음에는 큐 들어가는 원소 카운팅으로 문제를 풀려고 했으나, 흔히 말하는 '막다른 길'의 원소도 카운팅이 되어 오답이 발생
# 이런 경우는 해당 인덱스의 값을 누적시켜 카운팅하는 게 더 좋음


from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

print(graph)

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


queue.append((0, 0))
cnt = 1
while queue:
    print(queue)

    x, y = queue.popleft()
    print("*현재 노드: ", x, y)
    print("*현재 누적값: ", graph[x][y])

    # can_visit = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        print("주변 인덱스: ", nx, ny)

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if graph[nx][ny] == 0 or graph[nx][ny] > 1:
            continue

        if graph[nx][ny] == 1:
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[N-1][M-1])
