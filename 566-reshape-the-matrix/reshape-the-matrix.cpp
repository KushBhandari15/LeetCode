class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int org_row = mat.size();
        int org_col = mat[0].size();
        if(org_row*org_col != r*c){
            return mat;
        }
        vector<vector<int>> res(r, vector<int>(c, 0));
        int curr_row = 0, curr_col = 0;
        int res_row = 0, res_col = 0;
        while(true){
            if(res_col == c){
                res_col = 0;
                res_row += 1;
            }
            if(curr_col == org_col){
                curr_col = 0;
                curr_row += 1;
            }
            if(curr_row == org_row || res_col == c){
                break;
            }

            res[res_row][res_col] = mat[curr_row][curr_col];
            res_col += 1;
            curr_col += 1;
        }

        return res;
    }
};