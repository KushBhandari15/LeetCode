class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0;
        int start = 0;
        int end = height.size()-1;

        while(start < end){
            int len = min(height[start], height[end]);
            int d = end-start;
            int curr = len*d;
            maxArea = max(maxArea, curr);
            if(height[start] > height[end]){
                end--;
            }
            else{
                start++;
            }
        }

        return maxArea;
    }
};