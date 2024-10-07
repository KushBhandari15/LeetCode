class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long int start = 0;
        long int maxSum = 0;
        long int state = 0;
        unordered_map<long int,long int> map;

        for(int end=0; end<nums.size();end++){
            state += nums[end];
            map[nums[end]]++;

            if(end-start+1 == k){
                if(map.size()==k){
                    maxSum = max(maxSum, state);
                }
                state -= nums[start];
                map[nums[start]]--;
                if(map[nums[start]]==0){
                    map.erase(nums[start]);
                }
                start++;
            }
        }
        return maxSum;

    }
};