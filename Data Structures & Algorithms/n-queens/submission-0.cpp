class Solution {
private:
    bool is_valid(int n, int row, int column, vector<string>& curr) {
        int i = 0, j = 0;

        // check if have the same column
        for (i=0; i<row; i++) {
            if (curr[i][column] == 'Q') return false;
        }

        // check left-up diagonal
        i = row - 1;
        j = column - 1;
        while (i>=0 && j>=0) {
            if (curr[i][j] == 'Q') return false;
            i--; j--;
        }

        // check right-up diagonal
        i = row - 1;
        j = column + 1;
        while (i>=0 && j<n) {
            if (curr[i][j] == 'Q') return false;
            i--; j++;
        }
        return true;
    }
    void backtrack(int n, int row,
        vector<string>& curr, vector<vector<string>>& ret) {
        if (row == n) {
            ret.push_back(curr);
            return;
        }
        for (int column=0; column<n; column++) {
            if (!is_valid(n, row, column, curr)) continue;
            string val = "";
            for (int i=0; i<column; i++) val += ".";
            val += "Q";
            for (int i=column+1; i<n; i++) val += ".";
            curr.push_back(val);
            backtrack(n, row+1, curr, ret);
            curr.pop_back();
        }

    }
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ret;
        vector<string> curr;
        curr.clear();
        ret.clear();
        backtrack(n, 0, curr, ret);
        return ret;
    }
};
