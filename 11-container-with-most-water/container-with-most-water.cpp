class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int length = 0, breadth = 0;
        int res = 0;
        while (left < right){
            length = min(height[left],height[right]);
            breadth = right - left;
            cout<<length<<" "<<breadth<<endl;
            int curr = length*breadth;
            res = max(res, curr);
            if(height[left] > height[right]){
                right--;
            }
            else{
                left++;
            }
        }
        return res;
    }
};