def updateMatrix(mat):
    M, N = len(mat), len(mat[0])
    ret = [ [ None ] * N for _ in range(M) ]

    # Breadth-first search appraoch
    cur_boundary = []
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0:
                ret[i][j] = 0
                cur_boundary.append((i, j))

    distance = 1
    while cur_boundary:
        new_boundary = []
        for i, j in cur_boundary:
            if i < M - 1 and ret[i + 1][j] is None:
                ret[i + 1][j] = distance
                new_boundary.append((i + 1, j))
            if i > 0 and ret[i - 1][j] is None:
                ret[i - 1][j] = distance
                new_boundary.append((i - 1, j))
            if j < N - 1 and ret[i][j + 1] is None:
                ret[i][j + 1] = distance
                new_boundary.append((i, j  + 1))
            if j > 0 and ret[i][j - 1] is None:
                ret[i][j - 1] = distance
                new_boundary.append((i, j - 1))
        cur_boundary = new_boundary
        distance += 1
 
    return ret
    
### Test
def printMatrix(mat):
    print("-" * 9)
    for row in mat:
        print(row)

mat = [ [0,0,0,1],
        [1,1,0,0],
        [1,1,1,1],
        [1,1,1,0] ]

printMatrix(mat)

ret = updateMatrix(mat)

printMatrix(ret)
