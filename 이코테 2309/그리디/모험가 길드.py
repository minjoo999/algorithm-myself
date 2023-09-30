import sys

input = sys.stdin.readline

N = int(input())
traveler = list(map(int, input().split()))

traveler.sort()

print(traveler)

group = []
cnt = 0
for t in traveler:
    if len(group) + 1 < t:
        group.append(t)
    elif len(group) + 1 == t:
        group.append(t)
        cnt += 1
        group.clear()

print(cnt)
