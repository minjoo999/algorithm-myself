# 각 좌표가 0인지 1인지 표시하는 visited 리스트와 좌표 (1, 1) 등 표시하는 graph 리스트 함께 만들었음
# '편하게 상하좌우를 살피게 할 수 있는 방법'을 몰라 애먹음


from collections import deque

N, M = map(int, input().split())
visited = []
graph = []

for n in range(N):
    k = input()
    visited.append(k)
    for m in range(M):
        # visited.append(int(k[m]))
        graph.append((n+1, m+1))

print(visited)
print(graph)

D = deque()

cnt = 0

def count_ice(width, height):
    if visited[width][height] == '0':
        # 상하좌우 탐색해서 0인 곳 찾기



for n in range(N):
    for m in range(M):
        if visited[n][m] == '0':


for i in range(len(graph)):
    if visited[i] == 0:
        g = graph[i]


# for i in range(len(graph)):
#     if visited[i] == 0: