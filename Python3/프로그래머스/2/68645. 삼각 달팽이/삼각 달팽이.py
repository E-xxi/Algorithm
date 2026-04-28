def solution(n):
    tri = [[0] * i for i in range(1, n + 1)]

    dx = [1, 0, -1]   # 아래, 오른쪽, 위-왼쪽
    dy = [0, 1, -1]

    x, y = 0, 0
    num = 1
    direction = 0

    total = n * (n + 1) // 2

    for _ in range(total):
        tri[x][y] = num
        num += 1

        nx = x + dx[direction]
        ny = y + dy[direction]

        if (
            nx < 0 or nx >= n or
            ny < 0 or ny >= len(tri[nx]) or
            tri[nx][ny] != 0
        ):
            direction = (direction + 1) % 3
            nx = x + dx[direction]
            ny = y + dy[direction]

        x, y = nx, ny

    answer = []
    for row in tri:
        answer.extend(row)

    return answer