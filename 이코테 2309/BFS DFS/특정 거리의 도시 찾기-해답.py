# DFS를 생각하고 풀었으나, 풀이는 BFS로 접근함. 같은 거리를 같은 뎁스로 접근해야 하니 이 접근이 맞음.

from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 도로 연결 정보 받기
# (1, 3), (2, 3)일 때 3에 1과 2가 연결되어 있다고 입력하지는 않음
# 근데 어차피 3에 1과 2가 연결된 걸 표시한다 쳐도, 아래에서 방문 이력 있는 도시로 이미 분류되어서 어차피 결과에는 영향 없음
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b].append(a)

print("도로 연결 정보: ", graph)

# 최단거리는 도시별로 기록. 미방문 시 -1
# 최단거리 기록이 BFS/DFS 교재 예제의 visited 와도 기능을 같이함
distance = [-1] * (N + 1)
distance[X] = 0

# BFS 수행
q = deque([X])
while q:
    now = q.popleft()
    # now와 도로로 연결된 graph[now]에서 미방문지가 있으면 거리 올리고 큐에 집어넣기
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

print("최단거리 리스트: ", distance)

check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)