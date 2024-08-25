class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        vector<int> res;
        int rows = mat.size();
        int cols = mat[0].size();

        int curr_row = 0, curr_col = 0;
        bool direction_up = true;

        while(res.size() != rows*cols){

            if(direction_up){
                while(curr_row >= 0 && curr_col < cols){
                    res.push_back(mat[curr_row][curr_col]);

                    curr_row -= 1;
                    curr_col += 1;
                }

                if(curr_col == cols){
                    curr_col -= 1;
                    curr_row += 2;
                }
                else{
                    curr_row += 1;
                }
                direction_up = false;
            }

            else{
                while(curr_row < rows && curr_col >= 0){
                    res.push_back(mat[curr_row][curr_col]);

                    curr_row += 1;
                    curr_col -= 1;
                }

                if(curr_row == rows){
                    curr_col += 2;
                    curr_row -= 1;
                }
                else{
                    curr_col += 1;
                }
                direction_up = true;
            }
        }

        return res;
    }
};