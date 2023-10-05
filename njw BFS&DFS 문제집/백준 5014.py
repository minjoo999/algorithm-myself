# 직접 짠 코드에 참고사항 보완
# 참고사항: https://www.acmicpc.net/board/view/99006

import sys
from collections import deque

input = sys.stdin.readline


F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F)]

# 10층이라면 인덱스 0~9로 간다고 생각하고 함수 제작


def bfs():
    queue = deque([S-1])
    # 첫층 방문처리 필수
    # 써주고 이후에 뺀다 쳐도, 일단 쓰는게 맞음. 이후 첫층 방문처리 안해서 오계산 꽤 발생하는 듯.
    visited[S-1] = 1

    while queue:
        x = queue.popleft()
        if x == G-1:
            break

        for nx in (x - D, x + U):
            print("*현재좌표: ", nx)
            if 0 <= nx < F and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                print(f"좌표 {nx}: {visited[nx]}")
                queue.append(nx)

        print(queue)


bfs()
print("결과: ", visited)

# 시작층==끝층 일 경우 현재 로직상 1 나오므로 일부러 0 보여주기
if S == G:
    print(0)
else:
    if visited[G-1] == 0:
        print("use the stairs")
    else:
        # visited[첫층]에 +1 해줬으니 막판에 -1 해주기
        print(visited[G-1]-1)
