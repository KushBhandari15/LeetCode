class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zero = 0;
        int count = 0;
        int nonZero = 0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                int start = i+1;
                while(start < nums.size()){
                    if(nums[start]!=0){
                        nums[i] = nums[start];
                        nums[start] = 0;
                        break;
                    }
                    start++;
                }
            }
        }
    }
};