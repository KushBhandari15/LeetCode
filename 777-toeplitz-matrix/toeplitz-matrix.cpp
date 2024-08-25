class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();

        for(int i=0; i<col-1; i++){
            int compare = matrix[0][i];
            int curr_col = i, curr_row = 0;
            while(curr_row < row && curr_col < col){
                if(matrix[curr_row][curr_col] != compare){
                    return false;
                }
                curr_row += 1;
                curr_col += 1;
            }
        }
        for(int i=1; i<row-1; i++){
            int compare = matrix[i][0];
            int curr_col = 0, curr_row = i;
            while(curr_row < row && curr_col < col){
                if(matrix[curr_row][curr_col] != compare){
                    return false;
                }
                curr_row += 1;
                curr_col += 1;
            }
        }

        return true;
    }
};