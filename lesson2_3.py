def generateMatrix(n: int):
    dp = [[0] * n for i in range(n)]
    print(dp)
    count = 1
    i = 0
    j = -1
    direction = 0
    while count <= n * n:
        u, v = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}[direction]
        while i + u < n and i + u >= 0 and j + v < n and j + v >= 0 and dp[i + u][j + v] == 0:
            i += u
            j += v
            dp[i][j] = count
            count += 1
        direction = (direction + 1) % 4
    return dp

print(generateMatrix(4))
