class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int rows[9] = {0};
        int colums[9] = {0};
        int squares[9] = {0};
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                if (board[i][j] == '.') continue;
                int target = 1<<(board[i][j]-'1');
                if (rows[i] & target) return false;
                rows[i] |= target;
                if (colums[j] & target) return false;
                colums[j] |= target;
                if (squares[(i/3)*3+j/3] & target) return false;
                squares[(i/3)*3+j/3] |= target;
            }
        }
        return true;
    }
};
