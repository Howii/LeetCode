from typing import List

def diagonalSum(self, mat: List[List[int]]) -> int:
    N = len(mat)
    res = 0
    for i in range(N):
        res += mat[i][i]
        res += mat[i][N-1-i]
    if N % 2 == 1:
        mid = N // 2
        res -= mat[mid][mid]
    return res
