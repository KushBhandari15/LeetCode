class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int res = 0;

        for(auto i:nums){
            if(numSet.find(i-1)==numSet.end()){
                int length = 1;
                while(numSet.find(i+length)!=numSet.end()){
                    length++;
                }
                res = max(res, length);
            }
        }

        return res;

    }
};