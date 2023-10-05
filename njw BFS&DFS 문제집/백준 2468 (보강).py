# recursion error 방지용 (참고: https://velog.io/@phw1996/백준-2468번-안전-영역-파이썬)
# setrecursionlimit 남용 주의해야 하지 않을까?
import sys
sys.setrecursionlimit(100000)

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


def dfs(x, y, std):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        print("진행 자표: ", nx, ny)

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if area[nx][ny] > std and visited[nx][ny] == 0:
            print("*방문가능 좌표: ", nx, ny)
            visited[nx][ny] = 1
            dfs(nx, ny, std)

    return False


# 물 높이별로 영역 갯수 세는 파트
now_x = min_x

# 비교대상인 '현재 최대값' ans를 만들어놓고, 내부에서의 재귀횟수 (=영역 갯수) cnt와 비교해서 ans를 조정하는 것
# 과거에는 cnt를 리스트로 만들어서 max값 구하는 식으로 했는데 이게 ValueError 만드는 맹점 있었음
ans = 1
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

    ans = max(ans, cnt)
    now_x += 1

print(ans)
