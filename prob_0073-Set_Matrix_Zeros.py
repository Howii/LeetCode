def setZeroes(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    M, N = len(matrix), len(matrix[0])
    zero_rows = set()
    zero_cols = set()
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    for i in zero_rows:
        for j in range(N):
            matrix[i][j] = 0
    for j in zero_cols:
        for i in range(M):
            matrix[i][j] = 0
