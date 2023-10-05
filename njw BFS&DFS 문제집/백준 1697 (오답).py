import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

# x = N
cnt = 0
results = []


def dfs(x):
    global cnt
    cnt += 1
    print("현재 좌표: ", x)
    print("현재 초수: ", cnt)

    dx = [-1, 1, x]
    li = deque()

    for i in range(3):
        nx = x + dx[i]
        if nx < 0 or nx > 2*K:
            return False
        if nx == K:
            cnt += 1
            results.append(cnt)
            print(results)
            return True
            # return cnt
        else:
            li.append(nx)
            # dfs(nx)
            # # return False

    while li:
        dfs(li.popleft())

    return False


a = dfs(N)
print(a)
# print(results)
# print(min(results))
