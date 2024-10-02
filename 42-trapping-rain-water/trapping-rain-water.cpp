class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size()-1;
        int maxRight = height[right], maxLeft = height[left]; 
        int count = 0;
        while(left < right){
            if(maxRight < maxLeft){
                right--;
                int temp = maxRight - height[right];
                if(temp > 0){
                    count += temp;
                }
                maxRight = max(maxRight, height[right]);
            }
            else{
                left++;
                int temp = maxLeft - height[left];
                if(temp > 0){
                    count += temp;
                }
                maxLeft = max(maxLeft, height[left]);
            }
        }

        return count;
    }
};