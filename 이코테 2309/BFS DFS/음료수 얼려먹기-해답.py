N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))  # split 없이도 숫자 떼어내서 리스트 만들기 가능하네

# [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]] 형태로 출력
print(graph)

# graph[0][1] = 0 과 같은 형태로 볼 수 있음. 그러므로 가로세로 좌표를 늘리고 줄이며 진행시키기 가능


def dfs(x, y):
    # x, y는 인덱스. -1, +1 과정에서 원하는 범위를 넘으면 함수 진행 멈추기
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1  # 방문처리

        # 상하좌우 위치에 대해 함수 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False


result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행 이후, 이 위치가 방문된 위치라면 result += 1
        # 재귀 처음 시작하는 노드의 갯수만큼 result가 나오게 함. 재귀 첫시작이어야 dfs가 True를 리턴하니까.
        # 처음 하는 재귀 말고, 2-3-4차 재귀 뎁스가 들어간 경우까지 result를 더하라는 건 아님.
        if dfs(i, j) == True:
            result += 1

print(result)
