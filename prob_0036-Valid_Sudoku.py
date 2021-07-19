def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    if len(board) != 9:
        return False
    rows     = [set() for i in range(9)]
    columns  = [set() for i in range(9)]
    subgrids = [set() for i in range(9)]
    for i in range(len(board)):
        if len(board[i]) != 9:
            return False
        for j in range(len(board[i])):
            c = board[i][j];
            if c == ".":
                continue
            if not c.isdigit():
                return False
            d = int(c)
            if d < 1 or d > 9:
                return False
            idx_subgrid = i / 3 + 3 * (j / 3)
            if d in rows[i] or d in columns[j] or d in subgrids[idx_subgrid]:
                return False
            rows[i].add(d)
            columns[j].add(d)
            subgrids[idx_subgrid].add(d)
    return True
