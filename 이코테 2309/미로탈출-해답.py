# DFS 때도 그러했듯, 문제 상황을 어떻게 추상화시킬지를 알고 판단하고 익숙해지는 게 참 중요함
# BFS 알고리즘 활용

from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 이동할 방향 정의 (상하좌우)
# 이후 x, y를 갖고 x + dx, y + dy를 인덱스로 삼아 BFS 진행함
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 활용 위해 함수 정의
def bfs(x, y):
    # 큐에 첫 원소 집어넣고 시작
    queue = deque()
    queue.append((x, y))

    while queue:

        # 큐에서 원소 꺼내기
        x, y = queue.popleft()

        # dx, dy 맞물려 상하좌우 인덱스좌표 돌도록 구성
        # 상하좌우 다 돌면 queue.popleft() 찍고 다음으로 넘어가기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 패스하기
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 값이 0이면 패스하기
            if graph[nx][ny] == 0:
                continue

            # 값이 1이면 지나가는 것으로 함
            # 이번칸이 1이면 다음칸은 2, 그다음칸은 3 이런 식으로 값이 늘어나도록 함
            # 갈길의 좌표를 큐에 집어넣음.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]


print(bfs(0, 0))
