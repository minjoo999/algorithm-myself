# 풀이 제시 실패 버전

import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

# 빈 리스트 N개짜리 리스트 cities
cities = [[] for _ in range(N+1)]

for _ in range(M):
    home, away = map(int, input().split())
    cities[home].append(away)
    cities[away].append(home)

print(cities)

visited = [False] * (N+1)

distance = 0
can_go = [[] for _ in range(N+1)]

# DFS를 기반으로 거리 체킹을 어떻게 하는가?

# for city in cities:
# for i in range(1, N+1):
#     visited[i] = True

#     for city in cities[i]:
#         if not visited[city]:
#             visited[city] = True


def make_distance(cities, x, visited, distance):
    if not visited[x]:
        visited[x] = True
    print(x)

    for i in cities[x]:
        if not visited[i]:
            visited[i] = True

    # if distance == K:
    #     # can_go.append(x)
    #     # can_go[K].append(x)
    #     print("거리별 목적지 모음: ", can_go)
    #     return can_go[K]
    # else:
    #     distance += 1
    #     for i in cities[x]:
    #         if not visited[i]:
    #             can_go[distance].append(i)
    #             print("거리별 목적지 모음: ", can_go)
    #             # make_distance(cities, i, visited, distance)

    # return can_go

print(make_distance(cities, X, visited, distance))

# print(can_go)