# BFS 풀이 (루트 잇기 구성이라 DFS도 해봤지만, 무한루프를 피하지 못함)
# BFS를 파고들면서도 무한정 늘어나지 않을 방법은 뭘까?
# 해설 참고 (링크: https://wook-2124.tistory.com/273)
# 5-10-9-18-17 루트 어떻게 찍히지? -> 이런 식으로 한 루트로 이어지는 흐름을 visited[nx] = visited[d] + 1 로 표현
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0 for _ in range(10**5 + 1)]


def bfs(x, y):
    global cnt
    D = deque([x])
    print(D)

    while D:
        d = D.popleft()
        if d == y:
            print("최종 결과: ", visited[d])
            break
        dx = [-1, 1, d]
        for i in range(3):
            nx = d + dx[i]
            print("예상 좌표: ", nx)

            # visited[nx]를 함수 원 좌표인 visited[x]가 아니라,
            # 덱에서 뺀 visited[d]와 비교해야 하는 거였음
            if 0 <= nx < 10**5 and not visited[nx]:
                visited[nx] = visited[d] + 1
                D.append(nx)
                print(D)


bfs(N, K)
