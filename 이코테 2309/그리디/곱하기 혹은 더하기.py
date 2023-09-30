import sys

input = sys.stdin.readline

S = input().strip()
print(S)

result = int(S[0])
for i in range(1, len(S)):
    print(S[i])

    if int(S[i]) == 0 or int(S[i]) == 1 or result == 0:
        result += int(S[i])
    else:
        result *= int(S[i])

    print("현재 결과: ", result)

print(result)
