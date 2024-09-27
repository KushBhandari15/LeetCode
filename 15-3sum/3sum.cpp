class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> res;
        for(int i=0;i<nums.size()-1;i++){
            if(i!=0 && nums[i]==nums[i-1]){
                continue;
            }
            int left = i+1;
            int right = nums.size()-1;
            while(left < right){
                int currSum = nums[i]+nums[left]+nums[right];
                if(currSum > 0){
                    right--;
                }
                else if(currSum < 0){
                    left++;
                }
                else{
                    res.push_back({nums[i],nums[left],nums[right]});
                    while(left<right && nums[right]==nums[right-1]){
                        right--;
                    }
                    while(left<right && nums[left]==nums[left+1]){
                        left++;
                    }
                    left++;
                    right--;
                }
            }
        }

        return res;
    }
};