class Solution(object):
    DIGIT_SET = {str(x) for x in range(1, 10)}
    DOT = "."
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        subs = [set() for i in range(9)]
        dots = []
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == self.DOT:
                    dots.append((i, j))
                else:
                    idx_sub = i // 3 + 3 * (j // 3)
                    rows[i].add(c)
                    cols[j].add(c)
                    subs[idx_sub].add(c)
        dots.reverse()
        if not self.solveHelper(board, rows, cols, subs, dots):
            raise "No Solution Found"
            
    def solveHelper(self, board, rows, cols, subs, dots):
        if not dots:
            return True
        pos = dots.pop()
        i = pos[0]
        j = pos[1]
        idx_sub = i // 3 + 3 * (j // 3)
        candidates = self.DIGIT_SET - (rows[i] | cols[j] | subs[idx_sub])
        for c in candidates:
            board[i][j] = c
            rows[i].add(c)
            cols[j].add(c)
            subs[idx_sub].add(c)
            if self.solveHelper(board, rows, cols, subs, dots):
                return True
            else:
                board[i][j] = self.DOT
                rows[i].remove(c)
                cols[j].remove(c)
                subs[idx_sub].remove(c)
        dots.append(pos)
        return False
