# 막판에 예외처리로 애를 좀 먹음. dfs가 여러개 있는 단지에서는 제대로 된 갯수를 뽑아내는데, 1개짜리 단지에서는 0개로 나와서.
# 변수 갯수 처리할 때 디테일한 흐름 봐야할듯 (풀이: https://hongcoding.tistory.com/71)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

print(graph)

# 단지수: dfs의 첫 트리거가 몇 번 실행되었는가?
# 단지별 집의 수: dfs 파고들어 횟수 더해주는 거로 하기
# dfs(x, y)에서 graph[x][y]의 방문처리가 미흡했던 게 원인. 이거 해결하니 예외처리 없이도 정답 나옴.
buildings = 0


def dfs(x, y):
    global buildings
    buildings += 1
    graph[x][y] = 0
    print("현재 좌표: ", x, y)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if graph[nx][ny] == 1:
            # graph[nx][ny] = graph[x][y] + 1
            # buildings += 1
            dfs(nx, ny)


results = []
groups = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            groups += 1
            dfs(i, j)
            print(f"**{groups}단지 아파트: {buildings}개")
            print("=================")
            # if buildings == 0:
            #     results.append(1)
            # else:
            #     results.append(buildings)
            results.append(buildings)
            buildings = 0

print(groups)
results.sort()
for r in results:
    print(r)
