class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def search(i, j, k, visited):
            if board[i][j] != word[k]: return False
            if k == len(word)-1: return True
            for di, dj in dirs:
                newi, newj = i+di, j+dj
                if newi<0 or newi>=m: continue
                if newj<0 or newj>=n: continue
                if (newi, newj) in visited: continue
                visited.add((newi, newj))
                if search(newi, newj, k+1, visited):
                    return True
                visited.remove((newi, newj))
            return False

        for i in range(m):
            for j in range(n):
                if search(i, j, 0, set([(i, j)])):
                    return True
        return False