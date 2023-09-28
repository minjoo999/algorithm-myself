from collections import deque

# 이동 가능한 위치들을 반환하는 함수
# 지금 위치 pos 좌표와, 로봇이 다녀야 하는 맵인 board를 재료로 삼아 다음 갈 곳 next_pos를 뽑는 함수
def get_next_pos(pos, board):
    next_pos = []   # 반환 결과 (이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환 (집합 set -> 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 상하좌우 이동 (미로탈출과 유사하게 조형, BFS 특성 반영)
    # 칸 2개를 한꺼번에 이동시킴. 같은 방향으로 2개를 한번에 한칸씩 옮김. 통째로 들어다 옮기는 것 같음.
    # 위로 2개, 아래로 2개 이런 식으로
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]

        # 이동하고자 하는 두 칸이 모두 비어 있다면 next_pos에 집어넣기
        # 좌표 2개를 통째로 들어서 갖다 옮기는 식
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    # 현재 로봇이 가로로 놓여 있는 경우 (같은 행에 놓여 있다고 좌표가 찍힘)
    # 로봇을 그대로 위나 아래로 옮길 때, 로봇이 놓이려는 두 칸이 모두 0이라면 next_pos에 둘 다 집어넣기
    # 집합 중에서 두번째 좌표만 x가 바뀌어 있음. pos1의 x값만 바뀐 버전과 pos2의 x값만 바뀐 버전을 모두 넣기.
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})

    # (반대로) 현재 로봇이 세로로 놓여 있는 경우 (같은 열에 놓여 있다고 좌표가 찍힘)
    # 로봇을 그대로 좌나 우로 옮길 때, 로봇이 놓이려는 두 칸이 모두 0이라면 next_pos에 둘 다 집어넣기
    # 집합 중에서 두번째 좌표만 y가 바뀌어 있음. pos1의 y값만 바뀐 버전과 pos2의 y값만 바뀐 버전을 모두 넣기.
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    return next_pos

def solution(board):

    n = len(board)
    
    # 벽으로 네모를 둘러싼 뒤, 모든 빈칸을 1로 채우기
    # 벽을 쳐준다 이런 식이면 첫 번째 좌표를 (1, 1)로 만들 수 있음
    # 아래 new_board는 [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]] 이렇게 나옴
    new_board = [[1] * (n + 2) for _ in range(n + 2)]

    # new_board의 원래 주어진 값들 중 좌표에 따라 board 값 바꿔 넣기
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []    # 방문여부 표시하기
    pos = {(1, 1), (1, 2)}  # 로봇이 처음 놓인 곳 좌표
    q.append((pos, 0)) # 일단 초기값 pos와 지금까지 든 시간 0을 큐에 넣기

    while q:

        # pos, 그니까 지금 로봇이 놓인 곳과 지금까지 든 시간을 같이 큐에 넣고, 큐에서 좌표를 하나씩 뽑아씀
        pos, cost = q.popleft()

        # 목적지 도착했으면 cost (값) 을 반환
        if (n, n) in pos:
            return cost
        
        # get_next_pos로 반환받은 후보값들을 갖고 반복문 돌리기
        # 후보값 반환을 위해서는 지금 로봇의 위치 pos와, 좌표판 new_board를 모두 넣어야 함
        for next_pos in get_next_pos(pos, new_board):
            print("후보: ", next_pos)

            # next_pos가 방문 안한 값이면 큐에 넣고, 방문처리 하기
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

        print("방문완료: ", visited)

    return 0

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))