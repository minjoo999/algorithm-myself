# 답은 맞는데 recursion error, recursion error 해결 이후에는 ValueError가 뜨네
# 전체 DFS 탐색을 여러번 돌리는 구조가 문제인것 같은데, 그걸 어떻게 하면 될까?


N = int(input())
area = []

min_areas = []
max_areas = []

for _ in range(N):
    li = list(map(int, input().split()))
    area.append(li)
    min_areas.append(min(li))
    max_areas.append(max(li))

# 높이 범위 구하기
min_x = min(min_areas)
max_x = max(max_areas)

print(area)
print(min_x, max_x)

# 각 물 높이별로 영역 갯수 세서 (아마도 DFS 흐름갯수...) 그중 최대치 구하기
# 탐색횟수를 줄일수 있는 아이디어는 뭘까

# DFS 함수 파트


def dfs(x, y, std):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        print("진행 자표: ", nx, ny)

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if visited[nx][ny] == 1:
            continue

        if area[nx][ny] > std and visited[nx][ny] == 0:
            print("*방문가능 좌표: ", nx, ny)
            visited[nx][ny] = 1
            dfs(nx, ny, std)

    return False


# 물 높이별로 영역 갯수 세는 파트
now_x = min_x

results = []
while now_x < max_x:
    cnt = 0
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] > now_x:
                print("*현재 좌표: ", i, j)

                cnt += 1
                print(f"지금 카운트: {cnt}, 지금 높이: {now_x}")
                visited[i][j] = 1
                dfs(i, j, now_x)

    results.append(cnt)
    now_x += 1

print(results)

if max(results) == 0:
    print(1)
else:
    print(max(results))
