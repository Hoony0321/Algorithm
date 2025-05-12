from collections import defaultdict

MOD = 10 ** 9 + 7

def solution(grid, d, k):
    n, m = len(grid), len(grid[0])
    size = n * m
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 좌표를 인덱스로 변환
    def pos_to_idx(y, x):
        return y * m + x

    # 경사 수열 한 번에 대한 경로 계산
    dp = [defaultdict(int) for _ in range(len(d) + 1)]
    for y in range(n):
        for x in range(m):
            idx = pos_to_idx(y, x)
            dp[0][(idx, idx)] = 1

    for depth in range(len(d)):
        for (start, end), count in dp[depth].items():
            ey, ex = divmod(end, m)
            for dy, dx in directions:
                ny, nx = ey + dy, ex + dx
                if 0 <= ny < n and 0 <= nx < m:
                    if grid[ny][nx] - grid[ey][ex] == d[depth]:
                        new_end = pos_to_idx(ny, nx)
                        dp[depth + 1][(start, new_end)] = (dp[depth + 1][(start, new_end)] + count) % MOD

    # 행렬 표현
    mat = [[0] * size for _ in range(size)]
    for (start, end), count in dp[len(d)].items():
        mat[start][end] = count

    # 행렬 곱셈
    def mat_mult(a, b):
        result = [[0] * size for _ in range(size)]
        for i in range(size):
            for k in range(size):
                if a[i][k]:
                    for j in range(size):
                        result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % MOD
        return result

    # 행렬 거듭제곱
    def mat_pow(matrix, power):
        result = [[int(i == j) for j in range(size)] for i in range(size)]
        while power:
            if power % 2:
                result = mat_mult(result, matrix)
            matrix = mat_mult(matrix, matrix)
            power //= 2
        return result

    # k번 반복에 대한 행렬 계산
    mat_k = mat_pow(mat, k)

    # 전체 경로 수 계산
    answer = sum(sum(row) for row in mat_k) % MOD
    return answer