class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i=0;i<nums.size();i++){
            int start = i;
            int end = nums.size()-1;
            while(start < end){
                if(nums[start]+nums[end]==target){
                    return {start, end};
                }
                end--;
            }
        }
        return {};
    }
};