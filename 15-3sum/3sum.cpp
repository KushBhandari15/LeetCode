class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-1;i++){
            if(i!=0 && nums[i]==nums[i-1]){
                continue;
            }
            int start = i+1;
            int end = nums.size()-1;
            while (start < end){
                int curr = nums[start] + nums[end] + nums[i];
                if(curr>0){
                    end--;
                }
                else if(curr<0){
                    start++;
                }
                else{
                    res.push_back({nums[i],nums[start],nums[end]});
                    while(start < end && nums[end]==nums[end-1]){
                        end--;
                    }
                    while(start < end && nums[start]==nums[start+1]){
                        start++;
                    }
                    start++;
                    end--;
                }
            }
        }
        return res;
    }
};