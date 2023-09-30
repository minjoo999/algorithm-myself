N = int(input())

# 시, 분, 초를 셋팅하는 법?
# '000000' ~ 'N5959'

cnt = 0

hour = 0

# 별개 변수를 시분초 할당하는 방식이 오히려 부정확한 결과를 낼 수 있음.
while hour <= N:
    minute = 0

    for i in range(59):
        minute += 1
        second = 0
        for j in range(59):
            second += 1

            now = str(hour) + str(minute) + str(second)

            for n in now:
                if int(n) == 3:
                    cnt += 1
                    break

    print(f"지금 {hour}시대: 숫자 3은 {cnt}회 등장")

    hour += 1

print(cnt)
