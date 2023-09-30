N = int(input())
plan = input().split()

print(plan)

# (1, 1)에서 (N, N)으로 이동해야 함
# x가 가로축, y가 세로축 -> 답은 (y, x) 형태여야 함
x = 0
y = 0

for p in plan:
    if p == 'L':
        if x > 0:
            x -= 1
    elif p == 'R':
        if x < N - 1:
            x += 1

    elif p == 'U':
        if y > 0:
            y -= 1

    elif p == 'D':
        if y < N - 1:
            y += 1

print(y + 1, x + 1)
