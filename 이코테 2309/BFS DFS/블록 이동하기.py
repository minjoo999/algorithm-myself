from collections import deque


def solution(board):
    height = len(board)
    width = len(board[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # dx = [1, 0]
    # dy = [0, 1]

    # '다음 진도'는 오른쪽 또는 아래쪽으로만 진전 가능?

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        print("큐: ", queue)

        cnt = 0

        while queue:

            x, y = queue.popleft()
            print("이번좌표: ", x, y)

            for i in range(4):
                # for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                print("다음좌표: ", nx, ny)

                if nx < 0 or nx >= width or ny < 0 or ny >= height:
                    continue

                if board[nx][ny] == 1:
                    continue

                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
                    break
                    # continue

                print("큐: ", queue)
                print("시간: ", cnt)

        return cnt

    answer = bfs(0, 1)

    return answer


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
      0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
