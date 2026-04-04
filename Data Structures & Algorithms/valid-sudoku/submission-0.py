class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9x9
        row_visited = [set() for _ in range(9)]
        col_visited = [set() for _ in range(9)]
        block_visited = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                if board[i][j] in row_visited[i]: return False
                row_visited[i].add(board[i][j])
                if board[i][j] in col_visited[j]: return False
                col_visited[j].add(board[i][j])
                block_id = i//3*3 + j//3
                if board[i][j] in block_visited[block_id]: return False
                block_visited[block_id].add(board[i][j])
        
        return True