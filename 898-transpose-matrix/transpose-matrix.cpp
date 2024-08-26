class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        if(row==col){
            for(int i=0;i<row;i++){
                for(int j=0; j<=i; j++){
                    swap(matrix[i][j], matrix[j][i]);
                }
            }

            return matrix;
        }
        else{
            vector<vector<int>> res(col, vector<int>(row, 0));
            for(int i=0;i<row;i++){
                for(int j=0;j<col;j++){
                    res[j][i] = matrix[i][j];
                }
            }
            return res;
        }
    }
};