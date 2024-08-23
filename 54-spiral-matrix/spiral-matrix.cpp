class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int x = 0;
        int y = 0;
        int dx = 0;
        int dy = 1;
        vector<int> res;

        for(int i = 0; i<rows * cols; i++){
            res.push_back(matrix[x][y]);
            matrix[x][y] = -101;
            if(!(x+dx >= 0 && x+dx < rows && y+dy >= 0 && y+dy < cols) || matrix[x+dx][y+dy]==-101){
                int temp = dy;
                dy = -dx;
                dx = temp;
            }

            x += dx;
            y += dy;
        }

        return res;
    }
};