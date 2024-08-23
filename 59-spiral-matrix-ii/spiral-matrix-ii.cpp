class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        
        vector<vector<int>> res(n, vector<int>(n, 0));
        int x = 0;
        int y = 0;
        int dx = 0;
        int dy = 1;

        for(int i=0;i<n*n;i++){
            res[x][y] = i+1;
            if(!(x+dx >= 0 && x+dx < n && y+dy >= 0 && y+dy < n && res[x+dx][y+dy]==0)){
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